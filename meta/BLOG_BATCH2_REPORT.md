# 第三方技术博客归档 · 第二批报告

归档日期：2026-07-27　·　配置：`meta/blog_sources_batch2.json`　·　清单：`meta/blog_index/<key>.json`

```
BLOG_CONFIG=meta/blog_sources_batch2.json python3 tools/blog.py discover|fetch|render [<key>...]
```

`tools/blog.py` 的 `CONFIG` 现在支持 `BLOG_CONFIG` 环境变量覆盖（不设时行为与之前完全一致），
所以这一批的源配置单独放在 `blog_sources_batch2.json`，没有动 `blog_sources.json`。

---

## 1. 总览

| 优先 | key | 站点 | lang | 清单 | 归档 | 中位正文 | 代码块覆盖率 | 授权 | robots |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `objcio` | www.objc.io | en | 149 | **149** | 2251 词 | 70 % | 未声明 → 私有 | 无 robots.txt（404），无限制 |
| 2 | `nshipster` | nshipster.com | en | 196 | **196** | 1160 词 | 91 % | **CC BY-NC** → 可非商业再分发 | `User-agent: * / Allow: /` |
| 3 | `ciechanowski` | ciechanow.ski | en | 23 | **23** | 5739 词 | 30 % | © Bartosz Ciechanowski → 私有 | 无 robots.txt（404），无限制 |
| 4 | `jessesquires` | www.jessesquires.com | en | 298 | **298** | 604 词 | 39 % | © 2014–2026 Jesse Squires → 私有 | 只点名禁 GPTBot，`*` 放开 |
| 5 | `emergetools` | www.emergetools.com | en | 34 | **34** | 1591 词 | 74 % | All rights reserved → 严格私有 | 只禁 `/private/` |
| 6 | `devtang` | blog.devtang.com | zh | — | **0（跳过）** | — | — | — | **点名 `ClaudeBot: Disallow: /` → 跳过** |
| 7 | `southpeak` | southpeak.github.io | zh | 86 | **86** | 2210 汉字 | 86 % | © 2017 南峰子 → 私有 | 无 robots.txt（404），无限制 |
| 8 | `fbeng` | engineering.fb.com | en | 95 | **95** | 1014 词 | 20 % | © Meta → 私有 | `User-agent: * / Disallow:`（空＝全放开） |
| 9 | `kreya` | kreya.app | en | 47 | **47** | 771 词 | 47 % | © riok GmbH → 私有 | 只有 `User-agent: *` + Sitemap，无 Disallow |

合计 **928 篇**（8 个源），另有 1 个源因 robots.txt 被跳过。最终抓取零失败
（首轮并发两批时有 52 篇碰到瞬时 ConnectError / RemoteProtocolError：nshipster 23、southpeak 18、
jessesquires 10、fbeng 1；`fetch` 按缓存文件断点续抓，串行重跑一遍全部补齐，无一 4xx/5xx），
渲染零失败、零「缺 container」。

**只有 `nshipster` 一个源可以公开再分发（CC BY-NC，须署名、非商业）。其余全部按私有归档处理。**

---

## 2. 被跳过的源

### `blog.devtang.com`（唐巧）—— robots.txt 点名禁止，未抓取任何页面

`https://blog.devtang.com/robots.txt` 的 Cloudflare Managed content 段：

```
User-agent: *
Content-Signal: search=yes,ai-train=no,use=reference
Allow: /

User-agent: ClaudeBot
Disallow: /
```

同段还禁掉了 CCBot / GPTBot / Google-Extended / Applebot-Extended / Amazonbot / Bytespider /
meta-externalagent。**只看 `User-agent: *` 会误判为放开**，`tools/blog.py` 的 `robots_allows()`
专门检查点名段，实测输出：

```
devtang: 跳过 —— robots.txt 点名禁止 ['claudebot']：Disallow: /
```

配置条目保留在 `blog_sources_batch2.json` 里（`status: skipped-robots`），这样每次 discover/fetch
都会重新核验并打印跳过原因；`.cache/blogs/devtang/` 与 `blogs/zh/devtang/` 均不存在。
唐巧的 GCD / 对象模型内容如需归档，只能人工按需保存单页，不跑爬虫。

其余 8 个源的 robots.txt 都不含针对 ClaudeBot / anthropic-ai / claude-web 的禁令，也没有
`User-agent: * Disallow: /`。

---

## 3. 清单来源：一律 sitemap 或全量索引页，不用 feed

本批 **没有一个源用 feed**。实测依据：

