---
title: 缩短你的 App 的启动时间
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reducing-your-app-s-launch-time
source_url: 'https://developer.apple.com/documentation/xcode/reducing-your-app-s-launch-time'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reducing-your-app-s-launch-time.json'
content_hash: 'sha256:59ed2d14b915db6b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md)

# 缩短你的 App 的启动时间

<sub>文章</sub>

通过最小化启动所花费的时间，为你的 App 创造更具响应能力的体验。

## 概述

用户对一款 App 的第一次体验，就是等待它启动的过程。操作系统会在 iOS 上通过启动画面、在 macOS 上通过程序坞中弹跳的图标来指示 App 正在启动。App 需要尽快准备好帮助用户完成任务。启动耗时过长的 App 可能会让用户感到沮丧，而在 iOS 上，如果启动时间过长，看门狗机制会将其终止。通常，如果一款 App 是用户日常工作流程的一部分，他们每天会启动它很多次，而较长的启动时间会导致执行任务时出现延误。

当用户点按主屏幕上某个 App 的图标时，iOS 会先为该 App 做好启动准备，然后再将控制权交给 App 进程。之后 App 会运行代码，为将其界面绘制到屏幕上做好准备。即使 App 的界面已经可见，App 可能仍在准备内容，或者正在用最终的控制替换过渡性界面（例如加载指示符）。这些步骤中的每一个都会计入 App 感知上的总启动时间，你可以采取措施来缩短它们的耗时。

### 了解 App 的激活

当用户点击你的图标或以其他方式回到你的 App 时，就会发生一次_激活_。

在 iOS 上，一次激活可能是一次启动，也可能是一次恢复。_启动_是指进程需要启动，而恢复是指你的 App 已经有一个存活的进程，即使它处于挂起状态。_恢复_通常要快得多，优化启动和优化恢复的工作也各不相同。

在 macOS 上，系统不会在正常使用过程中终止你的进程。一次激活可能需要系统从压缩器、交换空间中调入内存，并重新渲染。

### 了解冷启动和热启动

你 App 的激活情况会因设备之前的操作而有很大差异。

例如，在 iOS 上，如果你滑动返回主屏幕后立即重新进入该 App，这就是可能实现的最快激活方式。这也很可能是一次恢复。当系统判断需要进行一次启动时，这通常被称为「热启动」。

相反，如果用户刚玩过一款占用大量内存的游戏，然后重新进入你的 App，这次激活可能会比平均水平慢得多。在 iOS 上，你的 App 通常已被从内存中清除，以便为前台 App 提供更多内存。你的 App 启动所依赖的框架和守护进程也可能需要重新启动，并从磁盘中重新调页。这种情形，或是设备刚启动后的一次启动，通常被称为「冷启动」。

可以把热启动和冷启动看作一个连续的区间。在实际使用中，你的用户会根据设备的状态体验到一系列不同的性能表现。正是因为存在这样一个区间，在各种条件下进行测试对于预测你在真实世界中的性能表现才至关重要。

### 收集有关你 App 启动时间的指标

启动过程中的这些变化，意味着理解你的 App 在实际使用环境中的运行情况可能颇具挑战。

对于 iOS App，可以使用 Xcode Organizer 中的「启动时间」面板，查看从用户点按你的图标，到（在静态启动画面之后）第一个屏幕被绘制出来之间所经过的毫秒数。使用筛选器可以查看不同设备上的启动时间，以及典型值（第 50 百分位）和最长值（第 90 百分位）。通过点击图表中所需版本对应的柱状条，可以将当前发布版本的启动时间与之前的版本进行比较。

![](../../../attachments/b223c14508f0f0d07c006e3e90747f11/reducing-your-app-s-launch-time-1@2x.png)

<sub>Xcode Organizer 中「启动时间」指标面板的屏幕截图。从左到右依次是指标和报告列表、显示过去 8 个 App 版本启动时间的柱状图指标界面、图表中高亮显示的所选版本柱状条，以及右侧所选版本与最新版本的对比数据。</sub>

