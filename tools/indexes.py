#!/usr/bin/env python3
"""生成面向读者的导航索引。

    python3 tools/indexes.py

README.md 是人工维护的稳定入口，本脚本不再覆盖它。动态统计、来源目录、文章级目录、
主题目录和翻译状态全部写入 _indexes/。生成后应运行 tools/check_links.py。
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import urllib.parse
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IDX = ROOT / "_indexes"
SOURCES = IDX / "sources"
TOPICS = IDX / "topics"

LONGFORM_KINDS = {"article", "overview", "collection", "sampleCode", "module"}
LONGFORM_ROLES = {"article", "collectionGroup", "sampleCode"}

TOPIC_RULES: tuple[tuple[str, str], ...] = (
    (
        "Objective-C Runtime",
        r"\bobjective-c\b|\bobjc\b|\bruntime\b|\bisa\b|selector|method swizzl|"
        r"message forwarding|associated object|tagged pointer|class object|metaclass",
    ),
    (
        "内存与 ARC",
        r"\bmemory\b|\barc\b|retain|release|autorelease|\bweak\b|reference count|"
        r"\bheap\b|\bstack\b|\bmalloc\b|\bleak\b|\bvmmap\b|allocation|ownership|pointer",
    ),
    (
        "Block 与闭包",
        r"\bblocks?\b|\bclosures?\b|capture list|escaping closure",
    ),
    (
        "RunLoop 与响应性",
        r"run\s*loop|runloop|event loop|display\s*link|\btimer\b|\bhangs?\b|\bhitches?\b|"
        r"responsiveness|main thread stall",
    ),
    (
        "并发与线程",
        r"concurren|\bthreads?\b|\bgcd\b|grand central dispatch|\bdispatch\b|\blocks?\b|"
        r"\bmutex\b|semaphore|data race|\bactors?\b|async|await|sendable|atomic",
    ),
    (
        "性能与调试",
        r"performance|profil|instruments|\bdebug|lldb|\bcrash|optimi[sz]|benchmark|"
        r"sanitizer|diagnos|memory graph",
    ),
    (
        "启动、链接与二进制",
        r"\blaunch|\bdyld\b|mach-o|\blinkers?\b|\blinking\b|binary|dylib|"
        r"dynamic librar|framework|load time|app size|compil",
    ),
    (
        "网络与安全",
        r"\bnetwork|\bhttp|\bhttps|\btls\b|\bssl\b|urlsession|\bsocket|security|"
        r"certificate|crypt|authentication|authorization|keychain",
    ),
    (
        "UI 与渲染",
        r"\buikit\b|\bswiftui\b|\bviews?\b|\blayout\b|\banimation|\brender|graphics|"
        r"\bmetal\b|\bimages?\b|collection view|table view|core animation",
    ),
    (
        "Swift 语言",
        r"\bswift\b|\bgenerics?\b|\bprotocols?\b|\bmacros?\b|type inference|"
        r"value semantics|copyable|existential",
    ),
    (
        "数据与持久化",
        r"core data|\bdatabase|\bsqlite\b|\bjson\b|file system|persistence|storage|"
        r"userdefaults|serialization|archive",
    ),
    (
        "架构、测试与工程实践",
        r"\barchitecture\b|design pattern|\btesting\b|\btests?\b|api design|dependency|"
        r"modular|package manager|continuous integration|\bci\b",
    ),
)

WWDC_GROUP_TOPICS = {
    "A": ("Objective-C Runtime", "Swift 语言"),
    "B": ("内存与 ARC",),
    "C": ("并发与线程",),
    "D": ("RunLoop 与响应性", "性能与调试"),
    "E": ("UI 与渲染", "性能与调试"),
    "F": ("启动、链接与二进制",),
    "G": ("性能与调试",),
    "H": ("数据与持久化",),
    "I": ("网络与安全",),
}


def read_fm(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")[:5000]
    except Exception:
        return {}
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fm: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            value = value.strip()
            if len(value) >= 2 and value.startswith("'") and value.endswith("'"):
                value = value[1:-1].replace("''", "'")
            elif len(value) >= 2 and value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            fm[key.strip()] = value
    return fm


def plain_heading(value: str) -> str:
    value = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    return value.replace("`", "").strip()


def display_title(path: Path, fm: dict[str, str] | None = None) -> str:
    """正文 H1 比易受网页摘要污染的 frontmatter title 更适合作展示标题。"""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return path.stem
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            body = text[end + 5 :]
    heading = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    if heading:
        return plain_heading(heading.group(1))
    return plain_heading((fm or read_fm(path)).get("title") or path.stem)


def table_text(value: str) -> str:
    return re.sub(r"\s+", " ", str(value)).replace("|", r"\|").strip()


def relative_url(target: Path, page: Path) -> str:
    rel = os.path.relpath(target, page.parent)
    return urllib.parse.quote(rel, safe="/._~-")


def local_link(label: str, target: Path | None, page: Path) -> str:
    if target is None:
        return "—"
    return f"[{table_text(label)}]({relative_url(target, page)})"


def external_link(label: str, url: str) -> str:
    return f"[{table_text(label)}]({url})" if url else ""


def is_longform(fm: dict[str, str]) -> bool:
    return (
        fm.get("symbol_kind") in LONGFORM_KINDS
        or fm.get("role") in LONGFORM_ROLES
    )


def classify_topics(text: str) -> tuple[str, ...]:
    haystack = text.casefold()
    found = [
        name
        for name, pattern in TOPIC_RULES
        if re.search(pattern, haystack, re.IGNORECASE)
    ]
    return tuple(found[:3])


def item(
    *,
    kind: str,
    source_key: str,
    source_name: str,
    en: Path | None,
    zh: Path | None,
    source_url: str,
    en_fm: dict[str, str] | None = None,
    zh_fm: dict[str, str] | None = None,
    topics: tuple[str, ...] = (),
) -> dict:
    en_fm = en_fm or (read_fm(en) if en else {})
    zh_fm = zh_fm or (read_fm(zh) if zh else {})
    en_title = display_title(en, en_fm) if en else ""
    zh_title = display_title(zh, zh_fm) if zh else ""
    if en and zh:
        status = "已翻译"
    elif en:
        status = "待翻译"
    else:
        status = "原生中文"
    derived_topics = classify_topics(" ".join([en_title, zh_title, source_name]))
    return {
        "kind": kind,
        "source_key": source_key,
        "source_name": source_name,
        "en": en,
        "zh": zh,
        "en_title": en_title,
        "zh_title": zh_title,
        "source_url": source_url,
        "status": status,
        "topics": tuple(dict.fromkeys((*topics, *derived_topics)))[:3],
    }


def catalog_header(title: str, note: str) -> list[str]:
    return [
        f"# {title}",
        "",
        f"> {note}",
        f"> 自动生成于 {date.today()}，请勿手工编辑；运行 `python3 tools/indexes.py` 刷新。",
        "",
        "| 中文标题 | 英文标题 | 作者/来源 | 主题 | 原文 | 译文 | 翻译状态 |",
        "|---|---|---|---|---|---|---|",
    ]


def catalog_row(entry: dict, page: Path) -> str:
    if entry["en"]:
        original = local_link("英文", entry["en"], page)
        if entry["source_url"]:
            original += " · " + external_link("网页", entry["source_url"])
    else:
        original = local_link("中文原文", entry["zh"], page)
        if entry["source_url"]:
            original += " · " + external_link("网页", entry["source_url"])
    translation = local_link("中文", entry["zh"], page) if entry["en"] else "—"
    topics = "、".join(entry["topics"]) or "—"
    return (
        f"| {table_text(entry['zh_title']) or '—'} "
        f"| {table_text(entry['en_title']) or '—'} "
        f"| {table_text(entry['source_name'])} "
        f"| {table_text(topics)} "
        f"| {original} | {translation} | {entry['status']} |"
    )


def load_blog_configs() -> dict[str, dict]:
    configs: dict[str, dict] = {}
    for name in ("blog_sources.json", "blog_sources_batch2.json"):
        path = ROOT / "meta" / name
        if not path.exists():
            continue
        for source in json.loads(path.read_text(encoding="utf-8")).get("sources", []):
            configs[source["key"]] = source
    return configs


def collect_apple_docs() -> tuple[list[dict], dict[str, dict]]:
    en_root = ROOT / "apple-docs" / "en"
    zh_root = ROOT / "apple-docs" / "zh"
    entries: list[dict] = []
    stats: dict[str, dict] = defaultdict(
        lambda: {"total": 0, "longform": 0, "translated": 0}
    )
    for path in en_root.rglob("*.md"):
        rel = path.relative_to(en_root)
        framework_key = rel.parts[0] if len(rel.parts) > 1 else path.stem
        fm = read_fm(path)
        data = stats[framework_key]
        data["total"] += 1
        zh = zh_root / rel
        if zh.exists():
            data["translated"] += 1
        if not is_longform(fm):
            continue
        data["longform"] += 1
        framework = fm.get("framework") or framework_key
        entries.append(
            item(
                kind="Apple 文档",
                source_key=framework_key,
                source_name=f"Apple · {framework}",
                en=path,
                zh=zh if zh.exists() else None,
                source_url=fm.get("source_url", ""),
                en_fm=fm,
                topics=classify_topics(f"{framework} {fm.get('title', '')}"),
            )
        )
    return entries, stats


def collect_wwdc() -> list[dict]:
    en_root = ROOT / "wwdc" / "en"
    zh_root = ROOT / "wwdc" / "zh"
    entries: list[dict] = []
    for path in en_root.rglob("*.md"):
        rel = path.relative_to(en_root)
        fm = read_fm(path)
        group = fm.get("group", "")
        letter = group[:1]
        entries.append(
            item(
                kind="WWDC",
                source_key=rel.parts[0],
                source_name=f"Apple · {rel.parts[0].upper()}",
                en=path,
                zh=(zh_root / rel) if (zh_root / rel).exists() else None,
                source_url=fm.get("source_url", ""),
                en_fm=fm,
                topics=WWDC_GROUP_TOPICS.get(letter, ()),
            )
        )
    return entries


def collect_blogs() -> tuple[list[dict], dict[str, dict]]:
    configs = load_blog_configs()
    en_root = ROOT / "blogs" / "en"
    zh_root = ROOT / "blogs" / "zh"
    keys = {
        p.name
        for base in (en_root, zh_root)
        if base.exists()
        for p in base.iterdir()
        if p.is_dir()
    }
    entries: list[dict] = []
    per_source: dict[str, dict] = {}
    for key in sorted(keys):
        cfg = configs.get(key, {})
        source_name = cfg.get("name") or key
        en_files = {
            p.relative_to(en_root / key): p
            for p in (en_root / key).glob("*.md")
        } if (en_root / key).exists() else {}
        zh_files = {
            p.relative_to(zh_root / key): p
            for p in (zh_root / key).glob("*.md")
        } if (zh_root / key).exists() else {}
        source_entries: list[dict] = []
        for rel in sorted(set(en_files) | set(zh_files), key=str):
            en = en_files.get(rel)
            zh = zh_files.get(rel)
            fm = read_fm(en or zh)
            source_entries.append(
                item(
                    kind="技术博客",
                    source_key=key,
                    source_name=source_name,
                    en=en,
                    zh=zh,
                    source_url=fm.get("source_url", ""),
                    en_fm=fm if en else None,
                    zh_fm=fm if zh else None,
                )
            )
        entries.extend(source_entries)
        per_source[key] = {
            "name": source_name,
            "status": cfg.get("status", ""),
            "license": cfg.get("license", "未记录"),
            "entries": source_entries,
            "en_dir": (en_root / key) if (en_root / key).exists() else None,
            "zh_dir": (zh_root / key) if (zh_root / key).exists() else None,
        }

    snapshots = ROOT / "blogs" / "snapshots"
    snapshot_entries: list[dict] = []
    if snapshots.exists():
        for path in sorted(snapshots.rglob("*.md")):
            fm = read_fm(path)
            lang = fm.get("original_language", "")
            snapshot_entries.append(
                item(
                    kind="网页快照",
                    source_key="snapshots",
                    source_name=fm.get("source") or "学习计划网页快照",
                    en=path if lang == "en" else None,
                    zh=path if lang != "en" else None,
                    source_url=fm.get("source_url", ""),
                    en_fm=fm if lang == "en" else None,
                    zh_fm=fm if lang != "en" else None,
                )
            )
        entries.extend(snapshot_entries)
        per_source["snapshots"] = {
            "name": "学习计划点名的单页快照",
            "status": "snapshot",
            "license": "逐条不同",
            "entries": snapshot_entries,
            "en_dir": snapshots,
            "zh_dir": None,
        }
    return entries, per_source


def write_source_catalogs(
    apple_entries: list[dict],
    wwdc_entries: list[dict],
    blog_sources: dict[str, dict],
) -> None:
    shutil.rmtree(SOURCES, ignore_errors=True)
    (SOURCES / "apple").mkdir(parents=True)
    (SOURCES / "blogs").mkdir(parents=True)

    apple_by_source: dict[str, list[dict]] = defaultdict(list)
    for entry in apple_entries:
        apple_by_source[entry["source_key"]].append(entry)
    for key, entries in apple_by_source.items():
        page = SOURCES / "apple" / f"{key}.md"
        lines = catalog_header(
            f"Apple · {key} · 成篇文章",
            "仅列出有完整正文的 article、overview、collection、sample code 和 module；"
            "短 API 条目仍保留在原始目录。",
        )
        for entry in sorted(entries, key=lambda e: e["en_title"].casefold()):
            lines.append(catalog_row(entry, page))
        page.write_text("\n".join(lines) + "\n", encoding="utf-8")

    for key, data in blog_sources.items():
        page = SOURCES / "blogs" / f"{key}.md"
        lines = catalog_header(
            data["name"],
            f"状态：{data['status'] or '未记录'}；授权：{data['license']}。",
        )
        for entry in sorted(
            data["entries"],
            key=lambda e: (e["en_title"] or e["zh_title"]).casefold(),
        ):
            lines.append(catalog_row(entry, page))
        page.write_text("\n".join(lines) + "\n", encoding="utf-8")

    page = SOURCES / "wwdc.md"
    lines = catalog_header(
        "WWDC session 文章目录",
        "按年份与标题列出本地逐字稿；幻灯片归档是待完成的独立工程。",
    )
    for entry in sorted(
        wwdc_entries,
        key=lambda e: (
            e["source_key"],
            e["en_title"].casefold(),
        ),
        reverse=True,
    ):
        lines.append(catalog_row(entry, page))
    page.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_apple_index(entries: list[dict], stats: dict[str, dict]) -> dict:
    page = IDX / "apple-docs.md"
    lines = [
        "# Apple 现行文档",
        "",
        f"> 来源：`developer.apple.com/documentation`，索引生成于 {date.today()}。",
        "> “成篇文章”有逐篇目录；短 API 条目仍可从框架归档目录浏览。",
        "",
        "| 框架 | 页面总数 | 成篇文章 | 已翻译 | 文章目录 | 原始归档 |",
        "|---|---:|---:|---:|---|---|",
    ]
    for key, data in sorted(stats.items(), key=lambda pair: -pair[1]["total"]):
        catalog = SOURCES / "apple" / f"{key}.md"
        catalog_cell = local_link("逐篇查看", catalog, page) if catalog.exists() else "—"
        archive_dir = ROOT / "apple-docs" / "en" / key
        archive = archive_dir if archive_dir.exists() else archive_dir.with_suffix(".md")
        lines.append(
            f"| {key} | {data['total']:,} | {data['longform']:,} "
            f"| {data['translated']:,} | {catalog_cell} "
            f"| {local_link('目录', archive, page)} |"
        )
    total = sum(v["total"] for v in stats.values())
    longform = sum(v["longform"] for v in stats.values())
    translated = sum(v["translated"] for v in stats.values())
    lines.append(
        f"| **合计** | **{total:,}** | **{longform:,}** | **{translated:,}** | | |"
    )
    page.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "total": total,
        "longform": longform,
        "translated": translated,
        "frameworks": len(stats),
    }


def write_wwdc_index(entries: list[dict]) -> dict:
    page = IDX / "wwdc.md"
    groups: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        fm = read_fm(entry["en"])
        groups[fm.get("group", "未分组")].append(entry)
        entry["_fm"] = fm
    lines = [
        "# WWDC session 逐字稿",
        "",
        f"> 共 {len(entries)} 场，索引生成于 {date.today()}。逐字稿可能包含 Apple 自动转写错误。",
        f"> 也可打开{local_link('文章级总目录', SOURCES / 'wwdc.md', page)}直接比较中英文状态。",
        "",
    ]
    for group in sorted(groups):
        items = sorted(
            groups[group],
            key=lambda e: (
                -(int(e["_fm"].get("year") or 0) if (e["_fm"].get("year") or "").isdigit() else 0),
                e["en_title"].casefold(),
            ),
        )
        evergreen = sum(e["_fm"].get("evergreen") == "true" for e in items)
        lines += [
            f"## {group}",
            "",
            f"{len(items)} 场，其中 {evergreen} 场标为“讲机制、长期有效”。",
            "",
        ]
        for entry in items:
            fm = entry["_fm"]
            suffix = "" if fm.get("evergreen") == "true" else " _(版本性)_"
            zh = f" · {local_link('中文', entry['zh'], page)}" if entry["zh"] else ""
            lines.append(
                f"- {local_link(entry['en_title'], entry['en'], page)}{zh} "
                f"· {fm.get('collection', '')} · {fm.get('duration', '')}{suffix}"
            )
        lines.append("")
    page.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "total": len(entries),
        "translated": sum(e["status"] == "已翻译" for e in entries),
        "groups": len(groups),
    }


def write_blogs_index(blog_sources: dict[str, dict]) -> dict:
    page = IDX / "blogs.md"
    lines = [
        "# 第三方技术博客与网页快照",
        "",
        "> 本仓库为私有个人学习归档。逐篇查找请进入“文章目录”，不要再从文件名猜文章。",
        "> 授权状态仅用于约束本仓库的使用范围，不代表取得了再发布授权。",
        "",
        "| 来源 | 英文 | 中文 | 其中译文 | 待翻译 | 文章目录 | 原始归档 | 授权 |",
        "|---|---:|---:|---:|---:|---|---|---|",
    ]
    total_entries = total_en = total_zh = total_translated = 0
    for key, data in sorted(blog_sources.items(), key=lambda pair: pair[1]["name"].casefold()):
        entries = data["entries"]
        en_count = sum(bool(e["en"]) for e in entries)
        zh_count = sum(bool(e["zh"]) for e in entries)
        translated = sum(e["status"] == "已翻译" for e in entries)
        pending = sum(e["status"] == "待翻译" for e in entries)
        total_entries += len(entries)
        total_en += en_count
        total_zh += zh_count
        total_translated += translated
        archive_links = []
        if data["en_dir"]:
            archive_links.append(local_link("英文", data["en_dir"], page))
        if data["zh_dir"]:
            archive_links.append(local_link("中文", data["zh_dir"], page))
        lines.append(
            f"| {table_text(data['name'])} | {en_count} | {zh_count} | {translated} | {pending} "
            f"| {local_link('逐篇查看', SOURCES / 'blogs' / f'{key}.md', page)} "
            f"| {' · '.join(archive_links) or '—'} | {table_text(data['license'])} |"
        )
    lines.append(
        f"| **合计** | **{total_en}** | **{total_zh}** | **{total_translated}** "
        f"| **{total_en - total_translated}** | | | |"
    )
    page.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "entries": total_entries,
        "en": total_en,
        "zh": total_zh,
        "translated": total_translated,
    }


def write_topics(entries: list[dict]) -> None:
    shutil.rmtree(TOPICS, ignore_errors=True)
    TOPICS.mkdir(parents=True)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        for topic in entry["topics"]:
            grouped[topic].append(entry)

    landing = IDX / "topics.md"
    lines = [
        "# 按主题找资料",
        "",
        "> 主题由标题、来源元数据和 WWDC 人工分组确定，用于发现资料，不代替全文检索。",
        "> 同一篇文章可以出现在多个主题中；没有可靠匹配的文章仍可从来源目录找到。",
        "",
        "| 主题 | 资料数 |",
        "|---|---:|",
    ]
    for topic, items in sorted(grouped.items(), key=lambda pair: (-len(pair[1]), pair[0])):
        slug = hashlib.sha1(topic.encode("utf-8")).hexdigest()[:10]
        target = TOPICS / f"{slug}.md"
        lines.append(f"| {local_link(topic, target, landing)} | {len(items)} |")
        body = [
            f"# {topic}",
            "",
            f"> 共 {len(items)} 份资料。自动生成于 {date.today()}。",
            "",
            "| 标题 | 类型 | 来源 | 英文/原文 | 中文 | 状态 |",
            "|---|---|---|---|---|---|",
        ]
        for entry in sorted(
            items,
            key=lambda e: (e["zh_title"] or e["en_title"]).casefold(),
        ):
            title = entry["zh_title"] or entry["en_title"]
            preferred = entry["zh"] or entry["en"]
            original = local_link("英文", entry["en"], target) if entry["en"] else local_link("中文原文", entry["zh"], target)
            chinese = local_link("中文", entry["zh"], target) if entry["en"] and entry["zh"] else "—"
            body.append(
                f"| {local_link(title, preferred, target)} | {entry['kind']} "
                f"| {table_text(entry['source_name'])} | {original} | {chinese} | {entry['status']} |"
            )
        target.write_text("\n".join(body) + "\n", encoding="utf-8")
    landing.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_translation_status(
    apple_entries: list[dict],
    wwdc_entries: list[dict],
    blog_sources: dict[str, dict],
) -> None:
    page = IDX / "translation-status.md"
    rows = []
    apple_groups: dict[str, list[dict]] = defaultdict(list)
    for entry in apple_entries:
        apple_groups[entry["source_key"]].append(entry)
    for key, entries in apple_groups.items():
        rows.append(
            (
                "Apple 文档",
                key,
                len(entries),
                sum(e["status"] == "已翻译" for e in entries),
                SOURCES / "apple" / f"{key}.md",
            )
        )
    rows.append(
        (
            "WWDC",
            "全部 session",
            len(wwdc_entries),
            sum(e["status"] == "已翻译" for e in wwdc_entries),
            SOURCES / "wwdc.md",
        )
    )
    for key, data in blog_sources.items():
        en_entries = [e for e in data["entries"] if e["en"]]
        rows.append(
            (
                "技术博客",
                data["name"],
                len(en_entries),
                sum(e["status"] == "已翻译" for e in en_entries),
                SOURCES / "blogs" / f"{key}.md",
            )
        )
    lines = [
        "# 翻译状态",
        "",
        "> 本页按实际中英文文件配对生成，不把原生中文文章误算成译文。",
        "> 当前项目采用暑期定向完成标准；“待翻译”不等于全部都在当前白名单。",
        "",
        "| 类型 | 来源 | 可翻译原文 | 已有中文译文 | 待翻译 | 完成率 | 逐篇目录 |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for kind, name, total, translated, target in sorted(
        rows, key=lambda row: (row[0], -row[2], row[1])
    ):
        pending = total - translated
        rate = f"{translated / total * 100:.0f}%" if total else "—"
        lines.append(
            f"| {kind} | {table_text(name)} | {total} | {translated} | {pending} "
            f"| {rate} | {local_link('查看', target, page)} |"
        )
    page.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_articles_landing(
    apple: dict,
    wwdc: dict,
    blogs: dict,
) -> None:
    page = IDX / "articles.md"
    lines = [
        "# 文章目录",
        "",
        "> 从这里按资料类型进入文章级目录。每一行都直接提供本地原文、中文译文和翻译状态。",
        "> 学习计划周次不属于通用资料元数据，因此只保留在独立的学习计划索引中。",
        "",
        "| 类型 | 收录范围 | 文章级入口 |",
        "|---|---|---|",
        f"| Apple 现行文档 | {apple['longform']:,} 篇成篇文章 | {local_link('按框架查看', IDX / 'apple-docs.md', page)} |",
        f"| WWDC | {wwdc['total']} 场逐字稿 | {local_link('逐篇查看', SOURCES / 'wwdc.md', page)} |",
        f"| 技术博客与网页快照 | {blogs['entries']:,} 条独立记录 | {local_link('按来源查看', IDX / 'blogs.md', page)} |",
        "",
        "## 其他查找方式",
        "",
        f"- {local_link('按主题找资料', IDX / 'topics.md', page)}",
        f"- {local_link('查看翻译状态', IDX / 'translation-status.md', page)}",
        f"- {local_link('按暑期学习计划查找', IDX / 'study-plan.md', page)}",
        "",
        "在 GitHub 中还可以使用仓库搜索，例如：",
        "",
        "```text",
        'repo:Biscoffee/apple-docs-vault "RunLoop"',
        "```",
    ]
    page.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    IDX.mkdir(parents=True, exist_ok=True)
    apple_entries, apple_stats = collect_apple_docs()
    wwdc_entries = collect_wwdc()
    blog_entries, blog_sources = collect_blogs()

    write_source_catalogs(apple_entries, wwdc_entries, blog_sources)
    apple = write_apple_index(apple_entries, apple_stats)
    wwdc = write_wwdc_index(wwdc_entries)
    blogs = write_blogs_index(blog_sources)
    all_entries = [*apple_entries, *wwdc_entries, *blog_entries]
    write_topics(all_entries)
    write_translation_status(apple_entries, wwdc_entries, blog_sources)
    write_articles_landing(apple, wwdc, blogs)

    print(f"Apple 成篇文章：{apple['longform']:,}，译文 {sum(e['status'] == '已翻译' for e in apple_entries):,}")
    print(f"WWDC：{wwdc['total']}，译文 {wwdc['translated']}")
    print(f"博客/快照记录：{blogs['entries']:,}，配对译文 {blogs['translated']}")
    print(f"主题页：{len(list(TOPICS.glob('*.md')))}")
    print("README.md 未改写；请运行 python3 tools/check_links.py 验证导航")


if __name__ == "__main__":
    main()