| key | 用了什么 | 为什么不是别的 |
|---|---|---|
| `objcio` | 索引页 `/issues/` | `sitemap.xml` **404**。`/issues/` 单页就含全部 24 期 × 全部文章共 149 条 |
| `nshipster` | `sitemap.xml`（209 条） | 排除 13 个 `/authors/` 页 + 首页 → 196 篇 |
| `ciechanowski` | `sitemap.xml`（28 条） | 排除 `/archives/`、`/post/`、`/extra/`、`/index.html`、首页 → 23 篇 |
| `jessesquires` | `sitemap.xml`（502 条） | **204 条是 tags/categories/archive/关于页**，排除后 298 篇 |
| `emergetools` | `sitemap.xml`（38 条） | `/blog` 索引页只给 13 篇（首屏），sitemap 反而全；另有 2 条拼接错误的外链，netloc 不匹配自动剔除 → 34 篇 |
| `southpeak` | 索引页 `/archives/` **共 9 页** | `sitemap.xml` / `atom.xml` / `rss.xml` / `baidusitemap.xml` **全 404**，站点没有任何 feed。单页只有 10 篇，必须逐页翻 → 86 篇 |
| `fbeng` | 分类页 `/category/ios/` **共 8 页** | 全站 `post-sitemap` 有 **1089 篇**，绝大多数与移动端无关 → 见下节 |
| `kreya` | `sitemap.xml`（137 条） | 排除产品页/对比页/分页/作者页 → 47 篇 |

### 为此给 `blog.py` 加的第二处改动（向后兼容）

`discover` 的 `url` 现在可以是**字符串或字符串数组**。Hexo 的 `/archives/page/N/` 和
WordPress 的 `/category/x/page/N/` 都只在单页给十来条，原来的单 URL 抓法会静默丢掉 90 % 的文章
（southpeak 只会拿到 10 篇而不是 86 篇）。传字符串时行为与改动前完全一致。

### `engineering.fb.com` 的过滤口径

用站方**自己的 iOS 分类** `/category/ios/`（8 页，逐页翻），而不是整站 sitemap：

- 全站 `post-sitemap.xml` + `post-sitemap2.xml` 共 **1089 篇** —— 绝不整站抓
- `/category/ios/` 8 页去重后 **95 篇**，全部是站方归到 iOS 分类下的文章
- 按 URL 里的主分类统计：android 44、ios 30、security 5、open-source 3、developer-tools 3、
  video-engineering 3、ml-applications 2、web 2、其余各 1 —— 交叉归类到 iOS 分类的移动端文章
  （如 WhatsApp E2EE、HDR video、QUIC）也在内，这正是要的
- 站方另有 `/category/android/` 分类，本项目是 Apple 平台归档，未纳入

---

## 4. 逐源体检

体检口径：正文＝去掉 frontmatter、「> 原文」行和全部围栏代码块之后，英文数单词、中文数汉字；
代码块覆盖率＝有围栏的篇数占比。

### 4.1 `objcio` — 149 篇 → `blogs/en/objcio/`

- 中位正文 **2251 词**（平均 2403，最短 99，最长 7930），总围栏 **1555**
- 代码块覆盖率 **70 %**（105/149）
- **覆盖率不是问题**：149 篇里有 24 篇「Editorial（卷首语）」和 issue #20 的 4 篇人物访谈，
  本来就没有代码。最短的 5 篇全是 editorial（99–187 词），与原站一致
- 抽查 `core-data-overview.md`（Core Data 概述）与 `importing-large-data-sets.md`：
  开头直接是正文首段、无导航残留，小节标题层级完整，结尾是文章最后一段
- container 用 `//div[contains(@class,'c-article__body')]`。`//article` 会连「浏览本期」侧栏
  和 header 一起吃进来

### 4.2 `nshipster` — 196 篇 → `blogs/en/nshipster/`

- 中位正文 **1160 词**，代码块覆盖率 **91 %**（178/196），中位 8 个代码块，总围栏 1673
- 全批代码率最高的源，符合 NSHipster「短文＋大量代码片段」的风格
- 抽查 `pragma.md`、`rawrepresentable.md`：开头是 h1 标题 + 作者署名行，随后直接进正文；
  代码缩进完好；结尾是原文末段
- 三篇点名要的经典篇全在且完整：`method-swizzling.md`（1321 词 / 2 块）、
  `associated-objects.md`（1097 词 / 3 块）、`key-value-observing.md`（1648 词 / 9 块）

### 4.3 `ciechanowski` — 23 篇 → `blogs/en/ciechanowski/`

- 中位正文 **5739 词**（平均 6965，最长 17187），全批最长
- 代码块覆盖率 **30 %**（7/23），**这是内容本身决定的**：早期 ObjC 逆向系列代码密集，
  2017 年之后转成 WebGL 交互式长文（gears / mechanical-watch / cameras-and-lenses 等），
  正文本来就没有代码块，交互 canvas 无法转成 Markdown（已知损失，文字与配图完整）
- 点名要的两篇代码最密：`exposing-nsmutablearray`（4389 词 / **50 个代码块**）、
  `exposing-nsdictionary`（3583 词 / 35 块），另有配套的
  `nsdictionaryi-objectforkey`（反汇编分析，39 块）
- 抽查 `cameras-and-lenses`、`nsdictionaryi-objectforkey`：开头无导航垃圾，
  反汇编那篇结尾停在 `ret` 指令上，代码列对齐完整
- container 必须显式配 `//div[@id='content']`（站点无 `article` / `main`）

### 4.4 `jessesquires` — 298 篇 → `blogs/en/jessesquires/`

- 中位正文 **604 词**，代码块覆盖率 **39 %**（117/298）
- **中位数低是真实的**：Jesse 的博客有大量「链接博客」式短文（转发 + 两三句评论）、
  播客节目公告、读书笔记。最短的几篇（70–172 词）逐一核对过，原站就是那么短
