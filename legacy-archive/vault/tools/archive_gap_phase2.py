#!/usr/bin/env python3
"""恢复第一轮抓取跳过的 Apple Developer Archive 记录。

来源优先级：

1. Apple 仍可直接返回的原始 Archive HTML/PDF；
2. Internet Archive 中接近 2019 年末的历史快照；
3. 无法验证为历史原文的条目保持 unresolved，不拿现行 DocC 页面冒充。

运行：

    python3 tools/archive_gap_phase2.py recover
    python3 tools/archive_gap_phase2.py render
    python3 tools/archive_gap_phase2.py report
    python3 tools/archive_gap_phase2.py all

所有网络缓存和中间产物都在 ``.staging/``。只有 ``install``/``all`` 会把已经
机械校验通过的产物复制进仓库；提交前仍需人工抽查来源清单。
"""
from __future__ import annotations

import argparse
import concurrent.futures
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
from collections import Counter
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup
from pypdf import PdfReader

import archive_scrape as core


ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "doc" / "ARCHIVE_GAP_PHASE2_INPUT.json"
SOURCE_REPORT = ROOT / "doc" / "ARCHIVE_GAP_PHASE2_SOURCES.json"
ASSET_REPORT = ROOT / "doc" / "ARCHIVE_GAP_PHASE2_ASSETS.json"
STATE = core.STATE
OUT = core.OUT
ARCHIVE_ROOT = core.ARCHIVE_ROOT

# Apple 在 2020 年前后迁移了大量 Archive 页面。先找接近 Archive 最后稳定期的快照，
# 再向前/向后退一档。Wayback 会把目标时间解析到最近的一次实际抓取。
SNAPSHOT_TARGETS = (
    "20191231235959",
    "20181231235959",
    "20201231235959",
)

SNAPSHOT_OVERRIDES = {
    "DTS40010209": "20190805193515",
    # help.apple.com 与 docs.info.apple.com 的有效抓取远早于 Archive 停服期。
    "TP40006825": "20150110164633",
    "TP40008111": "20030325062408",
    "TP40008112": "20080202192502",
    "TP40008113": "20070812061751",
    "TP40012299": "20150328005613",
    "TP40010206": "20180607120500",
    "TP40012262": "20181026174831",
    # QuickTime 用户指南原始记录使用 images.apple.com，实际 PDF 曾迁到 www。
    "TP40004644": "20150218170513",
}

PDF_URL_ALIASES = {
    "TP40004644": "http://www.apple.com/quicktime/pdf/QuickTime7_User_Guide.pdf",
}

HTML_URL_ALIASES = {
    "TP40012299": "http://help.apple.com/iadproducer/mac/5.0/",
}

ALIAS_FIXES = {
    "DTS10002175": ROOT / "qa/snd/Playing Compressed WAVE files via the Sound Manager.md",
    "DTS10001488": ROOT / "qa/ops/What Does Extension Manager Turn Off/Legacy Documentclose button.md",
}

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}
KNOWN_UNAVAILABLE_IMAGE_NAMES = {
    "tn2410_WatchApp_InfoPlist.png",
    "tn2410_WatchApp_BuildSettings.png",
    "tn2410_WathApp_Resources.png",
    "tn2410_WatchExtension_InfoPlst.png",
    "tn2410_WatchExtension_BuildSettings.png",
    "tn2410_WatchExtension_Phases.png",
    "tn2410_device_logs.png",
    "tn2424_Figure_1.png",
    "tn2424_Figure_2.png",
    "tn2424_Figure_3.png",
    "tn2424_Figure_4.png",
    "tn2424_Figure_5.png",
    "tn2424_Figure_6.png",
}


