---
title: 使用 Swift 并发消除数据争用
session_id: 110351
collection: wwdc2022
year: 2022
duration: '28:54'
topics: [Essentials, Swift]
group: C · 并发、锁与线程
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2022/110351/'
content_hash: 'sha256:859dbe9857121db1'
translated: true
---

# 使用 Swift 并发消除数据争用

<sub>WWDC2022 · 28:54 · Essentials、Swift</sub>

加入我们，一同探索 Swift 并发的核心概念之一：任务与 Actor 的隔离。我们将为你介绍 Swift 的……

> [!note] 归档理由
> Sendable 与数据争用的静态消除模型

## 相关资源

- [并发](https://developer.apple.com/documentation/Swift/concurrency)
- [《Swift 编程语言》：并发](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/110351/3/2B82DC62-6057-4460-93F4-B99CF7073221/downloads/wwdc2022-110351_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/110351/3/2B82DC62-6057-4460-93F4-B99CF7073221/downloads/wwdc2022-110351_sd.mp4?dl=1)
- [认识 Swift 中的分布式 Actor](https://developer.apple.com/videos/play/wwdc2022/110356)
- [问答：Swift 并发](https://developer.apple.com/videos/play/wwdc2022/110480)
- [可视化并优化 Swift 并发](https://developer.apple.com/videos/play/wwdc2022/110350)
- [Swift 的新特性](https://developer.apple.com/videos/play/wwdc2022/110354)
- [UIKit 的新特性](https://developer.apple.com/videos/play/wwdc2022/10068)
- [探索 SwiftUI 中的并发](https://developer.apple.com/videos/play/wwdc2021/10019)
- [探索 Swift 中的结构化并发](https://developer.apple.com/videos/play/wwdc2021/10134)
- [认识 Swift 中的 async/await](https://developer.apple.com/videos/play/wwdc2021/10132)
- [使用 Swift Actor 保护可变状态](https://developer.apple.com/videos/play/wwdc2021/10133)
- [Swift 并发：幕后](https://developer.apple.com/videos/play/wwdc2021/10254)
- [Swift 并发：更新示例 App](https://developer.apple.com/videos/play/wwdc2021/10194)
- [将 async/await 与 URLSession 结合使用](https://developer.apple.com/videos/play/wwdc2021/10095)
- [任务](https://developer.apple.com/videos/play/wwdc2022/110351/?time=78)
- [什么是菠萝？](https://developer.apple.com/videos/play/wwdc2022/110351/?time=151)
- [加入小鸡](https://developer.apple.com/videos/play/wwdc2022/110351/?time=195)
- [Sendable 协议](https://developer.apple.com/videos/play/wwdc2022/110351/?time=275)
- [使用实现来指定哪些类型是 Sendable](https://developer.apple.com/videos/play/wwdc2022/110351/?time=284)
- [跨任务边界检查 Sendable](https://developer.apple.com/videos/play/wwdc2022/110351/?time=297)
- [Sendable 约束来自 Task 结构体](https://developer.apple.com/videos/play/wwdc2022/110351/?time=326)
- [枚举和结构体的 Sendable 检查](https://developer.apple.com/videos/play/wwdc2022/110351/?time=383)
- [集合相关的枚举和结构体的 Sendable 检查](https://developer.apple.com/videos/play/wwdc2022/110351/?time=412)
- [使用非 Sendable 集合的枚举和结构体的 Sendable 检查](https://developer.apple.com/videos/play/wwdc2022/110351/?time=437)
- [类中的 Sendable 检查](https://developer.apple.com/videos/play/wwdc2022/110351/?time=456)
- [自行进行内部同步的引用类型](https://developer.apple.com/videos/play/wwdc2022/110351/?time=478)
- [任务创建期间的 Sendable 检查](https://developer.apple.com/videos/play/wwdc2022/110351/?time=501)
- [Sendable 函数类型](https://developer.apple.com/videos/play/wwdc2022/110351/?time=548)
- [Actor](https://developer.apple.com/videos/play/wwdc2022/110351/?time=628)
- [一次只能有一艘船访问一个岛屿](https://developer.apple.com/videos/play/wwdc2022/110351/?time=663)
- [非 Sendable 数据不能在任务和 Actor 之间共享](https://developer.apple.com/videos/play/wwdc2022/110351/?time=694)
- [哪些代码是 Actor 隔离的？](https://developer.apple.com/videos/play/wwdc2022/110351/?time=763)
- [非隔离代码](https://developer.apple.com/videos/play/wwdc2022/110351/?time=843)
- [非隔离同步代码](https://developer.apple.com/videos/play/wwdc2022/110351/?time=888)
- [非隔离异步代码](https://developer.apple.com/videos/play/wwdc2022/110351/?time=915)
- [将函数隔离到主要 Actor](https://developer.apple.com/videos/play/wwdc2022/110351/?time=1021)
- [@MainActor 类型](https://developer.apple.com/videos/play/wwdc2022/110351/?time=1058)
- [非事务性代码](https://developer.apple.com/videos/play/wwdc2022/110351/?time=1198)
- [海盗！](https://developer.apple.com/videos/play/wwdc2022/110351/?time=1256)
- [将 `deposit` 函数改为同步](https://developer.apple.com/videos/play/wwdc2022/110351/?time=1317)
- [AsyncStream 按顺序交付元素](https://developer.apple.com/videos/play/wwdc2022/110351/?time=1436)
- [最小严格并发检查](https://developer.apple.com/videos/play/wwdc2022/110351/?time=1502)
- [目标严格并发检查](https://developer.apple.com/videos/play/wwdc2022/110351/?time=1521)
- [完整严格并发检查](https://developer.apple.com/videos/play/wwdc2022/110351/?time=1613)

## 逐字稿

> [!warning] 逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ Mellow instrumental hip-hop music ♪

♪

大家好。

我是 Swift 团队的 Doug，今天来介绍 Swift 并发如何消除数据争用。

我们引入了 Swift 并发，这是一组语言特性，让编写并发程序变得更简单。

关于这些语言特性各自的机制，请参阅涵盖各项特性的 2021 年 WWDC 讲座。

本次讲座从不同的、更整体的角度来审视 Swift 并发，把它看作一种组织程序的方式，让你在高效利用并发的同时不会引入数据争用。

但要这样做，我们需要一个很好的类比，因此我们邀请你和我们一起在并发的大海上航行。

并发之海不可预测，很多事情同时发生，但有你掌舵、有 Swift 帮你导航，就能创造出令人惊叹的结果。

让我们开始吧！我们首先谈谈隔离，这是 Swift 并发模型的关键思想之一，确保数据不会以可能引入数据争用的方式被共享。

先从任务隔离说起。

在并发之海上，任务由小船表示。

小船是我们的主力工作者——它们有自己要完成的任务，从头到尾按顺序执行。

它们是异步的，其工作可以在代码中有“await”操作的任何地方被挂起任意多次。

最后，它们是自包含的：每个任务都有自己的资源，因此它可以独立于海上所有其他小船独自运行。

如果我们的小船完全独立，我们就有了没有数据争用的并发，但如果没有任何交流方式，它就不太有用。

让我们加入一些交流！例如，一艘小船可能有一个菠萝，想和另一艘小船分享。

于是两艘船在公海相遇，我们把菠萝从一艘船转移到另一艘船。

现在，这个物理类比有点行不通了，因为这个菠萝不是一个从一艘船移动到另一艘船的物理物品。

它是数据，在 Swift 中我们有几种不同的方式来表示这些数据。

我们如何定义我们的菠萝类型？我们在 Swift 中喜欢值类型，所以我们把菠萝定义为一个由重量和成熟度决定的结构体。

让我们看看它是如何工作的。当两艘船在公海相遇时，我们实际上是把菠萝实例的一份拷贝从一艘船传递到另一艘船，每艘船都有自己的副本。

如果你修改这些副本，比如调用 slice() 和 ripen() 方法，它对另一个副本不会有任何影响。

Swift 一直偏爱值类型，正是因为这个原因——修改只有局部影响。

这一原则帮助值类型保持隔离。

现在，让我们扩展一下数据模型，加入小鸡！与基本上只能用来吃的菠萝不同，小鸡是美丽的生物，有自己独特的个性。

所以，我们将用一个类来模拟它们，像这样。

让我们勇敢的水手们交换一只小鸡。

当两艘船相遇时，我们分享这只小鸡，只不过复制像小鸡这样的引用类型不会给你另一只完整的小鸡副本，而是给你一个指向那个特定对象的引用。

所以一旦两艘船分道扬镳，我们会发现一个问题：两艘船都在并发地做它们的工作，但它们并不独立，因为它们都引用同一个小鸡对象。

这种共享的可变状态容易产生数据争用，例如当一艘船试图喂小鸡，而另一艘船想和小鸡玩时，就会导致一只非常困惑的小鸡。

我们需要一种方法来知道在小船之间分享菠萝是安全的，但分享小鸡则不安全。

然后我们需要在 Swift 编译器中加入一些检查，以确保小鸡不会被意外地从一艘船传到另一艘船。

Swift 协议是对类型进行分类的好方法，这样你就可以推理它们的行为。

Sendable 协议用于描述可以安全地在不同隔离域之间共享、而不会产生数据争用的类型。

通过编写一个实现声明，可以使一个类型成为 Sendable。

Pineapple 结构体满足 Sendable，因为它是一个值类型，但 Chicken 类不能，因为它是一个未同步的引用类型。

将 Sendable 建模为一个协议，让我们能够描述数据将在哪些地方跨隔离域共享。

例如，当一个任务返回一个值时，这个值会被提供给所有正在等待该值的任务。

这里，我们试图从 Task 中返回一个 Chicken，并且我们得到一个错误，指出这是不安全的，因为 Chicken 不是 Sendable。

实际的 Sendable 约束来自 Task 结构体本身的定义，它指定了 Task 的结果类型（称为 Success）必须满足 Sendable 协议。

在你拥有泛型参数且它们的值会跨不同隔离域传递的地方，你应该使用 Sendable 约束。

现在，让我们重新审视一下在小船之间共享数据的想法。

当两艘船在公海上相遇并想要共享数据时，我们需要有人持续地检查所有货物，确保它们可以安全共享。

这就是我们友好的海关检查员——由 Swift 编译器扮演——的角色，确保只有 Sendable 类型才能被交换。

菠萝没问题，可以自由交换，因为它是 Sendable。

然而，小鸡不能被交换，我们友好的海关检查员会阻止我们犯这个错误。

编译器在众多不同的点上参与检查 Sendable 的正确性。

Sendable 类型必须在构造上就是正确的，并且不能允许任何共享数据通过它们走私出去。

枚举和结构体通常定义值类型，它们复制所有实例数据以产生独立的值。

因此，只要它们的所有实例数据也都是 Sendable，它们就可以是 Sendable。

Sendable 可以通过条件实现传播到集合和其他泛型类型。

Sendable 类型的数组是 Sendable，所以装满菠萝的 Crate 也是 Sendable。

所有这些 Sendable 实现甚至可以被 Swift 编译器针对非公开类型推断出来，因此 Ripeness、Pineapple 和 Crate 都是隐式 Sendable 的。

但是，假设我们创建一个 coop 来容纳我们的一群小鸡。

这个类型不能标记为 Sendable，因为它包含非 Sendable 的状态：Chicken 不是 Sendable，所以小鸡数组也不是 Sendable。

我们会从编译器得到一个错误消息，指示这个类型不能安全地共享。

类是引用类型，所以它们只能在非常狭窄的条件下被标记为 Sendable，例如当一个 final 类只拥有不可变存储时。

我们尝试将 Chicken 类标记为 Sendable 会产生一个错误，因为它包含可变状态。

现在，实现自己进行内部同步的引用类型是可能的，例如，通过一致地使用锁。

这些类型在概念上是 Sendable 的，但 Swift 无法对此进行推理。

使用 `@unchecked Sendable` 来禁用编译器的检查。

在使用时要小心，因为通过 `@unchecked Sendable` 走私可变状态会破坏 Swift 提供的数据争用安全保障。

任务创建涉及在一个新的、独立的任务中执行一个闭包，就像从你的船上放下一艘小艇。

当我们这样做时，我们可以从原始任务中捕获值并将它们传递到新任务中，所以我们需要 Sendable 检查来确保我们不引入数据争用。

如果我们确实尝试跨这个边界共享一个非 Sendable 类型，Swift 编译器会为我们兜底，产生一个像这样的错误消息。

这对于任务创建来说并不是魔法。

闭包被推断为一个 Sendable 闭包，这本来可以显式地写成 `@Sendable`。

Sendable 闭包是 Sendable 函数类型的值。

`@Sendable` 可以写在一个函数类型上，以指示该函数类型满足 Sendable 协议。

这意味着该函数类型的值可以被传递到其他隔离域并在那里调用，而不会在其捕获的状态上引入数据争用。

通常，函数类型不能满足协议，但 Sendable 是特殊的，因为编译器验证它的语义要求。

对于 Sendable 类型的元组也支持满足 Sendable 协议，这允许 Sendable 在整个语言中使用。

我们描述的系统有许多并发执行且彼此隔离的任务。

Sendable 协议描述了可以在任务之间安全共享的类型，Swift 编译器在每个级别检查 Sendable 实现以维持任务的隔离。

然而，如果在任何地方都没有共享可变数据的概念，任务很难进行有意义的协调。

所以我们需要某种方式在我们的任务之间共享数据，同时不重新引入数据争用。

这就是 Actor 的用武之地。

Actor 提供了一种隔离状态的方法，这些状态可以被不同任务访问，但是以一种消除了数据争用的协调方式访问。

Actor 是我们并发之海中的岛屿。

像小船一样，每个岛屿都是自包含的，拥有自己独立于海上其他一切的状态。

要访问那个状态，你的代码需要在岛屿上运行。

例如，advanceTime 方法被隔离到这个岛屿。

它存在于岛屿上，可以访问岛屿的所有状态。

要实际在岛屿上运行代码，你需要一艘小船。

一艘小船可以访问该岛屿以在岛屿上运行代码，此时它可以访问那个状态。

一次只能有一艘小船访问该岛屿以运行代码，这确保了对岛屿状态没有并发访问。

如果其他小船出现，它们必须等待轮到它们访问该岛屿。

而且，因为一艘特定小船可能需要很长时间才能有机会访问该岛屿，进入一个 Actor 是一个潜在的挂起点，由 “await” 关键字标记。

一旦岛屿空闲——同样是在挂起点——另一艘船就可以访问。

就像两艘船在公海上相遇一样，一艘船和一个岛屿之间的交互需要维持两者的隔离，通过确保非 Sendable 类型不会在两者之间传递。

例如，也许我们试图从小船上添加一只小鸡到岛屿上的鸡群中。

这会在不同的隔离域中创建对同一只小鸡对象的两个引用，所以 Swift 编译器拒绝了它。

同样，如果我们试图从岛屿领养一只宠物小鸡并把它带到我们的小船上，Sendable 检查会确保我们无法创建这个数据争用。

Actor 是引用类型，但与类不同，它们隔离了它们所有的属性和代码以防止并发访问。

因此，从一个不同的隔离域持有一个 Actor 的引用是安全的。

这就像拥有一张去往岛屿的地图：你可以使用地图去参观那个岛屿，但你仍然需要通过停靠程序来访问它的状态。

因此，所有 Actor 类型都是隐式 Sendable 的。

你可能想知道如何知道哪些代码是隔离到 Actor 的，哪些代码不是。

Actor 隔离由你所在的上下文决定。

Actor 的实例属性被隔离到该 Actor。

Actor 上或 Actor 扩展中的实例方法默认也是隔离的，比如这个 advanceTime 方法。

非 Sendable 的闭包，比如传递给 reduce 算法的闭包，停留在 Actor 上，并且当它们处于 Actor 隔离的上下文中时是 Actor 隔离的。

Task 初始化器也从其上下文继承 Actor 隔离，因此创建出来的任务将在与它被创建时相同的 Actor 上被调度。

在这里，这赋予了访问 flock 的权限。

另一方面，一个 detached 任务不会从其上下文继承 Actor 隔离，因为它完全独立于它被创建时的上下文。

我们可以看到，这里的闭包中的代码被认为是在 Actor 之外，因为它需要使用 “await” 来引用隔离的 “food” 属性。

我们给这个闭包起了一个术语：它是 non-isolated 代码。

Non-isolated 代码是完全不在任何 Actor 上运行的代码。

你可以通过使用 `nonisolated` 关键字显式地使 Actor 内部的函数成为 non-isolated，将其置于 Actor 之外。

就像为 detached 任务使用的闭包中隐式发生的那样。

这意味着如果我们想读取一些隔离到 Actor 的状态，我们需要使用 “await” 来访问岛屿并获取我们需要的状态的副本。

Non-isolated 异步代码总是在全局协作池上运行。

可以把它想象成只有当船在公海时才会运行，所以你必须离开你正在访问的岛屿去做工作。

这意味着要检查以确保你没有带走任何非 Sendable 数据！在这里，编译器检测到了潜在的数据争用，其中非 Sendable Chicken 的一个实例正试图离开该岛屿。

让我们再考虑一个 non-isolated 代码的情况。

“greet” 操作是 non-isolated 的同步代码。

它对小船或岛屿或一般的并发一无所知。

在这里，我们从 Actor 隔离的 greetOne 函数中调用它，这是可以的！这个同步代码，当从岛屿调用时，将停留在岛屿上，因此它可以自由地操作鸡群中的小鸡。

相反，如果我们有一个 non-isolated 的异步操作调用了 “greet”，那么 “greet” 将在那里，在小船上，在公海上运行。

大多数 Swift 代码都是这样的：同步的，不隔离到任何 Actor，只操作给它提供的参数，所以它停留在它被调用的隔离域中。

Actor 持有与程序其余部分隔离的状态。

一次只能有一个任务在 Actor 上运行，因此对该状态没有并发访问。

Sendable 检查在任务进入或退出 Actor 时应用，以确保没有未同步的可变状态逃逸。

总而言之，这使 Actor 成为 Swift 中并发程序的构建块之一。

还有另一个我们经常谈到的特殊 Actor，叫做主要 Actor（main actor）。

把主要 Actor 想象成大海中央的一个大岛。

它代表主线程（main thread），所有用户界面的绘制和交互都在那里发生。

所以如果你想绘制一些东西，你需要在主要 Actor 的岛屿上运行代码。

它对你的 UI 如此重要，也许我们甚至应该称之为 “U-I-land”。当我说主要 Actor 是“大”的，我的意思是它包含了许多与程序用户界面相关的状态。

有很多代码，无论是在 UI 框架中还是在你的 App 中，都需要在它上面运行。

然而，它仍然是一个 Actor，所以它一次只运行一个任务。

因此你必须小心不要在主要 Actor 上放置太多或运行时间过长的工作，因为它可能会使你的 UI 无响应。

对主要 Actor 的隔离通过 `@MainActor` 特性（attribute）来表达。

这个特性可以应用于一个函数或闭包，以指示该代码必须在主要 Actor 上运行。

然后，我们说这段代码被隔离到主要 Actor。

Swift 编译器将保证主要 Actor 隔离的代码只会在主线程上执行，使用与确保其他 Actor 互斥访问相同的机制。

如果一个人从一个没有隔离到主要 Actor 的上下文中调用 updateView，它将需要引入一个 “await” 来考虑切换到主要 Actor。

`@MainActor` 特性也可以应用于类型，在这种情况下，这些类型的实例将被隔离到主要 Actor。

同样，这就像任何其他 Actor 一样——属性只有在主要 Actor 上才能访问，方法则被隔离到主要 Actor，除非它们明确选择退出。

与普通 Actor 一样，对主要 Actor 类的引用本身就是 Sendable 的，因为它们的数据是隔离的。

这使得 `@MainActor` 注解适用于你的 UI 视图和视图控制器（view controllers），它们本身就被框架绑定到主线程。

你可以将指向你的视图控制器的引用分享给程序中的其他任务和 Actor，它们可以异步回调到视图控制器以发布结果。

这对你的 App 架构有直接的影响。

在你的 App 中，你的视图和视图控制器将在主要 Actor 上。

其他程序逻辑应该与那个主要 Actor 分离，使用其他 Actor 来安全地建模共享状态，使用任务来描述独立的工作。

而这些任务可以根据需要在主要 Actor 和其他 Actor 之间穿梭。

在并发 App 中有很多事情发生，所以我们构建了一些很棒的工具来帮助你理解它。

我邀请你查看“《可视化并优化 Swift 并发》讲座”以了解更多。

让我们深入更深的水域来谈谈原子性（atomicity）。

Swift 并发模型的目标是消除数据争用。

这真正意味着它消除了低级别的数据争用，涉及数据损坏。

你仍然需要在高级别上推理原子性。

正如我们之前讨论过的，Actor 一次只运行一个任务。

然而，当你停止在 Actor 上运行时，Actor 可以运行其他任务。

这确保了程序持续推进，消除了死锁的可能性。

然而，这要求你在 `await` 语句周围仔细考虑你的 Actor 的不变量。

否则，你最终可能得到一个高级别的数据争用，其中程序处于意外状态，即使没有数据被实际损坏。

让我们分解一个例子。

这里我们有一个意图向一个岛屿存入一些额外菠萝的函数。

它在 Actor 外部，所以是 non-isolated 异步代码。

这意味着它在这里的公海上运行。

它被给了一些菠萝和一张通往它应该存放这些菠萝的岛屿的地图。

这里的第一个有趣的操作是从岛屿获取 `food` 数组的一份副本。

要做到这一点，小船需要访问该岛屿，由 “await” 关键字指示。

一旦它有了食物的副本，小船就回到公海继续它的工作。

这意味着将 `pineapples` 参数中的菠萝添加到它从岛屿得到的那两个菠萝中。

现在，我们可以继续到函数的最后一行。

我们的小船现在需要再次访问该岛屿，将岛屿的 `food` 数组设置为那三个菠萝。

在这里，一切都很顺利，岛上有了三个菠萝！但事情可能会有不同的发展。

假设一艘海盗船在我们第一艘船等待轮到它访问岛屿时潜入并偷走了所有的菠萝。

现在，我们最初的船将其三个菠萝存入岛屿，我们注意到一个问题。

三个菠萝突然变成了五个菠萝！这里发生了什么？嗯，注意我们有两次 `await` 来访问同一个 Actor 上的状态，我们在这里做了一个假设，即岛屿上的 `food` 数组在这两次 `await` 之间不会改变。

但这些都是 `await`，意味着我们的任务可能会在这里被挂起，而 Actor 可以做其他更高优先级的工作，比如与海盗战斗。

在这个具体案例中，Swift 编译器会拒绝直接修改另一个 Actor 上的状态的尝试。

然而，我们真的应该将我们的 `deposit` 操作重写为 Actor 上的同步代码，像这样。

因为这是同步代码，它会在 Actor 上不间断地运行。

所以我们可以确保，在整个函数执行期间，岛屿的状态不会被其他任何人改变。

当你编写你的 Actor 时，要以同步的、事务性的操作来思考，这些操作可以以任何方式交错。

每一个操作都应该确保 Actor 在退出时处于良好状态。

对于异步 Actor 操作，保持它们简单，主要由你的同步的事务性操作构成，并注意你的 Actor 在每一个 `await` 操作处都处于良好状态。

这样，你就可以充分利用 Actor 来消除低级别和高级别两种数据争用。

在并发程序中，许多事情同时发生，所以这些事情发生的顺序会因一次执行而不同。

然而，程序通常依赖于以一致的顺序处理事件。

例如，来自用户输入或来自服务器的消息的事件流。

当这些事件流进来时，我们期望它们的效果按顺序发生。

Swift 并发为操作排序提供了工具，然而，Actor 并不是做这件事的工具。

Actor 首先执行最高优先级的工作，以帮助整个系统保持响应性。

这消除了优先级反转，即低优先级工作最终发生在同一 Actor 上的高优先级工作之前。

请注意，这与串行 Dispatch 队列有显著区别，后者严格按先进先出顺序执行。

Swift 并发有几个用于排序工作的工具。

第一个我们已经谈论了很多——任务。

任务从头到尾执行，具有你习惯的正常控制流，所以它们自然地排序工作。

AsyncStream 可以用来模拟一个实际的事件流。

一个任务可以用 `for await in` 循环遍历事件流，依次处理每个事件。

一个 AsyncStream 可以共享给任意数量的事件生产者，它们可以在保持顺序的同时向流中添加元素。

我们已经讨论了很多关于 Swift 的并发模型如何设计为使用隔离的概念来消除数据争用，这种隔离通过在任务和 Actor 边界进行 Sendable 检查来维持。

然而，我们不能所有人立刻停止我们正在做的事情，去把所有地方的 Sendable 类型都标记上。

相反，我们需要一种增量式的方法。

Swift 5.7 引入了一个构建设置，用于指定 Swift 编译器检查 Sendable 的严格程度。

默认设置是 Minimal，意味着编译器只会在有人明确尝试将某些东西标记为 Sendable 的位置进行诊断。

这与 Swift 5.5 和 5.6 的行为类似，对于上述情况，不会有任何警告或错误。

现在，如果你添加一个 Sendable 实现，编译器会抱怨 Coop 类型不能是 Sendable，因为 Chicken 不是 Sendable。

然而，这个以及其他与 Sendable 相关的问题在 Swift 5 中会作为警告呈现，而不是错误，以便更容易地逐个解决问题。

为了进一步向数据争用安全迈进，启用 “targeted” 严格并发设置。

这个设置为已经采用了 Swift 并发特性（如 async/await、任务或 Actor）的代码启用 Sendable 检查。

例如，这将识别出在新创建的任务中捕获非 Sendable 类型值的尝试。

有时非 Sendable 类型来自另一个模块。

可能是一些还没有为 Sendable 更新的包，甚至是你自己还没有来得及处理的模块。

对于这些情况，你可以使用 `@preconcurrency` 特性临时禁用来自该模块类型的 Sendable 警告。

这将在此源文件内为 Chicken 类型静默 Sendable 警告。

在某个时候，FarmAnimals 模块将附带 Sendable 实现进行更新。

然后，会出现两种情况之一：要么 Chicken 以某种方式变成了 Sendable，在这种情况下，`@preconcurrency` 特性可以从 import 语句中移除。

要么 Chicken 将被认为是非 Sendable 的，在这种情况下，警告会回来，表明你关于 Chicken 是 Sendable 的假设实际上是不正确的。

Targeted 严格性设置试图在现有代码的兼容性和识别潜在数据争用之间取得平衡。

然而，如果你想看到所有可能发生争用的地方，还有一个选项：complete 检查。

Complete 检查近似于预期的 Swift 6 语义，以完全消除数据争用。

它检查了前两种模式检查的所有内容，但针对模块中的所有代码进行检查。

在这里，我们实际上根本没有使用 Swift 的并发特性。

相反，它是在一个 Dispatch 队列上执行工作，该队列将并发地执行那段代码。

Dispatch 队列上的异步操作实际上被认为是接受一个 Sendable 闭包，因此当非 Sendable 的 `body` 被队列上运行的代码捕获时，编译器会产生一个警告，表明存在数据争用。

我们可以通过使 `body` 参数成为 Sendable 来修复这个问题。

这个更改消除了这个警告，现在 `doWork` 的所有调用者都知道他们需要提供一个 Sendable 闭包。

这意味着我们对数据争用有了更好的检查，我们可以看到 `visit` 函数现在是数据争用的来源。

Complete 检查将帮助清除程序中潜在的数据争用。

为了实现 Swift 消除数据争用的目标，我们最终需要达到 complete 检查。

我们鼓励你逐步朝着这一目标前进：采用 Swift 的并发模型来为数据争用安全而设计你的 App，然后逐步启用更严格的并发检查，以消除代码中的错误类别。

不要为用 `@preconcurrency` 标记 import 来抑制导入类型的警告而烦恼。

随着这些模块采用更严格的并发检查，编译器将重新检查你的假设。

在这条路的尽头，你的代码将受益于内存安全和数据争用安全，帮助你专注于构建优秀的 App。

感谢你和我一起在并发的海洋上航行。

♪
