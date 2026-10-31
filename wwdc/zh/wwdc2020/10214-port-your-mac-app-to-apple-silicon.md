---
title: 将你的 Mac App 迁移到 Apple 芯片
session_id: 10214
collection: wwdc2020
year: 2020
duration: '40:44'
topics: [Developer Tools]
group: F · Mach-O / dyld / 编译链接 / 启动优化
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10214/'
content_hash: 'sha256:e7f59fe59be089db'
translated: true
---

# 将你的 Mac App 迁移到 Apple 芯片

<sub>WWDC2020 · 40:44 · Developer Tools</sub>

你的迁移问题，有答案了：了解如何为 Apple 芯片 Mac 重新编译 macOS App，并构建可在两种架构上运行的通用 App……

> [!note] 归档理由
> Mach-O 通用二进制、架构迁移的实际问题

## 相关资源

- [了解 Apple Silicon 的更多信息](https://developer.apple.com/documentation/apple-silicon)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10214/7/871FAB69-F6A4-470A-80F0-00028CDC0E58/wwdc2020_10214_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10214/7/871FAB69-F6A4-470A-80F0-00028CDC0E58/wwdc2020_10214_sd.mp4?dl=1)
- [Bring your Metal app to Apple silicon Macs](https://developer.apple.com/videos/play/wwdc2020/10631)
- [Explore the new system architecture of Apple silicon Macs](https://developer.apple.com/videos/play/wwdc2020/10686)
- [iPad and iPhone apps on Apple silicon Macs](https://developer.apple.com/videos/play/wwdc2020/10114)
- [Optimize Metal Performance for Apple silicon Macs](https://developer.apple.com/videos/play/wwdc2020/10632)
- [All About Notarization](https://developer.apple.com/videos/play/wwdc2019/703)
- [Understanding Crashes and Crash Logs](https://developer.apple.com/videos/play/wwdc2018/414)
- [Don’t assume the time is returned in nanoseconds](https://developer.apple.com/videos/play/wwdc2020/10214/?time=1279)
- [Use clock_gettime_nsec_np to read timestamp in nanoseconds](https://developer.apple.com/videos/play/wwdc2020/10214/?time=1300)
- [Avoid spinlocks and spinning to check for work](https://developer.apple.com/videos/play/wwdc2020/10214/?time=1600)
- [Prefer blocking locks and condition variables](https://developer.apple.com/videos/play/wwdc2020/10214/?time=1623)
- [Load a plug-in dynamically](https://developer.apple.com/videos/play/wwdc2020/10214/?time=2031)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。

大家好，欢迎来到《将你的 Mac App 迁移到 Apple 芯片》。我叫 Kuba Mracek，我将带领 Mac App 开发者踏上把 App 迁移到 Apple 芯片的旅程。我们先从迁移对你和你的 App 意味着什么的概述开始。然后讨论构建通用 Mac App 以及可能遇到的问题。我会演示在 Apple 芯片上运行、调试和测试，并讨论插件的影响。最后我还会提到几条使用通用 App 的技巧。让我们开始吧。Mac 正在向 Apple 芯片过渡。你可能想知道这对你和你的 App 到底意味着什么。先从基础说起。Apple 芯片 Mac 上的原生 CPU 架构称为 arm64，如果你开发 iOS，这听起来会很熟悉。iOS 设备使用相同的架构。

App 当然可以构建为原生 ARM 代码并原生运行，但现有的 Intel App 仍然可以在 Apple 芯片 Mac 上工作。Rosetta 翻译会无缝运行它们。arm64 是今天的主题，因为那是你的 App 将使用的新的 CPU 架构，而且不只你的 GUI 代码。所有用户空间程序现在都将使用 arm64 作为 CPU 架构。本节将介绍如何使用 Xcode 12 把所有代码编译成 arm64，让它原生运行。我这里有一台 Apple 芯片 Mac，我将启动 Xcode 并打开一个名为 Solar System 的现有项目。让我们关注工具栏里包含当前运行目标的这个区域。它显示"My Mac"，但打开后会显示更多选项。我可以选择在 Rosetta 下运行，或构建同时支持 Apple 芯片和 Intel 的通用 App。让我们坚持原生构建，直接构建并运行 App。就是它。无需任何代码更改或项目设置调整，App 只需在 Xcode 中按一下 Run 按钮就原生构建并运行。在活动监视器中，我可以验证进程类型。在 Solar System Mac 下的"种类"列，显示为 Apple CPU 架构。这意味着它确实原生运行。Xcode 12 会为你处理必要的项目设置。你不必更改构建设置来选择 CPU 架构。正如我们刚看到的，对于没有可移植性问题的 App，构建原生版本往往就像在 Xcode 中点击 Run 按钮一样简单。我建议你直接去试试。如果 App 能正常工作并正确运行，你的工作就完成了。如果遇到问题，我将在本节后面描述一些常见陷阱。我们还在 developer.apple.com/documentation 发布了大量迁移文档，你可以从名为 Apple Silicon 的页面开始，从那里导航到涵盖本节许多主题的其他文章。文档……（原文截断）

如果你有现有的仅 Intel 的 App，或因某种原因不能立即开始原生构建 App，Apple 芯片电脑配有 Rosetta，一个可以无缝运行这些 App 的翻译环境。在 Rosetta 中，整个进程总是被翻译的。你不能把原生代码加载到被翻译的进程中，反之亦然。你也不能对内核扩展、AVX 向量指令或虚拟化使用 Rosetta。Xcode 完全支持为 Rosetta 构建和运行 App。让我们看看它是如何工作的。正如之前注意到的，Xcode 中的运行目标允许你以 Rosetta 为目标。按下 Run 会构建 Intel 代码，然后在 Rosetta 中运行它。在活动监视器中，App 现在显示为 Intel CPU。所以它正在翻译中运行。Xcode 的所有开发方面，包括测试、调试和性能分析都得到支持，并且都是即时翻译的。所以如果你恰好使用调试器查看单个 CPU 指令，你会发现它们是 Intel 指令。不要对此感到惊讶。它们都被 Rosetta 透明地翻译。现在让我们专注于把 App 迁移到 Apple 芯片 Mac 上原生运行。第一步是把 App 构建为通用 App。让我先解释为什么我认为为 Apple 芯片构建 App 实际上会是一项非常简单的任务。首先，arm64 的字节序与 x86 相同。所以如果你还记得 PowerPC 到 Intel 的过渡，这次你不必处理任何字节序交换问题。

其次，如果你有与 iOS App 共享的代码，该代码几乎肯定已经完全移植到 arm64，因为 iOS 使用的 CPU 架构与 Apple 芯片 Mac 相同。第三，你可以使用已有的任何 Mac 来构建通用 App。Xcode 12、SDK 和整个工具链完全支持交叉编译。也就是说，它能够为与你运行 Xcode 的架构不同的架构生成代码。

我将在一个名为 Network Benchmarking 的小工具 App 上演示一些可能的迁移问题。我有去年的这个 App 的副本，所以它是仅 Intel 的，我们可以在 Finder 的"显示简介"中看到它显示为"Application (Intel)"。但正如你所见，我仍然可以运行它，它将在 Rosetta 下运行。这个 App 让我创建 TCP 服务器和客户端，并启动基准测试，同时测量数据吞吐量。App 还显示大量系统信息，如当前 CPU 和内存使用情况。这就是它的全部功能。

现在让我们在 Xcode 12 中打开这个 App，开始把它变成原生 App。让我简要描述这个项目的整体结构。它里面有几个 target，比如第一个是 App 的实际 GUI。它大多是高层 AppKit 代码，所以有 App 委托和视图控制器等。但我也有一些更底层的组件，比如这个 TimeTools 包和一些网络库，甚至包含一个插件。通常你应该预期高层 AppKit 代码不会有可移植性问题。但对于更底层的部分，我们可能需要做一些修复。让我们开始构建。第一步是验证 App 仍然能用 Xcode 12 为 Intel 正确构建。所以让我选择"My Mac (Rosetta)"作为运行目标，然后点 Build。在我的情况下 App 能正常构建。通常这不会产生任何错误，但有一个情况我想指出。

Intel 机器和 Apple 芯片系统之间的原生页面大小不同。如果你使用 PAGE_SIZE 宏，它不再是编译时常量，所以你可能会因此看到构建失败。修复非常简单：要么使用 PAGE_MAX_SIZE 作为编译时上限，要么使用 vm_page_size 在运行时动态读取该值。还要注意 Rosetta 会完全匹配 Intel 环境：Apple 芯片 Mac 上的 CPU 将为被翻译的进程支持 4 kB 页面。现在进入第二步。切换为原生架构构建，让我们解决错误。在 Xcode 中，我将再次打开运行目标菜单，并选择"My Mac"，执行另一次构建。这次我确实得到了一个编译时错误。让我们看看。看起来这个名为 GetDefaultTimerClass 的函数使用预处理器宏——这些 #if 行——在不同平台之间切换行为。这是一种相当常见的模式。它被称为 target conditionals。但看起来我在写这段代码时犯了一个错误。对于这里的这个分支，我想以 macOS 和模拟器为目标，但我的条件却写成了 __x86_64__ —— 也就是 Intel CPU —— 这过去没问题但现在不再正确。这里使用 target conditionals 的正确方式是用正确的术语表达。如果我想以 macOS 和模拟器为目标，应该使用 TARGET_OS_OSX 或 TARGET_OS_SIMULATOR。这个问题在可移植代码中相当常见。你应该基于你实际想要表达的内容使用语义化的 target conditionals。这里有一张常见 target conditionals 的表格。当你想为 Mac 条件编译代码时，使用 TARGET_OS_OSX 或在 Swift 代码中使用 #if os(macOS)。不要假设 CPU 架构就意味着平台。

当你想为 Intel 条件编译代码时，使用 TARGET_CPU_X86_64 或在 Swift 代码中使用 #if arch(x86_64)。其他情况类似。不要假设某个平台或在模拟器中运行使用特定的 CPU 架构。

与此相关的是任何使用 CPU 特定代码和汇编的情况，无论是内联在 Objective-C 代码中还是独立的汇编文件。所有此类代码都需要用 #ifs 和我刚提到的正确 target conditionals 正确保护。如果你只有一些函数的 Intel 实现，比如这样，你将需要为 Apple 芯片提供第二个实现。然而在很多情况下你可以直接依赖 OS 提供的功能。使用 Accelerate 和 Compression 框架来获得数学函数和压缩算法的高性能优化实现。

现在代码已修复，让我们再次构建。

这次我收到了不同的构建时问题。这不是我写的任何源代码中的 bug，因为错误消息实际上不指向任何源文件。如果我点击它，它只会带我去构建日志。这次是链接器发出错误。这引导我们进入第三步：解决链接时问题。问题是我的 App 无法链接。让我切换到"仅错误"，以便专注于链接器想要告诉我什么："Undefined symbols for architecture arm64"，我看到了符号名，但它对我来说并不熟悉。这不是我代码中的符号或类名。错误消息中真正重要的部分其实是它上面的黄色警告。让我们看看。

链接器说："ignoring file when building for macOS-arm64, but attempting to link with file built for macOS-x86_64." 这个错误意味着我依赖的是一个不是通用的二进制框架。这个输出还提供了详情。它提到了有问题的框架名，并打印了符号名——在本例中是一个 Objective-C 类名——以及引用它的对象文件。在我的 App 中，是 AppDelegate 文件使用了这个类。这有助于了解，因为你可能想尝试移除依赖以取得进展。所以在我 App 中，我会去编辑 AppDelegate 源代码。但总之，问题是我项目中有一个预编译的二进制框架。在项目中拥有预编译二进制需要做一些工作。你依赖的所有静态和动态库都必须先构建为通用，然后你才能实际构建 App。你需要联系这些二进制的供应商，要求他们提供同时包含 Intel 代码和 Apple 芯片代码的通用构建。然后你可以用通用版本替换旧二进制，链接器就能真正链接 App。为了逐步取得进展，你可以考虑暂时移除那个二进制依赖，但不要忘记一旦有了那个库的通用构建就把它加回来。我还建议立即扫描源代码，搜索任何不是从源代码构建、而是由别人预编译的内容。通常那是扩展名为 .a、.dylib、.framework 和 .xcframework 的文件和 bundle。你可以使用 lipo -info 命令检查任何二进制，看看它是否已经是通用的。让我们在演示项目上试试。我将在 Finder 中打开项目目录，同时打开 Terminal。

然后我将把 Sparkle.framework 拖到 Terminal 以获取其完整文件路径，并对框架内的二进制使用 lipo -info 命令。

一旦我运行这个命令，lipo 会说它真的是一个仅 Intel 的二进制。

所以我需要做的是用一个新的通用版本更新这个框架。这里你通常会联系供应商要求新版本，或去供应商网站下载已发布的通用二进制。但我已经有了这个框架的新通用版本。我的队友实际上已经为我提供了。因为这个框架是开源的，把它构建为通用 буквально只是用 Xcode 12 重新构建的问题，我们根本没有遇到任何可移植性问题。让我用新版本替换旧版本，并检查这个新版本的框架。

确实现在是通用的了。lipo 说它现在是一个 fat 文件，同时包含 x86_64 代码和 arm64 代码。如果我再在 Xcode 中构建一次 App，这次它将成功构建。第四步。没有第四步！我现在就有了 App 的原生构建。

在这个示例项目中，我们看到了构建通用 App 时的几个典型问题。请参阅 developer.apple.com 上 Apple Silicon 页面的文档，它涵盖了许多我们遇到的迁移问题。如果你更喜欢用 xcodebuild 在命令行构建，选择正确的构建目标很重要。使用 -showdestinations 选项获取可用运行目标的列表。

然后你可以使用 -destination 标志来选择一个。这里有两個示例，分别针对 arm64 或 x86_64。让我总结一下我们为了能够把 App 构建为原生 App 而经历的步骤。首先，我们验证了 App 仍然能为 Intel CPU 正确构建。然后我们切换为原生构建并修复了代码问题。这是代码本身不可移植的情况。第三，我们修复了链接时问题，这通常是由二进制依赖引起的。

就是这样。提醒一下，构建通用 App 可以在任何 Mac 上进行。你也可以使用 Intel Mac 电脑。现在 App 已经构建好了，让我们继续讨论运行和调试你的原生构建。我知道你在想：App 构建了，那我们出货吧？不。你的原生 App 仍然绝对需要运行时测试。不要假设 App 构建了就能完美工作。这一部分你需要一台 Apple 芯片 Mac。调试、运行单元测试、性能分析、使用 sanitizers 等都需要运行原生代码，而这只能在 Apple 芯片上进行。请计划在发布 App 之前对两种 CPU 架构都进行完整的运行时测试、验证和性能分析。让我们在演示项目上做一些运行时测试。现在 App 构建了，我终于可以原生运行它了。它似乎启动正常：UI 显示出来了，系统信息表似乎准确。让我们尝试启动客户端服务器数据传输。注意传输统计和进度条有问题。它似乎以错误的频率刷新。它应该每一百毫秒更新一次，但进度条却做出这些奇怪的大跳。让我们调查这个问题。基于基准值，我认为基准测试实际上运行正常。只是 UI 刷新不够快。所以让我在视图控制器的一个名为 updateClientProgressUI 的方法中设置断点，然后再次运行基准测试。

我们最终会命中这个断点，但注意这花了好一会儿——超过几秒。所以我认为调用这个方法的定时器有问题。让我们往下看几帧堆栈，那里我有一个自定义定时器的实现。它似乎在使用名为 mach_absolute_time 的 API 测量单调时间戳。所以我认为这就是问题的来源： whoever 写了这段代码假设 mach_absolute_time 总是返回纳秒值。这就是下面的代码除以一千三次以转换为秒的原因。然而这不正确。我可以 option-点击该 API 来查看它的文档，它说它返回的是 tick 单位的值。

所以，假设这些 tick 单位是一个纳秒是不正确的。这个 API 的时间基准在不同的 CPU 架构上不同。可能最好的解决方案是直接避免使用底层 API 编写自定义定时器。Foundation 和 GCD 有通常更好用的定时器实现。但如果你真的需要使用时间戳来测量时间，我们既可以动态查询时间基准，也可以切换到另一个 API。有一个 clock_gettime API 的变体总是返回纳秒时间戳。让我们在演示中使用它。文档弹窗方便地提到了这个其他 API，所以我可以直接从这里复制。

让我们再运行一次 App，也让我禁用之前设置的断点。这次如果我运行基准测试，进度条将流畅更新。这个问题其实相当常见，这个 bug 的典型效果是某件事运行速度大约慢 40 倍，或者某个事件发生频率大约是应有的 1/40。如果你观察到类似情况，在代码库中搜索 mach_absolute_time。当然，测试软件的最好方式是自动化。这个项目中大部分代码都有单元测试覆盖，让我们运行它们。

幸运的是我所有的单元测试都通过了。但注意整个测试套件只运行了一次。在这种情况下，在运行目标菜单中我选择了原生模式。所以我的所有测试和被测代码都在原生模式下运行。如果我想以 Intel 代码在 Rosetta 下运行测试，我必须切换运行目标并重新运行测试。

在我的项目中它们在两种架构下似乎都通过了。但如果你看到某个测试只在两种目标之一下失败，那又表明存在不可移植的代码。与命令行构建类似，用 xcodebuild 测试时，要考虑测试使用的运行目标。如果你想原生运行测试，在 -destination 标志中指定 arch=arm64。这也是默认值，所以如果你不使用任何运行目标，测试将作为原生代码运行。要以 Intel 代码在 Rosetta 下运行测试，使用 arch=x86_64。你可能还想设置 CI 系统在两种模式下运行测试，以捕获导致测试失败的不可移植代码。让我们看一个我有的特定测试，因为它是性能基准。我将再次选择原生运行目标并运行测试，它只是测量从本地服务器传输 10 兆字节数据需要多长时间。结果是 21 毫秒。如果我切换到 Rosetta，再次运行测试，我们会得到不同的结果。

这次是 29 毫秒，比原生慢，但被翻译的代码仍然表现非常好，结果与原生执行非常接近。

在 Apple 芯片 Mac 上进行性能分析和基准测试时，原生代码通常性能最好，你应该致力于优化原生执行。如果你在原生模式下看到性能下降，注意你可能有的任何 Intel 特定代码优化，例如使用 SSE 或 AVX 的优化汇编。为了获得最佳性能，你可能需要使用 ARM 指令集为 Apple 芯片提供匹配的实现。但总的来说，你应该尽可能使用 Apple 提供的 API，比如 Accelerate.framework，因为它们会为所有支持的 CPU 提供高性能实现。Apple 芯片 Mac 使用非对称 CPU 核心，这可能影响你的高性能代码。有两种类型的 CPU 核心：高性能的，也称为 P 核心，和节能的，称为 E 核心。所有核心都可以同时活跃，以在并行工作负载上获得最大性能。

在 Instruments 中，这种区别在时间线的 CPU 视图中可见。列表中的各个 CPU 核心有标签，告诉你哪些是能效核心，哪些是性能核心。如果你看到像这样的图，其中几乎所有工作都只调度在 P 核心或只调度在 E 核心上，不要感到惊讶。系统正在动态选择执行工作的最佳方式，以做出正确的性能和电池寿命权衡。在非对称 CPU 系统上要避免的一个重要模式是使用自旋锁和忙等待代码。在这个例子中，第一个函数使用自旋锁，第二个示例是忙等待。这意味着主动花费 CPU 时间在循环中检查队列中是否有新作业可用。这在任何计算机系统上通常都是错误的。第一个函数的一个好得多的替代方案是使用某种阻塞类型的锁——例如 os_unfair_lock——而不是在自旋循环中检查条件，使用条件变量，它会阻塞直到条件满足。在 Apple 芯片 Mac 上，忙等待可能 pointless 地占用 P 核心，导致整个工作的完成总体延迟。你应该优先使用无法取得进展时会阻塞的同步原语，NSLock、os_unfair_lock、pthread mutexes 都是阻塞锁的例子。NSCondition 和 pthread 条件变量提供了等待特定条件发生的方式。

一般来说，尽可能使用 GCD，并避免根据可用 CPU 数量拆分工作。相反，倾向于把任务拆分为更小的单位。关于 GCD 的详情，请观看 WWDC 2017 的视频。如果你使用线程进行音频处理，今年的 Meet Audio Workgroups 会议将帮助你微调音频 App 和插件。所以当你调试、测试和性能分析 App 时，记住你可以在任何 Mac 上构建，但运行原生 arm64 代码需要 Apple 芯片 Mac。运行测试时，尝试在原生和被翻译模式下都运行，以发现测试中的不可移植代码。注意任何 Intel 特定的代码优化以及使用忙等待而非阻塞的代码。下一个我想讨论的话题是插件，因为这些在 Apple 芯片电脑上需要一些特殊考虑。插件是一种动态加载和执行代码的方式。使用仅实现通过 NSExtension 的标准系统扩展点的插件将会直接工作：原生和被翻译的插件都得到支持。然而，如果你的 App 是插件宿主，并且它使用自定义的插件加载机制，你将需要考虑插件在 Apple 芯片 Mac 上如何工作。你的 App 的进程在运行时将包含你写的代码以及来自系统框架的代码。如果你的 App 支持插件，它通常会在运行时发现它们，然后在需要时加载它们。这称为进程内插件模型，通常 App 使用 dlopen 或 Bundle.load 的调用来实现。

或者，插件可以作为新进程生成，我们称那些为进程外插件。App 和插件进程然后使用某种进程间通信机制，如 XPC。加载另一个插件通常会生成另一个进程。虽然进程外插件通常提供更好的安全性和稳定性，但进程内插件仍然非常常见。如果你的 App 使用进程内插件，你需要考虑在 macOS 上的 Apple 芯片，一个进程中的所有代码必须始终具有相同的 CPU 架构。让我们看看插件的典型用例。如我所提到的，有进程外和进程内插件。同样重要的是插件是一方的，这意味着你从源代码构建并在 App 内发布它，还是三方插件，由其他软件供应商以预编译二进制形式分发。如果你的插件是一方的并且你可以重新构建它们，确保把它们构建为通用插件，一切都会工作。对于使用进程外插件模型的三方插件，你可以在加载代码中做一些小改动以支持两种 CPU 架构。如果你确保以正确的 CPU 架构加载插件可执行文件，你的 App 将能够加载原生和被翻译的插件。进程内三方插件有一些限制。原生 App 只能加载原生插件，Rosetta 被翻译的 App 只能加载基于 Intel 的插件。

如果你的插件供应商尚未把插件更新为通用，它可能影响你的用户。让我们看看如果我们有插件 CPU 不匹配会发生什么。在我的网络基准测试 App 中，我使用一个插件来实现 TLS 支持。它在我第一次切换到 TLS 模式时加载，让我这样做。插件加载失败，让我们检查控制台。动态链接器解释了发生了什么。我们试图使用 dlopen 加载一个具有这个名称的插件，文件在磁盘上找到了，但它有错误的 CPU 架构。让我们验证一下。我将复制这个文件的完整路径并打开 Terminal，然后把路径粘贴到 Terminal 并再次使用 lipo -info。确实这个二进制仅 Intel。

现在如果这是三方预编译插件，正确的解决方案是联系该三方并敦促他们尽快发布插件的通用构建。但让我们回到 Xcode，因为本例中我确实有这个插件的源代码，我应该能够把它重新构建为通用。让我们进入我的项目，打开 TLS 插件 target，检查其 Build Settings。看起来我有一些不寻常的配置。我强制 Architectures 始终为 x86_64。这可能是我想放弃 32 位支持时的遗留，但硬编码 x86_64 现在不正确了。我们反而应该到处使用 Standard Architectures。但更好的选择是干脆根本不设置 Architectures。所以我将只需选择该构建设置并按 Delete 键。这样 Xcode 将使用正确的默认设置。让我们再次构建并运行 App，这次如果我切换到 TLS 模式，插件现在将正确加载。加载插件的典型模式是使用带文件路径的 dlopen。始终检查 dlopen 的返回值非常重要，如果它是 NULL，调用 dlerror 会提供解释什么出错的完整错误消息。当用不匹配的插件 CPU 架构运行此代码时，你会得到一个错误，解释磁盘上的哪个文件有错误的架构。这表明插件不是通用的。我想指出进程外插件模型没有这个限制。如果你使用进程内插件，我鼓励你探索 XPC 作为解决方案。你可以每个插件一个进程，也可以每个 CPU 架构一个进程。在这种情况下，你最多只会使用两个额外进程。进程外插件为你的 App 提供更好的稳定性和安全性，关于 XPC 的详情我推荐观看 2013 年的 WWDC 会议《Efficient Design with XPC》。如果你的用户困在 Intel-onl...（原文截断）

在 Xcode 中，你的分发过程从归档构建开始，现在默认生成通用 App。在 Xcode 中，Archive 操作在 Product 菜单中可用。如果你的主要开发工作流只使用一种类型的 Mac 电脑，做归档构建实际上可能是你的代码首次通用构建。所以如果你的调试迭代构建正常，但归档构建失败，那表明存在我们本节前面涵盖的可移植性问题。一旦归档构建成功，你可以在 Xcode 的 Organizer 窗口中找到用于分发的包。在 Xcode 12 中，它现在显示归档构建中包含哪些 CPU 架构。Organizer 还提供对用户 App 的崩溃统计和单个崩溃日志的访问。关于崩溃日志以及如何调查崩溃的根本原因的详情，请观看 WWDC 2018 的视频《Understanding Crashes and Crash Logs》。使用通用 App 时，现在要注意你将收到三种不同的崩溃日志：来自 Intel Mac 的 x86 崩溃日志、来自 Apple 芯片 Mac 的原生 arm64 崩溃日志，以及在 Apple 芯片 Mac 上 Rosetta 下运行时的被翻译 x86 崩溃日志。如果你在 Organizer 中选择特定的崩溃日志，Details 部分现在显示崩溃发生在哪个 CPU 架构上，以及进程是否在被翻译。如果你的 App 依赖内核扩展，或你使用 DriverKit 为硬件提供驱动程序，在迁移这类软件时有一些特殊考虑需要理解。特别是，在 Apple 芯片 Mac 上更多类型的内核扩展现在被废弃或禁止，你将不得不改用 DriverKit。请参阅 macOS 迁移文档了解详情。还有一件事要注意是多线程 bug。Intel CPU 和 Apple 芯片实现了不同的内存排序模型。为了正确的多线程……（原文截断）

最后，我想提醒你 developer.apple.com/documentation 包含更多详情。名为 Apple Silicon 的文章提供了关于迁移 App 的指导和你可能有的问题的答案。感谢观看。
