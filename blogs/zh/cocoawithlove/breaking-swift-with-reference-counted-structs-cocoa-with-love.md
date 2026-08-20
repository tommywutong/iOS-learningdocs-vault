---
title: 用引用计数的结构体打破 Swift | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/03/27/on-delete.html'
original_language: en
published: 2016-03-27
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:315e6b092b8fcc25'
translated: true
---

> 原文：[Breaking Swift with reference counted structs | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/03/27/on-delete.html)　·　Cocoa with Love (Matt Gallagher)

在 Swift 中，`class` 类型分配在堆上，使用引用计数（reference counting）来追踪其生命周期，并且可以在删除时执行清理行为。相比之下，`struct` 不会单独分配在堆上，不使用引用计数，也无法执行清理行为。

对吧？

实际上，“堆”、“引用计数”和“清理行为”这些特性也都可以适用于 `struct` 类型。但要注意：不符合其本性的行为很容易引发问题。我将展示 `struct` 如何最终拥有一些你可能认为属于 `class` 的特性，并说明这如何成为内存泄漏、异常行为和编译器崩溃的根源。

> **本文内容在 Swift 3 中已过时**：虽然在 Swift 3 中仍然可以让一个 `struct` 拥有分配在堆上、带引用计数和清理行为，但已无法像本文所述那样在 `struct` 方法中捕获对 `self` 的引用。本文第 2 节详细描述的问题已在 Swift 3 中修复，本文其余部分仅作为历史记录。别担心：结果对你来说是好事。

## 结构体中的类字段

虽然 `struct` 通常没有 `deinit` 行为，但 `struct` 类型的值（就像 Swift 中所有其他值一样）需要正确维护其内容的引用计数。`struct` 中的任何引用计数字段，在它们被添加到 `struct` 时、被移除时或 `struct` 被删除时，其引用计数都必须正确地递增和递减。

我们可以利用引用计数字段在 `struct` 超出作用域时被递减这一事实，为 `struct` 附加行为，就好像它有一个 `deinit` 方法一样。

为此，我们需要做的就是向 `struct` 添加一个类字段：

```swift
struct OrdinaryStruct {
   let classField: SomeClass
}
```

一个有效使用此效果的示例是将 `OnDelete` 字段附加到你的 `struct`。`OnDelete` 类在清理时运行一个自定义闭包（closure）：

```swift
public final class OnDelete {
   var block: () -> Void
   public init(_ @escaping c: () -> Void) {
      block = c
   }
   deinit {
      block()
   }
}
```

下面是一个名为 `DeletionLogger` 的示例 `struct`，它使用 `OnDelete` 类在其被删除时向标准输出写入内容：

```swift
struct DeletionLogger {
   let od = OnDelete { print("DeletionLogger deleted") }
}

do {
   let dl = DeletionLogger()
   print("Not deleted, yet")
   withExtendedLifetime(dl) {}
}
```

输出结果为：

```
Not deleted, yet
DeletionLogger deleted
```

## 尝试从闭包中访问结构体

到目前为止，没什么太奇怪的地方。`OnDelete` 对象可以在 `struct` 的清理时执行一个函数，有点像 `deinit` 方法。但是，尽管它看起来像是在模仿 `class` 的 `deinit` 行为，`OnDelete` 闭包却无法执行 `deinit` 方法能做的最重要的事情：操作 `struct` 的字段。

尽管有些明显的理由表明这是个坏主意，但我们还是尝试访问 `struct`，看看会出现什么问题。我们将使用一个包含 `Int` 值的简单 `struct`，并尝试在 `OnDelete` 闭包运行时输出该 `Int` 的值。

```swift
struct Counter {
   let count = 0
   let od = OnDelete { print("Counter value is \(count)") }
}
```

我们无法这样做（错误：`Instance member 'count' cannot be used on type 'SomeStruct'`）。不过这并不奇怪：即使是在 `class` 上，我们也不被允许这样做，因为你不能像这样从初始化方法中访问其他字段。

