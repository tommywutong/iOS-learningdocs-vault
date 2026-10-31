---
title: Apple silicon Mac 上的 iPad 与 iPhone App
session_id: 10114
collection: wwdc2020
year: 2020
duration: '17:29'
topics: [Developer Tools, 'App Store, Distribution & Marketing']
group: F · Mach-O / dyld / 编译链接 / 启动优化
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10114/'
content_hash: 'sha256:049cfec175f1ee01'
translated: true
---

# Apple silicon Mac 上的 iPad 与 iPhone App

<sub>WWDC2020 · 17:29 · Developer Tools、App Store, Distribution & Marketing</sub>

Apple silicon Mac 可以原样运行许多 iPad 与 iPhone App，这些 App 将通过 Mac App……

> [!note] 归档理由
> iOS 应用跑在 macOS 的二进制与环境差异

## 相关资源

- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10114/4/6F739926-5C96-42A5-8EAC-176185E35089/wwdc2020_10114_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10114/4/6F739926-5C96-42A5-8EAC-176185E35089/wwdc2020_10114_sd.mp4?dl=1)
- [Qualities of great iPad and iPhone apps on Macs with M1](https://developer.apple.com/videos/play/wwdc2021/10056)
- [Port your Mac app to Apple silicon](https://developer.apple.com/videos/play/wwdc2020/10214)
- [Introducing iPad Apps for Mac](https://developer.apple.com/videos/play/wwdc2019/205)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。

欢迎来到「Apple silicon Mac 上的 iPad 与 iPhone App」。我是 Jason Beaver，稍后我的同事 James Snee 和 Patrick Heynen 将加入。你可能已经在主题演讲或 State of the Union 中看到，Apple Silicon 上的 Big Sur 可以在 Mac 上原生运行 iOS App，而无需重新编译。Mac 是一个强大的开发平台，能支持各种 App。从强大的桌面 App 到基于 Web 的体验和图形密集型游戏，应有尽有。这些体验都由我们专用的 UI 框架驱动。在 macOS Catalina 中，我们添加了用 Mac Catalyst 构建 iOS App 以运行在 Mac 上的能力。Mac Catalyst 让 UIKit 成为 Mac 上这些其他 UI 框架的原生对等物，并使你能够把 iOS App 作为一等体验带到 Mac 上。你可以参考去年的「Introducing iPad Apps for Mac」session，了解我们是如何做到的。Mac Catalyst 需要使用 macOS SDK 构建你的 App，并允许你自定义和优化 App，以充分利用 Mac。

在 macOS Big Sur 中，我们利用这个 Mac Catalyst 基础设施，支持在基于 Apple Silicon 的 Mac 上按原样运行现有 iOS App。这里的「按原样」真的就是「按原样」。我们让用户在 Mac 上通过 Mac App Store 购买或下载你已经在 iOS App Store 上提供的 App。这是完全相同的二进制。

因为这些 App 使用与 Mac Catalyst App 相同的底层基础设施——相同的统一框架以及相同的 iOS 框架被带到 Mac 并与 Mac 集成——你的 iPad 和 iPhone App 自动获得大量行为，使它们在 Mac 上感到如在家一般。

然而，它们无法访问 Mac App 所能提供的一切。如果你希望在 Mac 上把 iOS App 推得更远，可以通过在 Xcode 中勾选那个开关创建 Mac Catalyst 版本。这将让你自定义 App 在 Mac 上的行为，还允许你在所有 Mac 上分发 App，而不仅仅是 Apple Silicon 上的 Mac。要让你的 App 在 Mac App Store 上架，它必须与 Mac 兼容。你的 App 不能依赖不可用的符号或框架，不能依赖现有框架中缺失的功能，也不能依赖 Mac 上不存在的硬件能力。

兼容的 iOS App 会自动在 Mac App Store 上架，但你可以在 App Store Connect 中管理 App 的可用性。如果你已经有 Mac App 或计划发布一个，或者你的 App 在 Mac 上没有意义，你可能会选择不让你的 iOS App 在 Mac App Store 上架。Patrick 稍后会在 session 中进一步讨论这一点。

大多数现有的 iPad 和 iPhone App 在 macOS 上运行得很好，但环境有一些你应该了解的差异。这些差异分为三类：硬件差异、UI 差异和系统软件差异。让我们从硬件差异开始。iOS 围绕直接的多点触控交互模型构建，而 macOS 围绕间接的、基于光标的交互模型构建。基础设施会自动映射许多多点触控手势，但如果你的 App 使用自定义触控处理，你应该测试 App 是否与 Mac 兼容。如果你的 App 支持键盘输入作为自定义触控处理的替代，那也有助于 App 更好地与 Mac 兼容，同时在 iOS 上提供更好的体验。

iOS 设备有一系列 Mac 上没有的传感器，如加速度计、陀螺仪、磁力计、深度感应摄像头和 GPS。通过在代码中动态确认适当的传感器存在，你可以确保 App 与整个 iOS 设备范围兼容，同时也与 Mac 兼容。注意，并非所有依赖这些传感器的 API 在 Mac 上都无法工作。例如，即使 Mac 不包含 GPS 接收器，它们也支持 Core Location，可以向你的 App 提供位置信息，尽管比 GPS 精确度低。iOS 设备通常只有前置和后置摄像头。Mac 则可能有内置前置摄像头（如笔记本和部分台式机），也可能包括集成在外部显示器中的摄像头或通过 USB 插入的摄像头。iOS App 可能未准备好处理所有这些配置，但使用 AVCaptureDeviceDiscoverySession 而非枚举所有 AV capture 设备，将允许我们确保你的 App 可访问最适合你需求的摄像头。现在，让我们谈谈一些 UI 差异。

如我们之前讨论的，iOS App 自动从 macOS 获得大量系统行为。这在外观和行为上必然与 iOS 设备不同。例如，提醒和弹出窗口可能在 Mac 上的不同位置显示，Open 和 Save 面板将显示在单独窗口中。这意味着你的 App 不要硬编码任何关于 UI 的假设，比如系统 UI 的位置，因为这些假设在 Mac 上运行时可能是错误的。在 macOS 上，窗口通常可由用户调整大小。如果你的 iPad App 已经在 iOS 上支持多任务，它在 macOS 上将完全可调整大小。这意味着它可以运行在很宽的尺寸范围，而不只是 iOS 多任务支持的少量固定尺寸。使用 Auto Layout 将帮助你确保 App 能在任何尺寸下正确运行。窗口调整在 macOS 上也是实时的。优化 App 布局的性能将改善 Mac 上的调整体验，并让你的 App 在 iOS 上多任务时更响应。如果你的 iPad App 不支持多任务，或者你有 iPhone App，它将在固定大小窗口中运行，不可调整大小。现在让我们看看一些系统软件差异。在 iOS 上，App 位于标准位置，但在 macOS 上，用户可以把 App 移动到他们喜欢的任何位置。你的 App 数据容器在 Mac 上也在不同位置。如果你使用 Foundation API 来定位文件系统中的项目，所有这些对你都是透明的，你的 App 在 Mac 上运行时将行为正确。

一些系统 API 会揭示你的 App 正在 Mac 上运行。例如，如果你在软件中（无论在设备还是服务器上）硬编码了部分系统，预期只接受 iPhone、iPod Touch 或 iPad 设备，那么在 Mac 上运行 iOS App 时你可能会遇到问题。更好的做法是确保软件健壮地处理意外值，并回退到某种默认行为。其他设备属性，如屏幕大小，可能在 Mac 上差异巨大，你的 App 不应假设它会匹配我们 iOS 设备之一的屏幕分辨率。现在我交给同事 James，他将讨论在 Mac 上测试和调试 iOS App。

谢谢，Jason。能够原生运行 iPhone 和 iPad App 在 Apple Silicon Mac 上，让你触达全新的用户群。在 macOS Big Sur 中，Apple 已完成所有艰苦工作，以最小到零的努力使这成为可能。所以我确信你想看看你的 App 在 Apple Silicon Mac 上运行的样子。如 Jason 所提，你的 App 可能对运行设备做了一些在 Mac 上不再成立的假设。这里的目标是确保 App 功能正确，没有重大 UI 故障或意外行为。好消息是，Xcode 对在 Mac 上原生调试、测试和剖析 iPhone 和 iPad App 提供了出色支持，就像在模拟器或 iOS 设备上运行一样。让我展示这是如何工作的。

这里我有一个 iOS App 项目在 Xcode 中打开。有些人可能认出它来自之前的 session。

要在 Apple Silicon Mac 上运行 iOS App，你需要做的只是选择新的运行目标：My Mac, Designed for iPad。让我们构建并运行这个 App。

我想指出，这个 App 是针对 iOS SDK 构建的，因此 barring Jason 提到的边缘情况，你不需要做任何源代码更改就可以让它运行。

所以，这里我们有这个 iOS App 原生运行在 Apple Silicon Mac 上。它针对 iOS SDK 构建，不是在模拟器中运行。当我点击各个视图时，我可以验证其行为与在 iPhone 上相同。

除了运行 iPhone 和 iPad App，我们还把 Xcode 所有出色的调试和剖析能力一并带来。

App 运行时，你可以通过查看 Xcode 的调试仪表盘获得其性能的高层视图。

你可以看到它消耗了多少 CPU 时间和内存，以及它可能执行的任何网络和磁盘 I/O。

如果你想更针对性地查看 App 在做什么，你可以暂停它或设置断点，并使用 Xcode 的调试功能之一，就像在 iPhone 或 iPad 上一样。例如，调试器的常见用途是响应用户操作调查 App 状态。让我用这个原生运行在 Mac 上的 iOS App 向你展示这是如何工作的。

我将在这里的这个 IBAction 方法中设置断点。我将通过点击 App 中这个有用的按钮来触发它。

你会看到，响应触发这个断点，Xcode 呈现其调试界面。一旦进入调试器，你可以使用所有你期望的功能，如检查变量和求值表达式。要调查更具体的问题，你可以查看 Memory 和 View 调试器。要理解和跟踪 App 性能，你可以使用 Instruments。最后，我确信你在想测试。测试是验证软件行为符合预期的好方法。让我展示一下。

使用 Xcode，你可以原生在 Apple Silicon Mac 上运行 iOS App 的 XCTest 单元测试。我将点击 Test Navigator 中的 Run 来执行这些测试。

和运行 App 一样，这些测试是针对 iOS SDK 构建并原生运行的。

很好。测试通过了。

Xcode 提供了一套很好的工具，帮助你在 Apple Silicon Mac 上原生调试、测试和剖析 iPhone 和 iPad App。现在我交给 Patrick，讨论为 Mac 分发 iPhone 和 iPad App。

所以，现在我们理解了 iPad 和 iPhone App 如何工作，让我们谈谈这些 App 如何到达你的用户和团队成员将运行的 Mac 上。

好消息是，iOS App 在 Mac 上的分发与今天在 iPad 或 iPhone 上完全相同。你今天熟悉的所有工作流，通过把 Mac 添加到你的 App 支持的设备家族中，已被无缝扩展。

要让 App 在 Mac 上可用，你真正要做的就是签署新的开发者协议，你的兼容 App 将在今年晚些时候在 Mac App Store 上架。

对于新提交，Mac 的分发将无缝融入你现有的开发工作流。

从 Xcode organizer，你可以通过 App Store Connect 导出或使用任何本地分发选项（如 ad hoc、enterprise 或 development）来把你的 iPad 或 iPhone App 版本直接分发给团队成员，从而为在 Mac 上运行准备 App。如果你的 App 利用 App Store 功能，它们在 Mac 上运行 iPad 或 iPhone App 时都将被支持。用户在 Mac 上运行时将完全访问与你的 iPad 或 iPhone App 关联的任何 App 内购买和订阅，并可以使用 StoreKit 框架进行新购买。如果你的 App 使用 on-demand resources 来动态管理为 App 下载的内容，那么在 Mac 上运行时体验将完全相同。事实上，所有 App Store 功能都与 iPad 和 iPhone 上完全一样。

App thinning 也被扩展以支持部署到 Apple Silicon Mac。App 内容会自动选择最适合在 Mac 上运行的版本，不适合其他 iPad 或 iPhone 设备的资源会被排除，以获得精简的安装体验。事实上，对于 app thinning，一台新 Mac 看起来就像任何其他非常 capable 的 iPad。

为了支持这个工作流，Xcode 在 Organizer 导出工作流中添加了一个新的 Mac 虚拟 thinning 目标。使用 Mac 设备来生成针对任何 Apple Silicon Mac 运行或测试优化的安装变体。

注意，因为 Mac 用户习惯在机器和可移动存储之间无缝移动 App，只需要单个 App 变体和 thinning 目标。

如果你的 App 依赖 developer 或 ad hoc 分发，它将与 iPhone 和 iPad 上一样工作。好消息是，你可以像为其他 iOS 设备一样导出，把 iPhone 或 iPad App 放到 Mac 上。如果你利用 Over-the-Air 安装，分发到 Mac 不需要任何更改。Mac 会自动从你的 OTA manifest 中选择适当的变体，下载并运行在适当配置的 Mac 上。

对于涉及管理设备的场景，iPad 和 iPhone App 可以像任何其他设备一样推送到已注册的 Mac。

尽管分发到 Mac 非常直接，但 Mac 是一个独立平台，在部署到 Mac 时有一些关键点需要考虑。

TestFlight 不适用于 Mac，因此在最终提交之前进行预发布分发，将需要使用 ad hoc 或 development 分发作为替代，以在 Mac 上测试你的 App。此外，正如 Jason 早前指出的，iPad 和 iPhone App 在 Mac 上的运行时兼容性有限。

Xcode 会告诉你 App 是否对 Mac 上不可用的符号或框架有硬依赖，但最好在可用时在 Apple Silicon Mac 硬件上测试 App，以评估 App 在 Mac 上的用户体验。

我们让把 App 上架 Mac App Store 变得极其容易。为了确保客户在 Mac 上获得 iOS App 的最佳体验，App Store Connect 将在今年夏天晚些时候提供工具，帮助你测试和验证该体验。当然，你仍然可以选择你的 App 是否在 Mac App Store 上架。

让我们看看现在如何控制这一点。

签署开发者协议后，所有兼容 App 将自动在 Mac 上架。使用 App Store Connect 查看所有 App 的状态。

在 App Store Connect 中，Pricing and Availability 页面是你决定是否在 Mac App Store 上分发 App 的地方。如果你不想让这个 App 在 Mac 上架，只需取消勾选这个框，它将不再在 Mac App Store 上销售。

注意，一旦 App 被设为不可用，Mac 用户将无法重新下载 App 的现有版本，直到 App 在 Mac 上重新上架。

所以，现在你知道了。你的 App 现在可以无需更改就原生运行在 Apple Silicon Mac 上。用户将喜欢在桌面上运行你的 App。大多数功能都能工作，App 会适应熟悉的 Mac 用户体验。构建和调试就是你已经知道并使用的工具。所以你需要做的就是测试你的 App 在 Apple Silicon Mac 上，确认 App 能很好地迁移过来。然后你将很快有一整批新用户从 Mac App Store 享受你的 App。

谢谢观看。