- 点名要的 `implementing-a-main-thread-watchdog-on-ios.md` 在（519 词 / 4 个代码块），
  含完整的 watchdog 实现代码
- 抽查 `ios-14-app-library.md`、`xcode-13-device-orientation-options-bug.md`：开头即正文，
  图片链接绝对化正确，结尾完整（含 Feedback 编号）

### 4.5 `emergetools` — 34 篇 → `blogs/en/emergetools/`

- 中位正文 **1591 词**，代码块覆盖率 **74 %**（25/34）
- 点名要的两篇都在：`how-ios-15-makes-your-app-launch-faster`（1474 词 / 4 块，含
  `dyld_chained_ptr_64_rebase` 结构体与 `otool` 输出）、
  `how-order-files-reduce-app-startup-time`（1804 词）
- Next.js + Tailwind 站，class 全是原子类没有语义名，样板只能靠「内含什么」定位。
  已剔：分享条（含 twitter intent 链接的块，页首页尾各一处）、Related articles、
  订阅区、Back to blog。抽查两篇确认页尾不再有分享链接表格
- 保留了文章头部的标题/日期/作者行（是有效元信息）

### 4.6 `southpeak` — 86 篇 → `blogs/zh/southpeak/`

- 中位正文 **2210 汉字**，代码块覆盖率 **86 %**（74/86），中位 8 个代码块，总围栏 1084
- 点名要的 `foundation-nsnotificationcenter.md` 在（3601 词元 / **16 个代码块**）
- 抽查 `uikit-uicontrol.md`、`quartz-2d编程指南之十三…md`：开头即正文首段，
  行内 `` `UIButton` `` 等代码标记完好，多行方法签名分行正确，结尾是参考链接列表
- **本源触发了一个新结构，已改 `tools/html2md.py`**：见第 6 节

### 4.7 `fbeng` — 95 篇 → `blogs/en/fbeng/`

- 中位正文 **1014 词**，代码块覆盖率 **20 %**（19/95）
- **20 % 是这个站的真实形态，不是抓漏**：Meta Engineering 大量是发布公告、会议回顾、
  播客节目页、开源项目介绍，本来就没有代码。逐篇核对了最短的 5 篇
  （214–275 词），原文就是那么长（例如 `how-meta-built-threads-in-5-months` 是一条
  播客节目预告，正文只有几段 + 收听链接列表）
- 抽查 `facebook-open-source-2016-year-in-review.md`、`2018-scale-conference-recap.md`：
  开头即正文，链接与图片完整，无侧栏/相关文章残留
- container `//div[contains(@class,'entry-content')]`（WordPress + Yoast）

### 4.8 `kreya` — 47 篇 → `blogs/en/kreya/`

- 中位正文 **771 词**，代码块覆盖率 **47 %**（22/47）
- **覆盖率低是因为一半是版本更新日志**（`kreya-1.7 ~ 1.20 what's new` 共 14 篇），
  这些本来就没代码；技术长文那一档代码完整
- 核心价值的两篇在且完整：`demystifying-the-protobuf-wire-format`（1051 词 / **11 个代码块**）
  和它的 part 2
- 抽查 `telemetry-insights-q2-2021`、`catching-api-regressions-with-snapshot-testing`：
  开头即正文，Docusaurus 的标题锚点已剔干净（见第 6 节）

---

## 5. objc.io ↔ objccn 对应关系

**149 组全部配上，一一对应，无一遗漏、无一重复。**

- `blogs/en/objcio/` 149 篇英文原文
- `blogs/zh/objccn/` 149 篇官方中文译文（第一批已归档）
- 机器可读的配对清单：**`meta/blog_index/objcio_objccn_pairs.json`**

### 配对方法与交叉验证

两个站的 URL 结构不同：objc.io 是 `/issues/<N>-<主题>/<文章 slug>`，objccn 是 `/issue-<N>-<M>`。
用了两条**互相独立**的线索并交叉验证：

1. **序号法**（采用）：objccn 的 `issue-N-M` 中 `M` 就是该期第 M 篇（0 = 卷首语/介绍）。
   对 objc.io `/issues/` 索引页上每期文章的**文档顺序**取第 M 个。24 期全部对得上，
   得到 149 ↔ 149 的双射。
