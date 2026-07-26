# Apple WWDC Session 视频页面侦察报告

- 侦察日期：2026-07-26
- 总请求数：**约 61 个**（预算 120，未超）；请求间隔 1–2 秒
- 产出：本报告 + `wwdc_sessions.json`（1841 条全量清单）+ `wwdc_shortlist.json`（178 条推荐短名单）
- 所有结论均基于实际访问过的页面；未验证的地方已明确标注为「未验证 / 推断」

---

## 1. 全量清单从哪来

### 1.1 结论：唯一且最佳的来源是 `/videos/all-videos/`

| 候选来源 | 实测结果 |
|---|---|
| `https://developer.apple.com/videos/all-videos/` | **HTTP 200，4,617,499 字节，服务端渲染全量卡片** ← 最佳 |
| `https://developer.apple.com/videos/` | HTTP 200，160KB，只是首页精选，不全 |
| `https://developer.apple.com/videos/wwdc2018/` 等年份页 | HTTP 200，内容与 all-videos 中该年份的子集**完全一致** |
| `https://developer.apple.com/sitemap.xml` | **404**（返回 Page Not Found 的 HTML） |
| `https://developer.apple.com/videos/sitemap.xml` | **404** |
| `/videos/data/all-videos.json`、`/videos/data/videos.json`、`/videos/play/wwdc2020/10163/data.json`、`/videos/data/play/wwdc2020/10163.json` | **全部 404**。文档站那套 `/tutorials/data/*.json` 模式在 `/videos/` 下**不存在**，视频站是传统服务端渲染，不是 SPA |

**没有任何 JSON API。** 抓 `all-videos` 这一个页面就能拿到全量清单，这是 1 个请求换 1841 条记录，性价比极高。

### 1.2 robots.txt 对 `/videos/` 的规定

`https://developer.apple.com/robots.txt`（HTTP 200，368 字节）全文的 Disallow 只有：

```
User-agent: *
Disallow: /click/
Disallow: /cgi-bin/
Disallow: /survey/
Disallow: /temp/
Disallow: /search/
Disallow: /unsubscribe/
Disallow: /reference/
（以下为 /forums/ 的若干条）
```

**`/videos/` 未被禁止，也没有 `Crawl-delay` 指令。** 抓取在 robots 层面是允许的。

### 1.3 all-videos 卡片的 HTML 结构（每条记录的字段全在这里）

以 `wwdc2020/10163` 为例，实际摘录（缩进已压缩）：

```html
<a href="/videos/play/wwdc2020/10163/" class="vc-card tile ..."
   data-released="true" data-category="developer-tools">
  <img class="vc-card__image" width="250"
       src="https://devimages-cdn.apple.com/wwdc-services/images/49/3606/3606_wide_250x141_2x.jpg"
       alt="Advancements in the Objective-C runtime" loading="lazy">
  <span class="vc-card__duration">23:05</span>
  <h5 class="vc-card__title">Advancements in the Objective-C runtime</h5>
  <span class="vc-card__tag vc-card__tag--event">WWDC20</span>
  <span class="vc-card__keywords hidden"
    data-filter-title="advancements in the objective-c runtime"
    data-filter-description="dive into the microscopic world of low-level bits and bytes ..."
    data-filter-title-en="..." data-filter-description-en="..."
    data-filter-keywords=""
    data-filter-collectionid="wwdc20"
    data-filter-subtitle="english|japanese|simplified chinese"
    data-filter-platform="ios|ipados|macos|tvos|watchos"
    data-filter-topics="Developer Tools">
  </span>
</a>
```

一个卡片就直接给出：**URL、标题、时长、年份/系列、摘要全文、官方 topic 标签、支持平台、字幕语言列表、是否已发布**。不需要访问单页就能建索引。

### 1.4 一共多少个 session、覆盖哪些年份

**1841 条卡片，其中 1560 条是真实有视频的 session。**

剩余 281 条 `data-released="false"`（同时无 `vc-card__duration`）——实测全是 WWDC22/23 数字休息室的占位条目，标题形如 `Q&A: Metal`、`Meet the Presenter: Analyze hangs with Instruments`，**没有视频也没有逐字稿**，抓取时必须按 `data-released` 过滤掉。

| 系列 | 卡片总数 | 其中已发布（可归档） |
|---|---|---|
| wwdc2014 | 6 | 6 |
| wwdc2015 | 11 | 11 |
| wwdc2016 | 17 | 16 |
| wwdc2017 | 36 | 36 |
| wwdc2018 | 38 | 38 |
| wwdc2019 | 159 | 153 |
| wwdc2020 | 209 | 209 |
| wwdc2021 | 202 | 202 |
| wwdc2022 | 316 | 184 |
| wwdc2023 | 316 | 181 |
| wwdc2024 | 123 | 123 |
| wwdc2025 | 122 | 122 |
| wwdc2026 | 138 | 138 |
| tech-talks | 96 | 96 |
| meet-with-apple | 52 | 45 |
| **合计** | **1841** | **1560** |

已发布视频总时长 **38,110 分钟 ≈ 635 小时**。

### 1.5 重要发现：2013 年及更早的 session 已被 Apple 彻底下架，2014–2018 被大幅裁剪

- `https://developer.apple.com/videos/wwdc2013/` 返回 **HTTP 200**（`<title>WWDC13 - Videos - Apple Developer`），但页面内 **`/videos/play/` 链接数为 0** —— 是个空壳页。
- 直接访问历史 URL 全部 **302 重定向**（实测 10 个，全部 302、`size_download=0`）：
  `wwdc2013/404`、`wwdc2013/712`、`wwdc2012/406`、`wwdc2018/402`、`wwdc2018/409`、`wwdc2018/413`、`wwdc2016/406`、`wwdc2015/409`、`wwdc2014/416`、`wwdc2017/413`
- 也就是说 WWDC2018 当年一百多场只剩 **38** 场；WWDC2014 只剩 **6** 场（且全是 Metal/Design）。
- **推论（未验证具体范围）**：Apple 会持续下架老 session。经典课如 "Advanced Graphics and Animations for iOS Apps"（2014/419）、"Building Concurrent User Interfaces"（2012）、早年的 ObjC runtime 场次**已经不可能从官方拿到了**。这是最紧迫的归档理由。

### 1.6 URL 规律与 ID 编号规律

URL 形式统一：`https://developer.apple.com/videos/play/{collection}/{id}/`
`collection` ∈ {`wwdc2014`…`wwdc2026`, `tech-talks`, `meet-with-apple`}。注意是 `wwdc2020` 四位年份，但卡片里的 `data-filter-collectionid` 是 `wwdc20` 两位，两者不通用。

ID 位数实测分布：

