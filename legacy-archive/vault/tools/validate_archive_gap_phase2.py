#!/usr/bin/env python3
"""对 Archive Gap Phase 2 的来源、文档、附件、索引和统计做机械校验。"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "doc" / "ARCHIVE_GAP_PHASE2_INPUT.json"
SOURCES = ROOT / "doc" / "ARCHIVE_GAP_PHASE2_SOURCES.json"
ASSETS = ROOT / "doc" / "ARCHIVE_GAP_PHASE2_ASSETS.json"
FM_KEYS = [
    "title",
    "apple_id",
    "resource_type",
    "platform",
    "topic",
    "technology",
    "published",
    "source_url",
    "archived_at",
]
RESOLVED = {
    "restored-alias-metadata",
    "restored-html",
    "restored-mirror-html",
    "restored-mirror-pdf",
    "restored-pdf",
    "staged-html",
}
DECORATIVE_IMAGE_NAMES = {
    "task_2x.png",
    "tips_2x.png",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(path: Path) -> tuple[dict, str, list[str]]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("frontmatter missing")
    raw, body = text[4:].split("\n---\n", 1)
    keys = re.findall(r"^([a-z_]+):", raw, re.M)
    return yaml.safe_load(raw), body, keys


def content_markdown() -> list[Path]:
    files = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if rel.parts[0] in (".git", ".staging", "_indexes", "doc", "tools"):
            continue
        if rel.as_posix() in ("README.md", "agent.md"):
            continue
        files.append(path)
    return files


def image_good(path: Path) -> bool:
    data = path.read_bytes()
    suffix = path.suffix.lower()
    if suffix == ".png":
        return data.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in {".jpg", ".jpeg"}:
        return data.startswith(b"\xff\xd8\xff")
    if suffix == ".gif":
        return data.startswith((b"GIF87a", b"GIF89a"))
    return True


def main() -> int:
    errors: list[str] = []
    manifest = json.loads(INPUT.read_text(encoding="utf-8"))["documents"]
    report = json.loads(SOURCES.read_text(encoding="utf-8"))
    asset_report = json.loads(ASSETS.read_text(encoding="utf-8"))
    sources = report["documents"]
    expected_ids = {d["apple_id"] for d in manifest}
    if len(manifest) != 148 or len(expected_ids) != 148:
        fail(errors, "phase2 输入不是 148 个唯一 Apple ID")
    if set(sources) != expected_ids:
        fail(errors, "来源报告的 Apple ID 集合与输入不一致")

    counts = Counter(v.get("status") for v in sources.values())
    if counts != Counter(report["meta"]["status_counts"]):
        fail(errors, "来源报告 status_counts 与逐条状态不一致")
    resolved_ids = {aid for aid, value in sources.items() if value["status"] in RESOLVED}
    unresolved_ids = {
        aid for aid, value in sources.items() if value["status"] == "unresolved"
    }
    if len(resolved_ids) != 114 or len(unresolved_ids) != 34:
        fail(errors, f"恢复/未恢复数量错误：{len(resolved_ids)}/{len(unresolved_ids)}")
    net_new_ids = {
        aid
        for aid in resolved_ids
        if sources[aid]["status"] != "restored-alias-metadata"
    }
    if len(net_new_ids) != 112:
        fail(errors, f"净新增文档数应为 112，实际 {len(net_new_ids)}")

    pages_by_id: dict[str, list[Path]] = {}
    for path in content_markdown():
        try:
            fm, _body, _keys = parse_frontmatter(path)
        except Exception:
            continue
        aid = fm.get("apple_id")
        if aid:
            pages_by_id.setdefault(str(aid), []).append(path)

    present = expected_ids & set(pages_by_id)
    if present != resolved_ids:
        fail(
            errors,
            "磁盘上出现的 phase2 Apple ID 与 resolved 状态不一致："
            f"多 {sorted(present - resolved_ids)}，少 {sorted(resolved_ids - present)}",
        )
    net_new_pages = sum(len(pages_by_id[aid]) for aid in net_new_ids)
    if net_new_pages != 592:
        fail(errors, f"净新增 Markdown 页面数应为 592，实际 {net_new_pages}")
    # 5183 是索引中的文档数；另有 2 份历史遗留、未进入索引的 WebObjects 文档。
    if len(pages_by_id) != 5185:
        fail(errors, f"全库唯一 Apple ID 应为 5185，实际 {len(pages_by_id)}")

    indexed_ids: set[str] = set()
    # 标题可能包含方括号，例如 “Every Picture [Comment] Tells Its Story”。
    entry_rx = re.compile(r"^- \*\*\[(.*)\]\((.*?)\)\*\* — ", re.M)
    for index in (ROOT / "_indexes" / "by-type").glob("*.md"):
        text = index.read_text(encoding="utf-8")
        for _title, href in entry_rx.findall(text):
            rel = urllib.parse.unquote(href)
            if not rel.startswith("../../"):
                continue
            target = ROOT / rel[6:]
            if not target.is_file():
                fail(errors, f"by-type 索引目标不存在：{index.relative_to(ROOT)} -> {rel}")
                continue
            try:
                fm, _body, _keys = parse_frontmatter(target)
            except Exception as exc:
                fail(errors, f"索引入口 frontmatter 无效：{target.relative_to(ROOT)} ({exc})")
                continue
            indexed_ids.add(str(fm.get("apple_id")))
    if len(indexed_ids) != 5183:
        fail(errors, f"by-type 索引唯一 Apple ID 应为 5183，实际 {len(indexed_ids)}")
    if not resolved_ids <= indexed_ids:
        fail(errors, f"phase2 已恢复但未进入 by-type 索引：{sorted(resolved_ids - indexed_ids)}")

    attachment_rx = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
    local_link_rx = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    for aid in sorted(resolved_ids):
        source = sources[aid]
        for path in pages_by_id[aid]:
            fm, body, keys = parse_frontmatter(path)
            rel = path.relative_to(ROOT)
            if keys != FM_KEYS:
                fail(errors, f"frontmatter 键或顺序错误：{rel}")
            if fm.get("apple_id") != aid:
                fail(errors, f"Apple ID 错误：{rel}")
            if re.search(r"Page Not Found|The page you.re looking for", body, re.I):
                fail(errors, f"正文含 404 特征：{rel}")
            nav = body.splitlines()[0] if body.splitlines() else ""
            if not nav.startswith("> 导航："):
                fail(errors, f"导航行缺失：{rel}")
            for raw_target in attachment_rx.findall(body):
                target = urllib.parse.unquote(raw_target.split("#", 1)[0])
                target = target.split(' "', 1)[0]
                if target.startswith(("http:", "https:", "data:")):
                    continue
                if Path(target).name in DECORATIVE_IMAGE_NAMES:
                    continue
                destination = (path.parent / target).resolve()
                if not destination.is_file():
                    fail(errors, f"图片目标不存在：{rel} -> {raw_target}")
                elif not image_good(destination):
                    fail(errors, f"图片文件头无效：{rel} -> {raw_target}")
            for raw_target in local_link_rx.findall(body):
                target = urllib.parse.unquote(raw_target.split("#", 1)[0])
                if not target:
                    continue
                if target.startswith(("/", "//")) or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                    continue
                if not (path.parent / target).resolve().is_file():
                    fail(errors, f"本地链接目标不存在：{rel} -> {raw_target}")

        acquisition = source.get("acquisition", {})
        final = acquisition.get("final", "")
        replay = final.split("id_/", 1)[-1]
        if (
            "developer.apple.com/documentation/" in replay
            and "developer.apple.com/library/archive/" not in replay
        ):
            fail(errors, f"现代 DocC 被误收为旧归档：{aid}")

        if source["status"] in ("restored-pdf", "restored-mirror-pdf"):
            attachment = ROOT / source["attachment"]
            if not attachment.is_file() or attachment.read_bytes()[:4] != b"%PDF":
                fail(errors, f"PDF 原件无效：{aid}")
        sample = source.get("sample_archive")
        if sample:
            archive = ROOT / sample["path"]
            if not archive.is_file() or archive.read_bytes()[:2] != b"PK":
                fail(errors, f"Sample Code ZIP 无效：{aid}")
        mirror = source.get("mirror")
        if mirror and mirror.get("commit") != "40bbfb75fbca44be17a305321eaee3ab8382572b":
            fail(errors, f"镜像提交未固定：{aid}")

    asset_counts = Counter(
        record["status"] for record in asset_report["assets"]
    )
    expected_asset_counts = Counter(
        {
            "network-error": 625,
            "recovered": 116,
            "unavailable": 20,
            "valid-existing": 208,
        }
    )
    if asset_counts != expected_asset_counts:
        fail(errors, f"附件审计状态数量错误：{dict(asset_counts)}")
    asset_paths = [record["path"] for record in asset_report["assets"]]
    if len(asset_paths) != 969 or len(set(asset_paths)) != 969:
        fail(errors, "附件审计应包含 969 个唯一文件路径")
    if Counter(asset_report["meta"]["status_counts"]) != asset_counts:
        fail(errors, "附件审计 meta.status_counts 与逐条状态不一致")
    for record in asset_report["assets"]:
        path = ROOT / record["path"]
        status = record["status"]
        if status in {"valid-existing", "recovered"}:
            if not path.is_file() or not image_good(path):
                fail(errors, f"附件审计中的有效图片不存在或文件头错误：{record['path']}")
        elif path.exists():
            fail(errors, f"确认缺失或待重试的附件不应保留伪文件：{record['path']}")
        page_text = (ROOT / record["page"]).read_text(encoding="utf-8")
        filename = Path(record["path"]).name
        if status == "unavailable" and filename not in page_text:
            fail(errors, f"确认缺失附件没有 Markdown 说明：{record['path']}")
        if status == "network-error" and filename not in page_text:
            fail(errors, f"网络待重试附件没有 Markdown 说明：{record['path']}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "- 文档：5183 份" not in readme or "- 页面：40090 个 Markdown 文件" not in readme:
        fail(errors, "README 统计不是 5183 份 / 40090 页")
    expected_type_counts = {
        "guide.md": 701,
        "qa.md": 1517,
        "release-note.md": 222,
        "sample-code.md": 1934,
        "technical-note.md": 809,
    }
    for filename, expected in expected_type_counts.items():
        text = (ROOT / "_indexes" / "by-type" / filename).read_text(encoding="utf-8")
        actual = len(entry_rx.findall(text))
        if actual != expected:
            fail(errors, f"{filename} 条目数应为 {expected}，实际 {actual}")

    if errors:
        print(f"FAIL：{len(errors)} 项")
        for item in errors:
            print("  -", item)
        return 1
    print("PASS")
    print(
        f"  输入 {len(manifest)}：已恢复 {len(resolved_ids)}，未恢复 {len(unresolved_ids)}；"
        f"净新增 {len(net_new_ids)} 份 / {net_new_pages} 页"
    )
    print(
        f"  全库唯一 Apple ID {len(pages_by_id)}"
        f"（含 2 份历史未索引文档），by-type 索引 {len(indexed_ids)}"
    )
    print("  配图 969：有效/恢复 324，确认不可用 20，网络待重试 625")
    print("  README 5183 份 / 40090 页")
    return 0


if __name__ == "__main__":
    sys.exit(main())