def binary_good(url: str, body: bytes) -> bool:
    """拒绝扩展名伪装成图片/PDF/ZIP 的 404 HTML 或跳转页。"""
    suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if suffix == ".png":
        return body.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in {".jpg", ".jpeg"}:
        return body.startswith(b"\xff\xd8\xff")
    if suffix == ".gif":
        return body.startswith((b"GIF87a", b"GIF89a"))
    if suffix == ".pdf":
        return body.startswith(b"%PDF")
    if suffix == ".zip":
        return body.startswith((b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08"))
    head = body[:512].lstrip().lower()
    return not head.startswith((b"<!doctype html", b"<html"))


def load_docs() -> list[dict]:
    return json.loads(INPUT.read_text(encoding="utf-8"))["documents"]


def load_sources() -> dict[str, dict]:
    if SOURCE_REPORT.exists():
        return json.loads(SOURCE_REPORT.read_text(encoding="utf-8"))["documents"]
    return {}


def save_sources(sources: dict[str, dict]) -> None:
    counts = Counter(v.get("status", "unknown") for v in sources.values())
    payload = {
        "meta": {
            "input_records": len(load_docs()),
            "audited_records": len(sources),
            "status_counts": dict(sorted(counts.items())),
            "source_priority": [
                "Apple original archive",
                "Apple original PDF",
                "Internet Archive historical snapshot",
            ],
            "note": "A live DocC redirect is not accepted as an Archive recovery.",
        },
        "documents": dict(sorted(sources.items())),
    }
    SOURCE_REPORT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def same_historic_target(requested: str, final: str) -> bool:
    """Wayback 重放若落到现行 DocC，则拒绝。"""
    if "/web/" not in final:
        return False
    replay = final.split("id_/", 1)[-1]
    replay = urllib.parse.unquote(replay)
    req = urllib.parse.urlparse(requested)
    got = urllib.parse.urlparse(replay)
    if requested.startswith(ARCHIVE_ROOT):
        return (
            got.hostname == "developer.apple.com"
            and got.path.startswith("/library/archive/")
        )
    # Wayback 常把旧 HTTP URL 规范化成显式的 :80；端口不应导致同源误判。
    return req.hostname == got.hostname


def generic_html_good(status: int, text: str) -> tuple[bool, str]:
    if status != 200:
        return False, f"http{status}"
    head = text[:8000].lower()
    preview = BeautifulSoup(text[:20000], "html.parser")
    title = preview.title.get_text(" ", strip=True).lower() if preview.title else ""
    if "page not found" in head or "not found" in title:
        return False, "notfound-title"
    soup = BeautifulSoup(text, "html.parser")
    body = soup.find("main") or soup.find("body")
    if body is None or len(body.get_text(" ", strip=True)) < 300:
        return False, "empty-body"
    return True, "ok"


class HistoricalFetcher(core.Fetcher):
    """以原 URL 为缓存键，必要时从 Wayback ``id_`` 原始重放端点取内容。"""

    def __init__(self, aid: str, generic: bool = False):
        super().__init__(delay=0.8)
        self.aid = aid
        self.generic = generic
        self.preferred_timestamp: str | None = None

    def _validate(
        self,
        status: int,
        body: bytes,
        binary: bool,
        kind: str,
        original: str,
    ):
        if binary:
            if status != 200 or not body:
                return False, f"http{status}"
            if not binary_good(original, body):
                return False, "invalid-binary-content"
            return True, "ok"
        text = body.decode("utf-8", "replace")
        if kind == "json":
            try:
                json.loads(text)
                return status == 200, "ok" if status == 200 else f"http{status}"
            except Exception:
                return False, "bad-json"
        if self.generic:
            return generic_html_good(status, text)
        return core.page_is_good(status, text)

    def _request(self, acquisition_url: str, binary: bool = False):
        delay = self.delay - (time.time() - self.last)
        if delay > 0:
            time.sleep(delay)
        self.last = time.time()
        self.n_net += 1
        error = ""
        # 主批次单次尝试；失败项由 --retry-unresolved 再跑，避免一个失联 URL
        # 阻塞整批数分钟。
        attempts = 1
        for attempt in range(attempts):
            try:
                response = self.s.get(
                    acquisition_url,
                    timeout=(8, 15 if binary else 20),
                    allow_redirects=True,
                )
                return response, error
            except Exception as exc:
                error = str(exc)[:240]
                if attempt + 1 < attempts:
                    time.sleep(2**attempt)
        return None, error

    def get(self, url: str, binary: bool = False, kind: str = "html"):
        original = url if self.generic else core.canonical_url(url)
        cp = self.cache_path(original)
        info = self.index.get(original)
        invalid_cached_binary = False
        if cp.exists() and info is not None and info.get("ok"):
            data = cp.read_bytes()
            ok, why = self._validate(
                int(info.get("status", 200)),
                data,
                binary,
                kind,
                original,
            )
            if ok:
                return True, data if binary else data.decode("utf-8", "replace"), info
            info = {**info, "ok": False, "why": why}
            self.index[original] = info
            invalid_cached_binary = binary

        attempts: list[tuple[str, str, str | None]] = []
        if not (invalid_cached_binary and self.preferred_timestamp):
            attempts.append(("apple", original, None))
        targets = SNAPSHOT_TARGETS
        if self.preferred_timestamp:
            targets = (self.preferred_timestamp,)
        elif binary:
            targets = SNAPSHOT_TARGETS[:2]
        attempts += [
            (
                "wayback",
                f"https://web.archive.org/web/{timestamp}id_/{original}",
                timestamp,
            )
            for timestamp in targets
        ]
        last_info = {"status": 0, "ok": False, "why": "not-attempted"}
        for mode, acquisition_url, target_timestamp in attempts:
            response, error = self._request(acquisition_url, binary=binary)
            if response is None:
                last_info = {
                    "status": 0,
                    "ok": False,
                    "why": error or "network-error",
                    "source": mode,
                    "acquisition_url": acquisition_url,
                }
                continue

            # 直接请求只接受仍在原 Archive 的 HTML；PDF 可接受 Apple 自有域名跳转。
            if mode == "apple" and not binary:
                if original.startswith(ARCHIVE_ROOT) and not response.url.startswith(ARCHIVE_ROOT):
                    continue
                if not original.startswith(ARCHIVE_ROOT) and response.url != original:
                    continue
            if mode == "wayback" and not same_historic_target(original, response.url):
                continue

            body = response.content
            ok, why = self._validate(
                response.status_code,
                body,
                binary,
                kind,
                original,
            )
            snapshot = None
            match = re.search(r"/web/(\d{8,14})(?:id_)?/", response.url)
            if match:
                snapshot = match.group(1)
            last_info = {
                "status": response.status_code,
                "final": response.url,
                "size": len(body),
                "ctype": response.headers.get("Content-Type", ""),
                "ok": ok,
                "why": why,
                "source": mode,
                "acquisition_url": acquisition_url,
                "snapshot": snapshot,
                "target_timestamp": target_timestamp,
            }
            if not ok:
                continue
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_bytes(body)
            if snapshot:
                self.preferred_timestamp = snapshot
            self.index[original] = last_info
            self.save()
            return ok, body if binary else body.decode("utf-8", "replace"), last_info

        self.index[original] = last_info
        self.save()
        return False, b"" if binary else "", last_info


def fix_alias(d: dict) -> dict:
    path = ALIAS_FIXES[d["apple_id"]]
    text = path.read_text(encoding="utf-8")
    raw, fence, body = text[4:].partition("\n---\n")
    if not fence:
        raise ValueError(f"frontmatter missing: {path}")
    fm = yaml.safe_load(raw)
    fm.update(
        {
            "title": d["name"],
            "apple_id": d["apple_id"],
            "resource_type": core.RESOURCE_TYPE[d["type_name"]],
            "platform": d["platform"],
            "topic": d.get("topic") or None,
            "technology": d.get("framework") or None,
            "published": d.get("published") or "",
            "source_url": d["url"].split("#")[0],
        }
    )
    ordered = {key: fm[key] for key in core.FM_KEYS}
    path.write_text(
        "---\n"
        + yaml.safe_dump(
            ordered,
            sort_keys=False,
            allow_unicode=True,
            width=80,
            default_flow_style=False,
        )
        + "---\n"
        + body,
        encoding="utf-8",
    )
    return {
        "status": "restored-alias-metadata",
        "path": str(path.relative_to(ROOT)),
        "source_url": d["url"].split("#")[0],
        "note": "The body was already present under the neighbouring record's metadata.",
    }


def pdf_destination(d: dict) -> tuple[Path, str]:
    url = d["url"].split("#")[0]
    title = core.sanitize(d["name"])
    if url.startswith(ARCHIVE_ROOT):
        catmap = core.category_map()
        occupancy: dict[str, int] = {}
        for doc in load_docs():
            u = core.canonical_url(doc["url"])
            if u.startswith(ARCHIVE_ROOT):
                segments = u[len(ARCHIVE_ROOT) :].split("/")
                if len(segments) >= 3:
                    key = "/".join(segments[:2])
                    occupancy[key] = occupancy.get(key, 0) + 1
        top, category = core.top_and_category(url, catmap, occupancy)
    else:
        top = "releasenotes" if d["type_name"] == "Release Notes" else "documentation"
        category = None
    base = ROOT / top
    if category:
        base /= category
    doc_dir = base / title
    return doc_dir, f"{title}.md"


def render_pdf(d: dict, fetcher: HistoricalFetcher) -> dict:
    original_url = d["url"].split("#")[0]
    candidates = [original_url]
    if d["apple_id"] in PDF_URL_ALIASES:
        candidates.append(PDF_URL_ALIASES[d["apple_id"]])
    ok = False
    data = b""
    info = {"why": "PDF unavailable"}
    acquisition_url = original_url
    for candidate in candidates:
        acquisition_url = candidate
        ok, data, info = fetcher.get(candidate, binary=True)
        if ok and data.startswith(b"%PDF"):
            break
    if not ok or not data.startswith(b"%PDF"):
        return {
            "status": "unresolved",
            "source_url": original_url,
            "reason": (
                "not-pdf"
                if ok and data and not data.startswith(b"%PDF")
                else info.get("why", "PDF unavailable")
            ),
            "last_attempt": info,
        }
    doc_dir, filename = pdf_destination(d)
    doc_dir.mkdir(parents=True, exist_ok=True)
    attachment = doc_dir / "attachments" / "original.pdf"
    attachment.parent.mkdir(parents=True, exist_ok=True)
    attachment.write_bytes(data)

    pages: list[str] = []
    try:
        reader = PdfReader(io.BytesIO(data))
        for number, page in enumerate(reader.pages, 1):
            content = (page.extract_text() or "").strip()
            if content:
                pages.append(f"## 第 {number} 页\n\n{content}")
    except Exception as exc:
        pages.append(f"> PDF 文本抽取失败：{type(exc).__name__}。请打开原始 PDF 阅读。")

    rel = str((doc_dir / filename).relative_to(ROOT))
    nav = core.nav_line(rel, rel.split("/")[0], d["name"], None)
    link = "[打开 Apple 原始 PDF](attachments/original.pdf)"
    body = f"# {d['name']}\n\n{link}"
    if pages:
        body += "\n\n" + "\n\n".join(pages)
    text = core.frontmatter(d, original_url) + nav + "\n\n\n\n" + body + "\n"
    (doc_dir / filename).write_text(text, encoding="utf-8")
    return {
        "status": "restored-pdf",
        "path": rel,
        "attachment": str(attachment.relative_to(ROOT)),
        "pages": len(pages),
        "source_url": original_url,
        "acquisition_source_url": acquisition_url,
        "acquisition": info,
    }


def generic_destination(d: dict) -> tuple[Path, str]:
    top = "releasenotes" if d["type_name"] == "Release Notes" else "documentation"
    title = core.sanitize(d["name"])
    doc_dir = ROOT / top / title
    return doc_dir, f"{title}.md"


def render_generic_html(
    d: dict,
    fetcher: HistoricalFetcher,
    html: str,
    info: dict,
    base_url: str,
) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("main") or soup.find("article") or soup.find("body")
    if article is None:
        return {
            "status": "unresolved",
            "source_url": d["url"].split("#")[0],
            "reason": "no usable body",
        }
    doc_dir, filename = generic_destination(d)
    doc_dir.mkdir(parents=True, exist_ok=True)
    rel = str((doc_dir / filename).relative_to(ROOT))
    url_map = core.old_vault_map()
    url_map[core.canonical_url(d["url"])] = rel

    # 先保存正文图片，再让共用预处理器把 src 改成 attachments/。
    image_count = 0
    for image in article.find_all("img"):
        src = (image.get("src") or "").split("?")[0]
        if not src or src.startswith("data:"):
            continue
        absolute = urllib.parse.urljoin(base_url, src)
        ok, data, _ = fetcher.get(absolute, binary=True)
        if not ok or not data:
            continue
        sub = re.sub(r"^(\.\./)+", "", src)
        destination = doc_dir / "attachments" / sub
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        image_count += 1

    core.preprocess(article, base_url, url_map, rel, True)
    body = core.to_markdown(article)
    nav = core.nav_line(rel, rel.split("/")[0], d["name"], None)
    text = core.frontmatter(d, d["url"].split("#")[0]) + nav + "\n\n\n\n" + body + "\n"
    (doc_dir / filename).write_text(text, encoding="utf-8")
    return {
        "status": "restored-html",
        "path": rel,
        "images": image_count,
        "source_url": d["url"].split("#")[0],
        "acquisition": info,
        "layout": "generic-offsite",
    }


def prefetch_images(fetcher: HistoricalFetcher, urls: list[str]) -> None:
    for url in urls:
        ok, html, _ = fetcher.get(url)
        if not ok:
            continue
        article = core.article_of(core.soup_of(html))
        if article is None:
            continue
        for image in article.find_all("img"):
            src = (image.get("src") or "").split("?")[0]
            if not src or src.startswith("data:"):
                continue
            absolute = urllib.parse.urljoin(url, src)
            if core.in_archive(absolute) and "/Resources/" not in absolute:
                fetcher.get(absolute, binary=True)


def recover_html(d: dict) -> tuple[dict, dict | None]:
    original = d["url"].split("#")[0]
    generic = not original.startswith(ARCHIVE_ROOT)
    # Archive 内页需要统一 index/_index；旧帮助站和知识库的目录 URL 必须原样保留。
    url = HTML_URL_ALIASES.get(d["apple_id"], original)
    url = url if generic else core.canonical_url(url)
    fetcher = HistoricalFetcher(d["apple_id"], generic=generic)
    fetcher.preferred_timestamp = SNAPSHOT_OVERRIDES.get(d["apple_id"])
    ok, html, info = fetcher.get(url)
    if not ok:
        return (
            {
                "status": "unresolved",
                "source_url": d["url"].split("#")[0],
                "reason": info.get("why", "HTML unavailable"),
                "last_attempt": info,
            },
            None,
        )
    if generic:
        return render_generic_html(d, fetcher, html, info, url), None

    soup = core.soup_of(html)
    primary_url = url
    article = core.article_of(soup)
    # 一些 Getting Started 首页只有 meta refresh，正文实际从 chapters/ 开始。
    refresh = soup.find("meta", attrs={"http-equiv": re.compile("^refresh$", re.I)})
    if article is not None and len(article.get_text(" ", strip=True)) < 80 and refresh:
        match = re.search(r"url\s*=\s*([^;]+)", refresh.get("content", ""), re.I)
        if match:
            candidate = urllib.parse.urljoin(url, match.group(1).strip(" '\""))
            page_ok, page_html, _ = fetcher.get(candidate)
            if page_ok:
                primary_url = candidate
                soup = core.soup_of(page_html)
                article = core.article_of(soup)
    meta = core.head_meta(soup)
    urls = core.book_pages(fetcher, primary_url, meta)
    if not urls:
        urls = core.follow_chain(fetcher, primary_url, article)
    if primary_url not in urls:
        urls = [primary_url] + [
            candidate for candidate in urls if candidate != primary_url
        ]
    good: list[str] = []
    for candidate in urls[: core.MAX_PAGES_PER_DOC]:
        page_ok, _, _ = fetcher.get(candidate)
        if page_ok:
            good.append(candidate)
    if not good:
        return (
            {
                "status": "unresolved",
                "source_url": d["url"].split("#")[0],
                "reason": "entry fetched but no valid pages",
            },
            None,
        )
    prefetch_images(fetcher, good)
    return (
        {
            "status": "staged-html",
            "source_url": d["url"].split("#")[0],
            "pages": len(good),
            "acquisition": info,
        },
        {"entry": primary_url, "urls": good, "bad": len(urls) - len(good)},
    )


def command_recover(args) -> None:
    docs = load_docs()
    if args.ids:
        wanted = set(args.ids.split(","))
        docs = [d for d in docs if d["apple_id"] in wanted]
    if args.limit:
        docs = docs[: args.limit]
    sources = load_sources()
    pages_path = STATE / "pages.json"
    STATE.mkdir(parents=True, exist_ok=True)
    pages = json.loads(pages_path.read_text()) if pages_path.exists() else {}

    for index, d in enumerate(docs, 1):
        aid = d["apple_id"]
        if aid in sources and not args.ids and not args.retry_unresolved:
            continue
        if (
            aid in sources
            and args.retry_unresolved
            and sources[aid].get("status") != "unresolved"
        ):
            continue
        try:
            if aid in ALIAS_FIXES:
                result = fix_alias(d)
                page_info = None
            elif d["url"].split("#")[0].lower().endswith(".pdf"):
                fetcher = HistoricalFetcher(aid)
                fetcher.preferred_timestamp = SNAPSHOT_OVERRIDES.get(aid)
                result = render_pdf(d, fetcher)
                page_info = None
            else:
                result, page_info = recover_html(d)
            sources[aid] = {"name": d["name"], **result}
            if page_info:
                pages[aid] = page_info
        except Exception as exc:
            sources[aid] = {
                "name": d["name"],
                "status": "unresolved",
                "source_url": d["url"].split("#")[0],
                "reason": f"{type(exc).__name__}: {exc}",
            }
        pages_path.write_text(json.dumps(pages, ensure_ascii=False), encoding="utf-8")
        save_sources(sources)
        print(
            f"[{index}/{len(docs)}] {aid} {sources[aid]['status']} "
            f"{sources[aid].get('pages', '')}",
            flush=True,
        )


def command_render(_args) -> None:
    class Args:
        types = None

    core.cmd_render(Args())
    core.cmd_assets(Args())
    core.cmd_selftest(Args())


def command_repair_assets(args) -> None:
    """重试正文配图，删除伪图片，并把最终缺口显式写入 Markdown 和审计报告。"""
    plans_path = STATE / "plans.json"
    if not plans_path.exists():
        raise SystemExit("缺少 .staging plans.json，请先运行 recover 和 render")
    plans = json.loads(plans_path.read_text(encoding="utf-8"))
    sources = load_sources()
    records: list[dict] = []
    touched_pages: set[Path] = set()
    jobs: dict[str, dict] = {}

    for aid, plan in plans.items():
        if aid not in sources:
            continue
        fetcher = HistoricalFetcher(aid)
        fetcher.delay = args.delay
        acquisition = sources[aid].get("acquisition", {})
        fetcher.preferred_timestamp = (
            acquisition.get("snapshot") or SNAPSHOT_OVERRIDES.get(aid)
        )
        for page_url, rel in zip(plan["urls"], plan["rels"]):
            ok, html, _ = fetcher.get(page_url)
            if not ok:
                continue
            article = core.article_of(core.soup_of(html))
            if article is None:
                continue
            page_path = ROOT / rel
            touched_pages.add(page_path)
            for image in article.find_all("img"):
                src = (image.get("src") or "").split("?")[0]
                if not src or src.startswith("data:"):
                    continue
                absolute = urllib.parse.urljoin(page_url, src)
                if not core.in_archive(absolute) or "/Resources/" in absolute:
                    continue
                if Path(urllib.parse.urlparse(absolute).path).name.lower() in core.DECOR_IMAGES:
                    continue
                sub = re.sub(r"^(\.\./)+", "", src)
                destination = page_path.parent / "attachments" / sub
                relative = destination.relative_to(ROOT).as_posix()
                filename = Path(urllib.parse.urlparse(absolute).path).name
                if destination.is_file() and binary_good(absolute, destination.read_bytes()):
                    records.append(
                        {
                            "apple_id": aid,
                            "page": rel,
                            "url": absolute,
                            "path": relative,
                            "status": "valid-existing",
                        }
                    )
                    continue
                if filename in KNOWN_UNAVAILABLE_IMAGE_NAMES:
                    if destination.is_file():
                        destination.unlink()
                    records.append(
                        {
                            "apple_id": aid,
                            "page": rel,
                            "url": absolute,
                            "path": relative,
                            "status": "unavailable",
                            "last_attempt": {"why": "known-missing-wayback-asset"},
                        }
                    )
                    continue
                jobs.setdefault(
                    relative,
                    {
                        "apple_id": aid,
                        "page": rel,
                        "url": absolute,
                        "path": relative,
                        "destination": destination,
                        "snapshot": fetcher.preferred_timestamp
                        or SNAPSHOT_TARGETS[0],
                    },
                )

    def fetch_asset(job: dict) -> tuple[dict, bytes, dict]:
        acquisition_url = (
            f"https://web.archive.org/web/{job['snapshot']}id_/{job['url']}"
        )
        info = {
            "status": 0,
            "ok": False,
            "why": "not-attempted",
            "acquisition_url": acquisition_url,
        }
        result = subprocess.run(
            [
                "curl",
                "--location",
                "--fail",
                "--silent",
                "--show-error",
                "--retry",
                "2",
                "--retry-all-errors",
                "--connect-timeout",
                "6",
                "--max-time",
                "25",
                "--user-agent",
                core.UA,
                acquisition_url,
            ],
            capture_output=True,
            check=False,
        )
        data = result.stdout
        ok = result.returncode == 0 and binary_good(job["url"], data)
        info = {
            "status": 200 if ok else 0,
            "size": len(data),
            "ok": ok,
            "why": (
                "ok"
                if ok
                else f"curl-exit-{result.returncode}: "
                + result.stderr.decode("utf-8", "replace")[:180]
            ),
            "source": "wayback",
            "acquisition_url": acquisition_url,
            "target_timestamp": job["snapshot"],
        }
        return job, data if ok else b"", info

    completed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(fetch_asset, job) for job in jobs.values()]
        for future in concurrent.futures.as_completed(futures):
            job, data, info = future.result()
            destination = job.pop("destination")
            job.pop("snapshot")
            if data:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(data)
                records.append({**job, "status": "recovered", "acquisition": info})
            else:
                if destination.is_file():
                    destination.unlink()
                status = (
                    "unavailable"
                    if info["why"].startswith("curl-exit-0:")
                    else "network-error"
                )
                records.append({**job, "status": status, "last_attempt": info})
            completed += 1
            if completed % 25 == 0 or completed == len(futures):
                print(
                    f"  Wayback 附件 {completed}/{len(futures)} …",
                    flush=True,
                )

    # 同一图片可能被 wide/ipad 两个 img 标签重复引用；审计按最终文件路径去重。
    records_by_path: dict[str, dict] = {}
    priority = {
        "network-error": 0,
        "unavailable": 1,
        "valid-existing": 2,
        "recovered": 3,
    }
    for record in records:
        previous = records_by_path.get(record["path"])
        if previous is None or priority[record["status"]] >= priority[previous["status"]]:
            records_by_path[record["path"]] = record
    records = list(records_by_path.values())

    image_rx = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    statuses_by_path: dict[str, set[str]] = {}
    for record in records:
        statuses_by_path.setdefault(record["path"], set()).add(record["status"])
    missing_status_by_path = {
        path: (
            "unavailable"
            if "unavailable" in statuses
            else "network-error"
        )
        for path, statuses in statuses_by_path.items()
        if not statuses.intersection({"valid-existing", "recovered"})
    }
    available_by_page: dict[tuple[str, str], str] = {}
    for record in records:
        if record["status"] == "unavailable":
            continue
        page = ROOT / record["page"]
        target = os.path.relpath(ROOT / record["path"], page.parent)
        available_by_page[(record["page"], Path(record["path"]).name)] = (
            core.quote_path(target)
        )
    for page_path in sorted(touched_pages):
        if not page_path.is_file():
            continue
        text = page_path.read_text(encoding="utf-8")
        page_rel = page_path.relative_to(ROOT).as_posix()
        placeholder_rx = re.compile(r"（原归档配图未能恢复：`([^`]+)`）")
        text = placeholder_rx.sub(
            lambda match: (
                f"![{match.group(1)}]"
                f"({available_by_page[(page_rel, match.group(1))]})"
                if (page_rel, match.group(1)) in available_by_page
                else match.group(0)
            ),
            text,
        )

        def replace_missing(match: re.Match[str]) -> str:
            raw_target = match.group(2).split(' "', 1)[0]
            target = urllib.parse.unquote(raw_target.split("#", 1)[0])
            if not target or target.startswith(("http:", "https:", "data:")):
                return match.group(0)
            filename = Path(target).name
            if filename.lower() in core.DECOR_IMAGES:
                return ""
            destination = (page_path.parent / target).resolve()
            try:
                relative = destination.relative_to(ROOT).as_posix()
            except ValueError:
                return match.group(0)
            status = missing_status_by_path.get(relative)
            if status is None:
                return match.group(0)
            if status == "network-error":
                return f"（原归档配图获取待重试：`{filename}`）"
            return f"（原归档配图未能恢复：`{filename}`）"

        updated = image_rx.sub(replace_missing, text)
        updated = re.sub(
            r"(（原归档配图未能恢复：`([^`]+)`）)"
            r"(?:\1)+",
            r"\1",
            updated,
        )
        if updated != text:
            page_path.write_text(updated, encoding="utf-8")

    status_counts = Counter(record["status"] for record in records)
    by_document: dict[str, Counter] = {}
    for record in records:
        by_document.setdefault(record["apple_id"], Counter())[record["status"]] += 1
    payload = {
        "meta": {
            "records": len(records),
            "unique_assets": len({record["path"] for record in records}),
            "status_counts": dict(sorted(status_counts.items())),
            "note": (
                "unavailable means a replay returned non-image content; "
                "network-error is a transport failure and must not be counted "
                "as a confirmed source gap"
            ),
        },
        "by_document": {
            aid: dict(sorted(counts.items()))
            for aid, counts in sorted(by_document.items())
        },
        "assets": records,
    }
    ASSET_REPORT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"附件审计 {payload['meta']['unique_assets']} 个唯一文件："
        + "，".join(f"{key} {value}" for key, value in sorted(status_counts.items()))
    )