| collection | ID 位数分布 |
|---|---|
| wwdc2014–2019 | 全部 3 位（`415`、`423`） |
| wwdc2020 | 5 位 207 个（`10163`），3 位 2 个 |
| wwdc2021 | 5 位 195，3 位 6，6 位 1 |
| wwdc2022 | **6 位 183（`110362`），5 位 127** ← 同一年混用两套 |
| wwdc2023 | 5 位 226，6 位 86 |
| wwdc2024 | 5 位 115，6 位 3，4 位 1，3 位 4 |
| **wwdc2025** | **全部 3 位（`312`）** ← 回归短 ID |
| **wwdc2026** | 3 位 119，4 位 19（`8001` 系列是 Group Lab） |
| tech-talks | 6 位 38、5 位 24、3 位 34（混杂） |
| meet-with-apple | 全部 3 位 |

规律：2014–2019 三位数（首位≈轨道号，4xx=开发工具/Swift，7xx=系统框架，8xx=设计）；2020 起改为全站唯一的 5–6 位内部内容 ID，跟年份无关；**2025 起 Apple 又改回三位数短 ID**。

**结论：ID 无法枚举推测，必须从 all-videos 索引取。** 不要写 for 循环猜 ID。

---

## 2. 单个 session 页面能拿到什么

实测抓取 **23 个 session 页**，跨 2014→2026 全部年份 + tech-talks + meet-with-apple。

### 2.1 逐字稿覆盖：抽样 23/23 全部命中，且全部服务端渲染

| 页面 | HTTP | `class="sentence"` 数 | `<p>` 段落数 | 幻灯片 PDF | 章节 |
|---|---|---|---|---|---|
| wwdc2014/604 Working with Metal: Fundamentals | 200 | 1219 | 265 | ✅ | – |
| wwdc2015/408 Protocol-Oriented Programming | 200 | 808 | 163 | ✅ | – |
| wwdc2016/411 System Trace in Depth | 200 | 931 | – | ✅ | – |
| wwdc2016/416 Understanding Swift Performance | 200 | 1191 | 181 | ✅ | – |
| wwdc2017/706 Modernizing GCD Usage | 200 | 1985 | – | ✅ | – |
| wwdc2018/416 iOS Memory Deep Dive | 200 | 1733 | 228 | ✅ | – |
| wwdc2018/803 Designing Fluid Interfaces | 200 | 2122 | – | ✅ | – |
| wwdc2019/423 Optimizing App Launch | 200 | 1280 | 126 | ✅ | – |
| wwdc2020/10163 Advancements in the ObjC runtime | 200 | 415 | 121 | ❌ | – |
| wwdc2020/10686 Apple silicon 系统架构 | 200 | 371 | – | ❌ | – |
| wwdc2021/10216 ARC in Swift | 200 | 400 | 159 | ❌ | – |
| wwdc2021/10254 Swift concurrency: Behind the scenes | 200 | 767 | – | ❌ | – |
| wwdc2022/110362 Link fast | 200 | 529 | 14 | ❌ | – |
| wwdc2023/10248 Analyze hangs with Instruments | 200 | 757 | 92 | ❌ | 13 |
| wwdc2023/10268 Meet mergeable libraries | 200 | 405 | – | ❌ | 9 |
| wwdc2024/10173 Analyze heap memory | 200 | 659 | 120 | ❌ | 14 |
| wwdc2025/312 Improve memory usage and performance | 200 | 542 | 92 | ❌ | 18 |
| wwdc2026/268 Improve app responsiveness | 200 | 461 | 67 | ❌ | 12 |
| wwdc2026/321 Lazy stacks and scrolling | 200 | 360 | – | ❌ | 12 |
| tech-talks/111374 Metal profiling M3/A17 | 200 | 622 | 136 | ❌ | – |
| tech-talks/10855 UI animation hitches and render loop | 200 | 223 | – | ❌ | – |
| tech-talks/204 iOS Storage Best Practices | 200 | 201 | – | ❌ | – |
| meet-with-apple/206 Memory Integrity Enforcement | 200 | 132 | – | ❌ | 13 |

**没有发现任何年份缺逐字稿。** 2014 年的老 session 与 2026 年的新 session 结构完全一致。

⚠️ 未验证的部分：只抽了 23 个，未逐一验证全部 1560 个。风险点在于时长极短的条目（如 tech-talks/10865 只有 2:34、wwdc2017/250 只有 3:46），以及 `Group Lab` / `Code-along` 这类长直播（60–100 分钟）。这些**未抽样**，建议实抓时把「sentence 数为 0」当作告警而不是当作失败。

### 2.2 逐字稿的 HTML 结构（关键：`sentence` 不是句子，是字幕行）

容器与选择器：

```html
<li class="supplement transcript" data-supplement-id="transcript"
    data-shortcut-base-url="/videos/play/wwdc2025/312/">
  <input type="text" id="transcript-search-box" class="transcript-search ...">
  <div style="font-size:34px" id="get-transcript"><sf-symbol name="arrow.down.document" ...></div>
  <section id="transcript-content">
    <p><span class="sentence"><span data-start="7.0">…</span></span><span class="sentence">…
```

- **选择器**：`#transcript-content` → `p` → `span.sentence` → `span[data-start]`
- **带时间戳**：每个 `span.sentence` 内嵌一个 `<span data-start="秒数">`，精度到 0.1 秒（实测值形如 `13.0`、`421`）
- **能还原段落**：`<p>` 就是段落边界，实测 14–265 段/场（`wwdc2022/110362` 只有 14 段是异常值，段落切得很粗）
- **⚠️ 陷阱**：`span.sentence` 平均只有 **4.6–9.3 个词**，是字幕行而非完整句子。实测 `wwdc2019/423` 的连续 4 个 span 分别断在 `my name is` / `Spencer Lewson, and I'm an` / `engineer on the Performance Team` / `here at Apple.` —— **句子被硬切断了**。
- **正确做法**：先把同一 `<p>` 内所有 `span.sentence` 的文本用空格拼成一整段，再按标点重新分句，然后送翻译。**逐 span 翻译会产出语义破碎的中文。** 时间戳只保留每段的第一个 `data-start` 即可。
- `#get-transcript` 是个纯 JS 下载按钮（无 `href`），**没有对应的服务端逐字稿文件接口**，只能解析 HTML。

### 2.3 能拿到的元数据

**页面上（`li.supplement.details`）**：`<h1>` 标题 + 摘要段落，以及 `<input id="analytics-meta">` 这个隐藏元素，字段非常干净：

```html
<input id="analytics-meta" type="hidden" data-event-name="WWDC18"
       data-event-id="wwdc2018-416" data-session-id="416"
       data-video-name="iOS Memory Deep Dive" data-session-response-id="">
```

还有面包屑给出系列名：`<a href="/videos/wwdc2018/">WWDC18</a>`。

