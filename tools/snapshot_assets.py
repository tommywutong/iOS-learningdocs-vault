#!/usr/bin/env python3
"""本地化暑期计划英文快照中的远程图片。

    python3 tools/snapshot_assets.py plan
    python3 tools/snapshot_assets.py fetch --concurrency 8
    python3 tools/snapshot_assets.py verify

只处理 ``summer-snapshots`` 显式白名单。下载前逐资源域名检查 robots.txt；被明确禁止、
非图片响应或网络失败的 URL 保持原样，并记录到 ``meta/snapshot_assets.json``。
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import mimetypes
import os
import re
import shutil
import subprocess
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from shard import ROOT, summer_snapshot_allowlist
from validate import IMAGE

MANIFEST = ROOT / "meta" / "snapshot_assets.json"
ATTACHMENTS = ROOT / "attachments" / "snapshots"
USER_AGENT = "apple-docs-vault-personal-archive/1"
SELF_AGENTS = {"claudebot", "anthropic-ai", "claude-web", "gptbot"}
SUPPORTED_TYPES = {
    "image/avif": ".avif",
    "image/gif": ".gif",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/svg+xml": ".svg",
    "image/webp": ".webp",
}


def remote_targets(path: Path) -> list[str]:
    return sorted({
        target
        for target in IMAGE.findall(path.read_text(encoding="utf-8"))
        if target.startswith(("http://", "https://"))
    })


def article_key(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^source_url:\s*['\"]?([^'\"\n]+)", text, re.MULTILINE)
    source = match.group(1) if match else str(path.relative_to(ROOT))
    return hashlib.sha256(source.encode("utf-8")).hexdigest()[:12]


def extension(content_type: str, url: str) -> str | None:
    media_type = content_type.split(";", 1)[0].strip().lower()
    if media_type in SUPPORTED_TYPES:
        return SUPPORTED_TYPES[media_type]
    suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if suffix in set(SUPPORTED_TYPES.values()):
        return ".jpg" if suffix == ".jpeg" else suffix
    guessed = mimetypes.guess_extension(media_type)
    return guessed if media_type.startswith("image/") else None


def atomic_write(path: Path, content: str) -> None:
    temp_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=".snapshot-assets-",
            suffix=".tmp",
            delete=False,
        ) as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
            temp_name = handle.name
        os.replace(temp_name, path)
        temp_name = None
    finally:
        if temp_name:
            Path(temp_name).unlink(missing_ok=True)


def replace_target(text: str, old: str, new: str) -> str:
    return text.replace(f"]({old}", f"]({new}").replace(
        f"](<{old}>)", f"](<{new}>)"
    )


def tasks() -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for rel in sorted(summer_snapshot_allowlist()):
        path = ROOT / rel
        for url in remote_targets(path):
            out.append({"article": rel, "url": url})
    return out


def robots_allows_origin(origin: str) -> tuple[bool, str]:
    request = urllib.request.Request(
        origin.rstrip("/") + "/robots.txt",
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            text = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return True, f"robots.txt HTTP {exc.code}，视为无限制"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return True, f"robots.txt 取不到（{type(exc).__name__}），视为无限制"

    blocks: list[tuple[list[str], list[str]]] = []
    agents: list[str] = []
    rules: list[str] = []
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip().lower(), value.strip()
        if key == "user-agent":
            if rules:
                blocks.append((agents, rules))
                agents, rules = [], []
            agents.append(value.lower())
        elif key == "disallow":
            rules.append(value)
    if agents:
        blocks.append((agents, rules))
    for agent_list, disallows in blocks:
        if any(agent in SELF_AGENTS for agent in agent_list) and "/" in disallows:
            return False, f"robots.txt 点名禁止 {agent_list}：Disallow: /"
    for agent_list, disallows in blocks:
        if "*" in agent_list and "/" in disallows:
            return False, "robots.txt 对所有爬虫 Disallow: /"
    return True, "robots.txt 允许"


def download(url: str) -> tuple[int, bytes, str, str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "image/*,*/*;q=0.8"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return (
                int(response.status),
                response.read(),
                response.headers.get("Content-Type", ""),
                response.geturl(),
            )
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read(), exc.headers.get("Content-Type", ""), exc.geturl()
    except (urllib.error.URLError, TimeoutError, OSError):
        curl = shutil.which("curl")
        if not curl:
            raise
        temp_name: str | None = None
        try:
            with tempfile.NamedTemporaryFile(delete=False) as handle:
                temp_name = handle.name
            result = subprocess.run(
                [
                    curl,
                    "-L",
                    "--fail",
                    "--silent",
                    "--show-error",
                    "--max-time",
                    "60",
                    "-A",
                    USER_AGENT,
                    "-o",
                    temp_name,
                    "-w",
                    "%{http_code}\n%{content_type}\n%{url_effective}",
                    url,
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode != 0:
                raise OSError(result.stderr.strip() or f"curl exit {result.returncode}")
            lines = result.stdout.splitlines()
            if len(lines) < 3:
                raise OSError("curl 没有返回完整元数据")
            return int(lines[0]), Path(temp_name).read_bytes(), lines[1], lines[2]
        finally:
            if temp_name:
                Path(temp_name).unlink(missing_ok=True)


async def fetch_one(
    semaphore: asyncio.Semaphore,
    robots: dict[str, tuple[bool, str]],
    task: dict[str, str],
) -> dict[str, object]:
    rel, url = task["article"], task["url"]
    parsed = urllib.parse.urlparse(url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    if origin not in robots:
        robots[origin] = await robots_allows(client, origin)
    allowed, why = robots[origin]
    base: dict[str, object] = {"article": rel, "asset_url": url}
    if not allowed:
        return {**base, "status": "robots-disallow", "detail": why}

    try:
        async with semaphore:
            status, payload, content_type, final_url = await asyncio.to_thread(
                download, url
            )
    except Exception as exc:
        return {
            **base,
            "status": "network-error",
            "detail": f"{type(exc).__name__}: {exc}"[:500],
        }
    if status != 200:
        return {
            **base,
            "status": f"http-{status}",
            "detail": f"{len(payload)} bytes",
        }
    suffix = extension(content_type, final_url)
    if suffix is None:
        return {
            **base,
            "status": "not-image",
            "detail": content_type,
        }

    digest = hashlib.sha256(payload).hexdigest()
    article = ROOT / rel
    domain = article.parent.name
    destination = ATTACHMENTS / domain / article_key(article) / f"{digest[:20]}{suffix}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        destination.write_bytes(payload)
    local = Path(os.path.relpath(destination, article.parent)).as_posix()
    return {
        **base,
        "status": "downloaded",
        "final_url": final_url,
        "path": str(destination.relative_to(ROOT)),
        "markdown_target": local,
        "content_type": content_type.split(";", 1)[0],
        "bytes": len(payload),
        "sha256": digest,
    }


async def cmd_fetch(concurrency: int) -> int:
    pending = tasks()
    retained: list[dict[str, object]] = []
    if MANIFEST.exists():
        old = json.loads(MANIFEST.read_text(encoding="utf-8"))
        for entry in old.get("assets", []):
            if entry.get("status") != "downloaded":
                continue
            article = ROOT / str(entry.get("article") or "")
            target = str(entry.get("markdown_target") or "")
            if article.is_file() and target in IMAGE.findall(
                article.read_text(encoding="utf-8")
            ):
                retained.append(entry)
    origins = sorted({
        f"{parsed.scheme}://{parsed.netloc}"
        for item in pending
        if (parsed := urllib.parse.urlparse(item["url"]))
    })
    robots = {
        origin: await asyncio.to_thread(robots_allows_origin, origin)
        for origin in origins
    }
    semaphore = asyncio.Semaphore(concurrency)
    refreshed = await asyncio.gather(*[
        fetch_one(semaphore, robots, task) for task in pending
    ])
    results = retained + list(refreshed)

    by_article: dict[str, list[dict[str, object]]] = {}
    for entry in results:
        by_article.setdefault(str(entry["article"]), []).append(entry)
    for rel, entries in by_article.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        for entry in entries:
            if entry["status"] == "downloaded":
                text = replace_target(
                    text,
                    str(entry["asset_url"]),
                    str(entry["markdown_target"]),
                )
        atomic_write(path, text)

    manifest = {
        "version": 1,
        "scope": "summer-snapshots",
        "files": len(summer_snapshot_allowlist()),
        "assets": sorted(results, key=lambda x: (str(x["article"]), str(x["asset_url"]))),
    }
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    counts: dict[str, int] = {}
    for entry in results:
        status = str(entry["status"])
        counts[status] = counts.get(status, 0) + 1
    print("，".join(f"{name} {count}" for name, count in sorted(counts.items())))
    return 0


def cmd_plan() -> int:
    pending = tasks()
    print(
        f"计划内快照 {len(summer_snapshot_allowlist())} 篇，"
        f"远程图片引用 {len(pending)} 个，唯一 URL {len({x['url'] for x in pending})} 个"
    )
    return 0


def cmd_verify() -> int:
    if not MANIFEST.exists():
        print("缺少 meta/snapshot_assets.json")
        return 1
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    issues: list[str] = []
    for entry in data.get("assets", []):
        if entry.get("status") != "downloaded":
            continue
        path = ROOT / str(entry.get("path") or "")
        if not path.is_file():
            issues.append(f"文件不存在：{entry.get('path')}")
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != entry.get("sha256"):
            issues.append(f"哈希不匹配：{entry.get('path')}")
        article = ROOT / str(entry["article"])
        target = str(entry.get("markdown_target") or "")
        if target not in IMAGE.findall(article.read_text(encoding="utf-8")):
            issues.append(f"文章未引用本地图片：{entry['article']} → {target}")
    print(
        f"校验 {len(data.get('assets', []))} 条图片记录："
        + ("全部通过" if not issues else f"{len(issues)} 个问题")
    )
    for issue in issues[:30]:
        print(f"  {issue}")
    return 1 if issues else 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("plan")
    fetch = sub.add_parser("fetch")
    fetch.add_argument("--concurrency", type=int, default=8)
    sub.add_parser("verify")
    args = parser.parse_args()
    if args.command == "plan":
        code = cmd_plan()
    elif args.command == "fetch":
        if args.concurrency < 1:
            parser.error("--concurrency 必须大于 0")
        code = asyncio.run(cmd_fetch(args.concurrency))
    else:
        code = cmd_verify()
    raise SystemExit(code)


if __name__ == "__main__":
    main()
