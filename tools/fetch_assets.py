#!/usr/bin/env python3
"""下载 meta/assets.json 里登记的图片等资源到 attachments/。

    python3 tools/fetch_assets.py            # 下载全部未下载的
    python3 tools/fetch_assets.py --dry-run  # 只看要下多少

渲染阶段只登记 URL → 本地路径的映射，实际下载放在这里，好处是渲染可以反复重跑
而不会重复打 Apple 的服务器。已存在且非空的文件直接跳过。
"""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "meta" / "assets.json"

CONCURRENCY = 12
HEADERS = {
    "User-Agent": "apple-developer-docs-vault/0.1 (personal documentation mirror)",
}


async def main() -> None:
    if not ASSETS.exists():
        sys.exit("缺 meta/assets.json，先跑 render.py")
    mapping: dict[str, str] = json.loads(ASSETS.read_text(encoding="utf-8"))

    todo = [(u, p) for u, p in mapping.items() if not (ROOT / p).exists() or (ROOT / p).stat().st_size == 0]
    print(f"资源共 {len(mapping)} 项，待下载 {len(todo)}")
    if "--dry-run" in sys.argv or not todo:
        return

    sem = asyncio.Semaphore(CONCURRENCY)
    ok = fail = 0
    total_bytes = 0

    async with httpx.AsyncClient(timeout=60.0, headers=HEADERS, follow_redirects=True) as client:

        async def one(url: str, rel: str) -> None:
            nonlocal ok, fail, total_bytes
            delay = 1.0
            for attempt in range(4):
                async with sem:
                    try:
                        r = await client.get(url)
                    except Exception as e:
                        if attempt == 3:
                            print(f"  [失败] {url} :: {e}", file=sys.stderr)
                            fail += 1
                            return
                    else:
                        if r.status_code == 200:
                            out = ROOT / rel
                            out.parent.mkdir(parents=True, exist_ok=True)
                            out.write_bytes(r.content)
                            ok += 1
                            total_bytes += len(r.content)
                            return
                        if r.status_code in (404, 410):
                            print(f"  [404] {url}", file=sys.stderr)
                            fail += 1
                            return
                await asyncio.sleep(delay)
                delay *= 2
            fail += 1

        await asyncio.gather(*(one(u, p) for u, p in todo))

    print(f"下载完成：成功 {ok}，失败 {fail}，{total_bytes / 1e6:.1f} MB")


if __name__ == "__main__":
    asyncio.run(main())