**从索引页（推荐走这条）**：标题、年份、时长、英文摘要全文、官方 topic 标签、平台列表、字幕语言列表。索引比单页更全（单页上没有 topic 标签和平台）。

**相关 session 链接**：以 `href="/videos/play/..."` 形式出现在 details 区。实测数量 0–5 个（`wwdc2014/604` 和 `wwdc2019/423` 是 0 个，`wwdc2018/416` 有 4 个指向 2018/412、2018/414、2023/10100）。
⚠️ 2024 年后同一页里还混入大量 `?time=` 形式的自跳转链接（`wwdc2024/10173` 有 42 个「相关链接」，其中绝大多数是章节跳转），**解析时必须排除带 `?time=` 的和指向自身的**。

### 2.4 Resources 区里有什么

supplement 容器共 4 种，实测：`details`、`transcript`、`sample-code`、`summary`（`summary` 只在 2024+ 出现）。

- **幻灯片 PDF**：只在 **2014–2019** 存在，形式为
  `<li class="download"><a href="https://devstreaming-cdn.apple.com/videos/wwdc/2019/423lzf3qsjedrzivc7/423/423_optimizing_app_launch.pdf?dl=1">Presentation Slides (PDF)</a></li>`
  URL 规律：`.../videos/wwdc/{年}/{id}{随机串}/{id}/{id}_{slug}.pdf?dl=1`，**中间那段随机串无法推测，必须从页面里取**。
  实测 **2020/10163、2021/10216、2022/110362、2023、2024、2025、2026 全部为 0 个 PDF** —— Apple 从 WWDC20 起不再提供幻灯片。
- **示例代码**：`li.supplement.sample-code`。2018 及以前实测**是空的**（`<ul>` 里无内容）；2025 里是内联代码块，带跳转时间和语法高亮：
  ```html
  <li class="sample-code-main-container">
    <button class="btn-copy-code" ...>Copy Code</button>
    <p>7:01 - <a class="jump-to-time-sample" href="/videos/play/wwdc2025/312/?time=421"
        data-start-time="421">Corrected Data.readByte() method</a></p>
    <pre class="code-source"><code><span class="syntax-keyword">import</span> Foundation …
  ```
  **这块很值得存**：它是演讲里出现过的代码，比逐字稿里念的代码可靠得多。
- **相关文档链接**：页面上 `href="/documentation/..."` 的计数在所有 23 个页面上恒为 **18** —— 说明这 18 个是全站导航里的，**不是 session 专属资源**。真正的 session 相关文档链接需要限定在 details 区内解析。
- **视频文件**：每页恒定给出 sd/hd 两个 mp4 + 一个 m3u8：
  - 老格式（2018）：`.../videos/wwdc/2018/416n2fmzz0fz88f/416/416_hd_ios_memory_deep_dive.mp4` 与 `hls_vod_mvp.m3u8`
  - 新格式（2025）：`.../videos/wwdc/2025/312/4/{uuid}/downloads/wwdc2025-312_hd.mp4` 与 `cmaf.m3u8`

### 2.5 章节 / 大纲

**2023 起才有，2022 及更早没有。** 实测：2022/110362 = 0 章节；2023/10248 = 13；2023/10268 = 9；2024/10173 = 14；2025/312 = 18；2026/268 = 12；2026/321 = 12。

结构在 `li.supplement.summary` 里，而且**每章还附带一段 Apple 自己写的章节摘要**，质量很高：

```html
<li class="supplement summary margin-top-small" data-supplement-id="summary">
 <li>0:00 - <a class="jump-to-time" href="/videos/play/wwdc2025/312/?time=0"
     data-start-time="0" data-chapter-end-time="79" data-chapter-lenght="79"
     data-chapter-index="1">Introduction &amp; Agenda</a></li>
 <li class="chapter-summary"><p>Learn about optimizing performance of Swift code …</p></li>
```

（注意 Apple 自己把属性拼错成 `data-chapter-lenght`，解析时别写成 `length`。）

**建议**：把章节标题 + 章节摘要一起归档，它们是天然的中文翻译切分单元，也是最好的目录。

### 2.6 老 session（2014–2016）与新 session 的结构差异

**逐字稿部分完全一致**，同一套 `#transcript-content` / `p` / `span.sentence` / `data-start`。差异只在周边：

| 维度 | 2014–2019 | 2020–2022 | 2023–2026 |
|---|---|---|---|
| 逐字稿结构 | 相同 | 相同 | 相同 |
| 幻灯片 PDF | ✅ 有 | ❌ 无 | ❌ 无 |
| 章节 / 章节摘要 | ❌ 无 | ❌ 无 | ✅ 有 |
| 内联示例代码 | 空 | 部分有 | ✅ 有 |
| mp4 URL 格式 | `{id}{hash}/{id}/{id}_{slug}.mp4` | 过渡 | `{year}/{id}/{n}/{uuid}/downloads/wwdc{year}-{id}_hd.mp4` |
| 简体中文字幕 | 2015 起有，2014 无 | ✅ | ✅ |

**一套解析器可以吃下所有年份**，只需把 PDF / 章节 / 示例代码当作可选字段。

---

## 3. 按主题筛选建议

### 3.1 Apple 官方的 topic 标签体系（能直接用来筛，但粒度太粗）

从 all-videos 的筛选器 `<filter-checkbox ... data-filter-topic-value="...">` 抽出的**完整 19 类**：

Accessibility & Inclusion / AI & Machine Learning / App Services / App Store, Distribution & Marketing / Audio & Video / Business & Education / Design / **Developer Tools** / Essentials / Graphics & Games / Health & Fitness / Maps & Location / Photos & Camera / Privacy & Security / Safari & Web / Spatial Computing / **Swift** / **SwiftUI & UI Frameworks** / **System Services**

覆盖率 100%（1841/1841 条都有 topic），一条 session 可有多个 topic。数量分布：SwiftUI & UI Frameworks 374、Developer Tools 282、App Services 234、Graphics & Games 229、Essentials 199、…、Maps & Location 33。

**能否直接用它筛？——只能用来做粗筛，不能直接定名单。** 理由（实测）：

1. `Advancements in the Objective-C runtime` 的 topic 只有 `Developer Tools`，**没有 Swift**。ObjC runtime 这种纯底层内容被塞进「开发者工具」，标签体系里根本没有「runtime / 内存 / 并发 / 编译链接」这些维度。
2. 用户关心的 9 个底层主题，映射到官方标签就只剩 `Developer Tools` + `Swift` + `System Services` 三类，一共 **453 场**已发布 session —— 而这 453 场里混着 Xcode Cloud、App Store Connect、CloudKit Console、DocC、Swift Playgrounds、Game Center、CarPlay 等大量无关内容。
3. 反过来还会漏：`Designing Fluid Interfaces`（交互物理）topic 是 `Design`，`Profile and optimize your game's memory`（内存剖析）topic 是 `Graphics & Games`，都在三类之外。

