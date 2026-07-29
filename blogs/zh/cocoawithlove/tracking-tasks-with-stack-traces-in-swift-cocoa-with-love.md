---
title: 在 Swift 中使用堆栈跟踪追踪任务 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/02/28/stack-traces-in-swift.html'
original_language: en
published: 2016-02-28
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:594cce39a87205e6'
translated: true
---

> 原文：[Tracking tasks with stack traces in Swift | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/02/28/stack-traces-in-swift.html)　·　Cocoa with Love (Matt Gallagher)

调试具有复杂或异步控制流（control flow）的任务可能会很困难，因为它让你最重要的调试工具之一——调试器堆栈跟踪（stack trace）——变得毫无用处。为了克服这一点，我们可以在 Debug 构建中让自己的任务捕获其自身的堆栈跟踪，通过重建长时间运行的任务对象在程序中所经过的路径来辅助调试。

本文还将分享我自己的自定义代码，用于创建和符号化（symbolicate）堆栈跟踪，这些代码比 Swift 中现有的实现更快、更灵活。

## 概述

分析程序以查找错误来源的最佳方式之一就是调试器堆栈跟踪。

假设我们在函数 (1) 中创建一个任务对象，然后将该任务对象传入另一个函数 (2)，函数 (2) 接着将任务对象传入第三个函数 (3)，后者代表任务的终点。在这个例子中，对象在程序中所经路径与调用栈是相同的：

