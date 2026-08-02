---
title: Swift 协议的默认实现
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/swift-default-protocol-implementations/'
original_language: en
published: 2014-09-02
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:e3bee09813aad3dc'
translated: true
---

> 原文：[Swift Default Protocol Implementations](https://nshipster.com/swift-default-protocol-implementations/)　·　NSHipster (Mattt)

# [Swift 协议的默认实现](https://nshipster.com/swift-default-protocol-implementations/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2014 年 9 月 2 日

Swift 在三个月前的今天发布。对我们许多人来说，这是职业生涯中最震撼、最令人兴奋的事件之一。在这几个月里，我们对这门语言的共同理解和欣赏显然已经有了显著演变。

最初是迷恋期。我们盯着外表和表层特性，例如 Unicode 支持（`let 🐶🐮`！）以及崭新、精简的语法。说真的，甚至连它的*名字*都客观上比前任更好。

不过几周后，当我们有机会把 Swift 手册读过几遍，便开始理解这门多范式语言的完整含义。那些为了显得更聪明而摆出函数式编程狂热姿态的人（泛型！），已经学到足以名副其实的东西。我们终于弄清了 `class` 和 `struct` 的区别，也顺便掌握了一些技巧，例如[自定义运算符](https://nshipster.com/swift-operators/)和[字面量可转换类型](https://nshipster.com/swift-literal-convertible/)。最初的兴奋现在可以被有效地投入 App、库和教程。

下周的发布实际上标志着 iOS 与 OS X 开发者夏天的结束。该收束实验、重新开始交付产品了。

不过，真正忙起来前还有几天。再学几件事吧：

---

泛型是 Swift 的决定性特性。它与强大的类型系统协同工作，让开发者能写出比 Objective-C 时代更安全、性能更好的代码。

泛型的底层机制是协议。Swift 协议与 Objective-C 的 [`@protocol`](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithProtocols/WorkingwithProtocols.html)一样，声明遵守它所需实现的方法和属性。

> 在面向对象范式中，类型常常与类身份混为一谈。**但在 Swift 编程时，应先通过*协议*来理解多态，最后才诉诸继承。**

无论在 Swift 还是 Objective-C 中，协议的一个主要不足是没有内建方式为方法提供默认实现；而在其他语言中，这可以通过 [mixin](https://en.wikipedia.org/wiki/Mixin) 或 [trait](https://en.wikipedia.org/wiki/Trait_%28computer_programming%29) 实现。

……但故事并未结束。Swift 的[面向方面](https://en.wikipedia.org/wiki/Aspect-oriented_programming)特征比它起初显露出来的要多不少。

以标准库中广泛使用的 `Equatable` 协议为例：

```
protocol Equatable {
    static func ==(lhs: Self, rhs: Self) -> Bool
}
```

对于包含 `title` 和 `body` 字段的 `Article` `struct`，实现 `Equatable` 很直接：

```
struct Article {
    let title: String
    let body: String
}

extension Article: Equatable {}

func ==(lhs: Article, rhs: Article) -> Bool {
    return lhs.title == rhs.title && lhs.body == rhs.body
}
```

准备就绪后，看看 `Equatable` 的实际效果：

```
let title = "Swift Custom Operators: Syntactic Sugar or Menace to Society?"
let body = "..."

let a = Article(title: title, body: body)
let b = Article(title: title, body: body)

a == b // true
a != b // false
```

等等……`!=` 从哪里来的？

`Equatable` 协议并未定义 `!=`，`Article` 当然也没有实现它。那发生了什么？

`!=` 实际使用的是标准库中的这个函数实现：

```
func !=<T : Equatable>(lhs: T, rhs: T) -> Bool
```

因为 `!=` 被实现为面向 `Equatable` 的泛型函数，所有遵守 `Equatable` 的类型，包括 `Article`，都会自动获得 `!=` 运算符。

如果确有需要，我们可以覆写 `!=` 的实现：

```
func !=(lhs: Article, rhs: Article) -> Bool {
    return !(lhs == rhs)
}
```

就相等性而言，几乎不可能提供比取给定 `==` 检查的否定更高效的实现；但在其他情形下，这样做也许有意义。Swift 的类型推断系统允许更具体的声明优先于任何泛型或隐式候选。

标准库到处都在使用泛型运算符，例如位运算：

```
protocol BitwiseOperationsType {
    func &(_: Self, _: Self) -> Self
    func |(_: Self, _: Self) -> Self
    func ^(_: Self, _: Self) -> Self
    prefix func ~(_: Self) -> Self

    class var allZeros: Self { get }
}
```

用这种方式实现功能，能显著减少在既有基础设施上构建功能所需的样板代码。

## 方法的默认实现

不过，前述技巧实际上只适用于运算符。要为协议方法提供默认实现就没那么方便了。

考虑一个带有方法 `m()`、接受单个 `Int` 参数的协议 `P`：

```
protocol P {
    func m(arg: Int)
}
```

最接近默认实现的做法，是提供一个把显式 `self` 作为第一个参数的顶层泛型函数：

```
protocol P {
    func m() /* {
        f(self)
    }*/
}

func f<T: P>(_ arg: T) {
    …
}
```

> 协议中的注释代码有助于向使用者说明所提供的函数式实现。

---

这一切凸显了 Swift 中方法与函数之间的重要张力。

面向对象范式以封装状态和行为的对象为基础。然而在 Swift 中，某些泛型函数根本无法实现为 `struct` 或 `class` 自身的方法。

以 `contains` 方法为例：

```
func contains<S : SequenceType where S.Generator.Element : Equatable>(seq: S, x: S.Generator.Element) -> Bool
```

由于序列生成器元素必须是 `Equatable` 的约束，不能在泛型容器上声明该方法，否则就会要求集合中的元素都遵守 `Equatable`。

将 `contains`、`advance` 或 `partition` 这类行为放到顶层函数，会损害标准库的体验。它不仅让方法自动补全隐藏了功能，也使 API 分散在面向对象与函数式范式之间。

这不太可能赶在 1.0 前解决（而且肯定有更紧急的事），但可以通过几种方式处理：

- 提供 mixin 或 trait 功能来扩展协议，使协议能够提供默认实现。
- 允许带有泛型参数的扩展，让类似 `extension Array<T: Equatable>` 的写法可以定义额外方法，例如只对符合特定条件的关联类型可用的 `func contains(x: T)`。
- 自动将第一个参数为 `Self` 的函数调用桥接为可通过隐式 `self` 调用的方法。
