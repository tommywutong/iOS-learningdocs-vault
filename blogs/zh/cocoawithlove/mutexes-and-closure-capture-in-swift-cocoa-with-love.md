---
title: 'Swift 中的互斥锁与闭包捕获 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/06/02/threads-and-mutexes.html'
original_language: en
published: 2016-06-02
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:f20f5d69a21de364'
translated: true
---

> 原文：[Mutexes and closure capture in Swift | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/06/02/threads-and-mutexes.html)　·　Cocoa with Love (Matt Gallagher)

我想简要谈谈 Swift 中缺少线程和线程同步语言特性这一问题。我将讨论 Swift 未来的“并发”提案，以及在此特性出现之前，Swift 的线程处理将如何涉及传统的互斥锁和共享可变状态。

在 Swift 中使用互斥锁并不特别困难，但我打算借这个话题来强调 Swift 中一个微妙的性能困扰：闭包捕获期间的动态堆分配。我们希望互斥锁运行得快，但由于内存分配开销，向互斥锁内部传递闭包执行可能会使性能降低一个数量级。我将探讨几种不同的方法来解决这个问题。

## Swift 中线程特性的缺失

当 Swift 在 2014 年 6 月首次发布时，我认为这门语言明显缺少了两样东西：

- 错误处理
- 线程与线程同步

错误处理在 Swift 2 中得到了解决，并且是该版本的关键特性之一。

截至 Swift 4，线程仍基本被 Swift 忽略。Swift 没有提供语言级别的线程特性，而是在所有平台上包含了 `Dispatch` 模块（libdispatch，即 Grand Central Dispatch），并隐晦地建议：使用 `Dispatch` 而不是指望语言来帮忙。

与 Go 和 Rust 等将线程原语和严格的线程安全性（分别）作为其语言核心特性的现代语言相比，将责任委托给一个捆绑的库显得尤为奇怪。即便是 Objective-C 的 `@synchronized` 和 `atomic` 属性，与 Swift 的_一无所有_相比，似乎也显得慷慨大方。

Swift 明显缺少这些特性的背后原因是什么？

## Swift 未来的“并发”

