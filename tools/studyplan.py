#!/usr/bin/env python3
"""把用户的《2026 暑假 iOS 底层学习计划》里的每个外链，映射到本地归档文件。

    python3 tools/studyplan.py            # 生成学习计划原表与暑期模块专题
    python3 tools/studyplan.py --report   # 只打印覆盖率统计，不写文件

## 生成的两种索引

归档了数千篇材料，计划提供学习顺序。脚本生成两种互补入口：

- `_indexes/study-plan.md`：计划点名的外链逐条映射到本地文件，便于补齐归档；
- `_indexes/summer/`：按计划的每个模块收拢仓库内全部相关文章，中文优先，
  再按计划核心、官方资料和深度补充排序。

## 映射规则

| 计划里的链接 | 本地位置 |
|---|---|
| `developer.apple.com/documentation/<path>` | `apple-docs/{en,zh}/<path>.md` |
| `developer.apple.com/videos/play/<coll>/<id>/` | `wwdc/{en,zh}/<coll>/<id>-*.md` |
| `developer.apple.com/library/archive/…` | 旧仓库 `apple-developer-archive-vault`（跨仓库，只给提示） |
| 第三方博客 | `blogs/{en,zh}/<source>/*.md`，按 frontmatter 的 source_url 反查 |
| GitHub 仓库 | `oss/<repo>/`（尚未 clone 的标注为待办） |
"""
from __future__ import annotations

import json
import os
import re
import shutil
import sys
import urllib.parse
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# 学习计划的位置。默认指向作者的 Obsidian vault，可用环境变量覆盖，
# 避免把个人路径写死在仓库里。
PLAN = Path(os.environ.get(
    "STUDY_PLAN",
    str(Path.home() / "Obsidian/iOS/10 学习计划/2026 暑假 iOS 底层学习计划.md"),
))
OUT = ROOT / "_indexes" / "study-plan.md"
IDX = ROOT / "_indexes"
SUMMER_INDEX = ROOT / "_indexes" / "summer.md"
SUMMER_DIR = ROOT / "_indexes" / "summer"

