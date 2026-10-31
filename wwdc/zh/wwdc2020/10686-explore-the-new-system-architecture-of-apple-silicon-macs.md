---
title: 探索 Apple silicon Mac 的新系统架构
session_id: 10686
collection: wwdc2020
year: 2020
duration: '23:16'
topics: [Developer Tools, System Services]
group: F · Mach-O / dyld / 编译链接 / 启动优化
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10686/'
content_hash: 'sha256:dd8b210a0c638302'
translated: true
---

# 探索 Apple silicon Mac 的新系统架构

<sub>WWDC2020 · 23:16 · Developer Tools、System Services</sub>

了解配备 Apple silicon 的 Mac 如何利用 Apple 的片上系统（SoC）架构提供现代优势。利用统一……

> [!note] 归档理由
> Apple silicon 系统架构：内存/页/指针认证/Rosetta

## 相关资源

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10686/4/63FE46AD-053B-4294-B04F-A4BE576BD265/wwdc2020_10686_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10686/4/63FE46AD-053B-4294-B04F-A4BE576BD265/wwdc2020_10686_sd.mp4?dl=1)
- [Protect your Mac app with environment constraints](https://developer.apple.com/videos/play/wwdc2023/10266)
- [Optimize Metal Performance for Apple silicon Macs](https://developer.apple.com/videos/play/wwdc2020/10632)
- [Port your Mac app to Apple silicon](https://developer.apple.com/videos/play/wwdc2020/10214)
- [Set up DMA transfer in a PCIe driver](https://developer.apple.com/videos/play/wwdc2020/10686/?time=582)
- [Check if running in Rosetta](https://developer.apple.com/videos/play/wwdc2020/10686/?time=871)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。

大家好。我是 Gavin，我在 Core OS 团队，我的团队一直在把 macOS 带到 Apple Silicon 上。所以我很高兴能介绍这些系统中的一些变化。我们将讨论新功能以及如何在 macOS 应用中利用它们。我们将介绍一些安全增强，以及触及应用兼容性。然后我会交给同事 Anand，他将带你了解启动功能与恢复。基于 Intel 的 Mac 包含多核 CPU，许多还有独立 GPU，最近的 Mac 还有 T2 芯片，支持 Apple Pay、Touch ID 和 Hey Siri 等功能。

带独立 GPU 的机器为 CPU 和 GPU 提供独立内存。

现在，新的 Apple Silicon Mac 把所有这些组件合并到单个片上系统，即 SoC。把所有东西集成到一个芯片中给系统带来统一内存架构。

这意味着 GPU 和 CPU 在同一内存上工作。图形资源（如纹理、图像和几何数据）可以在 CPU 和 GPU 之间高效共享，没有开销，因为不需要跨 PCIe 总线复制数据。

在 Mac 上使用 Apple Silicon 还允许我们把为 iPhone 和 iPad 开发的独特技术带到 Apple Mac 上。Apple Silicon 包含协处理器，包括强大高效的视频编码器和解码器、神经引擎和矩阵乘法机器学习加速器。

Mac 多年来一直有多核 CPU，但对于基于 Intel 的 Mac，所有核心性能相似。

Apple Silicon Mac 有性能核心，当你的应用需要最大性能时使用，还有更节能的核心用于 CPU 密集度较低的任务。

我们称之为非对称多处理，或 AMP。

这些核心支持相同的架构特性并运行相同的软件。macOS 会同时使用所有这些核心，应用根据当前性能需求调度到适当核心。

那么，你的应用应如何利用 macOS 的这些新能力？你可能期望我们宣布新的 API 供你采用。但多年来我们一直在所有平台上构建一致的 API 集，并为 Apple Silicon 优化这些框架。

要在 GPU 上运行工作，你应该在基于 Intel 和 Apple Silicon 的 Mac 上都使用 Metal API。

在 Apple Silicon 上，运行受益于统一内存架构的任务时，你会看到显著的速度提升。

要利用硬件视频编码器和解码器，你可以使用 macOS 现有的相同 AVFoundation 和 VideoToolbox 框架。要获得最佳性能，你希望使用硬件优化的像素格式。Apple Silicon 特别擅长处理 BiPlanar 格式，如这个。

我不打算读出来，但留意名称中带 BiPlanar 的。

你的相同 Core ML 代码可以在任何 Mac 上运行。该功能在基于 Intel 的 Mac 上也可用，但在 Apple Silicon 上，Core ML 快得多、高效得多，并利用神经引擎和机器学习加速器。

你的 Core ML 代码应该直接在神经引擎上运行，无需你做任何更改。

你可能想检查你没有显式把模型配置为运行在 cpuOnly 或 cpuAndGPU。要符合在神经引擎上运行的条件，你希望 computeUnits 设为"all"，这也是默认值。

在 Apple Silicon 上，你还可以使用 accelerate 框架更直接地利用机器学习加速器。

当然，accelerate、compression 和 SIMD 框架中的所有内容对基于 Intel 和 Apple Silicon 的 Mac 都有高度调优的实现。

关于 AMP，我们有两条关键建议。首先，确保在所有工作项上设置服务质量（QoS）。这些 QoS 属性是对 macOS 应如何优先处理工作的指示。

动作是需要以最高性能完成，还是 OS 应优先能效。

正确设置 QoS 在所有平台上都很重要，但在 AMP 平台上尤其重要，因为 QoS 是决定任务运行在哪个核心上的因素之一。

我的第二条建议是使用 Grand Central Dispatch。同样，这在所有平台上都是好建议，但在 AMP 系统上尤其重要。

为什么？因为把工作分配到多个核心上特别棘手，当这些核心有非常不同的性能特性时。要获得最佳性能，你需要把任务的正确比例分配到每个线程。

Grand Central Dispatch 中的 API（如 concurrentPerform）可以帮助把任务最优地分配到所有核心并行运行的艰苦工作。

使用这类 API 时，确保把任务分解到足够多的迭代。这将帮助系统有效负载均衡。

这些框架在 macOS 中存在多年，因此如果你愿意了解更多，还有更多文档。很好的起点是这些 WWDC 场次。

Metal 团队今年还有几个关于 Apple Silicon Mac 上 Metal 的新场次。

好的，那就是 Apple Silicon 上的 macOS。现在我们转到安全。

构建我们自己的 Silicon 使我们能够为 iPhone 开发出色的安 全功能，我们很高兴把这些保护带到 Mac 上，同时确保不失去让 Mac 成为 Mac 的任何能力。

这些功能包括 write XOR execute、内核完整性保护、指针认证和设备隔离。

Apple Silicon 强制执行名为 write XOR execute 的限制。这意味着内存页可以是可写的或可执行的，但不能同时两者。既可写又可执行的页可能是危险的安全漏洞。然而，许多现代应用嵌入即时编译器以支持 Java 或 JavaScript 等语言。

这些 JIT 编译器经常依赖内存既可写又可执行。

因此，我们添加新 API，允许内存在可写和可执行权限之间快速切换。真正酷的是，这是按线程工作的，所以两个线程可以对同一页看到不同权限。这使得在多线程 JIT 中采用很容易。它将支持既快速又安全的 JIT 编译器。

Apple Silicon 在内存控制器中有硬件支持使 OS 内核代码不可变。一旦内核被加载到内存，内核完整性保护防止包含内核代码的页被修改或额外页被设为可执行。这阻止了在内核运行时注入新代码的攻击。

指针认证防止指针滥用，可以加固以防止诸如面向返回的编程等攻击。64 位指针中未使用的位用于存储指针认证码，指针被使用时检查。

现在，我们在内核、系统应用和系统服务中启用其使用。我们尚未准备好让你开始用指针认证分发应用。但如果你有兴趣实验，有一个 boot-arg 你可以设置，以便自己尝试。

PCIe 设备通过 IOMMU 访问系统内存。

在基于 Intel 的 Mac 上，macOS 给所有设备提供系统内存的共享视图。

在 Apple Silicon 上，所有设备获得独立的内存映射。这把设备限制为只访问它们预期的内存。并防止设备相互窥探。

要在 PCIe 设备驱动中设置 DMA 传输，你应该使用 IOMapper 和 IODMACommand API。

确保从你的设备获取 IOMapper，然后在配置 IODMACommand 时传递它。

一些较旧的驱动不使用这个 API，只是直接在 ioMemoryDescriptor 上使用 getPhysicalSegment。那不会工作，这些驱动需要在移植到新平台之前更新到新 API。你只会在用内核扩展编写的 IOKit 驱动中使用这个旧 API。

内核扩展仍然支持，但你和你的用户都会看到更多不便。我介绍的最后三个安全功能都影响内核扩展开发。

为了支持内核完整性保护，我们不得不改变 macOS 加载内核扩展的方式。

这意味着现在需要重启。

还有指针认证。如果你开发内核扩展，你将需要启用指针认证。随着我们继续改进平台，你应该期待围绕内核扩展看到更多摩擦。

我们去年在 Catalina 引入 DriverKit，使你能构建在用户空间运行的驱动，改善系统稳定性和安全性。

如果你还没有在你开发的任何驱动中研究 DriverKit，现在是时候了。

这里有帮助你了解更多并开始使用 DriverKit 的资源。

好的，那就是安全。现在让我们看看这个平台上的应用支持。

Rosetta 是我们用于运行现有 x86_64 应用的翻译器。它运行所有种类的应用：macOS 应用、Catalyst 应用、游戏和复杂应用如嵌入 JIT 编译器的 web 浏览器。

使用 Metal 的应用将直接为 Apple GPU 生成正确命令，使用 Core ML 的翻译应用能在神经引擎上运行。

Rosetta 的性能和兼容性只有通过 Apple Silicon 和软件团队密切合作才可能。

Rosetta 从应用安装的那一刻就开始工作。由 App Store 或包安装器触发，Rosetta 开始翻译你应用中的所有可执行代码。如果你的应用不使用我们的安装器，你可能会在首次启动时看到 dock 中额外 bounce 一两次，因为我们会那时开始翻译。

安全深入集成到这个翻译过程中。

你应用的翻译都经过代码签名， tied to a single machine，安全存储，并在 OS 更新时刷新。

当你的应用启动时，我们加载存储的翻译。Rosetta 然后完全模拟 x86_64 进程，直到系统调用接口。进程中的所有内容都被翻译，包括所有系统框架。如果 Rosetta 新遇到安装时未翻译的代码，我们会即时编译。

Rosetta 维护你期望的安全，hardened run-time 保护完全在 Rosetta 中运行的进程上强制执行。现在，希望一切都能直接工作，但如果你确实需要调试或分析应用，那是完全支持的。你可以直接从 Xcode 构建并运行翻译应用，可以从 Instruments 分析。你也可以使用命令行工具如 LLDB。基于 Intel 和 Apple Silicon Mac 上运行的进程有一些差异。页大小、内存排序规则、mach_absolute_time 的频率和浮点行为的一些细节，这些都会改变。

对于在 Rosetta 中运行的应用，我们确保一切匹配基于 Intel 的 Mac 上的行为。Rosetta 不支持 x86 的 AVX 向量扩展。

应用应该已经在尝试使用 AVX 之前检查机器是否支持。如果你需要，有一个 sysctl 可用。

另外，你将在 Developer Transition Kit 上看到一些限制，因为该硬件有一些兼容性限制。DTK 发行说明有更多信息。最后，如果你的应用确实需要知道何时在 Rosetta 中运行，我们添加了 sysctl.proc_translated 来检查。

好的，那就是 Rosetta。当然，你的客户真正想要的是应用的原生 arm64 端口。我们在开发者文档网站上有大量关于移植和优化应用的信息。

还有一个整场关于移植应用建议的场次，所以请查看，开始原生移植。

而且首次，兼容的 iPad 和 iPhone 应用也将可在 Mac 上获得。我们还有整场供你了解更多。我希望我已为你提供了 macOS on Apple Silicon、新安全增强和应用支持的一些有用见解。现在交给 Anand，他将深入 Apple Silicon 系统的启动架构。谢谢。谢谢，Gavin。过渡到 Apple Silicon 是一次伟大的冒险，启动过程是其中的重要部分。我很兴奋告诉你所有相关信息。

这部分将给你新启动过程的概述。我们将讨论启动和登录体验的变化、macOS 恢复模式的变化以及系统启动安全和数据保护层的增强。

在 Apple Silicon Mac 上，启动过程基于 iOS 和 iPadOS 的 Secure Boot 架构。

Secure Boot 确保每个启动组件都由 Apple 加密签名，且只有在验证信任链后才启动。这在 macOS 上提供启动时更强大的安全。

此外，我们添加了从内部或外部卷上安装的多个 macOS 启动的支持，以及启用启动 Apple 签名的任何版本 macOS。这将允许未来 macOS 继续启动旧版本。

最后，我们介绍了新的 macOS 恢复流程。那么 Apple Silicon Mac 上的启动如何工作？启动体验比以前简单得多。所有启动键现在统一了。

只需按住 Mac 便携式上的 Touch ID 按钮或台式机上的电源按钮以启动 Startup Options。Startup Options 是新 macOS Recovery UI 的一部分。一旦进入 Startup Options，你可以通过 UI 或快捷键访问功能和工具。

这是它的样子。这是 Apple Silicon Mac 上集成 Startup Manager 的 macOS Recovery Startup Options UI。

macOS Recovery 是启动和恢复相关一切的一站式商店。它以新用户体验 transformed。值得强调的两个特性是 Startup Disk 和 Mac Sharing Mode。先从 Mac Sharing Mode 开始。Mac Sharing Mode 替代 Target Disk Mode。它使用 SMB 文件共享提供对用户数据的文件级访问。

需要用户认证以启用此服务。接下来，Startup Disk。

macOS Recovery Startup Disk 专注于为每个安装了 macOS 的卷选择安全策略。你可以从完整或降低安全中选择，如这里显示。那么安全模式是什么？在完整安全模式下，新 Apple Silicon Mac 享有 iPhone 上存在的相同一流安全技术。此模式默认启用。此外，你现在可以从外部磁盘启动而无需降低系统安全。我们认为这很棒。相比之下，降低安全为你的 Mac 提供灵活性和可配置性，保持 Mac 的本色。

降低安全允许你运行任何版本的 macOS，包括 Apple 不再签名的版本。此外，想要安装 notarized 内核扩展的用户必须启用此模式才能这样做。

要启用降低安全，用户必须先在 macOS Recovery 中认证。

使用现有安全配置工具 CSRUtil，你也可以配置 Mac 安全以支持特定工作流程。

例如，如果你开发内核扩展，或你是探索 Apple 平台的研究人员或爱好者，你可能想这样做。

CSRUtil 提供许多 norms。这里突出几个。

现在，在基于 Intel 的 Mac 上，活动安全策略适用于整个系统。所以如果你在多个卷上安装了 macOS，降低一个的安全性会影响所有安装。然而，Apple Silicon Mac 为每个 macOS 安装维护独立的安全策略。你可以降低用于开发或测试的 OS 安全，同时保留用于日常使用的完整安全 macOS 安装。让我们继续谈谈新登录。

这很美。在 Apple Silicon Mac 上，macOS 有统一登录体验。它支持更丰富 UI 与加速图形，也与 macOS 外观一致。这个体验通过在不要求用户解锁系统的情况下完全启动 macOS 而成为可能。统一登录体验允许引入新功能，即使 FileVault 开启。

例如，它现在内置支持与 CCID- 和 PIV 兼容智能卡的认证，以及 VoiceOver 辅助功能改进。让我们谈一下数据保护。与 T2 Mac 类似，Apple Silicon Mac 上的 macOS 默认支持完整数据卷加密。当 FileVault 开启时，此加密与用户凭证绑定。

Apple Silicon Mac 还支持安全休眠。

除了在低电量事件期间保留桌面和应用，安全休眠通过提供完整静态内存内容保护（完整性与抗重放保护）提供。过渡到 Apple Silicon 使此功能成为可能。谈谈 Apple Silicon Mac 的恢复如何工作。

从高层看，软件由两个组件组成：macOS 和 macOS Recovery。如果 macOS 不可访问，你可以使用 macOS Recovery 重新安装和恢复系统。但当 macOS Recovery 本身不可访问时会发生什么？在基于 Intel 的 Mac 上，你可以使用 Internet Recovery。

在 Apple Silicon Mac 上，我们介绍 System Recovery。它是在单独隐藏容器中安装的最小 macOS 环境。它使你能通过重新安装 macOS 和 macOS Recovery 来恢复 Mac。

Apple Configurator 2 将继续支持。当 System Recovery 本身无法运行时，它允许你恢复 Mac。你可以擦除并重新安装 macOS，包括 System Recovery。

总结一下，在这个场次中，我们触及了 Apple Silicon 功能，包括安全增强，以及 macOS 应用如何利用它们。我们还介绍了应用兼容性并介绍 Rosetta。最后，我们描述了新启动功能和恢复过程。过渡到 Apple Silicon 为 macOS 带来显著改进。我们希望这个场次为你提供了良好见解。我们期待看到你在自己的应用中如何利用这些改进。非常感谢参加。