让我们正确初始化 `struct`，然后尝试捕获它的一个字段。

```swift
struct Counter {
   let count = 0
   var od: OnDelete? = nil
   init() {
      od = OnDelete { print("Counter value is \(self.count)") }
   }
}
```

> 这在 Swift 3 中已不再可能。它会阻止我们做这种相当愚蠢的事情，并显示错误信息：“Closure cannot implicitly capture a mutating self parameter”。

编译器在 Swift 2.2 中会抛出段错误（segmentation fault），在 Swift Development Snapshot 2016-03-24 中会引发致命错误（fatal error）。

太好了！我已经开始觉得有趣了。

当然，我可以通过这样做来避免所有编译器问题：

```swift
struct Counter {
   var count: Int
   let od: OnDelete
   init() {
      let c = 0
      count = c
      od = OnDelete { print("Counter value is \(c)") }
   }
}
```

或者使用不常见的捕获列表（capture list），在这种情况下是等价的：

```swift
struct Counter {
   var count = 0
   let od: OnDelete?
   init() {
      od = OnDelete { [count] in print("Counter value is \(count)") }
   }
}
```

但这两种方式实际上都不允许我们访问 `struct` 本身；这两种方式都捕获了 `count` 字段的一个不可变副本，但我们想要访问的是最新的可变 `count`。

```swift
struct Counter {
   var count = 0
   var od: OnDelete?
   init() {
      od = OnDelete { print("Counter value is \(self.count)") }
   }
}
```

> 和之前一样，这在 Swift 3 中已不再可能。

万岁！这样好多了。一切都是可变且共享的。我们捕获了 `count` 变量，并且没有发生编译器崩溃。

我们应该发布这段代码，因为它明显可行，不是吗？

## 完全循环

它显然不可行。如果我们像之前一样运行代码：

```swift
do {
   let c = Counter()
   print("Not deleted, yet")
   withExtendedLifetime(c) {}
}
```

我们得到的唯一输出是：

```
Not deleted, yet
```

`OnDelete` 闭包没有被调用。为什么？

查看 SIL（Swift 中间语言，由 `swiftc -emit-sil` 返回），很明显，在 `OnDelete` 闭包中捕获 `self` 阻止了 `self` 被优化到栈上。这意味着，`self` 变量不是使用 `alloc_stack` 分配，而是使用 `alloc_box` 分配的：

```
%1 = alloc_box $Counter, var, name "self", argno 1 // users: %2, %20, %22, %29
```

并且 `OnDelete` 闭包持有（retain）了这个 `alloc_box`。

为什么这是个问题？因为它形成了一个引用计数循环（reference counted loop）：

- 闭包持有 `Counter` 的装箱版本 → `Counter` 的装箱版本持有 `OnDelete` → `OnDelete` 持有闭包

这个循环创建后，我们的 `OnDelete` 对象永远不会被释放，也永远不会调用它的闭包。

## 我们能打破这个循环吗？

如果 `Counter` 是一个 `class`，我们会使用 `[weak self]` 闭包来捕获它，从而避免引用计数循环。但是，由于 `Counter` 是一个 `struct`，尝试这样做会导致错误。此路不通。

我们可以在构造之后，通过将 `od` 字段设置为 `nil` 来手动打破循环吗？

```swift
var c = Counter()
c.od = nil
```

不行。仍然不起作用。为什么？

当 `Counter.init` 函数返回时，它创建的 `alloc_box` 被复制到了栈上。这意味着 `OnDelete` 持有的版本与我们能访问的这个版本是不同的。`OnDelete` 持有的那个版本现在变得不可访问。

我们创建了一个**无法打破**的循环。