除了启动时间之外，[MetricKit](../metrickit.md) 还会报告 App 恢复所需的时间。[TimeToFirstDrawMetric](https://developer.apple.com/documentation/metrickit/timetofirstdrawmetric) 和 [ApplicationResumeTimeMetric](https://developer.apple.com/documentation/metrickit/applicationresumetimemetric) 包含了你前一天的启动时间和恢复时间的直方图。

### 识别可改进启动时间的区域

要确定你的 iOS App 启动时哪些进程占用了时间，可以使用 Xcode Organizer 中的「启动」面板。报告区域会显示一个按顺序排列的列表，列出 App 启动时系统调用的运行时间最长的函数，同一行中还会显示该进程占启动时间的百分比。

在报告列表中点击某个报告，会显示运行的函数及其对应的栈回溯。检查器（Inspector）中包含更多详细信息，具体包括：

- iOS 版本
- 设备型号
- 包含此签名的日志的总启动时间
- 收到的日志数量
- 14 天的报告趋势

利用耗时百分比指标，以及有关操作系统和受影响设备类型的信息，来确定缩短启动时间的优先级。通过使用报告列表中特定报告的函数签名及其对应的栈回溯，找出导致 App 启动时间增加的代码。在更新代码并验证修复后，将该报告标记为已解决。

![](../../../attachments/7baa8a19f0b130c23463519f6785cc33/reducing-your-app-s-launch-time-7@2x.png)

<sub>Xcode Organizer 中「启动」面板的屏幕截图。从左到右依次是报告列表——按运行耗时百分比排列的函数列表、报告列表中所选函数对应的调用栈，以及启动日志详情和统计信息（包括 14 天的报告趋势）。</sub>

### 获取针对启动时间问题的编码助手建议

选中一个启动报告后，点击检查器中的「生成建议」，即可在 Xcode 中获得辅助排查。选择工作区后，Xcode 会打开你的项目，并将栈回溯和启动时间占比粘贴到编码助手中，帮助你找出并修复导致启动时间衰退的根本原因。

### 对你 App 的启动时间进行性能分析

一旦你知道了 App 启动需要多长时间，你还需要知道为什么会花这么长时间。对 App 代码进行性能分析，是收集有关 App 时间花在哪里的数据的一种方式。在性能分析过程中，[Instruments](https://help.apple.com/instruments/mac/current/#/dev7b09c84f5) 会收集有关你的 App 调用了哪些方法，以及执行这些方法花了多长时间的信息。利用这些数据来识别代码中潜在的瓶颈或问题。

使用 App Launch 模板在 Instruments 中对你的 App 进行性能分析。在启动期间，Instruments 会收集时间概况（time profile）和线程状态跟踪。使用时间概况来识别 App 在启动期间运行的代码。使用线程状态跟踪来查找线程处于活动或阻塞状态的时间点，并找出线程被阻塞的原因。

在不同情况下对你 App 的启动时间进行性能分析，了解这些因素如何影响体验。以下是一些可以测试的不同情形示例：

- 打开设备，首次解锁，然后启动你的 App。
- 强制退出你的 App，然后再启动它。系统会终止你的 App 进程，随后系统会执行一次热启动。
- 如果你先打开其他 App，然后再启动自己的 App，系统会部分清除你的 App 及其依赖项。这反映了一种常见的用户工作流程。
- 使用一个占用资源非常多的 App——例如处理大量图形资源或实时摄像头输入的 App——然后再启动你的 App。系统很可能会终止你的 App 进程，这意味着系统需要在你下次启动时重新调入 App 的许多依赖项。

![显示 Instruments 中线程状态跟踪、以及对被阻塞线程说明的图像。](../../../attachments/06d851d843a5ad7bffdab22f3a5e7bd2/reducing-your-app-s-launch-time-2.png)

UIKit 在主线程上绘制视图并处理用户事件，因此当 App 完成启动时，该线程必须可用以绘制第一帧。在 Instruments 的线程跟踪中，主线程处于运行或被抢占状态的时间，都是它无法绘制视图或响应用户输入事件的时间。

要以不同的视角查看 App 启动情况，可以使用 Time Profile 模板对 App 进行性能分析。App Life Cycle 时间线会将 App 启动期间的活动划分为进程初始化、UIKit 初始化、UIKit 初始场景渲染和初始帧渲染。

![显示 Instruments 中 App Life Cycle 时间线的图像。](../../../attachments/48270584ea3ff3fdd6bc250cd4bb8446/reducing-your-app-s-launch-time-3.png)

### 减少对外部框架和动态库的依赖

在你的任何代码运行之前，系统必须先找到并加载你 App 的可执行文件及其依赖的所有库。

动态加载器（`dyld`）会加载 App 的可执行文件，并检查该可执行文件中的 Mach 加载命令，以找到 App 所需的框架和动态库。然后它会将每个框架加载到内存中，并解析可执行文件中的动态符号，使其指向动态库中相应的地址。

你 App 加载的每一个额外的第三方框架都会增加启动时间。尽管 `dyld` 会在用户安装 App 时将大量这类工作缓存到一个启动闭包（launch closure）中，但启动闭包的大小以及加载它之后需要完成的工作量，仍然取决于所加载库的数量和大小。你可以通过限制内嵌的第三方框架数量来缩短 App 的启动时间。你导入的框架，或者在 Xcode 的 Target editor 中添加到 App 的 Linked Frameworks and Libraries 设置里的框架，都计入这个数量。像 CoreFoundation 这样的内置框架对启动的影响要小得多，因为它们与使用同一框架的其他进程共享内存。

### 使用可合并的动态库

在 Xcode 15 或更高版本中，你可以使用可合并的动态库，在不损失调试构建中动态链接的构建速度的情况下，获得与发布构建中静态链接相近的 App 启动时间。可合并的动态库包含额外的元数据，使 Xcode 能够将该库合并到另一个二进制文件中。有关可合并库的更多信息，请参阅[配置你的项目以使用可合并库](configuring-your-project-to-use-mergeable-libraries.md)。

### 移除或减少代码中的静态初始化程序

某些 App 中的代码必须在 iOS 运行 App 的 `main()` 函数之前运行，这会增加启动时间。这类代码包括：

- C++ 静态构造函数。
- 类或分类中定义的 Objective-C `+load` 方法。
- 标有 clang 属性 `__attribute__((constructor))` 的函数。
- 链接到 App 或框架二进制文件的 `__DATA,__mod_init_func` 区段中的任何函数。

在可能的情况下，将这些代码移到 App 生命周期中更靠后的阶段——也就是 App 完成启动之后、但在需要这些工作结果之前的阶段。在 Instruments 中，dyld Activity 检测工具会测量你 App 运行静态初始化程序所花的时间，并报告其他有用的指标，帮助你加快 App 的启动速度。

### 将开销较大的任务移出你的 App 委托

审查你的初始化代码，推迟开销较大的工作。系统会在启动周期内调用你 App 委托的方法，让你有时间执行必要的任务。这些方法在主线程上同步执行，只有当这两个方法都成功返回后，启动周期才会结束。因此，你在这些方法中执行的任何开销较大的任务，都会延迟该启动周期的完成。

UIKit 会初始化你 App 委托类（即采用 [UIApplicationDelegate](../uikit/uiapplicationdelegate.md) 协议的类）的一个实例，并向它发送 [application(_:willFinishLaunchingWithOptions:)](<../uikit/uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) 和 [application(_:didFinishLaunchingWithOptions:)](<../uikit/uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) 消息。UIKit 在主线程上发送这些消息，在这些方法中执行代码所花的时间会增加 App 的启动时间。在这些方法中只做准备 App 初始显示所必需的工作；将其他任务推迟到 App 生命周期中更合适的时间点执行。

如果在内容刷新期间向用户展示旧内容是可以接受的，那么可以将数据模型与网络服务的同步推迟到 App 运行之后。将同步工作移到一个异步的后台队列中。注册一个后台任务，用于从网络服务获取更新，从而既减少启动时数据的陈旧程度，也减少让数据保持最新所需的工作量。

将非视图相关的功能（比如持久化存储和位置服务）的初始化推迟到首次使用时，而不是在 App 启动时进行。只获取显示 App 初始视图所必需的数据。留意你的 App 是否正在恢复状态，并准备好显示正在恢复的那个视图所需的数据。如果没有状态需要恢复，就只准备默认的初始视图。例如，一款照片图库 App 可能默认显示一组图像缩略图，让用户挑选一张照片以查看详情视图。如果 App 是在没有恢复状态的情况下启动的，它只需要为满屏的缩略图显示占位符，并在 App 完成启动后用真实的图像缩略图填充它们。它不需要在用户点按某个缩略图之前就加载完整的详细图像。

初始化一个已知在初次启动时可用的、受限的 App 行为子集。例如，一款任务管理器 App 可以让用户在启动时就创建一个新任务，即使该 App 尚未从其持久化存储或网络服务中获取用户所有的现有任务。

### 降低初始视图的复杂度

Xcode Organizer 和 MetricKit 都以「首帧时间」作为启动时间的度量标准，其中包括绘制第一帧所显示视图所需的时间。你只能在主线程上修改视图层级结构；因此，视图更多、更复杂的视图层级结构比简单的层级结构渲染耗时更长。

降低 App 初始视图的复杂度可以改善加载时间，用标准视图替换重写了 [draw(_:)](<../uikit/uiview/draw(__).md>) 的自定义视图同样有帮助。在你需要自定义绘制的地方，请留意传给 `draw(_:)` 的矩形区域，只渲染该矩形范围内的视图部分。这样做可以避免在视图中未渲染到屏幕上的部分进行图像解码，以及计算颜色、坐标和绘制命令。

### 跟踪其他启动活动

启动时间指标衡量的是从用户在主屏幕上点按 App 图标，到 App 在屏幕上绘制第一帧之间的时间。绘制 `default.png` 或启动屏幕故事板就发生在这段时间内，它的出现并不会结束启动时间的计时。

如果你的 App 在绘制完第一帧之后、但在用户能够开始使用 App 之前，仍需运行代码，那段时间不会计入启动时间指标。不过，额外的启动活动仍然会影响用户对 App 响应能力的感知。例如，如果你的 App 在打开后需要渲染一份文稿，用户很可能会等待文稿渲染完成，并将其视为启动时间的一部分，即使系统在你显示加载图标期间就已经结束了启动计时。

要跟踪其他启动活动，请在你的 App 中创建一个类别为 [pointsOfInterest](../os/oslog/category/pointsofinterest.md) 的 [OSLog](../os/oslog.md) 对象。使用 `os_signpost` 函数记录 App 准备任务的开始和结束，如以下示例所示：

```swift
class ViewController: UIViewController {
    static let startupActivities:StaticString = "Startup Activities"
    let poiLog = OSLog(subsystem: "com.example.CocoaPictures", category: .pointsOfInterest)

    override func viewDidAppear() {
        super.viewDidAppear()
        os_signpost(.begin, log: self.poiLog, name: ViewController.startupActivities)
        // do work to prepare the view
        os_signpost(.end, log: self.poiLog, name: ViewController.startupActivities)
    }
}
```

在 Instruments 中，「关注点」（Points of Interest）会在其时间线中显示这些 os_signpost。你可以利用这些信息，将 App 中的活动与 App 的其他启动任务关联起来。

![](../../../attachments/8af771222ac18b46017898a01ec66e51/reducing-your-app-s-launch-time-5@2x.png)

<sub>显示「关注点」检测工具的屏幕截图，其中的时间线展示了 App 额外启动活动期间各区域的开始和结束。</sub>

## 另请参阅

### 响应能力

- [分析你已发布 App 中的响应能力问题](analyzing-responsiveness-issues-in-your-shipping-app.md) — 识别用户遇到的响应能力问题，并使用 Xcode Organizer 中的挂起和卡顿数据来确定最需要优先修复的问题。
- [提升 App 的响应能力](improving-app-responsiveness.md) — 通过消除 App 中的挂起和卡顿，创造感觉响应灵敏的用户体验。
- [了解用户界面的响应能力](understanding-user-interface-responsiveness.md) — 通过检查事件处理和渲染循环，让你的 App 响应更灵敏。
- [了解并提升 SwiftUI 性能](understanding-and-improving-swiftui-performance.md) — 识别并解决长时间运行的视图更新问题，降低更新频率。
- [了解你的 App 中的挂起](understanding-hangs-in-your-app.md) — 通过检查主线程和主运行循环，确定用户交互延迟的原因。
- [了解你的 App 中的卡顿](understanding-hitches-in-your-app.md) — 通过检查渲染循环来确定动作中断的原因。
- [及早诊断性能问题](diagnosing-performance-issues-early.md) — 在开发和测试期间，使用 Xcode 中的 Thread Performance Checker 工具诊断 App 中潜在的性能问题。
- [减少你的 App 中的终止情况](reduce-terminations-in-your-app.md) — 通过解决常见的终止原因，减少系统停止你 App 的频率。
