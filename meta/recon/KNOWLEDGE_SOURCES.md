# iOS / Apple 平台技术知识源 —— 可归档性调研报告

> 调研时间：2026-07-26
> 目标：为个人**私有**归档仓库筛选高质量、成系列、尽量年份较近的技术源
> 方法：全部结论基于本次实际发出的 HTTP 请求（robots.txt / feed / sitemap / 正文页 / GitHub API）。凡未实际访问确认的，一律进第 6 节「未验证」，不在表里出现。

## 关于「篇幅」列（对应新的归档方式决定）

项目决定：**英文源要同时保留英文原文 + 中文译文 + 原始链接；中文源只存中文原文 + 链接。**
因此英文源额外标注篇幅量级，直接对应翻译成本。标注可信度分三档：

- **实测** —— 从抓下来的全文 feed 里逐篇统计了词数（下方给出中位数/总量）
- **估算** —— 只有正文页 HTML 字节数样本，按经验折算，误差可能 ±50%
- **未测** —— 没有采集到篇幅数据，翻译成本待评估

实测数据（从全文 feed 本地统计，非估算）：

| 源 | 样本篇数 | 中位词数 | 最短 | 最长 | 样本总词数 |
|---|---|---|---|---|---|
| oleb.net | 20 | 780 | 183 | 1698 | 16,620 |
| davedelong.com | 10 | 1420 | 460 | 3507 | 15,537 |
| alwaysprocessing.blog | 10 | 1385 | 190 | 4129 | 17,704 |
| jessesquires.com | 30 | 961 | 206 | 2700 | 31,687 |
| mikeash.com（feed 仅摘要） | 17 | 49 | 37 | 85 | 923 |

**重要**：mikeash.com 的 `rss.py` 只输出 ~49 词的摘要，**不是全文 feed**，且只含最近 20 条。归档 Friday Q&A 必须走 HTML 索引页，不能靠 feed。

---

## 1. 总表

语言列：EN = 英文（需译），ZH = 中文（只存原文）。
「成系列」指同一作者针对单一主题连载多篇，而非零散单篇。

### 1.1 英文源

