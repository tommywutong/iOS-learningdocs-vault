# 项目状态与交接

> 最后更新：2026-07-26 22:40。换模型或换会话后，从这份文件接手。

## 一、四条线

| # | 项目 | 目标仓库 | 状态 |
|---|---|---|---|
| 1 | 补旧归档缺口 1,098 份 | `XiyouMobile3G-iOS/apple-developer-archive-vault`（组织，公开）→ 提 PR | 侦察完成，**被另一个进程阻塞** |
| 2 | Apple 现行文档镜像 + 翻译 | **`Biscoffee/<名字待定>`（个人账户，私有）** | 抓取中，样品已验收 |
| 3 | WWDC session 逐字稿 + 翻译 | 同上 | **英文侧已完成**（178 场） |
| 4 | 第三方优质博客归档 | 同上 | 抓取中（2,383 篇已建清单） |

## 二、需要用户决定的事（回来先看这节）

### 1. 仓库名（阻塞首次推送）

我建议 `apple-docs-vault`。目前本地目录叫 `apple-developer-docs-vault`。**GitHub 仓库还没建、一行代码没推。**

### 2. 术语表里 16 条待裁决，3 条高优先

★ **`View Controller` / `Collection View` / `Scroll View`** —— 旧仓库规范要求保留英文，但 Apple 官方中文译作「视图控制器 / 集合视图 / 滚动视图」。`view controller` 在现行 UIKit 语料里出现 **958 次，是全项目最高频术语簇**，选错代价最大。当前暂按旧规范保留英文。

★ **`control` → 控件（社区）还是 控制（Apple 官方）**；**`navigation` → 导航（社区）还是 导览（Apple 官方）**。当前暂按社区。

★ **`accessor`** —— 旧规范定「存取方法」（旧语料 29 次），但实际译文里「访问器」用了 **75 次**，反超 2.6:1。

其余 13 条见 `meta/TERMS.md` 第五节。已确认不必纠结的：`Liquid Glass` 保留英文（Apple 官方中文 HIG 通篇直接写原文，「液态玻璃」是媒体叫法）、`actor` / `Sendable` / `async/await` 全部保留英文（官方中文标题就这么写）。

### 3. 旧仓库那个翻译进程

**另一个 Claude Code 会话正在往组织的旧仓库写翻译并提交**（分支 `translate/cocoa-batch2`，本次观察期间一直在推进）。项目 1 要写同一个仓库，必须等它跑完或你让它停。**我全程没有对那个仓库做任何写操作。**

### 4. WWDC 归档范围

已按主题筛出 178 场（88 小时，9 个分组，122 场长期有效 / 56 场版本性）并全部抓完。全站现存 1560 场，要不要扩大？另外 **1355 场有 Apple 官方简体中文字幕**，可以拿来做术语校准和译文对照。

## 三、已确认的决定

- 新仓库放**个人账户 Biscoffee**、**私有**、不进组织
- 抓取范围：34 个 archive（不是全部 393 个技术）；`kernel` 只取长文
- 翻译范围：只译成篇文章，API 条目保留英文
- 目录布局：按来源分顶层目录，来源内按语言分 `en/` `zh/`，`attachments/` 在仓库根共用
- **英文源**：`en/` 存原文 + `zh/` 存译文 + frontmatter 带原始链接；**中文源**：只存 `zh/` + 链接
- 不原地替换英文（现行文档是活的，留基线才能靠 `content_hash` 做增量重抓）
- 模型分工：抓取/渲染/校验、翻译 → Sonnet 5；审校、术语表、翻译规范 → Opus 5

## 四、目录布局

```
├── apple-docs/{en,zh}/<archive>/**.md    Apple 现行文档
├── wwdc/{en,zh}/<collection>/*.md        WWDC 逐字稿
├── blogs/{en,zh}/<source>/*.md           第三方博客
├── attachments/<hash>/*                  图片，三个来源共用
├── meta/
│   ├── PROJECT_STATUS.md                 本文件
│   ├── TRANSLATION_STYLE.md              翻译规范
│   ├── TERMS.md / TERMS_SOURCES.md       术语表 + 核实记录
│   ├── manifest/<archive>.json           每 archive 的页面清单
│   ├── blog_sources.json                 博客源配置
│   ├── blog_index/<source>.json          每源的文章清单
│   ├── wwdc_shortlist.json               178 场短名单
│   ├── archive_gap.json                  项目 1 的 1,098 条缺口清单
│   ├── assets.json                       图片 URL → 本地路径
│   └── recon/*.md                        六份侦察报告，3,853 行
└── tools/
    ├── paths.py        路径规范化，fetch 与 render 共用（必须一致）
    ├── fetch.py        Apple 文档三阶段抓取
    ├── render.py       DocC JSON → Markdown
    ├── fetch_assets.py 图片下载
    ├── wwdc.py         WWDC 抓取 + 渲染
    ├── blog.py         博客 probe/discover/fetch/render
    ├── html2md.py      HTML → Markdown，代码块逐字节保真
    └── validate.py     译文机械校验（13 类错误，已测零漏检）
```

