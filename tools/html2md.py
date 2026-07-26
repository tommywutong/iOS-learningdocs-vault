#!/usr/bin/env python3
"""HTML → Markdown，**代码块逐字节保真**。

为什么不用 trafilatura / html2text：实测三个目标源，通用抽取器都会破坏代码——

| 源 | 通用抽取器的表现 |
|---|---|
| mikeash.com | 代码缩进被抹平（`_foo = newFoo;` 丢了 4 个空格） |
| alwaysprocessing.blog | 同样丢缩进，且混入作者简介样板 |
| blog.ibireme.com | **代码块整个丢失**（0 个围栏，实际有 15 个），标题抽成了「163 评论」 |

对一个以代码为主的技术归档来说，丢缩进等于毁掉资料。所以这里自己走 DOM：
`<pre>` 一律取 `text_content()` 原样输出，一个空格都不动。

## Crayon 高亮插件的特殊处理

WordPress 的 Crayon 插件（ibireme 等中文博客常用）把代码打散进上千个
`<span class="crayon-*">`，按 DOM 顺序拼接会得到带行号的乱码。但插件同时把
**原始代码完整存在 `<textarea class="crayon-plain">` 里** —— 那才是干净的源。
"""
from __future__ import annotations

import re

import lxml.html

# 这些标签整棵子树丢弃
DROP = {
    "script", "style", "noscript", "iframe", "form", "button", "svg",
    "nav", "footer", "aside",
}

# 常见的样板容器 class/id 关键词（分享按钮、评论区、作者简介、相关文章）
BOILERPLATE = re.compile(
    r"share|social|comment|disqus|related|author-?(bio|box|info)|subscribe|newsletter"
    r"|advert|sidebar|breadcrumb|pagination|post-?nav|meta-?nav|tags?-?list|toc-?wrap",
    re.I,
)

BLOCK_TAGS = {
    "p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li",
    "pre", "blockquote", "table", "hr", "figure", "figcaption", "section", "article",
    # 表格的行/单元格也要能递归进去。老站用 table 做布局，正文全在 td 里；
    # 漏掉这几个标签的话，布局 table 递归到一半就断，正文会整篇丢失。
    "tr", "td", "th", "tbody", "thead", "tfoot", "main", "header", "body",
}

# 这些是纯结构容器，自己不产生内容，一律递归进去
PASSTHROUGH = {"tr", "td", "th", "tbody", "thead", "tfoot", "body", "main", "section", "header"}

# 行内标签。它们可以直接挂在块级容器下面（`<li><code>x</code> 不能为 nil</li>`），
# 块级处理必须把连续的行内内容攒成一段，否则这些标签会整个被丢掉。
INLINE_TAGS = {
    "code", "strong", "b", "em", "i", "del", "s", "strike", "sub", "sup", "small",
    "abbr", "kbd", "var", "mark", "q", "cite", "time", "tt", "u", "big", "font",
    "label", "ins", "samp", "dfn", "acronym", "bdi", "bdo", "ruby", "rt", "rp",
    "span", "a", "br", "wbr",
}


def _text(el) -> str:
    """行内文本，压缩空白（代码路径不会走到这里）。"""
    return re.sub(r"\s+", " ", el.text_content() or "")


def _is_boilerplate(el) -> bool:
    ident = " ".join(filter(None, [el.get("class") or "", el.get("id") or ""]))
    return bool(ident and BOILERPLATE.search(ident))