**推荐做法**：用 `Developer Tools ∪ Swift ∪ System Services`（453 场）+ 从 `SwiftUI & UI Frameworks / Graphics & Games / Design` 里按标题关键词补捞（另约 105 场候选），再人工过一遍。本报告的短名单就是这么产出的。

### 3.2 推荐归档短名单：**178 场**（结构化数据见 `wwdc_shortlist.json`）

- 全部 178 个 ID **已逐一对照官方索引校验存在**（校验脚本输出 `MISSING: []`），没有一个是凭记忆猜的
- 总时长 **88 小时 26 分**
- 年份跨度 2015–2026（2014 年仅存的 6 场全是 Metal/Design，无一条符合底层主题，故未入选）
- **164/178 已有 Apple 官方简体中文字幕**
- 56/178 附带幻灯片 PDF（即 2019 及更早的）
- ★ = **讲底层原理、多年后依然有效**（122 场）；☆ = 讲某版本新 API、会过时（56 场）

分组统计：A-runtime 35 / B-内存 8 / C-并发 19 / D-响应性 11 / E-UI渲染 23 / F-链接启动 19 / G-调试 27 / H-持久化 20 / I-系统底层 16。

以下按主题列出，`理由`一列一句话说明为什么值得归档。完整机器可读版（含 URL、topics、duration、字幕语言）在 `wwdc_shortlist.json`。

#### A · ObjC/Swift runtime 与语言实现（35 场）

| | Session | 年 | URL 尾段 | 理由 |
|---|---|---|---|---|
|★|Advancements in the Objective-C runtime|2020|`wwdc2020/10163`|ObjC runtime 内部数据结构、method list、tagged pointer 的权威一手材料|
|★|Understanding Swift Performance|2016|`wwdc2016/416`|值/引用类型、witness table、动态派发的成本模型，至今必读|
|★|Explore Swift performance|2024|`wwdc2024/10217`|上一条的现代重写版：内存布局、派发、特化|
|★|Improve memory usage and performance with Swift|2025|`wwdc2025/312`|InlineArray/Span，去分配与去引用计数的新范式|
|★|ARC in Swift: Basics and beyond|2021|`wwdc2021/10216`|ARC 插入规则、生命周期与 withExtendedLifetime|
|★|Refine Objective-C frameworks for Swift|2020|`wwdc2020/10680`|ObjC 头文件如何被 Swift 导入，桥接层规则|
|★|Swift and Objective-C Interoperability|2015|`wwdc2015/401`|互操作与桥接的底层规则|
|★|Protocol-Oriented Programming in Swift|2015|`wwdc2015/408`|POP 原始出处，理解 existential 与 witness table|
|★|Protocol and Value Oriented Programming in UIKit Apps|2016|`wwdc2016/419`|把 POP 落到 UIKit，值语义实践|
|★|Swift Generics (Expanded)|2018|`wwdc2018/406`|泛型实现原理与特化|
|★|Embrace Swift generics|2022|`wwdc2022/110352`|any/some 的现代表述|
|★|Design protocol interfaces in Swift|2022|`wwdc2022/110353`|primary associated type|
|★|Safely manage pointers in Swift|2020|`wwdc2020/10167`|Swift 指针语义、内存绑定规则|
|★|Unsafe Swift|2020|`wwdc2020/10648`|Unsafe API 全景，未定义行为边界|
|★|Consume noncopyable types in Swift|2024|`wwdc2024/10170`|noncopyable 与所有权模型|
|★|Embrace Swift type inference|2020|`wwdc2020/10165`|类型推断如何工作、为何编译慢|
|★|Embracing Algorithms|2018|`wwdc2018/223`|算法与集合抽象的思维方式|
|★|Modern Swift API Design|2019|`wwdc2019/415`|读源码时的判断依据|
|★|Go small with Embedded Swift|2024|`wwdc2024/10197`|无 runtime 的 Swift 子集，反向理解 runtime 依赖|
|★|Safely mix C, C++, and Swift|2025|`wwdc2025/311`|混编的 ABI 与内存安全边界|
|★|Mix Swift and C++|2023|`wwdc2023/10172`|Swift/C++ 互操作模型|
|★|Binary Frameworks in Swift|2019|`wwdc2019/416`|module interface 与 ABI 稳定|
|☆|Generalize APIs with parameter packs|2023|`wwdc2023/10168`|变参泛型|
|☆|Write Swift macros / Expand on Swift macros|2023|`wwdc2023/10166`、`10167`|宏的展开机制（编译期代码生成）|
|☆|Distribute binary frameworks as Swift packages|2020|`wwdc2020/10147`|XCFramework 分发|
|☆|What's New in Swift ×9|2018–2026|`wwdc2018/401`、`wwdc2019/402`、`wwdc2020/10170`、`wwdc2021/10192`、`wwdc2022/110354`、`wwdc2023/10164`、`wwdc2024/10136`、`wwdc2025/245`、`wwdc2026/262`|版本时间线索引，单看会过时，成套看能看清语言演进|

#### B · 内存管理与内存性能（8 场）

| | Session | 年 | URL 尾段 | 理由 |
|---|---|---|---|---|
|★|iOS Memory Deep Dive|2018|`wwdc2018/416`|内存足迹、脏内存/压缩内存、图片解码真实成本，经典|
|★|Detect and diagnose memory issues|2021|`wwdc2021/10180`|Memory Graph、泄漏与循环引用的系统诊断法|
|★|Analyze heap memory|2024|`wwdc2024/10173`|堆内存分析的现代工具链与判读方法|
|★|Profile and optimize your game's memory|2022|`wwdc2022/10106`|讲到分配器与常驻内存|
|★|Secure your app with Memory Integrity Enforcement|—|`meet-with-apple/206`|内存完整性强制，硬件级内存安全，新知识|
|★|Improve app size and runtime performance|2022|`wwdc2022/110363`|包体积与运行时性能取舍（含 ObjC/Swift 元数据成本）|
|★|Optimizing Storage in Your App|2019|`wwdc2019/419`|存储占用与缓存/清理策略|
|★|Optimizing App Assets|2018|`wwdc2018/227`|资源与图片资产的内存/体积成本|

#### C · 并发、锁与线程（19 场）