[Swift 仓库中的“并发”提案](https://github.com/apple/swift/blob/c760f6dfbf0179e9aff90f7bf7375f3af5331318/docs/proposals/Concurrency.rst)简要地讨论了一种可能的未来。

> 我提到这个提案是为了强调 Swift 开发者希望在未来就并发做点_事_，但请记住 [Swift 开发者 Joe Groff 指出的](https://twitter.com/jckarter/status/739109723408994304)：“该文档只是一个提案，而非官方方向声明。”

这个提案似乎描述了一种情况，就像在 [Cyclone](http://homes.cs.washington.edu/~djg/papers/cycthreads.pdf) 或 [Rust](http://blog.rust-lang.org/2015/04/10/Fearless-Concurrency.html) 中那样，引用不能在线程之间共享。在那种可能的情景下，计划让 Swift 消除线程之间的共享内存，除非是实现了 `Copyable` 并通过严格管理的通道（提案中称为 `Stream`）传递的类型。此外，还将有一种形式的协程（提案中称为 `Task`），其行为类似于可暂停/可恢复的异步调度 block。

然后，该提案声称，大多数常见的线程_语言_特性（类似 Go 的 `chan`nel、类似 .NET 的 `async`/`await`、Erlang 风格的 `actor`）都可以基于 `Stream`/`Task`/`Copyable` 这些原语在_库_中实现。

这一切听起来很棒，但 Swift 的并发特性预计何时到来？Swift 5.1？不太可能。Swift 6？也许吧。别抱太大希望。

## 尝试寻找一个快速、通用的互斥锁

短期内，如果我们想要多线程行为，就需要使用现有的线程和互斥锁特性自行构建。

[Swift 中关于互斥锁的常见建议](http://stackoverflow.com/questions/24045895/what-is-the-swift-equivalent-to-objective-cs-synchronized)通常是：使用 `DispatchQueue` 并对其调用 `sync`。

我很喜欢 libdispatch，但在大多数情况下，将 `DispatchQueue.sync` 用作互斥锁是解决方案中最慢的一档——比其他选项慢_超过一个数量级_，这是因为传递给 `sync` 函数的闭包存在不可避免的闭包捕获开销。这并非因为 libdispatch 本身是一个慢的库，而是由于其 API 与 Swift 之间存在一个不可避免的复杂问题：闭包捕获。具体来说，我们传递给 `DispatchQueue.sync` 的任何闭包都需要捕获你在其内部使用的受保护资源的引用，而这种捕获涉及堆分配，由于函数的内容位于另一个库中，因此无法被优化掉。

> 我将讨论互斥锁之间相对的速度。如果你对原始数据感兴趣，本文末尾的表格中有它们。

在 Swift 中，大多数闭包不会产生堆分配，因为 Swift 可以内联它们，完全消除闭包。这就是为什么完全在你自己的项目中使用的闭包运行得很快。由于 Swift 总是内联标准库，传递给它的闭包也很快。但对于 `DispatchQueue.sync` 来说，内联是不可能的，因为函数的内容存在于一个单独的模块（用 C 编写）中，因此 Swift 无法优化掉闭包捕获，这使得 `DispatchQueue.sync` 在 Swift 中成为一个不必要地慢的选择。

下一个我最常看到的建议是 `objc_sync_enter`/`objc_sync_exit`。虽然这里的机制很慢，但我们可以直接在我们的代码周围进行调用，这意味我们可以避免使用闭包及其相关的捕获，使其速度比 `DispatchQueue.sync` 快大约 8 倍。它比理想情况稍慢（因为它是一个_可重入_互斥锁，实际上只是在另一层中包装了底层的 `pthread_mutex_t` 机制），但也不算太差。然而，它仅限于 Apple 平台，因此无法支持 Linux。

过去最快的互斥锁选项是 `OSSpinLock`——比 `dispatch_sync` 快 20 倍以上——但此函数现已已废弃，你不应再使用它。除了自旋锁的标准限制（如果多个线程实际尝试同时进入，CPU 使用率会很高）之外，还存在一些[严重的调度问题，使得该互斥锁在 macOS 上存在问题，在 iOS 上完全无法使用](https://lists.swift.org/pipermail/swift-dev/Week-of-Mon-20151214/000372.html)。

现实的选项中，最快的是 `os_unfair_lock`，它比 `objc_sync_enter`/`objc_sync_exit` 快 3 倍，仅比 `OSSpinLock` 慢 30%。然而，这个锁不是先入先出（FIFO）的。相反，互斥锁会被交给一个随机的等待者（因此称为“unfair”）。你需要判断这对你的程序是否构成问题，但一般来说，这意味着它不应是你的通用互斥锁的首选。它也仅限于 Apple 平台。

最后的选择是 C 语言的老朋友：`pthread_mutex_lock`/`pthread_mutex_unlock`。这个互斥锁性能合理（仅比 `os_unfair_lock` 慢 40%），可移植，并且是公平的——因此你不会遇到等待者饥饿的问题。或者至少它过去是公平的——显然在 macOS 10.14 和 iOS 12 及更高版本中，默认情况下它使用了一种更接近“unfair”的等待策略。为什么？大概是为了避免意外的优先级反转。不公平性有多大影响？尚不清楚——默认的 `PTHREAD_MUTEX_POLICY_FIRSTFIT_NP` 策略涉及的具体调度逻辑尚不明确。

## 互斥锁与闭包捕获陷阱

我将继续讨论 `pthred_mutex_t`——尽管大部分经验同样适用于任何独立的 `lock`/`unlock` 互斥锁（包括 `objc_sync_enter`、`os_unfair_lock`）。

让我们在一个库模块中使用 `pthread_mutex_lock`/`pthread_mutex_unlock` 实现我们自己的 `sync` 函数。我会忽略初始化，因为我想要关注的是在互斥锁内部执行代码。标准方法是实现一个 `sync` 函数。看起来像这样：

```swift
public class PThreadMutex {
   var mutex: pthread_mutex_t
   
   public init() { /* ... */ }
   
   public func sync<R>(execute: () throws -> R) rethrows -> R {
      pthread_mutex_lock(&mutex)
      defer { pthread_mutex_unlock(&mutex) }
      return try execute()
   }
}
```

这个函数本应是高性能的，但并不是。

如果我将这个函数放在另一个模块中，同样的性能问题依然存在：Swift 无法进行跨模块内联，因此闭包不能被内联，闭包捕获会导致一个数量级的减速。

## 避免捕获

我们需要避免闭包捕获及其相关的堆分配。我们可以通过将相关参数传递给闭包，而不是捕获它，来避免这种情况。如果我们的闭包不_捕获_，那么它就应该不需要分配空间。

```swift
public extension PThreadMutex {
   func sync_generic_param<T, R>(_ p: inout T, execute: (inout T) -> R) -> R {
      pthread_mutex_lock(&mutex)
      defer { pthread_mutex_unlock(&mutex) }
      return execute(&p)
   }
}
```

这样好多了……如果我以一个 `Int` 作为参数，`Double` 作为返回类型来调用这个函数，它几乎可以全速运行（比内联的 pthread 调用慢约 10%）。

## 启用内联

我们仍然比理想情况慢 10%，但通过一个泛型参数传递只是略显笨拙。闭包的优点在于其使用起来非常自然。

让我们看看能否让闭包方法全速运行。要做到这一点，我们需要让编译器能够内联闭包，并通过将代码复制到使用它的文件中来消除捕获的需要。

为此，我们可以在 `PThreadMutex` 的调用处所在的同一文件中添加以下扩展：

```swift
private extension PThreadMutex {
   func sync_same_file<R>(execute: () throws -> R) rethrows -> R {
      pthread_mutex_lock(&m)
      defer { pthread_mutex_unlock(&m) }
      return try execute()
   }
}
```

这让 Swift 能够内联整个函数，消除了 retain/release 开销，我们终于达到了 100% 的性能基准。

是的，我确实建议你通过复制粘贴代码来避免闭包捕获。如果你使用了全模块优化（自 Swift 3 以来发布版本的默认设置），你不必将其粘贴到同一文件中；你可以粘贴到模块内的任何位置。

但是，如果你需要在特定函数上获得最大性能，那么在 Swift 中，需要在每个模块中复制你的代码（直到未来某个编译器版本中实现跨模块内联）。

## 使用信号量，而不是互斥锁？

在我最初撰写这篇文章后，有几个人问……为什么不使用 `dispatch_semaphore_t` 呢？`dispatch_semaphore_wait` 和 `dispatch_semaphore_signal` 的优点是无需闭包——它们是独立的、无作用域的调用，就像 `pthread_mutex_lock`/`pthread_mutex_unlock` 一样。

你可以使用 `dispatch_semaphore_t` 来创建类似互斥锁的结构，如下所示：

```swift
public struct DispatchSemaphoreWrapper {
   let s = DispatchSemaphore(value: 1)
   init() {}
   func sync<R>(execute: () -> Void)  {
      _ = s.wait(timeout: DispatchTime.distantFuture)
      defer { s.signal() }
      execute()
   }
}
```

在同一个模块中，它的速度大约与 `os_unfair_lock` 相当。但是，如果你将其放在一个单独的模块中，对于 `execute` 闭包，你仍然会遇到所有先前独立模块实现所面临的闭包捕获问题。

而且，以这种方式滥用信号量存在更严重的风险。

信号量是工作线程和监听线程之间传达完成通知的好方法（这是互斥锁不容易做到的，因为互斥锁必须在获取它的同一线程上释放）。但是，当信号量被用作互斥锁时，它与线程无关这一事实会导致许多[优先级反转](https://en.wikipedia.org/wiki/Priority_inversion)问题。系统无法将线程优先级逻辑应用于信号量，低优先级线程可能会使高优先级线程饥饿，并且不同优先级的等待线程组之间可能发生死锁。优先级反转是与使 `OSSpinLock` 在 iOS 上无法使用的相同类型的问题，虽然信号量的问题更复杂一些，但当涉及多个不同优先级的线程时，它仍可能导致你的 App 死锁。

所有这些可能看起来有点深奥——因为你可能不会在自己的程序中故意创建不同优先级的线程。然而，Cocoa 框架在这里加入了一个你需要考虑的变化：Cocoa 框架普遍使用 dispatch queues，并且每个 dispatch queue 都有一个“QoS class”，这可能导致队列以不同的线程优先级运行。除非你知道程序中每个任务是如何排队的（包括由 Cocoa 框架排队的用户界面和其他任务），否则你可能会发现自己陷入了一个未曾预料到的多线程优先级场景。

最好避免这种风险——至少在一般情况下这样做。

## 使用

> 一个包含 `PThreadMutex` 和 `UnfairLock` 实现封装的项目可在 github 上获取：[mattgallagher/CwlUtils](https://github.com/mattgallagher/CwlUtils)。

[CwlMutex.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlMutex.swift?ts=3) 文件是完全独立的，因此如果你只需要它，可以直接复制该文件。为了性能，我建议你在使用这些 `sync` 函数的编译单元（取决于全模块优化的模块或文件）中制作这些函数的 `internal` 或 `private` 副本，或者使用 `unbalancedLock` 和 `unbalancedUnlock` 函数来避免闭包捕获。

[该项目的 ReadMe.md 文件](https://github.com/mattgallagher/CwlUtils/blob/master/README.md)包含克隆整个仓库并将它生成的框架添加到你自己项目的详细信息。

## 结论

最简单的互斥锁选项可能仍然是 `DispatchQueue.sync`。它有一个 Swift 包装器，并在标准库中得到广泛支持。

如果你需要显著级别的性能，那么 `os_unfair_lock` 或 `pthread_mutex_t` 是唯一真正的选择。还有其他选项，但它们存在一些复杂问题，妨碍在一般情况下的使用。这两者都不是严格“公平”的。你可以将 `pthread_mutex_t` 配置为公平的，但默认情况下它（至少部分）不公平——这可能是件好事，因为它避免了意外的优先级死锁。

但无论你选择哪种互斥锁 API，要在 Swift 中实现最大性能都需要避免堆分配，而堆分配是影响典型接受闭包的 `sync` 函数的常见问题。闭包捕获上下文的堆分配会使典型的互斥锁 `sync` 函数慢一个数量级（即大约慢十倍）。

为了避免典型 `sync` 函数的闭包捕获，需要将整个函数从任何库模块复制到使用它的编译模块中，或者重新定义带有内置参数的闭包函数以避免需要随闭包一起捕获。此时，在模块之间复制粘贴通常是实现内联的最佳解决方案（栈分配闭包终于将在 Swift 5 或不久后到来）。

线程、异步、并发和内联都是我希望在 Swift 5 之后会发生巨大变化的话题，但现在屏息以待还为时过早。

## 附录：性能数据

我运行了一个简单的循环，一千万次，进入互斥锁，递增一个计数器，然后离开互斥锁。“慢”版本的 `DispatchSemaphore` 和 `PThreadMutex` 是作为动态框架的一部分编译的，与测试代码分离。

以下是计时结果：

| 互斥锁变体 | 秒 (Swift 3.0, MacPro 4,1) | 秒 (Swift 4.2, MacBookPro 15,1) | 秒 (Swift 5.0 master 2019-01-19, MacBookPro 15,1) |
|---|---|---|---|
| `DispatchQueue.sync` | 3.530 | 3.687 | 3.484 |
| `PThreadMutex.sync` (捕获闭包) | 3.124 | 2.015 | 0.384 (禁用独占访问时 0.212) |
| `objc_sync_enter`/`objc_sync_exit` | 0.833 | 0.446 | 0.422 |
| `PThreadMutex.sync_generic_param` (非捕获) | 0.284 | 0.184 | 0.284 (禁用独占访问时 0.182) |
| `PThreadMutex.sync_same_file` (内联) | 0.265 | 0.175 | 0.171 |
| `pthread_mutex_lock`/`pthread_mutex_unlock` | 0.263 | 0.175 | 0.172 |
| `os_unfair_lock_lock`/`os_unfair_lock_unlock` | 0.187 | 0.130 | 0.12 |
| `OSSpinLockLock`/`OSSpinLockUnlock` | 0.108 | 0.075 | 0.069 |

使用的测试代码是链接的 [CwlUtils](https://github.com/mattgallagher/CwlUtils) 项目的一部分，但包含这些性能测试的测试文件（CwlMutexPerformanceTests.swift）默认情况下未链接到测试模块中，需要手动启用。