class Converter:
    def __init__(self, base_url: str = "", code_mode: str = "auto") -> None:
        self.base_url = base_url
        self.code_mode = code_mode  # auto | pre | crayon
        self.images: list[str] = []

    # ------------------------------------------------------------ 行内

    def inline(self, el) -> str:
        """渲染 el 的**内容**（不含 el 自己的标签语义）。"""
        out: list[str] = []
        if el.text:
            out.append(self.escape(el.text))
        for child in el:
            tag = child.tag if isinstance(child.tag, str) else ""
            # tag 为空＝注释/处理指令，本身不是内容，但 tail 要留
            if tag and tag not in DROP:
                out.append(self.inline_el(child))
            if child.tail:
                out.append(self.escape(child.tail))
        return "".join(out)

    def inline_el(self, child) -> str:
        """把**单个元素本身**当行内内容渲染（含它自己的标签语义）。

        块级处理里也要用它：行内标签有可能直接挂在 <li> / <div> 下面，
        那时不能只渲染它的子节点，否则 `<code>`、`<strong>` 的标记会丢。
        """
        tag = child.tag if isinstance(child.tag, str) else ""
        if tag == "code":
            # 行内 code：内容不转义、不压空白
            return f"`{child.text_content()}`"
        if tag in ("strong", "b"):
            inner = self.inline(child).strip()
            return f"**{inner}**" if inner else ""
        if tag in ("em", "i"):
            inner = self.inline(child).strip()
            return f"_{inner}_" if inner else ""
        if tag in ("del", "s", "strike"):
            return f"~~{self.inline(child).strip()}~~"
        if tag in ("sup", "sub"):
            # 上下标不留标记会得到彻头彻尾的错数：mikeash 讲浮点时写
            # `2<sup>31</sup>`，直接拼接就变成「231」，`1010<sub>2</sub>` 变成「10102」。
            inner = self.inline(child).strip()
            return ("^" if tag == "sup" else "~") + inner if inner else ""
        if tag == "a":
            href = child.get("href", "")
            inner = self.inline(child).strip()
            # 空内容 + 纯锚点 href＝标题旁的「¶」永久链接（Hexo headerlink、
            # Docusaurus hash-link、Rouge anchor）。浏览器里它是个图标，退回用
            # href 当文字会在每个标题后面糊上一条 `[#小节名](#小节名)`。
            # Docusaurus 塞的是零宽空格，普通 strip() 去不掉，要单列出来。
            if not inner.strip("​‌‍﻿ ") and href.startswith("#"):
                return ""
            href = self.absolutize(href)
            inner = inner or href
            return f"[{inner}]({href})" if href else inner
        if tag == "img":
            return self.image(child)
        if tag == "br":
            return "  \n"
        return self.inline(child)

    def escape(self, text: str) -> str:
        text = re.sub(r"\s+", " ", text)
        # 只转义真正会造成歧义的：行首标记留给块级处理，这里只挡尖括号和反斜杠
        return text.replace("\\", "\\\\").replace("<", "\\<").replace(">", "\\>")

    def absolutize(self, url: str) -> str:
        if not url or url.startswith(("http://", "https://", "#", "mailto:", "data:")):
            return url
        if not self.base_url:
            return url
        from urllib.parse import urljoin

        return urljoin(self.base_url, url)

    def image(self, el) -> str:
        src = self.absolutize(el.get("src") or el.get("data-src") or "")
        if not src:
            return ""
        self.images.append(src)
        alt = re.sub(r"\s+", " ", el.get("alt") or "").strip()
        return f"![{alt}]({src})"

    # ------------------------------------------------------------ 代码

    def code_block(self, el) -> str:
        """`<pre>` → 围栏代码块。**内容一个字符都不动。**"""
        # 语言标注：从 class 里猜（language-swift / lang-objc / highlight-c 等）
        lang = ""
        for probe in (el, *el.iter()):
            if not isinstance(probe.tag, str):
                continue
            cls = probe.get("class") or ""
            m = re.search(r"(?:language|lang|brush|highlight)[-:]([a-z0-9+#]+)", cls, re.I)
            if m:
                lang = m.group(1).lower()
                break
        # `<pre>` 唯一的子元素是 `<code>` 时取 code 的内容，而不是 pre 的。
        # HTML5 里 `<pre><code>` 才是代码块的规范写法，很多模板会把 <code> 另起一行
        # 并缩进（objc.io 就是 `<pre>\n\t\t\t\t<code>…`）。取 pre.text_content() 会把
        # 那串模板制表符当成第一行代码的缩进，每个代码块的首行都被推歪。
        node = el
        codes = el.xpath("./code")
        if (
            len(codes) == 1
            and not (el.text or "").strip()
            and not (codes[0].tail or "").strip()
        ):
            node = codes[0]
        raw = node.text_content()
        # 去掉整块统一的前后空行，但**保留每行的行内缩进**
        lines = raw.split("\n")
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        code = "\n".join(lines)
        # 内容里若含 ``` 就用更长的围栏
        fence = "```"
        while fence in code:
            fence += "`"
        return f"{fence}{lang}\n{code}\n{fence}"

    def crayon_blocks(self, root) -> dict[int, str]:
        """Crayon 插件：把 textarea.crayon-plain 的原文按出现顺序取出。"""
        blocks = {}
        for i, ta in enumerate(root.xpath(".//textarea[contains(@class,'crayon-plain')]")):
            raw = ta.text or ""
            lines = raw.split("\n")
            while lines and not lines[0].strip():
                lines.pop(0)
            while lines and not lines[-1].strip():
                lines.pop()
            blocks[i] = "```\n" + "\n".join(lines) + "\n```"
        return blocks

    # ------------------------------------------------------------ 块级

    def convert(self, root) -> str:
        # Crayon 模式：先把代码取出来，再把高亮容器整个替换成占位符
        crayon = {}
        if self.code_mode in ("auto", "crayon"):
            containers = root.xpath(".//div[contains(@class,'crayon-syntax')]")
            if containers:
                crayon = self.crayon_blocks(root)
                for i, c in enumerate(containers):
                    ph = lxml.html.Element("pre")
                    ph.set("data-crayon", str(i))
                    c.getparent().replace(c, ph)

        blocks = self.blocks(root, crayon)
        text = "\n\n".join(b for b in blocks if b and b.strip())
        return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    def blocks(self, el, crayon: dict, depth: int = 0) -> list[str]:
        """把 el 的子节点切成块。

        连续的行内内容（容器自己的 text、行内标签、各节点的 tail）攒进 buf，
        遇到真正的块级元素或结束时才冲刷成一段。不这样做的话
        `<li><code>x</code> 不能为 nil</li>` 里的 `<code>` 会整个丢掉，
        `<li>文字<code>x</code></li>` 的「文字」（挂在 el.text 上）也会丢。
        """
        out: list[str] = []
        buf: list[str] = []

        def flush() -> None:
            if not buf:
                return
            t = "".join(buf).strip()
            del buf[:]
            if t:
                out.append(t)

        if el.text and el.text.strip():
            buf.append(self.escape(el.text))

        for child in el:
            tag = child.tag if isinstance(child.tag, str) else ""
            if not tag:
                # 注释 / 处理指令：本身不是内容（mikeash 页面里有 `<!-- enable-comments -->`），
                # 但它后面的文本还要留下
                if child.tail and child.tail.strip():
                    buf.append(self.escape(child.tail))
                continue
            if tag in DROP or _is_boilerplate(child):
                continue
            # 行号表格式高亮要在其它分支之前拦掉：它外层可能是 figure/code/div/table，
            # 落到那些分支就会把行号当代码、或把整段代码当行内 code 压成一行。
            hl = self.highlight_code(child) if tag in ("figure", "code", "div", "table") else None
            if hl:
                flush()
                out.append(hl)
                continue
            if tag == "pre":
                flush()
                idx = child.get("data-crayon")
                out.append(crayon.get(int(idx), "") if idx is not None else self.code_block(child))
            elif re.fullmatch(r"h[1-6]", tag):
                flush()
                inner = self.inline(child).strip()
                if inner:
                    out.append(f"{'#' * int(tag[1])} {inner}")
            elif tag == "p":
                flush()
                block = self.para_code(child)
                if block:
                    out.append(block)
                else:
                    inner = self.inline(child).strip()
                    if inner:
                        out.append(inner)
            elif tag in ("ul", "ol"):
                flush()
                out.append(self.list_block(child, crayon, tag == "ol", depth))
            elif tag == "blockquote":
                flush()
                body = "\n\n".join(self.blocks(child, crayon, depth))
                out.append("\n".join("> " + l for l in body.splitlines()))
            elif tag == "table":
                # 老站（如 2013 年的 sealiesoftware）用 table 做页面布局，不是数据表格。
                # 当成表格渲染会把整篇正文塞进单元格里毁掉。判据：单元格里含块级元素。
                flush()
                if self.is_layout_table(child):
                    out.extend(self.blocks(child, crayon, depth))
                else:
                    out.append(self.table(child))
            elif tag == "hr":
                flush()
                out.append("---")
            elif tag == "figure":
                flush()
                out.extend(self.blocks(child, crayon, depth))
            elif tag == "figcaption":
                flush()
                inner = self.inline(child).strip()
                if inner:
                    out.append(f"<sub>{inner}</sub>")
            elif tag == "img":
                flush()
                s = self.image(child)
                if s:
                    out.append(s)
            elif tag in PASSTHROUGH or tag in BLOCK_TAGS or tag == "center":
                # 结构容器：里面还有块级元素就递归；否则整块当一段收下，
                # 否则老站那种 <td> 里直接堆文本的写法会整段丢掉。
                flush()
                if any(isinstance(c.tag, str) and c.tag in BLOCK_TAGS for c in child):
                    out.extend(self.blocks(child, crayon, depth))
                else:
                    inner = self.inline(child).strip()
                    if inner:
                        out.append(inner)
            elif tag in INLINE_TAGS and not any(
                isinstance(c.tag, str) and c.tag in BLOCK_TAGS for c in child
            ):
                # 行内标签直接挂在块级容器下面：并入当前这一段，别单独成段、更别丢掉
                buf.append(self.inline_el(child))
            else:
                flush()
                if any(isinstance(c.tag, str) and c.tag in BLOCK_TAGS for c in child):
                    out.extend(self.blocks(child, crayon, depth))
                else:
                    inner = self.inline(child).strip()
                    if inner:
                        out.append(inner)
            if child.tail and child.tail.strip():
                buf.append(self.escape(child.tail))
        flush()
        return out

    def list_block(self, el, crayon: dict, ordered: bool, depth: int) -> str:
        lines: list[str] = []
        n = 0
        for li in el.xpath("./li"):
            n += 1
            marker = f"{n}." if ordered else "-"
            sub = self.blocks(li, crayon, depth + 1)
            # li 的直接文本（没被包在 p 里的那种）
            direct = self.inline(li).strip() if not sub else ""
            body = direct or "\n\n".join(sub)
            if not body:
                continue
            first, *rest = body.split("\n")
            lines.append(f"{'  ' * depth}{marker} {first}")
            for line in rest:
                lines.append(f"{'  ' * depth}  {line}" if line.strip() else "")
        return "\n".join(lines)

    def highlight_code(self, el) -> str | None:
        """处理「行号表格」式的代码高亮（Hexo / Jekyll / Rouge / Pygments 通用）。

        典型结构：

            <figure class="highlight swift"> 或 <code>
              <table><tr>
                <td class="gutter"><pre>1\\n2\\n3…</pre></td>   ← 只有行号
                <td class="code"><pre>真正的代码</pre></td>
              </tr></table>
            </figure>

        直接找 `<pre>` 会取到行号那一格，得到 `1\\n2\\n3` 这种垃圾，真代码全丢。
        Hexo 在中文技术博客里占主流，所以这个坑影响面很大。
        """
        gutter = el.xpath(".//td[contains(@class,'gutter')]")
        codecell = el.xpath(".//td[contains(@class,'code')]")
        if not (gutter and codecell):
            return None
        # 关键守卫：只有当这个元素**几乎只包含这段代码**时才当代码块处理。
        # 否则命中的是外层文章容器（它子树里恰好有个高亮表格），会把整篇正文
        # 换成一个代码块、其余内容全部丢失。踩过一次：maskray 的中位字数从
        # 15,626 掉到 573，sunnyxx 从 4,307 掉到 318。
        total = len((el.text_content() or "").strip())
        gut = sum(len((g.text_content() or "").strip()) for g in gutter)
        code_len = sum(len((c.text_content() or "").strip()) for c in codecell)
        if total - gut <= 0 or code_len / (total - gut) < 0.9:
            return None
        # 语言标注：从 class 里挑出语言名，剥掉 language- / lang- 前缀，
        # 并排除 highlighter-rouge / highlight 这类框架自带的类名
        lang = ""
        for cls in (el.get("class") or "").split():
            c = cls.lower()
            if c in ("highlight", "hljs", "code", "codeblock") or c.startswith("highlighter"):
                continue
            lang = re.sub(r"^(language|lang|brush)[-:]", "", c)
            break
        # td.code 里逐行取。Hexo 每行包一个元素，但标签随主题变：
        #   onevcat / 多数 Rouge 主题  → <span class="line">
        #   NexT 主题（southpeak 等）  → <div  class="line">
        # 只找 span 会漏掉 div 版，退化到 text_content() 时 <div> 之间没有换行，
        # 整块代码会被拼成一行（几十行 Swift 挤成一行），必须两种都认。
        lines = [
            el for el in codecell[0].xpath(".//span|.//div")
            if "line" in (el.get("class") or "").split()
        ]
        if lines:
            code = "\n".join(l.text_content() for l in lines)
        else:
            code = codecell[0].text_content()
        code = "\n".join(l.rstrip() for l in code.split("\n")).strip("\n")
        if not code:
            return None
        fence = "```"
        while fence in code:
            fence += "`"
        return f"{fence}{lang}\n{code}\n{fence}"

    def is_layout_table(self, el) -> bool:
        """判断一个 <table> 是页面布局还是真数据表格。

        判据（任一成立即视为布局）：
          - 单元格里含块级元素（p / h1-h6 / pre / ul / ol / div / table）
          - 只有一行或只有一个单元格
        真数据表格的单元格通常只有行内内容。
        """
        cells = el.xpath(".//td|.//th")
        if len(cells) <= 1:
            return True
        rows = el.xpath(".//tr")
        if len(rows) <= 1:
            return True
        for c in cells:
            if c.xpath("./p|./h1|./h2|./h3|./h4|./h5|./h6|./pre|./ul|./ol|./div|./table"):
                return True
        return False

    def para_code(self, el) -> str | None:
        """`<p>` 里只有一个 <code> 且含换行（<br> 或真换行）→ 当成代码块。

        老站没有 `<pre>`，代码是 `<p><code>…<br>…</code></p>` 这种写法（如
        sealiesoftware）。当行内 code 渲染会把多行代码压成一行，必须还原成块。
        """
        codes = el.xpath("./code")
        if len(codes) != 1:
            return None
        code = codes[0]
        # <p> 的文本必须几乎全在这个 code 里
        total = len((el.text_content() or "").strip())
        inner = len((code.text_content() or "").strip())
        if total == 0 or inner / total < 0.8:
            return None
        has_break = bool(code.xpath("./br")) or "\n" in (code.text_content() or "")
        if not has_break:
            return None
        # 用 <br> 还原换行
        lines: list[str] = []
        buf = [code.text or ""]
        for part in code:
            if isinstance(part.tag, str) and part.tag == "br":
                lines.append("".join(buf))
                buf = [part.tail or ""]
            else:
                buf.append(part.text_content() or "")
                buf.append(part.tail or "")
        lines.append("".join(buf))
        body = "\n".join(l.rstrip() for l in lines).strip("\n")
        if not body:
            return None
        fence = "```"
        while fence in body:
            fence += "`"
        return f"{fence}\n{body}\n{fence}"

    def table(self, el) -> str:
        rows = []
        for tr in el.xpath(".//tr"):
            cells = [
                re.sub(r"\s+", " ", self.inline(td)).replace("|", "\\|").strip()
                for td in tr.xpath("./th|./td")
            ]
            if cells:
                rows.append(cells)
        if not rows:
            return ""
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
        for r in rows[1:]:
            out.append("| " + " | ".join(r) + " |")
        return "\n".join(out)


def node_to_markdown(node, base_url: str = "", code_mode: str = "auto") -> tuple[str, list[str]]:
    """直接对一个已选中（并且已剔过样板）的节点做转换。

    调用方先拿到容器节点、按需删掉样板子树，再交给这里——比先序列化再用 XPath
    重新定位可靠得多。
    """
    conv = Converter(base_url=base_url, code_mode=code_mode)
    return conv.convert(node), conv.images


def to_markdown(html: str, container_xpath: str, base_url: str = "", code_mode: str = "auto") -> tuple[str, list[str]]:
    """返回 (markdown, 图片 URL 列表)。container_xpath 指向正文容器。"""
    doc = lxml.html.fromstring(html)
    nodes = doc.xpath(container_xpath)
    if not nodes:
        raise ValueError(f"正文容器未命中：{container_xpath}")
    return node_to_markdown(nodes[0], base_url, code_mode)