SUMMER_MODULES = (
    {
        "prefix": "模块 1",
        "slug": "01-object-memory",
        "title": "模块 1：对象模型与进程内存地图",
        "summary": "从虚拟地址空间、对象布局和 isa 链建立 Objective-C 对象模型。",
        "topics": ("Objective-C Runtime", "内存与 ARC"),
        "pattern": r"virtual memory|address space|heap|call stack|stack (?:memory|object)|"
        r"memory layout|isa|metaclass|"
        r"tagged pointer|object model|内存|堆|栈|对象模型|元类|内存对齐",
    },
    {
        "prefix": "模块 2",
        "slug": "02-ownership-arc-blocks",
        "title": "模块 2：所有权、ARC、weak、属性与 Block",
        "summary": "把内存管理关键字还原为所有权关系、编译器变换和运行时数据结构。",
        "topics": ("内存与 ARC", "Block 与闭包"),
        "pattern": r"arc|retain|release|autorelease|weak|ownership|reference count|property|"
        r"block|copy|引用计数|所有权|属性|循环引用",
    },
    {
        "prefix": "模块 3",
        "slug": "03-runtime",
        "title": "模块 3：Runtime：消息发送、转发、Category、KVO",
        "summary": "沿方法查找、转发、Category、关联对象和 KVC/KVO 建立运行时行为地图。",
        "topics": ("Objective-C Runtime", "架构、测试与工程实践"),
        "pattern": r"runtime|objc_msgsend|message|forward|category|swizzl|associated|kvc|kvo|"
        r"selector|运行时|消息|转发|关联对象|键值",
    },
    {
        "prefix": "模块 4",
        "slug": "04-concurrency",
        "title": "模块 4：线程、GCD、Operation、锁与 RunLoop",
        "summary": "从共享可变状态出发，理解线程、队列、锁、QoS 和事件循环的约束。",
        "topics": ("并发与线程", "RunLoop 与响应性", "性能与调试"),
        "pattern": r"thread|concurr|dispatch|gcd|operation|queue|lock|atomic|qos|runloop|"
        r"线程|并发|队列|锁|原子|事件循环",
    },
    {
        "prefix": "模块 5",
        "slug": "05-uikit-rendering",
        "title": "模块 5：UIKit、响应者链、渲染与列表性能",
        "summary": "从事件传递到像素上屏，串起视图生命周期、渲染和列表性能。",
        "topics": ("UI 与渲染", "RunLoop 与响应性", "性能与调试"),
        "pattern": r"uikit|view|responder|event|render|animation|table|collection|scroll|"
        r"offscreen|视图|响应者|事件|渲染|动画|列表|离屏",
    },
    {
        "prefix": "模块 6",
        "slug": "06-build-launch",
        "title": "模块 6：编译链接、Mach-O、dyld 与 App 启动",
        "summary": "沿源文件、目标文件、Mach-O、链接器和 dyld 追到冷启动优化。",
        "topics": ("启动、链接与二进制", "性能与调试"),
        "pattern": r"compile|compiler|link|macho|mach-o|dyld|binary|launch|startup|load|"
        r"编译|链接|二进制|启动|加载",
    },
    {
        "prefix": "模块 7",
        "slug": "07-data-architecture",
        "title": "模块 7：持久化、序列化、源码库与架构",
        "summary": "把本地存储、模型转换、源码阅读和工程架构放进同一条实践链路。",
        "topics": ("数据与持久化", "架构、测试与工程实践"),
        "pattern": r"core data|database|sqlite|file|persist|serial|json|model|architect|test|"
        r"持久化|数据库|文件|序列化|模型|架构|测试",
    },
    {
        "prefix": "模块 8",
        "slug": "08-os-network-database",
        "title": "模块 8：操作系统、网络与数据库基础",
        "summary": "补齐进程线程、虚拟内存、网络协议和数据库索引等通用基础。",
        "topics": ("并发与线程", "内存与 ARC", "网络与安全", "数据与持久化"),
        "pattern": r"process|thread|virtual memory|socket|tcp|udp|http|network|database|sqlite|"
        r"index|进程|线程|虚拟内存|网络|协议|数据库|索引",
    },
    {
        "prefix": "模块 9",
        "slug": "09-algorithms",
        "title": "模块 9：算法与数据结构并行线",
        "summary": "保留计划指定的算法与数据结构练习入口，不与 iOS 主题资料混排。",
        "topics": (),
        "pattern": r"$^",
    },
)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from indexes import collect_apple_docs, collect_blogs, collect_wwdc
from paths import safe_rel
from reader_navigation import display_status, preferred_title


SOURCE_VALUE_ORDER = {
    "alwaysprocessing": 0,
    "mikeash": 0,
    "objc": 0,
    "objcio": 0,
    "cocoawithlove": 0,
    "nshipster": 0,
    "ibireme": 0,
    "onevcat": 1,
    "objc-cn": 1,
    "objccn": 1,
}


def norm_url(url: str) -> str:
    """URL 规范化，用于跨来源比对。

    同一篇文章在计划里和在 frontmatter 里的写法经常不一致：http vs https、
    带不带 www、尾斜杠、`index.html`、锚点、查询串。不规范化的话，明明抓了
    305 篇的 mikeash 也会有链接匹配不上。
    """
    p = urllib.parse.urlparse(url.split("#")[0])
    host = p.netloc.lower().removeprefix("www.")
    path = p.path.rstrip("/")
    path = re.sub(r"/(index|_index)\.html?$", "", path)
    return f"{host}{path}".lower()