2. **反链法**（验证）：149 篇 objccn 译文里有 147 篇正文中带一句
   「原文 [Title](http://www.objc.io/issue-N/<slug>.html)」，直接给出英文 slug。

两法在 **148/149** 上一致。唯一分歧：

| objccn | 中文标题 | 序号法 | 反链法 |
|---|---|---|---|
| `issue-1-4` | View Controller 容器 | `containment-view-controller` ✅ | `testing-view-controllers` ❌ |

`issue-1-4` 的中文标题是「View Controller 容器」，对应的显然是 *View Controller Containment*；
**objccn 页面上那条原文链接本身写错了**（指向了同期的 *Testing View Controllers*，而
`issue-1-3` 才是「测试 View Controllers」）。以序号法为准，两篇各归各位。
另外 2 篇没有反链的是 issue #1 和 #24 的卷首语，按序号法归位。

### 完整对应表


#### Issue #1 — View Controllers（5 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Introduction | `introduction.md` | 介绍 | `介绍.md` |
| 1 | Lighter View Controllers | `lighter-view-controllers.md` | 更轻量的 View Controllers | `更轻量的-view-controllers.md` |
| 2 | Clean Table View Code | `clean-table-view-code.md` | 整洁的 Table View 代码 | `整洁的-table-view-代码.md` |
| 3 | Testing View Controllers | `testing-view-controllers.md` | 测试 View Controllers | `测试-view-controllers.md` |
| 4 | View Controller Containment | `view-controller-containment.md` | View Controller 容器 | `view-controller-容器.md` |

#### Issue #2 — Concurrency（6 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-778e4b.md` | 卷首语 | `卷首语.md` |
| 1 | Concurrent Programming: APIs and Challenges | `concurrent-programming-apis-and-challenges.md` | 并发编程：API 及挑战 | `并发编程-api-及挑战.md` |
| 2 | Common Background Practices | `common-background-practices.md` | 常见的后台实践 | `常见的后台实践.md` |
| 3 | Low-Level Concurrency APIs | `low-level-concurrency-apis.md` | 底层并发 API | `底层并发-api.md` |
| 4 | Thread-Safe Class Design | `thread-safe-class-design.md` | 线程安全类的设计 | `线程安全类的设计.md` |
| 5 | Testing Concurrent Applications | `testing-concurrent-applications.md` | 测试并发程序 | `测试并发程序.md` |

#### Issue #3 — Views（6 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-fd4920.md` | 卷首语 | `卷首语-323959.md` |
| 1 | Getting Pixels onto the Screen | `getting-pixels-onto-the-screen.md` | 绘制像素到屏幕上 | `绘制像素到屏幕上.md` |
| 2 | Understanding Scroll Views | `understanding-scroll-views.md` | 理解 Scroll Views | `理解-scroll-views.md` |
| 3 | Custom Collection View Layouts | `custom-collection-view-layouts.md` | 自定义 Collection View 布局 | `自定义-collection-view-布局.md` |
| 4 | Custom Controls | `custom-controls.md` | 自定义控件 | `自定义控件.md` |
| 5 | Advanced Auto Layout Toolbox | `advanced-auto-layout-toolbox.md` | 先进的自动布局工具箱 | `先进的自动布局工具箱.md` |

#### Issue #4 — Core Data（8 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-31efa0.md` | 卷首语 | `卷首语-fa5dcb.md` |
| 1 | Core Data Overview | `core-data-overview.md` | Core Data 概述 | `core-data-概述.md` |
| 2 | A Complete Core Data Application | `a-complete-core-data-application.md` | 一个完整的 Core Data 应用 | `一个完整的-core-data-应用.md` |
| 3 | On Using SQLite and FMDB Instead of Core Data | `on-using-sqlite-and-fmdb-instead-of-core-data.md` | 用 SQLite 和 FMDB 替代 Core Data | `用-sqlite-和-fmdb-替代-core-data.md` |
| 4 | Data Models and Model Objects | `data-models-and-model-objects.md` | 数据模型和模型对象 | `数据模型和模型对象.md` |
| 5 | Importing Large Data Sets | `importing-large-data-sets.md` | 导入大数据集 | `导入大数据集.md` |
| 6 | Fetch Requests | `fetch-requests.md` | Fetch 请求 | `fetch-请求.md` |
| 7 | Custom Core Data Migrations | `custom-core-data-migrations.md` | 自定义 Core Data 迁移 | `自定义-core-data-迁移.md` |

#### Issue #5 — iOS 7（8 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-9c41c6.md` | 卷首语 | `卷首语-e24a8d.md` |
| 1 | Getting to Know TextKit | `getting-to-know-textkit.md` | 初识 TextKit | `初识-textkit.md` |
| 2 | UICollectionView + UIKit Dynamics | `uicollectionview-uikit-dynamics.md` | UICollectionView + UIKit 力学 | `uicollectionview-uikit-力学.md` |
| 3 | View Controller Transitions | `view-controller-transitions.md` | View Controller 转场 | `view-controller-转场.md` |
| 4 | From NSURLConnection to NSURLSession | `from-nsurlconnection-to-nsurlsession.md` | 从 NSURLConnection 到 NSURLSession | `从-nsurlconnection-到-nsurlsession.md` |
| 5 | Multitasking in iOS 7 | `multitasking-in-ios-7.md` | iOS 7 的多任务 | `ios-7-的多任务.md` |
| 6 | iOS 7: Hidden Gems and Workarounds | `ios-7-hidden-gems-and-workarounds.md` | iOS 7 : 隐藏技巧和变通之道 | `ios-7-隐藏技巧和变通之道.md` |
| 7 | Re-Designing an App for iOS 7 | `re-designing-an-app-for-ios-7.md` | 为 iOS 7 重新设计 App | `为-ios-7-重新设计-app.md` |

#### Issue #6 — Build Tools（6 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-98e2c3.md` | 卷首语 | `卷首语-c335e3.md` |
| 1 | The Build Process | `the-build-process.md` | Build 过程 | `build-过程.md` |
| 2 | The Compiler | `the-compiler.md` | 编译器 | `编译器.md` |
| 3 | Mach-O Executables | `mach-o-executables.md` | Mach-O 可执行文件 | `mach-o-可执行文件.md` |
| 4 | CocoaPods Under The Hood | `cocoapods-under-the-hood.md` | 深入理解 CocoaPods | `深入理解-cocoapods.md` |
| 5 | Travis CI for iOS | `travis-ci-for-ios.md` | 为 iOS 建立 Travis CI | `为-ios-建立-travis-ci.md` |

#### Issue #7 — Foundation（7 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-1dc21d.md` | 卷首语 | `卷首语-e5f663.md` |
| 1 | The Foundation Collection Classes | `the-foundation-collection-classes.md` | 基础集合类 | `基础集合类.md` |
| 2 | Value Objects | `value-objects.md` | 值对象 | `值对象.md` |
| 3 | Key-Value Coding and Observing | `key-value-coding-and-observing.md` | KVC 和 KVO | `kvc-和-kvo.md` |
| 4 | Communication Patterns | `communication-patterns.md` | 消息传递机制 | `消息传递机制.md` |
| 5 | Custom Formatters | `custom-formatters.md` | 自定义 Formatters | `自定义-formatters.md` |
| 6 | Linguistic Tagging | `linguistic-tagging.md` | 语言标签 | `语言标签.md` |

#### Issue #8 — Quadcopter（5 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-27e2d2.md` | 卷首语 | `卷首语-325536.md` |
| 1 | The Project | `the-project.md` | 项目介绍 | `项目介绍.md` |
| 2 | Communicating with the Quadcopter | `communicating-with-the-quadcopter.md` | 与四轴无人机的通讯 | `与四轴无人机的通讯.md` |
| 3 | The Navigator App | `the-navigator-app.md` | 导航应用 | `导航应用.md` |
| 4 | The Client App | `the-client-app.md` | 客户端 | `客户端.md` |

#### Issue #9 — Strings（6 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-b10ee8.md` | 卷首语 | `卷首语-c3c909.md` |
| 1 | NSString and Unicode | `nsstring-and-unicode.md` | NSString 与 Unicode | `nsstring-与-unicode.md` |
| 2 | Working with Strings | `working-with-strings.md` | 玩转字符串 | `玩转字符串.md` |
| 3 | String Localization | `string-localization.md` | 字符串本地化 | `字符串本地化.md` |
| 4 | String Parsing | `string-parsing.md` | 字符串解析 | `字符串解析.md` |
| 5 | String Rendering | `string-rendering.md` | 字符串渲染 | `字符串渲染.md` |

#### Issue #10 — Syncing Data（7 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-43c2fe.md` | 卷首语 | `卷首语-b5235c.md` |
| 1 | Data Synchronization | `data-synchronization.md` | 数据同步 | `数据同步.md` |
| 2 | iCloud and Core Data | `icloud-and-core-data.md` | iCloud 和 Core Data | `icloud-和-core-data.md` |
| 3 | Mastering the iCloud Document Store | `mastering-the-icloud-document-store.md` | 精通 iCloud 文档存储 | `精通-icloud-文档存储.md` |
| 4 | A Sync Case Study | `a-sync-case-study.md` | 同步案例学习 | `同步案例学习.md` |
| 5 | A Networked Core Data Application | `a-networked-core-data-application.md` | Core Data 网络应用实例 | `core-data-网络应用实例.md` |
| 6 | IP, TCP, and HTTP | `ip-tcp-and-http.md` | IP，TCP 和 HTTP | `ip-tcp-和-http.md` |

#### Issue #11 — Android（7 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-9c0a1e.md` | 卷首语 | `卷首语-eabfd1.md` |
| 1 | Android 101 for iOS Developers | `android-101-for-ios-developers.md` | iOS 开发者的 Android 第一课 | `ios-开发者的-android-第一课.md` |
| 2 | Android Intents | `android-intents.md` | Android Intents | `android-intents.md` |
| 3 | Responsive Android Applications | `responsive-android-applications.md` | 响应式 Android 应用 | `响应式-android-应用.md` |
| 4 | Android’s Notification Center | `android-s-notification-center.md` | Android 通知中心 | `android-通知中心.md` |
| 5 | SQLite Database Support in Android | `sqlite-database-support-in-android.md` | Android 中的 SQLite 数据库支持 | `android-中的-sqlite-数据库支持.md` |
| 6 | Dependency Injection, Annotations, and why Java is Better Than you Think it is | `dependency-injection-annotations-and-why-java-is-better-than-you-think-it-is.md` | 依赖注入和注解，为什么 Java 比你想象的要好 | `依赖注入和注解-为什么-java-比你想象的要好.md` |

#### Issue #12 — Animations（7 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-ca1ff4.md` | 卷首语 | `卷首语-a3b477.md` |
| 1 | Animations Explained | `animations-explained.md` | 动画解释 | `动画解释.md` |
| 2 | Animating Custom Layer Properties | `animating-custom-layer-properties.md` | Layer 中自定义属性的动画 | `layer-中自定义属性的动画.md` |
| 3 | Custom Container View Controller Transitions | `custom-container-view-controller-transitions.md` | 自定义 ViewController 容器转场 | `自定义-viewcontroller-容器转场.md` |
| 4 | View-Layer Synergy | `view-layer-synergy.md` | View-Layer 协作 | `view-layer-协作.md` |
| 5 | Animating Collection Views | `animating-collection-views.md` | Collection View 动画 | `collection-view-动画.md` |
| 6 | Interactive Animations | `interactive-animations.md` | 交互式动画 | `交互式动画.md` |

#### Issue #13 — Architecture（6 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-e32626.md` | 卷首语 | `卷首语-9dc017.md` |
| 1 | Introduction to MVVM | `introduction-to-mvvm.md` | MVVM 介绍 | `mvvm-介绍.md` |
| 2 | Avoiding Singleton Abuse | `avoiding-singleton-abuse.md` | 避免滥用单例 | `避免滥用单例.md` |
| 3 | Behaviors in iOS Apps | `behaviors-in-ios-apps.md` | iOS 中的行为 | `ios-中的行为.md` |
| 4 | Subclassing | `subclassing.md` | 子类 | `子类.md` |
| 5 | Architecting iOS Apps with VIPER | `architecting-ios-apps-with-viper.md` | 使用 VIPER 构建 iOS 应用 | `使用-viper-构建-ios-应用.md` |

#### Issue #14 — Mac（6 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-9b979c.md` | 卷首语 | `卷首语-6db119.md` |
| 1 | Making Your Mac App’s Data Scriptable | `making-your-mac-app-s-data-scriptable.md` | 使 Mac 应用数据脚本化 | `使-mac-应用数据脚本化.md` |
| 2 | Scripting from a Sandbox | `scripting-from-a-sandbox.md` | 在沙盒中编写脚本 | `在沙盒中编写脚本.md` |
| 3 | Plugins | `plugins.md` | 插件 | `插件.md` |
| 4 | XPC | `xpc.md` | XPC | `xpc.md` |
| 5 | AppKit for UIKit Developers | `appkit-for-uikit-developers.md` | 从 UIKit 到 AppKit | `从-uikit-到-appkit.md` |

#### Issue #15 — Testing（8 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-5d6844.md` | 卷首语 | `卷首语-778d2c.md` |
| 1 | Behavior-Driven Development | `behavior-driven-development.md` | 行为驱动开发 | `行为驱动开发.md` |
| 2 | Real-World Testing with XCTest | `real-world-testing-with-xctest.md` | XCTest 测试实战 | `xctest-测试实战.md` |
| 3 | Dependency Injection | `dependency-injection.md` | 依赖注入 | `依赖注入.md` |
| 4 | Bad Testing Practices | `bad-testing-practices.md` | 糟糕的测试 | `糟糕的测试.md` |
| 5 | Test Doubles: Mocks, Stubs, and More | `test-doubles-mocks-stubs-and-more.md` | 置换测试: Mock, Stub 和其他 | `置换测试-mock-stub-和其他.md` |
| 6 | User Interface Testing | `user-interface-testing.md` | UI 测试 | `ui-测试.md` |
| 7 | Snapshot Testing | `snapshot-testing.md` | 截图测试 | `截图测试.md` |

#### Issue #16 — Swift（6 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-1c8bb7.md` | 卷首语 | `卷首语-f78d48.md` |
| 1 | The Power of Swift | `the-power-of-swift.md` | Swift 的强大之处 | `swift-的强大之处.md` |
| 2 | A Warm Welcome to Structs and Value Types | `a-warm-welcome-to-structs-and-value-types.md` | 结构体和值类型 | `结构体和值类型.md` |
| 3 | The Many Faces of Swift Functions | `the-many-faces-of-swift-functions.md` | Swift 方法的多面性 | `swift-方法的多面性.md` |
| 4 | Functional APIs with Swift | `functional-apis-with-swift.md` | Swift 的函数式 API | `swift-的函数式-api.md` |
| 5 | Rapid Prototyping in Swift Playgrounds | `rapid-prototyping-in-swift-playgrounds.md` | Playground 快速原型制作 | `playground-快速原型制作.md` |

#### Issue #17 — Security（4 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-667b78.md` | 卷首语 | `卷首语-cbb494.md` |
| 1 | Why Security Still Matters Today | `why-security-still-matters-today.md` | 为什么今天安全仍然重要 | `为什么今天安全仍然重要.md` |
| 2 | Inside Code Signing | `inside-code-signing.md` | 代码签名探析 | `代码签名探析.md` |
| 3 | Receipt Validation | `receipt-validation.md` | 收据验证 | `收据验证.md` |

#### Issue #18 — Games（6 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-2ff8e1.md` | 卷首语 | `卷首语-811d4c.md` |
| 1 | Designing Elegant Mobile Games | `designing-elegant-mobile-games.md` | 设计优雅的移动游戏 | `设计优雅的移动游戏.md` |
| 2 | Metal | `metal.md` | Metal | `metal.md` |
| 3 | Scene Kit | `scene-kit.md` | Scene Kit | `scene-kit.md` |
| 4 | Multipeer Connectivity in Games | `multipeer-connectivity-in-games.md` | 游戏中的多点互联 | `游戏中的多点互联.md` |
| 5 | Virtual Soundscapes: The Art of Sound Design | `virtual-soundscapes-the-art-of-sound-design.md` | 虚拟音域 - 声音设计的艺术 | `虚拟音域-声音设计的艺术.md` |

#### Issue #19 — Debugging（6 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-7878c6.md` | 卷首语 | `卷首语-c6e938.md` |
| 1 | Debugging: A Case Study | `debugging-a-case-study.md` | 调试：案例学习 | `调试-案例学习.md` |
| 2 | Dancing in the Debugger — A Waltz with LLDB | `dancing-in-the-debugger-a-waltz-with-lldb.md` | 与调试器共舞 - LLDB 的华尔兹 | `与调试器共舞-lldb-的华尔兹.md` |
| 3 | Debugging Checklist | `debugging-checklist.md` | 调试核对清单 | `调试核对清单.md` |
| 4 | DTrace | `dtrace.md` | DTrace | `dtrace.md` |
| 5 | Activity Tracing | `activity-tracing.md` | 活动追踪 | `活动追踪.md` |

#### Issue #20 — Interviews（4 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-291631.md` | 卷首语 | `卷首语-960501.md` |
| 1 | A Generation of Lifelong Learners | `a-generation-of-lifelong-learners.md` | 终身学习的一代人 | `终身学习的一代人.md` |
| 2 | Something Slightly Less Terrible | `something-slightly-less-terrible.md` | 让东西变得不那么糟 | `让东西变得不那么糟.md` |
| 3 | Infinite Things to Learn | `infinite-things-to-learn.md` | 学无止境 | `学无止境.md` |

#### Issue #21 — Camera and Photos（10 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-8c1ef4.md` | 卷首语 | `卷首语-430e21.md` |
| 1 | How Your Camera Works | `how-your-camera-works.md` | 相机工作原理 | `相机工作原理.md` |
| 2 | Image Formats | `image-formats.md` | 图片格式 | `图片格式.md` |
| 3 | Camera Capture on iOS | `camera-capture-on-ios.md` | iOS 上的相机捕捉 | `ios-上的相机捕捉.md` |
| 4 | The Photos Framework | `the-photos-framework.md` | 照片框架 | `照片框架.md` |
| 5 | Photo Extensions | `photo-extensions.md` | 照片扩展 | `照片扩展.md` |
| 6 | An Introduction to Core Image | `an-introduction-to-core-image.md` | Core Image 介绍 | `core-image-介绍.md` |
| 7 | GPU-Accelerated Image Processing | `gpu-accelerated-image-processing.md` | GPU 加速下的图像处理 | `gpu-加速下的图像处理.md` |
| 8 | GPU-Accelerated Machine Vision | `gpu-accelerated-machine-vision.md` | GPU 加速下的图像视觉 | `gpu-加速下的图像视觉.md` |
| 9 | Face Recognition with OpenCV | `face-recognition-with-opencv.md` | 基于 OpenCV 的人脸识别 | `基于-opencv-的人脸识别.md` |

#### Issue #22 — Scale（6 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-4c6795.md` | 卷首语 | `卷首语-29146b.md` |
| 1 | Inside Omni | `inside-omni.md` | Omni 内部 | `omni-内部.md` |
| 2 | Artsy | `artsy.md` | Artsy | `artsy.md` |
| 3 | Scaling Square Register | `scaling-square-register.md` | Square Register 的扩张 | `square-register-的扩张.md` |
| 4 | The Art of Code Review: A Dropbox Story | `the-art-of-code-review-a-dropbox-story.md` | 代码审查的艺术：Dropbox 的故事 | `代码审查的艺术-dropbox-的故事.md` |
| 5 | React-Inspired Views | `react-inspired-views.md` | 响应式视图 | `响应式视图.md` |

#### Issue #23 — Video（4 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial-2d6484.md` | 卷首语 | `卷首语-d6eee6.md` |
| 1 | Capturing Video on iOS | `capturing-video-on-ios.md` | 在 iOS 上捕获视频 | `在-ios-上捕获视频.md` |
| 2 | Core Image and Video | `core-image-and-video.md` | Core Image 和视频 | `core-image-和视频.md` |
| 3 | Video Toolbox and Hardware Acceleration | `video-toolbox-and-hardware-acceleration.md` | 视频工具箱和硬件加速 | `视频工具箱和硬件加速.md` |

#### Issue #24 — Audio（5 篇）

| # | 英文原文 | `blogs/en/objcio/` | 中文译文 | `blogs/zh/objccn/` |
|---|---|---|---|---|
| 0 | Editorial | `editorial.md` | 卷首语 | `卷首语-d64a71.md` |
| 1 | The Audio Processing Dog House | `the-audio-processing-dog-house.md` | 音频处理的狗屋 | `音频处理的狗屋.md` |
| 2 | Functional Signal Processing Using Swift | `functional-signal-processing-using-swift.md` | 使用 Swift 进行函数式信号处理 | `使用-swift-进行函数式信号处理.md` |
| 3 | Play, Fail, Iterate: Sound Design for Products | `play-fail-iterate-sound-design-for-products.md` | 播放，失败，迭代：面向产品的音效设计 | `播放-失败-迭代-面向产品的音效设计.md` |
| 4 | Audio API Overview | `audio-api-overview.md` | 音频 API 一览 | `音频-api-一览.md` |

---

## 6. 对 `tools/html2md.py` 的改动，以及回归验证

体检过程中发现新源触发了 4 类结构问题，其中 3 类是**已有源也一直在踩**的静默丢内容。
全部已修，并对**第一批全部 17 个源、1736 篇**做了词元级回归核对。

### 6.1 Hexo NexT 主题的行号表格：每行是 `<div class="line">` 而不是 `<span class="line">`

`highlight_code()` 原来只找 `span.line`，找不到就退回 `td.code` 的 `text_content()`。
但 `<div>` 之间没有换行符，几十行 Swift 会被拼成**一行**。southpeak 用的正是 div 版。

改为 span / div 都认（按 class 的空白分隔 token 匹配 `line`）。已有的 onevcat（span 版）
输出零变化。

### 6.2 `<pre>` 下唯一 `<code>` 子元素时，取 `<code>` 的内容

objc.io 的模板写成：

```html
<pre>
								<code class="objc hljs">+ (UIColor *)boringColor;
```

`pre.text_content()` 会把模板那串制表符当成**第一行代码的缩进**，每个代码块首行都被推歪。
改成：`<pre>` 只有一个 `<code>` 子元素、且 `<pre>` 自身文本只有空白时，取 `<code>` 的内容
（`<pre><code>` 本来就是 HTML5 里代码块的规范写法）。

### 6.3 行内标签直接挂在块级容器下面时被整个丢掉（**影响全部 17 个已有源**）

原来的 `blocks()` 逐个子节点分派，`code` / `strong` / `em` / `sup` 这些行内标签
既不在 `BLOCK_TAGS` 也不在 `("span","a","center")` 里，会**掉到所有分支外面、直接丢弃**；
容器自己的 `el.text`（`<li>文字<code>x</code></li>` 里的「文字」）同样从来没被读过。
实测 sunnyxx 的一段：

```
改前： 1. 消息
改后： 1. 自定义的Top Level Objects收到`- init`消息
```

改法：`blocks()` 改成**攒行内缓冲区**——容器自身 text、行内标签、各节点的 tail 连续攒成一段，
遇到真正的块级元素或结束时才冲刷。同时把 `inline()` 拆出 `inline_el()`，
让块级路径能复用同一套行内渲染（不然 `<code>` 的反引号会丢）。

顺带修的两个小问题：`<sup>`/`<sub>` 现在渲染成 `2^31` / `1010~2`（原来直接拼接得到
「231」「10102」，是**错的数**）；HTML 注释（`<!-- enable-comments -->`、
`<!--[if lt IE 9]>`）不再当正文输出。

### 6.4 标题旁的空锚点永久链接

Hexo `a.headerlink` / Docusaurus `a.hash-link` / Rouge `a.anchor` 是空内容 + `#片段` 的
永久链接（浏览器里显示成一个图标）。原来会退回用 href 当链接文字，于是每个标题后面糊上一条
`## [#方案-A](#方案-A)方案 A`。改成：内容为空（零宽空格也算空）且 href 是纯片段 → 不输出。

### 6.5 回归验证结果

对第一批 17 个源全部重渲染，与改动前逐篇做**词元级**比对（`archived_at` 除外）：

| | 数量 |
|---|---|
| 比对篇数 | 1736 |
| **找回的正文词元** | **+71 084** |
| 删除的词元 | −7 430 |

删除的 7430 全部是噪声，逐条核对过来源：

- **−4004 `yulingtianxia` / −3243 `sunnyxx`**：标题旁的 `[#小节名](#小节名)` 锚点（6.4）
- **−127 `belkadan`**：`<!--more-->` 摘要标记、`aria-hidden="true"` 之类注释内容（6.3）
- **−21 `mikeash` / −13 `ibireme`**：`<!-- enable-comments -->`、
  `<!--[if lt IE 9]>…<![endif]-->` 条件注释（6.3）
- 其余零星同类

**没有任何一篇正文被削短**，`blogs/` 下无文件消失。三个点名的回归标的都在改善方向上：

| 源 | 结果 |
|---|---|
| `blogs/en/mikeash`（代码缩进） | 缩进零变化；找回 10 775 词元（行内 `code`/`strong`/`em` 与 `2^31` 上标） |
| `blogs/zh/ibireme`（Crayon 插件） | 代码块零变化；找回 6 词元，去掉 13 个条件注释词元 |
| `blogs/zh/onevcat`（Rouge 行号表格） | 代码块零变化；找回 9 226 词元 |

（改动 6.1 / 6.2 单独验证过：只加这两项时，17 个源 1736 篇输出**逐字节零差异**——
说明它们只对新结构生效，没有波及已有源。）

---

## 7. 已知局限

- `ciechanowski` 后期文章的 WebGL 交互演示无法转成 Markdown，只留文字与静态配图（站点特性，非抓取缺陷）
- `emergetools` 每篇头部保留了一行连排的标签串（如 `SwiftiOSPerformance`），Tailwind 原子类无法可靠定位，未剔
- `objcio` 的代码块没有语言标注：语言写在 `<code class="objc hljs">` 上，
  现有的 `language-/lang-/brush-/highlight-` 前缀规则匹配不到裸语言名。不影响内容，仅影响高亮
- `fbeng` 只取了站方 iOS 分类；`/category/android/` 未纳入
