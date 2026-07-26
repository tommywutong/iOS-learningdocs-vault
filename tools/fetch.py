#!/usr/bin/env python3
"""抓取 Apple 现行开发者文档（developer.apple.com/documentation）的 DocC render JSON。

三个阶段，各自可独立重跑、断点续跑：

    python3 tools/fetch.py archives                 # 阶段 0：技术清单 → meta/archives.json
    python3 tools/fetch.py index  <archive>...      # 阶段 1：导航树   → meta/manifest/<archive>.json
    python3 tools/fetch.py pages  <archive>...      # 阶段 2：逐页 JSON → .cache/pages/<archive>/**.json

原始 JSON 一律落在 .cache/（已 gitignore），渲染成 Markdown 是另一个阶段的事。
抓取阶段唯一的瓶颈是 Apple 侧限速，所以这里用固定并发 + 指数退避，不追求更高并行。
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import re
import sys
import time
import urllib.parse
from pathlib import Path

import httpx

from paths import cache_rel

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache"
META = ROOT / "meta"

BASE = "https://developer.apple.com"
TECHNOLOGIES = f"{BASE}/tutorials/data/documentation/technologies.json"
INDEX = f"{BASE}/tutorials/data/index"
PAGE = f"{BASE}/tutorials/data/documentation"

CONCURRENCY = 12
MAX_RETRY = 4
# pool 超时是关键：httpx 默认等连接池永久等待，一旦有请求没正常释放连接，
# 后续请求会无限期挂起——表现就是进程活着、CPU 0%、一页都不再落盘。
# 实测踩过一次：swift archive 抓到 712/19216 后整整停滞 15 分钟。
TIMEOUT = httpx.Timeout(20.0, connect=10.0, read=20.0, write=20.0, pool=15.0)
# 单个请求的硬上限。就算 httpx 内部卡住，这一层也会把它掐掉。
HARD_TIMEOUT = 45.0
HEADERS = {
    # 表明身份，便于 Apple 侧在需要时识别流量来源。
    "User-Agent": "apple-developer-docs-vault/0.1 (personal documentation mirror; +https://github.com/XiyouMobile3G-iOS)",
    "Accept": "application/json",
}

# 索引里这些节点不是页面，只是分组标题
NON_PAGE_TYPES = {"groupMarker"}

# “成篇文章”——真正有正文、值得翻译的类型
LONGFORM_TYPES = {"article", "overview", "collection", "sampleCode", "tutorial", "project", "module"}


# ---------------------------------------------------------------- 基础设施


class Fetcher:
    """并发受限、带指数退避的 JSON 抓取器。"""

    def __init__(self, concurrency: int = CONCURRENCY) -> None:
        self.sem = asyncio.Semaphore(concurrency)
        self.client: httpx.AsyncClient | None = None
        self.stats = {"ok": 0, "miss": 0, "fail": 0, "skip": 0, "bytes": 0}

    async def __aenter__(self) -> "Fetcher":
        self.client = httpx.AsyncClient(
            timeout=TIMEOUT, headers=HEADERS, follow_redirects=True, http2=False
        )
        return self

    async def __aexit__(self, *exc) -> None:
        assert self.client is not None
        await self.client.aclose()

    async def get_json(self, url: str) -> dict | None:
        """取一个 JSON。404 返回 None（Apple 有不少索引里存在但无独立页面的节点）。"""
        assert self.client is not None
        delay = 1.0
        for attempt in range(MAX_RETRY):
            async with self.sem:
                try:
                    # 双层超时：httpx 自己的 + asyncio 的硬上限
                    r = await asyncio.wait_for(self.client.get(url), timeout=HARD_TIMEOUT)
                except (httpx.TimeoutException, httpx.TransportError, asyncio.TimeoutError) as e:
                    if attempt == MAX_RETRY - 1:
                        print(f"  [网络失败] {url} :: {e}", file=sys.stderr)
                        self.stats["fail"] += 1
                        return None
                else:
                    if r.status_code == 200:
                        self.stats["ok"] += 1
                        self.stats["bytes"] += len(r.content)
                        try:
                            return r.json()
                        except ValueError:
                            print(f"  [非 JSON] {url}", file=sys.stderr)
                            self.stats["fail"] += 1
                            return None
                    if r.status_code in (404, 410):
                        self.stats["miss"] += 1
                        return None
                    if r.status_code not in (429, 500, 502, 503, 504):
                        print(f"  [HTTP {r.status_code}] {url}", file=sys.stderr)
                        self.stats["fail"] += 1
                        return None
                    # 429/5xx 才重试
            await asyncio.sleep(delay)
            delay *= 2
        self.stats["fail"] += 1
        return None


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(path)


def cache_path(archive: str, doc_path: str) -> Path:
    """/documentation/uikit/uiview → .cache/pages/uikit/uiview.json

    命名规则见 paths.cache_rel：百分号编码保证可逆，超长组件截断拼哈希
    （Apple 有方法签名编码后超过 400 字节，直接落盘会 OSError）。
    """
    return CACHE / "pages" / cache_rel(archive, doc_path)


# ---------------------------------------------------------------- 阶段 0


async def stage_archives() -> None:
    """拉全量技术清单，落 meta/archives.json。

    注意：索引端点是按 DocC archive 返回的，不是按框架。多个框架可能共用一个
    archive（如 Observation 属于 swift），也有框架没有独立 archive（如
    swift_concurrency / coreanimation → 404）。这里只记录候选，实际归并在阶段 1
    用 index 的内容哈希判定。
    """
    async with Fetcher() as f:
        data = await f.get_json(TECHNOLOGIES)
    if not data:
        sys.exit("technologies.json 抓取失败")

    techs = {}
    for ref in data.get("references", {}).values():
        url = ref.get("url", "")
        if re.fullmatch(r"/documentation/[^/]+", url):
            slug = url.rsplit("/", 1)[-1]
            techs[slug] = {
                "slug": slug,
                "title": ref.get("title", slug),
                "url": url,
                "abstract": plain_text(ref.get("abstract", [])),
            }

    write_json(META / "archives.json", {"count": len(techs), "technologies": techs})
    print(f"阶段 0 完成：{len(techs)} 个技术 → meta/archives.json")


def plain_text(inline: list) -> str:
    """把 DocC 的 inline content 数组压成纯文本（只用于摘要/日志）。"""
    out = []
    for node in inline or []:
        t = node.get("type")
        if t == "text":
            out.append(node.get("text", ""))
        elif t in ("codeVoice", "inlineHead"):
            out.append(node.get("code") or plain_text(node.get("inlineContent", [])))
        elif "inlineContent" in node:
            out.append(plain_text(node["inlineContent"]))
    return "".join(out).strip()


# ---------------------------------------------------------------- 阶段 1


def walk_index(nodes: list, parent: str = "") -> list[dict]:
    """把 DocC 索引树拍平成页面清单，保留层级路径用于后续生成索引与面包屑。"""
    flat = []
    for node in nodes or []:
        ntype = node.get("type", "?")
        title = node.get("title", "")
        path = node.get("path")
        crumb = f"{parent}/{title}" if parent else title
        if ntype not in NON_PAGE_TYPES and path:
            flat.append(
                {
                    "path": path,
                    "title": title,
                    "type": ntype,
                    "breadcrumb": crumb,
                    "longform": ntype in LONGFORM_TYPES,
                    "deprecated": bool(node.get("deprecated")),
                    "beta": bool(node.get("beta")),
                }
            )
        # groupMarker 自己不是页面，但它的 children 仍要继续走；层级名沿用父级
        flat.extend(walk_index(node.get("children", []), crumb if path else parent))
    return flat


async def stage_index(archives: list[str]) -> None:
    async with Fetcher() as f:
        results = await asyncio.gather(*(f.get_json(f"{INDEX}/{a}") for a in archives))

    seen: dict[str, str] = {}
    for archive, data in zip(archives, results):
        if not data or "interfaceLanguages" not in data:
            print(f"  {archive:26} 无独立 archive（404 或空），跳过")
            continue

        # 用 includedArchiveIdentifiers + 树内容判断是否与已处理的 archive 重复
        fingerprint = hashlib.sha256(
            json.dumps(data.get("interfaceLanguages", {}), sort_keys=True).encode()
        ).hexdigest()
        if fingerprint in seen:
            print(f"  {archive:26} 与 {seen[fingerprint]} 是同一 archive，跳过")
            continue
        seen[fingerprint] = archive

        langs = data["interfaceLanguages"]
        # Swift 视角为主；Objective-C 独有的页面补进来（如纯 ObjC 的老 API）
        pages: dict[str, dict] = {}
        for lang in ("swift", "occ"):
            for p in walk_index(langs.get(lang, [])):
                p.setdefault("langs", [])
                if p["path"] in pages:
                    pages[p["path"]]["langs"].append(lang)
                else:
                    p["langs"] = [lang]
                    pages[p["path"]] = p

        manifest = {
            "archive": archive,
            "included": data.get("includedArchiveIdentifiers", []),
            "page_count": len(pages),
            "longform_count": sum(1 for p in pages.values() if p["longform"]),
            "pages": list(pages.values()),
        }
        write_json(META / "manifest" / f"{archive}.json", manifest)
        print(
            f"  {archive:26} {manifest['page_count']:>7} 页"
            f"（成篇文章 {manifest['longform_count']}）"
        )
    print("阶段 1 完成 → meta/manifest/")


# ---------------------------------------------------------------- 阶段 2


async def stage_pages(archives: list[str], only_longform: bool = False) -> None:
    for archive in archives:
        mf = META / "manifest" / f"{archive}.json"
        if not mf.exists():
            print(f"  {archive}: 缺 manifest，先跑 index 阶段", file=sys.stderr)
            continue
        manifest = json.loads(mf.read_text(encoding="utf-8"))
        pages = manifest["pages"]
        if only_longform:
            pages = [p for p in pages if p["longform"]]

        todo = [p for p in pages if not cache_path(archive, p["path"]).exists()]
        print(
            f"\n{archive}: 共 {len(pages)} 页"
            f"{'（仅成篇文章）' if only_longform else ''}"
            f"，已缓存 {len(pages) - len(todo)}，待抓 {len(todo)}"
        )
        if not todo:
            continue

        t0 = time.monotonic()
        done = 0
        async with Fetcher() as f:

            async def one(page: dict) -> None:
                nonlocal done
                # 单页失败不能拖垮整批：这一批动辄几万页，跑了一小时被一个
                # 边缘 case 掀翻不值得。异常记下来，继续跑。
                try:
                    enc = urllib.parse.quote(page["path"].removeprefix("/documentation/"))
                    data = await f.get_json(f"{PAGE}/{enc}.json")
                    if data is not None:
                        write_json(cache_path(archive, page["path"]), data)
                except Exception as e:
                    f.stats["fail"] += 1
                    print(f"  [跳过] {page['path']} :: {type(e).__name__}: {e}", file=sys.stderr)
                done += 1
                if done % 500 == 0:
                    el = time.monotonic() - t0
                    print(
                        f"    {done}/{len(todo)}  {done / el:.1f} 页/秒  "
                        f"ok={f.stats['ok']} 404={f.stats['miss']} 失败={f.stats['fail']}"
                    )

            await asyncio.gather(*(one(p) for p in todo))
            el = time.monotonic() - t0
            print(
                f"  {archive} 完成：{done} 页，{el:.0f} 秒，"
                f"ok={f.stats['ok']} 404={f.stats['miss']} 失败={f.stats['fail']}，"
                f"{f.stats['bytes'] / 1e6:.1f} MB"
            )


# ---------------------------------------------------------------- 入口


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, rest = sys.argv[1], sys.argv[2:]
    only_longform = "--only-longform" in rest
    rest = [a for a in rest if not a.startswith("--")]

    if cmd == "archives":
        asyncio.run(stage_archives())
    elif cmd == "index":
        asyncio.run(stage_index(rest))
    elif cmd == "pages":
        asyncio.run(stage_pages(rest, only_longform))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