def build_blog_index() -> dict[str, Path]:
    """source_url → 本地 md 路径。译文优先，其次英文原文。"""
    idx: dict[str, Path] = {}
    for lang in ("zh", "en"):
        base = ROOT / "blogs" / lang
        if not base.exists():
            continue
        for f in base.rglob("*.md"):
            text = f.read_text(encoding="utf-8")[:1200]
            m = re.search(r"^source_url: '?([^'\n]+)'?$", text, re.M)
            if m:
                idx.setdefault(norm_url(m.group(1)), f)
    return idx


def build_wwdc_index() -> dict[tuple[str, str], Path]:
    idx: dict[tuple[str, str], Path] = {}
    base = ROOT / "wwdc" / "en"
    if base.exists():
        for f in base.rglob("*.md"):
            m = re.match(r"(\d+)-", f.name)
            if m:
                idx[(f.parent.name, m.group(1))] = f
    return idx


def parse_plan_text(text: str) -> list[dict]:
    """按当前计划的「## 模块 N」切段，提取各模块链接。"""
    entries: list[dict] = []
    module = ""
    for line in text.splitlines():
        if line.startswith("## "):
            match = re.match(r"^##\s+(模块\s+\d+[:：].*)$", line)
            module = match.group(1).strip() if match else ""
            continue
        if not module:
            continue
        for url in re.findall(r"https?://[^\s)\]]+", line):
            entries.append({"module": module, "url": url.rstrip(".,;")})
    return entries


def parse_plan() -> list[dict]:
    if not PLAN.exists():
        sys.exit(f"找不到学习计划：{PLAN}")
    return parse_plan_text(PLAN.read_text(encoding="utf-8"))


def parse_plan_steps_text(text: str) -> dict[str, list[tuple[str, str, str]]]:
    """读取各模块步骤表中的编号、内容和产出。"""
    result: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    module = ""
    for line in text.splitlines():
        if line.startswith("## "):
            match = re.match(r"^##\s+(模块\s+\d+[:：].*)$", line)
            module = match.group(1).strip() if match else ""
            continue
        if not module or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 3:
            continue
        if cells[0] in {"步骤", "方向", "阶段"} or all(
            re.fullmatch(r":?-+:?", cell) for cell in cells
        ):
            continue
        result[module].append(tuple(cells))
    return dict(result)


def parse_plan_steps() -> dict[str, list[tuple[str, str, str]]]:
    if not PLAN.exists():
        sys.exit(f"找不到学习计划：{PLAN}")
    return parse_plan_steps_text(PLAN.read_text(encoding="utf-8"))


def classify(url: str, blogs: dict, wwdc: dict) -> tuple[str, Path | None, str]:
    """返回 (类别, 本地文件或 None, 说明)。"""
    p = urllib.parse.urlparse(url)
    host, path = p.netloc.replace("www.", ""), p.path

    if host == "developer.apple.com":
        if path.startswith("/documentation/"):
            rel = safe_rel(path.rstrip("/"))
            f = ROOT / "apple-docs" / "en" / (rel + ".md")
            return ("Apple 现行文档", f if f.exists() else None, "" if f.exists() else "未归档")
        m = re.match(r"/videos/play/([^/]+)/(\d+)", path)
        if m:
            f = wwdc.get((m.group(1), m.group(2)))
            return ("WWDC", f, "" if f else "不在 178 场短名单里")
        if path.startswith("/library/archive/"):
            return ("Apple 旧归档", None, "在旧仓库 apple-developer-archive-vault")
        return ("Apple 其它", None, "")

    if host == "github.com":
        match = re.match(r"^/([^/]+)/([^/]+)/blob/[^/]+/(.+)$", path)
        if match:
            owner, repo, raw_rel = match.groups()
            rel = Path(urllib.parse.unquote(raw_rel))
            if not rel.is_absolute() and ".." not in rel.parts:
                if owner.lower() == "biscoffee" and repo == "apple-docs-vault":
                    target = ROOT / rel
                    return (
                        "本仓库资料",
                        target if target.is_file() else None,
                        "" if target.is_file() else "链接路径尚不存在",
                    )
                if (
                    owner.lower() == "xiyoumobile3g-ios"
                    and repo == "apple-developer-archive-vault"
                ):
                    candidates = (
                        ROOT / "legacy-archive" / "zh" / rel,
                        ROOT / "legacy-archive" / "en" / rel,
                        ROOT / "legacy-archive" / "vault" / rel,
                    )
                    target = next((item for item in candidates if item.is_file()), None)
                    return (
                        "Apple 旧归档",
                        target,
                        "" if target else "组织仓库当前也没有该路径",
                    )
        return ("GitHub 源码", None, "待 clone 到 oss/")

    f = blogs.get(norm_url(url))
    if f:
        return ("第三方博客", f, "")
    return ("第三方博客", None, f"未归档（{host}）")


