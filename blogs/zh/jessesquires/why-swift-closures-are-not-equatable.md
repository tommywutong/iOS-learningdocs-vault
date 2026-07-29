---
title: 为什么 Swift 闭包不是 Equatable 的
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2021/04/05/why-swift-closures-are-not-equatable/'
original_language: en
published: 2021-04-05
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bc29cb368109680c'
translated: true
---

> 原文：[Why Swift closures are not Equatable](https://www.jessesquires.com/blog/2021/04/05/why-swift-closures-are-not-equatable/)　·　Jesse Squires

尽管在 Swift 中闭包（closure）和函数[是引用类型](https://docs.swift.org/swift-book/LanguageGuide/Closures.html#ID104)，但它们不能使用 `==` 或 `===` 进行比较。但这是为什么呢？

今天我钻了一次牛角尖，因为我原以为我需要这个功能（实际上并不需要）。在其他语言（比如 Objective-C）中，比较函数指针很容易做到。但在 Swift 中，你会收到一个错误。尝试使用 `==` 比较两个签名相同的闭包（或函数）会产生编译器错误 “Binary operator ‘==’ cannot be applied”。如果你尝试使用 `===`，编译器会产生错误 “Cannot check reference equality of functions”。

为了寻找原因，我最终找到了 [Apple Developer Forums 上的这个讨论](https://developer.apple.com/forums/thread/666060?answerId=645336022#645336022)。讽刺的是，它链接到了 [StackOverflow 上的这个讨论](https://stackoverflow.com/questions/24111984/how-do-you-test-functions-and-closures-for-equality)，后者又链接到了[旧的 Apple Dev Forums 讨论](https://devforums.apple.com/message/1035180#1035180)，当然，这个链接现在已经失效了，因为去年[新论坛上线](https://developer.apple.com/news/?id=obvo7r3i)时，Apple 没有人愿意认真地做 Web 开发。

##### [更新](#updated-06-april-2021)  _2021 年 4 月 6 日_

一位读者善意地指出，指向 Chris 帖子的失效链接并不是去年丢失的，而是在更早几年的从私有论坛到公共论坛的**前一次过渡（transition）**中丢失的。我已经数不清 Apple Dev Forums 经历过多少次改版了。[论坛上的这个讨论](https://developer.apple.com/forums/thread/653468?answerId=620033022#620033022)有详细信息。当然，回答者正是那位宝贵而传奇的 [Quinn](https://github.com/macshome/The-Wisdom-of-Quinn)。

总之，显然在旧论坛的某个角落，存在着来自 [Chris Lattner](https://twitter.com/clattner_llvm) 的以下回答。（谢天谢地，StackOverflow 上的人直接引用了论坛的讨论内容，而不只是发布了一个链接。）

> 这是一个我们有意不打算支持的特性。有多种因素会导致函数（在 Swift 类型系统的意义上，它包含多种闭包）的指针相等（pointer equality）失败或因优化而改变。如果对函数定义了 `===`，编译器将不允许合并相同的方法体、共享 thunk，以及执行闭包中的某些捕获优化。此外，这种相等性在泛型上下文中会极其令人惊讶，因为你会得到调整函数实际签名以匹配函数类型所期望签名的重抽象 thunk（reabstraction thunk）。

你不仅不能比较函数指针，而且就算能比较，你也是在自找麻烦。

#### * * *

当然，你可以深入 Swift 的 “unsafe” API，创建一个 `UnsafePointer` 来比较它们，等等。但这是个非常糟糕的主意。™ 即使你最终写出的东西通过了单元测试，它在开启了优化的情况下也可能无法正常工作——或者更糟糕的是，它只是偶尔能工作。或者，它会在未来失效。

就像我说的，事实证明我**根本**不需要真的去比较函数指针。有一个更好的解决方案。你可能认为你需要这个功能。但你（几乎肯定）并不需要。
