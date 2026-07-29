---
title: 协议扩展中的方法派发
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/06/lily-ballard-swift-dispatch/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b319a9cf16551aa7'
translated: true
---

> 原文：[Method Dispatch in Protocol Extensions](https://oleb.net/blog/2016/06/lily-ballard-swift-dispatch/)　·　Ole Begemann

# 协议扩展中的方法派发

我们在 [WWDC 2015 的“面向协议编程”讲座](https://developer.apple.com/videos/play/wwdc2015-408/?time=1767)中了解到，Swift 对协议扩展中的方法使用了两种不同的派发机制。^[1](#fn:1) 那些属于 _协议要求_ 的方法（即在协议本身中声明的方法）是动态派发的，而不属于协议要求的方法则使用静态派发。

我记得去年曾疑惑为什么 Swift 要做这种区分。当时对我来说这并不合理，而且[和其他人一样](https://nomothetis.svbtle.com/the-ghost-of-swift-bugs-future)，我担心这会潜在地引发大量难以发现的 Bug。（事实证明，到目前为止在实践中这对我并没有造成问题。）我最近偶然看到 Lily Ballard 在 [Swift Evolution](https://forums.swift.org/c/evolution/discuss) 上发的[这篇文章](https://forums.swift.org/t/proposal-universal-dynamic-dispatch-for-method-calls/237/57)，其中包含了我所见过对协议中方法派发机制的最佳解释：

> [协议扩展] 自始至终严格遵循静态类型。这很合理，因为根本没有虚函数表（或用 Swift 的术语来说，协议见证表（protocol witness table））来存放这些方法。扩展可以提供协议方法的默认实现，因为遵循协议的类型会将该扩展方法的实现放入自己的协议见证表中（并且只有当该类型本身没有实现该方法时才会这样做）。由于协议见证表只包含协议本身定义的内容，不属于协议的协议扩展方法就没有地方可放。因此，调用这些方法时没有任何虚函数表可供查询，唯一能做的就是静态调用扩展中的方法。这就是为什么你不能重写它们（或者更准确地说，当方法解析通过协议进行时，你的重写不会被调用）的原因。
>
> 要让协议扩展方法通过虚派发工作，唯一的办法是为扩展本身定义一个新的协议见证表，但在定义类型时无法看到这个扩展，类型自然也就不知道要创建和填充这个协议见证表。[……]
>
> 我能想到的唯一其他解决方案是把所有协议派发都变成动态派发，但我想你会同意这并非一个好主意。

所以本质上，尽管协议拥有虚函数表，但协议扩展并没有，而且很难拥有，因为采用协议的类型在编译时不一定知道所有扩展，因此无法将扩展方法添加到自己的虚函数表中。对于是否总是对协议进行动态派发是一个可行的替代方案，可能见仁见智，但这显然不是 Swift 团队对该语言的设计意图。

如果你想深入了解 Swift 类型在内存中的内部布局及其包含的信息，请查看 [Swift ABI 文档](https://github.com/apple/swift/blob/master/docs/ABI.rst)。非常有趣。

1. [观看视频](https://developer.apple.com/videos/play/wwdc2015-408/?time=1767)，从 29 分 27 秒开始。[↩︎](#fnref:1)