## 五、进度数字

| 来源 | 抓取 | 渲染 |
|---|---|---|
| Apple 文档 | 68,906 / 96,463 页（进行中，1.6 GB） | 285 篇长文（uikit） |
| WWDC | **178 / 178 场完成** | **178 篇，5.3 MB，16,900 段逐字稿** |
| 博客 | **17 个源全部完成** | **1,736 篇，23 MB** |
| 图片 | 178 项 / 40 MB | — |

全部 34 个 archive 合计 **96,463 页**，其中**成篇文章 3,962 篇**（这才是翻译工作量）。

Apple 文档抓取全程只有 **3 个 403**（`os` archive 里三个含特殊字符的 URL），无限速迹象。

### 博客归档逐源明细（1,736 篇）

| 源 | 篇数 | 中位字数 | 代码率 | 语言 |
|---|---:|---:|---:|---|
| oleb | 307 | 5,399 | 38% | en |
| mikeash | 305 | 11,033 | 64% | en |
| cocoawithlove | 206 | 10,524 | 86% | en |
| belkadan | 177 | 3,904 | 32% | en |
| onevcat | 176 | 6,402 | 57% | zh |
| objccn | 149 | 9,162 | 70% | zh |
| yulingtianxia | 114 | 6,953 | 90% | zh |
| dirtmelon / sunnyxx | 50 / 50 | 5,830 / 4,272 | 74% / 90% | zh |
| lowlevelbits | 39 | 8,215 | 79% | en |
| worthdoingbadly | 35 | 13,493 | 94% | en |
| ibireme | 40 | 1,639 | 25% | zh |
| sealiesoftware | 29 | 4,497 | 28% | en |
| saagarjha | 20 | 10,738 | 70% | en |
| leichunfeng | 16 | 10,426 | 94% | zh |
| alwaysprocessing | 13 | 13,753 | 85% | en |
| maskray | 10 | 15,555 | 90% | en |

体检办法：`中位字数` 和 `代码率` 是发现静默失败的主要手段。**渲染报告说"成功 N 篇零失败"完全不能证明内容没丢** —— sealiesoftware 曾报告成功 29 篇，实际每篇只有 23 行、正文全丢。

## 六、已踩过的坑（都已修，别再犯）

1. **引用 URL 大小写不一致**：索引端点给全小写，页面内 references 有 21%（3,899 处）带大写。macOS 大小写不敏感所以本地看不出，一推 GitHub/Linux 链接全断。`paths.safe_rel()` 统一小写解决。
2. **7,018 个路径含冒号**（Swift 方法签名 `init(a:b:)`），Windows 非法，会导致 checkout 失败。替换成 `_`。
3. **单个文件名超 255 字节**：AVFoundation 有个初始化方法百分号编码后超 400 字节，直接 OSError 掀翻整批。`paths._fit()` 截断拼哈希解决。**抓取要能容忍单页失败**，否则跑一小时被一个边缘 case 掀翻。
4. **块之间缺空行**：相邻段落会被 Markdown 合并成一段。所有块用空行连接。
5. **图片相对路径漏算目录层级**：md 在 `apple-docs/en/` 下、`attachments/` 在仓库根，算 relpath 时必须带上前缀，否则 195 个图片链接全断。
6. **通用抽取器会毁代码**：trafilatura 对 mikeash/alwaysprocessing **抹平全部缩进**，对 ibireme **整个丢失 15 个代码块**、标题抽成「163 评论」。所以自己写了 `html2md.py`，`<pre>` 一律 `text_content()` 原样输出。
7. **WordPress Crayon 插件**把代码打散进上千个 span，但原文完整存在 `textarea.crayon-plain` 里 —— 那才是干净的源。
8. **RSS/Atom feed 普遍被截断**：onevcat 的 feed 只给 **5 篇**，sitemap 有 **498 篇**；mikeash 的 feed 只有摘要+20 条。**归档一律优先 sitemap 或全量索引页，不要信 feed。**
9. **sitemap 条数 ≠ 文章数**：lowlevelbits 的 sitemap 有 242 条，其中 **202 条是 `/tags/` 和 `/categories/` 标签页**，真文章只有 40 篇。所以每个源都要配 `exclude` 正则，否则统计虚高、还会渲染出一堆空壳。
10. **自动猜正文容器的阈值不能定高**：原本要求容器 >800 字，导致 onevcat 大量三五百字的短文匹配不到容器、**静默丢失 349 篇**。降到 200 字后恢复。
11. **Hexo/Jekyll/Rouge 的「行号表格」式高亮**（中文技术博客里占主流）：结构是 `<td class="rouge-gutter"><pre>1\n2\n3…</pre></td><td class="rouge-code"><pre>真代码</pre></td>`。直接找 `<pre>` 会取到**行号那一格**，真代码全丢。onevcat 因此一度 176 篇里只有 3 篇有代码，修完变成 101 篇。
12. **修第 11 条时踩的反向坑**：`highlight_code()` 用 `.//` 在整棵子树里找代码单元格，会命中**外层文章容器**（它子树里恰好有个高亮表格），于是整篇正文被换成一个代码块。表现是 maskray 中位字数从 15,626 掉到 573、sunnyxx 从 4,307 掉到 318。已加比例守卫：只有该元素**几乎只含这段代码**（占比 >90%）才当代码块。
13. **XML 声明**：有些老站页首是 `<?xml version=… encoding=…?>`，`lxml.html.fromstring` 对 str 输入会直接抛 `ValueError`。要先剥掉声明。
14. **同名文章会静默互相覆盖**：各期的「话题」页标题相同，slug 撞名，后写的把前一篇覆盖掉（表现是"写出 29 篇"但目录里只有 27 个文件）。已改成撞名拼 URL 哈希。
9. **`library.json` 是非标准 JSON**（含尾随逗号），要先 `re.sub(r",(\s*[}\]])", r"\1", raw)` 才能解析。
10. **Apple 归档区的 404 页有 82,981 字节**，比大多数真实页面还大；裸目录 URL 返回 1,610 字节空壳而补 `_index.html` 返回 30,256 字节正文，**两者状态码都是 200**。项目 1 抓取必须双重校验：`status==200` 且含 `<article id="contents"`。

