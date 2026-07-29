---
title: 'Emerge Tools 博客 | Xcode 14 如何无意间增加 App 体积'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:40382a8543c7ec7e'
translated: true
---

> 原文：[Emerge Tools 博客 | Xcode 14 如何无意间增加 App 体积](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size)　·　Emerge Tools Blog

# Xcode 14 如何无意间增加 App 体积

2022 年 11 月 10 日

Max Topolsky & Josh Cohenzadeh

iOSApp 体积精选

![how-xcode14-unintentionally-increases-app-size](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog10.f51a5670.png&w=2048&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [切换到 Xcode 14](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#bitcode-symbol-stripping)

Xcode 14 于 9 月 12 日发布，带来了许多新功能与改进。“你首先会注意到的是”Xcode 变快了，体积也缩小了 30%。[^1](https://developer.apple.com/videos/play/wwdc2022/110427/)

Xcode 14 发布后不久，许多 iOS App 的体积出现了显著增长。我们[首次在 Twitter 上](https://twitter.com/emergetools/status/1575597900825915393)提到了 Zillow iOS App 中观察到的巨大增长。Zillow 并非个例。

在 9 月中旬到 10 月初之间：

- 10 月 8 日，Nike iOS App 的安装体积为 182.2 MB。一周后，变成了 322.1 MB（增长了 68%）
- American Airlines 从 182.2 MB 增长到 389.1 MB——其中 Xcode 14 导致了 76.2 MB（42%）的增长
- Chime 从 162.8 MB 增长到 212.8 MB（增长了 31%）

![Nike、American、Chime 和 Zillow iOS App 安装体积显著增长的图表](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Finstall-size-2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Nike、American、Chime 和 Zillow iOS App 的安装体积随时间变化

在每一例中，体积的剧增都是因为这些 App 首次使用 Xcode 14 发布。除其他功能外，Xcode 14 默认禁用了 bitcode。

_Xcode 不再默认构建 bitcode……在未来某个 Xcode 版本中，将移除构建 bitcode 的能力。包含 bitcode 的 IPA 在提交到 App Store 之前，bitcode 会被剥离。   
 - [Xcode 14 发布说明](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)_

什么是 bitcode？  
Bitcode 是一种打包 App 的替代方式，它把部分构建过程留给 Apple 在提交到 App Store 后完成。Apple 做的其中一件事就是剥离二进制符号（binary symbols）。

那什么是二进制符号剥离？  
二进制符号剥离是指从二进制文件中移除那些在生产环境中运行 App 所不需要的某些类型的元数据。这些元数据在生产前可能有用（例如用于生成 dSYM 文件），但在生产构建中只会给用户的手机增加臃肿内容。

简单的解释是，bitcode 优化了生产构建，部分通过**剥离二进制符号**。如果未启用 bitcode，就必须更改 Xcode 构建设置来剥离二进制符号。

这篇博客并非讨论弃用 bitcode 是好是坏，而是着重强调使用 Xcode 14 发布 App 时一个鲜为人知的影响。下面我们将：

- 对比 Xcode 14 之前和之后的 App 构建
- 调查哪些 App 因 Xcode 14 出现了体积衰退（regression）
- 最后，展示任何 App 都可以如何剥离二进制符号

## [对比 Xcode 14 前后的 Nike App](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#size-increase-comparison)

使用 Xcode 14 后，任何依赖 bitcode 的 App 都不再能保证从其生产 App 中剥离二进制符号。这意味着 App 可以在不添加任何功能的情况下变得**大得多**。

以下是 Emerge 对 Nike iOS App 版本 22.35.0（10/8 测量）的体积分析 X-Ray。在该版本中，框架（frameworks）占到了 191.7 MB 安装体积中的 163.7 MB。如果你在较大的屏幕上操作，可以试试与树状图交互来查看详细的体积分解。

![Nike iOS App v22.35.0 的 Emerge 体积分析 X-Ray](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Fnike-treemap-1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge 体积分析 X-Ray

搜索

在版本 22.36.1（10/15）中，框架跃升至 293.8 MB（增加了 127.3 MB），总大小为 322.1 MB。注意每个框架中都新增了深蓝色的“字符串表”。

![Nike iOS App v22.36.1 的 Emerge 体积分析 X-Ray](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Fnike-treemap.gif&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge 体积分析 X-Ray

搜索

当我们对比这两个构建时，会发现几乎全部 130 MB 的增长都来源于 [dyld](https://www.emergetools.com/glossary/dyld) 字符串表的增长。这些字符串表就是那些现在被带入了生产环境的不必要的元数据。

![两个 Nike 构建之间的 Emerge 对比表](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Fnike-size-comp.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

两个 Nike 构建之间的体积对比

Nike 的二进制符号从 213.9 KB（占 App 总大小的 0.11%）增长到了 127.5 **MB**——几乎占整个 App 的 40%。

![v22.35.0（Xcode 14 之前）中的二进制符号体积](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Finsight_comp1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

v22.35.0（Xcode 14 之前）中的二进制符号体积

![v22.36.1（Xcode 14 之后）中的二进制符号体积](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Finsight_comp2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

v22.36.1（Xcode 14 之后）中的二进制符号体积

总体而言，Nike iOS App 在没有任何重大改动的情况下增加了 130 MB。

![Nike iOS App 体积增长的条形图](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Fnike-size-chart.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [有多少 App 受到影响](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#apps-affected)

Emerge Tools 会定期从 App Store 下载 App 进行分析，这使我们能够检测到这些衰退并进行更仔细的检查。以下数据代表满足以下所有条件的 App：

- 二进制符号超过 2 MB
- 二进制符号占 App 体积超过 5%
- 在两次构建之间，二进制符号占 App 体积的百分比至少增长了 5%

所有 App 均直接从 App Store 获取。提供的分析仅用于教育目的，不代表 Emerge Tools 客户的情况。

上述 App 很可能都因使用 Xcode 14 发布而出现了衰退。话虽如此，还有许多其他 App 通过剥离二进制符号获得了显著的体积节省，但这些节省并不能明确归因于 Xcode 14。

Toyota（v2.0.9），即博客开头提到的那个 App，其安装体积为 550.2 MB，通过剥离二进制符号可以节省 109.8 MB（占总 App 体积的 20%）。那是 Emerge Tools 第一次分析 Toyota App，我们无法判断它之前的构建是否存在二进制符号臃肿。

还有一些 App，比如 TurboTax，自 2022 年 4 月以来我们每周都会对其进行分析。在我们测量的每一个构建中，TurboTax 都有超过 100 MB 的潜在节省空间。Intuit 的三个主要 iOS App——[TurboTax](https://www.emergetools.com/app/example/ios/turbotax-xcode14)、[Mint](https://www.emergetools.com/app/example/ios/mint-xcode14) 和 [Quickbooks](https://www.emergetools.com/app/example/ios/quickbooks-xcode14)——的安装体积总和为 1.37 GB。仅通过剥离二进制符号，它们就能节省 578 MB（占体积的 42%）。

以下是二进制符号超过 15 MB 的 App 列表，但我们无法确定这是否与切换到 Xcode 14 有关。

## [如何在没有 bitcode 的情况下剥离二进制符号](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#stripping-symbols)

幸运的是，从最终构建产物中剥离二进制符号很简单。这里有两种方法可以剥离二进制符号。

### [使用 Xcode 构建设置](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#xcode-build-settings)

你可以通过在 Archive 构建操作期间设置以下选项来进行自动剥离：

- “Deployment Postprocessing” = “Yes”
- “Strip Linked Product” = “Yes”
- “Additional Strip Flags” = `-rSTx`
- 其他所有剥离设置保留默认值

但使用此方法时，必须注意确保所有 target 的设置一致。另外，在与包管理器（package managers）一起使用时可能存在陷阱。对于 Cocoapods，这里有关于该问题的[讨论](https://github.com/CocoaPods/CocoaPods/issues/10277)，其中链接了一个可能的[解决方案](https://github.com/home-assistant/iOS/pull/2234/files#diff-8f7d6adf31268a2d897ee34bd170592648d6e520aa237104395e4a4438af50cb)（如果这样做，请确保被剥离的框架都是动态的）。

### [使用 Shell 脚本](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#shell-script)

你也可以在构建过程的最后、签名之前运行下面的脚本。请注意，对于某些包管理器（如 Cocoapods），在框架被拷贝完成到签名完成之间可能没有可以运行自定义脚本的点。在这种情况下，必须在剥离之后手动重新进行签名，因为剥离会使签名失效（invalidate）。

下面是一个可用于二进制剥离的脚本示例。非常感谢来自 Doordash 的 Filip Busic 提供的帮助！

在构建阶段的设置中，确保取消选中“Based on dependency analysis”，这样脚本会在每次构建时运行。你可以在[我们的文档](https://docs.emergetools.com/docs/strip-binary-symbols)中了解更多关于此方法的信息。

**注意：** 二进制剥离必须在给 App 进行代码签名之前完成，否则代码签名将失效。

## [为何这很重要](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#conclusion)

正如 Apple 在其 Xcode 14 视频中所说，App 体积是你的用户首先会注意到的事情。而用户也确实很在意，正如最近一位 American Airlines iOS App 的评论者所说：

![由于安装体积过大，American Airlines iOS App 收到的差评](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Famerican-review.jpeg&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

American Airlines iOS App 的 App Store 评论

Google 的 Play Console 文档也有类似的建议：

_App 体积是可能影响你 App 安装和卸载指标的最大因素之一。定期监测并了解如何减小 App 的下载和安装体积非常重要。   
 - [Play Console 文档](https://support.google.com/googleplay/android-developer/answer/9859372?hl=en)_

好的……体积很重要……假设这是真的，这个衰退可以如何避免呢？

指望开发者始终掌握平台版本变化的所有细微之处是不现实的。这就是持续监控的价值所在。如果测量是手动的，衰退就不能在进入生产环境之前被始终如一地发现。

![关于因 Xcode 14 导致体积增长的 Slack 消息发送给 Emerge Tools](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Ffirst-message.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

上面是我们一位客户发来的 Slack 消息，询问他们在切换到 Xcode 14 后 App 体积增长的问题。他们在发布前借助 Emerge 的持续集成工具发现了这个衰退。

作为 Xcode 14 一部分的 bitcode 弃用，毫无疑问是一个 App 体积衰退的极端例子。然而，我们发现更小的衰退随时都在发生，无论是由于 SDK 更新还是新功能。随着时间的推移，这些变化会累积成明显更差的用户体验，这更加说明主动关注你 App 体积的理由。
