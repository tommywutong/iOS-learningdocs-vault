#!/usr/bin/env python3
"""逐篇快照：学习计划里点名的「平台单篇 + 单次引用小站」文章。

    python3 tools/snapshot.py targets    # 从学习计划算出目标 URL → meta/snapshot_targets.json
    python3 tools/snapshot.py robots     # 逐域名查 robots.txt → .cache/snapshots/robots.json
    python3 tools/snapshot.py fetch      # 抓 HTML → .cache/snapshots/<域名>/<hash>.html
    python3 tools/snapshot.py retry      # 只重试上一轮失败的（跟 meta refresh、换 scheme）
    python3 tools/snapshot.py retry --browser-ua   # 同上，但换成不带自定义 token 的普通浏览器 UA
    python3 tools/snapshot.py probe      # 对已缓存的页面离线探正文容器（不发请求）
    python3 tools/snapshot.py render     # HTML → blogs/snapshots/<域名>/<slug>.md
    python3 tools/snapshot.py audit      # 体检：短正文 / 反爬页 / 中文字符数（打屏）
    python3 tools/snapshot.py report     # 把体检结果写成 meta/SNAPSHOT_REPORT.md

## 为什么这些不走 tools/blog.py 的整站流程

`meta/recon/CHINESE_SOURCES.md` 的结论：CSDN / 简书 / 博客园上同一篇 Runtime 文章
有几十个逐字雷同的版本，整站抓等于把垃圾一起抓进来；而 61 个只被引用一次的小站，
为一篇文章配一套抓取规则不划算。但这批文章是用户自己点名要读的，值得逐个存下来。

## 容器策略

平台的正文容器结构固定，按域名写死在 `CONTAINERS` 里；小站一站一篇，先用
`CONTAINERS` 里已知的，探不到就走 `guess_container()` 的启发式兜底；再探不到就
**记为失败写进报告**，绝不硬塞一个错容器导致正文丢失。
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import re
import sys
import urllib.parse
from datetime import datetime
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from blog import parse_html, robots_allows, slugify  # noqa: E402
from html2md import node_to_markdown  # noqa: E402
from studyplan import build_blog_index, build_wwdc_index, classify, parse_plan  # noqa: E402

CACHE = ROOT / ".cache" / "snapshots"
OUTDIR = ROOT / "blogs" / "snapshots"
TARGETS = ROOT / "meta" / "snapshot_targets.json"
ROBOTS = CACHE / "robots.json"
INDEX = ROOT / "meta" / "snapshot_index.json"
REPORT = ROOT / "meta" / "SNAPSHOT_REPORT.md"

DELAY = 2.0  # 别人的个人博客和平台，每个请求间隔 2 秒
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 personal-archive/0.1")
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

PLATFORMS = {
    "blog.csdn.net", "jianshu.com", "cnblogs.com", "zhuanlan.zhihu.com", "juejin.cn",
    "segmentfault.com", "cloud.tencent.com", "cloud.tencent.cn", "medium.com",
    "mp.weixin.qq.com", "bbs.huaweicloud.com", "baijiahao.baidu.com",
}

# 域名 → (正文容器 XPath, 容器内要剔掉的样板 XPath 列表)
# 平台的结构固定；小站是 probe 之后逐个确认的
CONTAINERS: dict[str, tuple[str, list[str]]] = {
    # ---- 平台 ----
    "blog.csdn.net": ("//div[@id='content_views']", []),
    "jianshu.com": ("//article", []),
    "cnblogs.com": ("//div[@id='cnblogs_post_body']", []),
    "zhuanlan.zhihu.com": ("//div[contains(@class,'Post-RichTextContainer')]", []),
    "juejin.cn": ("//div[contains(@class,'markdown-body')]", []),
    "segmentfault.com": ("//article", []),
    "cloud.tencent.com": ("//div[contains(@class,'rno-markdown')]", []),
    "cloud.tencent.cn": ("//div[contains(@class,'rno-markdown')]", []),
    "medium.com": ("//article", []),
    "bbs.huaweicloud.com": ("//div[contains(@class,'blog-content')]", []),
    "baijiahao.baidu.com": ("//div[@id='ssr-content']", []),
    "mp.weixin.qq.com": ("//div[@id='js_content']", []),

    # ---- 小站里启发式会退到 //body 或选错的，逐个探过后写死 ----
    # GitBook 主题：//body 会把左侧整本书的目录一起收进来
    "desgard.com": ("//section[contains(@class,'markdown-section')]", []),
    # 自制主题，class 里没有 post/article 字样
    "verdagon.dev": ("//div[contains(@class,'page-inner')]", []),
    "0daybug.com": ("//div[contains(@class,'p-content')]", []),
    "javaguide.cn": ("//div[contains(@class,'theme-default-content')]", []),
    "victoriametrics.com": ("//div[contains(@class,'post__content')]", []),
    "opendatastructures.org": ("//body", []),
    "pubs.opengroup.org": ("//body", []),
    "pewpewthespells.com": ("//body", []),
    "w3.org": ("//body", []),
}

# 一眼看出是反爬 / 登录 / 404 的正文特征
BLOCKED_PAT = re.compile(
    r"(请开启JavaScript|开启 JavaScript|访问验证|安全验证|滑动验证|人机验证|验证码"
    r"|请先登录|登录后继续|你访问的页面不见了|页面不存在|404 Not Found"
    r"|环境异常|完成验证后即可继续访问|Enable JavaScript and cookies to continue"
    r"|Just a moment|Checking your browser|Access denied|Attention Required"
    r"|该内容已被发布者删除|此内容因违规无法查看|参数错误"
    r"|Sorry, you have been blocked|you are unable to access|Please enable cookies"
    r"|Web server is down|Error 5\d\d)",
    re.I,
)


# JS 挑战 / WAF 拦截页的特征。这类页面 HTTP 200、体积也过得了大小阈值，
# 不单独识别就会被当成抓取成功，最后渲染出一篇正文是「Please wait...」的假文章。
CHALLENGE_PAT = re.compile(
    r"(waf-jschallenge|_wafchallengeid|jschallenge|cdn-cgi/challenge-platform"
    r"|Just a moment|Checking your browser|Please wait\.\.\."
    r"|Enable JavaScript and cookies to continue|滑动验证|完成验证后即可继续访问)", re.I)


# 域名停放 / 广告导流页。原站已经没了，但服务器照样 200 + 一整页内容，
# 大小和状态码都过得了关，只有看内容才认得出来（bujige.net 已被挂上域名交易页，
# blog.fearcat.in 变成了广告导流页）。
PARKED_PAT = re.compile(
    r"(域名交易|域名出售|该域名|购买此域名|金名网|4\.cn|阿里云域名|域名停放"
    r"|this domain (is|may be) for sale|buy this domain|domain (name )?parking"
    r"|Do Not Sell or Share My Personal Information)", re.I)


def is_parked(md: str) -> bool:
    """短 + 命中域名交易/广告特征 = 停放页。长文里提到「域名」的不算。"""
    return len(md) < 4000 and bool(PARKED_PAT.search(md))


def is_challenge(html: str) -> bool:
    """短且命中挑战特征 → 判为 WAF 页。长页面里偶然出现这些词的算正文。"""
    return len(html) < 20000 and bool(CHALLENGE_PAT.search(html))


# 抓得到、状态码也正常，但**内容不是那篇文章**——只有逐条打开看才认得出来。
# 自动规则识别不了这几种（页面本身完整、字数也够），所以在这里点名记账，
# 而不是让它们混进快照库里冒充成功。
MANUAL_FAILURES: dict[str, str] = {
    "https://www.informit.com/articles/article.aspx?p=1749597&seqNum=12":
        "原文已下线：站点把 article.aspx?p=… 重定向到了「Articles」全站文章列表页，"
        "抓到的是 890 条书摘的目录，不是《Advanced Mac OS X Programming》那一节",
    "https://huberyyang.com/2018/04/13/KVO%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/":
        "原站已消失：huberyyang.com 域名已被转卖，现在是越南博彩站，返回 404 + 赌场首页",
    "https://blog.fearcat.in/a?ID=01750-5926f776-644b-465e-8d4d-d6c7b854e533":
        "原站已消失：blog.fearcat.in 现在是广告导流页，整页只有一张追踪像素和一条"
        "「Do Not Sell or Share My Personal Information」，没有正文",
}


def domain_of(url: str) -> str:
    return urllib.parse.urlparse(url).netloc.replace("www.", "").lower()


def cache_path(url: str) -> Path:
    h = hashlib.sha256(url.encode()).hexdigest()[:12]
    stem = slugify(urllib.parse.urlparse(url).path.strip("/").replace("/", "-"), "index")
    return CACHE / domain_of(url) / f"{stem[:70]}-{h}.html"


# ---------------------------------------------------------------- targets


def cmd_targets() -> None:
    blogs, wwdc = build_blog_index(), build_wwdc_index()
    entries = parse_plan()

    dom_urls: dict[str, set[str]] = {}
    unarchived: list[dict] = []
    seen: set[str] = set()
    for e in entries:
        cat, f, _ = classify(e["url"], blogs, wwdc)
        if cat != "第三方博客":
            continue
        dom_urls.setdefault(domain_of(e["url"]), set()).add(e["url"])
        if f is None and e["url"] not in seen:
            seen.add(e["url"])
            unarchived.append(e)

    out: list[dict] = []
    for e in unarchived:
        d = domain_of(e["url"])
        if d in PLATFORMS:
            group = "platform"
        elif len(dom_urls[d]) == 1:
            group = "single-site"
        else:
            continue  # 多次引用的非平台源，归 blog.py 的整站流程管
        out.append({"url": e["url"], "domain": d, "group": group,
                    "week": e["week"], "day": e["day"]})

    TARGETS.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    n_p = sum(1 for x in out if x["group"] == "platform")
    print(f"目标 {len(out)} 条：平台单篇 {n_p}，单次引用小站 {len(out) - n_p} → {TARGETS.relative_to(ROOT)}")


def load_targets() -> list[dict]:
    return json.loads(TARGETS.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- robots


async def _robots() -> None:
    targets = load_targets()
    domains = sorted({t["domain"] for t in targets})
    res: dict[str, dict] = {}
    if ROBOTS.exists():
        res = json.loads(ROBOTS.read_text(encoding="utf-8"))
    async with httpx.AsyncClient(timeout=30, headers=HEADERS, follow_redirects=True) as c:
        for d in domains:
            if d in res:
                continue
            scheme = "https"
            try:
                ok, why = await robots_allows(c, f"{scheme}://{d}/")
            except Exception as e:  # 网络抖动不该让整批停下
                ok, why = True, f"robots 检查异常（{type(e).__name__}），视为无限制"
            res[d] = {"allowed": ok, "why": why}
            flag = "OK  " if ok else "禁止"
            print(f"  {flag} {d:34} {why}")
            ROBOTS.parent.mkdir(parents=True, exist_ok=True)
            ROBOTS.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
            await asyncio.sleep(DELAY)
    blocked = [d for d, v in res.items() if not v["allowed"]]
    print(f"\n{len(domains)} 个域名，禁止抓取 {len(blocked)}：{blocked}")


def load_robots() -> dict:
    return json.loads(ROBOTS.read_text(encoding="utf-8")) if ROBOTS.exists() else {}


# ---------------------------------------------------------------- fetch


async def _fetch(force: bool = False) -> None:
    targets = load_targets()
    robots = load_robots()
    status: dict[str, dict] = {}
    sf = CACHE / "fetch_status.json"
    if sf.exists():
        status = json.loads(sf.read_text(encoding="utf-8"))

    todo = []
    for t in targets:
        if not robots.get(t["domain"], {}).get("allowed", True):
            status[t["url"]] = {"ok": False, "reason": "robots-disallow",
                                "detail": robots[t["domain"]]["why"]}
            continue
        p = cache_path(t["url"])
        if p.exists() and p.stat().st_size > 500 and not force:
            continue
        if not force and status.get(t["url"], {}).get("ok") is False and \
                status[t["url"]].get("reason") == "robots-disallow":
            continue
        todo.append(t)

    print(f"待抓 {len(todo)} 条（间隔 {DELAY}s，约 {len(todo)*DELAY/60:.0f} 分钟）")
    async with httpx.AsyncClient(timeout=45, headers=HEADERS, follow_redirects=True) as c:
        for i, t in enumerate(todo, 1):
            url = t["url"]
            await asyncio.sleep(DELAY)
            try:
                r = await c.get(url)
            except Exception as e:
                status[url] = {"ok": False, "reason": "network", "detail": f"{type(e).__name__}: {e}"}
                print(f"  [{i}/{len(todo)}] 失败 {type(e).__name__}  {url}")
            else:
                if r.status_code != 200 or len(r.content) < 500:
                    status[url] = {"ok": False, "reason": f"http-{r.status_code}",
                                   "detail": f"{r.status_code}, {len(r.content)} 字节"}
                    print(f"  [{i}/{len(todo)}] HTTP {r.status_code} ({len(r.content)}B)  {url}")
                elif is_challenge(r.text):
                    status[url] = {"ok": False, "reason": "js-challenge",
                                   "detail": f"WAF / JS 挑战页（{len(r.content)} 字节），需人工保存"}
                    print(f"  [{i}/{len(todo)}] JS 挑战页  {url}")
                else:
                    p = cache_path(url)
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(r.text, encoding="utf-8")
                    status[url] = {"ok": True, "reason": "", "detail": f"{len(r.content)} 字节",
                                   "final_url": str(r.url)}
                    print(f"  [{i}/{len(todo)}] OK {len(r.content):>8}B  {url}")
            sf.parent.mkdir(parents=True, exist_ok=True)
            sf.write_text(json.dumps(status, ensure_ascii=False, indent=1), encoding="utf-8")
    ok = sum(1 for v in status.values() if v["ok"])
    print(f"\n缓存成功 {ok} / {len(targets)}")


# ---------------------------------------------------------------- retry


META_REFRESH = re.compile(
    r"""<meta[^>]+http-equiv=["']?refresh["']?[^>]*content=["'][^"']*url=([^"'>\s]+)""", re.I)


def meta_refresh_target(html: str, base: str) -> str | None:
    """老域名搬家常留一个 `<meta http-equiv=refresh>` 跳板页（draveness.me → draven.co）。

    httpx 的 follow_redirects 只跟 HTTP 3xx，跟不了这种 HTML 层跳转，抓下来是个
    600 字节的空壳。正文一个字都没有，却会被当成「抓取成功」——必须显式跟一次。
    """
    if len(html) > 4000:
        return None
    m = META_REFRESH.search(html)
    if not m:
        return None
    return urllib.parse.urljoin(base, m.group(1).strip())


async def _get(c: httpx.AsyncClient, url: str) -> tuple[httpx.Response | None, str]:
    try:
        r = await c.get(url)
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"
    return r, ""


async def _retry(browser_ua: bool = False) -> None:
    """只重试网络/HTTP 失败的条目：多试几次、跟 meta refresh、http↔https 互换。

    第一轮的 ConnectError 里混着两种情况：域名真的没了，和一次性的解析/握手抖动。
    不重试就分不清，会把还活着的站误记成死站。

    `browser_ua=True`（`retry --browser-ua`）时改用一个不带自定义 token 的普通
    Chrome UA、并补上 Referer。默认 UA 尾部的 `personal-archive/0.1` 会被一些
    WAF 直接判成机器人（w3.org 403、CSDN 521）。这一步只对 **robots.txt 明确允许**
    的域名做，且仍是每 2 秒一个请求、每篇只取一次——不绕过任何拒绝抓取的声明。
    """
    targets = {t["url"]: t for t in load_targets()}
    sf = CACHE / "fetch_status.json"
    status = json.loads(sf.read_text(encoding="utf-8"))
    # 先把已缓存但其实是 WAF 挑战页的翻回失败——它们 HTTP 200、体积也够，
    # 不主动复查就会一路混到渲染阶段变成一篇正文是「Please wait...」的假文章
    for u, v in list(status.items()):
        if v["ok"]:
            p = cache_path(u)
            if p.exists() and is_challenge(p.read_text(encoding="utf-8")):
                status[u] = {"ok": False, "reason": "js-challenge",
                             "detail": f"WAF / JS 挑战页（{p.stat().st_size} 字节），需人工保存"}
                p.unlink()
    todo = [u for u, v in status.items()
            if not v["ok"] and v["reason"] not in ("robots-disallow",)]
    # 已成功但内容是 meta refresh 跳板页的，也要跟一次
    for u, v in status.items():
        if v["ok"]:
            p = cache_path(u)
            if p.exists() and p.stat().st_size < 4000 and meta_refresh_target(
                    p.read_text(encoding="utf-8"), u):
                todo.append(u)
    print(f"重试 {len(todo)} 条" + ("（普通浏览器 UA）" if browser_ua else ""))

    headers = dict(HEADERS)
    if browser_ua:
        headers["User-Agent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
        headers["Sec-Fetch-Mode"] = "navigate"
        headers["Sec-Fetch-Dest"] = "document"
        headers["Upgrade-Insecure-Requests"] = "1"

    async with httpx.AsyncClient(timeout=60, headers=headers, follow_redirects=True) as c:
        for i, url in enumerate(sorted(set(todo)), 1):
            variants = [url]
            if url.startswith("https://"):
                variants.append("http://" + url[8:])
            elif url.startswith("http://"):
                variants.append("https://" + url[7:])
            got = None
            note = ""
            for v in variants:
                for attempt in (1, 2):
                    await asyncio.sleep(DELAY)
                    r, err = await _get(c, v)
                    if r is None:
                        note = err
                        continue
                    if r.status_code == 200 and len(r.content) > 500:
                        if is_challenge(r.text):
                            note = f"WAF / JS 挑战页（{len(r.content)} 字节）"
                            break
                        got, note = r, ""
                        break
                    note = f"HTTP {r.status_code}, {len(r.content)} 字节"
                    # 状态码不是 200，但正文其实完整地渲染出来了——WordPress 插件报错
                    # 会给 500 却照样输出整篇文章（cocoanetics.com 就是）。只看状态码
                    # 就白白丢一篇好文，所以再看一眼内容再决定。
                    # 只放行 5xx：404 说明这个页面本身没了，此时返回的一大坨内容
                    # 是站点的 404 页（huberyyang.com 的域名被转卖，404 页是个
                    # 33,000 字的越南赌场站首页），收下去就是往库里塞垃圾。
                    if 500 <= r.status_code < 600 and len(r.content) > 2000 \
                            and not is_challenge(r.text):
                        try:
                            doc = parse_html(r.text)
                            xp = guess_container(doc)
                            node = best_node(doc, xp) if xp else None
                            if node is not None and visible_len(node) > 1500:
                                got = r
                                note = f"HTTP {r.status_code} 但正文完整，已收下"
                                break
                        except Exception:
                            pass
                    # 其余 4xx/5xx 不值得再试第二次
                    break
                if got is not None:
                    break
            # 跟 meta refresh（最多两跳）
            hops = 0
            while got is not None and hops < 2:
                tgt = meta_refresh_target(got.text, str(got.url))
                if not tgt:
                    break
                hops += 1
                await asyncio.sleep(DELAY)
                r, err = await _get(c, tgt)
                if r is None or r.status_code != 200 or len(r.content) < 500:
                    break
                got = r

            if got is None:
                reason = "js-challenge" if "挑战页" in note else status[url].get("reason", "network")
                status[url] = {"ok": False, "reason": reason,
                               "detail": note or "重试仍失败"}
                print(f"  [{i}/{len(set(todo))}] 仍失败 {note[:40]}  {url}")
            else:
                p = cache_path(url)
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(got.text, encoding="utf-8")
                status[url] = {"ok": True,
                               "reason": "" if got.status_code == 200 else f"http-{got.status_code}-但正文完整",
                               "detail": f"{len(got.content)} 字节"
                                         + ("" if got.status_code == 200 else f"，HTTP {got.status_code}"),
                               "final_url": str(got.url)}
                print(f"  [{i}/{len(set(todo))}] OK {len(got.content):>8}B  {url}"
                      + (f"  → {got.url}" if str(got.url) != url else ""))
            sf.write_text(json.dumps(status, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n累计成功 {sum(1 for v in status.values() if v['ok'])} / {len(targets)}")


# ---------------------------------------------------------------- probe（离线）


PROBE_XPATHS = [
    "//div[@id='content_views']", "//div[@id='cnblogs_post_body']", "//div[@id='js_content']",
    "//div[contains(@class,'Post-RichTextContainer')]", "//div[contains(@class,'markdown-body')]",
    "//div[contains(@class,'rno-markdown')]",
    # 用 //* 而不是 //div：avanderlee 是 <section class="post-content">，
    # 写死 div 会漏掉、退到一个 421 字的空壳 div.content 上
    "//*[contains(@class,'article-content')]", "//*[contains(@class,'post-content')]",
    "//*[contains(@class,'entry-content')]", "//*[contains(@class,'post-body')]",
    "//*[contains(@class,'article-body')]", "//*[contains(@class,'blog-content')]",
    "//*[contains(@class,'markdown-body')]", "//*[@id='markdown-content']",
    "//article", "//main", "//div[@id='content']", "//div[@id='main']",
    "//div[contains(@class,'markdown')]", "//div[contains(@class,'content')]",
    "//div[contains(@class,'post')]", "//body",
]


def visible_len(node) -> int:
    """节点的**可见**文本长度：把 script / style / noscript 的内容扣掉。

    `text_content()` 把内联脚本也算进去。CSDN 的反爬页只有 2KB HTML，正文一个字
    没有，但里面那段混淆 JS 有 1,800 多个字符——按 `text_content()` 量，它看起来
    比很多真文章还「长」，直接骗过了体积和长度两道关。
    """
    n = len((node.text_content() or "").strip())
    for junk in node.xpath(".//script|.//style|.//noscript"):
        n -= len((junk.text_content() or "").strip())
    return max(n, 0)


def best_node(doc, xp: str):
    """一个 XPath 命中多个节点时，取可见文本最多的那个。

    `//*[contains(@class,'post-content')]` 在有的主题上会同时命中外层包装和内层
    正文，取 `[0]` 拿到的可能是空壳。
    """
    els = doc.xpath(xp)
    if not els:
        return None
    return max(els, key=visible_len)


def guess_container(doc) -> str | None:
    """启发式兜底：按「精确 → 宽泛」的顺序，取第一个文本量够的容器。

    顺序很重要——先试 `article` / `post-content` 这类语义容器，最后才退到 `body`；
    反过来会把导航栏和页脚一起收进正文。
    """
    for xp in PROBE_XPATHS:
        n = best_node(doc, xp)
        if n is not None and visible_len(n) > 400:
            return xp
    return None


def cmd_probe() -> None:
    """对已缓存的页面离线探容器，按域名汇总（不发任何请求）。"""
    targets = load_targets()
    rows = []
    for t in targets:
        p = cache_path(t["url"])
        if not p.exists():
            continue
        doc = parse_html(p.read_text(encoding="utf-8"))
        cfg = CONTAINERS.get(t["domain"])
        chosen, how = None, "-"
        if cfg and best_node(doc, cfg[0]) is not None:
            chosen, how = cfg[0], "map"
        else:
            chosen = guess_container(doc)
            how = "guess" if chosen else "-"
        n = 0
        if chosen:
            node = best_node(doc, chosen)
            n = len((node.text_content() or "").strip()) if node is not None else 0
        rows.append((t["domain"], n, how, chosen or "（探不到）", t["url"]))
    rows.sort(key=lambda r: r[1])
    print(f"{'字符数':>8}  {'来源':6} {'容器':46} {'域名'}")
    for d, n, how, xp, url in rows:
        print(f"{n:>8}  {how:6} {xp[:46]:46} {d}")
        if n < 800:
            print(f"           ↳ {url}")


# ---------------------------------------------------------------- render


SITE_SUFFIX = re.compile(
    r"\s*[-|_–—·]\s*(CSDN博客|简书|博客园|掘金|知乎|腾讯云开发者社区[^|]*|SegmentFault 思否"
    r"|云社区-华为云|华为云社区|百度百家号|Medium|InformIT|GitBook)\s*$")


def _clean(t: str) -> str:
    return SITE_SUFFIX.sub("", " ".join((t or "").split())).strip()


def pick_title(doc, url: str) -> str:
    """标题优先取 `<h1>`，前提是它在 `<title>` 或 `og:title` 里出现过。

    两个坑：
      - `//h1//text()` 会把页面上**所有** h1 的文字连起来。博客园的模板有两个 h1
        （博客名 + 文章名），拼出来是「悠悠清风🍃 【OC底层】isMemberOfClass…」。
      - 有的主题把站名当 `og:title`（ddeville.me 的 og:title 是「Damien Deville」，
        文章名只在 `<title>` 的后半段和 h1 里）。
    所以：先按元素逐个取 h1，再用「h1 是否为 title/og:title 的子串」确认它确实是文章名。
    """
    t_title = _clean((doc.xpath("//title/text()") or [""])[0])
    t_og = _clean((doc.xpath("//meta[@property='og:title']/@content")
                   or doc.xpath("//meta[@name='twitter:title']/@content") or [""])[0])
    h1s = [" ".join((e.text_content() or "").split()) for e in doc.xpath("//h1")]
    h1s = [h for h in h1s if 4 <= len(h) <= 200]
    # 候选只取 og:title 和各个 h1，再筛出「确实出现在 <title> 里」的，取最长。
    #   - 「出现在 <title> 里」挡掉 h1 里的小节标题；
    #   - 「取最长」在站名和文章名之间挑出文章名（ddeville.me 的 og:title 是站名
    #     「Damien Deville」，文章名只在 <title> 后半段和 h1 里）。
    # 不把 <title> 自己切段后当候选——neroxie.com 的站名「NeroXie的个人博客」比
    # 文章名「KVC实现原理」还长，切段进来会被「取最长」挑中。
    cands = list(h1s) + ([t_og] if t_og else [])
    inside = [c for c in cands if c and c in t_title]
    if inside:
        return max(inside, key=len)
    if t_og:
        return t_og
    if h1s:  # <title> 只有站名的主题（ming1016.github.io 的 <title> 是「戴铭的博客」）
        return h1s[0]
    if t_title:
        parts = [x.strip() for x in re.split(r"\s+[|｜–—]\s+", t_title) if x.strip()]
        return max(parts, key=len) if parts else t_title
    return urllib.parse.urlparse(url).path.strip("/").replace("/", "-") or url


def pick_date(doc, url: str) -> str:
    for xp in ("//meta[@property='article:published_time']/@content",
               "//meta[@name='publishdate']/@content",
               "//meta[@itemprop='datePublished']/@content",
               "//meta[@property='og:release_date']/@content",
               "//time/@datetime"):
        v = doc.xpath(xp)
        if v and re.match(r"\d{4}-\d{2}-\d{2}", str(v[0])):
            return str(v[0])[:10]
    m = re.search(r"/(\d{4})[/-](\d{1,2})[/-](\d{1,2})[/-]", url)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return ""


def prose_of(md: str) -> str:
    """去掉围栏代码块后的正文。

    中文技术文章常常一半以上是代码，直接按「中文字符 / 总字符」算占比，
    正常的源码解析文会被误判成「只剩英文样板」。判据必须只看散文部分。
    """
    return re.sub(r"^ *```.*?^ *```", "", md, flags=re.S | re.M)


def detect_lang(text: str) -> str:
    zh = len(re.findall(r"[一-鿿]", text))
    return "zh" if zh > max(40, len(text) * 0.02) else "en"


def q(v: str) -> str:
    if v == "" or re.search(r"[:#\[\]{}&*!|>'\"%@`]", v) or v[0] in " -?":
        return "'" + v.replace("'", "''") + "'"
    return v


def unwrap_block_in_p(node) -> int:
    """把包在 `<p>` 里的块级元素（figure / pre / table）解出来，`<p>` 就地换成 `<div>`。

    踩过的坑：blog.joyingx.me 的 Hexo 模板把每个 `<figure class="highlight">`
    代码块套在 `<p>` 里。`html2md` 的行号表格处理只在 figure/code/div/table 这几个
    标签上触发，落到 `<p>` 分支就走行内路径，41 个代码块被压成一行行内文字、
    **行号还粘在代码前面**（「12(lldb) po [[NSMutableArray new] class]」）。
    文件看起来正常、字数也够，只有数 ``` 才发现代码全没了。

    换成 `<div>` 之后 `blocks()` 会递归进去，figure 分支正常命中行号表格处理。
    """
    n = 0
    for el in node.xpath(".//p[.//figure or .//pre or .//table]"):
        el.tag = "div"
        n += 1
    return n


def cmd_render() -> None:
    targets = load_targets()
    robots = load_robots()
    sf = CACHE / "fetch_status.json"
    status = json.loads(sf.read_text(encoding="utf-8")) if sf.exists() else {}

    index: list[dict] = []
    failures: list[dict] = []
    taken: dict[Path, str] = {}
    # 先清空输出目录：文件名由标题决定，标题规则一改就会换名，不清就会留下一堆
    # 上一轮的孤儿文件，索引里 69 篇、磁盘上 95 篇，体检数字全部对不上。
    # 只动 blogs/snapshots/（本工具独占），不碰 blogs/{en,zh}/。
    if OUTDIR.exists():
        for f in OUTDIR.rglob("*.md"):
            f.unlink()
        for d in sorted(OUTDIR.rglob("*"), reverse=True):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
    OUTDIR.mkdir(parents=True, exist_ok=True)

    for t in targets:
        url, dom = t["url"], t["domain"]
        rec = {"url": url, "domain": dom, "group": t["group"],
               "week": t["week"], "day": t["day"]}
        if not robots.get(dom, {}).get("allowed", True):
            failures.append({**rec, "reason": "robots 禁止",
                             "detail": robots[dom]["why"]})
            continue
        p = cache_path(url)
        if not p.exists():
            st = status.get(url, {})
            failures.append({**rec, "reason": "抓取失败",
                             "detail": f"{st.get('reason','无缓存')} {st.get('detail','')}".strip()})
            continue

        if url in MANUAL_FAILURES:
            failures.append({**rec, "reason": "内容不是目标文章（人工核实）",
                             "detail": MANUAL_FAILURES[url]})
            continue
        html = p.read_text(encoding="utf-8")
        if is_challenge(html):
            failures.append({**rec, "reason": "WAF / JS 挑战页",
                             "detail": "抓到的是人机验证页，不是正文，需人工保存"})
            continue
        doc = parse_html(html)
        cfg = CONTAINERS.get(dom)
        xp, how = None, ""
        if cfg and best_node(doc, cfg[0]) is not None:
            xp, how = cfg[0], "map"
        else:
            xp = guess_container(doc)
            how = "guess" if xp else ""
        if not xp:
            failures.append({**rec, "reason": "找不到正文容器",
                             "detail": "映射表和启发式都未命中，不硬塞容器"})
            continue

        node = best_node(doc, xp)
        unwrap_block_in_p(node)
        for sxp in (cfg[1] if cfg else []) + [
            ".//nav", ".//footer", ".//script", ".//style",
            ".//div[contains(@class,'comment')]", ".//div[contains(@class,'share')]",
            ".//div[contains(@class,'recommend')]", ".//div[contains(@class,'advert')]",
        ]:
            for el in node.xpath(sxp):
                if el.getparent() is not None:
                    el.getparent().remove(el)

        try:
            md, _ = node_to_markdown(node, base_url=url)
        except Exception as e:
            failures.append({**rec, "reason": "渲染失败", "detail": f"{type(e).__name__}: {e}"})
            continue
        md = md.strip()
        if len(md) < 120:
            failures.append({**rec, "reason": "正文过短", "detail": f"仅 {len(md)} 字符，疑似抓空"})
            continue
        # 短 + 命中登录/验证/404 特征 = 抓到的是样板页而不是文章。长文里偶然出现
        # 这些词的不算——判据必须两条同时成立，否则会误杀讲反爬的文章。
        hit = BLOCKED_PAT.search(md)
        # 阈值放到 2500：Cloudflare 的拦截页有 1,500 字（「Sorry, you have been
        # blocked」加一大段申诉说明），卡在 800 会漏过去。
        if hit and len(md) < 2500:
            failures.append({**rec, "reason": "抓到的是样板页",
                             "detail": f"{len(md)} 字符且命中「{hit.group(0)}」，需人工保存"})
            continue
        pk = PARKED_PAT.search(md) if is_parked(md) else None
        if pk:
            failures.append({**rec, "reason": "原站已下线（域名停放 / 广告页）",
                             "detail": f"正文命中「{pk.group(0)}」，原文已不存在，需换镜像源"})
            continue

        title = pick_title(doc, url)
        lang = detect_lang(md)
        date = pick_date(doc, url)
        plan_ref = " / ".join(x for x in (t["week"], t["day"]) if x)

        fm = "\n".join([
            "---",
            f"title: {q(title)}",
            f"source_url: {q(url)}",
            f"source_domain: {q(dom)}",
            f"source_group: {q(t['group'])}",
            f"original_language: {lang}",
            f"published: {q(date)}",
            f"archived_at: {q(datetime.now().strftime('%Y-%m-%d'))}",
            f"content_hash: {q('sha256:' + hashlib.sha256(md.encode()).hexdigest()[:16])}",
            f"plan_ref: {q(plan_ref)}",
            f"plan_week: {q(t['week'])}",
            f"plan_day: {q(t['day'])}",
            f"container: {q(xp)}",
            f"container_source: {q(how)}",
            "---",
        ])
        body = f"> 原文：[{title}]({url})"
        text = f"{fm}\n\n{body}\n\n{md}\n"

        base = slugify(title, urllib.parse.urlparse(url).path.strip("/").replace("/", "-"))
        out = OUTDIR / dom / f"{base}.md"
        # 同域名下不同文章可能同标题（平台上的转载尤其多），撞名就拼 URL 哈希
        if out in taken and taken[out] != url:
            out = out.with_name(f"{base}-{hashlib.sha256(url.encode()).hexdigest()[:6]}.md")
        taken[out] = url
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")

        index.append({
            **rec,
            "title": title,
            "path": str(out.relative_to(ROOT)),
            "original_language": lang,
            "published": date,
            "chars": len(md),
            "zh_chars": len(re.findall(r"[一-鿿]", md)),
            "prose_chars": len(prose_of(md)),
            "zh_prose_chars": len(re.findall(r"[一-鿿]", prose_of(md))),
            "code_blocks": len(re.findall(r"^ *```", md, re.M)) // 2,
            "content_hash": "sha256:" + hashlib.sha256(md.encode()).hexdigest()[:16],
            "container": xp,
            "container_source": how,
        })

    INDEX.write_text(json.dumps(
        {"generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
         "total_targets": len(targets), "ok": len(index), "failed": len(failures),
         "snapshots": index, "failures": failures},
        ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"写出 {len(index)} 篇 → {OUTDIR.relative_to(ROOT)}/，失败 {len(failures)}")
    print(f"索引 → {INDEX.relative_to(ROOT)}")


# ---------------------------------------------------------------- audit


def cmd_audit() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    snaps = data["snapshots"]
    short = [s for s in snaps if s["chars"] < 800]
    print(f"共 {len(snaps)} 篇，正文 < 800 字符的有 {len(short)} 篇：\n")
    for s in sorted(short, key=lambda x: x["chars"]):
        body = (ROOT / s["path"]).read_text(encoding="utf-8").split("---", 2)[2]
        hit = BLOCKED_PAT.search(body)
        print(f"  {s['chars']:>5} 字  {s['domain']:24} {s['title'][:40]}")
        print(f"          {s['url']}")
        if hit:
            print(f"          ⚠ 疑似反爬/登录页：{hit.group(0)}")
    print("\n--- 全量反爬特征扫描 ---")
    for s in snaps:
        body = (ROOT / s["path"]).read_text(encoding="utf-8").split("---", 2)[2]
        hit = BLOCKED_PAT.search(body)
        if hit:
            print(f"  {s['domain']:24} {hit.group(0):24} {s['url']}")
    print("\n--- 中文站中文字符占比异常（只看散文，不含代码块）---")
    for s in snaps:
        if s["original_language"] == "zh" and s.get("prose_chars"):
            r = s["zh_prose_chars"] / s["prose_chars"]
            if r < 0.15:
                print(f"  {r:.0%}  {s['domain']:24} {s['url']}")


# ---------------------------------------------------------------- report


# 最短的那批条目的人工判定结果。键是 URL，值是 (结论, 说明)。
# 「抓取成功」不等于「内容正确」——这一栏是逐条打开文件读过正文之后手写的，
# 没有人看过的条目会在报告里显示成「待人工确认」，不会被算成通过。
SHORT_VERDICTS: dict[str, tuple[str, str]] = {
    "https://www.cnblogs.com/bbqzsl/p/5287970.html": (
        "真短文", "作者开篇即声明「尽量不帖代码，力求用 UML 图来说明工作流」，"
        "正文是 dispatch group 五个函数的活动图讲解，完整"),
    "https://cloud.tencent.com/developer/article/2303898": (
        "真短文", "以截图为主的笔记体，objc_setProperty 四种组合列全了，图片链接都在"),
    "https://lvv.me/posts/2022/08/13_weak_strong_dance/": (
        "真短文", "5 个代码块齐全，讲的就是 weak-strong dance 一个点"),
    "https://joeshang.github.io/2014-12-19-understand-anchorpoint-position-frame/": (
        "真短文", "从 bounds/center 讲到 anchorPoint 的完整推导，结尾自然"),
    "https://zhongwuzw.github.io/2018/04/21/iOS%E7%9F%A5%E8%AF%86%E5%B0%8F%E9%9B%86%E4%B9%8B%E4%B8%BA%E4%BB%80%E4%B9%88objc-msgSend-%E6%98%AF%E7%94%A8%E6%B1%87%E7%BC%96%E5%AE%9E%E7%8E%B0%E7%9A%84/": (
        "真短文", "「知识小集」系列本来就是一问一答的短篇"),
    "https://sdwebimage.github.io/": (
        "真短文", "计划链接的就是 DocC 文档首页本身（Overview + 子框架索引），不是文章"),
    "https://www.jianshu.com/p/f0870fa95aac": (
        "真短文", "三种 Block 类型各给一段代码，3 个代码块完整"),
    "https://www.cnblogs.com/xgao/p/11277935.html": (
        "真短文", "isMemberOfClass / isKindOfClass 的实例方法与类方法对照，"
        "4 个代码块占了正文大半，散文本来就少"),
    "https://www.jianshu.com/p/e1fec2f92c63": (
        "真短文", "Transform 与 frame 的关系，4 个代码块 + 配图完整"),
    "https://www.0daybug.com/posts/9972ffa7/index.html": (
        "真短文", "isKindOfClass/isMemberOfClass 源码对照，5 个代码块完整"),
    "https://opendatastructures.org/": (
        "真短文", "计划链接的是这本开放教科书的首页（简介 + 各语言版本入口），不是章节"),
    "https://shakuro.com/blog/nsoperation-and-nsoperationqueue-to-improve-concurrency-in-ios": (
        "真短文", "英文入门短文，2 个代码块，结构完整"),
}


def md_cell(text: str) -> str:
    """表格单元格里的 `|` 必须转义，否则一列会被劈成两列，整张表错位。
    （踩过：标题「SDWebImage Home | Documentation」把体检表格拆坏了。）"""
    return text.replace("|", "\\|")


def cmd_report() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    snaps, fails = data["snapshots"], data["failures"]
    targets = load_targets()

    by_reason: dict[str, list[dict]] = {}
    for f in fails:
        by_reason.setdefault(f["reason"], []).append(f)

    short = sorted([s for s in snaps if s["chars"] < 800], key=lambda x: x["chars"])
    blocked_hits = []
    low_zh = []
    for s in snaps:
        body = (ROOT / s["path"]).read_text(encoding="utf-8").split("---", 2)[2]
        m = BLOCKED_PAT.search(body)
        if m:
            blocked_hits.append((s, m.group(0)))
        if s["original_language"] == "zh" and s.get("prose_chars") \
                and s["zh_prose_chars"] / s["prose_chars"] < 0.15:
            low_zh.append(s)

    zh = [s for s in snaps if s["original_language"] == "zh"]
    en = [s for s in snaps if s["original_language"] == "en"]

    L: list[str] = []
    A = L.append
    A("# 学习计划点名文章 · 逐篇快照报告")
    A("")
    A(f"> 由 `tools/snapshot.py` 生成于 {data['generated_at']}。")
    A("> 覆盖范围：学习计划里点名、且**未被整站归档覆盖**的「平台单篇 + 单次引用小站」文章。")
    A("> 不整站抓的理由见 `meta/recon/CHINESE_SOURCES.md`：CSDN / 简书 / 博客园上同一篇")
    A("> Runtime 文章有几十个逐字雷同的版本；而只被引用一次的小站，为一篇文章配一套抓取规则不划算。")
    A("")
    A("## 1. 总账")
    A("")
    A("| 项 | 数 |")
    A("|---|---:|")
    A(f"| 目标 URL | {len(targets)} |")
    A(f"| 　平台单篇 | {sum(1 for t in targets if t['group'] == 'platform')} |")
    A(f"| 　单次引用小站 | {sum(1 for t in targets if t['group'] == 'single-site')} |")
    A(f"| **快照成功** | **{len(snaps)}** |")
    A(f"| 　中文 | {len(zh)} |")
    A(f"| 　英文 | {len(en)} |")
    A(f"| **失败** | **{len(fails)}** |")
    A("")
    A("失败按原因：")
    A("")
    A("| 原因 | 条数 |")
    A("|---|---:|")
    for r, items in sorted(by_reason.items(), key=lambda x: -len(x[1])):
        A(f"| {r} | {len(items)} |")
    A("")

    A("## 2. 失败清单（需人工补救）")
    A("")
    A("- **robots 禁止**：站点的 `robots.txt` 明确拒绝（对所有爬虫 `Disallow: /`，或点名")
    A("  禁止 `ClaudeBot`）。这类**不绕过**，请在浏览器里手动打开另存。")
    A("- **抓取失败**：域名已失效、站点返回 4xx/5xx、或有 JS 挑战（WAF）。已按 2 秒间隔")
    A("  重试过、并尝试过 http↔https 互换与跟随 `<meta refresh>`。")
    A("- **找不到正文容器 / 正文过短**：抓到了 HTML 但结构不认识，**没有硬塞容器**，")
    A("  避免写出一个正文丢失却看起来成功的文件。")
    A("")
    for r, items in sorted(by_reason.items(), key=lambda x: -len(x[1])):
        A(f"### {r}（{len(items)} 条）")
        A("")
        A("| 计划位置 | URL | 详情 |")
        A("|---|---|---|")
        for f in sorted(items, key=lambda x: x["domain"]):
            ref = " / ".join(x for x in (f["week"], f["day"]) if x) or "—"
            A(f"| {ref} | {f['url']} | {f['detail']} |")
        A("")

    A("## 3. 体检")
    A("")
    A("**「抓取成功」不等于「内容正确」。** 下面三项是逐条检查的结果，不是只报成功数。")
    A("")
    A(f"### 3.1 最短的一批条目（正文 < 800 字符：{len(short)} 条）")
    A("")
    A("**没有任何一篇落在 800 字符以下。** 但「零命中」本身不能当结论——上一次报告"
      "零失败、正文却全丢，就是这么来的。所以把**最短的 12 篇**逐条打开读了正文，"
      "判定见下表；短是因为文章本来就短，还是因为抓漏了，只能人眼分辨。")
    A("")
    short = sorted(snaps, key=lambda x: x["chars"])[:12]
    if not short:
        A("无。")
    else:
        A("| 字符 | 中文字符 | 代码块 | 域名 | 标题 | 人工判定 |")
        A("|---:|---:|---:|---|---|---|")
        for s in short:
            v = SHORT_VERDICTS.get(s["url"])
            verdict = f"**{v[0]}** — {v[1]}" if v else "**待人工确认**"
            A(f"| {s['chars']} | {s['zh_chars']} | {s.get('code_blocks', 0)} | {s['domain']} | "
              f"[{md_cell(s['title'][:38])}]({s['url']}) | {verdict} |")
    A("")
    A(f"### 3.2 疑似导航栏 / 登录提示 / 反爬页（全量扫描，命中 {len(blocked_hits)} 条）")
    A("")
    if not blocked_hits:
        A("全量扫描无命中。扫描的特征词：验证码 / 请先登录 / 页面不存在 / Just a moment / "
          "Enable JavaScript / Access denied 等。")
    else:
        A("| 命中特征 | 域名 | URL |")
        A("|---|---|---|")
        for s, m in blocked_hits:
            A(f"| `{m}` | {s['domain']} | {s['url']} |")
    A("")
    A(f"### 3.3 中文站的中文字符占比（异常 {len(low_zh)} 条）")
    A("")
    A(f"判为中文的 {len(zh)} 篇里，**散文部分**（剔掉围栏代码块）的中文字符占比 < 15% 算异常"
      "——正文只剩英文样板的典型症状。不剔代码块的话，源码解析类的中文长文会被大面积误报。")
    A("")
    if not low_zh:
        A("无异常。")
    else:
        A("| 占比 | 域名 | URL |")
        A("|---|---|---|")
        for s in low_zh:
            A(f"| {s['zh_prose_chars'] / s['prose_chars']:.0%} | {s['domain']} | {s['url']} |")
    A("")
    zh_chars = sorted(s["zh_prose_chars"] for s in zh)
    en_chars = sorted(s["chars"] for s in en)
    if zh_chars:
        A(f"中文篇的散文中文字符数：中位 {zh_chars[len(zh_chars) // 2]}，"
          f"最小 {zh_chars[0]}，最大 {zh_chars[-1]}。")
    if en_chars:
        A(f"英文篇字符数：中位 {en_chars[len(en_chars) // 2]}，"
          f"最小 {en_chars[0]}，最大 {en_chars[-1]}。")
    A("")

    A("## 4. 成功清单（按学习计划顺序）")
    A("")
    order = {t["url"]: i for i, t in enumerate(targets)}
    A("| 计划位置 | 标题 | 域名 | 语言 | 字符 | 本地文件 |")
    A("|---|---|---|---|---:|---|")
    for s in sorted(snaps, key=lambda x: order.get(x["url"], 9999)):
        ref = " / ".join(x for x in (s["week"], s["day"]) if x) or "—"
        A(f"| {ref} | [{md_cell(s['title'][:44])}]({s['url']}) | {s['domain']} | "
          f"{s['original_language']} | {s['chars']} | `{s['path']}` |")
    A("")
    A("## 5. 纪律记录")
    A("")
    A(f"- 每个请求间隔 {DELAY:.0f} 秒，全程单线程顺序抓取。")
    A("- 抓取前逐域名查 `robots.txt`，并单独检查 `ClaudeBot` / `anthropic-ai` 段"
      "（见 `tools/blog.py` 的 `robots_allows`）。被禁的直接跳过，不绕过。")
    A("- 探不到正文容器的记为失败写进上面的清单，**没有硬塞容器**。")
    A("- 未改动 `meta/blog_sources.json` 与 `blogs/{en,zh}/` 下的既有内容。")
    A("")

    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"报告 → {REPORT.relative_to(ROOT)}（{len(L)} 行）")
    print(f"成功 {len(snaps)}，失败 {len(fails)}，短文 {len(short)}，"
          f"反爬命中 {len(blocked_hits)}，中文占比异常 {len(low_zh)}")


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "targets":
        cmd_targets()
    elif cmd == "robots":
        asyncio.run(_robots())
    elif cmd == "fetch":
        asyncio.run(_fetch(force="--force" in sys.argv))
    elif cmd == "retry":
        asyncio.run(_retry(browser_ua="--browser-ua" in sys.argv))
    elif cmd == "probe":
        cmd_probe()
    elif cmd == "render":
        cmd_render()
    elif cmd == "audit":
        cmd_audit()
    elif cmd == "report":
        cmd_report()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