## 七、版权边界（重要）

- **Apple 文档**：用户已知悉风险并选择自行承担
- **WWDC 逐字稿**：Apple 版权，同上
- **第三方博客**：逐源不同，已记在 `meta/blog_sources.json` 每条的 `license` 字段
  - ✅ **可公开**：`onevcat`（CC BY 4.0，须署名+原文链接）、`saagarjha`（CC BY-SA 4.0，**译文作为衍生作品也必须以 BY-SA 发布**）
  - ⛔ **明确保留所有权利**：`cocoawithlove`、`kean`、`fatbobman`
  - ⚠️ **未声明**（法律上默认全部保留，不等于可转载）：其余大部分
- **按 robots.txt 明确排除、不抓取**：`massicotte.org`、`casatwy.com` —— 这两站在 `User-agent: *` 放开的同时**单独点名 Disallow ClaudeBot / anthropic-ai / GPTBot / CCBot**。`blog.py` 里内置了运行时检查，会跳过它们。只能人工按需存单页。
- **Apple 开源代码**：APSL 2.0 要求「每份分发附全文许可证 + 不删文件头声明」。**笔记一律写在 `notes/`，源码目录保持逐字节原样**，永远停在 §2.1「unmodified copies」，避免触发 §2.2 的「标注改动 + 12 个月内公开修改后源码」义务。
- **forums.swift.org**：内容零开放许可，版权归各发帖人。可为个人学习抓进私有仓库，**绝不能公开**。

**这个仓库必须保持私有。**

## 八、已知缺口 / 待办

1. **仓库还没建、没推**（等名字）
2. Apple 文档剩余 archive 抓完后：全量渲染 → 生成 `_indexes/` → README 统计
3. 博客抓完后渲染；`maskray` 只拿到 10 篇（archives 页按年分页，需再改配置），优先级低
4. 翻译尚未开始。流程已就绪：译者 agent（Sonnet）→ 独立审校 agent（Opus）→ `validate.py` → 每批抽 3 篇给用户
5. Apple 开源仓库（objc4/dyld/CF 等，约 72–84 MB）尚未 clone。**`CF` 已冻结在 2021-10，Apple 之后不再公开源码，是消失风险最高的一个，建议优先**
6. Swift Evolution（565 份提案）、swift-book、SwiftGG 中文版、老司机周报等 git 源尚未 clone
7. 项目 1 的抓取器尚未写。格式规范已完全逆向（见 `meta/recon/VAULT_FORMAT_SPEC.md`，含文件名 sanitize 算法、base32 锚点算法、链接 quote 规则、frontmatter 的 `yaml.safe_dump(width=80)` 折行行为），但要等旧仓库那个翻译进程结束
8. 项目 1 里约 106 份文档已被 Apple 301 迁到现行文档站，归档 HTML 不存在，需单独立项走 DocC JSON