| | Session | 年 | URL 尾段 | 理由 |
|---|---|---|---|---|
|★|**Swift concurrency: Behind the scenes**|2021|`wwdc2021/10254`|**本组最重要**：协作线程池、continuation、如何避免线程爆炸|
|★|Modernizing Grand Central Dispatch Usage|2017|`wwdc2017/706`|QoS、优先级反转、队列层次——GCD 最深的一场|
|★|Concurrent Programming With GCD in Swift 3|2016|`wwdc2016/720`|队列模型、线程爆炸与同步原语，理解调度的起点|
|★|Meet async/await in Swift|2021|`wwdc2021/10132`|async/await 语义与挂起点|
|★|Protect mutable state with Swift actors|2021|`wwdc2021/10133`|actor 隔离与可重入，锁的替代方案|
|★|Explore structured concurrency in Swift|2021|`wwdc2021/10134`|任务树与取消传播|
|★|Eliminate data races using Swift Concurrency|2022|`wwdc2022/110351`|Sendable 与数据竞争的静态消除模型|
|★|Visualize and optimize Swift concurrency|2022|`wwdc2022/110350`|用 Instruments 看并发运行时的实际调度|
|★|Beyond the basics of structured concurrency|2023|`wwdc2023/10170`|任务组、优先级、取消的进阶语义|
|★|Migrate your app to Swift 6|2024|`wwdc2024/10169`|严格并发迁移路径与隔离模型|
|★|Embracing Swift concurrency|2025|`wwdc2025/268`|并发心智模型的最新统一表述|
|★|Bring Core Data concurrency to Swift and SwiftUI|2021|`wwdc2021/10017`|Core Data 的并发上下文模型|
|☆|Meet AsyncSequence / Swift concurrency: Update a sample app / Meet Swift Async Algorithms|2021–22|`wwdc2021/10058`、`wwdc2021/10194`、`wwdc2022/110355`|库与实战，价值次一级|
|☆|Explore / Discover concurrency in SwiftUI|2025/2021|`wwdc2025/266`、`wwdc2021/10019`|SwiftUI 侧的主 actor 行为|
|☆|Use structured concurrency with Network framework|2025|`wwdc2025/250`|Network 框架的并发用法|
|☆|Swift Group Lab|2026|`wwdc2026/8001`|实验室问答，含并发疑难|

#### D · 响应性、hang/hitch 与渲染循环（RunLoop 的现代替身，11 场）

> **重要**：Apple **没有任何一场专门讲 RunLoop 的现存 session**（用 `run loop`/`runloop` 在 1560 场标题里搜不到）。最接近的是下面这套 Tech Talks 三部曲，讲的是「渲染循环」各阶段与主线程时序，这是官方对 RunLoop/CADisplayLink 那一层最实质的公开讲解。

| | Session | 年 | URL 尾段 | 理由 |
|---|---|---|---|---|
|★|**Explore UI animation hitches and the render loop**|—|`tech-talks/10855`|**最接近 RunLoop 的一场**：渲染循环各阶段与 hitch 定义|
|★|Find and fix hitches in the commit phase|—|`tech-talks/10856`|commit 阶段（布局/绘制/提交）卡顿成因|
|★|Demystify and eliminate hitches in the render phase|—|`tech-talks/10857`|render 阶段（GPU 合成）卡顿成因|
|★|Understand and eliminate hangs from your app|2021|`wwdc2021/10258`|hang 分类、主线程阻塞源与消除|
|★|Analyze hangs with Instruments|2023|`wwdc2023/10248`|逐帧定位 hang，方法论极强|
|★|Track down hangs with Xcode and on-device detection|2022|`wwdc2022/10082`|设备端 hang 检测|
|★|Eliminate animation hitches with XCTest|2020|`wwdc2020/10077`|把动画卡顿变成可回归指标|
|★|Ultimate application performance survival guide|2021|`wwdc2021/10181`|性能问题分类与排查顺序（总纲）|
|★|Practical Approaches to Great App Performance|2018|`wwdc2018/407`|通用方法论，老但不过时|
|★|Optimize for variable refresh rate displays|2021|`wwdc2021/10147`|帧预算与 ProMotion 下的时序|
|☆|Profile, fix, and verify: Improve app responsiveness with Instruments|2026|`wwdc2026/268`|最新工具流程|

#### E · UIKit/SwiftUI 渲染与 UI 性能（23 场）

| | Session | 年 | URL 尾段 | 理由 |
|---|---|---|---|---|
|★|**Demystify SwiftUI**|2021|`wwdc2021/10022`|身份、依赖图与 body 求值时机——框架原理，本组第一读|
|★|Demystify SwiftUI performance|2023|`wwdc2023/10160`|性能因果模型：依赖过宽、结构性身份|
|★|Demystify SwiftUI containers|2024|`wwdc2024/10146`|容器与 ViewBuilder 的展开机制|
|★|Make blazing fast lists and collection views|2021|`wwdc2021/10252`|预取、cell 复用、diffable|
|★|A Tour of UICollectionView|2018|`wwdc2018/225`|UICollectionView 结构与布局体系|
|★|Advances in Collection View Layout|2019|`wwdc2019/215`|Compositional Layout 的布局求值模型|
|★|Advances in UI Data Sources|2019|`wwdc2019/220`|Diffable Data Source 与一致性快照|
|★|Meet TextKit 2|2021|`wwdc2021/10061`|视口化布局，排版性能原理|
|★|TextKit Best Practices|2018|`wwdc2018/221`|TextKit 1 的排版流水线|
|★|Unleash the UIKit trait system|2023|`wwdc2023/10057`|trait 失效/重解析机制|
|★|Explore SwiftUI animation|2023|`wwdc2023/10156`|插值与事务模型|
|★|Animate with springs|2023|`wwdc2023/10158`|弹簧动画物理参数|
|★|Beyond scroll views|2023|`wwdc2023/10159`|滚动视图底层行为与几何|
|★|Dive into lazy stacks and scrolling with SwiftUI|2026|`wwdc2026/321`|惰性栈的按需构建机制|
|★|**Designing Fluid Interfaces**|2018|`wwdc2018/803`|交互物理与响应性哲学，长期有效（虽挂在 Design 下）|
|☆|其余 8 场|2020–2026|`wwdc2020/10026`、`wwdc2020/10097`、`wwdc2021/10021`、`wwdc2022/10090`、`wwdc2023/10055`、`wwdc2025/306`、`wwdc2026/322`、`wwdc2026/370`|年度更新与实操，价值次一级|

#### F · Mach-O / dyld / 编译链接 / 启动优化（19 场）—— **用户学习计划的核心组**