def command_install(args) -> None:
    if not OUT.exists():
        raise SystemExit("没有渲染产物，请先运行 render")
    copied = 0
    skipped = 0
    for source in sorted(OUT.rglob("*")):
        if not source.is_file():
            continue
        relative = source.relative_to(OUT)
        destination = ROOT / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and destination.read_bytes() != source.read_bytes():
            if getattr(args, "skip_existing", False):
                skipped += 1
                continue
            raise SystemExit(f"拒绝覆盖不同内容：{relative}")
        if not destination.exists():
            shutil.copy2(source, destination)
            copied += 1
    print(f"安装 {copied} 个新文件，跳过 {skipped} 个既有文件")


def command_report(_args) -> None:
    sources = load_sources()
    counts = Counter(v.get("status", "unknown") for v in sources.values())
    print(f"输入 {len(load_docs())}，已审计 {len(sources)}")
    for status, count in sorted(counts.items()):
        print(f"{status:24} {count:4}")
    unresolved = [
        (aid, value.get("name"), value.get("reason"))
        for aid, value in sources.items()
        if value.get("status") == "unresolved"
    ]
    for aid, name, reason in unresolved:
        print(f"  {aid}\t{name}\t{reason}")


def main() -> None:
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest="command", required=True)
    recover = subs.add_parser("recover")
    recover.add_argument("--limit", type=int, default=0)
    recover.add_argument("--ids", default="")
    recover.add_argument("--retry-unresolved", action="store_true")
    recover.set_defaults(func=command_recover)
    for name, func in (
        ("render", command_render),
        ("repair-assets", command_repair_assets),
        ("report", command_report),
    ):
        sub = subs.add_parser(name)
        if name == "repair-assets":
            sub.add_argument(
                "--delay",
                type=float,
                default=0.5,
                help="同一进程两次网络请求之间的最短秒数",
            )
            sub.add_argument(
                "--workers",
                type=int,
                default=6,
                help="并行请求 Wayback 附件的工作线程数",
            )
        sub.set_defaults(func=func)
    install = subs.add_parser("install")
    install.add_argument(
        "--skip-existing",
        action="store_true",
        help="增量重渲染时保留已经安装的文件，仅复制新文件和新附件",
    )
    install.set_defaults(func=command_install)
    all_cmd = subs.add_parser("all")
    all_cmd.add_argument("--limit", type=int, default=0)
    all_cmd.add_argument("--ids", default="")
    all_cmd.add_argument("--retry-unresolved", action="store_true")

    def run_all(args):
        command_recover(args)
        command_render(args)
        command_install(args)
        command_report(args)

    all_cmd.set_defaults(func=run_all)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