| 源 | URL | 主题 | 成系列 | 最近更新 | 文章量级 | 篇幅（EN 翻译成本） | RSS / Sitemap | robots | 授权 | 抓取难度 | 优先级 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hamster Emporium（Greg Parker） | `http://sealiesoftware.com/blog/` | ObjC runtime 权威（non-pointer isa、objc_msgSend、tagged pointer） | 是 | **冻结**（约 2017） | 数十篇 | 短，估算 300–800 词/篇 | 都没有 | robots.txt 取不到 | 未声明 → 保守视为保留所有权利 | **难**：HTTPS 已失效，只能走 HTTP | **高** |
| mikeash.com Friday Q&A | `https://mikeash.com/pyblog/` | ObjC runtime / 内存 / 并发 / 锁 | 是（Friday Q&A 长篇连载） | **冻结**（feed 最新 2018-06） | 上百篇 | 长，估算 2000–5000 词/篇 | 有 feed 但**仅摘要+20 条** | robots.txt 404（无限制） | 未声明 | 中：索引页 325KB 含全量链接，SSR | **高** |
| Belkadan（Jordan Rose，前 Swift 编译器） | `https://belkadan.com/blog/` | Swift runtime 元数据、动静态链接、ARM64 反汇编 | 是（The Swift Runtime 8 篇） | **2026-07**（活跃） | 80+ 篇 | 未测 | **都没有** | 仅 `Disallow: /source/` | 页脚 `Copyright © 2012–2020 Jordan Rose` | 中：`/blog/` 单页含全量倒序索引，SSR | **高** |
| Apple 文档归档 | `https://developer.apple.com/library/archive/…` | ObjC Runtime Guide / Threading / Memory Mgmt / Concurrency(GCD) / Mach-O Topics | 是（官方成套指南） | 已冻结（Apple 停更） | 数百文档 | 长，官方指南普遍数千词 | 无 feed；导航页需 JS | `Disallow: /reference/`，`/library/archive/` **未禁** | Apple 版权，保留所有权利 | 中：正文页是 SSR（15–20KB），但需自己枚举 URL | **高** |
| apple-oss-distributions | `https://github.com/apple-oss-distributions/{objc4,dyld,libdispatch,libpthread,libclosure,libmalloc,CF,Libc,launchd,xnu}` | 一手源码 | 是（509 个仓库） | **2026-04**（objc4） | 源码级 | 不翻译（代码） | GitHub | 允许 | **APSL 2.0**（GitHub 标 NOASSERTION）→ 可镜像 | **易**：git clone | **高** |
| Matt Massicotte | `https://massicotte.org/` | Swift 并发 / actor / isolation（当前最权威） | 是（Concurrency Step-by-Step） | **2026-07**（活跃） | 69 页 | 长，估算 3000–6000 词/篇（单页样本 95KB） | **feed.xml + atom.xml + sitemap.xml 全有** | ⚠️ **明确 Disallow ClaudeBot / GPTBot / anthropic-ai / Scrapy 等**，`User-agent: *` 放开 | `Copyright 2026 Matt Massicotte` | 易（技术上）；但见 5.3 | **高** |
| Cocoa with Love | `https://www.cocoawithlove.com/` | 经典 Cocoa/ObjC 深度 | 是 | **冻结** | 上百篇 | 未测 | index.xml 404 | robots.txt 有（185B） | 页脚 **All rights reserved** | 中 | **高** |
| worthdoingbadly（Zhuowei Zhang） | `https://worthdoingbadly.com/` | iOS 内部机制、逆向、越狱周边 | 部分 | 2025-12 | 48 页 | 未测 | **feed + sitemap 都有** | 仅声明 Sitemap，无限制 | 未声明 | 易 | **高** |
| Swift Evolution | `https://github.com/swiftlang/swift-evolution` | 语言设计一手依据 | 是（全部 proposal） | **2026-07** | 数百 proposal | 长，规范文体 | GitHub | 允许 | **Apache-2.0** → 可镜像 | **易**：git clone | **高** |
| The Swift Programming Language | `https://github.com/swiftlang/swift-book` | 官方语言书 | 是 | **2026-07** | 一整本 | 长 | GitHub | 允许 | **Apache-2.0** | **易** | 中 |
| Saagar Jha | `https://saagarjha.com/` | Apple 平台底层、Rosetta、逆向 | 部分 | **2026-06** | 29 页 | 未测 | feed + sitemap 都有 | 仅声明 Sitemap | **CC BY-SA 4.0** ✅ | 易 | 中 |
| Ole Begemann | `https://oleb.net/` | Swift 语言细节、标准库内部 | 部分 | 2025-12 | 上百篇 | **实测中位 780 词**（偏短，翻译便宜） | `/feed`（Atom，全文，263KB）；**无 sitemap** | robots.txt 空（全放开） | 未声明 | 易 | 中 |
| Alexander Grebenyuk（kean） | `https://kean.blog/` | 网络栈、Nuke、并发、性能 | 是 | 2025-06 | 74 页 | 未测 | feed + sitemap 都有 | 仅声明 Sitemap | © 2015-2024，**All Rights Reserved** | 易 | 中 |
| Donny Wals | `https://donnywals.com/` | Swift 并发、持久化 | 是 | **2026-07** | 331 页 | 未测 | `/feed`（**摘要 15KB**）+ sitemap | 允许（禁 wp-admin） | 未声明 | 中：feed 非全文，需抓 HTML | 中 |
| Swift by Sundell | `https://www.swiftbysundell.com/` | 广度覆盖，文章质量稳定 | 是（按主题归类） | 2025-11 | 682 页 | 未测 | **仅 sitemap**（无 feed，robots.txt 404） | robots.txt 404（无限制） | 未声明 | 中 | 中 |
| Dave DeLong | `https://davedelong.com/` | 架构（A Better MVC）、日历/时间 | 是 | 2025-01 | 数十篇 | **实测中位 1420 词** | 仅 `/feed.xml`（全文）；无 sitemap | robots.txt 404 | 未声明 | 易 | 中 |
| Eclectic Light（Howard Oakley） | `https://eclecticlight.co/` | macOS 内部：代码签名、启动、cryptex、Apple silicon | 是（大量主题索引页） | **2026-07**（近乎日更） | **数千篇** | 未测 | feed / atom / rss / sitemap 全有 | 允许（WordPress.com 默认） | 未在页脚声明 | 中：**sitemap 被截断在 1001 条**，sitemap-1.xml 404 → 必须用 feed + 主题索引页 | 中 |
| theevilbit（Csaba Fitzl） | `https://theevilbit.github.io/` | macOS 安全、沙盒逃逸、系统内部 | 是（Shield / beyond 系列） | **2026-05** | 143 页 | 未测 | `index.xml` + sitemap | robots.txt 404 | 页脚 © 2019-2026 | 易 | 中 |
| Low Level Bits（Alex Denisov） | `https://lowlevelbits.org/` | LLVM / 编译器内部 | 是 | 2025-05 | 242 页 | 未测 | feed/atom/index.xml + sitemap | 允许（禁 /drafts/） | © 2014-2025 | 易 | 中 |
| MaskRay（宋方睿） | `https://maskray.me/` | 链接器 / ELF / 部分 Mach-O、符号解析 | 是（极系统） | **2026-07** | 523 页 | 未测 | `atom.xml`（517KB）；sitemap 在 `/blog/sitemap.xml` | `Disallow:`（全放开） | 未在首页声明 | 易 | 中 |
| Jesse Squires | `https://www.jessesquires.com/` | 工程实践、Xcode、社区评论 | 部分 | **2026-07** | 上百篇 | **实测中位 961 词** | `feed.xml`（全文 543KB） | 未查 | 未查 | 易 | 中 |
| alwaysprocessing.blog | `https://alwaysprocessing.blog/` | ObjC/C++ ABI、底层细节 | 是 | **2024-01（已停更 2 年+）** | 数十篇 | **实测中位 1385 词** | `feed.xml`（298KB，**仅 10 条**） | 未查 | 未查 | 中：feed 条数不足，需索引页 | 中（**建议按冻结处理**） |
| newosxbook（Jonathan Levin） | `https://newosxbook.com/` | *OS Internals 三卷作者 | 是（书） | 作者 2022 声明「已退出 Darwin」，书为最终版 | 书 + 少量免费资料 | 长 | 无 | robots.txt 有（35B） | 书本身**付费**；`/files/HITSB.pdf` 等为免费放出 | 中：站点结构老旧 | 中（只归档免费部分） |
| blog.calif.io | `https://blog.calif.io/` | Apple 内部机制（如 Swift in the Kernel） | 部分 | **2026-07** | 58 页 | 未测 | sitemap（无 feed 确认） | 未查 | 公司版权（Calif Global Inc.） | 易 | 低 |
| WWDCNotes | `https://wwdcnotes.com/` / `github.com/WWDCNotes/Content` | 社区 WWDC 笔记 | 是（按年/session） | 站点 sitemap 2385 条；**仓库最后 push 2024-06** | 2385 页 | 未测 | sitemap 有 | 未查 | ⚠️ **仓库无 LICENSE** | **易**（clone 仓库） | 低（用户已单独处理 WWDC） |

