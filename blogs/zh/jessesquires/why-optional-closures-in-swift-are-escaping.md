---
title: 为什么 Swift 中的可选闭包是逃逸的
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2018/06/10/why-optional-swift-closures-are-escaping/'
original_language: en
published: 2018-06-10
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:47d3ce2975321f5c'
translated: true
---

> 原文：[Why optional closures in Swift are escaping](https://www.jessesquires.com/blog/2018/06/10/why-optional-swift-closures-are-escaping/)　·　Jesse Squires

在最近一期的[播客](https://spec.fm/podcasts/swift-unwrapped/144991)中，JP 和我讨论了 Swift 中闭包的隐式逃逸（implicit escaping）。随着 Swift 不断成熟和演进，函数中闭包参数的默认行为已经发生了变化。在 Swift 3 之前，闭包参数的默认行为是 _逃逸_。在 [SE-103](https://github.com/apple/swift-evolution/blob/master/proposals/0103-make-noescape-default.md) 之后，默认行为改为 _非逃逸_（non-escaping）。

在 Swift 3 中，要选择不使用默认行为，你可以用 `@noescape` 来注解函数参数。既然这已经是默认行为了，你需要指定 `@escaping` 来让闭包逃逸。Greg Heo 在 [Swift Unboxed](https://swiftunboxed.com/lang/closures-escaping-noescape-swift3/) 上提供了[很好的解释](https://swiftunboxed.com/lang/closures-escaping-noescape-swift3/)。

总之，我们的那期节目聚焦于 Swift 编译器中发现的一个新问题：从 Swift 桥接出来的非逃逸闭包（no-escape closure）在 Objective-C 中最终可能会逃逸。[Doug Gregor 在 Swift 论坛上详细解释了这个问题](https://forums.swift.org/t/implicit-escaping-of-closures-via-objective-c/12025)。在节目讨论过程中，还有另一个关于“逃逸闭包（escaping closure）”的情况，JP 和我都不太确定。

撇开所有这些规则和变化不谈，_可选_闭包参数不允许被注解，因为它们**始终是隐式逃逸的**。但为什么呢？

在 Twitter 上，[David Hart 解释道](https://twitter.com/dhartbit/status/998605843846311942)：

> 给可选闭包添加逃逸注解是没有意义的，因为它们不是函数类型：它们本质上是一个包含函数的 `enum`（Optional），就像你将闭包存储在任何其他类型中一样：它是隐式逃逸的，因为它被另一个类型持有。

我现在觉得这显而易见，但我之前确实不知道为什么可选闭包会被区别对待。可选类型（Optional）[只是一个包含两种 case 的枚举](https://github.com/apple/swift/blob/master/stdlib/public/core/Optional.swift#L122-L133)。就像任何其他拥有闭包的类型一样，该闭包根据定义就是逃逸的。因此，可选闭包与拥有闭包属性（property）的结构体没有太大区别：

```
typealias Handler = () -> Void

struct Closure {
    let handler: Handler
}
```

更重要的是，将非函数类型注解为 `@escaping` 是没有意义的。当然，我们自己验证这一点也很容易：

```
func performWorkOptional(handler: Handler?) {
    print(type(of: handler))
}

performWorkOptional { /* ... */ }

// 打印：Optional<() -> ()>
```

而对于非可选的情况：

```
func performWork(handler: @escaping Handler) {
    print(type(of: handler))
}

performWork { /* ... */ }

// 打印：() -> ()
```
