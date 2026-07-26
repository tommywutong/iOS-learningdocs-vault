#!/usr/bin/env python3
"""抓取 WWDC session 的逐字稿与元数据，渲染成 Markdown。

    python3 tools/wwdc.py fetch            # 抓短名单（178 场）的 HTML 到 .cache/wwdc/
    python3 tools/wwdc.py fetch --all      # 抓全部 1560 场
    python3 tools/wwdc.py render           # 缓存的 HTML → wwdc/en/**.md

## 为什么要按 <p> 重组段落

Apple 的逐字稿是 ASR（自动语音识别）产物，**没有人工校对**。DOM 结构是：

    #transcript-content > p > span.sentence > span[data-start]

`span.sentence` 的切分极碎——老年份只有 27% 的 span 以句末标点结尾，一句话经常
被切成三四个 span。如果按 span 逐条输出，中文译文会碎得没法读。所以这里按 `<p>`
聚合：一个 `<p>` 就是一个自然段，段内所有 sentence 拼接成连续文本。

## 这个链路的脆弱性

Apple 没有为 /videos/ 提供任何 JSON API（试过四种猜法全 404），sitemap 也是 404，
所以整条链路挂在 HTML 的 CSS class 上，改版即失效。Apple 自己把属性拼成
`data-chapter-lenght`（拼错了）——可见没有任何契约保证。因此：
**原始 HTML 一律留在 .cache/wwdc/，渲染逻辑可以随时重写而不必重抓。**
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import re
import sys
from pathlib import Path

import httpx
import lxml.html

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "wwdc"
META = ROOT / "meta"
OUT_DIR = "wwdc/en"
OUT = ROOT / OUT_DIR

CONCURRENCY = 4
HEADERS = {"User-Agent": "apple-developer-docs-vault/0.1 (personal archive)"}


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:80] or "session"


# ---------------------------------------------------------------- 抓取


async def fetch_all(sessions: list[dict]) -> None:
    todo = [s for s in sessions if not (CACHE / s["collection"] / f"{s['id']}.html").exists()]
    print(f"共 {len(sessions)} 场，已缓存 {len(sessions) - len(todo)}，待抓 {len(todo)}")
    if not todo:
        return

    sem = asyncio.Semaphore(CONCURRENCY)
    ok = fail = 0

    async with httpx.AsyncClient(timeout=60, headers=HEADERS, follow_redirects=True) as client:

        async def one(s: dict) -> None:
            nonlocal ok, fail
            delay = 2.0
            for attempt in range(4):
                async with sem:
                    try:
                        r = await client.get(s["url"])
                    except Exception as e:
                        if attempt == 3:
                            print(f"  [失败] {s['url']} :: {e}", file=sys.stderr)
                            fail += 1
                            return
                    else:
                        if r.status_code == 200:
                            p = CACHE / s["collection"] / f"{s['id']}.html"
                            p.parent.mkdir(parents=True, exist_ok=True)
                            p.write_text(r.text, encoding="utf-8")
                            ok += 1
                            if ok % 25 == 0:
                                print(f"    {ok}/{len(todo)}")
                            return
                        if r.status_code in (404, 410):
                            print(f"  [{r.status_code}] {s['url']}", file=sys.stderr)
                            fail += 1
                            return
                await asyncio.sleep(delay)
                delay *= 2
            fail += 1

        await asyncio.gather(*(one(s) for s in todo))

    print(f"抓取完成：成功 {ok}，失败 {fail}")


# ---------------------------------------------------------------- 解析


def parse(html: str) -> dict:
    doc = lxml.html.fromstring(html)
    out: dict = {}

    # 标题：优先页面内 h1，退回 <title>
    h1 = doc.xpath("//h1//text()")
    title = " ".join(t.strip() for t in h1 if t.strip())
    if not title:
        t = doc.xpath("//title/text()")
        title = re.sub(r"\s*-\s*(WWDC\d+|Tech Talks).*$", "", t[0]).strip() if t else ""
    out["title"] = title

    # 摘要：og:description 最稳，其次页面内的描述段
    og = doc.xpath("//meta[@property='og:description']/@content")
    if og:
        out["abstract"] = og[0].strip()
    else:
        d = doc.xpath("//div[contains(@class,'supplement') and contains(@class,'details')]//p//text()")
        out["abstract"] = " ".join(x.strip() for x in d if x.strip())[:1200]

    # 逐字稿：按 <p> 聚合成自然段，段内拼接 sentence
    paras: list[str] = []
    for p in doc.xpath("//*[@id='transcript-content']//p"):
        sentences = [
            " ".join(x.split())
            for x in p.xpath(".//span[contains(@class,'sentence')]//text()")
        ]
        text = " ".join(s for s in sentences if s)
        text = re.sub(r"\s+([,.;:!?])", r"\1", text).strip()
        if text:
            paras.append(text)
    out["transcript"] = paras

    # 章节（2023 起才有）
    chapters = []
    for a in doc.xpath("//*[contains(@class,'chapter')]//a[@href]"):
        name = " ".join(a.text_content().split())
        if name:
            chapters.append({"title": name, "href": a.get("href")})
    out["chapters"] = chapters

    # 资源链接：幻灯片 PDF、示例代码、相关文档
    resources = []
    for a in doc.xpath("//*[contains(@class,'supplement') or contains(@class,'resources')]//a[@href]"):
        href = a.get("href", "")
        name = " ".join(a.text_content().split())
        if href.startswith("#") or not name:
            continue
        if href.startswith("/"):
            href = "https://developer.apple.com" + href
        resources.append({"title": name, "url": href})
    # 去重保序
    seen = set()
    out["resources"] = [
        r for r in resources if not (r["url"] in seen or seen.add(r["url"]))
    ]
    return out


# ---------------------------------------------------------------- 渲染


def q(v: str) -> str:
    if v == "" or re.search(r"[:#\[\]{}&*!|>'\"%@`]", v) or v[0] in " -?":
        return "'" + v.replace("'", "''") + "'"
    return v


def render_one(s: dict, parsed: dict, content_hash: str) -> str:
    fm = [
        "---",
        f"title: {q(parsed['title'] or s['title'])}",
        f"session_id: {q(str(s['id']))}",
        f"collection: {q(s['collection'])}",
        f"year: {s['year'] if s.get('year') else 'null'}",
        f"duration: {q(s.get('duration') or '')}",
        f"topics: [{', '.join(q(t) for t in s.get('topics') or [])}]",
        f"group: {q(s.get('group') or '')}",
        f"evergreen: {'true' if s.get('evergreen') else 'false'}",
        f"source_url: {q(s['url'])}",
        f"content_hash: {q(content_hash)}",
        "translated: false",
        "---",
    ]
    parts = ["\n".join(fm)]

    parts.append(f"# {parsed['title'] or s['title']}")
    meta_line = " · ".join(
        x
        for x in [
            s["collection"].upper() if s.get("collection") else "",
            s.get("duration") or "",
            "、".join(s.get("topics") or []),
        ]
        if x
    )
    if meta_line:
        parts.append(f"<sub>{meta_line}</sub>")

    if parsed.get("abstract"):
        parts.append(parsed["abstract"])

    if s.get("reason"):
        parts.append(f"> [!note] 归档理由\n> {s['reason']}")

    if parsed.get("chapters"):
        lines = [f"- [{c['title']}]({c['href']})" for c in parsed["chapters"]]
        parts.extend(["## Chapters", "\n".join(lines)])

    if parsed.get("resources"):
        lines = [f"- [{r['title']}]({r['url']})" for r in parsed["resources"]]
        parts.extend(["## Resources", "\n".join(lines)])

    if parsed.get("transcript"):
        parts.append("## Transcript")
        parts.append(
            "> [!warning] 关于逐字稿\n"
            "> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。"
            "段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。"
        )
        parts.extend(parsed["transcript"])
    else:
        parts.append("> [!warning] 本场没有可用的逐字稿。")

    text = "\n\n".join(p for p in parts if p and p.strip())
    return re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"


def render_all(sessions: list[dict]) -> None:
    written = missing = 0
    no_transcript = []
    for s in sessions:
        cached = CACHE / s["collection"] / f"{s['id']}.html"
        if not cached.exists():
            missing += 1
            continue
        html = cached.read_text(encoding="utf-8")
        parsed = parse(html)
        if not parsed["transcript"]:
            no_transcript.append(f"{s['collection']}/{s['id']}")
        h = "sha256:" + hashlib.sha256(html.encode("utf-8")).hexdigest()[:16]
        out = OUT / s["collection"] / f"{s['id']}-{slugify(parsed['title'] or s['title'])}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_one(s, parsed, h), encoding="utf-8")
        written += 1
    print(f"渲染完成：写出 {written} 篇，缺缓存 {missing}")
    if no_transcript:
        print(f"  [注意] {len(no_transcript)} 场无逐字稿：{no_transcript[:8]}")


# ---------------------------------------------------------------- 入口


def main() -> None:
    which = META / ("wwdc_all_sessions.json" if "--all" in sys.argv else "wwdc_shortlist.json")
    data = json.loads(which.read_text(encoding="utf-8"))
    sessions = data if isinstance(data, list) else (data.get("sessions") or list(data.values())[0])
    # 全量清单里有无视频的占位条目（WWDC22/23 的 Q&A: / Meet the Presenter:），跳过
    sessions = [
        s
        for s in sessions
        if s.get("url") and not re.match(r"^(Q&A|Meet the Presenter):", s.get("title", ""))
    ]

    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "fetch":
        asyncio.run(fetch_all(sessions))
    elif cmd == "render":
        render_all(sessions)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