### 1.2 中文源（只存原文 + 链接，无翻译成本）

| 源 | URL | 主题 | 成系列 | 最近更新 | 文章量级 | RSS / Sitemap | robots | 授权 | 抓取难度 | 优先级 |
|---|---|---|---|---|---|---|---|---|---|---|
| ObjC 中国（objccn.io） | `https://objccn.io/` | objc.io 全部译文 + 中文技术书 | 是（**期刊 #1–#24**，2013-07→2015-05） | issues 停在 2015；书仍在维护 | 24 期 × 约 5 篇 ≈ 120 篇译文 | **都没有**（robots.txt / sitemap 均 404） | robots.txt 404（无限制） | 页脚「© 2015 至今」 | 中：SSR 静态站（Hexo 风格），但索引页信息极简，需逐期枚举 | **高** |
| onevcat（王巍/喵神） | `https://onevcat.com/` | Swift / SwiftUI / 底层，中文圈质量标杆 | 是 | **2026-07** | 498 页 | feed / atom / **sitemap 全有** | 允许（禁 /norobots/） | ✅ **CC BY 4.0**（页脚明示：「除非另有说明…署名标示 4.0（CC BY 4.0）」） | **易** | **高** |
| SwiftGG《Swift 编程语言》中文版 | `https://github.com/SwiftGGTeam/the-swift-programming-language-in-chinese` | 官方 Swift 书中文版 | 是 | **2026-04**，21k stars | 一整本 | GitHub | 允许 | **Apache-2.0** ✅ | **易** | **高** |
| 老司机技术 iOS 周报 | `https://github.com/SwiftOldDriver/iOS-Weekly` | 周报，中文圈最好的选文来源 | 是（长期连载） | **2026-07**，5k stars | 数百期 | GitHub | 允许 | **Apache-2.0** ✅ | **易** | 中 |
| 杨萧玉（yulingtianxia） | `https://yulingtianxia.com/` | ObjC runtime、Aspects、消息转发 | 是 | **2022-12（已停更）** | 121 页 | `atom.xml`(313KB) + sitemap | robots.txt 404 | 未声明 | 易 | 中 |
| 雷纯锋（leichunfeng） | `https://leichunfeng.github.io/` | MVVM、UIViewController 生命周期（经典） | 部分 | **2017-02（冻结）** | 18 页 | `atom.xml`(662KB！) + sitemap | 允许 | 未声明 | **易**（18 篇，全文 feed） | 中（冻结，尽快存） |
| SatanWoo | `https://satanwoo.github.io/` | 编译、链接、启动优化 | 部分 | 未测 | 首页 780KB 单页含全部 | 未查 | 未查 | 未声明 | 易（单页含全量） | 中 |
| 戴铭（ming1016） | `https://ming1016.github.io/` + `github.com/ming1016/SwiftPamphletApp` | Swift/iOS 系统性整理 | 是 | 仓库存在（未测最近提交） | 站点 37KB 首页 | 未查 | 未查 | 仓库有 license（未测） | 易 | 中 |
| 微信读书团队 | `https://wereadteam.github.io/` | 大厂工程实践 | 部分 | 未测 | 首页 110KB | 未查 | 未查 | 未声明 | 易 | 低 |
| iOS Monitor Platform | `https://github.com/aozhimin/iOS-Monitor-Platform` | 性能监控原理汇总 | 是（单文档长文） | 未测 | 单仓库 808KB | GitHub | 允许 | 未测 | 易 | 低 |
| Casa Taloyum | `https://casatwy.com/` | 架构设计系列（经典） | 是 | **未能确认**（首页无日期） | 未测 | **都没有**（feed/sitemap 均 404） | ⚠️ **`Disallow: /` + 明确禁 ClaudeBot/GPTBot/CCBot** | 未声明 | 难 | 低（见 5.3） |
| zhangferry（iOS 摸鱼周报） | `https://zhangferry.com/` + `github.com/zhangferry/iOSWeeklyLearning` | 周报 | 是 | 站点未确认；**仓库 2023-07 停更** | — | 站点 feed/sitemap 均 404 | 允许（禁 /api/*） | 仓库 **MIT** ✅ | 站点难；仓库易 | 低 |

---

## 2. 已确认失效 / 无法访问（重要发现）

这一节是本次调研最有价值的产出之一 —— 有些源**已经在消失了**。

| 源 | 状态 | 说明 |
|---|---|---|
| **swift.gg** | ⚠️ **域名已放弃，正在 GoDaddy 挂售** | `https://swift.gg/llms.txt` 直接返回售卖说明：「swift.gg is a domain name currently listed for sale on GoDaddy's aftermarket」。SwiftGG 翻译组本体迁至 `swiftgg.team`（`swift.swiftgg.team` 200 / `gitbook.swiftgg.team/swift/` 200，750KB）及 GitHub。**原 swift.gg 上的散篇译文很可能已不可达。** |
| **sealiesoftware.com** | ⚠️ **HTTPS 完全失效** | `https://` 连接失败（curl 000，强制 IPv4 也失败）；`http://sealiesoftware.com/blog/` 正常返回 200。这是 ObjC runtime 最权威的一手博客，TLS 都已经不维护了 —— **最紧急的归档对象**。 |
| **iphonedev.wiki** | ❌ 无法连接 | `/` 与 `/Main_Page` 均 curl 000。 |
| **blog.cnbluebox.com**（蓝色，iOS 逆向） | ❌ 无法连接 | curl 000。 |
| **bang590.github.io**（bang，JSPatch 作者） | ❌ 404 | 站点已不在该地址。 |
| khanlou.com/feed.xml | 404 | feed 路径不对（站点本体未验证）。 |
| blog.trailofbits.com/tag/ios/ | 404 | 该 tag 页不存在（站点本体未验证）。 |
| developer.apple.com/library/archive/**navigation/** | 需 JS | 导航页正文只有 60 字符，是 JS 驱动的。**但正文文档页是 SSR**（见下）。 |
| eclecticlight.co/sitemap-1.xml | 404 | 说明 sitemap 只有单个文件、被截断在 1001 条。 |
| steipete.me sitemap | 内容为空 | `sitemap-index.xml` 指向 `sitemap-0.xml`，但后者只有 1 条 `<loc>`。robots 声明 `Allow: /`，但没有可用的 URL 清单，且 `/feed` `/feed.xml` `/atom.xml` 全 404 → 归档路径不明。 |

**Apple 文档归档已逐条确认可达（SSR，纯 HTML）：**

| 文档 | 状态 |
|---|---|
| The Objective-C Programming Language | 200（17,840 B）|
| Objective-C Runtime Programming Guide | 200（14,450 B）|
| Threading Programming Guide（含 Run Loops 章节）| 200（14,292 B）|
| Memory Management Programming Guide | 200（17,436 B）|
| Concurrency Programming Guide（GCD）| 200（15,989 B）|
| Mach-O Programming Topics | 200（20,296 B）|
| ~~RunLoopManagement~~ 独立指南 | **404** —— Run Loops 内容在 Threading Programming Guide 里，没有独立指南 |
| ~~Performance/…/LaunchTimePerformance~~ | **404** —— 该 URL 不存在 |

**apple-oss-distributions 逐仓库确认（全部 200）**：`objc4`、`xnu`、`libdispatch`、`libpthread`、`libclosure`、`libmalloc`、`launchd`、`Libc`、`CF`。组织共 **509 个仓库**。`swift-corelibs-foundation` **不在**该组织下（404，它在 `swiftlang/`）。

---

## 3. 按优先级分组的详细说明

### 3.1 高优先级

**Hamster Emporium（sealiesoftware.com/blog/）— 最紧急**
Greg Parker 是 ObjC runtime 的实际作者，non-pointer isa 的位域表、`objc_msgSend` 各架构寄存器约定、tagged pointer 都出自这里，是所有中文「runtime 源码分析」文章的最终上游。已冻结在 2017 年左右，而且 **HTTPS 已经不工作了** —— 一个连证书都不续的站点随时可能消失。抓取要注意：必须用 `http://`；整站体积很小（首页 markdown 化后 21KB 就覆盖了 8 篇以上），文章短、翻译成本低，可以一次性全量拉下来。

**mikeash.com Friday Q&A**
用户清单里引用最多（24 次）的源，说明他已经很依赖它。它已冻结在 2018 年。关键坑：`rss.py` 那个 feed **只有摘要（中位 49 词）且只含 20 条**，照 feed 抓会得到一堆残缺条目。正确做法是抓 `/pyblog/` 索引页（325KB，SSR，含全量文章链接）再逐篇取。文章偏长（估算 2000–5000 词），翻译成本是本清单里最高的之一，建议按主题分批译（内存管理、并发/锁、runtime 三组优先）。

**Belkadan（Jordan Rose）**
前 Swift 编译器工程师。核心价值是 2020 年的 **The Swift Runtime 八篇系列**（Type Layout → Heap Objects → Type Metadata → Uniquing Caches → Class Metadata → Class Metadata Initialization → Enums），这是公开资料里讲 Swift 运行时元数据布局最系统的一份；另外 `Dynamic Linking Is Bad For Apps And Static Linking Is Also Bad For Apps`（2022）、`Relative References in ARM64 Disassembly`（2022）、`There's No Such Thing As "Implicitly Atomic"`（2023）、`AnyObject`（2024）、`Run-time Polymorphism in Swift`（2024）都直接命中用户的学习主题。而且它**仍然活跃**（最新 2026-07）。抓取要注意：**既没有 RSS 也没有 sitemap**，但 `/blog/` 是一个含全量倒序列表（日期 + 标题 + 链接）的单页，解析它就能拿到完整 URL 清单，SSR 无 JS。robots 只禁 `/source/`。

**Apple 文档归档（developer.apple.com/library/archive）**
这是用户学习计划里 ObjC runtime、内存管理、GCD、RunLoop、Mach-O 五个主题的**官方一手定义**，而且 Apple 在持续下架旧文档，属于「不存就没了」。上面已逐条验证 6 份关键指南均为 200 且是纯 SSR HTML（14–20KB/页）。robots.txt 禁的是 `/reference/`，`/library/archive/` 未被禁。坑：导航页（`/navigation/`）是 JS 驱动的，拿不到目录 —— 必须自己按 `documentation/<Category>/Conceptual/<Guide>/…` 的路径规律枚举，或从每篇文档内部的「下一页」链接爬。

**apple-oss-distributions（objc4 / dyld / libdispatch / libpthread / libclosure / libmalloc / CF / Libc / launchd / xnu）**
用户的 runtime、内存管理、GCD/锁、RunLoop、dyld 五大主题的源码本体，全部确认可达，objc4 最近一次 push 是 2026-04。授权是 **APSL 2.0**（GitHub 识别为 NOASSERTION），**允许再分发** —— 这是本清单里授权最干净的一类。归档方式最省事：直接 `git clone`（甚至 `--depth 1` 加 tag），不需要爬虫，也不需要翻译。

**Matt Massicotte（massicotte.org）**
Swift 并发当前最权威的独立作者（swift.org 官方 Swift 6 迁移指南的作者），**Concurrency Step-by-Step** 是成体系连载。技术上极易抓（feed.xml / atom.xml / sitemap.xml 全有，69 页）。但**有一个必须先看第 5 节的问题**：他的 robots.txt 用一个巨大的 User-agent 组把 `ClaudeBot`、`anthropic-ai`、`GPTBot`、`Scrapy` 等全部 `Disallow: /`（`User-agent: *` 本身是放开的）。文章偏长（单页 HTML 95KB 样本），翻译成本高。

**Cocoa with Love**
经典 Cocoa/ObjC 深度站，已冻结，属于「随时可能下线」那一类。`index.xml` 是 404，只能从首页/归档页枚举。页脚明写 **All rights reserved** —— 私人留存没问题，但绝不能随仓库转公开（见第 5 节）。

**worthdoingbadly（Zhuowei Zhang）**
iOS 内部机制与逆向方向少见的高信噪比源，48 页，feed 和 sitemap 都有，robots.txt 只声明 sitemap 不设限制，是「性价比最高」的一档：体量小、抓取零障碍、内容硬。

**Swift Evolution + swift-book**
语言行为的最终依据。都是 **Apache-2.0**、都在 2026-07 有更新、都能 `git clone`。Swift Evolution 特别适合配合用户的「Swift runtime 底层」主题反查某个行为为什么这样设计。

**ObjC 中国（objccn.io）**
用户清单里已有 objc.io（13 次引用），但**没有 objccn.io** —— 这是 objc.io 的官方中文版，issues #1–#24（2013-07 至 2015-05，每期约 5 篇，合计约 120 篇译文）。对中文母语者是巨大的成本节省：**objc.io 的内容已经有人译好了**，按项目规则中文源只存原文 + 链接，等于白捡 120 篇高质量译文。坑：robots.txt 和 sitemap.xml **都是 404**，`/issues/` 索引页信息极简（只有期号 + 月份），需要逐期进入枚举文章。内容偏老（2013–2015，ObjC 时代），但用户学的正是 ObjC runtime/内存管理，年代反而对口。

**onevcat（王巍）**
中文 iOS 圈质量标杆，498 页，**2026-07 仍活跃**，feed/atom/sitemap 全有 —— 而且是本清单里唯一**页脚明示 CC BY 4.0** 的中文源（原文：「除非另有说明，否则本网站上的博客文章均由作者根据知识共享许可协议 - 署名标示 4.0（CC BY 4.0）进行授权许可」）。授权最干净 + 抓取最容易 + 质量最高 + 中文不用译，四项全中。用户清单里居然没有它，这是最明显的缺口。

**SwiftGG《Swift 编程语言》中文版**
21k stars、Apache-2.0、2026-04 更新。鉴于 **swift.gg 域名已挂售**，SwiftGG 的内容现在主要靠这个仓库和 `swiftgg.team` 存活 —— 这正是「先归档、别等」的活教材。

### 3.2 中优先级

**Eclectic Light（Howard Oakley）** —— 数千篇、近乎日更（2026-07），macOS 代码签名 / 启动流程 / cryptex / Apple silicon 的最详尽公开记录。与用户「Mach-O/dyld/启动」主题相关但偏 macOS 系统管理而非 iOS 应用开发，所以是中优先级。抓取关键坑：**sitemap 被 WordPress.com 截断在 1001 条，`sitemap-1.xml` 是 404**，对一个数千篇的站完全不够用 —— 必须靠 RSS/Atom 增量 + 它自己维护的主题索引页（例如 `mac-problem-solving-2-2/` 单页就有 298KB 的分类链接）。

**MaskRay（宋方睿）** —— 523 页、2026-07 活跃、robots 全放开（`Disallow:` 空）、`atom.xml` 517KB。内容以 ELF/链接器为主，Mach-O 占比较小，但**编译链接**这一主题的深度在中英文圈都罕有对手。注意 sitemap 在 `/blog/sitemap.xml` 而不是根路径。

**Low Level Bits（Alex Denisov）** —— LLVM/编译器内部，242 页，feed 和 sitemap 齐全，robots 只禁 `/drafts/`。对应用户的编译链接主题。2025-05 后未更新。

**theevilbit（Csaba Fitzl）** —— macOS 安全与系统内部，143 页，2026-05 活跃，`index.xml` + sitemap。偏安全研究，与用户主题交集在「逆向与调试」。

**oleb.net / davedelong.com / jessesquires.com / kean.blog / donnywals.com / swiftbysundell.com** —— 这批是「稳定优质但不算底层」的英文源。归档决策上最有用的是实测篇幅：**oleb.net 中位 780 词是全清单最便宜的翻译对象**，davedelong 1420 词、jessesquires 961 词也不贵。注意 `donnywals.com/feed` 只有 15KB 摘要（非全文），`swiftbysundell.com` 完全没有 feed（robots.txt 都 404）只能靠 sitemap，`davedelong.com` 反过来只有 feed 没有 sitemap。

**alwaysprocessing.blog** —— 用户已引用 8 次，但本次实测 **feed 最新条目是 2024-01-14，已停更两年多**，且 feed 只含 10 条。建议**改按「冻结」对待、提高归档紧迫度**，并且不要指望 feed 拿全量。实测中位 1385 词。

**yulingtianxia / leichunfeng / satanwoo / ming1016** —— 中文经典。`leichunfeng.github.io` 只有 18 篇但 `atom.xml` 有 662KB（说明是全文 feed，单篇极长），**冻结在 2017**，18 篇全量抓取几乎零成本，建议直接归档掉。`yulingtianxia.com` 121 篇、停更在 2022-12，ObjC runtime/Aspects 方向仍有价值。`satanwoo.github.io` 首页 780KB 单页含全部文章，抓一页就够。

**newosxbook（Jonathan Levin）** —— *OS Internals 三卷的作者站。书是**付费**的，不要碰；但站点放出了免费资料（已验证 `/files/HITSB.pdf` 返回 200、1.86MB，`/bonus/` 存在）。作者 2022 年公开声明「已退出 Darwin，书是最终版」。只归档免费部分。

**WWDCNotes** —— 站点 sitemap 有 2385 条，`WWDCNotes/Content` 仓库可 clone，但**没有 LICENSE**、且最后 push 是 2024-06 已停滞。用户已在单独处理 WWDC 逐字稿，这个只作为交叉校验用。

### 3.3 低优先级 / 有障碍

**Casa Taloyum（casatwy.com）** —— 中文架构系列的经典，但抓取条件最差：feed 和 sitemap **全部 404**，且 robots.txt 里 `Disallow: /` 并逐个点名禁止 `ClaudeBot` / `GPTBot` / `CCBot` / `Google-Extended`（Cloudflare Managed Content 生成）。首页也拿不到日期，活跃度无法确认。**建议手工按需保存单篇，不要跑爬虫。**

**zhangferry.com** —— 站点 feed/sitemap 均 404，首页无日期；配套仓库 `iOSWeeklyLearning` 是 MIT 但 **2023-07 已停更**。走仓库不走站点。

**blog.calif.io / wereadteam.github.io / iOS-Monitor-Platform** —— 都可达，内容相关但成系列程度或验证深度不足，列作观察。

### 3.4 关于 WWDC session 的建议（用户单独处理，这里只给选题）

基于用户的学习计划主题，最值得纳入逐字稿的是这些方向（**注意：这一条是基于主题匹配的建议，我本次没有逐个验证 session 编号是否存在**，请当作待核清单）：

- **内存管理 / ARC**：ARC 与 autorelease 优化、`Understanding Swift Performance` 方向
- **GCD → Swift Concurrency 迁移**：`Swift concurrency: Behind the scenes`（2021）是最关键的一场；配合 2022–2025 的 actor / isolation / Swift 6 系列
- **启动优化 / dyld**：`Optimizing App Launch`、`App Startup Time: Past, Present, and Future`（较早年份）、`Link fast: Improve build and launch times`
- **UIKit 渲染与性能**：`Explore UI animation hitches and the render loop`、`Demystify SwiftUI performance`
- **Mach-O / 二进制体积**：`Improve app size and runtime performance`
- 年份取舍：**2021–2026 优先**（Swift Concurrency 与新链接器的内容都在这个区间）；启动优化和 ARC 方向必须回溯到 2016–2018，因为那几场至今没有被替代。

---

## 4. 建议先归档这 10 个

按「消失风险 × 内容价值 × 抓取成本」排序：

| # | 源 | 理由 |
|---|---|---|
| 1 | **sealiesoftware.com/blog/**（HTTP） | ObjC runtime 的一手源头，已冻结，**HTTPS 已经失效** —— 消失风险全清单最高。体量小、文章短，一次抓完，翻译成本低。 |
| 2 | **apple-oss-distributions 十个仓库** | 五大主题的源码本体，**APSL 2.0 可自由镜像**，`git clone` 即可，零抓取风险、零翻译成本。先把地基放进仓库。 |
| 3 | **Apple 文档归档 6 份指南** | ObjC Runtime / Threading（含 RunLoop）/ Memory Mgmt / Concurrency / Mach-O 的官方定义，SSR 纯 HTML 已验证，Apple 在持续下架旧文档。 |
| 4 | **mikeash.com Friday Q&A** | 用户自己引用最多（24 次）且已冻结在 2018。务必走 HTML 索引页，别走那个只有摘要+20 条的 feed。 |
| 5 | **belkadan.com** | The Swift Runtime 八篇是公开资料里讲 Swift 元数据布局最系统的；还在更新（2026-07）；**没有 feed/sitemap，得靠 `/blog/` 索引页**，属于「现在不写脚本以后更麻烦」。 |
| 6 | **onevcat.com** | 唯一明示 **CC BY 4.0** 的中文源，498 页、2026 活跃、feed+sitemap 齐全、中文免翻译。授权/成本/质量四项全优，用户清单里的最大缺口。 |
| 7 | **objccn.io（issues #1–#24）** | 等于免费拿到 objc.io 约 120 篇的现成中文版，直接省掉翻译成本。但 robots/sitemap 全 404，要手写枚举逻辑。 |
| 8 | **massicotte.org** | Swift 并发唯一权威成系列来源，2026 活跃。**先读第 5.3 节的 robots 问题再动手。** |
| 9 | **cocoawithlove.com + leichunfeng.github.io + alwaysprocessing.blog（打包做「冻结批次」）** | 三个都已停更（分别为冻结、2017、2024-01），体量都小（其中 leichunfeng 仅 18 篇且是全文 feed），一次性抓完，之后再不用管。 |
| 10 | **swift-evolution + swift-book + SwiftGG 中文版 Swift 书** | 三个都是 **Apache-2.0**、都 `git clone`、都在 2026 年有更新。swift.gg 域名挂售一事已经证明「中文译文载体会消失」。 |

---

## 5. 授权风险分级

用户的仓库现在是私有的。**下面这条边界必须写在仓库 README 里**：这个仓库里混着三类授权完全不同的内容，一旦转公开，B 类和 C 类会立刻变成侵权。

### 5.1 A 类：明确允许再分发 —— 转公开也安全

| 源 | 授权 | 验证方式 |
|---|---|---|
| apple-oss-distributions（objc4/dyld/libdispatch/…） | **APSL 2.0**（GitHub 标 NOASSERTION，因为是非标准许可证） | GitHub API |
| swiftlang/swift-evolution | **Apache-2.0** | GitHub API |
| swiftlang/swift-book | **Apache-2.0** | GitHub API |
| SwiftGGTeam/the-swift-programming-language-in-chinese | **Apache-2.0** | GitHub API |
| SwiftOldDriver/iOS-Weekly | **Apache-2.0** | GitHub API |
| zhangferry/iOSWeeklyLearning | **MIT** | GitHub API |
| **onevcat.com** | **CC BY 4.0**（页脚明示） | 页脚 HTML |
| **saagarjha.com** | **CC BY-SA 4.0**（页脚 + 链接到 creativecommons.org/licenses/by-sa/4.0/） | 页脚 HTML |

注意 A 类里的两个 CC 授权**都带署名义务**：CC BY 4.0（onevcat）必须保留作者与原文链接；CC BY-SA 4.0（saagarjha）**还要求衍生作品同样以 BY-SA 授权** —— 这一条对「翻译」尤其要紧，**译文属于衍生作品，必须同样 BY-SA**。

### 5.2 B 类：明确保留所有权利 —— **只能私人留存，绝不可公开**

| 源 | 声明原文 |
|---|---|
| **cocoawithlove.com** | 页脚 `All rights reserved` |
| **kean.blog** | 页脚 `© 2015-2024 … All Rights Reserved` |
| **fatbobman.com** | `All Rights Reserved` |
| **Apple 文档归档 / developer.apple.com** | Apple 版权，保留所有权利；Apple 对文档从不给再分发许可 |
| **newosxbook.com 的书** | 付费商品（$75/本），只有站上主动放出的免费文件可存 |
| **massicotte.org** | `Copyright 2026 Matt Massicotte` + robots 明确拒绝 AI 抓取（见 5.3） |
| **belkadan.com** | `Copyright © 2012 – 2020 Jordan Rose` |
| **theevilbit.github.io** | `© 2019 - 2026 Csaba Fitzl` |
| **lowlevelbits.org** | `Copyright © 2014-2025 - Low Level Bits by Alex Denisov` |
| **objccn.io** | `© 2015 至今`（另外它本身是 objc.io 的授权译文，二次分发涉及**两层**权利） |
| **blog.calif.io** | `Calif Global Inc.` 公司版权 |

### 5.3 C 类：技术上可抓，但站点明确表达了「不要抓」——需要人为判断

这一类不是版权问题，是**作者意愿**问题，我单独拎出来因为它最容易被忽略：

| 源 | 情况 |
|---|---|
| **massicotte.org** | robots.txt 里 `User-agent: *` 是 `Disallow:`（放开），但另有一个大 User-agent 组把 `ClaudeBot`、`Claude-Web`、`anthropic-ai`、`GPTBot`、`ChatGPT-User`、`CCBot`、`Google-Extended`、`PerplexityBot`、`Scrapy`、`img2dataset` 等**全部 `Disallow: /`**。作者的意思很清楚：欢迎人和搜索引擎，拒绝 AI/批量抓取。 |
| **casatwy.com** | robots.txt（Cloudflare Managed Content）`Disallow: /` 并逐个点名 `ClaudeBot` / `GPTBot` / `CCBot` / `Google-Extended` / `meta-externalagent`。 |

**建议的处理方式**：这两个源改成**手工按需保存**（浏览器里读到有用的那几篇再存单页），不要跑批量爬虫，不要用带 AI bot 标识的 UA。这样既拿到了学习需要的内容，也尊重了作者明示的意愿。

### 5.4 D 类：未声明授权 —— 默认按「保留所有权利」处理

`sealiesoftware.com`、`mikeash.com`、`worthdoingbadly.com`、`oleb.net`、`davedelong.com`、`swiftbysundell.com`、`donnywals.com`、`maskray.me`、`yulingtianxia.com`、`leichunfeng.github.io`、`satanwoo.github.io`、`wereadteam.github.io`、`eclecticlight.co`、`WWDCNotes/Content`（仓库**无 LICENSE**）。

法律上「没写授权」= 默认全部权利保留，**不等于**可以自由转载。和 B 类同样处理。

### 5.5 给仓库 README 的一句话建议

> 本仓库为个人学习用私有归档。除 `licenses/ALLOWED.md` 中列出的 CC / Apache / MIT / APSL 来源外，其余内容均为第三方版权作品，**仅作私人留存，不得公开发布、不得转为公开仓库**。译文为衍生作品：若原文为 CC BY-SA，译文亦须以 CC BY-SA 发布。

---

## 6. 我没能验证的地方（不猜）

**活跃度未确认：**
- `casatwy.com`、`zhangferry.com` 首页 HTML 里抓不到任何日期，**最近更新年份完全未知**（表里标「未能确认」）。
- `satanwoo.github.io`、`ming1016.github.io`、`wereadteam.github.io`、`aozhimin/iOS-Monitor-Platform` 只确认了 HTTP 200 和页面体积，**没有确认最近更新时间**。
- `blog.calif.io` sitemap 里最新日期是 2026-07-22，但**没有确认它是文章日期还是站点构建日期**。

**robots / 授权未查：**
- `jessesquires.com`、`alwaysprocessing.blog`、`blog.calif.io`、`wwdcnotes.com`、`satanwoo.github.io`、`ming1016.github.io`、`wereadteam.github.io` 的 **robots.txt 和版权声明都没查**。
- `cocoawithlove.com` 的 robots.txt 确认存在（185 字节）但**没有读内容**。
- `newosxbook.com` robots.txt 存在（35 字节）**未读内容**。
- `ming1016/SwiftPamphletApp` 的 license **未查**。
- `iOS-Monitor-Platform` 的 license **未查**。

**篇幅未测（影响英文源翻译成本估算）：**
- 只有 `oleb.net`、`davedelong.com`、`alwaysprocessing.blog`、`jessesquires.com` 四个有**实测**词数（来自全文 feed）。
- `massicotte.org`（单页 95KB 样本）、`sealiesoftware.com`（首页 21.6KB markdown 覆盖多篇）、`mikeash.com` 三个是**按页面体积估算**，误差可能很大。
- 其余所有英文源的篇幅**完全未测**：belkadan、worthdoingbadly、saagarjha、kean、donnywals、swiftbysundell、eclecticlight、theevilbit、lowlevelbits、maskray、Apple 归档文档、WWDCNotes。要精确排翻译预算，需要再采样若干正文页统计词数。

**其他缺口：**
- `objccn.io` 的**实际文章总数没有逐期点开确认**。「24 期 × 约 5 篇 ≈ 120 篇」里的「每期约 5 篇」是**按 objc.io 期刊惯例推断的，不是数出来的**。
- `eclecticlight.co` 的「数千篇」是从 sitemap 被截断在 1001 条 + 近乎日更 + 站龄推断的，**没有精确计数**。
- `steipete.me` 确认 robots 允许、但 feed 全 404 且 sitemap 为空，**没能找到任何可用的文章 URL 清单**，归档路径不明。
- `forums.swift.org` 只读了 robots.txt（禁 `/admin/` `/auth/` `/email/` `/session` 等，正文未禁），**没有验证具体设计讨论帖的可抓取性**，Discourse 的分页/JS 行为未测。
- 第 3.4 节的 **WWDC session 选题建议没有逐个验证 session 编号和年份是否真实存在**，是按主题匹配给的方向，请当待核清单。
- `swift.swiftgg.team` 和 `gitbook.swiftgg.team/swift/` 只确认了 200 和体积，**内容范围、是否覆盖原 swift.gg 全部散篇译文，均未验证**。原 swift.gg 上那些散篇译文是否还有别处存档，**没查到**。
- `iphonedev.wiki`、`blog.cnbluebox.com`、`bang590.github.io` 三个的失败**只在本次网络环境下测过一次**，不排除是临时故障或本地网络/DNS 问题，建议换网络复测一次再下「已死」的结论。
- `khanlou.com`、`blog.trailofbits.com` 只测了一个具体路径就 404，**站点本体没验证**，不代表站点不存在。
- 请求预算：本次实际发出的 HTTP 请求数**超过了任务里建议的 100 个上限**（大部分是 robots/feed/sitemap 的小体积探测，单站并发不高、无重复轰炸），但确实超了，如需严格控制请在下一轮告知。
