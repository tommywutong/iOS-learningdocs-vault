#!/usr/bin/env python3
"""把缓存的 DocC render JSON 渲染成 Obsidian 可读的 Markdown。

    python3 tools/render.py <archive>...          # 渲染成 en/<archive>/**.md
    python3 tools/render.py <archive> --longform  # 只渲染成篇文章，便于快速出样品

输入是 .cache/pages/ 下的原始 JSON（fetch.py 阶段 2 的产物），输出是 en/ 目录。
渲染是纯函数式的——不联网、可反复重跑，所以调格式不需要重抓。
图片不在这里下载，只登记到 meta/assets.json，由 fetch_assets.py 统一拉取。
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

from paths import ILLEGAL, cache_rel, safe_rel

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "pages"
META = ROOT / "meta"

# 仓库按「来源」分顶层目录，每个来源内部再按语言分 en/zh。
# 这样 Apple 文档、WWDC 逐字稿、第三方博客不会混在同一层。
# attachments/ 放在仓库根，三个来源共用一份，避免同一张图存多次。
EN = ROOT / "apple-docs" / "en"

# aside 的 name → Obsidian callout 类型
ASIDE_MAP = {
    "note": "note",
    "important": "important",
    "warning": "warning",
    "tip": "tip",
    "experiment": "example",
    "attention": "warning",
    "author": "quote",
    "authors": "quote",
    "bug": "bug",
    "complexity": "abstract",
    "copyright": "quote",
    "date": "info",
    "invariant": "info",
    "mutatingvariant": "info",
    "nonmutatingvariant": "info",
    "postcondition": "info",
    "precondition": "info",
    "remark": "note",
    "requires": "info",
    "since": "info",
    "todo": "todo",
    "version": "info",
    "throws": "danger",
    "seealso": "info",
    "deprecated": "warning",
}


def md_escape(text: str) -> str:
    """正文纯文本里会被 Markdown 误读的字符。

    刻意保守：只处理行首标记和最容易误伤的行内标记，不做全量转义，
    否则 Apple 文档里大量的 `*`、`_` 会被塞满反斜杠、译者读起来很痛苦。
    """
    text = text.replace("\\", "\\\\")
    text = re.sub(r"([<>])", r"\\\1", text)
    return text


class Renderer:
    # md 文件写在 apple-docs/en/ 下，但 attachments/ 在仓库根（各语言各来源共用）。
    # 算图片相对路径时必须把这些层级算进去，否则 ../attachments 会指向错的地方。
    OUT_DIR = "apple-docs/en"

    def __init__(self, archive: str, doc_path: str, data: dict, assets: dict) -> None:
        self.archive = archive
        self.doc_path = doc_path
        self.d = data
        self.refs: dict = data.get("references", {})
        self.assets = assets
        self.self_rel = safe_rel(doc_path)

    # ------------------------------------------------------------ 链接

    def link_to(self, url: str) -> str:
        """把 /documentation/... 的绝对路径转成相对本文件的 Markdown 链接目标。"""
        target = safe_rel(url.split("#")[0])
        anchor = url.split("#", 1)[1] if "#" in url else ""
        here = Path(self.self_rel).parent
        rel = os.path.relpath(target + ".md", here if str(here) != "." else "")
        if anchor:
            rel += "#" + anchor
        return rel

    def wrap_dest(self, dest: str) -> str:
        """含括号或空格的链接目标用尖括号包住，避免 Markdown 解析歧义。"""
        return f"<{dest}>" if re.search(r"[()\s]", dest) else dest

    def resolve(self, identifier: str) -> tuple[str, str] | None:
        """引用 → (显示文字, 链接目标)。无法解析的返回 None。"""
        ref = self.refs.get(identifier)
        if not ref:
            return None
        rtype = ref.get("type")
        title = ref.get("title") or self.inline(ref.get("titleInlineContent", []))
        if rtype == "topic":
            url = ref.get("url")
            if not url:
                return None
            # 符号类引用用 navigatorTitle 更贴近代码里的写法
            nav = ref.get("navigatorTitle")
            if nav and ref.get("kind") == "symbol":
                title = "".join(t.get("text", "") for t in nav)
            return title, self.link_to(url)
        if rtype in ("link", "download"):
            return title or ref.get("url", ""), ref.get("url", "")
        return None

    # ------------------------------------------------------------ 行内

    def inline(self, nodes: list) -> str:
        out = []
        for n in nodes or []:
            if not isinstance(n, dict):
                continue
            t = n.get("type")
            if t == "text":
                out.append(md_escape(n.get("text", "")))
            elif t == "codeVoice":
                code = n.get("code", "")
                out.append(f"`{code}`" if code else "")
            elif t == "emphasis":
                out.append(f"_{self.inline(n.get('inlineContent', []))}_")
            elif t in ("strong", "inlineHead"):
                out.append(f"**{self.inline(n.get('inlineContent', []))}**")
            elif t == "strikethrough":
                out.append(f"~~{self.inline(n.get('inlineContent', []))}~~")
            elif t == "reference":
                r = self.resolve(n.get("identifier", ""))
                if r:
                    text, dest = r
                    inner = self.inline(n.get("overridingTitleInlineContent", [])) or md_escape(text)
                    out.append(f"[{inner}]({self.wrap_dest(dest)})")
                else:
                    # 解析不了的（如 externally.resolved.symbol）退化成行内代码
                    ident = n.get("identifier", "")
                    out.append(f"`{ident.rsplit('/', 1)[-1]}`" if ident else "")
            elif t == "image":
                out.append(self.image(n))
            elif t == "inlineHTML":
                out.append(n.get("html", ""))
            elif t == "newTerm":
                out.append(f"**{self.inline(n.get('inlineContent', []))}**")
            elif "inlineContent" in n:
                out.append(self.inline(n["inlineContent"]))
        return "".join(out)

    # ------------------------------------------------------------ 资源

    def image(self, node: dict) -> str:
        ident = node.get("identifier", "")
        ref = self.refs.get(ident, {})
        variants = ref.get("variants", [])
        if not variants:
            return ""
        # 优先 light + 2x，其次任意
        best = next(
            (v for v in variants if "light" in v.get("traits", []) and "2x" in v.get("traits", [])),
            None,
        ) or next((v for v in variants if "light" in v.get("traits", [])), None) or variants[0]
        url = best.get("url", "")
        if not url:
            return ""
        local = self.register_asset(url)
        alt = md_escape(ref.get("alt") or node.get("alt") or "")
        # 注意要带上 OUT_DIR：md 在 en/ 下，attachments/ 在仓库根
        here = Path(self.OUT_DIR) / Path(self.self_rel).parent
        rel = os.path.relpath(local, here)
        # Apple 的 alt 常常是完整的无障碍描述，动辄上千字符，直接塞进 ![] 里
        # 会把整行撑爆、译者没法读。超长的挪到下一行当图注，内容不丢。
        if len(alt) > 120:
            return f"![]({self.wrap_dest(rel)})\n\n<sub>{alt}</sub>"
        return f"![{alt}]({self.wrap_dest(rel)})"

    def register_asset(self, url: str) -> str:
        """把远端资源登记到 assets 表，返回它在仓库里的相对路径。"""
        parsed = urllib.parse.urlparse(url)
        name = urllib.parse.unquote(Path(parsed.path).name)
        # docs-assets 的路径里带内容哈希目录，拿来做去重目录名
        parts = [p for p in parsed.path.split("/") if p]
        bucket = parts[-2] if len(parts) >= 2 else "misc"
        local = f"attachments/{bucket}/{re.sub(ILLEGAL, '_', name)}"
        self.assets[url] = local
        return local

    # ------------------------------------------------------------ 块

    def blocks(self, nodes: list, depth: int = 0) -> list[str]:
        out: list[str] = []
        for n in nodes or []:
            if not isinstance(n, dict):
                continue
            t = n.get("type")
            if t == "paragraph":
                s = self.inline(n.get("inlineContent", [])).strip()
                if s:
                    out.append(s)
            elif t == "heading":
                lvl = min(max(int(n.get("level", 2)), 2), 6)
                out.append(f"{'#' * lvl} {self.inline([{'type': 'text', 'text': n.get('text', '')}])}")
            elif t == "codeListing":
                lang = n.get("syntax") or ""
                code = "\n".join(n.get("code", []))
                out.append(f"```{lang}\n{code}\n```")
            elif t == "aside":
                name = (n.get("name") or "Note").strip()
                kind = ASIDE_MAP.get(name.lower().replace(" ", ""), "note")
                body = self.blocks(n.get("content", []), depth)
                inner = "\n>\n".join("> " + b.replace("\n", "\n> ") for b in body)
                out.append(f"> [!{kind}] {name}\n{inner}" if inner else f"> [!{kind}] {name}")
            elif t == "unorderedList":
                out.append(self.list_items(n.get("items", []), depth, ordered=False))
            elif t == "orderedList":
                out.append(self.list_items(n.get("items", []), depth, ordered=True))
            elif t == "termList":
                lines = []
                for item in n.get("items", []):
                    term = self.inline(item.get("term", {}).get("inlineContent", []))
                    defn = " ".join(self.blocks(item.get("definition", {}).get("content", []), depth))
                    lines.append(f"- **{term}** — {defn}")
                out.append("\n".join(lines))
            elif t == "table":
                out.append(self.table(n))
            elif t == "image":
                s = self.image(n)
                if s:
                    out.append(s)
            elif t == "video":
                ref = self.refs.get(n.get("identifier", ""), {})
                variants = ref.get("variants", [])
                if variants:
                    alt = md_escape(ref.get("alt", "") or "视频")
                    out.append(f"[{alt}]({variants[0].get('url', '')})")
            elif t == "tabNavigator":
                for tab in n.get("tabs", []):
                    out.append(f"**{md_escape(tab.get('title', ''))}**")
                    out.extend(self.blocks(tab.get("content", []), depth))
            elif t == "links":
                items = []
                for ident in n.get("items", []):
                    r = self.resolve(ident)
                    if r:
                        items.append(f"- [{md_escape(r[0])}]({self.wrap_dest(r[1])})")
                if items:
                    out.append("\n".join(items))
            elif t == "row":
                for col in n.get("columns", []):
                    out.extend(self.blocks(col.get("content", []), depth))
            elif t == "small":
                out.append(f"<sub>{self.inline(n.get('inlineContent', []))}</sub>")
            elif t == "dictionaryExample":
                code = n.get("example", {}).get("code", [])
                out.append("```json\n" + "\n".join(code) + "\n```")
            elif "content" in n:
                out.extend(self.blocks(n["content"], depth))
            elif "inlineContent" in n:
                s = self.inline(n["inlineContent"]).strip()
                if s:
                    out.append(s)
        return out

    def list_items(self, items: list, depth: int, ordered: bool) -> str:
        lines = []
        for i, item in enumerate(items, 1):
            marker = f"{i}." if ordered else "-"
            body = self.blocks(item.get("content", []), depth + 1)
            if not body:
                continue
            first, *rest = "\n\n".join(body).split("\n")
            lines.append(f"{'  ' * depth}{marker} {first}")
            for line in rest:
                lines.append(f"{'  ' * depth}  {line}" if line.strip() else "")
        return "\n".join(lines)

    def table(self, n: dict) -> str:
        rows = n.get("rows", [])
        if not rows:
            return ""
        def cell(c):
            return " ".join(self.blocks(c)).replace("\n", " ").replace("|", "\\|").strip()
        header = [cell(c) for c in rows[0]]
        width = max(len(r) for r in rows)
        header += [""] * (width - len(header))
        lines = ["| " + " | ".join(header) + " |", "|" + "---|" * width]
        for r in rows[1:]:
            cells = [cell(c) for c in r] + [""] * (width - len(r))
            lines.append("| " + " | ".join(cells) + " |")
        return "\n".join(lines)

    # ------------------------------------------------------------ 结构化区块

    def declarations(self, section: dict) -> list[str]:
        out = []
        for decl in section.get("declarations", []):
            langs = decl.get("languages", ["swift"])
            lang = "objc" if langs == ["occ"] else "swift"
            code = "".join(t.get("text", "") for t in decl.get("tokens", []))
            plats = decl.get("platforms") or []
            if plats:
                out.append(f"<sub>{', '.join(plats)}</sub>")
            out.append(f"```{lang}\n{code}\n```")
        return out

    def parameters(self, section: dict) -> list[str]:
        # en/ 是英文基线，结构性标题一律英文；译成中文是 zh/ 那一侧的事
        out = ["## Parameters"]
        for p in section.get("parameters", []):
            name = p.get("name", "")
            body = " ".join(self.blocks(p.get("content", []))).replace("\n", " ")
            out.append(f"- `{name}` — {body}")
        return out

    def topic_like(self, sections: list, heading: str) -> list[str]:
        out = []
        for sec in sections or []:
            title = sec.get("title")
            out.append(f"### {md_escape(title)}" if title else f"### {heading}")
            # 列表项攒成一个块再输出，否则块间空行会让它变成松散列表
            bullets: list[str] = []
            items = sec.get("identifiers") or sec.get("constraints") or []
            for ident in items:
                r = self.resolve(ident)
                if not r:
                    continue
                ref = self.refs.get(ident, {})
                abstract = self.inline(ref.get("abstract", []))
                line = f"- [{md_escape(r[0])}]({self.wrap_dest(r[1])})"
                if abstract:
                    line += f" — {abstract}"
                if ref.get("deprecated"):
                    line += " _(deprecated)_"
                elif ref.get("beta"):
                    line += " _(beta)_"
                bullets.append(line)
            if bullets:
                out.append("\n".join(bullets))
        return out

    def relationships(self) -> list[str]:
        out = []
        for sec in self.d.get("relationshipsSections", []) or []:
            names = []
            for ident in sec.get("identifiers", []):
                r = self.resolve(ident)
                if r:
                    names.append(f"[{md_escape(r[0])}]({self.wrap_dest(r[1])})")
            if names:
                out.append(f"- **{md_escape(sec.get('title', ''))}**: " + ", ".join(names))
        return ["## Relationships", *out] if out else []

    # ------------------------------------------------------------ frontmatter

    def frontmatter(self, page: dict, content_hash: str) -> str:
        m = self.d.get("metadata", {})
        plats = []
        for p in m.get("platforms", []) or []:
            name = p.get("name", "")
            intro = p.get("introducedAt")
            s = f"{name} {intro}+" if intro else name
            if p.get("beta"):
                s += " beta"
            if p.get("deprecatedAt"):
                s += f"（{p['deprecatedAt']} 起废弃）"
            plats.append(s)
        modules = [mm.get("name", "") for mm in m.get("modules", []) or []]

        def q(v: str) -> str:
            # 冒号、井号、引号、以特殊字符开头的值都要引号
            if v == "" or re.search(r"[:#\[\]{}&*!|>'\"%@`]", v) or v[0] in " -?":
                return "'" + v.replace("'", "''") + "'"
            return v

        fields = [
            ("title", q(m.get("title", page.get("title", "")))),
            ("framework", q(modules[0] if modules else self.archive)),
            ("symbol_kind", q(m.get("symbolKind") or self.d.get("kind", ""))),
            ("role", q(m.get("role", ""))),
            ("role_heading", q(m.get("roleHeading", ""))),
            ("platforms", "[" + ", ".join(q(p) for p in plats) + "]" if plats else "[]"),
            ("languages", "[" + ", ".join(page.get("langs", [])) + "]"),
            ("beta", "true" if page.get("beta") else "false"),
            ("deprecated", "true" if page.get("deprecated") or self.d.get("deprecationSummary") else "false"),
            ("doc_path", q(self.doc_path)),
            ("source_url", q("https://developer.apple.com" + self.doc_path)),
            ("doc_json", q("https://developer.apple.com/tutorials/data/documentation"
                           + urllib.parse.quote(self.doc_path.removeprefix('/documentation')) + ".json")),
            ("content_hash", q(content_hash)),
            ("translated", "false"),
        ]
        lines = ["---"] + [f"{k}: {v}" for k, v in fields] + ["---"]
        return "\n".join(lines)

    # ------------------------------------------------------------ 主渲染

    def render(self, page: dict, content_hash: str) -> str:
        # parts 里每一项都是一个独立的块，最后用空行连接。
        # 不能用单换行连接——相邻的两个段落会被 Markdown 合并成一段。
        m = self.d.get("metadata", {})
        parts = [self.frontmatter(page, content_hash)]

        # 面包屑：用 hierarchy.paths 的第一条
        crumbs = []
        paths = (self.d.get("hierarchy") or {}).get("paths") or []
        if paths:
            for ident in paths[0]:
                r = self.resolve(ident)
                if r:
                    crumbs.append(f"[{md_escape(r[0])}]({self.wrap_dest(r[1])})")
        if crumbs:
            parts.append("> Navigation: " + " · ".join(crumbs))

        title = m.get("title", page.get("title", ""))
        heading = m.get("roleHeading")
        parts.append(f"# {md_escape(title)}")
        if heading:
            parts.append(f"<sub>{md_escape(heading)}</sub>")

        if self.d.get("abstract"):
            parts.append(self.inline(self.d["abstract"]))

        if self.d.get("deprecationSummary"):
            body = " ".join(self.blocks(self.d["deprecationSummary"]))
            parts.append(f"> [!warning] Deprecated\n> {body}")

        for sec in self.d.get("primaryContentSections", []) or []:
            kind = sec.get("kind")
            if kind == "declarations":
                parts.extend(self.declarations(sec))
            elif kind == "parameters":
                parts.extend(self.parameters(sec))
            elif kind in ("content", "details"):
                parts.extend(self.blocks(sec.get("content", [])))
            elif kind == "mentions":
                # 「在这些文章里被提到」——是导航噪音，不进正文
                continue

        parts.extend(self.relationships())

        topics = self.topic_like(self.d.get("topicSections", []), "Topics")
        if topics:
            parts.extend(["## Topics", *topics])

        default_impl = self.topic_like(
            self.d.get("defaultImplementationsSections", []), "Default Implementations"
        )
        if default_impl:
            parts.extend(["## Default Implementations", *default_impl])

        see = self.topic_like(self.d.get("seeAlsoSections", []), "See Also")
        if see:
            parts.extend(["## See Also", *see])

        dl = self.d.get("sampleCodeDownload") or {}
        ident = (dl.get("action") or {}).get("identifier")
        if ident:
            ref = self.refs.get(ident, {})
            if ref.get("url"):
                parts.extend(
                    ["## Download", f"- [{Path(ref['url']).name}]({ref['url']})"]
                )

        text = "\n\n".join(p for p in parts if p and p.strip())
        text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
        return text


# ---------------------------------------------------------------- 驱动


def render_archive(archive: str, longform_only: bool = False) -> dict:
    mf = META / "manifest" / f"{archive}.json"
    if not mf.exists():
        sys.exit(f"缺 meta/manifest/{archive}.json，先跑 fetch.py index {archive}")
    manifest = json.loads(mf.read_text(encoding="utf-8"))
    pages = manifest["pages"]
    if longform_only:
        pages = [p for p in pages if p["longform"]]

    assets: dict[str, str] = {}
    written = missing = failed = 0
    seen_files: dict[str, str] = {}
    collisions = []

    for page in pages:
        # 必须和 fetch.py 用同一个函数算缓存路径，否则会出现「抓到了但说缺文件」
        cache_file = CACHE / cache_rel(archive, page["path"])
        if not cache_file.exists():
            missing += 1
            continue
        try:
            data = json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  [坏 JSON] {cache_file}: {e}", file=sys.stderr)
            failed += 1
            continue

        import hashlib

        content_hash = "sha256:" + hashlib.sha256(cache_file.read_bytes()).hexdigest()[:16]
        r = Renderer(archive, page["path"], data, assets)
        try:
            text = r.render(page, content_hash)
        except Exception as e:
            print(f"  [渲染失败] {page['path']}: {type(e).__name__}: {e}", file=sys.stderr)
            failed += 1
            continue

        out = EN / (safe_rel(page["path"]) + ".md")
        key = str(out).lower()
        if key in seen_files and seen_files[key] != page["path"]:
            collisions.append((seen_files[key], page["path"]))
        seen_files[key] = page["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        written += 1

    print(
        f"  {archive}: 写出 {written} 个 md，缺缓存 {missing}，失败 {failed}，"
        f"待下载资源 {len(assets)}"
    )
    if collisions:
        print(f"  [警告] {len(collisions)} 组路径清洗后撞名：", file=sys.stderr)
        for a, b in collisions[:5]:
            print(f"    {a}\n    {b}", file=sys.stderr)
    return assets


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    longform = "--longform" in sys.argv
    if not args:
        sys.exit(__doc__)

    all_assets: dict[str, str] = {}
    for archive in args:
        all_assets.update(render_archive(archive, longform))

    path = META / "assets.json"
    existing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    existing.update(all_assets)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(existing, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"资源清单 → meta/assets.json（累计 {len(existing)} 项）")


if __name__ == "__main__":
    main()
