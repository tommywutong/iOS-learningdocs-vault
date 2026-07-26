---
title: 用 Swift Actor 保护可变状态
session_id: 10133
collection: wwdc2021
year: 2021
duration: '28:32'
topics: [Swift]
group: C · 并发、锁与线程
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10133/'
content_hash: 'sha256:da8fee6e818ba4c9'
translated: true
---

# 用 Swift Actor 保护可变状态

<sub>WWDC2021 · 28:32 · Swift</sub>

当两个不同的线程并发访问同一个可变状态时，就会发生数据争用。构造出数据争用轻而易举，但它出了名地……

> [!note] 归档理由
> actor 隔离与可重入，理解锁的替代方案

## 相关资源

- [SE-0316：全局 Actor](https://github.com/apple/swift-evolution/blob/main/proposals/0316-global-actors.md)
- [SE-0313：对 Actor 隔离更精细的控制](https://github.com/apple/swift-evolution/blob/main/proposals/0313-actor-isolation-control.md)
- [SE-0306：Actor](https://github.com/apple/swift-evolution/blob/main/proposals/0306-actors.md)
- [SE-0302：Sendable 与 @Sendable 闭包](https://github.com/apple/swift-evolution/blob/main/proposals/0302-concurrent-value-and-concurrent-closures.md)
- [The Swift Programming Language：并发](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10133/5/C303A256-7F2C-401E-9986-E877F8C7525E/downloads/wwdc2021-10133_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10133/5/C303A256-7F2C-401E-9986-E877F8C7525E/downloads/wwdc2021-10133_sd.mp4?dl=1)
- [使用 Swift 并发消除数据争用](https://developer.apple.com/videos/play/wwdc2022/110351)
- [认识 Swift 中的分布式 Actor](https://developer.apple.com/videos/play/wwdc2022/110356)
- [使用 Xcode 进行服务器端开发](https://developer.apple.com/videos/play/wwdc2022/110360)
- [可视化并优化 Swift 并发](https://developer.apple.com/videos/play/wwdc2022/110350)
- [探索 SwiftUI 中的并发](https://developer.apple.com/videos/play/wwdc2021/10019)
- [探索 Swift 中的结构化并发](https://developer.apple.com/videos/play/wwdc2021/10134)
- [认识 Swift 中的 async/await](https://developer.apple.com/videos/play/wwdc2021/10132)
- [Swift 并发：幕后揭秘](https://developer.apple.com/videos/play/wwdc2021/10254)
- [Swift 并发：更新一个示例 App](https://developer.apple.com/videos/play/wwdc2021/10194)
- [AppKit 的新变化](https://developer.apple.com/videos/play/wwdc2021/10054)
- [Swift 的新变化](https://developer.apple.com/videos/play/wwdc2021/10192)
- [数据争用让并发变难](https://developer.apple.com/videos/play/wwdc2021/10133/?time=42)
- [值语义有助于消除数据争用](https://developer.apple.com/videos/play/wwdc2021/10133/?time=140)
- [有时共享可变状态是必需的](https://developer.apple.com/videos/play/wwdc2021/10133/?time=179)
- [Actor 隔离能防止未同步的访问](https://developer.apple.com/videos/play/wwdc2021/10133/?time=323)
- [在 Actor 内部的同步交互](https://developer.apple.com/videos/play/wwdc2021/10133/?time=471)
- [在 await 之后检查你的假设：那只伤心的猫](https://developer.apple.com/videos/play/wwdc2021/10133/?time=542)
- [在 await 之后检查你的假设：一种解决办法](https://developer.apple.com/videos/play/wwdc2021/10133/?time=710)
- [在 await 之后检查你的假设：一种更好的解决办法](https://developer.apple.com/videos/play/wwdc2021/10133/?time=719)
- [协议一致性：静态声明位于 Actor 之外](https://developer.apple.com/videos/play/wwdc2021/10133/?time=810)
- [协议一致性：非隔离（non-isolated）的声明位于 Actor 之外](https://developer.apple.com/videos/play/wwdc2021/10133/?time=855)
- [闭包可以被隔离到 Actor 上](https://developer.apple.com/videos/play/wwdc2021/10133/?time=932)
- [在分离任务（detached task）中执行的闭包不会被隔离到 Actor 上](https://developer.apple.com/videos/play/wwdc2021/10133/?time=989)
- [把数据传入、传出 Actor：结构体](https://developer.apple.com/videos/play/wwdc2021/10133/?time=1035)
- [把数据传入、传出 Actor：类](https://developer.apple.com/videos/play/wwdc2021/10133/?time=1059)
- [通过添加一致性来检查 Sendable](https://developer.apple.com/videos/play/wwdc2021/10133/?time=1208)
- [通过添加条件一致性来传播 Sendable](https://developer.apple.com/videos/play/wwdc2021/10133/?time=1243)
- [与主线程交互：使用 DispatchQueue](https://developer.apple.com/videos/play/wwdc2021/10133/?time=1459)
- [与主线程交互：主要 Actor](https://developer.apple.com/videos/play/wwdc2021/10133/?time=1501)
- [主要 Actor 类型](https://developer.apple.com/videos/play/wwdc2021/10133/?time=1581)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ 低音音乐响起 ♪ ♪ Dario Rexin：大家好，我是 Dario Rexin，Apple Swift 团队的工程师。

今天，我和同事 Doug 将聊聊 Swift 中的 actor，以及它们是如何被用来在并发 Swift 应用中保护可变状态的。

编写并发程序中一个根本性的难题，就是避免数据争用。

当两个不同的线程并发访问同一份数据，且至少有一个访问是写操作时，就会发生数据争用。

数据争用构造起来非常容易，但出了名地难以调试。

这里有一个简单的计数器类，只有一个操作：递增计数器并返回它的新值。

假设我们从两个并发任务中尝试递增它。

这是个糟糕的主意。

根据执行的时序，我们可能得到 1 然后 2，或者 2 然后 1——这是预期之中的，两种情况下计数器都会处于一致的状态。

但因为我们引入了数据争用，如果两个任务都读到了 0 并写入了 1，我们也可能得到 1 和 1；如果两个 return 语句都发生在两次递增操作完成之后，我们甚至可能得到 2 和 2。

数据争用出了名地难以避免和调试：它们需要非局部的推理，因为引发争用的数据访问可能分散在程序的不同部分；而且它们是不确定的，因为操作系统的调度器每次运行你的程序时，都可能以不同的方式交错执行这些并发任务。

数据争用是由共享可变状态引起的：如果你的数据不会变化，或者它没有在多个并发任务间共享，那你就不可能在它上面发生数据争用。

避免数据争用的一种方式，是使用值语义来消除共享可变状态。

对于一个值类型的变量，所有的修改都是局部的。而且，值语义类型的 "let" 属性是真正不可变的，所以从不同的并发任务里访问它们是安全的。

Swift 从诞生之初就一直在推崇值语义，因为它让我们更容易推理程序的行为，而这些同样的特性，也让它们在并发程序里用起来是安全的。

在这个例子里，我们创建了一个包含一些值的数组，接着把这个数组赋值给第二个变量，然后往每一份数组的副本里各自追加一个不同的值。当我们最后打印两个数组时，会看到两份副本都包含数组初始化时的那些值，但每个追加的值只出现在我们追加到的那一份副本里。

Swift 标准库里大多数类型都具有值语义，包括像字典这样的集合类型，或者像这个例子里的数组。

既然我们已经确认了值语义能解决所有的数据争用问题，那我们就把计数器改成一个值类型，把它变成一个 struct 吧。我们还得把 increment 函数标记为 mutating，这样它才能修改 value 这个属性。

这时候，如果我们试图修改这个计数器，就会得到一个编译错误，因为这个计数器是个 let，这会阻止我们修改它。

现在，把计数器变量从 let 改成 var 让它可变，看起来非常诱人。但那样的话，我们又会陷入竞态条件，因为这个计数器会被两个并发任务同时引用。

幸好，编译器帮我们兜住了，不允许我们编译这段不安全的代码。我们可以改成把计数器赋值给每个并发任务内部的一个局部可变变量。

这时再运行我们的例子，两个并发任务打印出来的结果就总是 1。但即便我们的代码现在没有数据争用了，它的行为也已经不是我们想要的了。

这恰好说明，确实有些场景是需要共享可变状态的。

当并发程序里存在共享可变状态时，我们就需要某种同步手段，来确保对共享可变状态的并发使用不会引发数据争用。有一系列同步的基本手段，从原子操作、锁这类底层工具，到串行 dispatch queue 这样的高层构造。这些基本手段各有各的优势，但它们都有同一个致命弱点：每一次都需要小心翼翼地用得恰到好处，否则我们就会得到一个数据争用。

这正是 actor 登场的地方。Actor 是一种针对共享可变状态的同步机制。一个 actor 有它自己的状态，而这份状态与程序的其余部分是隔离的：访问这份状态的唯一方式，就是通过这个 actor；而且每当你通过这个 actor 访问时，actor 的同步机制都会确保没有其他代码在并发地访问这个 actor 的状态。

这给了我们和手动使用锁或串行 dispatch queue 时同样的互斥属性，但对于 actor 来说，这是 Swift 提供的一项基本保证：你不可能忘记去做同步，因为一旦你尝试绕过它，Swift 就会产生一个编译错误。

Actor 是 Swift 里一种新的类型。它们提供了 Swift 里所有具名类型都具备的能力：可以有属性、方法、初始化方法、下标等等；可以遵循协议，也可以通过 extension 来扩展。和类一样，它们是引用类型——因为 actor 存在的目的就是表达共享可变状态。

事实上，actor 类型最主要的区分特征，就是它们会把自己的实例数据与程序的其余部分隔离开来，并确保对这份数据的访问是同步的。它所有的特殊行为都源于这两个核心理念。

在这里，我们把计数器定义成了一个 actor 类型：我们仍然有 value 这个实例属性来保存计数器的值，还有 increment 方法来递增这个值并返回新值。不同之处在于，这个 actor 会确保 value 不会被并发访问。在这个例子里，这意味着 increment 方法一旦被调用，就会运行到完成，中途不会有任何其他代码在这个 actor 上执行。这个保证消除了在 actor 状态上发生数据争用的可能性。

我们再来看一下之前的数据争用的例子。我们同样有两个并发任务尝试递增同一个计数器。Actor 内部的同步机制确保了一次 increment 调用会运行到完成，另一次才能开始。所以我们可能得到 1 和 2，或者 2 和 1，因为两者都是合法的并发执行结果，但我们不可能两次得到同样的计数，也不会跳过任何值，因为 actor 内部的同步已经消除了在 actor 状态上发生数据争用的可能性。

我们来想想，当两个并发任务同时试图递增计数器时，实际上会发生什么：一个会先到，另一个则必须耐心等待轮到自己。但我们怎么才能确保第二个任务能耐心地在这个 actor 上等到它的轮次呢？Swift 有一套机制来做到这一点。

每当你从外部与一个 actor 交互时，你都是异步地这么做的。如果这个 actor 正忙，你的代码就会挂起，这样你所运行的那个 CPU 就可以去做别的有用的工作。当这个 actor 再次空闲下来时，它会唤醒你的代码——恢复执行——这样这次调用就可以在这个 actor 上运行了。这个例子里的 await 关键字表示，对这个 actor 的这次异步调用可能涉及这样的一次挂起。

我们再进一步扩展一下这个计数器的例子，加上一个不必要的、很慢的重置操作：这个操作把 value 设回 0，然后调用适当次数的 increment，把计数器恢复到新的值。这个 resetSlowly 方法定义在这个计数器 actor 类型的一个 extension 里，所以它是在这个 actor 内部的——这意味着它可以直接访问这个 actor 的状态，它也确实这么做了，把计数器的值重置为 0。它还可以同步地调用这个 actor 上的其他方法，比如这里对 increment 的调用——这里不需要 await，因为我们已经知道自己是在这个 actor 上运行的。

这是 actor 一个很重要的特性：actor 上的同步代码总是会运行到完成，不会被打断。所以我们可以按顺序推理同步代码，而不需要考虑并发对我们这个 actor 状态造成的影响。

我们已经强调了同步代码会不受打断地运行下去，但 actor 常常会与其他 actor 或系统里的其他异步代码交互。我们花几分钟聊聊异步代码和 actor。不过首先，我们需要一个更好的例子。

这里我们在构建一个图片下载 actor，它负责从另一个服务下载一张图片，同时也会把下载好的图片存进一个缓存，以避免重复下载同一张图片。它的逻辑流程很直白：检查缓存、下载图片，然后在返回之前把图片记录进缓存。因为我们身处一个 actor 里，这段代码不会有底层的数据争用；任意数量的图片都可以被并发下载。这个 actor 的同步机制保证了在任意时刻，只有一个任务能执行访问 cache 这个实例属性的代码，所以缓存不可能被搞乱。

话虽如此，这里的 await 关键字正在传达一个非常重要的信息：每当出现一次 await，就意味着函数可能在这个点上被挂起。它交出自己的 CPU，让程序里的其他代码得以执行，而这会影响整体的程序状态。当你的函数恢复执行时，整体的程序状态可能已经发生了变化。重要的是，要确保你没有对 await 之前的状态做出某种假设，而这个假设在 await 之后可能已经不再成立。

想象一下，我们有两个不同的并发任务，同时尝试获取同一张图片。第一个任务发现缓存里没有条目，于是开始从服务器下载这张图片，然后因为下载需要一段时间而被挂起。在第一个任务下载图片期间，服务器上同一个 URL 下可能被部署了一张新图片。这时，第二个并发任务也试图获取那个 URL 下的图片：它同样发现没有缓存条目（因为第一次下载还没完成），于是发起了第二次下载，随后也因为等待下载完成而被挂起。

过了一会儿，其中一个下载——假设是第一个——会先完成，它所在的任务会在这个 actor 上恢复执行：它把结果填进缓存，并返回这只猫的图片。这时第二个任务的下载也完成了，于是它也醒了过来：它用自己拿到的那张伤心猫咪的图片，覆盖了缓存里的同一个条目。所以，尽管缓存里此前已经填入了一张图片，我们现在却为同一个 URL 得到了一张不同的图片。

这有点出乎意料。我们本来期望，一旦缓存了某张图片，同一个 URL 就应该总是取回同样那张图片，好让我们的用户界面保持一致——至少在我们手动清空缓存之前应该如此。但在这里，缓存中的图片却在意料之外发生了变化。

我们并没有出现底层的数据争用，但因为我们在一次 await 前后携带了对状态的假设，最终还是造成了一个潜在的 bug。

这里的修复办法，是在 await 之后重新检查我们的假设：如果我们恢复执行时缓存里已经有了一个条目，就保留那个原始版本，把新的那个扔掉。更好的解决方案，是彻底避免这种重复下载——我们已经把这个方案放进了这个视频配套的代码里。

Actor 的可重入性可以防止死锁、保证程序能持续向前推进，但它要求你在每一次 await 前后都重新检查自己的假设。为了更好地为可重入性做设计，应该在同步代码里对 actor 状态进行修改，理想情况下，最好放在一个同步函数里，这样所有的状态变化都能被很好地封装起来。状态变化的过程中，可能会让 actor 暂时处于一种不一致的状态，一定要确保在遇到 await 之前恢复一致性，并且记住，await 是一个潜在的挂起点：如果你的代码被挂起了，在你的代码恢复执行之前，整个程序、整个世界都会继续往前走。任何你对全局状态、时钟、定时器，或者对自己这个 actor 做出的假设，都需要在 await 之后重新检查。

接下来我的同事 Doug 会给大家介绍更多关于 actor 隔离的内容。Doug？Doug Gregor：谢谢，Dario。

Actor 隔离是 actor 类型行为的基础。Dario 刚才讲了 Swift 的语言模型是如何通过"从 actor 外部进行异步交互"这一方式来保证 actor 隔离的。在这一部分，我们会聊聊 actor 隔离是怎么和其他语言特性交互的，包括协议一致性、闭包和类。

和其他类型一样，只要能满足协议的要求，actor 也可以遵循协议。举例来说，我们让这个 LibraryAccount actor 遵循 Equatable 协议。这个静态的相等性方法根据两个 library account 的 ID 号来比较它们。因为这个方法是静态的，不存在 self 实例，所以它没有被隔离到这个 actor 上。相反，我们有两个 actor 类型的参数，而这个静态方法在这两者之外——这是可以的，因为它的实现只访问了这个 actor 上的不可变状态。

我们再进一步扩展这个例子，让 library account 遵循 Hashable 协议。要做到这一点，需要实现 hash(into) 操作，我们可以这样写。然而，Swift 编译器会报错，说这个一致性是不被允许的。这是怎么回事？其实，用这种方式遵循 Hashable，意味着这个函数可能从 actor 外部被调用，但 hash(into) 不是 async 的，所以没有办法维持 actor 隔离。

要解决这个问题，我们可以把这个方法标记为 nonisolated。Nonisolated 意味着这个方法会被当作处于这个 actor 之外——尽管从语法上看，它是写在这个 actor 上的。这意味着它可以满足 Hashable 协议里那个同步的要求。因为 nonisolated 的方法被当作处于 actor 之外，它们不能引用 actor 上的可变状态。这个方法没问题，因为它引用的是不可变的 ID 号；如果我们试图基于别的东西（比如借出的书籍数组）来做哈希，就会出错，因为从外部访问可变状态会带来数据争用的风险。

协议一致性就聊到这里，我们来说说闭包。闭包是定义在一个函数里、随后可以被传给另一个函数、在稍后某个时刻被调用的小函数。和函数一样，一个闭包可能是 actor 隔离的，也可能不是。

在这个例子里，我们要从借出的每本书里读一些内容，然后返回我们已读的总页数。这次对 reduce 的调用涉及一个执行读取操作的闭包，注意，这次对 readSome 的调用里没有 await——那是因为这个闭包是在这个 actor 隔离的函数 "read" 里创建的，所以它本身也是 actor 隔离的。我们知道这是安全的，因为 reduce 操作会同步执行，它没法把这个闭包逃逸到别的、可能引发并发访问的线程上去。

现在，我们来做一些不太一样的事：我现在没时间读书，那就晚点再读吧。这里我们创建了一个 detached task。一个 detached task 会和这个 actor 正在做的其他工作并发地执行这个闭包，所以这个闭包不能位于这个 actor 上，否则我们就会引入数据争用。所以这个闭包没有被隔离到这个 actor 上。当它想调用 read 方法时，必须像 await 所标示的那样，异步地这么做。

我们已经聊了一些关于代码的 actor 隔离——也就是这段代码是在 actor 内部运行还是在外部运行。现在，我们来聊聊数据的 actor 隔离。

在我们这个 library account 的例子里，我们一直刻意回避了 book 到底是什么类型这个问题。我一直假设它是一个值类型，比如一个 struct——这是个不错的选择，因为这意味着 library account actor 的每个实例，其全部状态都是自包含的。如果我们去调用这个方法来选一本随机的书来读，我们会得到这本书的一份副本，我们可以拿它去读。我们对这份副本所做的修改，不会影响到这个 actor，反过来也一样。

不过，如果把 book 改成一个类，情况就有点不一样了。我们的 library account actor 现在引用的是 book 这个类的实例，这本身不是问题；但当我们调用那个选取随机书籍的方法时会发生什么呢？现在我们拿到了一个指向这个 actor 可变状态的引用，而这个引用已经被共享到了 actor 之外——我们由此制造出了发生数据争用的可能性。这时，如果我们去更新书名，这次修改发生在 actor 内部可访问的状态上；而因为 visit 这个方法不在这个 actor 上，这次修改就有可能变成一次数据争用。

值类型和 actor 在并发场景下都可以安全使用，但类仍然可能带来问题。我们给"可以安全并发使用的类型"起了个名字：Sendable。一个 Sendable 类型，指的是它的值可以在不同的 actor 之间安全共享的类型。如果你把一个值从一处拷贝到另一处，而这两处都可以安全地修改各自的那份拷贝而互不干扰，那么这个类型就可以是 Sendable 的。值类型是 Sendable 的，因为正如 Dario 之前提到的，每一份拷贝都是独立的；actor 类型是 Sendable 的，因为它们会对自己的可变状态同步访问。类也可以是 Sendable 的，但只有在被精心实现的前提下：比如，如果一个类和它所有的子类都只持有不可变数据，那它就可以被称为 Sendable；或者如果这个类内部执行了同步（比如用一把锁）来确保并发访问的安全，它也可以是 Sendable 的。但大多数类都不属于这两种情况，因此不能是 Sendable 的。

函数未必是 Sendable 的，所以有了一种新的函数类型，专门用于那些可以安全地跨 actor 传递的函数——我们很快会回来讲这个。

你的 actor——事实上，你所有的并发代码——都应该主要以 Sendable 类型来通信。Sendable 类型能保护代码免受数据争用的影响，这是一个 Swift 最终会开始做静态检查的属性；到那时，跨越 actor 边界传递一个非 Sendable 的类型将会成为一个错误。

我们怎么知道一个类型是 Sendable 的呢？其实 Sendable 是一个协议，你像声明遵循其他协议一样，声明你的类型遵循 Sendable，Swift 随后就会检查，确保你的类型作为一个 Sendable 类型是说得通的。

如果一个 Book 结构体的所有存储属性都是 Sendable 类型的，那这个 Book 就可以是 Sendable 的。假设 Author 其实是一个类，那就意味着它——以及由此构成的 authors 数组——都不是 Sendable 的，Swift 就会产生一个编译错误，提示 Book 不能是 Sendable 的。

对于泛型类型来说，它们是否是 Sendable 的，可能取决于它们的泛型参数。我们可以用条件一致性，在合适的时候传播 Sendable：比如，一个 pair 类型，只有当它的两个泛型参数都是 Sendable 的时候，它才是 Sendable 的。同样的方式也被用来推断出：一个由 Sendable 类型组成的数组，本身也是 Sendable 的。

我们鼓励你为那些其值可以安全并发共享的类型引入 Sendable 一致性，并在你的 actor 内部使用这些类型。这样，等 Swift 开始在跨 actor 场景强制执行 Sendable 检查时，你的代码就已经准备好了。

函数本身也可以是 Sendable 的，意味着把这个函数值跨 actor 传递是安全的。这对闭包来说尤其重要，因为它限制了闭包能做的事情，从而有助于防止数据争用。举个例子，一个 Sendable 闭包不能捕获一个可变的局部变量，因为那样会在这个局部变量上引发数据争用；闭包所捕获的任何东西都需要是 Sendable 的，以确保这个闭包不会被用来把非 Sendable 的类型跨 actor 边界移动。最后，一个同步的 Sendable 闭包不能是 actor 隔离的，因为那样会让代码从外部在这个 actor 上运行。

其实在这场演讲里，我们一直依赖着 Sendable 闭包这个概念：创建 detached task 的那个操作，接受的就是一个 Sendable 函数——在这里写作函数类型里的 @Sendable。

还记得我们在演讲开头的那个反例吗？我们试图构建一个值类型的计数器，然后试图从两个不同的闭包同时去修改它——这会在这个可变的局部变量上引发数据争用。然而，因为 detached task 的闭包是 Sendable 的，Swift 会在这里产生一个错误。Sendable 函数类型被用来指出并发执行可能发生的地方，从而防止数据争用。

这是我们之前看到过的另一个例子：因为 detached task 的这个闭包是 Sendable 的，我们就知道它不应该被隔离到这个 actor 上，所以和它的交互都必须是异步的。

Sendable 类型和闭包，通过检查可变状态是否跨 actor 共享、是否可能被并发修改，帮助维持 actor 隔离。

我们主要一直在讲 actor 类型，以及它们是怎么和协议、闭包、Sendable 类型交互的。还有一个 actor 值得一提——一个特殊的 actor，我们称之为主要 Actor（main actor）。

当你在构建一个 App 时，你需要考虑主线程：它是核心用户界面渲染发生的地方，也是用户交互事件被处理的地方。和 UI 打交道的操作通常需要在主线程上执行。然而，你不会希望把所有的工作都放在主线程上做——如果你在主线程上做了太多工作，比如因为有某个缓慢的 I/O 操作，或者与服务器的阻塞式交互，你的 UI 就会卡死。所以，你需要小心：在涉及 UI 交互的时候在主线程上工作，但对于计算开销大或需要长时间等待的操作，要尽快离开主线程。所以，我们会在可能的时候把工作放到主线程之外去做，然后每当有某个特定的操作必须在主线程上执行时，就在代码里调用 DispatchQueue.main.async。

跳出这个机制的细节来看，这段代码的结构看起来有点眼熟：其实，与主线程交互和与一个 actor 交互，非常相似。如果你知道自己已经在主线程上运行了，你就可以安全地访问和更新你的 UI 状态；如果你不在主线程上，你就需要异步地与它交互——这正是 actor 的工作方式。

有一个专门用来描述主线程的特殊 actor，我们称之为主要 Actor：主要 Actor 是代表主线程的一个 actor。它在两个重要方面不同于普通的 actor：第一，主要 Actor 是通过主 dispatch queue 来完成它所有的同步的，这意味着，从运行时的角度来看，主要 Actor 和使用 DispatchQueue.main 是可以互换的；第二，需要放在主线程上的代码和数据，散落在各个地方——它存在于 SwiftUI、AppKit、UIKit 以及其他系统框架里，也散布在你自己的 view、view controller，以及数据模型里面向 UI 的那些部分。

有了 Swift 并发，你可以用主要 Actor 属性来标记一个声明，表示它必须在主要 Actor 上执行。我们在这里的这个 checked-out 操作上就这么做了，所以它总是在主要 Actor 上运行。如果你从主要 Actor 之外调用它，你就需要 await，这样这次调用才会在主线程上异步执行。通过把必须运行在主线程上的代码标记为在主要 Actor 上，关于什么时候该用 DispatchQueue.main，就再也不用去猜了——Swift 会确保这段代码总是在主线程上执行。

类型本身也可以被放到主要 Actor 上，这会让它的所有成员和子类都处于主要 Actor 上。对于你代码库里那些必须与 UI 交互、绝大部分内容都需要在主线程上运行的部分，这非常有用。单个方法可以通过 nonisolated 关键字选择退出，规则和你从普通 actor 那里熟悉的一样。

通过把面向 UI 的类型和操作放到主要 Actor 上，同时为管理其他程序状态引入你自己的 actor，你就可以为你的 App 架构出一种安全、正确使用并发的方式。

在这场演讲里，我们讲了 actor 是如何通过 actor 隔离、以及要求从 actor 外部进行异步访问来串行化执行，从而保护自己的可变状态不被并发访问的。请用 actor 在你的 Swift 代码里构建安全的并发抽象。

在实现你自己的 actor，以及编写任何异步代码时，请始终为可重入性而设计：你代码里的一次 await，就意味着整个世界可能已经往前走了，让你的假设失效。值类型和 actor 协同工作，共同消除数据争用。要留意那些没有自己处理同步的类，以及其他会重新引入共享可变状态的非 Sendable 类型。最后，在你与 UI 交互的代码上使用主要 Actor，以确保那些必须在主线程上运行的代码始终运行在主线程上。

想了解更多关于如何在你自己的应用里使用 actor，请看我们那场关于把一个 App 更新为使用 Swift 并发的演讲；想了解更多关于 Swift 并发模型（包括 actor）的实现细节，请看我们的 "幕后揭秘" 演讲。

Actor 是 Swift 并发模型的核心组成部分，它们与 async/await 和结构化并发协同工作，让构建正确、高效的并发程序变得更容易。我们迫不及待想看看你会用它们构建出什么。

♪
