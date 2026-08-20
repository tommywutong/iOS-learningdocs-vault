---
title: M3 Max 性能
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2023/12/05/m3-performance/'
original_language: en
published: 2023-12-05
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c76b36f466665488'
translated: true
---

> 原文：[M3 Max Performance](https://www.jessesquires.com/blog/2023/12/05/m3-performance/)　·　Jesse Squires

在[设置好我的新款 M3 MacBook Pro](https://www.jessesquires.com/blog/2023/12/04/new-m3-mbp/) 之后，我决定和我的旧款 Intel 机器做一些快速的性能对比。单凭使用感受，我本来会说它快得不可思议，但看到具体数据，我惊掉了下巴。

首先，两台机器的规格如下：

- 2020 年款 13 英寸 MacBook Pro，Intel 2.3 GHz 四核 i7，32GB RAM
- 2023 年款 14 英寸 MacBook Pro，M3 Max（16 核 CPU、40 核 GPU），128GB 内存

我真的**需要**一台 M3 Max 吗？大概不需要，但我一直等到 M 系列芯片的**第三代**才升级——我想让这次升级物有所值，而且希望这台机器能再用很多年。另外，作为[一名独立开发者](https://www.jessesquires.com/blog/2023/04/10/going-indie/)，我可以把这台机器作为业务开支在税前列支。:)

### Xcode 性能

在抹掉并重置我的旧笔记本电脑之前，我想看看 Intel 和 M3 在 Xcode 性能上的对比。我没有在这两台机器之间做特别「科学」的对比，而更像是一个真实世界的实验。例如，我没有退出每一个正在运行的 App 等。不过，在测试期间，我并没有主动使用任何一台机器。我使用迁移助理（Migration Assistant）从旧 Intel MacBook 设置了新的 M3 MacBook，因此它们的配置至少尽可能相似。

我在两台机器上构建并运行了同一个 Xcode 项目。这个项目非常庞大，根据 GitHub 统计数据，每月有超过 100 位代码提交者。它是一个 iOS App，已经开始让我想起当年在 Instagram iOS App 上工作的感觉。如果你曾经参与过这类超大型 App 的开发，你就会知道 Xcode **慢得让人痛苦**——这也是为什么这些大公司会实现 Buck 和 Bazel 等替代构建系统。这个项目包含大约 150 万行代码，包括第三方依赖——这是简单运行 `wc -l` 得出的粗略数字。它同时使用了 Objective-C 和 Swift，但主要是 Swift。大部分 Objective-C 代码来自第三方依赖。

以下是各种任务的运行结果。我列出了 Xcode 侧边栏构建日志中报告的构建时间。

在 Xcode 中对该项目执行一次 clean build：

- M3 Max：`2m 23s`
- Intel i7：`11m 32s`

速度提升了大约 5.5 倍！当然，Intel 机器的风扇在整个过程中全速运转。M3 的风扇只是短暂而安静地启动了大约 30-60 秒，我几乎都没注意到，因为 Intel 的风扇实在太吵了。

接下来，我尝试了一次增量构建：

- M3 Max：`20s`
- Intel i7：`66s`

最后，我进行了一次构建并运行，测量了 iOS 模拟器的冷启动（cold launch）：

- M3 Max：`51s`
- Intel i7：`2m 31s`

性能提升简直令人难以置信。使用这台新的 M3 机器是一种完全不同的体验，对我的开发工作流程（workflow）产生了**巨大的**、说实话是难以想象的影响。我从未经历过如此显著的硬件升级。现在在 Xcode 中的迭代周期几乎是瞬间完成。以前，我非常害怕在 Intel 机器上做 clean build——将近 12 分钟的时间足够做各种其他事情了！现在，clean build 根本不成问题。对于较小的项目，在 M3 上，Xcode 中的每一个操作都感觉几乎是瞬时的。

### 其他说明

电池续航非常出色。即使是在使用 Xcode 时，电池续航也令人印象深刻。在 Intel 机器上，仅使用 Xcode 1-2 小时后电池几乎就会耗尽。而在 M3 机器上，我能够充满电工作一整个工作日。

我没有测量日常使用和一般任务，但我可以自信地说，M3 在每个可以想象的方面都轻松地以数量级优势超越了 Intel。一切更快了。像 Photoshop 这类通常启动较慢的 App，现在几乎是瞬间启动。仅仅在 Intel 机器上打开大型 Xcode 项目通常都是一件苦差事，但对 M3 来说却毫不费力。

当使用 Xcode 处理像上面描述的那样的大型项目时，我的 Intel 机器会**慢如蜗牛**——有时它会变得非常卡顿，几乎无法使用，让我做不了其他任何事情。有了 M3，当我在其他 App 中切换到其他任务时，我甚至都感觉不到 Xcode 在运行。我的 Intel 机器即使在普通日子处理普通任务时也经常会出现彩球。在这台新的 M3 上，我还没见过加载转轮。

我非常高兴终于升级到了 Apple Silicon。如果你和我一样，一直在等待「合适的时机」从 Intel 机器升级，那么现在就是时候了。
