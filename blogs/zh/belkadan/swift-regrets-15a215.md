---
title: Swift 的遗憾
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/swift-regrets'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:588250b077f759a5'
translated: true
---

> 原文：[Swift regrets](https://belkadan.com/blog/tags/swift-regrets)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [Swift 的遗憾：总结](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/?tag=swift-regrets)

2021 年 12 月 31 日

就这样，五个月的 [Swift 的遗憾](https://belkadan.com/blog/2021/09/Swift-Regrets/)（以及惊喜）系列到此结束——这些都是我在 Apple 的最后一年里陆续收集起来的东西……还有一些是后来在 Twitter 上的讨论中冒出来的。我想聊聊这些事情，是因为每个项目都会从前人身上学习，而这既应该包括好的部分，也应该包括不好的部分。我记得我以前的同事 [Joe Groff](https://twitter.com/jckarter) 说过，我们应该把在我们这个领域里谈论错误和失误正常化、并加以鼓励，所以这篇也算是我的一份贡献。

[（继续阅读……）](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/?tag=swift-regrets)

发表于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[Swift 的遗憾](https://belkadan.com/blog/tags/swift-regrets)、[编程语言](https://belkadan.com/blog/tags/programming-languages)

## [Swift 历史：赋值方法](https://belkadan.com/blog/2021/12/Swift-History-Assignment-Methods/?tag=swift-regrets)

2021 年 12 月 30 日

> 为了给这个系列收尾，我打算聊一个既不是遗憾也不是惊喜、而是根本就不适合 Swift 的特性：赋值方法
> 
> — Jordan Rose (@UINT_MIN) [2021 年 12 月 30 日](https://twitter.com/UINT_MIN/status/1476649027332567050?ref_src=twsrc%5Etfw)

_属于 [Swift 的遗憾](https://belkadan.com/blog/2021/09/Swift-Regrets/) 系列。_

[（继续阅读……）](https://belkadan.com/blog/2021/12/Swift-History-Assignment-Methods/?tag=swift-regrets)

发表于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[Swift 的遗憾](https://belkadan.com/blog/tags/swift-regrets)

## [Swift 遗憾：inout 语法](https://belkadan.com/blog/2021/12/Swift-Regret-inout-Syntax/?tag=swift-regrets)

2021 年 12 月 28 日

> Swift 遗憾：inout 语法  
>   
> Swift 有 inout 参数这个概念，形式上是 copy-in/copy-out（也可能是 move-in/move-out），并在可能的情况下被优化为按引用传递。这在参数类型里写作 `inout Foo`……而在调用处写作 `&foo`。
> 
> — Jordan Rose (@UINT_MIN) [2021 年 12 月 28 日](https://twitter.com/UINT_MIN/status/1475912954000261120?ref_src=twsrc%5Etfw)

_属于 [Swift 的遗憾](https://belkadan.com/blog/2021/09/Swift-Regrets/) 系列。_

[（继续阅读……）](https://belkadan.com/blog/2021/12/Swift-Regret-inout-Syntax/?tag=swift-regrets)

发表于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[Swift 的遗憾](https://belkadan.com/blog/tags/swift-regrets)

## 更早的文章

1. 2021-12-26[Swift 惊喜：可选值的便利特性](https://belkadan.com/blog/2021/12/Swift-Delight-Optional-Conveniences/?tag=swift-regrets)
2. 2021-12-23[Swift 遗憾：try?](https://belkadan.com/blog/2021/12/Swift-Regret-Optional-Try/?tag=swift-regrets)
3. 2021-12-21[Swift 惊喜：try](https://belkadan.com/blog/2021/12/Swift-Delight-Try/?tag=swift-regrets)
4. 2021-12-17[Swift 遗憾：运算符函数查找规则](https://belkadan.com/blog/2021/12/Swift-Regret-Operator-Function-Lookup-Rules/?tag=swift-regrets)
5. 2021-12-15[Swift 遗憾："Double" 而非 "Float64"](https://belkadan.com/blog/2021/12/Swift-Regret-Float64/?tag=swift-regrets)
6. 2021-12-10[Swift 惊喜：隐式成员语法](https://belkadan.com/blog/2021/12/Swift-Delight-Implicit-Member-Syntax/?tag=swift-regrets)
7. 2021-12-08[Swift 遗憾：结构体中的 weak 变量](https://belkadan.com/blog/2021/12/Swift-Regret-Weak-Vars-in-Structs/?tag=swift-regrets)
8. 2021-12-03[Swift 遗憾：结构体中的 lazy 变量](https://belkadan.com/blog/2021/12/Swift-Regret-Lazy-Vars-in-Structs/?tag=swift-regrets)
9. 2021-11-30[Swift 惊喜：无未使用的结果](https://belkadan.com/blog/2021/11/Swift-Delight-No-Unused-Results/?tag=swift-regrets)
10. 2021-11-24[Swift 遗憾：open 协议](https://belkadan.com/blog/2021/11/Swift-Regret-Open-Protocols/?tag=swift-regrets)
11. 2021-11-21[Swift 遗憾：追溯一致性（Retroactive Conformances）](https://belkadan.com/blog/2021/11/Swift-Regret-Retroactive-Conformances/?tag=swift-regrets)
12. 2021-11-18[Swift 惊喜：库演进](https://belkadan.com/blog/2021/11/Swift-Delight-Library-Evolution/?tag=swift-regrets)
13. 2021-11-10[Swift mangling 之憾：私有判别符](https://belkadan.com/blog/2021/11/Swift-Mangling-Regret-Private-Discriminators/?tag=swift-regrets)
14. 2021-11-05[Swift mangling 之憾：「旧」mangling](https://belkadan.com/blog/2021/11/Swift-Mangling-Regret-The-Old-Mangling/?tag=swift-regrets)
15. 2021-11-03[Swift mangling 之憾：库演进](https://belkadan.com/blog/2021/11/Swift-Mangling-Regret-Library-Evolution/?tag=swift-regrets)
16. 2021-10-29[Swift 惊喜：#available](https://belkadan.com/blog/2021/10/Swift-Delight-Available/?tag=swift-regrets)
17. 2021-10-22[Swift 遗憾：隐式可 Hashable 的无关联值枚举](https://belkadan.com/blog/2021/10/Swift-Regret-Hashable-Enums/?tag=swift-regrets)
18. 2021-10-20[Swift 遗憾：脚本模式下的顶层声明](https://belkadan.com/blog/2021/10/Swift-Regret-Top-Level-Decls-in-Script-Mode/?tag=swift-regrets)
19. 2021-10-15[Swift 惊喜：泛型参数的名字](https://belkadan.com/blog/2021/10/Swift-Delight-Generic-Parameter-Names/?tag=swift-regrets)
20. 2021-10-13[Swift 遗憾：泛型参数不是成员](https://belkadan.com/blog/2021/10/Swift-Regret-Generic-Parameters-are-not-Members/?tag=swift-regrets)
21. 2021-10-08[Swift 遗憾：OpaquePointer](https://belkadan.com/blog/2021/10/Swift-Regret-OpaquePointer/?tag=swift-regrets)
22. 2021-10-06[Swift 遗憾：未标注的 C 枚举](https://belkadan.com/blog/2021/10/Swift-Regret-Unannotated-C-Enums/?tag=swift-regrets)
23. 2021-10-01[Swift 惊喜：值语义集合](https://belkadan.com/blog/2021/10/Swift-Delight-Value-Semantics-Collections/?tag=swift-regrets)
24. 2021-09-29[Swift 惊喜：guard](https://belkadan.com/blog/2021/09/Swift-Delight-Guard/?tag=swift-regrets)
25. 2021-09-24[Swift 遗憾：推断的属性类型](https://belkadan.com/blog/2021/09/Swift-Regret-Inferred-Property-Types/?tag=swift-regrets)
26. 2021-09-22[Swift 遗憾：隐式的可选类型初始化](https://belkadan.com/blog/2021/09/Swift-Regret-Implicit-Optional-Initialization/?tag=swift-regrets)
27. 2021-09-17[Swift 遗憾：下标的尾随闭包](https://belkadan.com/blog/2021/09/Swift-Regret-Subscript-Trailing-Closures/?tag=swift-regrets)
28. 2021-09-15[Swift 遗憾：下标参数标签规则](https://belkadan.com/blog/2021/09/Swift-Regret-Subscript-Argument-Label-Rules/?tag=swift-regrets)
29. 2021-09-10[Swift 的遗憾](https://belkadan.com/blog/2021/09/Swift-Regrets/?tag=swift-regrets)
30. 2021-09-10[Swift 遗憾：未应用的实例方法](https://belkadan.com/blog/2021/09/Swift-Regret-Unapplied-Instance-Methods/?tag=swift-regrets)
31. 2021-09-08[Swift 遗憾：绑定方法](https://belkadan.com/blog/2021/09/Swift-Regret-Bound-Methods/?tag=swift-regrets)
32. 2021-08-29[Swift 遗憾：基于类型的重载](https://belkadan.com/blog/2021/08/Swift-Regret-Type-based-Overloading/?tag=swift-regrets)
33. 2021-08-25[Swift 遗憾：AnyObject 派发](https://belkadan.com/blog/2021/08/Swift-Regret-AnyObject-Dispatch/?tag=swift-regrets)
34. 2021-08-20[Swift 遗憾：带标签的元组元素](https://belkadan.com/blog/2021/08/Swift-Regret-Labeled-Tuple-Elements/?tag=swift-regrets)
35. 2021-08-18[Swift 遗憾：元组与参数列表](https://belkadan.com/blog/2021/08/Swift-Regret-Tuples-and-Argument-Lists/?tag=swift-regrets)
36. 2021-08-13[Swift 遗憾：Sequence](https://belkadan.com/blog/2021/08/Swift-Regret-Sequence/?tag=swift-regrets)
37. 2021-08-11[Swift 遗憾：mutating 协议方法 vs. 类](https://belkadan.com/blog/2021/08/Swift-Regret-Mutating-Protocol-Methods/?tag=swift-regrets)
38. 2021-08-06[Swift 遗憾：NSUInteger](https://belkadan.com/blog/2021/08/Swift-Regret-NSUInteger/?tag=swift-regrets)
39. 2021-08-04[Swift 遗憾：协议语法](https://belkadan.com/blog/2021/08/Swift-Regret-Protocol-Syntax/?tag=swift-regrets)

### 可能相关的标签

- [编程语言](https://belkadan.com/blog/tags/programming-languages)
- [Swift](https://belkadan.com/blog/tags/swift)