def title_from_path(path: Path) -> str:
    """从本地页面读取可读标题，供暑期计划入口使用。"""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return path.stem
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            body = text[end + 5 :]
    match = re.search(r"^#\s+(.+?)\s*$", body, re.M)
    if match:
        title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", match.group(1))
        return re.sub(r"[`*_]", "", title).strip()
    frontmatter = re.search(r"^title:\s*['\"]?(.+?)['\"]?\s*$", text, re.M)
    if frontmatter:
        return frontmatter.group(1).strip()
    return path.stem


def relative_link(label: str, target: Path, page: Path) -> str:
    rel = os.path.relpath(target, page.parent)
    return f"[{label}]({urllib.parse.quote(rel, safe='/._~-')})"


def table_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().replace("|", r"\|")


def summer_module_for(heading: str) -> dict | None:
    for module in SUMMER_MODULES:
        if heading.startswith(module["prefix"]):
            return module
    return None


def entry_text(entry: dict) -> str:
    return " ".join(
        [
            entry.get("en_title", ""),
            entry.get("zh_title", ""),
            entry.get("title_alias", ""),
        ]
    )


def module_entry_matches(module: dict, entry: dict) -> bool:
    if not set(module["topics"]) & set(entry["topics"]):
        return False
    return bool(re.search(module["pattern"], entry_text(entry), re.I))


def direct_url_set(module_entries: list[dict]) -> set[str]:
    return {norm_url(entry["url"]) for entry in module_entries}


def is_direct_material(entry: dict, direct_urls: set[str]) -> bool:
    source_url = entry.get("source_url", "")
    return bool(source_url) and norm_url(source_url) in direct_urls


def collect_library_entries() -> list[dict]:
    """与通用主题目录使用同一批文章，避免两个目录口径不一致。"""
    apple, _ = collect_apple_docs()
    wwdc = collect_wwdc()
    blogs, _ = collect_blogs()
    return [entry for entry in [*apple, *wwdc, *blogs] if entry["reader_visible"]]


def article_value_key(entry: dict, direct_urls: set[str]) -> tuple[int, int, int, str]:
    """同一语言状态内的学习价值排序，优先尊重学习计划的人工取舍。"""
    if is_direct_material(entry, direct_urls):
        plan_rank = 0
    else:
        plan_rank = 1
    kind_rank = {
        "Apple 文档": 0,
        "WWDC": 1,
        "技术博客": 2,
        "网页快照": 3,
    }.get(entry["kind"], 4)
    source_rank = SOURCE_VALUE_ORDER.get(entry["source_key"], 2)
    return (plan_rank, kind_rank, source_rank, preferred_title(entry).casefold())


def priority_label(entry: dict, direct_urls: set[str]) -> str:
    if is_direct_material(entry, direct_urls):
        return "计划核心"
    if entry["kind"] in {"Apple 文档", "WWDC"}:
        return "官方资料"
    if SOURCE_VALUE_ORDER.get(entry["source_key"], 2) <= 1:
        return "深度补充"
    return "补充资料"


