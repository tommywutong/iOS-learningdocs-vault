#!/usr/bin/env python3
"""把待翻译文件切成互不重叠的分片，每片交给一个翻译 agent。

    python3 tools/shard.py --shards 8 --budget 90000            # 全部来源
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


def cmd_shard(shards: int, budget: int | None, source: str | None) -> None:
    items = collect(source)
    if not items:
        print("没有待翻译的文件了")
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

    cmd_shard(opt("--shards", 8, int), opt("--budget", None, int), opt("--source"))


if __name__ == "__main__":
    main()
