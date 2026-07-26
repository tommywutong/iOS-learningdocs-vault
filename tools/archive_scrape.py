#!/usr/bin/env python3
"""补抓 Apple Documentation Archive 中旧仓库漏收的文档，产出与旧仓库字节级同构的 Markdown。

    python3 tools/archive_scrape.py classify [--types 2,5,3]      # 阶段 0：分类（migrated / offsite / ok）
    python3 tools/archive_scrape.py fetch    [--types 2] [--limit N]  # 阶段 1：抓 HTML（含分页发现）
    python3 tools/archive_scrape.py assets   [--types 2]           # 阶段 2：抓插图（可选，单独跑）
    python3 tools/archive_scrape.py render   [--types 2]           # 阶段 3：渲染 Markdown
    python3 tools/archive_scrape.py selftest                       # 阶段 4：质量自检
    python3 tools/archive_scrape.py calibrate                      # 格式标定：与旧仓库现有文档逐字节比对

输入 meta/archive_gap.json，产物一律写 .staging/，**绝不写旧仓库**。

===========================================================================
四个会静默出错的陷阱，以及本文件里防住它们的位置
===========================================================================

1. **404 页比正文还大（82,981 字节）**
   Apple 的 "Page Not Found" 页有 83 KB，比大多数真实归档页都大，任何"响应体够大
   即成功"的判断都会把 404 页当正文写进仓库。
   → `page_is_good()`：必须同时满足 `status == 200`、HTML 里含 `<article id="contents"`、
     `<title>` 不含 `Page Not Found`。三条缺一不可。

2. **裸目录 URL 返回 1,610 字节空壳**
   `technotes/tn2420/` 返回 200 但只有 1,610 字节的空壳；`technotes/tn2420/_index.html`
   才返回 30,256 字节正文。两者状态码都是 200，靠状态码发现不了。
   → `canonical_url()`：所有以 `/` 结尾的 URL 强制补 `_index.html`。
   → `page_is_good()` 另外对 `article#contents` 的纯文本长度设下限，低于阈值告警。

3. **URL 大小写敏感**
   `.../softvdig/introduction/intro.html` 会 200 但多 2 次重定向（服务端纠正大小写）。
   → 全程只用 `archive_gap.json` 的 `url` 字段原始大小写；`url_normalized` 只做比对。

4. **book.json 的 sections 递归嵌套且同一 HTML 被多个 section 引用**
   不按 `#` 前的路径去重，页数会虚高好几倍。
   → `book_pages()`：递归收集 `sections[].href`，`href.split('#')[0]` 后按出现顺序去重。

另外：约 106 份文档已被 Apple 301 迁到现行 `/documentation/`（Swift-DocC JS 空壳，
体积恒定约 17 KB），归档 HTML 与 book.json 都不存在。`classify` 阶段先判定
`url_effective` 是否仍在 `/library/archive/` 下，不在就标 `migrated` 直接跳过，
不进抓取队列。

===========================================================================
格式复刻（依据 meta/recon/VAULT_FORMAT_SPEC.md + 对旧仓库产物的逆向）
===========================================================================
旧仓库的 HTML→Markdown 转换器已被逆向确认为 **markdownify**（BeautifulSoup 后端），
证据见 calibrate 子命令：markdownify 特有的 `convert_tr` 空表头补齐行为
（`|  |` + `| --- |`）在旧仓库 `qa/hw/A SCSI little secret/hw81.md:17-19` 中原样出现。
本文件用 markdownify==1.1.0 + 下列选项/预处理复刻：

* 选项：heading_style=ATX、strong_em_symbol='_'、bullets='-'、escape_underscores=False
* 预处理：`<aside>` 整棵子树丢弃（这正是旧仓库里 `> [!NOTE]` 全部为空的原因）、
  `div.copyright` 丢弃、`div.codesample` 里的 `table>tr>td>pre` 拍平成一个代码围栏
  （每个 `<pre>` 内部的换行按 `.replace('\\n', ' ')` 折成空格——这与旧仓库
  `qa/Accessing Image Metadata in iOS.md:26` 的字节完全一致）
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.parse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "meta"
STAGING = ROOT / ".staging"
OUT = STAGING / "archive-gap"                 # 产物：旧仓库的最终相对路径结构
CACHE = STAGING / "archive-gap-cache"         # 原始 HTML / book.json / 图片缓存
STATE = CACHE / "_state"                      # 抓取状态（断点续跑）
OLD_VAULT = Path("/Users/tommywu/Desktop/翻译/vault")   # 只读参照物

ARCHIVE_ROOT = "https://developer.apple.com/library/archive/"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
DELAY = 1.0          # 1 请求/秒，不并发
TIMEOUT = 40
MAX_PAGES_PER_DOC = 2000   # 巨型文档保护（旧仓库最大 1473 页）

# library.json 的 type_name → 旧仓库 frontmatter 的 resource_type。
# 旧仓库只出现过 4 种取值；Technical Notes 整类缺失，故新增 'Technical Note'（单数，
# 与既有 4 种的单数化规则一致）——这一条需要人工确认，已写进报告。
RESOURCE_TYPE = {
    "Technical Notes": "Technical Note",
    "Sample Code": "Sample Code",
    "Guides": "Guide",
    "Technical Q&As": "QA",
    "Release Notes": "Release Note",
    "Getting Started": "Guide",
    "Articles": "Guide",
    "Xcode Tasks": "Guide",
}

# frontmatter platform 的固定书写顺序（VAULT_FORMAT_SPEC §1.3）
PLATFORM_ORDER = ["watchOS", "tvOS", "iAd System JS", "Safari (Mobile)", "Safari",
                  "CloudKit JS", "iAd Producer", "Java", "iOS",
                  "Xcode Developer Tools", "macOS"]


# ---------------------------------------------------------------------------
# 基础工具
# ---------------------------------------------------------------------------

def sanitize(name: str) -> str:
    """标题 → 文件/目录名（VAULT_FORMAT_SPEC §2.4，2,291/2,311 命中）。"""
    s = re.sub(r"<[^>]*>", "", name)            # 1. 先剥 HTML 标签（<name>.app 会整段消失）
    s = re.sub(r"[_*#]", "", s)                 # 2. 删除 _ * #
    s = re.sub(r'[<>:"/\\|?\[\]]', "-", s)      # 3. 替换为 '-'
    s = re.sub(r"\s+", " ", s).strip()          # 4. 空白折叠
    s = s[:80]                                  # 5. 截断 80（在冲突后缀之前）
    s = s.rstrip(" .-")                         # 6. 去尾部空格/点/连字符
    return s


def anchor_of(apple_ref: str) -> str:
    """'//apple_ref/doc/uid/TP40012334-CH5-SW1' → 'apple-f4xwc4dq…'（§8.8）。"""
    b32 = base64.b32encode(apple_ref.encode()).decode().lower().rstrip("=")
    return "apple-" + b32


def quote_path(p: str) -> str:
    """内部链接 = urllib.parse.quote(相对路径)，默认 safe='/'（§9.2）。"""
    return urllib.parse.quote(p)


def camel_words(cid: str) -> str:
    """分类 id → 人类可读目录名（§2.2）。只在旧仓库索引没给出映射时兜底。"""
    if "_" in cid:
        return cid.replace("_", " ")
    if cid.islower() or cid.isupper():
        return cid
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", cid)
    s = re.sub(r"(?<=[A-Z0-9])(?=[A-Z][a-z])", " ", s)
    return s


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def canonical_url(url: str) -> str:
    """陷阱 2：裸目录返回 1,610 字节空壳，必须补 `_index.html`。锚点一律剥掉。"""
    url = url.split("#")[0]
    if url.endswith("/"):
        url += "_index.html"
    return url


def in_archive(url: str) -> bool:
    return url.startswith(ARCHIVE_ROOT)


# ---------------------------------------------------------------------------
# 抓取（1 请求/秒、磁盘缓存、断点续跑）
# ---------------------------------------------------------------------------

class Fetcher:
    def __init__(self, delay: float = DELAY):
        self.s = requests.Session()
        self.s.headers["User-Agent"] = UA
        self.delay = delay
        self.last = 0.0
        self.n_net = 0
        STATE.mkdir(parents=True, exist_ok=True)
        self.index_path = STATE / "fetch_index.json"
        self.index = json.loads(self.index_path.read_text()) if self.index_path.exists() else {}

    # 缓存路径 = URL 在 /library/archive/ 之后的路径，原样落盘（保留大小写，陷阱 3）
    def cache_path(self, url: str) -> Path:
        rel = url[len(ARCHIVE_ROOT):] if in_archive(url) else "_external/" + re.sub(r"^https?://", "", url)
        rel = rel.split("?")[0]
        return CACHE / rel

    def get(self, url: str, binary: bool = False, kind: str = "html"):
        """返回 (ok, text_or_bytes, info)。已缓存的不重抓。

        `kind='json'` 走 JSON 校验——book.json 不是 HTML，若拿 `<article` 去卡它会
        永远判失败，进而让所有多页文档静默退化成 nextLink 链式遍历。
        """
        cp = self.cache_path(url)
        info = self.index.get(url)
        if cp.exists() and info is not None:
            data = cp.read_bytes()
            return info.get("ok", False), (data if binary else data.decode("utf-8", "replace")), info
        # 限速
        dt = time.time() - self.last
        if dt < self.delay:
            time.sleep(self.delay - dt)
        self.last = time.time()
        self.n_net += 1
        try:
            r = self.s.get(url, timeout=TIMEOUT, allow_redirects=True)
        except Exception as e:                              # 单页失败不拖垮整批
            info = {"status": 0, "error": str(e)[:200], "final": url, "ok": False}
            self.index[url] = info
            return False, b"" if binary else "", info
        body = r.content
        text = "" if binary else body.decode(r.apparent_encoding or "utf-8", "replace")
        info = {"status": r.status_code, "final": r.url, "size": len(body),
                "ctype": r.headers.get("Content-Type", ""), "ok": False}
        if binary:
            info["ok"] = r.status_code == 200 and len(body) > 0
        elif kind == "json":
            try:
                json.loads(text)
                info["ok"] = r.status_code == 200
            except Exception:
                info["ok"], info["why"] = False, "bad-json"
        else:
            info["ok"], info["why"] = page_is_good(r.status_code, text)
        self.index[url] = info
        if info["ok"]:
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_bytes(body)
        return info["ok"], (body if binary else text), info

    def save(self):
        self.index_path.write_text(json.dumps(self.index, ensure_ascii=False, indent=0))


def page_is_good(status: int, html: str):
    """陷阱 1 的双重校验：状态码 200 **且** 有正文容器 **且** 标题不是 404。

    Apple 的 404 页有 82,981 字节，比大多数真实归档页还大，只看体积必然误判。
    正文容器有两代：DTS 模板是 `<article id="contents">`，新一点的 jazz 模板
    （featuredarticles / 部分 documentation）是 `<article class="chapter">`。
    """
    if status != 200:
        return False, f"http{status}"
    if "Page Not Found" in html[:4000]:
        return False, "notfound-title"
    if "<article" not in html:
        return False, "no-article"
    return True, "ok"


# ---------------------------------------------------------------------------
# HTML 解析
# ---------------------------------------------------------------------------

def soup_of(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")


def head_meta(soup) -> dict:
    d = {}
    for m in soup.find_all("meta"):
        k = m.get("id") or m.get("name")
        if k:
            d[k] = m.get("content", "")
    return d


def article_of(soup):
    """正文容器：DTS 模板 `article#contents`；jazz 模板 `article.chapter/.appendix/…`。"""
    return soup.find("article", id="contents") or soup.find("article")


def page_title_of(art) -> str | None:
    """页面自身标题：只认 `h1#pageTitle`。

    旧仓库对 legacy 页（`div#pagehead` + `div#pageheadsub`）**没有**取标题，而是回落
    成 HTML 文件 stem（证据：`qa/hw/A SCSI little secret/hw81.md` 的页名是 `hw81`）。
    这里保持同样行为，否则文件名会与旧仓库同类文档不一致。
    """
    if art is None:
        return None
    h = art.find(id="pageTitle")
    if h is None:
        return None
    t = re.sub(r"\s+", " ", h.get_text()).strip()
    return t or None


def book_pages(fetcher: Fetcher, entry_url: str, meta: dict):
    """用 book.json 发现多页文档的全部页面（陷阱 4：按 `#` 前路径去重）。"""
    bj = meta.get("book-json")
    if not bj:
        return None
    root = meta.get("book-root") or "./"
    base = urllib.parse.urljoin(entry_url, root)
    ok, text, _ = fetcher.get(urllib.parse.urljoin(base, bj), kind="json")
    if not ok:
        # book.json 请求本身也可能被 301 带走（已迁移文档），或干脆不存在
        return None
    try:
        data = json.loads(text)
    except Exception:
        return None
    urls, seen = [], set()

    def walk(sections):
        for sec in sections or []:
            href = (sec.get("href") or "").split("#")[0]      # ← 去重的关键：只看 # 前的路径
            if href:
                u = canonical_url(urllib.parse.urljoin(base, href))
                if u not in seen:
                    seen.add(u)
                    urls.append(u)
            walk(sec.get("sections"))

    walk(data.get("sections"))
    return urls or None


def next_prev(art):
    """`article#contents` 内的 a.nextLink / a.prevLink（`<link id="next-page">` 常为空，不可靠）。"""
    if art is None:
        return None, None
    nxt = art.select_one("a.nextLink")
    prv = art.select_one("a.previousLink") or art.select_one("a.prevLink")
    return (nxt.get("href") if nxt else None), (prv.get("href") if prv else None)


def follow_chain(fetcher: Fetcher, entry_url: str, first_art):
    """book.json 缺失时的兜底：顺着 a.nextLink 链式遍历。"""
    urls = [entry_url]
    seen = {entry_url}
    url, art = entry_url, first_art
    while len(urls) < MAX_PAGES_PER_DOC:
        nxt, _ = next_prev(art)
        if not nxt:
            break
        u = canonical_url(urllib.parse.urljoin(url, nxt))
        if u in seen or not in_archive(u):
            break
        ok, html, _ = fetcher.get(u)
        if not ok:
            break
        seen.add(u)
        urls.append(u)
        url, art = u, article_of(soup_of(html))
    return urls


# ---------------------------------------------------------------------------
# markdownify 复刻层
# ---------------------------------------------------------------------------

CODE_LANG_RULES = [
    ("objc",  re.compile(r"^\s*(@(interface|implementation|end|property|autoreleasepool)\b"
                         r"|#import\b|[-+]\s*\([A-Za-z])", re.M)),
    ("swift", re.compile(r"^\s*(import (UIKit|Foundation|SwiftUI|SpriteKit|SceneKit)\b"
                         r"|(public |private |internal )?(func|class|struct|enum|extension) \w+)", re.M)),
    ("c",     re.compile(r"^\s*(#include\b|typedef\s|static\s+\w+\s+\w+\s*\()", re.M)),
    ("xml",   re.compile(r"^\s*(<\?xml|<!DOCTYPE plist)", re.M)),
    ("shell", re.compile(r"^\s*(#!\s*/bin/(ba)?sh|\$ \w)", re.M)),
]


def guess_lang(code: str) -> str:
    """代码块语言标注。

    旧仓库的取值集合（objc/c/swift/xml/shell/json/text/bash/sh/perl）与"同一扩展名在不同
    文档标注不同"的事实说明它来自**内容启发式**而非扩展名映射，且大多数块（63,882/近 8 万）
    根本没有标注。规范 §12 #8 把这一项列为「存疑」。这里用行首锚定的保守启发式：
    只有明确匹配才标注，否则留空——与"多数不标注"的现状一致。
    """
    for lang, rx in CODE_LANG_RULES:
        if rx.search(code):
            return lang
    return ""


class VaultConverter(MarkdownConverter):
    """与旧仓库产物对齐的 markdownify 子类。

    这些选项不是猜的，每一条都有旧仓库里的字节级对照：
    * `table_infer_header=False` → 无表头的表会补 `|  |` + `| --- |` 两行**在数据行之前**
      （`qa/hw/A SCSI little secret/hw81.md:17-19`、`samplecode/DateCell/DateCell.md:18-19`）；
      若设 True，markdownify 会改成把数据行当表头 + 分隔行放其后，与旧仓库相反。
    * `convert_div` 透明 → `<div id="pagehead">A</div><div id="pageheadsub">B</div>` 在旧仓库里
      拼成 `AB`（hw81.md:19 `Technical Q&A HW81A SCSI little secret`，中间一个空格都没有）。
    """

    class Options(MarkdownConverter.DefaultOptions):
        heading_style = "ATX"          # 旧仓库全部是 `# ` 而不是 setext
        strong_em_symbol = "_"         # `__bold__` / `_italic_`（§8.6）
        bullets = "-"                  # 无序列表一律 `- `（§8.5）
        escape_asterisks = True        # 字面星号会被转义成 `\*`（§8.6）
        escape_underscores = False     # 但下划线不转义（全库只有 11 个文件含 `\_`）
        escape_misc = False            # `&` 裸写，`Q&A` 不转义
        table_infer_header = False
        autolinks = False              # 旧仓库写 `[http://x](http://x)` 而不是 `<http://x>`
        # 代码块语言标注：由 flatten_codesamples() 塞进 data-lang
        code_language_callback = staticmethod(lambda el: el.get("data-lang") or "")

    def convert_div(self, el, text, parent_tags):
        return text

    convert_article = convert_div
    convert_section = convert_div

    # 术语表 `<dl class="termdef">`：旧仓库写成 `**__术语__**` + 下一行 `: 释义`，
    # 且续段落**不缩进**（`documentation/Security/Secure Coding Guide/…:185-188`）。
    # markdownify 1.1.0 自带的 convert_dd 会缩进 4 空格、convert_dt 不加 `**`，都不一致。
    def convert_dt(self, el, text, parent_tags):
        text = re.sub(r"\s+", " ", (text or "").strip())
        if "_inline" in parent_tags:
            return " " + text + " "
        return ("\n\n**%s**\n" % text) if text else "\n"

    def convert_dd(self, el, text, parent_tags):
        text = (text or "").strip()
        if "_inline" in parent_tags:
            return " " + text + " "
        return (": %s\n" % text) if text else "\n"


def flatten_codesamples(art):
    """把 Apple 的 `div.codesample > table > tr > td > pre` 拍平成一个 `<pre>`。

    两个必须同时满足的观察（否则和旧仓库对不上）：
    * samplecode 的 Listings 页每一行源码是**独立的 `<tr><td><pre>`**，旧仓库把它们按
      `\\n` 拼回一个代码块且保留行首缩进（`samplecode/DateCell/main.m.md:19+`）；
    * qa/technote 的代码是**一个多行 `<pre>`**，旧仓库把其中的换行折成了空格
      （`qa/Accessing Image Metadata in iOS.md:26`，`info {` 后正好 6 个空格 =
      2 个换行各折 1 个空格 + 原有 4 个缩进）。
    两者的唯一自洽解释就是逐 `<pre>` 做 `.replace('\\n', ' ')` 再用 `\\n` 连接。
    """
    for div in art.select("div.codesample"):
        pres = div.find_all("pre")
        if not pres:
            continue
        code = "\n".join(p.get_text().replace("\n", " ") for p in pres)
        code = code.rstrip()
        if not code.strip():
            div.decompose()
            continue
        new = BeautifulSoup("<pre></pre>", "html.parser").pre
        new.string = code
        new["data-lang"] = guess_lang(code)
        div.replace_with(new)


RETIRED_BOILERPLATE = re.compile(r"no longer being updated|Retired Document|is deprecated and")


def preprocess(art, page_url: str, url_map: dict, rel_self: str, doc_has_dir: bool,
               faithful: bool = False):
    """转换前的 DOM 清理与链接改写。

    `faithful=True` 完全复刻旧仓库转换器的行为（calibrate 用它做逐行比对）；
    `faithful=False`（生产默认）有**两处刻意偏离**，理由见报告：

      A. 旧仓库把 `<aside>` 整棵子树丢弃 —— 这正是它 464 个 `> [!NOTE]` 全部为空
         （规范 §12 #14「已知内容丢失，不复现」）、`div.notebox` 正文全部消失的原因。
         生产模式只丢「本文档不再更新」这类站点样板，保留 Note/Important 正文；
         产出形态是 `__Note:__ …` 段落，这在旧仓库里本来就有 260+ 处，不显得异常。
      B. 旧仓库把 `h2.jump` / `h3.jump` 小标题整个丢掉（证据：
         `documentation/Security/Secure Coding Guide/` 的 14 页里 12 页全文只剩 1 个标题，
         而源 HTML 有 7 个 h2.jump + 若干 h3.jump）。DTS 模板的技术笔记全靠这些标题分节，
         照抄会让 424 份现代 technote 变成没有层级的大段文字，所以生产模式保留它们。
    """
    # 1) aside / 脚本 / 样式
    for t in art.find_all(["script", "style", "noscript"]):
        t.decompose()
    for t in art.find_all("aside"):
        if faithful or RETIRED_BOILERPLATE.search(t.get_text()[:200]):
            t.decompose()
        else:
            for ttl in t.select("p.aside-title"):
                ttl.decompose()          # jazz 模板的 "Note" 标题行，marker 已单独生成
            t.unwrap()
    if faithful:
        for h in art.select("h1.jump, h2.jump, h3.jump, h4.jump, h5.jump"):
            h.decompose()
    # 2) 页脚版权块丢弃（旧仓库产物里没有）
    for t in art.select("div.copyright"):
        t.decompose()
    # 3) 模板自带的上一页/下一页导航条丢弃——翻页行由模板统一生成，避免重复
    for t in art.select("div.pageNavigationLinks"):
        t.decompose()
    # 3b) jazz 模板的 admonition：`<div class="note">` → GitHub alert 引用块。
    #     旧仓库里这些 alert **全是空的**（464 个标记 0 条正文），因为内容在被丢弃的
    #     `<aside>` 里；这里保持同样形态，见报告里的「已知内容损失」一节。
    for cls, mark in (("note", "NOTE"), ("important", "IMPORTANT"),
                      ("warning", "WARNING"), ("tip", "TIP")):
        for t in art.select(f"div.{cls}"):
            bq = BeautifulSoup(f"<blockquote><p>[!{mark}]</p></blockquote>", "html.parser").blockquote
            for child in list(t.children):
                bq.append(child.extract())
            t.replace_with(bq)
    # 3c) `<code>` 里套 `<a href>` 时，旧仓库保留链接、丢掉反引号
    #     （`…UsingSegues.md` 的 `[showViewController:sender:](…)`，而不是 `` `…` ``）
    for c in art.find_all(["code", "tt"]):
        if c.find("a", href=True):
            c.unwrap()
    # 4) 代码块拍平
    flatten_codesamples(art)
    # 5) 链接改写
    for a in art.find_all("a"):
        href = a.get("href")
        if not href:
            continue
        if href.startswith(("mailto:", "ftp:", "applescript:", "javascript:", "BugDB:")):
            continue
        absu = urllib.parse.urljoin(page_url, href)
        # 旧仓库把 developer.apple.com 的 http 链接统一升成 https
        # （hw81.md:15 `[ADC Home](https://developer.apple.com/)`，源 HTML 里是 http://）
        absu = re.sub(r"^http://developer\.apple\.com", "https://developer.apple.com", absu)
        base, _, frag = absu.partition("#")
        base = canonical_url(base)
        target = url_map.get(base)
        if target:
            # 同页锚点只留 `#apple-…`，不写自己的文件名（§9.1 有 41,923 处纯同页锚点）
            rel = "" if target == rel_self else quote_path(
                os.path.relpath(target, os.path.dirname(rel_self)))
            link = rel + ("#" + anchor_of(frag) if frag.startswith("//apple_ref/") else "")
            a["href"] = link or "#"
        else:
            a["href"] = absu
    # 6) 图片改写：`attachments/<原相对路径去掉 ../>`（§2.7）
    for img in art.find_all("img"):
        src = img.get("src") or ""
        if not src or src.startswith("data:"):
            continue
        if not img.get("alt"):
            img["alt"] = src            # 无 alt 时旧仓库用原始 src 当 alt（§8.9）
        rel = re.sub(r"^(\.\./)+", "", src.split("?")[0])
        img["src"] = quote_path(("attachments/" + rel) if doc_has_dir else rel)


def to_markdown(art) -> str:
    md = VaultConverter().convert(str(art))
    md = "\n".join(l.rstrip() for l in md.split("\n"))   # 行尾空白清掉（`<br>` 的 '  ' 也在内）
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip("\n")


# ---------------------------------------------------------------------------
# 旧仓库 URL → 路径映射（只读扫描，用于把链接改写成相对 .md）
# ---------------------------------------------------------------------------

def old_vault_map() -> dict:
    cache = STATE / "old_vault_urls.json"
    if cache.exists():
        return json.loads(cache.read_text())
    m = {}
    if OLD_VAULT.exists():
        for p in OLD_VAULT.rglob("*.md"):
            parts = p.relative_to(OLD_VAULT).parts
            if parts[0] in (".git", ".obsidian", "_indexes", "doc"):
                continue
            try:
                head = p.read_text(encoding="utf-8")[:1200]
            except Exception:
                continue
            if not head.startswith("---\n"):
                continue
            mm = re.search(r"^source_url: (\S+)$", head, re.M)
            if mm:
                m[canonical_url(mm.group(1))] = str(p.relative_to(OLD_VAULT))
    STATE.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(m, ensure_ascii=False))
    return m


def old_vault_paths():
    """旧仓库已占用的「文档目录」与「文件」路径（小写）。

    暂存区是要整体挪进旧仓库的，所以消歧必须把旧仓库已有的路径也算上，
    否则 `documentation/General/<同名文档>/` 会和既有目录撞车。
    """
    cache = STATE / "old_vault_paths.json"
    if cache.exists():
        d = json.loads(cache.read_text())
        return set(d["dirs"]), set(d["files"])
    dirs, files = set(), set()
    if OLD_VAULT.exists():
        for p in OLD_VAULT.rglob("*"):
            rel = p.relative_to(OLD_VAULT)
            if rel.parts and rel.parts[0] in (".git", ".obsidian", "_indexes", "doc"):
                continue
            if p.is_dir() and p.name != "attachments":
                dirs.add(str(rel).lower())
            elif p.suffix == ".md":
                files.add(str(rel).lower())
    STATE.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps({"dirs": sorted(dirs), "files": sorted(files)}))
    return dirs, files


def category_map() -> dict:
    """从旧仓库 `_indexes/<type>.md` 反解 分类 id → 目录名（§2.2 的权威来源）。"""
    cache = STATE / "category_map.json"
    if cache.exists():
        return json.loads(cache.read_text())
    m = {}
    idx = OLD_VAULT / "_indexes"
    if idx.exists():
        for f in idx.glob("*.md"):
            for name, path in re.findall(r"^## \[([^\]]+)\]\(([^)]+)\)", f.read_text(encoding="utf-8"), re.M):
                cid = Path(path).stem
                # 索引里的分类名有 1 个已被翻译成中文（`## [用户体验](documentation/UserExperience.md)`），
                # 而磁盘上的目录仍是英文 `documentation/User Experience/`。以**磁盘上真实存在的
                # 目录名**为准，索引名只作候选。
                for cand in (name, camel_words(cid)):
                    if (OLD_VAULT / f.stem / cand).is_dir():
                        m[f"{f.stem}/{cid}"] = cand
                        break
                else:
                    m[f"{f.stem}/{cid}"] = name
    STATE.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(m, ensure_ascii=False))
    return m


# ---------------------------------------------------------------------------
# 阶段 0：分类
# ---------------------------------------------------------------------------

def load_gap(types=None):
    docs = json.loads((META / "archive_gap.json").read_text())["documents"]
    out = []
    for d in docs:
        if d.get("url_already_in_vault"):
            continue                                  # 2 条别名，跳过
        if types and d["type_code"] not in types:
            continue
        out.append(d)
    return out


def cmd_classify(args):
    docs = load_gap(args.types)
    f = Fetcher()
    state_path = STATE / "classify.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    n = 0
    for d in docs:
        aid = d["apple_id"]
        if aid in state:
            continue
        url = canonical_url(d["url"])
        if not in_archive(url):
            state[aid] = {"class": "offsite", "url": d["url"]}
            continue
        ok, html, info = f.get(url)
        final = info.get("final", url)
        if not in_archive(canonical_url(final)):
            cls = "migrated"                          # 301 → 现行 /documentation/，本次不抓
        elif ok:
            cls = "ok"
        else:
            cls = "dead"
        state[aid] = {"class": cls, "url": url, "final": final,
                      "status": info.get("status"), "size": info.get("size"),
                      "why": info.get("why", info.get("error", ""))}
        n += 1
        if n % 20 == 0:
            state_path.write_text(json.dumps(state, ensure_ascii=False, indent=1))
            f.save()
            print(f"  classify {n} … net={f.n_net}", flush=True)
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=1))
    f.save()
    print(Counter(v["class"] for v in state.values()))


# ---------------------------------------------------------------------------
# 阶段 1：抓页面
# ---------------------------------------------------------------------------

def cmd_fetch(args):
    docs = load_gap(args.types)
    cls = json.loads((STATE / "classify.json").read_text()) if (STATE / "classify.json").exists() else {}
    f = Fetcher()
    pages_path = STATE / "pages.json"
    pages = json.loads(pages_path.read_text()) if pages_path.exists() else {}
    todo = [d for d in docs if cls.get(d["apple_id"], {}).get("class") == "ok"
            and d["apple_id"] not in pages]
    if args.limit:
        todo = todo[:args.limit]
    print(f"待抓 {len(todo)} 份文档")
    for i, d in enumerate(todo, 1):
        aid = d["apple_id"]
        entry = canonical_url(d["url"])
        try:
            ok, html, _ = f.get(entry)
            if not ok:
                pages[aid] = {"error": "entry-bad", "urls": []}
                continue
            s = soup_of(html)
            meta = head_meta(s)
            urls = book_pages(f, entry, meta)
            if not urls:
                urls = follow_chain(f, entry, article_of(s))
            if entry not in urls:                      # book.json 偶尔漏掉落地页
                urls = [entry] + [u for u in urls if u != entry]
            urls = urls[:MAX_PAGES_PER_DOC]
            good = []
            for u in urls:
                ok2, _h, _i = f.get(u)
                if ok2:
                    good.append(u)
            pages[aid] = {"entry": entry, "urls": good, "bad": len(urls) - len(good)}
        except Exception as e:                          # 单份失败不拖垮整批
            pages[aid] = {"error": repr(e)[:200], "urls": []}
        if i % 10 == 0 or i == len(todo):
            pages_path.write_text(json.dumps(pages, ensure_ascii=False))
            f.save()
            done = sum(len(v.get("urls", [])) for v in pages.values())
            print(f"  [{i}/{len(todo)}] {aid} 累计页 {done} net={f.n_net}", flush=True)
    pages_path.write_text(json.dumps(pages, ensure_ascii=False))
    f.save()


# ---------------------------------------------------------------------------
# 阶段 3：渲染
# ---------------------------------------------------------------------------

CATEGORY_TOPS = ("documentation", "qa", "releasenotes", "referencelibrary", "technotes")


def top_and_category(entry_url: str, catmap: dict, occupancy: dict):
    """确定顶层目录与（可选的）分类层。

    分类层的判据是「URL 第二段是不是多份文档共用的目录」：
      qa/qa1622/_index.html    第二段 qa1622 只属这一份 → 无分类（旧仓库落在 `qa/<标题>.md`）
      qa/hw/hw81.html          第二段 hw 被上百份共用   → 分类 hw（旧仓库 `qa/hw/…`）
      technotes/tb/tb_15.html  同上，386 份 legacy 共用 → 分类 tb
      technotes/tn2413/…       只属这一份               → 无分类
      documentation/Security/Conceptual/SecureCodingGuide/… → 分类 Security（查旧仓库索引）
    `documentation` 这类"分类目录在旧仓库里已经存在、但本次缺口里只剩一两份"的情况，
    靠 occupancy 判不出来，所以先查旧仓库 `_indexes/<type>.md` 反解出来的权威映射表。
    """
    rel = entry_url[len(ARCHIVE_ROOT):]
    segs = rel.split("/")
    top = segs[0]
    if len(segs) < 3 or top not in CATEGORY_TOPS:
        return top, None                              # samplecode 等无分类层（§2.2）
    cid = segs[1]
    known = catmap.get(f"{top}/{cid}")
    if known:
        return top, known
    if occupancy.get(f"{top}/{cid}", 0) >= 2:
        return top, camel_words(cid)
    return top, None


def plan_doc(d, info, fetcher, catmap, occupancy):
    """决定这份文档的目录/文件布局。只读页标题，不保留 soup（避免上千份文档同时驻留内存）。"""
    urls = info["urls"]
    entry = info.get("entry") or urls[0]
    top, cat = top_and_category(entry, catmap, occupancy)
    base = top + ("/" + cat if cat else "")
    doc_name = sanitize(d["name"])                     # 目录名取自导航索引的文档名（§12 #15）

    names, kept, has_img = [], [], False
    used = {}
    for u in urls:
        ok, h, _ = fetcher.get(u)
        if not ok:
            continue
        art = article_of(soup_of(h))
        t = page_title_of(art)
        if not has_img and art is not None and art.find("img"):
            has_img = True
        stem = Path(urllib.parse.urlparse(u).path).stem
        nm = sanitize(t) if t else stem                # 抽不到 h1#pageTitle 就回落 HTML stem
        if not nm:
            nm = stem
        k = nm.lower()
        used[k] = used.get(k, 0) + 1
        if used[k] > 1:
            nm = f"{nm}-{used[k]}"                     # 同目录同名冲突：-2、-3…
        names.append(nm)
        kept.append(u)
    if not kept:
        return None

    need_dir = len(kept) > 1 or has_img or (names[0] != doc_name)
    doc_dir = f"{base}/{doc_name}" if need_dir else base
    rels = [f"{doc_dir}/{n}.md" for n in names]
    return dict(top=top, cat=cat, doc_dir=doc_dir, need_dir=need_dir,
                rels=rels, urls=kept)


def dedupe(plan, taken_dirs, taken_files):
    """跨文档的同名消歧：追加 `-2`、`-3`…（§2.4）。

    810 份 Technical Notes 里绝大多数是单页、全落在同一层目录，跨文档重名是必然的；
    截断到 80 字符发生在加后缀**之前**，所以带后缀时文件名可达 82 字符。
    """
    if plan["need_dir"]:
        base, d, n = plan["doc_dir"], plan["doc_dir"], 1
        while d.lower() in taken_dirs:
            n += 1
            d = f"{base}-{n}"
        taken_dirs.add(d.lower())
        plan["doc_dir"] = d
        plan["rels"] = [f"{d}/{Path(r).name}" for r in plan["rels"]]
    else:
        r = plan["rels"][0]
        stem, n, rr = r[:-3], 1, r
        while rr.lower() in taken_files:
            n += 1
            rr = f"{stem}-{n}.md"
        plan["rels"] = [rr]
    for r in plan["rels"]:
        taken_files.add(r.lower())
    return plan


def frontmatter(d, page_url) -> str:
    plats = [p for p in d["platform"].split("|") if p]
    plats.sort(key=lambda p: PLATFORM_ORDER.index(p) if p in PLATFORM_ORDER else 99)
    fm = {
        "title": d["name"],
        "apple_id": d["apple_id"],
        "resource_type": RESOURCE_TYPE.get(d["type_name"], "Guide"),
        "platform": "|".join(plats),
        "topic": d.get("topic") or None,
        "technology": d.get("framework") or None,
        "published": d.get("published") or "",
        "source_url": page_url,
        "archived_at": utcnow(),
    }
    body = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=80,
                          default_flow_style=False)
    return "---\n" + body + "---\n"


def nav_line(rel: str, top: str, doc_title: str, entry_name: str | None) -> str:
    depth = rel.count("/")
    up = "../" * depth
    s = f"> 导航：[总目录]({up}README.md) · [{top}]({up}_indexes/{top}.md)"
    if entry_name:                                     # 入口页只有 2 段（§4.4）
        s += f" · [{doc_title}]({quote_path(entry_name)})"
    return s


def pager_line(nxt: str | None, prv: str | None) -> str:
    """`[Next](…)[Previous](…)`，两个链接紧贴、无分隔符、Next 在前（§5.2）。"""
    s = ""
    if nxt:
        s += f"[Next]({nxt})"
    if prv:
        s += f"[Previous]({prv})"
    return s


def cmd_render(args):
    docs = {d["apple_id"]: d for d in load_gap(args.types)}
    pages = json.loads((STATE / "pages.json").read_text())
    catmap = category_map()
    url_map = dict(old_vault_map())
    f = Fetcher()

    # 全部缺口文档的入口 URL 目录占用数——用于判定「第二段是不是共用分类目录」
    occupancy = {}
    for d in load_gap(None):
        u = canonical_url(d["url"])
        if in_archive(u):
            segs = u[len(ARCHIVE_ROOT):].split("/")
            if len(segs) >= 3:
                occupancy["/".join(segs[:2])] = occupancy.get("/".join(segs[:2]), 0) + 1

    # 第一遍：规划全部路径（链接改写需要全局 URL→路径表）
    plans = {}
    taken_dirs, taken_files = old_vault_paths()      # 连旧仓库已占用的路径一起避让
    for aid in sorted(pages):                      # 固定顺序，保证 -2/-3 后缀可复现
        info = pages[aid]
        if aid not in docs or not info.get("urls"):
            continue
        try:
            p = plan_doc(docs[aid], info, f, catmap, occupancy)
        except Exception as e:
            print("plan fail", aid, repr(e)[:120]); continue
        if not p:
            continue
        p = dedupe(p, taken_dirs, taken_files)
        plans[aid] = p
        for u, rel in zip(p["urls"], p["rels"]):
            url_map[u] = rel

    # 第二遍：渲染
    n_pages = 0
    for aid, p in plans.items():
        d = docs[aid]
        entry_rel = p["rels"][0]
        entry_name = Path(entry_rel).name
        for i, (u, rel) in enumerate(zip(p["urls"], p["rels"])):
            try:
                ok, html, _ = f.get(u)
                if not ok:
                    continue
                art = article_of(soup_of(html))
                preprocess(art, u, url_map, rel, p["need_dir"])
                body = to_markdown(art)
                nxt = prv = None
                if len(p["rels"]) > 1:
                    if i + 1 < len(p["rels"]):
                        nxt = quote_path(os.path.relpath(p["rels"][i + 1], os.path.dirname(rel)))
                    if i > 0:
                        prv = quote_path(os.path.relpath(p["rels"][i - 1], os.path.dirname(rel)))
                # qa / releasenotes 类在旧仓库没有模板翻页行（§5.3）
                if p["top"] in ("qa", "technotes", "releasenotes"):
                    nxt = prv = None
                pager = pager_line(nxt, prv)
                nav = nav_line(rel, p["top"], d["name"], None if i == 0 else entry_name)
                head = frontmatter(d, u) + nav + "\n\n\n"
                if pager:
                    text = head + pager + "\n\n" + body + "\n\n" + pager + "\n\n"
                else:
                    tail = "\n\n" if body.rsplit("\n", 1)[-1].startswith("|") else "\n"
                    text = head + "\n" + body + tail
                out = OUT / rel
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text(text, encoding="utf-8")
                n_pages += 1
            except Exception as e:
                print("render fail", aid, u, repr(e)[:150])
    # 注意：render 不调用 f.save()——它只读缓存，回写会和后台正在跑的 fetch 抢同一个索引文件
    (STATE / "plans.json").write_text(json.dumps(
        {k: {"rels": v["rels"], "urls": v["urls"], "top": v["top"]} for k, v in plans.items()},
        ensure_ascii=False))
    print(f"渲染完成：{len(plans)} 份文档 / {n_pages} 页 → {OUT}")


# ---------------------------------------------------------------------------
# 阶段 2：插图
# ---------------------------------------------------------------------------

# legacy 页面的界面装饰图（不是正文插图，实测在 798 份 technote 里被引用 2,000+ 次，
# 而真正的插图是 `tnNNNN_NNN.gif` 这种带文档号的文件名）。侦察报告 §7 也点名要过滤。
DECOR_IMAGES = {
    "tnmenutop.gif", "tnmenubottom.gif", "tnmenubody.gif", "acrobatsmall.gif",
    "arrow_linkup.gif", "1dot.gif", "bluebook.gif", "redbook.gif",
    "mtop600.gif", "mbot600.gif", "closebutton.png", "spacer.gif", "blank.gif",
}


def cmd_assets(args):
    plans = json.loads((STATE / "plans.json").read_text())
    f = Fetcher()
    n = 0
    for aid, p in plans.items():
        for u, rel in zip(p["urls"], p["rels"]):
            ok, html, _ = f.get(u)
            if not ok:
                continue
            art = article_of(soup_of(html))
            if art is None:
                continue
            for img in art.find_all("img"):
                src = (img.get("src") or "").split("?")[0]
                if not src or src.startswith("data:"):
                    continue
                absu = urllib.parse.urljoin(u, src)
                if not in_archive(absu) or "/Resources/" in absu:
                    continue
                if absu.rsplit("/", 1)[-1].lower() in DECOR_IMAGES:
                    continue
                sub = re.sub(r"^(\.\./)+", "", src)
                dest = OUT / os.path.dirname(rel) / "attachments" / sub
                if dest.exists():
                    continue
                ok2, data, _i = f.get(absu, binary=True)
                if ok2 and data:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(data)
                    n += 1
                    if n % 25 == 0:
                        f.save(); print(f"  图片 {n} …", flush=True)
    f.save()
    print(f"下载插图 {n} 张")


# ---------------------------------------------------------------------------
# 自检与标定
# ---------------------------------------------------------------------------

FM_KEYS = ["title", "apple_id", "resource_type", "platform", "topic",
           "technology", "published", "source_url", "archived_at"]


def cmd_selftest(args):
    bad_404, bad_fm, bad_shell, small, bad_nav = [], [], [], [], []
    nav_segs = Counter()
    per_doc = {}
    files = sorted(OUT.rglob("*.md"))
    for p in files:
        s = p.read_text(encoding="utf-8")
        rel = str(p.relative_to(OUT))
        if not s.startswith("---\n"):
            bad_fm.append((rel, "no-frontmatter")); continue
        fm_txt, _, rest = s[4:].partition("\n---\n")
        keys = re.findall(r"^([a-z_]+):", fm_txt, re.M)
        if keys != FM_KEYS:
            bad_fm.append((rel, ",".join(keys)))
        nav = rest.split("\n", 1)[0]
        body = rest.split("\n", 1)[1] if "\n" in rest else ""
        # 导航行：`../` 层数必须等于路径中的目录层数，第二段标签必须是顶层目录名（§4.2/§4.3）
        m = re.match(r"> 导航：\[总目录\]\(((?:\.\./)*)README\.md\) · \[([^\]]+)\]", nav)
        if not m:
            bad_nav.append((rel, nav[:60]))
        else:
            if m.group(1).count("../") != rel.count("/"):
                bad_nav.append((rel, f"depth {m.group(1).count('../')} != {rel.count('/')}"))
            elif m.group(2) != rel.split("/")[0]:
                bad_nav.append((rel, f"label {m.group(2)}"))
            nav_segs[nav.count(" · ") + 1] += 1
        if re.search(r"Page Not Found|The page you.re looking for", body):
            bad_404.append(rel)
        if len(body.strip()) < 200:
            small.append((rel, len(body.strip())))
        aid = re.search(r"^apple_id: (.*)$", fm_txt, re.M)
        if aid:
            per_doc.setdefault(aid.group(1), []).append(rel)
    import statistics
    counts = sorted((len(v) for v in per_doc.values()))
    print(f"页面 {len(files)} 个 / 文档 {len(per_doc)} 份")
    print(f"frontmatter 9 键齐全且顺序正确：{len(files)-len(bad_fm)}/{len(files)}")
    for r in bad_fm[:10]:
        print("   ✗", r)
    print(f"导航行合规（层数+顶层标签）：{len(files)-len(bad_nav)}/{len(files)}；段数分布 {dict(nav_segs)}")
    for r in bad_nav[:8]:
        print("   ✗", r)
    print(f"正文含 404 特征：{len(bad_404)}")
    for r in bad_404[:10]:
        print("   ✗", r)
    print(f"正文 <200 字符（疑似空壳）：{len(small)}")
    for r in small[:10]:
        print("   ✗", r)
    if counts:
        print(f"每份文档页数：min={counts[0]} median={statistics.median(counts)} "
              f"mean={sum(counts)/len(counts):.2f} max={counts[-1]}")
        top = sorted(per_doc.items(), key=lambda kv: -len(kv[1]))[:5]
        for aid, v in top:
            print(f"   最多页：{aid} {len(v)} 页  {v[0]}")

    # 分类结果
    cp = STATE / "classify.json"
    if cp.exists():
        cls = json.loads(cp.read_text())
        print("分类：", dict(Counter(v["class"] for v in cls.values())))

    # 陷阱 2 的复查：抓下来的 HTML 里有没有 1,610 字节量级的空壳
    fi = STATE / "fetch_index.json"
    if fi.exists():
        idx = json.loads(fi.read_text())
        shells = [u for u, v in idx.items()
                  if v.get("ok") and u.endswith(".html") and 0 < (v.get("size") or 0) < 3000]
        print(f"疑似空壳页（HTML <3000 字节且判定成功）：{len(shells)}")
        for u in shells[:8]:
            print("   ?", u, idx[u]["size"])
        bad = Counter(v.get("why") or str(v.get("status")) for v in idx.values() if not v.get("ok"))
        print("抓取失败原因：", dict(bad))

    # 顶层目录分布 + 文件尾换行分布
    tops = Counter(r.split("/")[0] for r in (str(p.relative_to(OUT)) for p in files))
    print("顶层目录：", dict(tops))
    tails = Counter()
    for p in files:
        s = p.read_text(encoding="utf-8")
        tails[len(s) - len(s.rstrip("\n"))] += 1
    print("文件尾换行数：", dict(tails))


CALIBRATION = [
    # (旧仓库 md 路径, 说明)
    ("qa/Accessing Image Metadata in iOS.md", "现代 QA 单页（technote 同模板）"),
    ("qa/How to pause the animation of a layer tree.md", "现代 QA + 代码块"),
    ("qa/hw/A SCSI little secret/hw81.md", "legacy 表格排版（legacy technote 同模板）"),
    ("documentation/Security/Secure Coding Guide/Race Conditions and Secure File Operations.md",
     "多页 Guide + notebox/noteboxdef"),
    ("featuredarticles/View Controller Programming Guide for iOS/UsingSegues.md",
     "现代 Guide + figure/table/note"),
    ("samplecode/DateCell/main.m.md", "samplecode 源码页"),
    ("samplecode/DateCell/DateCell.md", "samplecode 入口页 + 规格表"),
]


def cmd_calibrate(args):
    """拿旧仓库现有文档的源 HTML 重跑本转换器，逐行 diff。这是格式一致性的硬证据。"""
    import difflib
    f = Fetcher()
    url_map = old_vault_map()
    tot = 0.0
    for relmd, why in CALIBRATION:
        p = OLD_VAULT / relmd
        if not p.exists():
            print("missing", relmd); continue
        s = p.read_text(encoding="utf-8")
        src = re.search(r"^source_url: (\S+)$", s, re.M).group(1)
        ok, html, _ = f.get(canonical_url(src))
        if not ok:
            print("fetch fail", src); continue
        sp = soup_of(html)
        art = article_of(sp)
        need_dir = relmd.count("/") >= (2 if relmd.startswith(("documentation/", "qa/hw")) else 1)
        preprocess(art, src, url_map, relmd, need_dir, faithful=True)
        mine = to_markdown(art)
        want = s.split("\n---\n", 1)[1]
        want = want.split("\n", 1)[1].strip("\n")      # 去掉导航行
        want = re.sub(r"^(\[(Next|Previous)\]\([^)]*\))+\s*", "", want).strip("\n")
        want = re.sub(r"\n\[(Next|Previous)\]\([^)]*\)(\[(Next|Previous)\]\([^)]*\))?\s*$", "", want).strip("\n")
        a, b = want.split("\n"), mine.split("\n")
        r = difflib.SequenceMatcher(None, a, b).ratio()
        tot += r
        print(f"{r:6.3f}  {relmd}   （{why}）")
        if args.verbose:
            for l in difflib.unified_diff(a, b, "vault", "mine", lineterm="", n=1):
                print("      " + l[:200])
    f.save()
    print(f"平均行级相似度 {tot/len(CALIBRATION):.3f}")


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in [("classify", cmd_classify), ("fetch", cmd_fetch), ("assets", cmd_assets),
                     ("render", cmd_render), ("selftest", cmd_selftest), ("calibrate", cmd_calibrate)]:
        p = sub.add_parser(name)
        p.add_argument("--types", type=lambda s: {int(x) for x in s.split(",")}, default=None,
                       help="library.json type_code，如 2=Technical Notes,5=Sample Code,3=Guides")
        p.add_argument("--limit", type=int, default=0)
        p.add_argument("-v", "--verbose", action="store_true")
        p.set_defaults(func=fn)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