正如 [Joe Groff 在 Twitter 的这个讨论串中强调的](https://twitter.com/jckarter/status/715171466283646977)，Swift 演进提案 [SE-0035](https://github.com/apple/swift-evolution/blob/master/proposals/0035-limit-inout-capture.md) 应通过限制 `inout` 的捕获（`Counter.init` 方法中使用的那种捕获）为 `@noescape` 闭包（这将会阻止被 `OnDelete` 的逃逸闭包捕获）来防止这个问题。

所以问题在于，`Counter.init` 方法返回的 `self` 副本与我们在该方法期间捕获的版本不同。我们需要让返回的版本和持有的版本相同。

让我们避免在 `init` 方法中做任何事情，而是在 `static` 函数中设置。

```swift
struct Counter {
   var count = 0
   var od: OnDelete? = nil
   static func construct() -> Counter {
      var c = Counter()
      c.od = OnDelete{
         print("Value loop break is \(c.count)")
      }
      return c
   }
}

do {
   var c = Counter.construct()
   c.count += 1
   c.od = nil
}
```

不行：我们仍然有同样的问题。我们有一个永久嵌入在 `OnDelete` 中的 `Counter` 捕获版本，它与返回的版本不同。

让我们修改那个 `static` 方法……

```swift
struct Counter {
   var count = 0
   var od: OnDelete? = nil
   static func construct() -> () -> () {
      var c = Counter()
      c.od = OnDelete{
         print("Value loop break is \(c.count)")
      }
      return {
         c.count += 1
         c.od = nil
      }
   }
}

do {
   var loopBreaker = Counter.construct()
   loopBreaker()
}
```

输出现在是：

```
Counter value is 1
```

这终于可行了，我们可以看到 `loopBreaker` 闭包中的状态（state）变化正确地影响了 `OnDelete` 闭包中打印的结果。

既然我们不再返回 `Counter` 实例，也就停止了创建它的单独副本。现在只有一个 `Counter` 实例的副本，那就是由两个闭包共享的 `alloc_box` 版本。我们在堆上有了一个带引用计数的 `struct`，以及一个可以在清理时访问 `struct` 字段的 `OnDelete` 方法。

## 一些思考

这段代码在技术上“可行”，但结果是一团糟。我们有一个需要手动打破的引用计数循环，只能通过 `construct` 函数中设置的闭包来访问 `Counter` 类型，并且对于一个底层实例，我们现在有了四个堆分配（`OnDelete` 中的闭包、`OnDelete` 对象本身、`c` 变量的装箱分配以及 `loopBreaker` 闭包）。

如果你到现在还没意识到……这一切都是在浪费大量时间。

我们一开始就可以把 `Counter` 做成一个 `class`，将堆分配的数量保持在 1。

```swift
class Counter {
   var count = 0
   deinit {
      print("Counter value is \(count)")
   }
}
```

长话短说：如果你需要从不同的作用域访问相同的可变数据，`struct` 可能不是一个好选择。

## 结论

闭包捕获是我们经常直接编写并假设编译器会完成必要工作的东西。然而，捕获可变值有一些微妙的语义差异，可能需要理解以避免出现问题。由于我们仍在等待 Swift 3 修复的一些小设计问题，情况变得复杂。

请记住，当捕获带有 `class` 字段的 `struct` 值时，要考虑引用计数循环的可能性。你不能弱捕获一个 `struct`，所以如果发生了引用计数循环，你需要通过其他方式打破循环。

无论如何，本文大部分内容都在探讨一个完全愚蠢的想法：试图让一个 `struct` 捕获自身。不要这样做。捕获，像其他引用计数结构一样，应该是一个**无环**的图。如果你发现自己试图创建循环，很可能是因为你应该使用 `class` 类型，并配合从子节点到父节点的 `weak` 引用。

最后，有一些**好的**理由去使用 `OnDelete` 类，但不要开始认为它像 `deinit` 方法一样工作——它主要用于副作用（即它所附加作用域之外的状态）。
