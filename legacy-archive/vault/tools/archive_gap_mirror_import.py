#!/usr/bin/env python3
"""从固定提交的 ADC 2009 镜像恢复 Apple 已下线的早期归档。

这不是第一来源抓取器。只有在 Apple 原始地址和 Internet Archive 均无法
恢复时才运行，并把镜像仓库、提交、相对路径写入来源审计报告。

用法：

    python3 tools/archive_gap_mirror_import.py \
      --mirror-root /path/to/ADC-reference-library-2009-july
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
import urllib.parse
from pathlib import Path

from bs4 import BeautifulSoup
from pypdf import PdfReader

import archive_gap_phase2 as phase2
import archive_scrape as core


ROOT = Path(__file__).resolve().parent.parent
MIRROR_REPOSITORY = "https://github.com/cellularmitosis/ADC-reference-library-2009-july"
MIRROR_COMMIT = "40bbfb75fbca44be17a305321eaee3ab8382572b"

# 每项都先在 Apple 原始地址、Wayback 中失败，再由固定提交的镜像补回。
HTML_RECORDS = {
    "DTS10000026": "samplecode/SCSI_Inquiry_(More)/index.html",
    "DTS10000165": "samplecode/SearchProcs_&_Color_Sep/index.html",
    "DTS10000340": "samplecode/2BufRecord&Play/index.html",
    "DTS10000734": "samplecode/Sample_(Traffic_Light)/index.html",
    "DTS10000829": "samplecode/makeeffectslideshow/index.html",
    "TP40000979": "documentation/Hardware/hardware2.html",
    "TP40000997": "documentation/Carbon/Conceptual/DesktopIcons/ch13.html",
    "TP40001014": "releasenotes/Carbon/HIToolboxOlderNotes.html",
    "TP40001024": "documentation/Hardware/legacy/legacy.html",
    "TP40001050": "documentation/QuickTime/whatsnew.htm",
}

PDF_RECORDS = {
    "TP40001358": (
        "documentation/Security/Conceptual/CertKeyTrustProgGuide/"
        "CertKeyTrustProgGuide.pdf"
    ),
    "TP40004285": (
        "documentation/QuickTime/Reference/QTRef_AtomsResources/"
        "QTRef_AtomsResources.pdf"
    ),
    "TP40004652": (
        "documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/"
        "InstrumentsUserGuide.pdf"
    ),
    "TP40006821": (
        "documentation/Carbon/Conceptual/DragMgrProgrammersGuide/"
        "DragMgrProgrammersGuide.pdf"
    ),
    "TP40006824": (
        "documentation/Performance/Conceptual/Mac_OSX_Numerics/"
        "Mac_OSX_Numerics.pdf"
    ),
}


def mirror_url(relative: str) -> str:
    quoted = urllib.parse.quote(relative, safe="/()_-.&")
    return f"{MIRROR_REPOSITORY}/blob/{MIRROR_COMMIT}/{quoted}"


def doc_map() -> dict[str, dict]:
    return {d["apple_id"]: d for d in phase2.load_docs()}


def clean_container(soup: BeautifulSoup, sample: bool) -> BeautifulSoup:
    """保留正文和源码，剔除旧站导航、反馈表单和脚本。"""
    out = BeautifulSoup("<article></article>", "html.parser")
    article = out.article
    pagehead = soup.select_one("#pagehead")
    if pagehead:
        heading = out.new_tag("h1")
        heading.string = pagehead.get_text(" ", strip=True)
        article.append(heading)

    source = soup.select_one("pre.sourcecodebox")
    if source is not None:
        source_heading = source.find_previous("h2")
        if source_heading:
            article.append(copy.copy(source_heading))
        article.append(copy.copy(source))
        return out

    if sample:
        details = soup.select_one("#scdetails")
        if details:
            article.append(copy.copy(details))
        description = next(
            (
                h
                for h in soup.find_all("h2")
                if h.get_text(" ", strip=True) == "Description"
            ),
            None,
        )
        if description and description.parent:
            for node in list(description.parent.children):
                if getattr(node, "name", None) or str(node).strip():
                    article.append(copy.copy(node))
        return out

    body = soup.find("body")
    if body:
        article.append(copy.copy(body))
    for unwanted in article.select(
        "script, style, form, #breadcrumb, #watermark, .legacybox"
    ):
        unwanted.decompose()
    return out


def copy_local_images(
    container: BeautifulSoup,
    html_path: Path,
    destination: Path,
) -> int:
    copied = 0
    for image in container.find_all("img"):
        src = (image.get("src") or "").split("?", 1)[0]
        if not src or src.startswith(("data:", "http:", "https:")):
            continue
        source = (html_path.parent / urllib.parse.unquote(src)).resolve()
        if not source.is_file():
            image.decompose()
            continue
        target = destination / "attachments" / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copy2(source, target)
            copied += 1
        image["src"] = f"attachments/{source.name}"
    return copied


def render_html(d: dict, mirror_root: Path, relative: str) -> dict:
    entry = mirror_root / relative
    if not entry.is_file():
        raise FileNotFoundError(entry)
    doc_dir, filename = phase2.pdf_destination(d)
    doc_dir.mkdir(parents=True, exist_ok=True)
    is_sample = d["type_name"] == "Sample Code"
    html_files = [entry]
    if is_sample:
        html_files += sorted(entry.parent.glob("listing*.html"))

    output_paths: list[str] = []
    image_count = 0
    archive_info = None
    for index, html_path in enumerate(html_files):
        raw = html_path.read_bytes()
        # 早期 ADC 页面同时存在 UTF-8 和 ISO-8859-1。
        html = raw.decode("utf-8", "replace")
        soup = BeautifulSoup(html, "html.parser")
        container = clean_container(soup, sample=is_sample)
        output_name = filename if index == 0 else f"{html_path.stem}.md"
        output = doc_dir / output_name
        rel = str(output.relative_to(ROOT))
        image_count += copy_local_images(container, html_path, doc_dir)
        core.preprocess(container, d["url"].split("#")[0], {}, rel, False)
        body = core.to_markdown(container).strip()
        if len(body) < 80:
            raise ValueError(f"正文过短：{relative}")

        if index == 0:
            zip_files = sorted(entry.parent.glob("*.zip"))
            if zip_files:
                source_zip = zip_files[0]
                target_zip = doc_dir / "attachments" / "original-sample.zip"
                target_zip.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_zip, target_zip)
                digest = hashlib.sha256(target_zip.read_bytes()).hexdigest()
                archive_info = {
                    "path": str(target_zip.relative_to(ROOT)),
                    "sha256": digest,
                    "bytes": target_zip.stat().st_size,
                }
                body = (
                    "[下载镜像保存的 Apple 原始 Sample Code 包]"
                    "(attachments/original-sample.zip)\n\n" + body
                )

        official_url = d["url"].split("#")[0]
        if index:
            official_url = urllib.parse.urljoin(official_url, html_path.name)
        nav = core.nav_line(
            rel,
            rel.split("/")[0],
            d["name"],
            None if index == 0 else filename,
        )
        output.write_text(
            core.frontmatter(d, official_url) + nav + "\n\n\n\n" + body + "\n",
            encoding="utf-8",
        )
        output_paths.append(rel)

    return {
        "status": "restored-mirror-html",
        "source_url": d["url"].split("#")[0],
        "paths": output_paths,
        "pages": len(output_paths),
        "images": image_count,
        "sample_archive": archive_info,
        "mirror": {
            "repository": MIRROR_REPOSITORY,
            "commit": MIRROR_COMMIT,
            "path": relative,
            "url": mirror_url(relative),
        },
    }


def render_pdf(d: dict, mirror_root: Path, relative: str) -> dict:
    source = mirror_root / relative
    data = source.read_bytes()
    if not data.startswith(b"%PDF"):
        raise ValueError(f"不是 PDF：{source}")
    doc_dir, filename = phase2.pdf_destination(d)
    doc_dir.mkdir(parents=True, exist_ok=True)
    attachment = doc_dir / "attachments" / "original.pdf"
    attachment.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, attachment)

    pages: list[str] = []
    reader = PdfReader(source)
    for number, page in enumerate(reader.pages, 1):
        text = (page.extract_text() or "").strip()
        if text:
            pages.append(f"## 第 {number} 页\n\n{text}")

    output = doc_dir / filename
    rel = str(output.relative_to(ROOT))
    nav = core.nav_line(rel, rel.split("/")[0], d["name"], None)
    body = (
        f"# {d['name']}\n\n[打开镜像保存的 Apple 原始 PDF]"
        "(attachments/original.pdf)"
    )
    if pages:
        body += "\n\n" + "\n\n".join(pages)
    output.write_text(
        core.frontmatter(d, d["url"].split("#")[0])
        + nav
        + "\n\n\n\n"
        + body
        + "\n",
        encoding="utf-8",
    )
    return {
        "status": "restored-mirror-pdf",
        "source_url": d["url"].split("#")[0],
        "path": rel,
        "attachment": str(attachment.relative_to(ROOT)),
        "pages": len(reader.pages),
        "sha256": hashlib.sha256(data).hexdigest(),
        "mirror": {
            "repository": MIRROR_REPOSITORY,
            "commit": MIRROR_COMMIT,
            "path": relative,
            "url": mirror_url(relative),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mirror-root", type=Path, required=True)
    args = parser.parse_args()
    mirror_root = args.mirror_root.resolve()
    docs = doc_map()
    sources = phase2.load_sources()

    for aid, relative in HTML_RECORDS.items():
        result = render_html(docs[aid], mirror_root, relative)
        sources[aid] = {"name": docs[aid]["name"], **result}
        print(f"{aid} {result['status']} {result['pages']} pages")
    for aid, relative in PDF_RECORDS.items():
        result = render_pdf(docs[aid], mirror_root, relative)
        sources[aid] = {"name": docs[aid]["name"], **result}
        print(f"{aid} {result['status']} {result['pages']} pages")

    phase2.save_sources(sources)


if __name__ == "__main__":
    main()
