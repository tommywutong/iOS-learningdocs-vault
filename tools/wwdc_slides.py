#!/usr/bin/env python3
"""归档 WWDC 官方幻灯片 PDF 的逐页 WebP。

    python3 tools/wwdc_slides.py plan
    python3 tools/wwdc_slides.py fetch --session wwdc2018/416
    python3 tools/wwdc_slides.py render --session wwdc2018/416
    python3 tools/wwdc_slides.py status
    python3 tools/wwdc_slides.py verify

原始 PDF 只保存在被 Git 忽略的 .cache/wwdc-slides/。正式目录只写入 WebP、
manifest.json 和 slides.md，并把英文/中文逐字稿链接到同一份 slides.md。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WWDC_EN = ROOT / "wwdc" / "en"
WWDC_ZH = ROOT / "wwdc" / "zh"
CACHE = ROOT / ".cache" / "wwdc-slides"
OUTPUT = ROOT / "wwdc" / "slides"
PDF_LINK = re.compile(r"\[Presentation Slides \(PDF\)\]\(([^)]+)\)")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
HEADERS = {"User-Agent": "apple-developer-docs-vault/0.1 (personal archive)"}


class SlidesError(RuntimeError):
    """可读的幻灯片流水线错误。"""


@dataclass(frozen=True)
class Session:
    key: str
    collection: str
    session_id: str
    title: str
    source_url: str
    pdf_url: str
    en_path: Path
    zh_path: Path | None

    @property
    def cache_dir(self) -> Path:
        return CACHE / self.collection / self.session_id

    @property
    def output_dir(self) -> Path:
        return OUTPUT / self.collection / self.session_id


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER.match(text)
    if not match:
        raise SlidesError("逐字稿缺少 frontmatter")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        cleaned = value.strip().strip("'\"").replace("''", "'")
        values[key.strip()] = cleaned
    return values


def discover() -> list[Session]:
    sessions: list[Session] = []
    for en_path in sorted(WWDC_EN.glob("*/*.md")):
        text = en_path.read_text(encoding="utf-8")
        pdf_match = PDF_LINK.search(text)
        if not pdf_match:
            continue
        meta = parse_frontmatter(text)
        heading = re.search(r"^# (.+)$", text, re.MULTILINE)
        collection = meta.get("collection") or en_path.parent.name
        session_id = meta.get("session_id") or en_path.name.split("-", 1)[0]
        key = f"{collection}/{session_id}"
        zh_candidate = WWDC_ZH / collection / en_path.name
        sessions.append(
            Session(
                key=key,
                collection=collection,
                session_id=session_id,
                title=heading.group(1).strip() if heading else meta.get("title") or en_path.stem,
                source_url=meta.get("source_url", ""),
                pdf_url=pdf_match.group(1),
                en_path=en_path,
                zh_path=zh_candidate if zh_candidate.is_file() else None,
            )
        )
    return sessions


def resolve_session(key: str) -> Session:
    matches = [session for session in discover() if session.key == key]
    if len(matches) != 1:
        raise SlidesError(f"找不到唯一 session：{key}")
    return matches[0]


def pdf_page_count(path: Path) -> int:
    pdfinfo = shutil.which("pdfinfo")
    if not pdfinfo:
        raise SlidesError("缺少 pdfinfo；请安装 Poppler")
    result = subprocess.run(
        [pdfinfo, str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if not match:
        raise SlidesError(f"pdfinfo 未返回页数：{path}")
    return int(match.group(1))


def fetch(session: Session, *, dry_run: bool = False) -> Path:
    pdf_path = session.cache_dir / "source.pdf"
    metadata_path = session.cache_dir / "source.json"
    if pdf_path.is_file() and pdf_path.stat().st_size > 4 and pdf_path.read_bytes()[:4] == b"%PDF":
        if not metadata_path.is_file():
            metadata_path.write_text(
                json.dumps(
                    {
                        "url": session.pdf_url,
                        "content_type": "application/pdf",
                        "bytes": pdf_path.stat().st_size,
                        "sha256": sha256_file(pdf_path),
                    },
                    ensure_ascii=False,
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
        print(f"已缓存：{pdf_path.relative_to(ROOT)}")
        return pdf_path
    if dry_run:
        print(f"将下载：{session.pdf_url}")
        return pdf_path

    session.cache_dir.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(session.pdf_url, headers=HEADERS)
    temp = pdf_path.with_suffix(".pdf.part")
    try:
        with urllib.request.urlopen(request, timeout=180) as response, temp.open("wb") as out:
            status = getattr(response, "status", 200)
            if status != 200:
                raise SlidesError(f"下载失败：HTTP {status}")
            content_type = response.headers.get_content_type().lower()
            if content_type not in {"application/pdf", "application/octet-stream"}:
                raise SlidesError(f"下载媒体类型不是 PDF：{content_type}")
            shutil.copyfileobj(response, out)
        if temp.stat().st_size <= 4 or temp.read_bytes()[:4] != b"%PDF":
            raise SlidesError("下载内容不是有效 PDF")
        os.replace(temp, pdf_path)
        metadata_path.write_text(
            json.dumps(
                {
                    "url": session.pdf_url,
                    "content_type": content_type,
                    "bytes": pdf_path.stat().st_size,
                    "sha256": sha256_file(pdf_path),
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    finally:
        temp.unlink(missing_ok=True)
    print(
        f"已下载：{pdf_path.relative_to(ROOT)} "
        f"({pdf_path.stat().st_size:,} bytes, sha256:{sha256_file(pdf_path)[:16]})"
    )
    return pdf_path


def transcript_link(session: Session, *, chinese: bool) -> str:
    label = "已归档的演讲幻灯片" if chinese else "Archived Presentation Slides"
    return f"- [{label}](../../slides/{session.collection}/{session.session_id}/slides.md)"


def add_transcript_link(path: Path, link: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if link in text:
        return False
    heading = "## 相关资源" if "/zh/" in path.as_posix() else "## Resources"
    marker = heading + "\n"
    if marker not in text:
        raise SlidesError(f"找不到资源章节：{path.relative_to(ROOT)}")
    updated = text.replace(marker, marker + "\n" + link + "\n", 1)
    path.write_text(updated, encoding="utf-8")
    return True


def build_slides_markdown(session: Session, images: list[dict]) -> str:
    lines = [
        f"# {session.title} - 演讲幻灯片",
        "",
        f"> 来源：[Apple Developer]({session.source_url}) · "
        f"[官方 PDF]({session.pdf_url})",
        "",
    ]
    for index, image in enumerate(images, 1):
        lines.extend(
            [
                f"## 第 {index} 页",
                "",
                f"![{session.title} - 幻灯片 {index:03d}]({image['file']})",
                "",
            ]
        )
    return "\n".join(lines)


def render(
    session: Session,
    *,
    dry_run: bool = False,
    dpi: int = 72,
    quality: int = 78,
    force: bool = False,
) -> None:
    pdf_path = fetch(session, dry_run=dry_run)
    if dry_run:
        print(f"将渲染到：{session.output_dir.relative_to(ROOT)}")
        return
    if session.output_dir.is_dir() and not force:
        verify_one(session)
        print(f"已通过校验，跳过：{session.output_dir.relative_to(ROOT)}")
        return

    pdftoppm = shutil.which("pdftoppm")
    cwebp = shutil.which("cwebp")
    if not pdftoppm or not cwebp:
        raise SlidesError("缺少 pdftoppm 或 cwebp")

    expected_pages = pdf_page_count(pdf_path)
    CACHE.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"{session.session_id}-", dir=CACHE) as temp_name:
        temp = Path(temp_name)
        raster = temp / "raster"
        subprocess.run(
            [pdftoppm, "-r", str(dpi), "-png", str(pdf_path), str(raster)],
            check=True,
        )
        pngs = sorted(temp.glob("raster-*.png"))
        if len(pngs) != expected_pages:
            raise SlidesError(f"渲染页数不一致：PDF {expected_pages}，PNG {len(pngs)}")

        build = temp / "output"
        build.mkdir()

        def convert(item: tuple[int, Path]) -> dict:
            index, png = item
            name = f"page-{index:03d}.webp"
            webp = build / name
            subprocess.run(
                [cwebp, "-quiet", "-q", str(quality), str(png), "-o", str(webp)],
                check=True,
            )
            return {
                "file": name,
                "sha256": sha256_file(webp),
                "bytes": webp.stat().st_size,
            }

        workers = min(8, os.cpu_count() or 4)
        with ThreadPoolExecutor(max_workers=workers) as pool:
            images = list(pool.map(convert, enumerate(pngs, 1)))

        manifest = {
            "schema_version": 1,
            "session_id": session.session_id,
            "collection": session.collection,
            "title": session.title,
            "session_url": session.source_url,
            "source_type": "official-pdf",
            "pdf": {
                "url": session.pdf_url,
                "content_type": json.loads(
                    (session.cache_dir / "source.json").read_text(encoding="utf-8")
                )["content_type"],
                "sha256": sha256_file(pdf_path),
                "bytes": pdf_path.stat().st_size,
                "pages": expected_pages,
            },
            "render": {
                "format": "webp",
                "dpi": dpi,
                "quality": quality,
                "rendered_pages": len(images),
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            },
            "images": images,
            "status": "completed",
            "error": None,
        }
        (build / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (build / "slides.md").write_text(
            build_slides_markdown(session, images),
            encoding="utf-8",
        )
        session.output_dir.parent.mkdir(parents=True, exist_ok=True)
        backup = session.cache_dir / "previous-output"
        if session.output_dir.exists():
            shutil.rmtree(backup, ignore_errors=True)
            os.replace(session.output_dir, backup)
        try:
            os.replace(build, session.output_dir)
            verify_one_files(session)
        except Exception:
            shutil.rmtree(session.output_dir, ignore_errors=True)
            if backup.exists():
                os.replace(backup, session.output_dir)
            raise
        else:
            shutil.rmtree(backup, ignore_errors=True)

    add_transcript_link(session.en_path, transcript_link(session, chinese=False))
    if session.zh_path:
        add_transcript_link(session.zh_path, transcript_link(session, chinese=True))
    verify_one(session)
    print(
        f"完成：{session.key}，{expected_pages} 页，"
        f"{sum(item['bytes'] for item in images):,} bytes WebP"
    )


def verify_one_files(session: Session) -> None:
    manifest_path = session.output_dir / "manifest.json"
    slides_path = session.output_dir / "slides.md"
    if not manifest_path.is_file() or not slides_path.is_file():
        raise SlidesError(f"缺少 manifest/slides：{session.key}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    images = manifest.get("images") or []
    if manifest.get("source_type") != "official-pdf":
        raise SlidesError(f"来源类型错误：{session.key}")
    if manifest.get("pdf", {}).get("pages") != len(images):
        raise SlidesError(f"manifest 页数不一致：{session.key}")
    if manifest.get("render", {}).get("rendered_pages") != len(images):
        raise SlidesError(f"渲染页数不一致：{session.key}")
    slides = slides_path.read_text(encoding="utf-8")
    for image in images:
        path = session.output_dir / image["file"]
        if not path.is_file():
            raise SlidesError(f"图片缺失：{path.relative_to(ROOT)}")
        if path.stat().st_size != image["bytes"] or sha256_file(path) != image["sha256"]:
            raise SlidesError(f"图片哈希或大小不匹配：{path.relative_to(ROOT)}")
        if f"]({image['file']})" not in slides:
            raise SlidesError(f"slides.md 未引用：{image['file']}")


def verify_one(session: Session) -> None:
    verify_one_files(session)
    expected_links = [(session.en_path, transcript_link(session, chinese=False))]
    if session.zh_path:
        expected_links.append((session.zh_path, transcript_link(session, chinese=True)))
    for path, link in expected_links:
        if link not in path.read_text(encoding="utf-8"):
            raise SlidesError(f"逐字稿缺少幻灯片链接：{path.relative_to(ROOT)}")


def cmd_plan() -> None:
    sessions = discover()
    translated = sum(session.zh_path is not None for session in sessions)
    cached = sum((session.cache_dir / "source.pdf").is_file() for session in sessions)
    rendered = sum(session.output_dir.is_dir() for session in sessions)
    print(
        f"官方 PDF：{len(sessions)} 场；已有中文译文 {translated}；"
        f"已缓存 PDF {cached}；已渲染 {rendered}"
    )
    for session in sessions:
        state = "rendered" if session.output_dir.is_dir() else "pending"
        print(f"{session.key}\t{state}\t{session.title}")


def cmd_status() -> None:
    sessions = discover()
    print(
        f"官方 PDF {len(sessions)}；缓存 "
        f"{sum((s.cache_dir / 'source.pdf').is_file() for s in sessions)}；"
        f"完成 {sum(s.output_dir.is_dir() for s in sessions)}"
    )


def cmd_verify() -> None:
    sessions = {session.key: session for session in discover()}
    failures: list[str] = []
    checked = 0
    for manifest in sorted(OUTPUT.glob("*/*/manifest.json")):
        key = f"{manifest.parent.parent.name}/{manifest.parent.name}"
        session = sessions.get(key)
        if not session:
            failures.append(f"未知 session 输出：{key}")
            continue
        try:
            verify_one(session)
        except (SlidesError, OSError, json.JSONDecodeError) as exc:
            failures.append(str(exc))
        checked += 1
    tracked_forbidden = subprocess.run(
        ["git", "ls-files", "wwdc/slides", "*.pdf", "*.mp4", "*.mov", "*.m3u8"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    tracked_forbidden = [
        path
        for path in tracked_forbidden
        if Path(path).suffix.lower() in {".pdf", ".mp4", ".mov", ".m3u8"}
    ]
    failures.extend(f"Git 中存在禁止媒体：{path}" for path in tracked_forbidden)
    if failures:
        print("\n".join(f"- {failure}" for failure in failures), file=sys.stderr)
        raise SystemExit(1)
    print(f"校验 {checked} 场幻灯片：全部通过")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("plan")
    subparsers.add_parser("status")
    subparsers.add_parser("verify")
    for command in ("fetch", "render"):
        child = subparsers.add_parser(command)
        child.add_argument("--session", required=True, metavar="COLLECTION/ID")
        if command == "render":
            child.add_argument("--dpi", type=int, default=72)
            child.add_argument("--quality", type=int, default=78)
            child.add_argument("--force", action="store_true")
    args = parser.parse_args()

    try:
        if args.command == "plan":
            cmd_plan()
        elif args.command == "status":
            cmd_status()
        elif args.command == "verify":
            cmd_verify()
        else:
            session = resolve_session(args.session)
            if args.command == "fetch":
                fetch(session, dry_run=args.dry_run)
            else:
                render(
                    session,
                    dry_run=args.dry_run,
                    dpi=args.dpi,
                    quality=args.quality,
                    force=args.force,
                )
    except (SlidesError, OSError, subprocess.CalledProcessError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
