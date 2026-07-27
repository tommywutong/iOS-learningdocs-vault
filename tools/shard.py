#!/usr/bin/env python3
"""把待翻译文件切成互不重叠的分片，每片交给一个翻译 agent。

    python3 tools/shard.py --shards 8 --budget 130000 --scope core   # 底层相关框架 + WWDC
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
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from translate_plan import ROOT, collect  # noqa: E402

SHARD_DIR = ROOT / "meta" / "shards"

# objc.io 的 149 篇在仓库里已经有 objccn 的**官方中文译文**（配对表
# meta/blog_index/objcio_objccn_pairs.json，149/149 两侧文件都在、
# 中文侧正文中位 9,749 字符）。再译一遍是纯浪费 277 万字符，永久排除。
PAIRED_TABLE = ROOT / "meta" / "blog_index" / "objcio_objccn_pairs.json"


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


def in_scope(rel_en: str, scope: str) -> bool:
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
    raise SystemExit(f"未知范围 {scope!r}，可选 core / apple / all")


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


def cmd_shard(shards: int, budget: int | None, source: str | None,
              scope: str = "all") -> None:
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
    # 单组上限取单片 budget 的一半，保证一片总能装下两组以上，装箱才有均衡余地
    bins = pack(group_items(items, (budget or 200_000) // 2), shards, budget)
    SHARD_DIR.mkdir(parents=True, exist_ok=True)
    for old in SHARD_DIR.glob("shard-*.json"):
        old.unlink()

    print(f"待译 {len(items)} 个文件 / {sum(i['chars'] for i in items):,} 字符 → {shards} 片\n")
    for n, groups in enumerate(bins, 1):
        if not groups:
            continue
        files = [f for g in groups for f in g["files"]]
        chars = sum(g["chars"] for g in groups)
        out = SHARD_DIR / f"shard-{n:02d}.json"
        out.write_text(json.dumps({
            "shard": n, "groups": groups,
            "file_count": len(files), "chars": chars,
        }, ensure_ascii=False, indent=1), encoding="utf-8")
        head = ", ".join(g["group"].split("/")[-1] for g in groups[:3])
        print(f"  shard-{n:02d}  {len(files):>4} 篇  {chars:>9,} 字符  {len(groups):>3} 组   {head}…")


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

    cmd_shard(opt("--shards", 8, int), opt("--budget", None, int),
              opt("--source"), opt("--scope", "all"))


if __name__ == "__main__":
    main()
