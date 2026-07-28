#!/usr/bin/env python3
"""翻译批次调度与进度追踪。

    python3 tools/translate_plan.py status                     # 总体进度
    python3 tools/translate_plan.py next [--budget 60000]      # 取下一批任务
    python3 tools/translate_plan.py next --source wwdc         # 只从某个来源取
    python3 tools/translate_plan.py verify                     # 对已译部分跑机械校验

## 为什么需要这个

要翻译的成篇文章约 3,962 篇（Apple 文档）+ 178 场 WWDC + 约 1,100 篇英文博客。
一个翻译 agent 一次能稳定处理的量是有限的，所以要切批次。切批的原则：

1. **按文档/目录聚合**，不跨主题切。同一份文档的页面里术语要一致，交给同一个
   agent 比事后对齐便宜得多。
2. **按字符数控制批量**，不按文件数。Apple 文档里 6 KB 和 60 KB 的文章都有，
   按篇数切会导致批次工作量差十倍。
3. **优先级**：用户学习计划涉及的主题优先（第一周到第八阶段的顺序），其余按
   框架重要性。

## 输出怎么用

`next` 输出的是给翻译 agent 的任务清单（JSON + 人读摘要）。每批交给一个
Sonnet agent 翻译，完成后交给一个 Opus agent 审校，最后跑 `validate.py`。
三道关都过了才算完成。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "meta"

# 来源 → (英文目录, 中文目录, 是否需要翻译)
SOURCES = {
    "apple-docs": ("apple-docs/en", "apple-docs/zh", True),
    "wwdc": ("wwdc/en", "wwdc/zh", True),
    "blogs": ("blogs/en", "blogs/zh", True),
    "snapshots": ("blogs/snapshots", "blogs/snapshots-zh", True),
}

# 用户 2026 暑假学习计划的主题顺序，用来定优先级。
# 越靠前的框架/关键词越早翻译，好让译文赶上他的学习进度。
PRIORITY_KEYWORDS = [
    # 第一、二周：对象模型、内存管理、Block
    "objectivec", "memory", "arc", "retain", "weak", "block", "autorelease",
    # 第三周：runtime 行为、KVC/KVO、通信
    "runtime", "kvo", "keyvalue", "notification", "delegate", "category",
    # 第四周：并发与锁
    "dispatch", "concurrency", "thread", "lock", "operation", "actor", "async",
    # 第五周：RunLoop、响应链、生命周期
    "runloop", "responder", "viewcontroller", "lifecycle", "event",
    # 第六周：渲染与性能
    "quartzcore", "coreanimation", "layer", "render", "offscreen", "tableview",
    "collectionview", "performance", "hitch",
    # 第七周：编译链接、Mach-O、dyld、启动
    "macho", "dyld", "launch", "link", "library", "framework", "startup",
    # 第八阶段：持久化、序列化、网络、架构
    "coredata", "swiftdata", "persist", "json", "codable", "url", "network",
]


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            fm[k.strip()] = v.strip().strip("'")
    return fm


def is_longform(path: Path, source: str) -> bool:
    """只翻译成篇文章。WWDC 和博客整体都算；Apple 文档看 symbol_kind。"""
    if source == "snapshots":
        return read_frontmatter(path).get("original_language") == "en"
    if source != "apple-docs":
        return True
    fm = read_frontmatter(path)
    return fm.get("symbol_kind", "") in (
        "article", "overview", "collection", "sampleCode", "module", "symbol-collection",
    ) or fm.get("role", "") in ("article", "collectionGroup", "sampleCode")


def priority(rel: str) -> int:
    """越小越优先。命中学习计划关键词的排前面，命中越早的越优先。"""
    low = rel.lower()
    for i, kw in enumerate(PRIORITY_KEYWORDS):
        if kw in low:
            return i
    return len(PRIORITY_KEYWORDS)


def collect(source: str | None = None) -> list[dict]:
    """收集所有待翻译的文件。"""
    items = []
    for name, (en_dir, zh_dir, needs) in SOURCES.items():
        if source and name != source:
            continue
        if not needs:
            continue
        en_root = ROOT / en_dir
        if not en_root.exists():
            continue
        for f in en_root.rglob("*.md"):
            rel = f.relative_to(en_root)
            zh = ROOT / zh_dir / rel
            if zh.exists():
                continue
            if not is_longform(f, name):
                continue
            size = f.stat().st_size
            items.append({
                "source": name,
                "en": str(f.relative_to(ROOT)),
                "zh": str((ROOT / zh_dir / rel).relative_to(ROOT)),
                "group": str(rel.parent),
                "chars": size,
                "priority": priority(str(rel)),
            })
    items.sort(key=lambda x: (x["priority"], x["source"], x["group"], x["en"]))
    return items


def cmd_status() -> None:
    print(f"{'来源':14}{'英文':>8}{'需译':>8}{'已译':>8}{'待译':>8}{'待译字符':>12}")
    grand = [0, 0, 0, 0]
    for name, (en_dir, zh_dir, needs) in SOURCES.items():
        en_root, zh_root = ROOT / en_dir, ROOT / zh_dir
        if not en_root.exists():
            continue
        en_files = list(en_root.rglob("*.md"))
        need = [f for f in en_files if is_longform(f, name)]
        done = [f for f in need if (zh_root / f.relative_to(en_root)).exists()]
        todo = [f for f in need if not (zh_root / f.relative_to(en_root)).exists()]
        chars = sum(f.stat().st_size for f in todo)
        print(f"{name:14}{len(en_files):>8}{len(need):>8}{len(done):>8}{len(todo):>8}{chars:>12,}")
        grand = [g + v for g, v in zip(grand, [len(en_files), len(need), len(done), len(todo)])]
    print(f"{'合计':14}{grand[0]:>8}{grand[1]:>8}{grand[2]:>8}{grand[3]:>8}")


def cmd_next(budget: int, source: str | None) -> None:
    """按字符预算取一批，尽量整目录整份文档地取，不把一份文档切到两批。"""
    items = collect(source)
    if not items:
        print("没有待翻译的文件了")
        return

    batch, total = [], 0
    cur_group = None
    for it in items:
        # 换组时如果已经超预算就停，保证一份文档不被切散
        if it["group"] != cur_group and total >= budget:
            break
        cur_group = it["group"]
        batch.append(it)
        total += it["chars"]

    groups: dict[str, list[dict]] = {}
    for it in batch:
        groups.setdefault(f"{it['source']}/{it['group']}", []).append(it)

    print(f"本批 {len(batch)} 个文件，{total:,} 字符，分 {len(groups)} 组：\n")
    for g, files in groups.items():
        gsize = sum(f["chars"] for f in files)
        print(f"  {g}  —— {len(files)} 篇，{gsize:,} 字符")
        for f in files[:4]:
            print(f"      {Path(f['en']).name}")
        if len(files) > 4:
            print(f"      …还有 {len(files) - 4} 篇")

    out = META / "translate_batch.json"
    out.write_text(json.dumps({
        "count": len(batch), "chars": total,
        "groups": {g: [f["en"] for f in fs] for g, fs in groups.items()},
        "files": batch,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n任务清单 → {out.relative_to(ROOT)}")
    print(f"剩余未入批：{len(items) - len(batch)} 个文件")


def cmd_verify() -> None:
    import subprocess
    for name, (en_dir, zh_dir, needs) in SOURCES.items():
        zh_root = ROOT / zh_dir
        if not needs or not zh_root.exists() or not any(zh_root.rglob("*.md")):
            continue
        print(f"\n=== {name} ===")
        subprocess.run(
            [sys.executable, str(ROOT / "tools" / "validate.py"), zh_dir],
            cwd=ROOT,
        )


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    budget = 60000
    source = None
    for i, a in enumerate(sys.argv):
        if a == "--budget" and i + 1 < len(sys.argv):
            budget = int(sys.argv[i + 1])
        if a == "--source" and i + 1 < len(sys.argv):
            source = sys.argv[i + 1]

    if cmd == "status":
        cmd_status()
    elif cmd == "next":
        cmd_next(budget, source)
    elif cmd == "verify":
        cmd_verify()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
