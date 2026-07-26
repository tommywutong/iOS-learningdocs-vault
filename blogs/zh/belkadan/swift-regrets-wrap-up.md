---
title: 'Swift 的遗憾：总结'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/'
original_language: en
published: 2021-12-31
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f9f8a51aaaf11e78'
translated: true
---

> 原文：[Swift Regrets: Wrap-up](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift 历史：赋值方法](https://belkadan.com/blog/2021/12/Swift-History-Assignment-Methods/)

[动态链接对 App 不利，静态链接对 App 也不利](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/) »

« [Swift 历史：赋值方法](https://belkadan.com/blog/2021/12/Swift-History-Assignment-Methods/?tag=swift)

[默认参数与基于标签的重载](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=swift) »

« [Swift 历史：赋值方法](https://belkadan.com/blog/2021/12/Swift-History-Assignment-Methods/?tag=swift-regrets)

« [Swift 的遗憾](https://belkadan.com/blog/2021/09/Swift-Regrets/?tag=programming-languages)

[默认参数与基于标签的重载](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=programming-languages) »

## [Swift 的遗憾：总结](#)

就这样，五个月的 [Swift 的遗憾](https://belkadan.com/blog/2021/09/Swift-Regrets/)（以及惊喜）系列到此结束——这些都是我在 Apple 的最后一年里陆续收集起来的东西……还有一些是后来在 Twitter 上的讨论中冒出来的。我想聊聊这些事情，是因为每个项目都会从前人身上学习，而这既应该包括好的部分，也应该包括不好的部分。我记得我以前的同事 [Joe Groff](https://twitter.com/jckarter) 说过，我们应该把在我们这个领域里谈论错误和失误正常化、并加以鼓励，所以这篇也算是我的一份贡献。

所有这些 Twitter 话题串都收集在了这个网站的「[Swift 的遗憾](https://belkadan.com/blog/tags/swift-regrets/)」标签下。它并不是一份关于 Swift 好坏之处的详尽清单，但确实涵盖了相当广的范围。我个人最喜欢的大概是我最早写的几篇之一，[Sequence](https://belkadan.com/blog/2021/08/Swift-Regret-Sequence/)。它把问题和可能的解法都讲得很清楚——当然，这是我自己的看法。

那么这个系列带来的收获是什么呢？除了「\<某特性\> 是个错误，在你的语言里加入类似特性前要三思」之外，我觉得我们大概还能提炼出几个更高层次的想法，其中最重要的一点是：语言开发到某个阶段，你就再也没法随便改东西了！这是一个大多数软件项目都不用面对的限制，只有（被广泛采用的）语言、具备 ABI 稳定性的库、以及交换格式才会遇到。在其他任何地方，你都可以推出一个替代旧版本的大版本，人们要么迁移过去要么不迁移——这可能很难，但*总归*是个选项。我觉得对于大多数来自开源项目、或者纯粹的 App 项目的人来说，这是一种文化冲击。（我说这些的时候，其实很清楚从 Swift 1b1 到 Swift 3 之间发生过*海量*的改动，所以想到居然还有一些东西*到现在*都没能、或者没法修好……）

这是最重要的一点。还有一些和「遗憾」相关的建议：

- 增加能力比去掉限制要容易，反过来就难得多。只要提供了某个特性，人们就会立刻开始用它，尤其是当它是完成某项任务的唯一方式时；即便你之后引入了一个众口称赞的更好特性，去掉旧的那个也会变成一次破坏性改动。
- 如果你*打算*搞破坏性改动，就大胆地做，因为你多半不会有第二次机会了。
- 把你最有野心的改动放在早期做，这样你才有机会试验、调整……如果有必要的话还能撤回。
- 话虽如此，除非你能举出真实世界里的用例，否则不要加入那些看起来「很酷」「很巧妙」甚至「显而易见」的东西。不然它可能是个陷阱，或者是额外的复杂度，再不济也是一样要永远维护下去的东西。
- 与此相关的是：如果某个特性在别的具备类似功能的语言里没被支持，也许是有原因的。
- 隐式的东西可以很方便，但它也可能是个糟糕的默认行为。
- 一致性是好事：意味着更少的实现，也意味着更少要学的东西。
- 但看起来互不相关的特性，也可能以奇怪的方式相互影响。
- 有机会回头把某件事重做一遍是很罕见的；你的第一版最好足够好，能撑到永远，哪怕你以后想回头修它。
- 与此相关的是：完美是好的敌人，好也是完美的敌人。没错，这在两个方向上都是问题。
- 但有时候你要等到东西被真正用起来了，才会知道自己做错了。而且有时候根本没有一个明显的正确答案。

在「惊喜」这一边，我觉得没那么容易找出一条能把所有东西串起来的主线，但这里还是有一些想法：

- 我在 Swift 里最喜欢的一些东西，其实是对其他语言早就有的东西做的一点点调整。有时候你能做的最好的事情，不是从零开始创造，而是打磨它、让它更容易被用起来……或者如果这是对的做法，干脆直接照搬别人已经做过的东西。（这是很典型的 Apple 式做法。）
- 类似地，你自己可能没法打破兼容性，但你可以找出所有*别人*希望能打破兼容性的地方，然后跟着做。
- 所有那些老生常谈的箴言，比如「简单的事情应该简单，困难的事情应该可能」「API 应该引导你走向正确的用法」「[清晰胜于简洁](https://swift.org/documentation/api-design-guidelines/)」，等等。

说了这么多，我大概还是应该再回答一次这个问题：「如果能让事情变得更好，打破兼容性不是值得的吗？」当你在谈论一门编程语言的时候，旧版本*不会消失*，如果你还能在编译期导入旧版本的库，那就是双重不会消失，而在 Apple 平台上加上 ABI 稳定性，那就是三重不会消失。打破兼容性意味着要么疏远你的用户，要么在未来多年里同时维护多个版本，或者更可能的是两者都要做，所以这些改动*最好*是值得的。（这里还有一个规模的问题：Apple 平台上有数百万开发者，进而大概有十亿量级的用户。）

我还想再重申一次，这里想传达的*不是*「Swift 是个失败品，你看看它有多少问题」。*所有*语言都有这样一份清单；我之所以为 Swift 做这件事，是因为我参与过 Swift 的开发，能提供一些关于事情为什么、以及怎样变成现在这样的洞见。我很想看到其他语言设计者也写一写他们的文章和话题串，讲讲他们后悔的地方、以及哪些地方经受住了时间考验。

这个系列引发了不少很好的讨论，我尤其想特别感谢一下 [Dave Zarzycki](https://twitter.com/davezarzycki)，他在 Apple 工作的许多年里也参与过早期 Swift 的开发，以及其他一些项目（包括最初的 launchd）。在我们的一次私下交流里，他提出了这样一个想法，说的是一门能持续用上很多年、并且适合大型协作项目的语言：

> 假设成功一定会发生，然后尽早解决*人*的规模化问题。就这样。
>
> 话虽如此，这是一项巨大的工作量。这意味着要把一大堆默认行为定对，要认真思考各个特性之间会如何相互作用，要考虑渐进式呈现，要为 API 的演进和韧性做规划，等等等等。
>
> 更重要的是，这意味着要放弃一些新语言常常抵挡不住诱惑的「图方便的陷阱」（比如随意的隐式转换）

在我看来，这些都是很好的建议。

如果你还想看更多关于语言设计的反思，我推荐 [Joe Duffy 写的关于 Midori 的系列文章](http://joeduffyblog.com/2015/11/03/blogging-about-midori/)，那是微软的一个语言兼*操作系统*项目，比 Swift 早开始几年。这个项目后来被中止了，开发者们也回到了微软的其他部门，但它的目标其实比 Swift 还要更有野心，其中既有一些引人注目的相似之处，也有一些我们本可以从中学到的东西。

谢谢大家跟着看完这五个月。2022 年见。

本文发表于 [2021](https://belkadan.com/blog/2021) 年 [12](https://belkadan.com/blog/2021/12) 月 31 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[Swift 的遗憾](https://belkadan.com/blog/tags/swift-regrets)、[编程语言](https://belkadan.com/blog/tags/programming-languages)
