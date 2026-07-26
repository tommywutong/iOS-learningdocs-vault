---
title: 'Swift 中的 ARC：基础与进阶'
session_id: 10216
collection: wwdc2021
year: 2021
duration: '20:42'
topics: [Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10216/'
content_hash: 'sha256:34930f3f5251d0ae'
translated: true
---

# Swift 中的 ARC：基础与进阶

<sub>WWDC2021 · 20:42 · Swift</sub>

了解 Swift 中对象生命周期与 ARC 的基础知识。深入探讨哪些语言特性会让对象生命周期变得可观察……

> [!note] 归档理由
> ARC 的插入规则、生命周期与 withExtendedLifetime，内存管理核心

## 相关资源

- [ARC - The Swift Programming Language](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10216/4/884C234F-2424-47DF-A4CF-A9010D869C66/downloads/wwdc2021-10216_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10216/4/884C234F-2424-47DF-A4CF-A9010D869C66/downloads/wwdc2021-10216_sd.mp4?dl=1)
- [ARC Example](https://developer.apple.com/videos/play/wwdc2021/10216/?time=109)
- [Reference Cycle Example](https://developer.apple.com/videos/play/wwdc2021/10216/?time=397)
- [Weak Reference Example](https://developer.apple.com/videos/play/wwdc2021/10216/?time=545)
- [Accessing an object via weak reference](https://developer.apple.com/videos/play/wwdc2021/10216/?time=605)
- [通过 weak 引用的可选绑定访问对象](https://developer.apple.com/videos/play/wwdc2021/10216/?time=674)
- [Safe techniques for handling weak references - withExtendedLifetime()](https://developer.apple.com/videos/play/wwdc2021/10216/?time=705)
- [安全处理 weak 引用的技巧 - 重新设计为通过强引用访问](https://developer.apple.com/videos/play/wwdc2021/10216/?time=775)
- [安全处理 weak 引用的技巧 - 重新设计以避免 weak/unowned 引用](https://developer.apple.com/videos/play/wwdc2021/10216/?time=860)
- [Deinitializer Example](https://developer.apple.com/videos/play/wwdc2021/10216/?time=923)
- [Sequencing deinitializer side-effects with external program effects](https://developer.apple.com/videos/play/wwdc2021/10216/?time=970)
- [安全处理反初始化方法副作用的技巧 - withExtendedLifetime()](https://developer.apple.com/videos/play/wwdc2021/10216/?time=1076)
- [安全处理反初始化方法副作用的技巧 - 重新设计以限制类内部细节的可见性](https://developer.apple.com/videos/play/wwdc2021/10216/?time=1111)
- [安全处理反初始化方法副作用的技巧 - 重新设计以避免反初始化方法副作用](https://developer.apple.com/videos/play/wwdc2021/10216/?time=1148)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ 低音音乐播放中 ♪ ♪ Meghana Gupta：大家好，我是 Meghana。

今天我要跟大家讲讲 Swift 中的 ARC。

Swift 提供了强大的值类型，比如结构体和枚举。

应该尽可能优先使用值类型，以避免引用类型带来的意外共享风险。

在 Swift 中，类是引用类型。如果你决定使用类，Swift 会通过自动引用计数（Automatic Reference Counting，ARC）来管理它的内存。

要写出高效的 Swift 代码，理解 ARC 的工作原理非常重要。

这场演讲我们就来做这件事。

我会先回顾一下 Swift 中的对象生命周期和 ARC。

然后，我会说明什么是可观察的对象生命周期。

我会详细解释哪些语言特性会让对象生命周期变得可观察、依赖被观察到的对象生命周期会带来什么后果，以及一些用来修正这类问题的安全技巧。

我们开始吧。

在 Swift 中，一个对象的生命周期始于初始化，终于最后一次使用。

ARC 会在一个对象的生命周期结束后将其释放，从而自动管理内存。

它通过追踪对象的引用计数来判断对象的生命周期。

ARC 主要由 Swift 编译器驱动，编译器会插入 retain 和 release 操作。

在运行时，retain 会让引用计数加一，release 会让引用计数减一。

当引用计数降为零时，对象就会被释放。

我们通过一个例子来看看它是怎么工作的。

假设我们想构建一个旅行 App。

为了表示一位旅行者，我们写一个带有 name 和一个可选 destination 属性的类。

在 test() 函数里，首先创建一个 Traveler 对象，然后复制它的引用，最后更新它的 destination。

为了自动管理 Traveler 对象的内存，Swift 编译器会在一个引用开始时插入一次 retain 操作，并在这个引用最后一次使用之后插入一次 release 操作。

traveler1 是对 Traveler 对象的第一个引用，它最后一次被使用是在那次复制中。

这里，Swift 编译器会在 traveler1 引用最后一次使用之后立即插入一次 release 操作。

它不会在这个引用开始时插入 retain 操作，因为初始化本身就已经把引用计数设为了一。

traveler2 是对 Traveler 对象的另一个引用，它最后一次被使用是在那次 destination 更新中。

这里，Swift 编译器会在这个引用开始时插入一次 retain 操作，并在这个引用最后一次使用之后立即插入一次 release 操作。

我们一步步过一遍代码，看看运行时会发生什么。

首先，Traveler 对象在堆上被创建，初始化时引用计数为一。

然后，为准备新的引用，retain 操作执行，把引用计数增加到二。

现在 traveler2 也成了 Traveler 对象的一个引用。

在 traveler1 引用最后一次使用之后，release 操作执行，把引用计数减少到一。

接着，Traveler 对象的 destination 被更新为 Big Sur。

由于这是 traveler2 引用最后一次被使用，release 操作执行，把引用计数减少到零。

一旦引用计数降为零，这个对象就可以被释放了。

Swift 中的对象生命周期是基于使用情况的。

一个对象「保证的最短生命周期」始于初始化，终于最后一次使用。

这和 C++ 这类语言不同——在 C++ 中，对象的生命周期保证会在闭合花括号处结束。

在这个例子里，我们看到对象在最后一次使用之后立即被释放了。

但在实践中，对象的生命周期是由 Swift 编译器插入的 retain 和 release 操作决定的。

而根据触发的 ARC 优化的不同，被观察到的对象生命周期可能会和它们「保证的最短生命周期」不同，会延续到超出对象最后一次使用的位置。

在这种情况下，对象会在超出其最后一次使用的某个程序位置被释放。

在大多数情况下，一个对象的确切生命周期到底是什么，其实并不重要。

但是，借助像 weak 和 unowned 引用、以及反初始化方法（deinitializer）副作用这样的语言特性，是有可能观察到对象生命周期的。

而如果你的程序依赖的是「被观察到的对象生命周期」，而不是「保证的对象生命周期」，将来就可能出问题。

因为依赖被观察到的对象生命周期，今天可能凑巧能用，但那只是巧合。

被观察到的对象生命周期是 Swift 编译器的一种涌现属性，会随着实现细节的变化而变化。

这类 bug 可能在开发阶段不会被发现，会隐藏很长一段时间，直到某次带来了改进版 ARC 优化的编译器更新，或者某个看似无关的源码改动激活了此前受限的某项 ARC 优化，才会被揭露出来。

我会逐一讲解哪些语言特性会让对象生命周期变得可观察，走一遍如果我们只依赖被观察到的对象生命周期可能会发生什么，以及一些用来修正它们的安全技巧。

和默认的强引用不同，weak 和 unowned 引用不参与引用计数，正因如此，它们常被用来打破引用循环。

在深入讲它们的细节之前，我们先来看看什么是引用循环。

这是我们旅行 App 例子的一个扩展。

现在我们想引入一个可选的积分系统。

一位旅行者可以拥有一个账户，并在其中累积积分。

为了表示这一点，我们新建一个带 points 属性的 Account 类。

Account 类引用 Traveler 类，而 Traveler 类又反过来引用 Account 类。

在 test() 函数里，我们创建 Traveler 和 Account 对象，然后通过 traveler 引用调用 printSummary() 函数。

我们一步步过一遍代码，看看 ARC 会发生什么。

首先，Traveler 对象在堆上被创建，引用计数为一。

然后，Account 对象在堆上被创建，引用计数为一。

由于 Account 对象引用了 Traveler 对象，Traveler 对象的引用计数被增加到二。

现在 Traveler 对象开始引用 Account 对象，所以 Account 对象的引用计数也被增加到二。

这是 account 这个引用最后一次被使用。

在这之后，account 这个引用消失，Account 对象的引用计数被减少到一。

然后，调用 printSummary() 函数，打印 name 和 points。

这是 Traveler 这个引用最后一次被使用。

在这之后，Traveler 这个引用消失，Traveler 对象的引用计数被减少到一。

即使所有让这些对象可达的引用都消失了，这些对象的引用计数依然是一。

这是因为存在引用循环。

结果就是，这些对象永远不会被释放，从而造成内存泄漏。

你可以用 weak 或 unowned 引用来打破这个引用循环。

因为它们不参与引用计数，所以在一个 weak 或 unowned 引用仍在使用的同时，它所指向的对象可能已经被释放了。

发生这种情况时，Swift 运行时会安全地把对 weak 引用的访问变成 nil，把对 unowned 引用的访问变成陷阱（trap）。

任何参与引用循环的引用都可以被标记为 weak 或 unowned 来打破这个循环，具体标记哪一个取决于应用场景。

在我们的例子里，我们把 Account 类里的 traveler 引用标记为 weak。

因为 weak 引用不参与引用计数，所以在 Traveler 对象最后一次被使用之后，它的引用计数会降到零。

一旦 Traveler 对象的引用计数为零，它就可以被释放。

当 Traveler 对象消失时，它对 Account 对象的引用也随之消失，使得 Account 对象的引用计数变为零。

现在 Account 对象也可以被释放了。

在这个例子里，我们用 weak 引用只是为了打破引用循环。

如果一个 weak 引用是在其对象「保证的生命周期」已经结束之后，还被用来访问这个对象，而你依赖的是「被观察到的对象生命周期」来保证对象仍然可用，那么将来当被观察到的对象生命周期因为一些无关的原因发生变化时，你就可能遇到 bug。

我们来看一个例子。

这里，printSummary() 函数从 Traveler 类挪到了 Account 类里。

而 test() 函数现在通过 Account 引用来调用 printSummary() 函数。

调用 printSummary() 函数时到底会发生什么？今天它可能会打印出旅行者的姓名和积分，但这只是巧合。

这是因为 Traveler 对象最后一次被使用，是在调用 printSummary() 函数之前。

在这之后，如果编译器在最后一次使用之后立即插入了一次 release，Traveler 对象的引用计数就可能降为零。

如果引用计数已经降为零，那么通过这个 weak 引用访问 Traveler 对象得到的就会是 nil，而且 Traveler 对象可能已经被释放了。

所以当 printSummary() 函数被调用时，对这个 weak 的 Traveler 引用做强制解包就会触发陷阱，导致崩溃。

你可能会想，是不是因为用了强制解包才导致了这次崩溃，用可选绑定是不是就能避免它。

可选绑定实际上会让问题变得更糟。

它不会带来明显的崩溃，而是制造出一个静默的 bug——当被观察到的对象生命周期因为一些无关的原因发生变化时，这个 bug 可能悄无声息地就出现了，不被人注意到。

要安全地处理 weak 和 unowned 引用，有几种不同的技巧，每一种在「前期实现成本」和「持续维护成本」之间的权衡都不一样。

我们结合这个例子逐一来看。

Swift 提供了 withExtendedLifetime() 这个工具函数，可以显式地延长一个对象的生命周期。

使用 withExtendedLifetime()，就可以在调用 printSummary() 函数期间安全地延长 Traveler 对象的生命周期，从而防止潜在的 bug。

同样的效果，也可以通过在现有作用域末尾放一个空的 withExtendedLifetime() 调用来实现。

对于更复杂的情况，我们可以用 defer，让编译器把一个对象的生命周期延长到当前作用域结束。

withExtendedLifetime() 看起来可能像是绕开对象生命周期 bug 的一条捷径。

但这个技巧是脆弱的，它把「保证正确性」的责任转移给了你自己。

用这种方式的话，你需要确保每当一个 weak 引用有可能引发 bug 时，都用上 withExtendedLifetime()。

如果不加以控制，withExtendedLifetime() 就可能在整个代码库里到处蔓延，增加维护成本。

用更好的 API 重新设计类，是一种原则性强得多的做法。

如果能把对该对象的访问限制为只能通过强引用，就可以从根本上避免对象生命周期方面的意外。

这里，printSummary() 函数被挪回了 Traveler 类，而 Account 类里的那个 weak 引用被隐藏了起来。

现在测试代码只能通过强引用来调用 printSummary() 函数，从而消除了潜在的 bug。

weak 和 unowned 引用除了带来性能开销之外，如果在类设计上不够小心，还可能暴露出 bug。

这时候值得停下来想一想：为什么需要 weak 和 unowned 引用？它们是不是只是用来打破引用循环的？如果一开始就避免产生引用循环呢？通过重新思考算法、把有环的类关系转变为树状结构，往往就能避免引用循环。

在我们的例子里，Traveler 类需要引用 Account 类。

但 Account 类其实并不真的需要引用 Traveler 类。

Account 类只需要访问旅行者的个人信息。

我们可以把旅行者的个人信息挪到一个新的类里，叫 PersonalInfo。

Traveler 类和 Account 类都可以引用 PersonalInfo 类，从而避免了这个循环。

避免对 weak 和 unowned 引用的需求，可能会带来额外的实现成本，但这是彻底消除所有潜在对象生命周期 bug 的确定做法。

另一个会让对象生命周期变得可观察的语言特性，是反初始化方法（deinitializer）的副作用。

反初始化方法会在对象释放之前运行，它的副作用可以被外部程序效果观察到。

如果你写的代码把反初始化方法的副作用和外部程序效果按顺序串在了一起，那就可能引出隐藏的 bug——只有当被观察到的对象生命周期因为一些无关的原因发生变化时，这些 bug 才会被揭露出来。

在讲这类 bug 是怎么产生的之前，我们先来看看什么是反初始化方法。

这是第一个例子的重复版本，现在加上了一个反初始化方法。

这个反初始化方法有一个全局副作用：在控制台打印一条消息。

今天，这个反初始化方法可能会在打印出 "Done traveling" 之后才运行。

但由于 Traveler 对象最后一次被使用是在那次 destination 更新中，根据触发的 ARC 优化不同，这个反初始化方法完全可能在 "Done traveling" 被打印之前就运行。

在这个例子里，反初始化方法的副作用是可以被观察到的，但没有被依赖。

我们来看一个更复杂的例子，其中反初始化方法的副作用被外部程序效果所依赖。

现在我们给 Traveler 类引入旅行指标（travel metrics）。

每当 destination 被更新时，都会被记录到 TravelMetrics 类里。

最终，在反初始化 Traveler 对象时，这些指标会被发布到一个全局记录里。

发布的指标包括：旅行者的匿名 ID、查询过的目的地数量，以及一个计算得出的旅行兴趣类别。

在 test() 函数里，首先创建一个 Traveler 对象，然后从这个 Traveler 对象复制一份对 travelMetrics 的引用。

旅行者的 destination 被更新为 Big Sur，这会把 Big Sur 记录到 TravelMetrics 里。

旅行者的 destination 被更新为 Catalina，这会把 Catalina 记录到 TravelMetrics 里。

然后，通过查看已记录的目的地，计算出旅行兴趣类别。

今天，这个反初始化方法可能会在旅行兴趣计算完成之后才运行，把兴趣类别发布为 Nature。

但 Traveler 对象最后一次被使用，是在那次更新为 Catalina 的 destination 更新中，紧接着之后，这个反初始化方法就可能运行。

由于这个反初始化方法在旅行兴趣计算完成之前就运行了，发布出去的会是 nil，从而导致一个 bug。

和 weak、unowned 引用一样，安全处理反初始化方法副作用也有几种不同的技巧。

每一种在「前期实现成本」和「持续维护成本」之间的权衡也各不相同。

我们逐一来看。

可以用 withExtendedLifetime() 显式地把 Traveler 对象的生命周期延长到旅行兴趣类别计算完成为止，从而防止潜在的 bug。

正如之前讨论过的，这会把「保证正确性」的责任转移给你自己。

用这种方式的话，你需要确保每当反初始化方法的副作用和外部程序效果之间存在潜在的错误交互时，都用上 withExtendedLifetime()，这会增加维护成本。

如果反初始化方法的所有副作用都是局部的，那这些副作用就无法被观察到。

通过限制类内部细节的可见性来重新设计类的 API，可以防止对象生命周期方面的 bug。

这里，TravelMetrics 被标记为 private，从而对外部访问隐藏起来。

这个反初始化方法现在负责计算出最感兴趣的旅行类别，并发布这些指标。

这样是可行的，但更原则性的做法是彻底去掉反初始化方法的副作用。

这里，改用 defer 而不是反初始化方法来发布指标，反初始化方法则只负责做验证。

通过去掉反初始化方法的副作用，我们就可以消除所有潜在的对象生命周期 bug。

我们通过这个用于教学的旅行 App 例子，了解了 ARC、weak 和 unowned 引用，以及反初始化方法的副作用。

透彻理解哪些语言特性会让对象生命周期变得可观察，并消除对「被观察到的对象生命周期」的潜在错误依赖，这一点非常重要，这样我们才不会在意想不到的时刻发现 bug。

在 Xcode 13 中，Swift 编译器新增了一个实验性的构建设置，叫 "Optimize Object Lifetimes"。

它会启用强大的、能缩短生命周期的 ARC 优化。

打开这个构建设置后，你可能会更普遍地看到对象在最后一次使用之后立刻被释放，让被观察到的对象生命周期更接近它们「保证的最短生命周期」。

这可能会暴露出隐藏的对象生命周期 bug，就和我们讨论过的那些例子类似。

你可以用这场演讲里讨论过的这些安全技巧，来消除所有这类 bug。

希望你喜欢这场演讲。

感谢观看。

♪