def article_table(
    entries: list[dict],
    target: Path,
    direct_urls: set[str],
) -> list[str]:
    lines = [
        "| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |",
        "|---|---|---|---|---|---|",
    ]
    for entry in sorted(entries, key=lambda value: article_value_key(value, direct_urls)):
        preferred = entry["zh"] or entry["en"]
        reading = (
            relative_link("中文", entry["zh"], target)
            if entry["zh"]
            else relative_link("英文", entry["en"], target)
        )
        lines.append(
            f"| {priority_label(entry, direct_urls)} "
            f"| {relative_link(table_text(preferred_title(entry)), preferred, target)} "
            f"| {table_text(entry['kind'])} | {table_text(entry['source_name'])} | {reading} "
            f"| {display_status(entry)} |"
        )
    return lines


def write_module_page(
    *,
    module: dict,
    steps: list[tuple[str, str, str]],
    module_entries: list[dict],
    library_entries: list[dict],
    target: Path,
) -> tuple[int, int]:
    """写一个计划模块页，并把计划原链与仓库扩展阅读放在一起。"""
    direct_urls = direct_url_set(module_entries)
    selected = [
        entry
        for entry in library_entries
        if module_entry_matches(module, entry)
        or is_direct_material(entry, direct_urls)
    ]
    chinese = [
        entry for entry in selected if entry["status"] in {"已翻译", "原生中文"}
    ]
    untranslated = [entry for entry in selected if entry not in chinese]
    topic_names = "、".join(module["topics"]) or "计划指定材料"

    lines = [
        f"# {module['title']}",
        "",
        f"> {module['summary']}",
        f"> 对应仓库范围：{topic_names}。中文正文优先，随后列出未翻译资料。",
        "",
        f"- {relative_link('返回暑期计划知识地图', SUMMER_INDEX, target)}",
        f"- {relative_link('查看全库主题地图', IDX / 'topics.md', target)}",
        "",
        "## 学习步骤",
        "",
        "| 步骤 | 内容 | 产出 |",
        "|---|---|---|",
    ]
    for number, content, output in steps:
        lines.append(
            f"| {table_text(number)} | {table_text(content)} | {table_text(output)} |"
        )

    lines += ["", "## 计划指定材料", ""]
    seen_urls: set[str] = set()
    for entry in module_entries:
        normalized = norm_url(entry["url"])
        if normalized in seen_urls:
            continue
        seen_urls.add(normalized)
        lines.append(summer_material_line(entry, target))
    if not seen_urls:
        lines.append("本模块没有单独指定外链。")

    lines += [
        "",
        "## 中文资料",
        "",
        f"共 {len(chinese)} 份。包含译文和原生中文文章。",
        "",
        *article_table(chinese, target, direct_urls),
        "",
        "## 未翻译资料",
        "",
        f"共 {len(untranslated)} 份。可能已有中文目录标题，但正文仍为英文。",
        "",
        *article_table(untranslated, target, direct_urls),
        "",
    ]
    target.write_text("\n".join(lines), encoding="utf-8")
    return len(chinese), len(untranslated)