| | Session | 年 | URL 尾段 | 理由 |
|---|---|---|---|---|
|★|Behind the Scenes of the Xcode Build Process|2018|`wwdc2018/415`|构建全流程：编译、链接、任务图（学习计划已选）|
|★|Optimizing App Launch|2019|`wwdc2019/423`|启动阶段拆解：dyld、初始化器、首帧（学习计划已选）|
|★|Link fast: Improve build and launch times|2022|`wwdc2022/110362`|静态链接器与 dyld 现代实现、chained fixups（学习计划已选）|
|★|**Meet mergeable libraries**|2023|`wwdc2023/10268`|动静态库合并链接，dyld 关键演进——**强烈建议补进学习计划**|
|★|Demystify parallelization in Xcode builds|2022|`wwdc2022/110364`|构建并行化与依赖图，构建耗时根因|
|★|Demystify explicitly built modules|2024|`wwdc2024/10171`|显式模块构建，Clang/Swift 模块缓存|
|★|Building Faster in Xcode|2018|`wwdc2018/408`|构建加速与增量编译原理|
|★|What's New in Clang and LLVM|2019|`wwdc2019/409`|编译器视角的年度进展|
|★|**Explore the new system architecture of Apple silicon Macs**|2020|`wwdc2020/10686`|内存/页/指针认证/Rosetta——最接近内核的一场|
|★|Port your Mac app to Apple silicon|2020|`wwdc2020/10214`|Mach-O 通用二进制与架构迁移实际问题|
|★|**Symbolication: Beyond the basics**|2021|`wwdc2021/10211`|dSYM、UUID、地址还原——崩溃分析基础|
|★|Explore advanced project configuration in Xcode|2021|`wwdc2021/10210`|xcconfig、target 依赖，构建系统实操|
|★|Getting to Know Swift Package Manager|2018|`wwdc2018/411`|依赖解析与构建模型|
|★|Verify app dependencies with digital signatures|2023|`wwdc2023/10061`|二进制信任链|
|☆|其余 5 场|2019–2022|`wwdc2019/408`、`wwdc2019/410`、`wwdc2019/703`、`wwdc2020/10114`、`wwdc2022/110359`|SwiftPM / 公证 / 跨架构运行|

#### G · 调试、崩溃与 Instruments（27 场）

| | Session | 年 | URL 尾段 | 理由 |
|---|---|---|---|---|
|★|**System Trace in Depth**|2016|`wwdc2016/411`|系统调用、线程状态、VM 事件——全场最底层的一场|
|★|Advanced Debugging with Xcode and LLDB|2018|`wwdc2018/412`|表达式求值、断点动作，调试能力天花板|
|★|Understanding Crashes and Crash Logs|2018|`wwdc2018/414`|崩溃日志结构、信号与异常类型判读|
|★|Advanced Debugging and the Address Sanitizer|2015|`wwdc2015/413`|ASan 原理（影子内存），内存错误检测底层|
|★|Debug Swift debugging with LLDB|2022|`wwdc2022/110370`|调试信息如何生成与丢失，反射与类型元数据|
|★|What's New in LLDB / LLDB: Beyond "po" / Run, Break, Inspect|2015/2019/2024|`wwdc2015/402`、`wwdc2019/429`、`wwdc2024/10198`|LLDB 机制与现代工作流|
|★|Measuring Performance Using Logging|2018|`wwdc2018/405`|os_log/signpost 的低开销日志原理|
|★|Explore logging in Swift|2020|`wwdc2020/10168`|Swift 日志与隐私修饰符|
|★|Debug with structured logging|2023|`wwdc2023/10226`|结构化日志与调试联动|
|★|Creating Custom Instruments / Modeling in Custom Instruments|2018/2019|`wwdc2018/410`、`wwdc2019/421`|自定义 Instruments 与 signpost 建模|
|★|Optimize CPU performance with Instruments|2025|`wwdc2025/308`|采样、调用树、微架构视角|
|★|Improving Battery Life and Performance|2019|`wwdc2019/417`|电量与性能因果关系，CPU/唤醒/网络成本|
|★|What's new in MetricKit|2020|`wwdc2020/10081`|线上性能与崩溃数据采集|
|★|Detect bugs early with the static analyzer|2021|`wwdc2021/10202`|静态分析器原理与误报判读|
|☆|其余 10 场|2019–2026|`wwdc2019/411`、`wwdc2019/414`、`wwdc2020/10076`、`wwdc2021/10087`、`wwdc2021/10203`、`wwdc2021/10209`、`wwdc2021/10212`、`wwdc2022/10083`、`wwdc2025/226`、`wwdc2026/222`|工具入门与年度更新|

#### H · 持久化与文件系统（20 场）

| | Session | 年 | URL 尾段 | 理由 |
|---|---|---|---|---|
|★|Core Data Best Practices|2018|`wwdc2018/224`|栈结构、上下文与批处理，长期有效|
|★|Core Data: Sundries and maxims|2020|`wwdc2020/10017`|细节与陷阱集合|
|★|Evolve your Core Data schema|2022|`wwdc2022/10120`|轻量/重量迁移机制|
|★|Dive deeper into SwiftData|2023|`wwdc2023/10196`|ModelContext 与持久化后端|
|★|Create a custom data store with SwiftData|2024|`wwdc2024/10138`|自定义后端，看清 SwiftData 抽象层|
|★|Track model changes with SwiftData history|2024|`wwdc2024/10075`|变更历史追踪机制|
|★|**What's New in Apple File Systems**|2019|`wwdc2019/710`|APFS：快照、克隆、空间共享——文件系统底层|
|★|iOS Storage Best Practices|—|`tech-talks/204`|iOS 存储行为与清理机制|
|★|Build robust and resumable file transfers|2023|`wwdc2023/10006`|涉及 URLSession 后台机制|
|★|Data Essentials in SwiftUI|2020|`wwdc2020/10040`|SwiftUI 数据流的所有权模型|
|★|Advances in Foundation / What's new in Foundation|2019/2021|`wwdc2019/723`、`wwdc2021/10109`|Unicode、Data、AttributedString、格式化|
|☆|其余 8 场|2019–2025|`wwdc2019/202`、`wwdc2019/719`、`wwdc2021/10182`、`wwdc2022/10119`、`wwdc2023/10186`、`wwdc2023/10187`、`wwdc2024/10137`、`wwdc2025/291`|年度更新与 CloudKit 集成|

#### I · 系统服务、进程与安全底层（16 场）

