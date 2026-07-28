---
title: Swift 并发不等待任何人
source: Saagar Jha
source_key: saagarjha
source_url: 'https://saagarjha.com/blog/2023/12/22/swift-concurrency-waits-for-no-one/'
original_language: en
published: 2023-12-22
status: active
license: CC BY-SA 4.0 → 可再分发，但译文必须同样 BY-SA 并署名
archived_at: 2026-07-27
content_hash: 'sha256:98995bcde406b92b'
translated: true
---

> 原文：[Swift Concurrency Waits for No One](https://saagarjha.com/blog/2023/12/22/swift-concurrency-waits-for-no-one/)　·　Saagar Jha

# Swift 并发不等待任何人

2023 年 12 月 22 日，星期五

> 曾有一位大师级工程师，她独自隐居在一个神秘而遥远的地方。那里养分充沛，脚下的泥土比黄金还要珍贵。那个地方连步行都无法到达，只有极少数人能踏上旅途，寻求她的智慧。有一天，一位热情但还很稚嫩的新手程序员前来拜访。
>
> “我读过你的代码，”他开口道，“我只能说它至高无上。可是，我学到了很多关于 Swift 并发的内容，却发现你并没有一直使用它。这是为什么？”
>
> 大师级工程师立刻用一个问题回应：“告诉我，异步程序该如何调用同步代码？”
>
> “这很简单，”他回答，“直接调用就行了。”
>
> “那如果要从同步的上下文调用异步代码，该怎么做呢？”
>
> “那自然是生成一个 `Task` 了！”新手工程师答道，很高兴自己的学习派上了用场。
>
> 大师级工程师微微一笑。“很好。可现在，想象一下你要等那项工作完成才能继续。那该怎么办？这个 API 是系统提供的，无法重新设计。”
>
> 这难住了新手。他紧锁眉头，思索了好一阵子。最后，一个半遗忘的记忆浮现出来：“`DispatchSemaphore`！可以用信号量来等待异步工作完成！”
>
> “Swift 并发要求任务必须向前推进（make forward progress）”，大师级工程师回答道。然后她沉默不语。过了一会儿，新手顿悟了。

## 背景

[Swift 并发](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)承诺让我们能够编写出正确、高性能的代码，以适应当今异步事件无处不在、硬件高度并行的世界。确实，只要使用得当，它就能做到这一点。然而，就像冰山一样，它所暴露的简单 API 之下隐藏着令人惊叹的复杂内容。不幸的是，与线性的同步代码相比，并发是一个难以理解的话题，任何编程模型都很难完全掩盖其所有微妙之处。

当然，对于大多数 Swift 开发者来说，并发并不是什么新鲜事。那些为 Apple 平台编程的人几乎肯定知道 [Grand Central Dispatch](https://developer.apple.com/documentation/dispatch)，甚至还有 [POSIX 线程](https://en.wikipedia.org/wiki/Pthreads)等其他 API。许多应用程序甚至会同时使用好几种！然而，新颖之处在于，Swift 并发是一种完全不同的并发编程范式，由一套全新的规则所支配。违反这些条件的后果，有时与之前的技术一样严重——无意中的重入（reentrancy）、死锁，甚至数据损坏。值得庆幸的是，Swift 并发的一个主要卖点是编译器会尝试替我们强制许多规则。违反指导方针的代码通常无法编译！其他规则虽然有详细文档并且易于遵循，即使编译器不进行检查也同样如此。某些不变性会在运行时（在实际可行时）无条件地进行验证，而其他一些则可以作为可选调试检查来启用。

尽管这些规则对于编写正确的程序至关重要，但它们有时却不够清晰（甚至根本未提及）。虽然运行时是开源的，但它不断演进，非专家很难理解。在某些极端情况下，可能完全无法用 Swift 并发编写某些代码，但构建出看似可行的东西却很容易——无论是因为 bug、运行时的实现细节，还是仅仅因为运气好。因此，一个成功的实践者需要扎实掌握如何推理他们代码的正确性。我们将通过解决一个长期以来对许多开发者来说都是难点的话题——Swift 并发的“向前推进”概念，来探索分析程序的一种方法。

## 并发与并行

如果你来自线程和队列的世界，Swift 并发在表面上看起来可能有些相似：你可以启动任务以异步方式运行，并等待它们完成，就像使用旧 API 一样。在许多情况下，将运行时视为拥有“无限线程”来运行我们调度的工作的模型，足以判断某些代码是否正确。显然，Swift 并发在底层管理着自己的协作线程池，所以我们实际上并不会创建无限多的线程，但在这些情况下，很容易认为运行时在“神奇地”为我们做正确的事情。

然而，有时协作线程池的特性就变得非常重要了。现在就是这样一个时刻。在讨论如何以及为何之前，我们需要先了解两个重要术语：**并发（concurrency）** 与 **并行（parallelism）**。如果你和我一样，你大概记得它们与同时管理多个任务有关，但仅此而已。毕竟，需要的时候你可以查阅它们的精确定义。不过，这里的区别很重要，所以你可以现在复习一下，或者忘了的时候再回来看：

- **并发（Concurrency）** 让你可以在任意时刻有多个任务“正在进行中”（即：尚未完成）。
- **并行（Parallelism）** 让你能够同时运行多个正在积极执行的任务。

不那么抽象地说，当你停止编码，开始回复老板在 Slack 上的消息时，你就在进行**并发**。同样地，当你坐在无聊的会议中刷 Hacker News 时，你就是在展示你的**并行**技巧。在计算机中，这通常是这样运作的：任务的并发调度涉及将任务切分并交错执行各部分，而并行调度则需要多个“内核”。请注意，没有并行也可以有并发：单核机器无法并行执行任何工作，但它通常会在多个任务之间进行上下文切换。

Swift 并发（正如其名称所示）是一个用于**并发**调度任务的系统。其实现的一个核心特性是，它可以透明地扩展以利用系统上的所有并行能力，但恰恰就是这个细节：一个**实现**细节。一个编写正确的程序，在大多数情况下，是无法区分只有一个线程还是有一百个线程的。

## 向前推进（Forward Progress）

粗略地说，**向前推进（forward progress）** 意味着某个任务必须能够持续进行工作。一个正在向前推进的程序可以“等待”（例如通过获取锁、休眠或执行 I/O），但必须始终有一种方式能使其从等待中出来。一个不向前推进程序的简单例子就是陷入无限循环的程序，因为无论你做什么尝试或等待多久，它都无法再做任何其他事情。

在 Swift 并发中，一个核心规则是 **[协作线程池上的所有任务都必须向前推进](https://developer.apple.com/videos/play/wwdc2021/10254/?time=1450)**。违反此规则将导致死锁。考虑到这一点，我们能否对以下代码说些什么？

```
let semaphore = DispatchSemaphore(value: 0)

func wait() async {
	semaphore.wait()
}

func signal() async {
	semaphore.signal()
}
```

你可能听说过，`DispatchSemaphore` 在 Swift 并发中使用是不安全的。当你构建这段代码时，警告也指向了这一点。但为什么呢？它有什么问题？

首先，我们知道 `wait()` 和 `signal()` 都是 `async` 函数，这意味着它们将在协作线程池上被调用。我们也知道这里的所有任务都需要向前推进。我们可以立即发现潜在的问题：`wait()` 调用了 `DispatchSemaphore.wait()`，它阻塞了当前线程，而没有像 `await` 那样通知运行时。当这种情况发生时，在该线程上，直到阻塞返回之前，没有其他任务可以运行，这意味着它可以无限地阻塞该任务的向前推进。

“但是，等等！”，你说。“谁说会无限地阻塞向前推进？我当然计划在未来的某个时刻调用 `signal()`，_那_ 将解除对 `wait()` 调用的阻塞。看吧，我可以确保向前推进！”然而，即使你平衡了所有对 `wait()` 和 `signal()` 的调用，这段代码仍然可能死锁。怎么会呢？答案需要我们回到关于并行的讨论中。

Swift 的协作线程池大小可以是任意值。这意味着它可以只有一个线程。在这种情况下，当你调用 `wait()` 时会发生什么？它阻塞了这唯一的线程，这意味着未来对 `signal()` 的任何调用将永远得不到调度的机会。它无法被调度：它_必须_在协作线程池上运行，但已经没有可用的线程了。因此，死锁。

“等等！”，你再次抗议。“这也太蠢了。我们为什么要在乎只有一个线程的协作线程池？我知道这在_理论上_是错的，但在实践中这永远不会出问题，因为总是有更多的线程。”好吧，但你仍然会看到死锁。为什么？因为我知道你不会像我示例那样写代码。相反，你很可能会这样写：

```
actor Lock {
	let semaphore = DispatchSemaphore(value: 0)

	func lock() {
		semaphore.wait()
	}

	func unlock() {
		semaphore.signal()
	}
}
```

谁会用一个信号量来写 App 呢？而且如果你要有一堆信号量，你顺便给它们起个名字也无妨。名字显然不重要；重要的是当你的 App 中的所有线程碰巧同时调用 `lock()` 时会发生什么。这种情况很少发生，但一旦发生，协作线程池上就无法再进行任何工作，你就又死锁了。`Lock` 本身没有什么特别之处：它只是一个代表，代表了在多个线程上同时阻塞，从而耗尽协作线程池直到它无法再处理新工作这个更普遍的问题。

## 等待 `async` 工作

让我们来看一个更复杂的例子。假设我们有一个借书的 API。它早于 Swift 并发，并使用委托（delegate）接口：

```
protocol LibraryDelegate {
	func shouldLend(_ book: Book) -> Bool
}
```

当用户去借书时，框架允许委托拒绝（也许他们有未付的罚款？）。一个简化后的实现可能看起来像这样：

```
class CheckoutMachine: LibraryDelegate {
	func shouldLend(_ book: Book) -> Bool {
		let account = library.lookupAccount(forCardNumber: cardNumber)
		return !account.hasFines
	}
}
```

这是个不错的开始，但图书馆还想确保我们不会借出有人已经预约的书。预约者可能是另一位图书馆访客，也可能是当地一所与他们建立了目录共享合作关系的大学研究员。幸好我们也有这方面的代码。与大学系统交互可能会有点慢，但与之通信的实现则稍微现代一些：

```
class HoldManager {
	func holds(on book: Book) async -> [Account] {
		let libraryHolds = library.holds(on: book)
		// 这会联系大学系统，看看是否有人预约了这本书
		let universityHolds = await university.holds(on: book)
		return libraryHolds + universityHolds
	}
}
```

现在我们只需更新 `shouldLend(_:)` 来使用它……等等。这是一个 `async` 函数，这意味着我们需要 `await` 它的结果。但 `shouldLend(_:)` 是同步的！我们如何让它工作呢？

显然，我们需要以某种方式等待任务完成。这个问题——让异步工作变成同步——在与那些设计之初并未考虑 Swift 并发的旧代码交互时非常常见。桥接同步和异步代码从来都不容易，但在过去，对于这种情况我们可能会使用信号量。这种方法有其自身的问题，但通常它不会阻塞向前推进。

Swift 并发的 `Task` 初始化器是一个同步函数，它接受一个 `async` 闭包，这至少符合我们正在寻找的模式。如果我们眯着眼看这个构造，它有点像我们过去用来等待回调的方式：

```
func shouldLend(_ book: Book) -> Bool {
	class Unreserved: @unchecked Sendable { var value: Bool! }
	let Unreserved = Unreserved()

	let semaphore = DispatchSemaphore(value: 0)
	Task {
		let holds = await holdManager.holds(on: book)
		unreserved.value = holds.isEmpty
		semaphore.signal()
	}
	semaphore.wait()

	let account = library.lookupAccount(forCardNumber: cardNumber)
	return !account.hasFines && unreserved.value
}
```

因为我们所做的有些不同寻常，我们需要一些仪式来将结果从 `Task` 中提取出来。尽管其外观不雅，`@unchecked Sendable` 和隐式解包可选值（implicitly unwrapped optional）都没问题，因为我们的控制流保证了初始化和独占访问。然而，这段代码正确吗？

乍一看，似乎可能没问题：尽管我们使用了 `DispatchSemaphore`，但这次我们只在异步上下文中 _signal_（发信号）。阻塞的等待发生在一条完全“不知道”Swift 并发的代码路径上。然而，这仍然可能死锁！

### 分析

其中的原因并不明显，尽管可以很简单地描述：这段代码死锁的原因是 `shouldLend(_:)` 最终可能在协作线程池上被调用，即使它是一个同步的、早于 Swift 并发的回调。以下是 `shouldLend(_:)` 调用实际的回溯：

```
* thread #2, queue = 'com.apple.root.default-qos.cooperative'
  * frame #0: App`CheckoutMachine.shouldLend(_: Book)
    frame #1: LibraryCore`Library.checkLendability(of: Book)
    frame #2: LibraryCore`Library.reallyDoCheckout(of: Book, from: Catalog)
    frame #3: LibraryCore`Library.checkoutCommonImpl(book: Book)
    frame #4: LibraryCore`Library.checkout(_: Book)
    frame #5: App`CheckoutMachine.checkoutBooks() async throws
```

它在协作线程池上！这是因为在我们 App 的另一部分，我们从 `async` 上下文中使用了 `Library.checkout(_:)`，而 LibraryCore 最终调用了我们的委托方法。这是个坏消息，因为在我们的实现中，信号量阻塞了这个线程。如果我们把并行度降低到一，我们启动的 `Task` 就无法获得执行机会，而由于我们依赖它的工作来发出我们正在等待的信号量，这就又造成了一个死锁。

这个分析可能感觉有点不公平，因为我并没有告诉你关于 `CheckoutMachine` 或 LibraryCore 其余部分的任何信息。但这就是重点：我们以一种出人意料且非局部的方式打破了向前推进的保证。即使你掌握了你自己 App 中的所有代码（对于任何复杂项目来说这都是一个很高的要求！），向前推进的保证也依赖于你调用栈中_每一个函数_的调度决策，其中的许多函数你可能并不拥有甚至没有源代码。毋庸置疑，某个函数决定以同步方式、在内部队列上运行其代码，还是使用 Swift 并发本身，都是你无法依赖的实现细节。

## 遗留代码中的向前推进

在这一点上，阻塞并发执行的代码会导致死锁，这一点可能已经很明显了。不过，我们分析的第二部分，集中在如果你阅读了上面的回顾可能会问自己的一个问题：如果我们不允许阻塞协作线程池，我们如何安全地调用任意代码？毕竟，我们使用的某个库可能在内部使用了信号量。这对我们来说是个问题吗？

根据实验，答案是“不是的”：行为良好的 Swift 并发代码似乎不会死锁，无论它所依赖的库如何选择进行自身同步。不知怎的，_我们_不允许阻塞或等待，但我们同步调用的代码_却可以_。`DispatchSemaphore` 不可能聪明到能区分其中的区别……它真的能吗？它能在我们不守规矩时用挂起（hang）来惩罚我们吗？

不用说，情况并非如此，但真正的原因很微妙。我们知道早于 Swift 并发的代码最终可能在协作线程池上运行，但它_自己_不会选择这样做。像这样的库代码非常普遍：

```
func foo() {
	let semaphore = DispatchSemaphore(value: 0)
	doSomeAsynchronousWork(completion: {
		semaphore.signal()
	})
	semaphore.wait()
}
```

尽管这看起来很像我们上面的例子，但我们通常可以安全地调用它，即使在 `async` 上下文中也一样。因为这段代码早于 Swift 并发，它不会像我们之前的例子那样启动一个 `Task` 来执行异步工作。它可能会执行 `dispatch_async`、XPC 调用或网络调用，但这些都不会在协作线程池上调度。这允许了向前推进，因为其他工作将独立启动并完成，从而在未来的某个时刻解除对等待线程的阻塞。

## 经验教训

向前推进是一个难以掌握的概念。虽然在推理任何并发设计时都很重要，但在像 Swift 并发这样的协作式系统中，死锁的后果要普遍得多、纠缠得多，并且通常更难调试。一些原语，特别是那些不使用 `await` 进行同步等待的技术，几乎不可能在 Swift 并发中安全使用。不幸的是，尝试构建一个自制的但存在细微错误的版本，远比分析它为什么崩溃要容易。这一点，加上随机性的故障，意味着世界上有大量代码面临着未来挂起的风险。（例如，本文中的例子来自我在 GitHub 上进行的搜索。）

一个不受欢迎的事实是，有些代码就是无法与 Swift 并发桥接。在其他情况下，编写此类代码并验证其正确性的工作量极高，以至于继续使用这项技术得不偿失。如果是在选择了使用 Swift 并发很长一段时间之后才发现这一点，这可能会尤为痛苦，而这里唯一的解决方案（尽管可能令人沮丧）就是回头去使用其他 API 重写程序。

尽管存在这些限制，Swift 并发对于许多希望管理异步工作的项目来说仍然是一个不错的选择；重要的是要理解哪些项目适合。检查向前推进是我们做出此类决策的一种方法。这种分析可能很复杂，但这里给出的例子应该为思考你自己的异步代码的正确性提供一个起点。
