#!/usr/bin/env python3
"""把待翻译文件切成互不重叠的分片，每片交给一个翻译 agent。

    python3 tools/shard.py --shards 12 --scope summer               # 暑期计划严格白名单
    python3 tools/shard.py --shards 8 --scope summer-b1             # 高价值博客补强白名单
    python3 tools/shard.py --shards 8 --scope summer-snapshots      # 计划内英文网页快照
    python3 tools/shard.py --shards 4 --scope legacy-review         # 36 篇早期译文补审
    python3 tools/shard.py --shards 8 --budget 130000 --scope core  # 已停止的旧宽泛范围
    python3 tools/shard.py --shards 8 --source apple-docs       # 只切一个来源
    python3 tools/shard.py --status                             # 看现有分片进度

## 为什么不用 translate_plan.py next

`next` 每次都写同一个 `meta/translate_batch.json`。多个 agent 并行时后启动的会
覆盖先启动的，两个 agent 领到同一批文件 —— 白干一半，还可能互相覆盖译文。
这里一次性产出 N 个不相交的分片文件，每个 agent 只认自己那一个。

## 切片原则（与 translate_plan.py 一致）

1. **按 group（目录）聚合**，同一份文档不拆开 —— 术语一致性靠这个保证。
2. **按字符数均衡**，不按文件数。6 KB 和 60 KB 的文章都有。
3. **优先级在前**：命中学习计划关键词的 group 先入片。

分片用贪心装箱：group 按（优先级, 体积降序）排，每次投给当前最空的箱子。
这样既保住 group 完整，又让各片工作量接近。
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from translate_plan import ROOT, collect  # noqa: E402

SHARD_DIR = ROOT / "meta" / "shards"

# objc.io 的 149 篇在仓库里已经有 objccn 的**官方中文译文**（配对表
# meta/blog_index/objcio_objccn_pairs.json，149/149 两侧文件都在、
# 中文侧正文中位 9,749 字符）。再译一遍是纯浪费 277 万字符，永久排除。
PAIRED_TABLE = ROOT / "meta" / "blog_index" / "objcio_objccn_pairs.json"
LEGACY_REVIEW_COMMIT = "9ee8b4b4efd0191076d07f11a8ed153ee12679d1"


def already_translated_elsewhere() -> set[str]:
    if not PAIRED_TABLE.exists():
        return set()
    data = json.loads(PAIRED_TABLE.read_text(encoding="utf-8"))
    return {p["en_file"] for p in data.get("pairs", [])
            if (ROOT / p["zh_file"]).exists()}


# 命名范围。`core` 对应用户 2026 暑假 8 周 iOS 底层学习计划真正涉及的框架：
# 对象模型与内存（objectivec / foundation）、runtime、并发（dispatch / swift 并发）、
# RunLoop 与响应链（uikit）、渲染（quartzcore）、编译链接与启动、调试与性能（xcode）、
# 内核接口（kernel）。刻意排除 swiftui / storekit / avfoundation / security / metal
# 这些与「底层」无直接关系的框架。
CORE_PREFIXES = (
    "objectivec", "dispatch", "kernel", "uikit", "xcode", "foundation",
    "os", "quartzcore", "coreanimation", "observation", "swift",
)


@lru_cache(maxsize=1)
def summer_allowlist() -> frozenset[str]:
    """从 SUMMER_TRANSLATION_PLAN.md 的 B0/O1/O2 三段提取严格白名单。"""
    plan = ROOT / "meta" / "SUMMER_TRANSLATION_PLAN.md"
    text = plan.read_text(encoding="utf-8")
    boundaries = (
        ("## 2. B0", "## 3.", "blogs/en/"),
        ("## 3.", "## 4.", "apple-docs/en/"),
        ("## 4.", "## 5.", "wwdc/en/"),
    )
    paths: set[str] = set()
    for start, end, prefix in boundaries:
        if start not in text or end not in text.split(start, 1)[1]:
            raise SystemExit(f"暑期计划缺少预期章节边界：{start} → {end}")
        block = text.split(start, 1)[1].split(end, 1)[0]
        paths.update(
            path
            for path in re.findall(r"^- `([^`]+)`", block, re.MULTILINE)
            if path.startswith(prefix)
        )
    if len(paths) != 69:
        raise SystemExit(f"暑期白名单应为 69 篇，实得 {len(paths)}；请先审阅计划格式变化")
    return frozenset(paths)


@lru_cache(maxsize=1)
def summer_b1_allowlist() -> frozenset[str]:
    """从计划的 B1 章节提取逐篇筛选后的高价值博客白名单。"""
    plan = ROOT / "meta" / "SUMMER_TRANSLATION_PLAN.md"
    text = plan.read_text(encoding="utf-8")
    start, end = "## 5. B1", "## 6."
    if start not in text or end not in text.split(start, 1)[1]:
        raise SystemExit(f"暑期计划缺少预期章节边界：{start} → {end}")
    block = text.split(start, 1)[1].split(end, 1)[0]
    paths = {
        path
        for path in re.findall(r"^- `([^`]+)`", block, re.MULTILINE)
        if path.startswith("blogs/en/")
    }
    if len(paths) != 32:
        raise SystemExit(f"B1 白名单应为 32 篇，实得 {len(paths)}；请先审阅计划格式变化")
    return frozenset(paths)


@lru_cache(maxsize=1)
def summer_snapshot_allowlist() -> frozenset[str]:
    """从计划 B2 章节提取与 iOS 暑期计划直接相关的英文网页快照。"""
    plan = ROOT / "meta" / "SUMMER_TRANSLATION_PLAN.md"
    text = plan.read_text(encoding="utf-8")
    start, end = "## 6. B2", "## 7."
    if start not in text or end not in text.split(start, 1)[1]:
        raise SystemExit(f"暑期计划缺少预期章节边界：{start} → {end}")
    block = text.split(start, 1)[1].split(end, 1)[0]
    block = block.split("明确排除：", 1)[0]
    paths = {
        path
        for path in re.findall(r"^- `([^`]+)`", block, re.MULTILINE)
        if path.startswith("blogs/snapshots/")
    }
    if len(paths) != 28:
        raise SystemExit(f"B2 快照白名单应为 28 篇，实得 {len(paths)}；请先审阅计划格式变化")
    return frozenset(paths)


@lru_cache(maxsize=1)
def legacy_review_allowlist() -> frozenset[str]:
    """从恢复提交提取 36 篇新增 Apple 译文对应的英文原文。"""
    result = subprocess.run(
        [
            "git",
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "--diff-filter=A",
            "-r",
            LEGACY_REVIEW_COMMIT,
        ],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    paths = {
        path.replace("/zh/", "/en/", 1)
        for path in result.stdout.splitlines()
        if path.startswith("apple-docs/zh/") and path.endswith(".md")
    }
    if len(paths) != 36:
        raise SystemExit(f"早期补审范围应为 36 篇，实得 {len(paths)}")
    missing = [path for path in paths if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"早期补审英文原文不存在：{missing[0]}")
    return frozenset(paths)


def in_scope(rel_en: str, scope: str) -> bool:
    if scope == "summer":
        return rel_en in summer_allowlist()
    if scope == "summer-b1":
        return rel_en in summer_b1_allowlist()
    if scope == "summer-snapshots":
        return rel_en in summer_snapshot_allowlist()
    if scope == "legacy-review":
        return rel_en in legacy_review_allowlist()
    if scope == "all":
        return True
    if rel_en.startswith("wwdc/"):
        return True
    if scope == "apple":                      # Apple 官方全部 + WWDC
        return rel_en.startswith("apple-docs/")
    if scope == "core":                       # 底层相关框架 + WWDC
        if not rel_en.startswith("apple-docs/en/"):
            return False
        rest = rel_en[len("apple-docs/en/"):]
        return any(rest.startswith(p) for p in CORE_PREFIXES)
    raise SystemExit(
        f"未知范围 {scope!r}，可选 summer / summer-b1 / summer-snapshots / "
        "legacy-review / core / apple / all"
    )


def translation_target(rel: str) -> str:
    if rel.startswith("blogs/snapshots/"):
        return rel.replace("blogs/snapshots/", "blogs/snapshots-zh/", 1)
    return rel.replace("/en/", "/zh/", 1)


def collect_allowlist(
    paths: frozenset[str],
    source: str | None = None,
    *,
    include_existing: bool = False,
) -> list[dict]:
    """直接从显式白名单构造任务，不经过会排除短 API 页的通用 collect()。"""
    items: list[dict] = []
    for rel in sorted(paths):
        source_name = rel.split("/", 1)[0]
        if source and source_name != source:
            continue
        en = ROOT / rel
        if not en.exists():
            raise SystemExit(f"白名单英文原文不存在：{rel}")
        zh = translation_target(rel)
        if (ROOT / zh).exists() and not include_existing:
            continue
        priority = 0 if source_name == "blogs" else 1 if source_name == "apple-docs" else 2
        items.append({
            "source": source_name,
            "group": str(Path(rel).parent),
            "priority": priority,
            "chars": len(en.read_text(encoding="utf-8")),
            "en": rel,
            "zh": zh,
        })
    return items


# 只有 Apple 文档需要按目录聚合：同一份文档的页面互相引用、术语必须一致，
# 交给同一个 agent 比事后对齐便宜。博客和 WWDC 的每一篇都是独立作品，
# 按目录聚合只会得到「mikeash 一组 386 万字符」这种撑破 budget 的巨组。
GROUP_BY_DIR = {"apple-docs"}


def group_items(items: list[dict], max_group: int) -> list[dict]:
    """把文件聚成组。

    Apple 文档按目录聚合，博客/WWDC 一篇一组。
    聚合后仍然超过 max_group 的组（uikit 这种 259 篇的目录）继续按序切块——
    切块边界在同目录内部，术语一致性的损失有限，但能让各片工作量真的均衡。
    """
    buckets: dict[tuple[str, str], dict] = {}
    for it in items:
        key = (it["source"], it["group"] if it["source"] in GROUP_BY_DIR else it["en"])
        g = buckets.setdefault(key, {
            "source": it["source"], "group": it["group"],
            "priority": it["priority"], "chars": 0, "files": [],
        })
        g["files"].append({"en": it["en"], "zh": it["zh"], "chars": it["chars"]})
        g["chars"] += it["chars"]
        g["priority"] = min(g["priority"], it["priority"])

    out: list[dict] = []
    for g in buckets.values():
        if g["chars"] <= max_group or len(g["files"]) == 1:
            out.append(g)
            continue
        chunk: list[dict] = []
        size = 0
        part = 1
        for f in g["files"]:
            if chunk and size + f["chars"] > max_group:
                out.append({**g, "group": f'{g["group"]} #{part}',
                            "chars": size, "files": chunk})
                chunk, size, part = [], 0, part + 1
            chunk.append(f)
            size += f["chars"]
        if chunk:
            out.append({**g, "group": f'{g["group"]} #{part}',
                        "chars": size, "files": chunk})
    return out


def pack(groups: list[dict], shards: int, budget: int | None) -> list[list[dict]]:
    """贪心装箱：优先级升序、同优先级内体积降序，每次投给最空的箱。

    budget 是单片字符上限。给了 budget 就只装满 shards 个箱子后停手
    （剩下的留给下一轮），不给就把全部 group 摊到 shards 片里。
    """
    groups = sorted(groups, key=lambda g: (g["priority"], -g["chars"]))
    bins: list[list[dict]] = [[] for _ in range(shards)]
    load = [0] * shards
    left: list[dict] = []
    for g in groups:
        i = min(range(shards), key=lambda k: load[k])
        if budget is not None and load[i] + g["chars"] > budget and bins[i]:
            left.append(g)
            continue
        bins[i].append(g)
        load[i] += g["chars"]
    if budget is not None and left:
        print(f"（本轮未入片 {len(left)} 组 / {sum(g['chars'] for g in left):,} 字符，下一轮再切）")
    return bins


def cmd_shard(
    shards: int,
    budget: int | None,
    source: str | None,
    scope: str = "all",
    prefix: str = "shard",
) -> None:
    allowlists = {
        "summer": summer_allowlist,
        "summer-b1": summer_b1_allowlist,
        "summer-snapshots": summer_snapshot_allowlist,
        "legacy-review": legacy_review_allowlist,
    }
    if scope in allowlists:
        items = collect_allowlist(
            allowlists[scope](),
            source,
            include_existing=scope == "legacy-review",
        )
    else:
        items = collect(source)
    skip = already_translated_elsewhere()
    n0, c0 = len(items), sum(i["chars"] for i in items)
    items = [i for i in items if i["en"] not in skip and in_scope(i["en"], scope)]
    if n0 != len(items):
        c1 = sum(i["chars"] for i in items)
        print(f"范围 {scope}：{n0} 篇 / {c0:,} 字符 → {len(items)} 篇 / {c1:,} 字符"
              f"（其中 {len(skip)} 篇已有他处官方中文译文，永久排除）")
    if not items:
        print("该范围内没有待翻译的文件了")
        return
    if scope in allowlists:
        allowlist = allowlists[scope]()
        expected = sum(
            1
            for rel in allowlist
            if (not source or rel.startswith(source + "/"))
            and (
                scope == "legacy-review"
                or not (ROOT / translation_target(rel)).exists()
            )
        )
        if len(items) != expected:
            raise SystemExit(f"{scope} 分片覆盖异常：应有 {expected} 篇，实得 {len(items)}")
    # 单组上限取单片 budget 的一半，保证一片总能装下两组以上，装箱才有均衡余地
    bins = pack(group_items(items, (budget or 200_000) // 2), shards, budget)
    SHARD_DIR.mkdir(parents=True, exist_ok=True)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,39}", prefix):
        raise SystemExit("分片前缀只能包含字母、数字、点、下划线和连字符")
    for old in SHARD_DIR.glob(f"{prefix}-*.json"):
        old.unlink()

    print(f"待译 {len(items)} 个文件 / {sum(i['chars'] for i in items):,} 字符 → {shards} 片\n")
    for n, groups in enumerate(bins, 1):
        if not groups:
            continue
        files = [f for g in groups for f in g["files"]]
        chars = sum(g["chars"] for g in groups)
        out = SHARD_DIR / f"{prefix}-{n:02d}.json"
        out.write_text(json.dumps({
            "shard": n, "groups": groups,
            "file_count": len(files), "chars": chars,
        }, ensure_ascii=False, indent=1), encoding="utf-8")
        head = ", ".join(g["group"].split("/")[-1] for g in groups[:3])
        print(
            f"  {prefix}-{n:02d}  {len(files):>4} 篇  {chars:>9,} 字符  "
            f"{len(groups):>3} 组   {head}…"
        )


def cmd_status() -> None:
    if not SHARD_DIR.exists():
        print("还没有分片")
        return
    for p in sorted(SHARD_DIR.glob("shard-*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        done = sum(1 for g in d["groups"] for f in g["files"] if (ROOT / f["zh"]).exists())
        print(f"  {p.name}  {done}/{d['file_count']} 篇已出译文")


def main() -> None:
    argv = sys.argv[1:]
    if "--status" in argv:
        cmd_status()
        return

    def opt(name, default=None, cast=str):
        for i, a in enumerate(argv):
            if a == name and i + 1 < len(argv):
                return cast(argv[i + 1])
        return default

    cmd_shard(
        opt("--shards", 8, int),
        opt("--budget", None, int),
        opt("--source"),
        opt("--scope", "all"),
        opt("--prefix", "shard"),
    )


if __name__ == "__main__":
    main()