def write_summer_indexes(entries: list[dict]) -> None:
    """按当前计划的 9 个模块生成知识地图。"""
    shutil.rmtree(SUMMER_DIR, ignore_errors=True)
    SUMMER_DIR.mkdir(parents=True, exist_ok=True)
    library_entries = collect_library_entries()
    plan_steps = parse_plan_steps()
    by_module: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        module = summer_module_for(entry["module"])
        if module:
            by_module[module["slug"]].append(entry)

    lines = [
        "# 暑期计划知识地图",
        "",
        "> 按本地 Obsidian 暑期计划的 9 个模块生成专题书架，而不是只列计划外链。",
        "> 每个模块保留原计划步骤和指定材料，再补充仓库内的相关中文与英文资料。",
        f"> 目录生成于 {date.today()}。计划原始链接总表见"
        f"{relative_link('学习计划 · 材料索引', OUT, SUMMER_INDEX)}。",
        "",
        "| 模块 | 步骤 | 计划材料 | 中文资料 | 未翻译资料 | 模块入口 |",
        "|---|---:|---:|---:|---:|---|",
    ]

    for module in SUMMER_MODULES:
        target = SUMMER_DIR / f"{module['slug']}.md"
        steps = next(
            (
                value
                for heading, value in plan_steps.items()
                if heading.startswith(module["prefix"])
            ),
            [],
        )
        module_entries = by_module.get(module["slug"], [])
        chinese, untranslated = write_module_page(
            module=module,
            steps=steps,
            module_entries=module_entries,
            library_entries=library_entries,
            target=target,
        )
        lines.append(
            f"| {module['title']} | {len(steps)} | {len(module_entries)} | "
            f"{chinese} | {untranslated} | "
            f"{relative_link('打开模块页', target, SUMMER_INDEX)} |"
        )

    SUMMER_INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")


def summer_material_line(entry: dict, page: Path) -> str:
    """生成计划材料索引中的单条链接。"""
    if entry["file"]:
        root_rel = entry["file"].relative_to(ROOT)
        zh_rel = Path(str(root_rel).replace("/en/", "/zh/", 1))
        zh = ROOT / zh_rel
        preferred = zh if zh.exists() else entry["file"]
        links = [relative_link(title_from_path(preferred), preferred, page)]
        if entry["file"] != preferred:
            links.append(relative_link("英文原文", entry["file"], page))
        if zh.exists() and entry["file"] != zh:
            links.append(relative_link("中文正文", zh, page))
        links.append(f"[原文网页]({entry['url']})")
        return f"- {' · '.join(links)} — {entry['cat']}"
    note = f"（{entry['note']}）" if entry["note"] else ""
    return f"- [计划材料]({entry['url']}) — {entry['cat']}{note}"


def main() -> None:
    blogs, wwdc = build_blog_index(), build_wwdc_index()
    entries = parse_plan()

    stats: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for e in entries:
        cat, f, note = classify(e["url"], blogs, wwdc)
        e["cat"], e["file"], e["note"] = cat, f, note
        stats[cat][0] += 1
        if f:
            stats[cat][1] += 1

    print(f"学习计划里共 {len(entries)} 个外链\n")
    print(f"{'类别':16}{'链接数':>7}{'已归档':>8}{'覆盖率':>8}")
    for cat, (tot, got) in sorted(stats.items(), key=lambda x: -x[1][0]):
        print(f"{cat:16}{tot:>7}{got:>8}{got / tot * 100:>7.0f}%")

    if "--report" in sys.argv:
        return

    write_summer_indexes(entries)

    lines = [
        "# 学习计划 · 材料索引",
        "",
        "> 由 `tools/studyplan.py` 从 `2026 暑假 iOS 底层学习计划.md` 自动生成。",
        "> 每一行是计划里点名的一份材料；有本地归档的给出链接，没有的标「未归档」。",
        "",
        "## 覆盖率",
        "",
        "| 类别 | 链接数 | 已归档 | 覆盖率 |",
        "|---|---:|---:|---:|",
    ]
    for cat, (tot, got) in sorted(stats.items(), key=lambda x: -x[1][0]):
        lines.append(f"| {cat} | {tot} | {got} | {got / tot * 100:.0f}% |")
    lines.append("")

    current_module = None
    seen: set[tuple] = set()
    for e in entries:
        if e["module"] != current_module:
            current_module = e["module"]
            lines += ["", f"## {current_module}", ""]
        key = (current_module, e["url"])
        if key in seen:
            continue
        seen.add(key)
        lines.append(summer_material_line(e, OUT))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n索引 → {OUT.relative_to(ROOT)}（{len(lines)} 行）")


if __name__ == "__main__":
    main()
