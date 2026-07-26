#!/usr/bin/env python3
"""第三方技术博客归档。

    python3 tools/blog.py probe <url>          # 探正文容器的 XPath（用于填 config）
    python3 tools/blog.py discover <key>...    # 建文章清单 → meta/blog_index/<key>.json
    python3 tools/blog.py fetch <key>...       # 抓文章 HTML → .cache/blogs/<key>/
    python3 tools/blog.py render <key>...      # HTML → blogs/{en,zh}/<key>/*.md
    python3 tools/blog.py list                 # 列出所有配置的源及状态

源配置在 `meta/blog_sources.json`。

## 归档策略（用户定的）

- **英文源**：`blogs/en/<key>/` 存英文原文，`blogs/zh/<key>/` 存中文译文，两边都在
  frontmatter 里带原始链接。
- **中文源**：只存 `blogs/zh/<key>/`，不需要翻译，同样带原始链接。

## robots.txt

除了配置阶段已核实过，这里**每次抓取前再查一遍运行时 robots**，并且专门检查
`ClaudeBot` / `anthropic-ai` 这两个 user-agent 段。有站点（massicotte.org、
casatwy.com）在 `User-agent: *` 放开的同时单独禁掉了 AI 爬虫——只看 `*` 会漏掉。
命中即跳过该源，不抓。
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

import httpx
import lxml.etree
import lxml.html

sys.path.insert(0, str(Path(__file__).resolve().parent))
from html2md import node_to_markdown, to_markdown

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "blogs"
META = ROOT / "meta"
INDEX_DIR = META / "blog_index"
# 默认读 meta/blog_sources.json；批次任务可用环境变量指向别的配置文件，
# 避免多个人同时改同一份 JSON。相对路径按仓库根解析。
CONFIG = META / "blog_sources.json"
if os.environ.get("BLOG_CONFIG"):
    _c = Path(os.environ["BLOG_CONFIG"])
    CONFIG = _c if _c.is_absolute() else (ROOT / _c)

CONCURRENCY = 3          # 对个人博客保持克制
DELAY = 1.0              # 每个请求之间的间隔（秒）
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 personal-archive/0.1"
HEADERS = {"User-Agent": UA}

# 我们自己要遵守的 user-agent 名字，除了通配符还要单独看这几个
SELF_AGENTS = ("claudebot", "anthropic-ai", "claude-web", "personal-archive")


def load_config() -> dict:
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def source_by_key(cfg: dict, key: str) -> dict | None:
    return next((s for s in cfg["sources"] if s["key"] == key), None)


def slugify(text: str, fallback: str = "post") -> str:
    s = re.sub(r"[^a-z0-9一-鿿]+", "-", (text or "").lower()).strip("-")
    return (s[:90] or fallback)


# ---------------------------------------------------------------- robots


async def robots_allows(client: httpx.AsyncClient, homepage: str) -> tuple[bool, str]:
    """返回 (是否允许抓, 说明)。取不到 robots.txt 视为允许（无限制）。"""
    parsed = urllib.parse.urlparse(homepage)
    url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    try:
        r = await client.get(url)
    except Exception as e:
        return True, f"robots.txt 取不到（{type(e).__name__}），视为无限制"
    if r.status_code != 200:
        return True, f"robots.txt HTTP {r.status_code}，视为无限制"

    # 逐段解析，只关心通配符段和点名我们的段
    blocks: list[tuple[list[str], list[str]]] = []
    agents: list[str] = []
    rules: list[str] = []
    for line in r.text.splitlines():
        line = line.split("#")[0].strip()
        if not line:
            continue
        k, _, v = line.partition(":")
        k, v = k.strip().lower(), v.strip()
        if k == "user-agent":
            if rules:
                blocks.append((agents, rules))
                agents, rules = [], []
            agents.append(v.lower())
        elif k == "disallow":
            rules.append(v)
    if agents:
        blocks.append((agents, rules))

    for agent_list, disallows in blocks:
        named = any(a in SELF_AGENTS for a in agent_list)
        if not named:
            continue
        if any(d == "/" for d in disallows):
            return False, f"robots.txt 点名禁止 {agent_list}：Disallow: /"
    for agent_list, disallows in blocks:
        if "*" in agent_list and any(d == "/" for d in disallows):
            return False, "robots.txt 对所有爬虫 Disallow: /"
    return True, "robots.txt 允许"


# ---------------------------------------------------------------- probe


async def probe(url: str) -> None:
    async with httpx.AsyncClient(timeout=45, headers=HEADERS, follow_redirects=True) as c:
        r = await c.get(url)
    print(f"HTTP {r.status_code}  {len(r.content)} 字节")
    if r.status_code != 200:
        return
    doc = lxml.html.fromstring(r.text)
    cands: list[tuple[int, str, str]] = []
    probes = [
        "//article", "//main", "//div[@id='content']", "//div[@id='main']",
        "//div[contains(@class,'post-content')]", "//div[contains(@class,'entry-content')]",
        "//div[contains(@class,'article-content')]", "//div[contains(@class,'post-body')]",
        "//div[contains(@class,'markdown')]", "//div[contains(@class,'content')]",
        "//div[contains(@class,'post')]", "//div[contains(@class,'entry')]",
    ]
    for xp in probes:
        for el in doc.xpath(xp):
            n = len(el.text_content() or "")
            ident = (el.get("class") or el.get("id") or "")[:46]
            cands.append((n, xp, ident))
    cands.sort(reverse=True)
    print(f"\n<pre> 数量: {len(doc.xpath('//pre'))}   "
          f"Crayon textarea: {len(doc.xpath('//textarea[contains(@class,\"crayon-plain\")]'))}")
    print("\n正文容器候选（按文本量降序，取第一个通常就对）：")
    seen = set()
    for n, xp, ident in cands[:8]:
        if (xp, ident) in seen:
            continue
        seen.add((xp, ident))
        print(f"  {n:>7} 字   {xp:52} class/id={ident}")
    h1 = doc.xpath("//h1//text()")
    print(f"\nh1: {' '.join(t.strip() for t in h1 if t.strip())[:90]!r}")
    for prop in ("article:published_time", "og:title", "og:description"):
        v = doc.xpath(f"//meta[@property='{prop}']/@content")
        if v:
            print(f"{prop}: {v[0][:90]!r}")


# ---------------------------------------------------------------- discover


async def discover(keys: list[str]) -> None:
    cfg = load_config()
    async with httpx.AsyncClient(timeout=60, headers=HEADERS, follow_redirects=True) as c:
        for key in keys:
            s = source_by_key(cfg, key)
            if not s:
                print(f"  {key}: 配置里没有这个源", file=sys.stderr)
                continue
            allowed, why = await robots_allows(c, s["homepage"])
            if not allowed:
                print(f"  {key}: 跳过 —— {why}")
                continue

            d = s["discover"]
            urls: list[dict] = []
            # `url` 可以是一个字符串，也可以是一串分页索引页（Hexo 的 /archives/page/N/、
            # WordPress 的 /category/x/page/N/ 都只在单页给十来条，必须逐页翻）。
            pages = d["url"] if isinstance(d["url"], list) else [d["url"]]
            try:
              for pi, page_url in enumerate(pages):
                if pi:
                    await asyncio.sleep(DELAY)
                r = await c.get(page_url)
                if r.status_code != 200:
                    print(f"  {key}: 清单源 HTTP {r.status_code} ({page_url})")
                    continue
                if d["type"] == "feed":
                    import feedparser

                    feed = feedparser.parse(r.text)
                    for e in feed.entries:
                        urls.append({
                            "url": e.get("link", ""),
                            "title": e.get("title", ""),
                            "date": (e.get("published") or e.get("updated") or "")[:10],
                        })
                elif d["type"] == "sitemap":
                    root = lxml.etree.fromstring(r.content)
                    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                    for loc in root.xpath("//s:url/s:loc/text()", namespaces=ns):
                        urls.append({"url": str(loc), "title": "", "date": ""})
                    if not urls:  # sitemap index
                        for loc in root.xpath("//s:sitemap/s:loc/text()", namespaces=ns):
                            rr = await c.get(str(loc))
                            sub = lxml.etree.fromstring(rr.content)
                            for l2 in sub.xpath("//s:url/s:loc/text()", namespaces=ns):
                                urls.append({"url": str(l2), "title": "", "date": ""})
                            await asyncio.sleep(DELAY)
                else:  # index 页
                    doc = lxml.html.fromstring(r.text)
                    doc.make_links_absolute(page_url)
                    pat = d.get("url_filter")
                    for a in doc.xpath("//a[@href]"):
                        href = a.get("href").split("#")[0]
                        rel = urllib.parse.urlparse(href).path
                        if pat and not (re.search(pat, rel) or re.search(pat, href)):
                            continue
                        urls.append({
                            "url": href,
                            "title": " ".join(a.text_content().split())[:200],
                            "date": "",
                        })
            except Exception as e:
                print(f"  {key}: 清单解析失败 {type(e).__name__}: {e}", file=sys.stderr)
                continue

            # 去重、剔掉明显不是文章的
            seen, clean = set(), []
            home = urllib.parse.urlparse(s["homepage"])
            for u in urls:
                url = u["url"]
                if not url or url in seen:
                    continue
                p = urllib.parse.urlparse(url)
                if p.netloc and p.netloc != home.netloc:
                    continue
                if re.search(r"\.(png|jpe?g|gif|svg|pdf|zip|xml|css|js)$", p.path, re.I):
                    continue
                # 每源可配的非文章路径排除（标签页、关于页、资源目录等）
                if s.get("exclude") and re.search(s["exclude"], url):
                    continue
                if p.path.rstrip("/") in ("", "/index", home.path.rstrip("/")):
                    continue
                seen.add(url)
                clean.append(u)

            INDEX_DIR.mkdir(parents=True, exist_ok=True)
            (INDEX_DIR / f"{key}.json").write_text(
                json.dumps({"key": key, "count": len(clean), "articles": clean},
                           ensure_ascii=False, indent=1),
                encoding="utf-8",
            )
            print(f"  {key:20} {len(clean):>5} 篇  （{d['type']}）  {why}")
            await asyncio.sleep(DELAY)


# ---------------------------------------------------------------- fetch


def article_cache(key: str, url: str) -> Path:
    h = hashlib.sha256(url.encode()).hexdigest()[:12]
    name = slugify(urllib.parse.urlparse(url).path.strip("/").replace("/", "-"), h)
    return CACHE / key / f"{name}-{h}.html"


async def fetch(keys: list[str]) -> None:
    cfg = load_config()
    async with httpx.AsyncClient(timeout=60, headers=HEADERS, follow_redirects=True) as c:
        for key in keys:
            s = source_by_key(cfg, key)
            idx = INDEX_DIR / f"{key}.json"
            if not s or not idx.exists():
                print(f"  {key}: 缺配置或清单，先跑 discover", file=sys.stderr)
                continue
            allowed, why = await robots_allows(c, s["homepage"])
            if not allowed:
                print(f"  {key}: 跳过 —— {why}")
                continue

            arts = json.loads(idx.read_text(encoding="utf-8"))["articles"]
            todo = [a for a in arts if not article_cache(key, a["url"]).exists()]
            print(f"\n{key}（{s['name']}）：共 {len(arts)} 篇，已缓存 {len(arts)-len(todo)}，待抓 {len(todo)}")
            if not todo:
                continue

            sem = asyncio.Semaphore(CONCURRENCY)
            ok = fail = 0

            async def one(a: dict) -> None:
                nonlocal ok, fail
                async with sem:
                    await asyncio.sleep(DELAY)
                    try:
                        r = await c.get(a["url"])
                    except Exception as e:
                        fail += 1
                        print(f"    [失败] {a['url']} :: {type(e).__name__}", file=sys.stderr)
                        return
                if r.status_code != 200:
                    fail += 1
                    print(f"    [{r.status_code}] {a['url']}", file=sys.stderr)
                    return
                p = article_cache(key, a["url"])
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(r.text, encoding="utf-8")
                ok += 1
                if ok % 20 == 0:
                    print(f"    {ok}/{len(todo)}")

            await asyncio.gather(*(one(a) for a in todo))
            print(f"  {key}: 成功 {ok}，失败 {fail}")


# ---------------------------------------------------------------- render


def guess_container(doc) -> str | None:
    # 阈值取 200 而不是 800——有些源（onevcat）有大量三五百字的短文，
    # 阈值定高会让它们全部匹配不到容器、静默丢失
    for xp in ["//article", "//div[contains(@class,'post-content')]", "//main",
               "//div[contains(@class,'entry-content')]", "//div[@id='content']",
               "//div[contains(@class,'article-content')]", "//div[contains(@class,'markdown')]"]:
        els = doc.xpath(xp)
        if els and len((els[0].text_content() or "")) > 200:
            return xp
    return None


def q(v: str) -> str:
    if v == "" or re.search(r"[:#\[\]{}&*!|>'\"%@`]", v) or v[0] in " -?":
        return "'" + v.replace("'", "''") + "'"
    return v


def self_title(doc, article: dict, source: dict) -> str:
    """按可靠性依次尝试：清单里的标题 → og:title → <title> → h1 → h2/h4 → URL。

    老站（sealiesoftware 是 2007–2017 的 table 布局）常常连 h1 都没有，只有 h4
    当小节标题，真正的文章名只在 <title> 里，且带站名前缀，需要用配置的
    `title_clean` 正则剥掉。
    """
    t = (article.get("title") or "").strip()
    if t and not re.match(r"^(<<|>>|archive$)", t):
        return t
    for xp in ("//meta[@property='og:title']/@content", "//title/text()"):
        v = doc.xpath(xp)
        if v:
            t = " ".join(str(v[0]).split())
            break
    if not t:
        for xp in ("//h1//text()", "//h2//text()", "//h4//text()"):
            v = doc.xpath(xp)
            if v:
                t = " ".join(" ".join(str(x) for x in v).split())
                break
    clean = source.get("title_clean")
    if clean and t:
        t = re.sub(clean, "", t).strip()
    return t


def parse_html(text: str):
    """lxml 拒绝带编码声明的 str 输入（有些老站页首是 <?xml version=… encoding=…?>），
    先把声明剥掉再解析。"""
    if text.lstrip().startswith("<?xml"):
        end = text.find("?>")
        if end != -1:
            text = text[end + 2 :]
    return lxml.html.fromstring(text)


def render(keys: list[str]) -> None:
    cfg = load_config()
    for key in keys:
        # 单源失败不能拖垮整批
        try:
            render_source(cfg, key)
        except Exception as e:
            print(f"  {key}: 整源渲染失败 {type(e).__name__}: {e}", file=sys.stderr)


def render_source(cfg: dict, key: str) -> None:
    if True:
        s = source_by_key(cfg, key)
        idx = INDEX_DIR / f"{key}.json"
        if not s or not idx.exists():
            print(f"  {key}: 缺配置或清单", file=sys.stderr)
            return
        arts = {a["url"]: a for a in json.loads(idx.read_text(encoding="utf-8"))["articles"]}
        lang = s["lang"]
        outdir = ROOT / "blogs" / lang / key
        written = skipped = failed = 0
        taken: dict[str, str] = {}
        no_container = []

        for url, a in arts.items():
            cached = article_cache(key, url)
            if not cached.exists():
                skipped += 1
                continue
            html = cached.read_text(encoding="utf-8")
            doc = parse_html(html)
            xp = s.get("container") or guess_container(doc)
            if not xp:
                no_container.append(url)
                failed += 1
                continue
            container = doc.xpath(xp)
            if not container:
                no_container.append(url)
                failed += 1
                continue
            node = container[0]
            # 在容器节点内剔样板（导航条、分享按钮、作者简介）
            for strip_xp in s.get("strip") or []:
                for el in node.xpath(strip_xp):
                    if el.getparent() is not None:
                        el.getparent().remove(el)
            try:
                md, images = node_to_markdown(
                    node, base_url=url, code_mode=s.get("code_mode", "auto")
                )
            except Exception as e:
                print(f"    [渲染失败] {url} :: {type(e).__name__}: {e}", file=sys.stderr)
                failed += 1
                continue

            title = self_title(doc, a, s)
            date = a.get("date") or ""
            if not date:
                for prop in ("article:published_time", "og:updated_time"):
                    v = doc.xpath(f"//meta[@property='{prop}']/@content")
                    if v:
                        date = v[0][:10]
                        break
            if not date:
                m = re.search(r"/(\d{4})/(\d{1,2})/(\d{1,2})/", url)
                if m:
                    date = f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"

            fm = "\n".join([
                "---",
                f"title: {q(title)}",
                f"source: {q(s['name'])}",
                f"source_key: {q(key)}",
                f"source_url: {q(url)}",
                f"original_language: {lang}",
                f"published: {q(date)}",
                f"status: {q(s.get('status',''))}",
                f"license: {q(s.get('license',''))}",
                f"archived_at: {q(__import__('datetime').datetime.now().strftime('%Y-%m-%d'))}",
                f"content_hash: {q('sha256:'+hashlib.sha256(html.encode()).hexdigest()[:16])}",
                f"translated: {'false' if lang=='en' else 'n/a'}",
                "---",
            ])
            body = f"> 原文：[{title or url}]({url})　·　{s['name']}"
            text = f"{fm}\n\n{body}\n\n{md}"

            base = slugify(title, urllib.parse.urlparse(url).path.strip("/").replace("/", "-"))
            out = outdir / f"{base}.md"
            # 不同文章可能有相同标题（如各期的「话题」页），撞名就拼 URL 哈希，
            # 否则后写的会静默覆盖前一篇。
            if out.exists() and taken.get(base) not in (None, url):
                out = outdir / f"{base}-{hashlib.sha256(url.encode()).hexdigest()[:6]}.md"
            taken[base] = url
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text, encoding="utf-8")
            written += 1

        print(f"  {key:20} 写出 {written:>4} 篇 → blogs/{lang}/{key}/   缺缓存 {skipped}，失败 {failed}")
        if no_container:
            print(f"    [需人工配 container] {len(no_container)} 篇，例如 {no_container[:2]}")


# ---------------------------------------------------------------- 入口


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    rest = sys.argv[2:]
    cfg = load_config()

    if cmd == "list":
        print(f"{'key':22}{'lang':6}{'优先':5}{'状态':8}{'名称'}")
        for s in sorted(cfg["sources"], key=lambda x: (x["priority"], x["key"])):
            print(f"{s['key']:22}{s['lang']:6}{s['priority']:<5}{s['status']:8}{s['name']}")
        print(f"\n另有 {len(cfg['git_sources'])} 个 git 源（clone 而非爬取），见配置的 git_sources")
        return

    keys = rest or [s["key"] for s in cfg["sources"]]
    if cmd == "probe":
        asyncio.run(probe(rest[0]))
    elif cmd == "discover":
        asyncio.run(discover(keys))
    elif cmd == "fetch":
        asyncio.run(fetch(keys))
    elif cmd == "render":
        render(keys)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
