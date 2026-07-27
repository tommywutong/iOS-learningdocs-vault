#!/usr/bin/env python3
"""生成 README.md 和 _indexes/ 下的导航索引。

    python3 tools/indexes.py

所有数字都是**实际统计出来的**，不是写死的——内容增加后重跑一遍就刷新。
这样避免了旧仓库那种「README 写 35,753 个文件、实测 35,752 / 35,884 三个数都对不上」
的情况。
"""
from __future__ import annotations

import json
import os
import re
import statistics
import urllib.parse
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IDX = ROOT / "_indexes"


def read_fm(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")[:2000]
    except Exception:
        return {}
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


def count_md(base: Path) -> tuple[int, int]:
    n = sz = 0
    for p in base.rglob("*.md"):
        n += 1
        sz += p.stat().st_size
    return n, sz


def link(path: Path) -> str:
    return urllib.parse.quote(str(path.relative_to(ROOT)))


# ---------------------------------------------------------------- 各来源索引


def index_apple_docs() -> dict:
    base = ROOT / "apple-docs" / "en"
    if not base.exists():
        return {}
    per_fw: dict[str, dict] = defaultdict(lambda: {"total": 0, "longform": 0, "bytes": 0})
    LONG = {"article", "overview", "collection", "sampleCode", "module"}
    for p in base.rglob("*.md"):
        fw = p.relative_to(base).parts[0]
        fm = read_fm(p)
        d = per_fw[fw]
        d["total"] += 1
        d["bytes"] += p.stat().st_size
        if fm.get("symbol_kind") in LONG or fm.get("role") in ("article", "collectionGroup", "sampleCode"):
            d["longform"] += 1

    lines = [
        "# Apple 现行文档 · 按框架",
        "",
        f"> 来源：`developer.apple.com/documentation`，抓取于 {date.today()}。",
        "> 「成篇文章」是有正文、值得翻译的部分；其余是 API 条目（一两句话的摘要 + 声明）。",
        "",
        "| 框架 | 页面总数 | 成篇文章 | 体积 |",
        "|---|---:|---:|---:|",
    ]
    for fw, d in sorted(per_fw.items(), key=lambda x: -x[1]["total"]):
        lines.append(
            f"| [{fw}](../apple-docs/en/{urllib.parse.quote(fw)}/) "
            f"| {d['total']:,} | {d['longform']:,} | {d['bytes'] / 1e6:.1f} MB |"
        )
    tot = sum(d["total"] for d in per_fw.values())
    lf = sum(d["longform"] for d in per_fw.values())
    lines.append(f"| **合计** | **{tot:,}** | **{lf:,}** | |")
    (IDX / "apple-docs.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"total": tot, "longform": lf, "frameworks": len(per_fw)}


def index_wwdc() -> dict:
    base = ROOT / "wwdc" / "en"
    if not base.exists():
        return {}
    groups: dict[str, list] = defaultdict(list)
    years = Counter()
    for p in base.rglob("*.md"):
        fm = read_fm(p)
        groups[fm.get("group", "未分组")].append((fm, p))
        if fm.get("year") and fm["year"] != "null":
            years[fm["year"]] += 1

    lines = [
        "# WWDC session 逐字稿",
        "",
        f"> 按主题筛选的 {sum(len(v) for v in groups.values())} 场，抓取于 {date.today()}。",
        "> 逐字稿是 Apple 的自动语音识别产物，未经人工校对。",
        "",
        "**注意**：2013 年及更早的 session 已被 Apple 彻底下架，老年份也被大幅裁剪"
        "（WWDC2014 只剩 6 场）。这是归档的紧迫性所在。",
        "",
    ]
    for g in sorted(groups):
        # year 可能是 'null'（Tech Talks 这类没有年份的），不能直接 int()
        def year_of(fm: dict) -> int:
            v = fm.get("year") or ""
            return int(v) if v.isdigit() else 0

        items = sorted(groups[g], key=lambda x: (-year_of(x[0]), x[0].get("title", "")))
        ever = sum(1 for fm, _ in items if fm.get("evergreen") == "true")
        lines += [f"## {g}", "", f"{len(items)} 场，其中 {ever} 场标为「讲机制、长期有效」", ""]
        for fm, p in items:
            tag = "" if fm.get("evergreen") == "true" else " _(版本性)_"
            lines.append(
                f"- [{fm.get('title', p.stem)}]({link(p)}) "
                f"· {fm.get('collection', '')} · {fm.get('duration', '')}{tag}"
            )
        lines.append("")
    (IDX / "wwdc.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"total": sum(len(v) for v in groups.values()), "groups": len(groups)}


def index_blogs() -> dict:
    lines = [
        "# 第三方技术博客归档",
        "",
        "> **本仓库为私有个人学习归档。** 第三方博客大多是 All rights reserved 或未声明",
        "> 授权（法律上默认保留全部权利），存作个人资料与公开发布是两回事。",
        "> 逐源授权状况见下表，也记在 `meta/blog_sources.json` 每条的 `license` 字段。",
        "> 表内统计的是 Markdown 文件数；同一英文文章及其中文译文分别计为两个文件。",
        "",
        "已按 robots.txt 明确排除、**未抓取**的站点：`massicotte.org`、`casatwy.com`"
        "——它们在 `User-agent: *` 放开的同时单独点名禁止 ClaudeBot / anthropic-ai。",
        "",
        "| 源 | 文件数 | 中位字数 | 代码率 | 语言 | 状态 | 授权 |",
        "|---|---:|---:|---:|---|---|---|",
    ]
    cfgs = {}
    for name in ("blog_sources.json", "blog_sources_batch2.json"):
        f = ROOT / "meta" / name
        if f.exists():
            for s in json.loads(f.read_text(encoding="utf-8")).get("sources", []):
                cfgs[s["key"]] = s

    total = 0
    for lang in ("en", "zh"):
        base = ROOT / "blogs" / lang
        if not base.exists():
            continue
        for d in sorted(base.iterdir()):
            if not d.is_dir():
                continue
            files = list(d.glob("*.md"))
            if not files:
                continue
            sizes, fenced = [], 0
            for f in files:
                body = f.read_text(encoding="utf-8").split("---", 2)[-1]
                sizes.append(len(body))
                if "```" in body:
                    fenced += 1
            s = cfgs.get(d.name, {})
            total += len(files)
            lines.append(
                f"| [{s.get('name', d.name)}](../blogs/{lang}/{urllib.parse.quote(d.name)}/) "
                f"| {len(files)} | {int(statistics.median(sizes)):,} "
                f"| {fenced / len(files) * 100:.0f}% | {lang} "
                f"| {s.get('status', '')} | {s.get('license', '未记录')[:28]} |"
            )
    snap = ROOT / "blogs" / "snapshots"
    if snap.exists():
        n = len(list(snap.rglob("*.md")))
        total += n
        lines.append(f"| [学习计划点名的单页快照](../blogs/snapshots/) | {n} | | | 混合 | | 逐条不同 |")
    lines.append(f"| **合计** | **{total}** | | | | | |")
    (IDX / "blogs.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"total": total}


# ---------------------------------------------------------------- README


def main() -> None:
    IDX.mkdir(parents=True, exist_ok=True)
    ad = index_apple_docs()
    ww = index_wwdc()
    bl = index_blogs()

    att = ROOT / "attachments"
    n_att = sum(1 for p in att.rglob("*") if p.is_file()) if att.exists() else 0
    sz_att = sum(p.stat().st_size for p in att.rglob("*") if p.is_file()) if att.exists() else 0
    oss = ROOT / "oss"
    n_oss = sum(1 for p in oss.iterdir() if p.is_dir()) if oss.exists() else 0

    zh_counts = {
        k: len(list((ROOT / k / "zh").rglob("*.md"))) if (ROOT / k / "zh").exists() else 0
        for k in ("apple-docs", "wwdc", "blogs")
    }
    translated_counts = {}
    for source in ("apple-docs", "wwdc", "blogs"):
        en_root = ROOT / source / "en"
        zh_root = ROOT / source / "zh"
        translated_counts[source] = sum(
            1
            for path in en_root.rglob("*.md")
            if (zh_root / path.relative_to(en_root)).exists()
        ) if en_root.exists() and zh_root.exists() else 0

    readme = rf"""# Apple 文档与 iOS 底层知识归档

> 私有个人学习归档。本文件由 `tools/indexes.py` 扫描实际内容生成，**所有数字都是实测的**，
> 重跑一遍就刷新。生成于 {date.today()}。

## 一、这是什么

把 iOS 底层学习需要的一手材料抓成本地 Markdown，放进 Obsidian 阅读，并翻译成中文。
起因是 2026 暑假的一份八周 iOS 底层学习计划——计划里点名了 338 个外部链接，
散落在 Apple 官网、WWDC 视频、上百个技术博客里，读起来要不停开浏览器，
而且其中不少站点随时会消失（已实测到 3 个原站在归档期间已经打不开）。

四个来源：

| 来源 | 内容 | 数量 | 中文文件 | 其中由英文翻译 |
|---|---|---:|---:|---:|
| **Apple 现行文档** | `developer.apple.com/documentation`，{ad.get('frameworks', 0)} 个框架 | {ad.get('total', 0):,} 页（成篇文章 {ad.get('longform', 0):,}） | {zh_counts['apple-docs']:,} | {translated_counts['apple-docs']:,} |
| **WWDC 逐字稿** | 按主题从现存 1,560 场里筛出，{ww.get('groups', 0)} 个分组 | {ww.get('total', 0)} 场 | {zh_counts['wwdc']:,} | {translated_counts['wwdc']:,} |
| **第三方技术博客** | 经甄别的一手来源 | {bl.get('total', 0):,} 个 Markdown 文件 | {zh_counts['blogs']:,} | {translated_counts['blogs']:,} |
| **Apple 开源与 Swift 一手资料** | objc4 / dyld / CF / libdispatch / swift-evolution 等 | {n_oss} 个仓库 | — | — |

图片附件 {n_att:,} 个 / {sz_att / 1e9:.2f} GB。

> 博客的“中文文件”同时包含原生中文文章和英文文章的中文译文，不能把这个数字
> 直接当成翻译进度；“其中由英文翻译”才是可与 `blogs/en/` 一一对应的数量。
> 同一英文文章及其中文译文分别计为两个 Markdown 文件。

## 二、怎么用

| 我想… | 去哪 |
|---|---|
| **按学习计划找材料** | [`_indexes/study-plan.md`](_indexes/study-plan.md) —— 把学习计划的 338 个外链逐个映射到本地文件，按周次和 Day 组织。学到哪天点开哪个文件 |
| 按框架浏览 Apple 文档 | [`_indexes/apple-docs.md`](_indexes/apple-docs.md) |
| 找某个主题的 WWDC session | [`_indexes/wwdc.md`](_indexes/wwdc.md) —— 九个主题分组，标注了哪些「讲机制、长期有效」哪些「版本性会过时」 |
| 看博客归档与**授权状况** | [`_indexes/blogs.md`](_indexes/blogs.md) |
| 查术语该怎么译 | [`meta/TERMS.md`](meta/TERMS.md) |
| **让新的 AI 接手** | 先读 [`meta/PROJECT_STATUS.md`](meta/PROJECT_STATUS.md)，再按 [`meta/NEXT_STEPS.md`](meta/NEXT_STEPS.md) 的进度表领取下一批 |

**在 Obsidian 里打开仓库根目录**即可。英文原文和中文译文路径一一对应，
`en/` 换成 `zh/` 就是译文。

## 三、目录结构

```
apple-docs/{{en,zh}}/<框架>/**.md    Apple 现行文档
wwdc/{{en,zh}}/<年份>/*.md           WWDC 逐字稿
blogs/{{en,zh}}/<源>/*.md            第三方博客（中文源只有 zh/）
blogs/snapshots/<域名>/*.md        学习计划点名的单页快照
oss/<仓库>/                        Apple 开源与 Swift 一手资料
attachments/                       图片，各来源共用
_indexes/                          导航索引
meta/                              规范、术语表、清单、侦察报告
tools/                             抓取与渲染工具链
.cache/                            原始 JSON/HTML 缓存（已 gitignore）
```

**为什么英文原文要留着**：现行文档是 Apple 在维护的活内容，每年 WWDC 后会改。
每个文件 frontmatter 里有 `content_hash`，重抓时对比哈希就知道哪些页面变了，
只需重译变化的部分。如果原地替换成中文，就失去了这个基线。

## 四、翻译体系

**规范**：[`meta/TRANSLATION_STYLE.md`](meta/TRANSLATION_STYLE.md)

**术语表**：[`meta/TERMS.md`](meta/TERMS.md)，按 **Apple 官方简体中文优先**裁决，
226 条新增术语里 187 条有官方依据。核实方法是抓 Apple 官方中文 HIG 的
`/tutorials/data/zh-cn/...json` 接口（网页是 SPA，HTML 里没中文正文）。

几条容易踩的：

- `actor` / `Sendable` / `async` / `await` / `Liquid Glass` **保留英文**——官方中文标题就这么写
- `view controller` → 视图控制器、`collection view` → 集合视图（**不再保留英文**，Apple 官方中文这么译）
- `hitch` → **卡顿**、`hang` → **挂起**——不同量级的性能问题，混用会让整个性能章节不可读
- `delegate` → 委托（不是「代理」）

> 与旧仓库 `apple-developer-archive-vault` 的术语选择**有意分歧**（旧的按旧规范保留英文）。
> 两个独立语料，不要互相「纠正」。

**三道质量关**：

1. 译者 agent 按规范和术语表翻译
2. **独立**审校 agent（不是自审）拿原文+译文找问题
3. `tools/validate.py` 机械校验——**唯一确定性的一关**

第 3 关查的是硬指标：frontmatter 除 title 外零改动、链接与图片目标集合完全一致、
代码块行数与非注释行逐字符一致、标题层级/列表项数/表格行数/callout 类型一致、
无残留成句英文。经 **13 类错误注入测试，零漏检零误报**。

```bash
python3 tools/validate.py apple-docs/zh    # 必须零问题
```

## 五、工具链

```bash
# Apple 文档：三阶段，各自可断点续跑
python3 tools/fetch.py archives                    # 技术清单
python3 tools/fetch.py index  <archive>...         # 导航树 → manifest
python3 tools/fetch.py pages  <archive>... [--only-longform]
python3 tools/render.py       <archive>... [--longform]   # DocC JSON → Markdown
python3 tools/fetch_assets.py                      # 下载图片

# WWDC
python3 tools/wwdc.py fetch [--all]                # 默认抓 178 场短名单
python3 tools/wwdc.py render

# 第三方博客
python3 tools/blog.py probe <url>                  # 探正文容器 XPath
python3 tools/blog.py discover <key>...            # 建文章清单
python3 tools/blog.py fetch <key>...
python3 tools/blog.py render <key>...
python3 tools/snapshot.py targets|fetch|render     # 单页快照

# 翻译调度与校验
python3 tools/translate_plan.py status             # 进度
python3 tools/translate_plan.py next --budget 60000  # 取下一批（按学习计划优先级）
python3 tools/shard.py --shards 8 --budget 130000 --scope core  # 并行分片
python3 tools/shard.py --status                    # 当前分片产出情况
python3 tools/validate.py <目录>                    # 机械校验

# 维护
python3 tools/indexes.py                           # 重新生成 README 和索引
python3 tools/studyplan.py                         # 重新生成学习计划映射
python3 tools/shrink_assets.py --dir <目录> --limit <字节>  # 压缩超大图
```

**原始数据全部缓存在 `.cache/`**，所以调整 Markdown 格式只需重跑 render，不用重抓。

## 六、构建过程中踩过的坑

这一节是给以后维护的人（也包括未来的我）看的。每条都是实际踩过、排查过的。

**抓取层**

1. **引用 URL 大小写不一致**：Apple 的索引端点给全小写路径，但页面内 references 有 21%（3,899 处）带大写。macOS 文件系统大小写不敏感所以本地看不出问题，一推到 Linux/GitHub 上链接全断。规则统一在 `tools/paths.py`，**fetch 和 render 必须共用同一份**。
2. **7,018 个路径含冒号**（Swift 方法签名 `init(a:b:)`），Windows 非法，会导致仓库无法 checkout。
3. **单个文件名超 255 字节**：AVFoundation 有个初始化方法百分号编码后超 400 字节，直接 OSError 掀翻整批。**抓取必须容忍单页失败**，否则跑一小时被一个边缘 case 毁掉。
4. **httpx 默认连接池等待无上限**：一个请求没正常释放连接，后续请求会永久挂起——表现是进程活着、CPU 0%、一页不落。实测卡了 15 分钟才发现。必须设 `pool` 超时 + `asyncio.wait_for` 硬超时。
5. **RSS/Atom feed 普遍被截断**：onevcat 的 feed 只给 5 篇而 sitemap 有 498 篇。**归档一律优先 sitemap 或全量索引页**。
6. **sitemap 条数 ≠ 文章数**：lowlevelbits 的 242 条里 202 条是 `/tags/` 标签页，真文章只有 40 篇。每个源都要配 `exclude` 正则。

**渲染层——静默失败是最大的敌人**

「渲染报告说成功 N 篇零失败」**完全不能证明内容没丢**。这个项目踩过六次静默失败，
全靠体检指标（中位正文字数、代码块覆盖率）才发现：

7. **sealiesoftware 报告成功 29 篇零失败，实际每篇只有 23 行、正文全丢**——那个 2013 年的站用 `<table>` 做页面布局，转换器没处理 `<tr>`/`<td>`，递归到一半就断。
8. **onevcat 176 篇里只有 3 篇有代码**——它用 Hexo 的行号表格高亮，代码在 `<td class="rouge-code">`，直接找 `<pre>` 取到的是**行号那一格**（`1\n2\n3...`）。
9. **修第 8 条时踩的反向坑**：新逻辑在整棵子树里找代码单元格，命中了外层文章容器，**整篇正文被换成一个代码块**。maskray 中位字数从 15,626 崩到 573。必须加「占比 >90% 才算代码块」的守卫。
10. **Hexo 的 `figure.highlight` 套在 `<p>` 里**时走行内路径，代码被压成一行、行号粘在代码前（`12(lldb) po ...`）。文件字数看着正常。
11. **CSDN 的反爬页 HTTP 521、只有 2KB，但混淆 JS 有 1800 多字符**，按 `text_content()` 量比很多真文章还长，差点被当正文收下。判据要改成扣掉 script/style 的**可见文本长度**。
12. **行内标签直接挂在块级容器下会被整个丢弃**——`<li><code>x</code>文字</li>` 里的 `<code>` 从来没被读到。这条影响全部已有源，修复后回归找回正文 71,084 词元。

**通用抽取器不能用**：实测 trafilatura 会抹平 mikeash 的代码缩进、丢失 ibireme 全部 15 个代码块、把标题抽成「163 评论」。对代码为主的技术归档，丢缩进等于毁资料。所以 `tools/html2md.py` 自己走 DOM，`<pre>` 一律 `text_content()` 原样输出。

**旧归档那侧（补齐项目用得上）**

13. **Apple 的 404 页有 82,981 字节**，比大多数真实归档页还大。「响应够大就算成功」会把 404 页写进仓库。必须校验 `status==200` **且** 含 `<article id="contents"`。
14. **裸目录 URL 返回 1,610 字节空壳，补 `_index.html` 才返回 30,256 字节正文**，两者状态码都是 200。
15. **`library.json` 是非标准 JSON**（含尾随逗号），要先 `re.sub(r",(\s*[}}\]])", r"\1", raw)` 才能解析。

## 七、版权与授权

**本仓库为私有个人学习归档，不得转为公开。**

- **Apple 文档与 WWDC 逐字稿**：Apple 版权所有，无再分发许可
- **第三方博客**：逐源不同，见 [`_indexes/blogs.md`](_indexes/blogs.md) 和 `meta/blog_sources*.json` 的 `license` 字段
  - 明确允许再分发的只有三个：`onevcat`（CC BY 4.0，须署名+原文链接）、`saagarjha`（CC BY-SA 4.0，**译文作为衍生作品也必须以 BY-SA 发布**）、`nshipster`（CC BY-NC）
  - 其余为 All rights reserved 或未声明（法律上默认保留全部权利）
- **Apple 开源代码**：APSL 2.0 / Apache-2.0。APSL 要求分发时附全文许可 + 不删文件头声明，
  所以**源码目录保持逐字节原样，笔记一律写在 `oss/notes/`**，永远停在「unmodified copies」
- **按 robots.txt 明确排除、未抓取**：`massicotte.org`、`casatwy.com`、`blog.devtang.com`
  ——它们在 `User-agent: *` 放开的同时**单独点名禁止 ClaudeBot / anthropic-ai**。
  只看通配符段会误判为放开，`tools/blog.py` 里内置了针对性检查

## 八、已知缺口

见 [`meta/PROJECT_STATUS.md`](meta/PROJECT_STATUS.md) 与
[`meta/NEXT_STEPS.md`](meta/NEXT_STEPS.md)。主要几项：

- **翻译远未完成**：Apple / WWDC / 英文博客合计完成
  {translated_counts['apple-docs'] + translated_counts['wwdc'] + translated_counts['blogs']:,} 篇；
  完整 A 方案的剩余量和 Token 预算见后续计划表
- 学习计划单篇快照 108 条中已归档 86 条，剩余 22 条有明确失败原因
- 旧归档缺口已通过另一个仓库的 PR #10 补入 950 / 1,098 份，剩余 148 份
- `ming1016/study` 只保留了 Markdown 和技术文章配图，旅游/绘画类配图未收（见 `oss/study/README-归档说明.md`）
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print(f"README.md + _indexes/ 已生成")
    print(f"  Apple 文档 {ad.get('total', 0):,} 页（成篇 {ad.get('longform', 0):,}）")
    print(f"  WWDC {ww.get('total', 0)} 场 · 博客 {bl.get('total', 0):,} 个文件 · OSS {n_oss} 仓库")
    print(f"  图片 {n_att:,} 个 / {sz_att / 1e9:.2f} GB")


if __name__ == "__main__":
    main()
