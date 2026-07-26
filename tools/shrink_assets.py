#!/usr/bin/env python3
"""把超大图片压到 1 MB 以内，不动其余图片。

    python3 tools/shrink_assets.py --dry-run   # 只看会动哪些
    python3 tools/shrink_assets.py             # 实际压缩

## 为什么只压大的

实测 2,741 张图里，**中位数只有 133 KB，但 222 张超过 1 MB 的巨图把总量拉到
1.45 GB**（最大一张 11.6 MB）。绝大多数图本来就小，压了没意义还掉画质；真正
占体积的是那条长尾。所以只动超标的，其余一个字节不改。

## 为什么用缩边长而不是转 JPEG

这些图大多是带文字标注的架构图和截图，转 JPEG 会在文字边缘产生振铃伪影。
按最长边逐档缩小（2400 → 2000 → 1600 → 1280 → 1024）保留 PNG 无损特性，
在视网膜屏上依然清晰。

文件名不变，所以 Markdown 里的引用不受影响。
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# 默认处理 attachments/，也可以用 --dir 指定别的目录、--limit 指定别的阈值。
# oss/ 下的中文笔记仓库带大量截图（749 MB），用更严的阈值压。
ATTACH = ROOT / "attachments"
LIMIT = 1_000_000          # 目标上限，1 MB
LADDER = [2400, 2000, 1600, 1280, 1024]   # 最长边逐档下调


def dimensions(path: Path) -> tuple[int, int] | None:
    try:
        out = subprocess.run(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
            capture_output=True, text=True, timeout=30,
        ).stdout
        w = h = None
        for line in out.splitlines():
            if "pixelWidth:" in line:
                w = int(line.split(":")[1])
            if "pixelHeight:" in line:
                h = int(line.split(":")[1])
        return (w, h) if w and h else None
    except Exception:
        return None


def shrink(path: Path) -> dict:
    before = path.stat().st_size
    dim = dimensions(path)
    rec = {
        "file": str(path.relative_to(ROOT)),
        "before": before,
        "dim_before": dim,
        "after": before,
        "dim_after": dim,
        "steps": [],
    }
    if not dim:
        rec["error"] = "读不出尺寸，跳过"
        return rec

    backup = path.with_suffix(path.suffix + ".orig")
    shutil.copy2(path, backup)
    try:
        for max_side in LADDER:
            if max(dim) <= max_side:
                continue          # 本来就比这一档小，跳过
            subprocess.run(
                ["sips", "-Z", str(max_side), str(path)],
                capture_output=True, timeout=60, check=True,
            )
            size = path.stat().st_size
            dim = dimensions(path) or dim
            rec["steps"].append({"max_side": max_side, "size": size})
            if size <= LIMIT:
                break
        rec["after"] = path.stat().st_size
        rec["dim_after"] = dimensions(path)
        # 压完反而变大（极少见，PNG 重编码可能如此）就还原
        if rec["after"] >= rec["before"]:
            shutil.copy2(backup, path)
            rec["after"] = rec["before"]
            rec["dim_after"] = rec["dim_before"]
            rec["reverted"] = True
    except Exception as e:
        shutil.copy2(backup, path)
        rec["error"] = f"{type(e).__name__}: {e}，已还原"
    finally:
        backup.unlink(missing_ok=True)
    return rec


def main() -> None:
    global ATTACH, LIMIT
    dry = "--dry-run" in sys.argv
    for i, a in enumerate(sys.argv):
        if a == "--dir" and i + 1 < len(sys.argv):
            ATTACH = ROOT / sys.argv[i + 1]
        if a == "--limit" and i + 1 < len(sys.argv):
            LIMIT = int(sys.argv[i + 1])
    if not ATTACH.exists():
        sys.exit(f"{ATTACH} 不存在")

    # 两道必须的防护：
    # 1. 只处理真正的图片。曾经差点把 .git/objects/pack/*.pack 当图片压，
    #    那会直接损坏 git 仓库。
    # 2. 跳过任何 .git 目录。
    IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".tiff", ".bmp"}

    def eligible(p: Path) -> bool:
        return (
            p.is_file()
            and p.suffix.lower() in IMG_EXT
            and ".git" not in p.parts
            and p.stat().st_size > LIMIT
        )

    big = sorted((p for p in ATTACH.rglob("*") if eligible(p)), key=lambda p: -p.stat().st_size)
    total_all = sum(p.stat().st_size for p in ATTACH.rglob("*")
                    if p.is_file() and ".git" not in p.parts)
    total_big = sum(p.stat().st_size for p in big)
    print(f"attachments/ 共 {sum(1 for p in ATTACH.rglob('*') if p.is_file()):,} 个文件，"
          f"{total_all / 1e9:.2f} GB")
    print(f"其中超过 {LIMIT / 1000:.0f} KB 的图片 {len(big)} 个，占 {total_big / 1e9:.2f} GB "
          f"（{total_big / total_all * 100:.0f}%）")

    if dry:
        print("\n最大的 10 个：")
        for p in big[:10]:
            print(f"  {p.stat().st_size / 1e6:>6.1f} MB  {p.relative_to(ROOT)}")
        return

    # 并行：每张图要跑多次 sips（读尺寸 + 逐档缩放），单张大图就要好几秒。
    # 串行实测 2 分钟只处理 3 张，224 张要两小时；进程池能把它压到几分钟。
    workers = max(2, (os.cpu_count() or 4) - 1)
    print(f"\n用 {workers} 个进程并行压缩…")
    records = []
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(shrink, p): p for p in big}
        for i, fut in enumerate(as_completed(futs), 1):
            try:
                records.append(fut.result())
            except Exception as e:
                records.append({"file": str(futs[fut]), "before": 0, "after": 0,
                                "error": f"{type(e).__name__}: {e}"})
            if i % 25 == 0 or i == len(big):
                saved = sum(r["before"] - r["after"] for r in records)
                print(f"  {i}/{len(big)}  已省 {saved / 1e6:.0f} MB")

    saved = sum(r["before"] - r["after"] for r in records)
    failed = [r for r in records if "error" in r]
    still_big = [r for r in records if r["after"] > LIMIT]
    print(f"\n完成：处理 {len(records)} 张，省下 {saved / 1e6:.0f} MB")
    print(f"  仍超 1 MB 的 {len(still_big)} 张（缩到 1024 仍超标，属超大原图）")
    if failed:
        print(f"  失败 {len(failed)} 张（已还原原图）")
    now = sum(p.stat().st_size for p in ATTACH.rglob("*") if p.is_file())
    print(f"  attachments/ 现在 {now / 1e9:.2f} GB")

    (ROOT / "meta" / f"shrink_report_{ATTACH.name}.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print("  明细 → meta/shrink_report.json")


if __name__ == "__main__":
    main()
