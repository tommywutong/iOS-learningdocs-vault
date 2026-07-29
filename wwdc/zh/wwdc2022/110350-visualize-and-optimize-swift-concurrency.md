---
title: 可视化与优化 Swift 并发
session_id: 110350
collection: wwdc2022
year: 2022
duration: '24:38'
topics: [Swift]
group: C · 并发、锁与线程
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2022/110350/'
content_hash: 'sha256:f2b0b4c3ab802649'
translated: true
---

# 可视化与优化 Swift 并发

<sub>WWDC2022 · 24:38 · Swift</sub>

了解如何通过 Instruments 中的 Swift 并发模板优化你的 App。我们将讨论常见的性能问题并展示……

> [!note] 归档理由
> 使用 Instruments 查看并发的运行时行为（可视化调度）

## 相关资源

- [Concurrency](https://developer.apple.com/documentation/Swift/concurrency)
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/110350/4/3B87EB1E-4E88-4D11-817A-16852AEA794C/downloads/wwdc2022-110350_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/110350/4/3B87EB1E-4E88-4D11-817A-16852AEA794C/downloads/wwdc2022-110350_sd.mp4?dl=1)
- [使用 Instruments 分析挂起](https://developer.apple.com/videos/play/wwdc2023/10248)
- [超越结构化并发的基础](https://developer.apple.com/videos/play/wwdc2023/10170)
- [使用 Swift 并发消除数据争用](https://developer.apple.com/videos/play/wwdc2022/110351)
- [问答：Swift 并发](https://developer.apple.com/videos/play/wwdc2022/110480)
- [使用 Xcode 和设备端检测追踪挂起](https://developer.apple.com/videos/play/wwdc2022/10082)
- [Swift 新功能](https://developer.apple.com/videos/play/wwdc2022/110354)
- [UIKit 新功能](https://developer.apple.com/videos/play/wwdc2022/10068)
- [探索 Swift 中的结构化并发](https://developer.apple.com/videos/play/wwdc2021/10134)
- [认识 Swift 中的 async/await](https://developer.apple.com/videos/play/wwdc2021/10132)
- [利用 Swift Actor 保护可变状态](https://developer.apple.com/videos/play/wwdc2021/10133)
- [Swift 并发：幕后探秘](https://developer.apple.com/videos/play/wwdc2021/10254)
- [Swift 并发：更新示例 App](https://developer.apple.com/videos/play/wwdc2021/10194)
- [CompressionState 类](https://developer.apple.com/videos/play/wwdc2022/110350/?time=624)
- [使用 ParallelCompressor Actor 的 CompressionState 类](https://developer.apple.com/videos/play/wwdc2022/110350/?time=709)
- [使用具有最小 Actor 隔离和分离任务的 ParallelCompressor 的 CompressionState 类](https://developer.apple.com/videos/play/wwdc2022/110350/?time=1066)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ 欢迎收看《可视化与优化 Swift 并发》。我是 Mike，在 Swift 运行时库团队工作。你好，我是 Harjas，我在 Instruments 团队工作。我们将一起探讨如何更好地理解你的 Swift 并发代码并使其运行更快，其中包括 Instruments 14 中提供的一个新的可视化工具。首先，我们来快速回顾一下 Swift 并发的各个组成部分及其协同工作方式，确保你跟上节奏。之后，我们将演示新的并发检测工具。我们会展示如何使用它来解决一个使用 Swift 并发的 App 中遇到的一些实际性能问题。最后，我们将讨论线程池耗尽和 continuation 的潜在问题以及如何避免它们。去年，我们推出了 Swift 并发。这是一个新的语言特性，包括 async/await、结构化并发和 Actor。我们很高兴看到这些特性自那以后得到了大量应用，无论是在 Apple 内部还是外部。Swift 并发为语言增加了几个新特性，它们协同工作，使并发编程更简单、更安全。Async/await 是并发代码的基本语法构建块。它们允许你创建和调用那些可以在执行过程中暂停工作，稍后恢复工作，而不会阻塞执行线程的函数。

任务（Task）是并发代码中的基本工作单元。任务执行并发代码并管理其状态和相关数据。它们包含局部变量、处理取消操作，以及开始和暂停异步代码的执行。结构化并发使得生成子任务并行运行并等待它们完成变得容易。该语言提供了语法来保持工作分组，并确保任务被等待或在不再使用时自动取消。Actor 协调多个需要访问共享数据的任务。它们将数据与外界隔离，并只允许一次一个任务操作其内部状态，从而避免因并发修改导致的数据争用（data race）。在 Instruments 14 中，我们推出了一套新的检测工具，可以捕获并可视化你 App 中的所有此类活动，帮助你了解 App 正在做什么，定位问题，并提高性能。关于 Swift 并发基础的更深入讨论，我们在相关视频部分链接了多部关于这些特性的视频。

让我们来看看如何优化一个使用 Swift 并发代码的 App。Swift 并发使得编写正确、并发的并行代码变得容易。然而，仍然有可能编写误用并发构造的代码。也有可能虽然正确使用了它们，但方式并未达到你期望的性能收益。

在编写使用 Swift 并发的代码时，可能会出现一些常见问题，导致性能不佳或出现 Bug。主要 Actor（main actor）阻塞会导致你的 App 挂起。Actor 争用和线程池耗尽（thread pool exhaustion）会通过减少并行执行来损害性能。continuation（一种用于桥接异步回调的机制）误用会导致泄漏或崩溃。新的 Swift 并发检测工具可以帮助你发现并修复这些问题。让我们逐一看看这些问题，首先从主要 Actor（main actor）阻塞开始。当长时间运行的任务在主要 Actor 上运行时，就会发生主要 Actor 阻塞。主要 Actor 是一个特殊的 Actor，它在主线程上执行其所有工作。UI 工作必须在主线程上完成，而主要 Actor 允许你将 UI 代码集成到 Swift 并发中。然而，由于主线程对于 UI 如此重要，它必须保持可用，不能被长时间运行的工作单元占据。当这种情况发生时，你的 App 看起来会锁定并且无响应。在主要 Actor 上运行的代码必须快速完成，要么完成其工作，要么将计算从主要 Actor 移出到后台。可以通过将工作放入普通 Actor 或分离任务（detached task）中，将其移至后台。可以在主要 Actor 上执行小的工作单元来更新 UI 或执行其他必须在主线程上完成的任务。让我们现场演示一下。谢谢，Mike。这里是我们开发的 File Squeezer 应用程序。我们构建这个应用程序是为了能够快速压缩文件夹中的所有文件。对于小文件来说，它似乎运行得还可以。然而，当我使用更大的文件时，它花费的时间比预期的要长得多，而且 UI 完全冻结，对任何交互都没有响应。这种行为让用户感到非常不快，可能会让他们认为应用程序已经崩溃或永远不会完成。为了获得最佳用户体验，我们应该努力确保我们的 UI 始终保持响应。要调查这个性能问题，我们可以使用 Instruments 中新的 Swift 并发模板。Swift 任务和 Swift Actor 检测工具提供了一套完整的工具，帮助你可视化和优化你的并发代码。当你刚开始调查性能问题时，首先应该查看 Swift 任务检测工具提供的顶层统计数据。首先是「运行中任务（Running Tasks）」，它显示同时执行的任务数。接下来是「存活任务（Alive Tasks）」，它显示在给定时间点存在的任务数。最后是「总任务（Total Tasks）」，它绘制截至某个时间点已创建的任务总数。当你试图减少应用程序的内存占用空间时，应密切关注「存活任务」和「总任务」统计数据。所有这些统计数据的结合，能让你清楚地了解你的代码并行化程度以及消耗了多少资源。该检测工具的众多详细视图之一是「任务森林（Task Forest）」；显示在此窗口的下半部分，它以图形方式表示结构化并发代码中任务之间的父子关系。接下来是我们的「任务摘要（Task Summary）」视图。它显示每个任务在不同状态下花费的时间。我们通过允许你右键点击某个任务，将包含该任务所有信息的轨道固定到时间轴上，极大地增强了该视图的功能。这使你能够快速找到并了解可能运行时间很长、或因为等待访问某 Actor 而卡住的任务。一旦你将一个 Swift 任务固定到时间线，你将获得四个关键功能。首先，是显示你的 Swift 任务所处状态的轨道。其次，是在扩展详细视图中的任务创建回溯（backtrace）。第三，是叙述视图，它提供有关 Swift 任务状态的更多上下文。例如，如果它在等待一个任务，它会告知你正在等待哪个任务。最后，你可以在叙述视图中访问与摘要视图中相同的固定操作。因此，你可以将子任务、线程甚至 Swift Actor 固定到时间线上。这个叙述视图对于发现 Swift 任务如何与其他并发原语和 CPU 相关至关重要。现在我们已经简要了解了新检测工具的一些功能，让我们分析一下我们的应用程序并优化代码。我们可以通过在 Xcode 中打开项目并按 Command-I 来做到这一点。这会编译我们的应用程序，打开 Instruments，并预先选择目标为 File Squeezer 应用程序。在这里，你可以在模板选择器中选择 Swift 并发选项并开始录制。

再一次，我将把大文件拖放到应用程序上。

再次，我们看到应用程序开始旋转，并且 UI 没有响应。我们将让它再运行几秒钟，以便 Instruments 能够捕获我们应用程序的所有信息。

现在我们有了追踪数据，可以开始调查了。我将全屏显示这条轨迹，以便更好地查看所有信息。

我们可以使用 Option-拖拽来放大我们关注的区域。

在进程轨道中，Instruments 精确地显示了这次 UI 挂起发生的位置。这在不确定挂起何时发生或持续多长时间时非常有用。正如我前面提到的，一个好的起点是顶层的 Swift 任务统计数据。立即引起我注意的是「运行中任务」计数。在大部分时间里，只有一个任务在运行。这告诉我们部分问题是所有的工作都被强制序列化了。我们可以使用任务状态摘要来找到我们运行时间最长的任务，并使用固定操作将其固定到时间线上。

这个任务的叙述视图告诉我们，它在后台线程上运行了一小段时间，然后长时间在主线程上运行。为了进一步调查，我们可以将主线程固定到时间线上。

主线程被几个长时间运行的任务阻塞了。这证明了 Mike 提到的「主要 Actor 阻塞」问题。所以我们必须问自己，“这个任务在做什么？” 以及 “这个任务来自哪里？” 我们可以切换回叙述视图来回答这两个问题。扩展详细视图中的创建回溯显示该任务是在 `compressAllFiles` 函数中创建的。叙述显示该任务正在执行 `compressAllFiles` 中的闭包一号。通过右键单击这个符号，我们可以在源代码查看器中打开它。

这个函数内部的闭包一号正在调用我们的压缩工作。现在我们知道这个任务是在哪里创建的以及它在做什么，我们可以在 Xcode 中打开我们的代码并修改它，这样我们就不会在主线程上运行这些繁重的计算。`compressFile` 函数位于 `CompressionState` 类中。整个 `CompressionState` 类被注解为在 `@MainActor` 上运行。这解释了为什么该任务也在主线程上运行。我们需要整个类在 MainActor 上，因为这里的 `@Published` 属性必须仅从主线程更新，否则我们可能会遇到运行时问题。因此，我们可以尝试将这个类转换成它自己的 Actor。然而，编译器会告诉我们不能这样做，因为本质上我们是在说这个共享的可变状态需要由两个不同的 Actor 来保护。但这确实给了我们关于真正解决方案的提示。在这个类中，我们有两个不同的可变状态。状态的一部分，即 `files` 属性，需要隔离到 MainActor，因为它被 SwiftUI 观察。但对另一部分状态，即日志（logs）的访问，需要防止并发访问，但哪个线程在任意时刻访问日志并不重要。因此，它实际上不需要在主要 Actor 上。不过我们仍然希望保护它免受并发访问，所以我们将其封装到它自己的 Actor 中。我们现在需要做的就是添加一种方式，让任务在两者之间按需跳转。我们可以创建一个新的 Actor，命名为 `ParallelCompressor`。

然后我们可以将日志状态复制到新的 Actor 中，并添加一些额外的设置代码。

从这里开始，我们需要让这些 Actor 相互通信。首先，让我们从 `CompressionState` 类中移除引用 `logs` 变量的代码，并将其添加到我们的 `ParallelCompressor` Actor 中。

最后，我们需要更新 `CompressionState`，让其调用 `ParallelCompressor` 上的 `compressFile` 方法。

通过这些更改，让我们再次测试我们的应用程序。再次，我将把大文件拖放到我们的应用程序上。

UI 不再挂起，这是一个很大的改进，但我们没有得到预期的速度。我们真的很想充分利用机器中的所有核心来尽可能快地完成这项工作。Mike，我们还应该注意什么？Mike: 我们通过将工作移出主要 Actor 解决了挂起问题，但我们仍然没有得到我们想要的性能。要了解原因，我们需要更仔细地研究 Actor。Actor 使得多个任务安全地操作共享状态成为可能。然而，它们是通过序列化对共享状态的访问来实现这一点的。一次只允许一个任务占用 Actor，而其他需要使用该 Actor 的任务将等待。Swift 并发允许使用非结构化任务、任务组和 async let 进行并行计算。理想情况下，这些构造能够同时使用多个 CPU 核心。当在这样的代码中使用 Actor 时，请注意不要在这些任务共享的 Actor 上执行大量工作。当多个任务尝试同时使用同一个 Actor 时，Actor 会序列化这些任务的执行。因此，我们失去了并行计算的性能优势。

这是因为每个任务都必须等待 Actor 变得可用。要解决这个问题，我们需要确保任务只在真正需要独占访问 Actor 数据时才在 Actor 上运行。其他所有操作都应在 Actor 之外运行。我们将任务分块。某些块必须在 Actor 上运行，而其他块则不需要。非 Actor 隔离的块可以并行执行，这意味着计算机可以更快地完成工作。让我们现场演示一下。Harjas: 谢谢，Mike。让我们看看我们更新后的 File Squeezer 应用程序的追踪数据，并牢记 Mike 刚刚教给我们的内容。任务摘要视图显示我们的并发代码在「已入队（Enqueued）」状态下花费了大量时间。这意味着我们有很多任务在等待获取某个 Actor 的独占访问权。让我们固定其中一个任务来了解原因。

这个任务在等待进入 `ParallelCompressor` Actor 上花费了相当长的时间，然后才运行压缩工作。让我们将这个 Actor 固定到我们的时间线上。

这里是一些关于 `ParallelCompressor` Actor 的顶层数据。这个 Actor 的队列似乎被一些长时间运行的任务阻塞了。任务只应在需要的时候停留在 Actor 上。让我们回到任务叙述。

在 `ParallelCompressor` 入队之后，该任务在 `compressAllFiles` 中的闭包一号中运行。那么让我们从那里开始调查。源代码显示这个闭包主要运行我们的压缩工作。由于 `compressFile` 函数是 `ParallelCompressor` Actor 的一部分，这个函数的整个执行过程都发生在 Actor 上；阻塞了所有其他的压缩工作。要解决这个问题，我们需要将 `compressFile` 函数从 Actor 隔离中提取出来，放到一个分离任务（detached task）中。

通过这样做，我们可以让分离任务只在需要更新相关可变状态时才短暂地停留在 Actor 上。现在 `compress` 函数可以在线程池中的任何线程上自由执行，直到它需要访问 Actor 保护的状态。例如，当它需要访问 `files` 属性时，它会移动到主要 Actor 上。但是一旦它在那边完成，它就立即回到「并发之海」中，直到它需要访问 `logs` 属性，为此它会移动到 `ParallelCompressor` Actor 上。同样，一旦它在那边完成，它就再次离开 Actor，在线程池上执行。当然，我们不仅仅只有一个任务在做压缩工作；我们有很多个。并且由于不受 Actor 的约束，它们都可以并发执行，唯一限制是线程数量。

当然，每个 Actor 一次只能执行一个任务，但在大多数时间里，我们的任务不需要停留在 Actor 上。所以，正如 Mike 解释的，这允许我们的压缩任务并行执行，并利用所有可用的 CPU 核心。那么我们现在就来进行这个更改。

我们可以将 `compressFile` 函数标记为 `nonisolated`。

这会导致一些编译器错误。通过将其标记为 `nonisolated`，我们告诉 Swift 编译器我们不需要访问这个 Actor 的共享状态。但这并不完全正确。这个 `log` 函数是 Actor 隔离的，它需要访问共享的可变状态。为了解决这个问题，我们需要将这个函数改为异步的，然后将所有 `log` 调用标记上 `await` 关键字。

现在我们需要更新任务的创建方式，改为创建一个分离任务。

我们这样做是为了确保任务不会继承它被创建时的 Actor 上下文。对于分离任务，我们需要显式地捕获 `self`。

让我们再次测试我们的应用程序。

App 能够同时压缩所有文件，并且 UI 保持响应。为了验证我们的改进，我们可以检查 Swift Actor 检测工具。查看 `ParallelCompressor` Actor，在 Actor 上执行的大部分工作持续时间都很短，并且队列大小从未失控。回顾一下，我们使用检测工具隔离了 UI 挂起的原因，重构了并发代码以获得更好的并行性，并使用数据验证了性能改进。现在 Mike 将告诉我们一些其他潜在的性能问题。Mike: 除了我们在演示中看到的，还有两个常见问题我想谈谈。首先，让我们讨论一下线程池耗尽。线程池耗尽会损害性能，甚至导致应用程序死锁。Swift 并发要求任务在运行时必须持续推进。当一个任务在等待某事时，它通常通过暂停（suspending）来实现。然而，任务内的代码有可能在不暂停的情况下执行阻塞调用，例如阻塞文件 IO 或网络 IO，或获取锁。这打破了任务必须持续推进的要求。当这种情况发生时，任务继续占据它正在执行的线程，但实际上并没有使用 CPU 核心。由于线程池是有限的，并且其中一些被阻塞，并发运行时无法充分利用所有 CPU 核心。这减少了可以完成的并行计算量，并限制了 App 的最大性能。在极端情况下，当整个线程池都被阻塞的任务占据，并且它们正在等待某个需要新任务在线程池上运行的事件时，并发运行时可能发生死锁。确保避免在任务中进行阻塞调用。文件 IO 和网络 IO 必须使用异步 API 执行。避免等待条件变量或信号量。如果需要，可以持有细粒度、短暂持有的锁，但应避免具有大量争用或持有时间过长的锁。如果你的代码需要执行这些操作，请将该代码移出并发线程池——例如，通过将其在 Dispatch 队列上运行——并使用 continuation 将其桥接到并发世界。尽可能使用异步 API 进行阻塞操作，以保持系统平稳运行。当你使用 continuation 时，必须小心正确地使用它们。Continuation 是 Swift 并发与其他形式异步代码之间的桥梁。continuation 暂停当前任务，并提供一个回调，该回调在被调用时恢复任务。这可以用于基于回调的异步 API。从 Swift 并发的角度来看，任务暂停，然后在 continuation 被恢复时恢复。从基于回调的异步 API 的角度来看，工作开始，然后在工作完成时调用回调。Swift 并发检测工具能够识别 continuation，并会相应地标记时间间隔，向你显示任务正在等待调用 continuation。continuation 回调有一个特殊要求：它们必须被精确调用一次，不能多也不能少。这在基于回调的 API 中是一个常见要求，但往往是非正式的，并且不由语言强制执行，因此遗漏很常见。Swift 并发使其成为一个硬性要求。如果回调被调用了两次，程序会崩溃或行为异常。如果回调从未被调用，任务就会泄漏。在这个代码示例中，我们使用 `withCheckedContinuation` 来获取一个 continuation。然后我们调用一个基于回调的 API。在回调中，我们恢复 continuation。这满足了精确调用一次的要求。当代码更复杂时，务必小心。在左边，我们修改了回调，使其仅在成功时恢复 continuation。这是一个 Bug。失败时，continuation 不会被恢复，任务将永远暂停。在右边，我们恢复了两次 continuation。这也是一个 Bug，App 将行为异常或崩溃。这两个片段都违反了精确恢复一次 continuation 的要求。有两种类型的 continuation 可用：checked 和 unsafe。除非性能至关重要，否则始终使用 `withCheckedContinuation` API。Checked continuations 会自动检测误用并标记错误。当 checked continuation 被调用两次时，continuation 会触发陷阱（trap）。当 continuation 从未被调用时，在 continuation 被销毁时会向控制台打印一条消息，警告你 continuation 泄漏了。Swift 并发检测工具会显示相应的任务无限期地卡在 continuation 状态中。关于 Instruments 中新的 Swift 并发模板，还有更多内容可以探索。你可以获得结构化并发的图形可视化，查看任务创建调用树，并检查精确的汇编指令，以获得对 Swift 并发运行时的全面了解。要了解更多关于 Swift 并发底层工作原理的信息，请观看去年的讲座「Swift 并发：幕后探秘」。要了解更多关于数据争用的信息，请观看「使用 Swift 并发消除数据争用」。感谢收看！祝你调试并发代码愉快。