| | Session | 年 | URL 尾段 | 理由 |
|---|---|---|---|---|
|★|**Advances in App Background Execution**|2019|`wwdc2019/707`|后台执行模型：任务类型、预算、调度器——系统机制核心|
|★|Introducing Network.framework|2018|`wwdc2018/715`|连接状态机、替代 socket 的设计|
|★|Advances in Networking, Part 1 / Part 2|2019|`wwdc2019/712`、`wwdc2019/713`|TCP/TLS/多路径与协议性能|
|★|Optimizing Your App for Today's Internet|2018|`wwdc2018/714`|连接与延迟的真实成本|
|★|Boost performance and security with modern networking|2020|`wwdc2020/10111`|现代网络 API 的性能与安全默认值|
|★|**System Extensions and DriverKit**|2019|`wwdc2019/702`|用户态驱动与进程隔离|
|★|**Build an Endpoint Security app**|2020|`wwdc2020/10159`|内核事件订阅，系统监控底层|
|★|Using Accelerate and simd|2018|`wwdc2018/701`|向量化与微架构|
|★|Introducing Combine / Combine in Practice|2019|`wwdc2019/722`、`wwdc2019/721`|发布者/订阅者与背压模型|
|★|Finish tasks in the background|2025|`wwdc2025/227`|后台任务的现代 API 与生命周期|
|☆|其余 4 场|2019–2022|`wwdc2019/718`、`wwdc2020/10210`、`wwdc2020/10217`、`wwdc2022/10142`|Accelerate/DriverKit/后台任务的次级材料|

### 3.3 「长期有效」vs「很快过时」的判定标准

打 ★（122 场）的判据是**内容讲的是机制而非 API 表面**：

- **一定要存**：runtime 数据结构、ARC 插入规则、GCD/Swift 并发运行时实现、dyld 与链接器、Mach-O/符号化、内存足迹与页管理、APFS、SwiftUI 依赖图、渲染循环阶段、ASan/System Trace 原理。这些十年内不会失效，而且 Apple 已经证明它会下架老视频。
- **可以后置**：所有 `What's new in X`、`Meet X`、`What's new in Xcode NN`、Xcode Cloud/DocC/TestFlight/App Store Connect 相关。成套归档有价值（能看出演进），单看很快过时。
- **明确排除**：Design 类（除 `Designing Fluid Interfaces`）、Spatial Computing、AI/ML、Game Center、CarPlay、Health、App Store 营销、Safari/Web、Accessibility（除非专门想学）。

### 3.4 对用户学习计划的建议

原计划 4 场（2018/415、2019/423、2020/10163、2022/110362）都在短名单里，主题集中在 F 组和 A 组。建议**至少补 5 场**再开始：

1. `wwdc2023/10268` Meet mergeable libraries —— 和 110362 是同一条链的下一环，不补会断
2. `wwdc2021/10211` Symbolication: Beyond the basics —— 没有它，dyld/Mach-O 学完也读不懂崩溃日志
3. `wwdc2018/416` iOS Memory Deep Dive —— 内存主题的地基
4. `wwdc2021/10254` Swift concurrency: Behind the scenes —— 并发主题唯一讲实现的一场
5. `wwdc2016/411` System Trace in Depth —— 全站最底层，看系统调用与线程状态

---

## 4. 工作量与风险

### 4.1 数据量估算（基于 13 个页面的实测文本量）

实测 13 场逐字稿：76,284 词 / 433,399 字符，**平均 5,868 词、约 32 KB 纯文本/场**。

| 项目 | 178 场短名单 | 全量 1560 场 |
|---|---|---|
| 逐字稿纯文本 | **约 5.6 MB** | 约 49 MB |
| 原始 HTML（若一并留档，平均 210 KB/场） | 约 37 MB | 约 320 MB |
| 加上中文译文（中文约为英文的 0.7–0.9 倍字节，UTF-8 汉字 3 字节 → 体积接近） | 再 +约 6 MB | 再 +约 50 MB |
| 幻灯片 PDF（56 场有，实测 0.9/2.6/2.7/4.8/9.6 MB，均值约 4 MB） | **约 220 MB** | 约 1.0 GB（约 260 场有 PDF） |
| 视频 mp4 | 不建议存（单场 HD 数百 MB～1 GB+） | 不可行 |

**结论：只存逐字稿 + 元数据 + 章节，178 场约 6 MB，纯文本仓库，Git 完全扛得住。** 请求数 178 个（每场 1 个请求），按 2 秒间隔约 6 分钟跑完。

### 4.2 反爬与限速：实测无

- 61 个请求全程无 429、无验证码、无 IP 封禁、无 Cloudflare 挑战
- **无需 User-Agent**：不带 UA 的裸 curl 访问 `wwdc2018/415` 同样返回 **HTTP 200**
- 响应头（`wwdc2018/415`）：
  ```
  HTTP/1.1 200 OK
  Server: Apple
  Cache-Control: max-age=300, public
  Via: https/1.1 sgsin8-edge-lx-008.ts.apple.com (acdn/327.16648), ...
  X-Cache: hit-stale, miss
  ```
  自建 CDN（acdn），5 分钟缓存，**没有任何 `X-RateLimit-*` / `Retry-After` 头**
- robots.txt 无 `Crawl-delay`
- **建议仍保守**：1–2 秒间隔、单线程、带正常 UA、失败退避重试。178 个请求的量级对 Apple CDN 毫无压力，但没有理由激进。
- ⚠️ 未测试：并发抓取、连续数百请求后的行为。**不要开并发。**

### 4.3 逐字稿的文字质量：**自动语音转写，未做人工校对**（这是最影响翻译的一点）

实测证据（13 场统计）：

| 指标 | 2014–2019 | 2020–2026 |
|---|---|---|
| 每个 `span.sentence` 平均词数 | 4.6–7.9 | 8.3–9.3 |
| 以句末标点结尾的 span 比例 | 27%–59% | 56%–61% |
| 以大写字母开头的 span 比例 | 30%–60% | 56%–61% |

判读：

1. **有标点、有大小写**，不是裸的无标点 ASR 输出，说明经过了标点恢复处理，读起来通顺。
2. **但切分是按字幕行走的，不是按句子**。`wwdc2019/423` 实测连续 4 行断在 `my name is` / `Spencer Lewson, and I'm an` / `engineer on the Performance Team` / `here at Apple.` —— 一句话被切成 4 段。老年份（2018/2019）只有 27%–32% 的 span 以句末标点结尾，说明**断句极碎**。
3. **新年份质量明显更好**：2020 年后 span 变长（8–9 词）、句末标点比例升到 56%–61%，接近「一行一句」。老年份需要更多的重新分句处理。
4. 未见 `[APPLAUSE]`、`[MUSIC]` 之类的标记（13 场里只有 3 场各出现 1 次方括号标记），但 2021–2023 有若干场出现 `♪` 音乐符号（2–4 个），预处理时应剔除。
5. **未验证**：没有系统性统计技术术语的转写错误率。ASR 对 `dyld`、`Mach-O`、`ObjC`、`autorelease` 这类术语容易出错，**建议翻译前先对照官方文档建一份术语表做正则修正**，否则错误会被翻译放大。

**对翻译流程的三条硬性建议**：

1. 翻译前必须做**段落重组**：同一 `<p>` 内的所有 span 拼成整段 → 重新分句 → 再送翻译。逐 span 翻译一定会得到破碎中文。
2. 保留每段首个 `data-start` 作为时间锚点，方便回看视频对照。
3. 2023+ 的 session 一并抓 `li.supplement.summary` 的**章节标题 + Apple 官方章节摘要**，那是人工撰写的高质量文本，可以当译文的校对基准，也是天然的目录。