![一个线性的三节点图](https://www.cocoawithlove.com/assets/blog/three_node_graph.svg)

如果在函数 (3) 结束时你没有得到预期的结果，可以在函数 (3) 的末尾设置一个断点，调试器中的堆栈跟踪将显示函数 (2) 和函数 (1) 位于栈中函数 (3) 之前。这样你就知道了任务从创建到完成所经过的函数路径。如果任务纯粹作为一系列嵌套调用来处理，那么最深处的调试器堆栈跟踪将捕获任务的完整历史，而重建控制流就像读取这条堆栈跟踪一样简单。

不幸的是，很多任务并非如此简单。对象不仅会被传入函数，也会从函数中返回，这会导致它们的源帧（source frame）在此过程中从调用栈中消失。对象还会在线程（thread）之间传递，这会使调用栈中其生命周期内的所有先前步骤全部丢失。

假设对象经过的三步简单路径变成了这样：

![一个非线性的三节点图](https://www.cocoawithlove.com/assets/blog/three_layer_graph.svg)

在此图中，函数 (2) 调用函数 (1)，任务对象在函数 (1) 中创建。然后函数 (1) 将任务对象返回给函数 (2)，函数 (2) 再异步地将对象传递给函数 (3)。

一旦函数 (1) 返回到函数 (2)，它随即从堆栈跟踪中消失；而当函数 (3) 被异步调用时，函数 (2) 也会从堆栈跟踪中消失。当你在函数 (3) 结束时发现问题时，你已经丢失了对象在程序中控制流的历史记录。

在这种情况下，如何才能保持足够的计算信息，以便在步骤 (3) 进行有用的响应式分析？

## 我们可以使用日志文件

传统上，我们通过日志文件（log file）来解决这类控制流追踪问题。我们记录任务对象的构建，记录将对象从一个线程交给另一个线程的时刻，并记录其结束。阅读日志文件，我们就可以看到发生了什么事件以及何时发生。

不过，日志文件最大的问题是控制它包含的信息量。日志文件通常是程序全局的，会将所有任务的事件记录在同一个位置。如果多个任务同时发生，它们在日志文件中会相互交错。如果你的程序中任务很多，日志会变得极其难以阅读。

日志文件的另一个问题是，它的帮助程度完全取决于你选择写入的信息——它们不会隐式地收集信息。良好的日志记录需要花费非零的时间来写出好的日志消息。

最后，日志记录只捕获当前作用域的信息。这使得日志信息在可复用代码中帮助大大降低，因为在这种代码中，你往往对调用方（call site）比可复用的被调用方（callee）更感兴趣。

## 改用堆栈跟踪日志

与其使用日志文件来追踪异步任务，我更喜欢使用一种我称之为“任务日志（task journal）”的结构。它并不是一个复杂的数据结构。下面是一个例子：

```swift
#if DEBUG
   var taskJournal: [[UInt]] = [callStackReturnAddresses()]
#endif
```

它本质上是一个堆栈跟踪数组，其中每条堆栈跟踪就是一组返回地址（`UInt`），我们可以稍后用它来重构函数以及这些函数内的偏移量。

与用于追踪控制流的日志文件相比，这种任务日志具有以下优势：

1. 它在你需要之前都不会碍事（不会被塞进一个公共位置）
2. 它对每个任务都独立（即使多个任务同时发生，也保持可读）
3. 它捕获调用者的信息，使其在**可复用**类中也很有用

初始的堆栈跟踪（由 `callStackReturnAddresses` 捕获）在 `taskJournal` 初始化时添加，当你的任务到达一个有趣的序列点（条件分支、接口边界或其他交接点）时，你可以追加一条堆栈跟踪。

日志文件在追踪控制流之外还有许多其他用途；我不是要提议用堆栈跟踪来取代日志文件。日志文件仍然是追踪多个任务聚合进度的最佳解决方案。日志文件也可以是持久化的、用户可读的，这使它们在简单的调试分析之外也很有用。

鉴于你习惯了日志文件，你可能会自然而然地觉得需要在堆栈跟踪里附带一条消息，但这条消息通常就是“我在这里”，而这一点堆栈跟踪已经隐含了。

这并不是说你不应该为任务存储额外的元数据——比如“该任务以参数 X、Y 和 Z 创建”或“任务收到错误消息 E”这类信息非常有用——但这些通常应该以适合你任务上下文的自定义格式存储。任务日志的关键目的，是提供不需要任何自定义格式、结构或消息的元数据——你只需在想添加序列点时添加即可。

## 等等……我们到底为什么要这么做？

从 Xcode 6 开始，Xcode 可以在使用 dispatch queue 异步调度 block 时自动记录回溯（backtrace），这样你就可以跟随调用栈跨越多次异步调用。你可以在 [WWDC 2014 的 Debugging in Xcode 6](https://developer.apple.com/videos/play/wwdc2014/413/) 中看到这一功能的实际演示。

我们还需要自己捕获堆栈跟踪吗？

Xcode 只会在 dispatch queue 上调度时记录回溯。你无法控制这些回溯，因此也无法在其他情况下请求它们。所以，有很多重要的控制流行为是它无法捕获的：

1. 不使用 dispatch 的持续任务，包括网络连接和用户输入等常见任务
2. 发生在单个线程上的操作，如基本的函数调用或选择了某个分支而非另一个

即便你想追踪的控制流就是 dispatch queue 上 block 的异步调用，Xcode 中记录的回溯也依赖于隐式行为。有时它工作，有时不工作，而当回溯根本不出现时，你得不到任何反馈。例如：在 Xcode 7.2.1 中，对我来说，Xcode 记录的回溯在 xctest 目标里似乎完全不起作用。我不知道这是“已知限制”还是 bug，但这让我需要一个替代方案。

## 捕获堆栈跟踪

在前面的例子中，我写了 `callStackReturnAddresses` 来捕获当前的堆栈跟踪。Swift 或 Cocoa 中并不存在这个名称的自由函数。

`NSThread` 上有一个同名的类方法，所以我们可以这样写：

```swift
var taskJournal: [[UInt]] = [Thread.callStackReturnAddresses()]
```

不幸的是，无论是 `NSThread` 还是 Foundation 中的任何其他类，都没有提供一种可以在将来需要时轻松将地址转换为符号的方法。

`NSThread` 上有另一个替代函数：

```swift
let trace = NSThread.callStackSymbols()
```

它会立即把返回地址转换成符号，但这对于附加到我们主要任务机制来说实在太耗时了（我们只希望在错误发生后才转换为符号，而不是在关键路径上这样做，因为在关键路径上我们可能需要每秒捕获数百甚至数千条堆栈跟踪）。

因此，出于性能原因，我们需要坚持使用基本的返回地址，并且需要再用 C 函数 `dladdr` 自己把它们转换为符号。至少 `NSThread.callStackReturnAddresses` 不会是一个完整的解决方案。

但我对 `NSThread` 实现还有另一个不满：你不能跳过栈顶的那几个栈帧，也不能限制捕获的帧数。使用 `NSThread.callStackReturnAddresses`，你必须总是捕获整个栈，然后再把结果裁剪到你实际需要的信息——这会强制重新分配内存并浪费时间。

如果我们能使用 C 函数 `backtrace`，会有更多灵活性，但在 Swift 中我们做不到。`backtrace` 函数来自 `execinfo.h` 头文件，并作为 libSystem 的一部分实现在 OS X 和 iOS 上（所有 Swift 程序都会链接到这个库），但出于某种原因，`execinfo.h` 的内容并未暴露给 Swift 程序。

## 自己动手实现

虽然 `NSThread.callStackReturnAddresses` 的功能对多数人来说可能已经足够，但我对它并不满意，所以我还是费心在 Swift 中重新实现了它，并加入了我想要的特性：

```swift
/// Traverses the frames on current stack and gathers the return addresses for traversed
/// stack frames as an array of UInt.
/// - parameter skip: number of stack frames to skip over before copying return addresses
///   to the result array.
/// - parameter maximumAddresses: limit on the number of return addresses to return
///   (default is `Int.max`)
/// - returns: The array of return addresses on the current stack within the
///   skip/maximumAddresses bounds.
@inline(never)
public func callStackReturnAddresses(skip: UInt = 0, maximumAddresses: Int = Int.max) ->
   [UInt]
```

为了支撑这个函数，我还写了：

```swift
/// When applied to the output of callStackReturnAddresses, produces identical output to
/// the execinfo function "backtrace_symbols" or Thread.callStackSymbols
/// - parameter addresses: an array of memory addresses, generally as produced by
///   `callStackReturnAddresses`
/// - returns: an array of formatted, symbolicated stack frame descriptions.
public func symbolsForCallStack(addresses: [UInt]) -> [String]
```

它可以接收 `[UInt]`，并按需生成与 `Thread.callStackSymbols()` 格式完全相同的调用栈符号。

## 使用这些函数的一个简单示例

我有时会使用一个名为 `DeferredWork` 的类。这个对象包装了一个闭包（closure），该闭包被推迟到以后执行。该类有一个严格的使用要求：在 `DeferredWork` 对象被删除之前的某个时刻，**必须**运行该工作，但它不会自动运行；必须手动触发。

该类的简化版本大致如下（注意：此代码假定 `DEBUG` 在 Debug 构建中已定义）：

```swift
class DeferredWork {
   let work: () -> Void

#if DEBUG
   // The task journal captures the stack trace on construction
   var taskJournal: [[UInt]] = [callStackReturnAddresses()]
   var didRun = false
#endif

   init(work: () -> Void) {
      self.work = work
   }
   
   func run() {
      work()
#if DEBUG
      didRun = true
#endif
   }

   func recordHandover() {
#if DEBUG
      // We can append additional stack traces whenever we wish.
      // For DeferredWork, this is intended to be done on ownership changes.
      taskJournal.append(callStackReturnAddresses())
#endif
   }
   
#if DEBUG
   deinit {
      if !didRun {
         // A "didn't run" condition at this point constitutes a failure.
         // We symbolicate and format the stack traces and trigger a fatal error.
         let traces = taskJournal.map {
            symbolsForCallStackAddresses($0).joinWithSeparator("\n")
         }
         preconditionFailure("Failed to perform work deferred at location:\n" +
            traces.joinWithSeparator("\n\nWith handover at:\n"))
      }
   }
#endif
}
```

为了解释它的原理：当 `DeferredWork` 类被创建时，它取得 `work` 闭包的所有权，并同意稍后运行该闭包。构建该实例的位置作为 `taskJournal` 的第一个元素被保存下来。

如果 `DeferredWork` 被移交给另一个所有者，可以手动调用 `recordHandover` 函数，记录所有权的变更。

最终，如果出现问题——对这个类来说，“问题”是指在 `deinit` 之前未能调用 `run`——我们就知道 `work` 闭包从何而来，也知道将它带到当前位置的保管链，从而能够快速定位未能运行的确切位置。

我们来看看，它是如何解决我上面展示的那个有问题的三步骤控制流的：

![一个非线性的三节点图](https://www.cocoawithlove.com/assets/blog/three_layer_graph.svg)

`DeferredWork.init` 是函数 (1)。`recordHandover` 函数应在函数 (2) 末尾的异步调用之前立即调用。当 `DeferredWork` 对象离开作用域时，`deinit` 函数在函数 (3) 末尾被调用。如果在函数 (2) 或函数 (3) 期间的任何时刻没有调用 `run` 函数，我们就可以立即看到对象在程序中所经过的路径，并判断在哪里犯了错。

## callStackReturnAddresses 的实现

和所有代码一样，我更喜欢在 Swift 中实现一切，但 Swift 缺少与 gcc/clang 内建函数 `__builtin_frame_address` 等价的功能，而该函数对于定位当前栈帧至关重要。我编写了一个名为 `frame_address` 的 C 函数，它返回 `__builtin_frame_address(1)`，并通过桥接头文件（bridging header）将这个函数暴露给 Swift。

利用这个函数，`callStackReturnAddresses` 的内部实现就非常简单了。我把 `frame_address` 的结果存到一个名为 `StackFrame` 的结构体中（它只不过是一些函数，包裹着一个 `uintptr_t`，该值存储了来自 `frame_address` 的结果）：

```swift
let frame = StackFrame(address: frame_address())
```

遍历栈就像解引用帧指针（frame pointer）一样简单（因为帧指针所存位置的值是前一帧的地址）：

```swift
let nextFrameAddress = UnsafeMutablePointer<UInt>(bitPattern: address)?.pointee
```

从每一帧获取返回地址同样容易，因为它就紧挨着存储在每帧的帧指针后面：

```swift
let returnAddress = UnsafeMutablePointer<UInt>(bitPattern: address)!.advanced(by: FP_LINK_OFFSET).pointee
```

所以我们只需在栈中反复执行这一操作，直到超出栈的边界。

在我试过的基本测试中，得到的 `callStackReturnAddresses` 函数速度大约是 `NSThread.callStackReturnAddresses` 的两倍（在我的 Mac 上，每个核心每秒约 200 万次调用，而 `Thread.callStackReturnAddresses` 约为每秒 100 万次）。即使在计算相当密集的路径上，这个速度也足以在 Debug 构建中收集大量数据。

## 用法

> 包含此代码的项目在 GitHub 上提供：[mattgallagher/CwlUtils](https://github.com/mattgallagher/CwlUtils)。

1. 在你项目目录的某个子目录中，运行 `git clone https://github.com/mattgallagher/CwlUtils.git`
2. 将 `CwlUtils.xcodeproj` 文件拖到 Xcode 中你自己的项目文件树中
3. 在文件树中点击你的项目以访问项目设置，然后点击你想要添加 CwlUtils 的目标（target）
4. 点击“Build Phases”标签页，在“Target Dependencies”下点击“+”，然后根据你的目标平台添加对应的 CwlUtils_OSX 或 CwlUtils_iOS target
5. 仍在“Build Phases”下，如果你还没有一个“Destination”为“Frameworks”的“Copy Files”构建阶段，请添加一个。在这个构建阶段中，添加 `CwlUtils.framework`。注意：列表中会出现**两个**同名 framework（一个是 OS X，另一个是 iOS）。`CwlUtils.framework` 会出现在对应的 CwlUtils OS X 或 iOS 测试 target 上方。

关于步骤 (1) 的说明：不要求必须把检出放在你的项目目录内部，但如果你在共享位置检出代码，然后在多个父项目中同时打开，Xcode 会报错——通常在每个项目内部单独创建一个副本会更容易。

### 打包说明

这篇文章以及我接下来要写的几篇代码文章，都将成为单个 framework——CwlUtils——的一部分。坦率地说，我对这种单体式 framework 的组织方式并不满意。理想情况下，我希望产出的许多代码是相互独立、隔离的类，并按需由依赖管理器拉取到一起。然而，目前 Swift 生态中已有的第三方依赖管理方案在此场景下工作得不够优雅（不完全是它们的错，因为静态链接和透明的 Xcode 集成本身就不可行）。

等到官方 Swift Package Manager 作为 Xcode 的一部分正式发布时，我一定会重新审视这个问题，但就目前而言，一个无依赖的单体式 framework 就是现状。如果你只对我写的某小段代码感兴趣，你需要自行把它提取出来。

## 结论

我谈论了为进行中的任务记录堆栈跟踪以辅助调试的简便性和好处。在异步调用或其他复杂控制流之后，如果没有这些信息，追查结果为何不正确可能完全是不切实际的，所以这是一项值得铭记的好技巧。
