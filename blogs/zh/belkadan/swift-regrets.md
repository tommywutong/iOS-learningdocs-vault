---
title: Swift 的遗憾
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2021/09/Swift-Regrets/'
original_language: en
published: 2021-09-10
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ba1ddefb7eb3b8ae'
translated: true
---

> 原文：[Swift Regrets](https://belkadan.com/blog/2021/09/Swift-Regrets/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift 遗憾：未应用的实例方法](https://belkadan.com/blog/2021/09/Swift-Regret-Unapplied-Instance-Methods/)

[Swift 遗憾：下标参数标签规则](https://belkadan.com/blog/2021/09/Swift-Regret-Subscript-Argument-Label-Rules/) »

« [Swift 遗憾：未应用的实例方法](https://belkadan.com/blog/2021/09/Swift-Regret-Unapplied-Instance-Methods/?tag=swift)

[Swift 遗憾：下标参数标签规则](https://belkadan.com/blog/2021/09/Swift-Regret-Subscript-Argument-Label-Rules/?tag=swift) »

« [Swift 遗憾：未应用的实例方法](https://belkadan.com/blog/2021/09/Swift-Regret-Unapplied-Instance-Methods/?tag=swift-regrets)

[Swift 遗憾：下标参数标签规则](https://belkadan.com/blog/2021/09/Swift-Regret-Subscript-Argument-Label-Rules/?tag=swift-regrets) »

« [多对多协议](https://belkadan.com/blog/2018/02/Many-to-Many-Protocols/?tag=programming-languages)

[Swift 的遗憾：总结](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/?tag=programming-languages) »

## [Swift 的遗憾](#)

过去几周里，我一直在 Twitter 上写关于「Swift 的遗憾」的话题串，讲的是 Swift 早期开发中，我希望我们能做得不一样的那些事。我之所以选择在 Twitter 上写，而不是写成博客文章，是因为我的 [RSI](https://belkadan.com/blog/2021/07/Keyboard-Pants/)——工作中我已经在键盘上花了太多时间，在手机上写短文比在键盘前写长文要轻松得多。但我还是把它们搬到这里来，稍作编辑，好让它们不至于消失在 Twitter 那永恒的历史长河里。你可以在 [Swift 的遗憾](https://belkadan.com/blog/tags/swift-regrets/) 这个标签下找到它们。

我从 Swift 发布前到 Swift 5.1 期间一直在 [Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/) 参与 Swift 的开发。人们喜欢 Swift 的很多东西、以及讨厌 Swift 的很多东西，我都至少要负部分责任。这份清单是我离开 Apple 前后开始收集的，我把它们公开出来，是希望其他语言设计者能从我们的错误里学到点什么。这些都是如今很难在 Swift 里改动的东西，因为它们会破坏大量人的代码。[现实世界的语言和库就是这样：用户越多，你能做的破坏性改动就越少。](https://mobile.twitter.com/UINT_MIN/status/1426402680763600900)

话虽如此，我不希望大家觉得「哦，Jordan 讨厌 Swift」，或者「天哪，Swift 里有这么多问题，他们怎么就搞不对呢」。这绝对*不是*这里想传达的意思。我爱 Swift。我向你保证，每一门语言都有它的疙瘩、错误和妥协。而且 Swift 做的很多事情也不是全新的；它是在借鉴、或许还改进了其他语言的一些想法。所以未来的语言应该在 Swift 的基础上做得更好，但与此同时，我也决定加入一些「Swift 的惊喜」，也就是我希望其他语言也能借鉴的东西。它们并不是只有 Swift 才有的东西，但它们*确实*是我在 Swift 里很欣赏、也希望未来语言里也能看到的东西。

显然我预料到大家会在很多条上和我意见不同；说实话，就算是过去的我，对其中不少条也会不同意，这也正是事情变成如今这样的原因！另外，欢迎随时提问。（如果你对某一条特别感兴趣，我建议去看看对应的 Twitter 话题串，看看别人还补充了些什么。）

本文发表于 [2021](https://belkadan.com/blog/2021) 年 [9](https://belkadan.com/blog/2021/09) 月 10 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[Swift 的遗憾](https://belkadan.com/blog/tags/swift-regrets)、[编程语言](https://belkadan.com/blog/tags/programming-languages)