### 4.4 幻灯片 PDF 值不值得一起存

- **只有 2014–2019 有**（2020 起 Apple 完全取消）。短名单 178 场里 56 场有。
- 实测体积：`wwdc2016/416` 0.9 MB、`wwdc2014/604` 2.6 MB、`wwdc2017/706` 2.7 MB、`wwdc2019/423` 4.8 MB、`wwdc2018/416` **9.6 MB**。均值约 4 MB。
- 56 场合计约 **220 MB**。
- **建议：值得存，但不要放进 Git 主库。** 理由：
  - 老 session 的关键内容（内存布局图、链接流程图、dyld 阶段图）大量在幻灯片里，逐字稿里只是「as you can see here」，**不存 PDF 会丢掉信息**
  - 2020 年后没有 PDF，逐字稿的自解释性反而更强（讲者被要求口述图表）
  - 但 220 MB 二进制会让 Git 仓库变臃肿。建议用 Git LFS，或单独放一个 `slides/` 目录并 gitignore，另做备份

### 4.5 最大的三个风险

**风险 1：Apple 持续下架老 session，且已经发生（最高优先级）**
2013 及更早**已全部消失**（`/videos/wwdc2013/` 是空壳，历史 URL 全部 302）。WWDC2018 从一百多场剩 38 场，WWDC2014 只剩 6 场。**当前能看到的 1560 场里，明年还剩多少不可知。** 缓解：尽快按短名单抓完；元数据（`wwdc_sessions.json`）现在就已存下，这份快照本身有价值。

**风险 2：逐字稿是 ASR 产物，术语错误会被翻译放大**
文本有标点但断句碎（老年份仅 27% 的 span 以句末标点结尾），且未见人工校对痕迹。技术术语转写错误率未量化。若直接机器翻译，`dyld`/`Mach-O`/`autorelease pool` 这类词的错误会级联到中文。缓解：段落重组 + 术语表正则预修正 + 用 2023+ 的官方章节摘要交叉校对。

**风险 3：无 API、无 sitemap，整个清单挂在一个 HTML 页面的 CSS class 上**
`vc-card`、`vc-card__title`、`data-filter-topics`、`span.sentence`、`data-start`、`#transcript-content` 这些都是 Apple 前端实现细节，**改版就会全部失效**（且没有 JSON 接口可以退守）。同时 `data-chapter-lenght` 这种拼写错误说明这些属性没有契约保证。缓解：把 `wwdc_sessions.json` 当作已固化的快照（不要每次重抓）；解析器对每个选择器做「命中数为 0 就告警」而不是静默跳过；原始 HTML 留档一份，将来选择器变了还能离线重解析。

**次级风险（补充）**：官方简体中文字幕的抓取成本极高——虽然 1355/1560 场有官方简中字幕（见下），但 HLS 把字幕切成 6 秒一片，`wwdc2020/10163` 的中文轨有 **229 个 `.webvtt` 分片**，`wwdc2025/312` 有 **315 个**。按 150 场算是 4 万多个请求，**不适合礼貌抓取**，不要走这条路。

---

## 5. 附：一个意外但很重要的发现 —— 官方简体中文字幕已存在

索引里的 `data-filter-subtitle` 显示，**1560 场已发布 session 中有 1355 场带 `simplified chinese`**（短名单 178 场里有 164 场）。分年份：wwdc2020 205/209、wwdc2021 183/202、wwdc2022 182/184、wwdc2019 153/153、wwdc2018 38/38、wwdc2017 36/36、wwdc2016 16/16、wwdc2015 11/11、**wwdc2014 0/6**（唯一缺口）。

已实测确认可下载。`wwdc2020/10163` 的 master playlist（HTTP 200）里有：

```
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",NAME="English",...,LANGUAGE="en",URI="cc/en/en.m3u8"
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",NAME="日本語",...,LANGUAGE="ja",URI="cc/ja/ja.m3u8"
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",NAME="简体中文",...,LANGUAGE="zh",URI="cc/zh/zh.m3u8"
```

抓取第一个中文分片 `cc/zh/fileSequence0.webvtt`（HTTP 200，209 字节）确认是标准 WebVTT，带 `X-TIMESTAMP-MAP` 和毫秒级时间轴，中文为人工感很强的规范译文（含用括号标注屏幕文字的惯例）。

2025 年的新打包（`cmaf.m3u8`）提供 7 种字幕语言（en/zh/pt/fr/ja/ko/…），路径为 `subtitles/zho/prog_index.m3u8`，结构相同。

**这对用户的意义**：
- **不必从零翻译。** 官方中文字幕可作为译文的**基准/对照**，用来校验术语（Apple 自己怎么译 `dyld`、`引用计数`、`挂起点`）和纠正 ASR 错误。这能显著提升译文质量。
- **但不要用它做主抓取路径**：分片数 229–315 个/场，请求成本比英文逐字稿（1 个请求）高两个数量级。
- **建议策略**：主线走「英文 HTML 逐字稿 → 段落重组 → 自己翻译」；只对最核心的 10–20 场（如 415/423/10163/110362/10268/10254）额外拉一次官方中文字幕做术语校准和译文比对。
- 2014 年那 6 场无中文字幕，且都不在短名单里，可忽略。

---

## 6. 产出文件清单

| 文件 | 内容 |
|---|---|
| `WWDC_RECON.md` | 本报告 |
| `wwdc_sessions.json` | **全量 1841 条**。字段：`id`、`collection`、`year`、`title`、`url`、`event`、`duration`、`topics`、`platforms`、`subtitles`、`released`、`category`、`description`（英文摘要全文）、`has_transcript`（`verified` 23 条 / `assumed` 1537 条 / `none` 281 条）、`transcript_sentence_count`（已验证的 23 条）、`slides_pdf` |
| `wwdc_shortlist.json` | **推荐归档 178 条**。上述字段 + `group`（9 个主题分组）、`evergreen`（是否长期有效）、`reason`（一句话理由） |
| `all_videos_index.json` | 解析中间产物，等价于 `wwdc_sessions.json` 但不含 transcript/pdf 判定 |
| `raw/*.html` | 实抓的 26 个原始 HTML（1 个 all-videos + 2 个 collection 页 + 23 个 session 页），供离线重解析与结论复核 |

**字段诚实性说明**：`has_transcript` 中 `assumed` 的 1537 条**未逐一验证**，依据是 23/23 的抽样命中率与 2014→2026 结构一致性。`slides_pdf` 依据「2014–2019 有、2020+ 无」的实测规律推断，其中 6 个年份各已实测确认至少一例。
