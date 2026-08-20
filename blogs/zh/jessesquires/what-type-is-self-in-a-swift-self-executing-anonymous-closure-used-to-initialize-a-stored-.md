---
title: 在 Swift 中，用于初始化存储属性的自执行匿名闭包里的 self 是什么类型？
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/12/22/swift-self-executing-anonymous-closures/'
original_language: en
published: 2020-12-22
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ab31bfd6058b1bcb'
translated: true
---

> 原文：[What type is self in a Swift self-executing anonymous closure used to initialize a stored property?](https://www.jessesquires.com/blog/2020/12/22/swift-self-executing-anonymous-closures/)　·　Jesse Squires

在 JavaScript 中，这种[模式称为](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)立即调用函数表达式（Immediately Invoked Function Expression，IIFE）或自执行匿名函数（Self-Executing Anonymous Function）。Swift 对此没有“官方”名称，但 IIFE、以及“立即执行的匿名闭包”或“自执行匿名闭包”同样适用。（感谢 Twitter 上的朋友帮忙确认。）

大多数 Swift 开发者都见过并用过这种常见的方法来初始化类型的属性：

```
class MyClass {

    let dateFormatter: DateFormatter = {
        let df = DateFormatter()
        df.timeStyle = .medium
        df.dateStyle = .long
        return df
    }()

    // 其他成员在此……
}
```

这是一种方便且简洁的模式，有助于组织代码。在使用 UIKit 和定义自定义视图时，这种方法尤其受欢迎。它简化了类型的初始化方法，并且通常易于阅读。最近，我在使用这种方法时发现了一个代码中的错误、一些非常意外的 Swift 行为，以及 _可能_ 是 Swift 的一个错误。

我正在构建一个典型的表格视图，其中包含的单元格有一个按钮子视图。点击整个单元格和点击单元格内的按钮会执行不同的操作。你可能以前也构建过类似的东西。以下是简化的示例代码：

```
class MyTableCell: UITableViewCell {

    let button: UIButton = {
        let button = UIButton()
        button.setTitle("Title", for: .normal)
        button.addTarget(self, action: #selector(didTapButton(_:)), for: .touchUpInside)
        return button
    }()

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        self.contentView.addSubview(self.button)
        // 添加约束、其他设置等……
    }

    @objc
    func didTapButton(_ sender: UIButton) {
        // 执行某些操作
    }
}
```

我正在构建这样一个常规、平凡的功能，以至于我在运行和测试之前就完成了大部分代码。这样的代码我写过数千次。所以，你可以想象当我发现单元格内的按钮没有触发动作时有多惊讶。点击按钮毫无反应，但其他一切似乎都按预期工作。上面的代码有个错误。你能找到它吗？我一行一行地检查，试图找到我遗漏了什么。我出于习惯忽略了什么？

问题出在调用 `addTarget(_:, action:, for:)` 上。把这行代码移到初始化方法中就解决了问题，一切按预期工作。

```
override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
    super.init(style: style, reuseIdentifier: reuseIdentifier)
    self.contentView.addSubview(self.button)

    // 修复：在此处添加 target/action
    self.button.addTarget(self, action: #selector(didTapButton(_:)), for: .touchUpInside)

    // 添加约束、其他设置等……
}
```

在发现 _是什么_ 问题之后，现在是时候问 _为什么_ 了。我最初的直觉如下：

1. `button` 是一个存储型常量属性，通过自执行匿名闭包立即初始化
2. Swift 的初始化规则意味着存储型属性（像这样有值的）_必须_ 在拥有它们的类型 _之前_ 初始化
3. 因此，在 `button` 初始化时（闭包执行时），`self` 必须是 `nil`
4. 方法 `addTarget(_:, action:, for:)` 接受 `Any?` 作为 `target` 参数，所以传递 `nil` 没问题
5. 结论：`self` 一直以来都是 `nil`！真是愚蠢的错误！

然而，情况并非如此。具体来说，`self` **并不是** `nil`。不仅如此，`self` 还不是我期望的那个 `self`。看看这段代码片段，你能确定 `self` 是什么类型以及为什么吗？

```
class MyTableCell: UITableViewCell {

    let button: UIButton = {
        let button = UIButton()
        button.setTitle("Title", for: .normal)

        // self 是什么？
        button.addTarget(self, action: #selector(didTapButton(_:)), for: .touchUpInside)

        return button
    }()
}
```

我在调试器中暂停了执行，检查 `po self` 是否打印 `nil`。结果它打印了 `(Function)`。在 Swift 中，[闭包是一等引用类型](https://docs.swift.org/swift-book/LanguageGuide/Closures.html)。因此，我得出结论，`self` 指的是 **这个闭包**，其类型是 `() -> UIButton`。对吗？实际上……不对。

继续调查，我打印了 `type(of: self)`，它返回了 `(MyTableCell) -> () -> MyTableCell`。什么？！这是一个接收 `MyTableCell` 实例并返回一个类型为 `() -> MyTableCell` 的闭包的闭包，后者不接受任何参数并返回一个 `MyTableCell`。我不明白为什么会这样。

我认为大多数开发者会和我有同样的直觉，认为这里的 `self` 指的是 `MyTableCell`，因为在其他看起来类似于此的模式中确实如此，比如[计算属性](https://docs.swift.org/swift-book/LanguageGuide/Properties.html#ID259)（computed properties）。尽管如此，一旦意识到 `self` 是一个函数，我认为大多数开发者也会直觉认为它的类型 **必须** 是 `() -> UIButton`。

这引发了一些有趣的问题。

首先，我意识到由 [SE-0022](https://github.com/apple/swift-evolution/blob/main/proposals/0022-objc-selectors.md) 引入的 `#selector` 构造能力有限。正如提案的[“考虑过的替代方案”](https://github.com/apple/swift-evolution/blob/main/proposals/0022-objc-selectors.md#alternatives-considered)部分所述，`#selector` **不是**类型安全的。然而，_它确实_ 能够判断一个选择器（selector）是否在作用域内。如果你试图传递另一个类的选择器，编译器会提供警告。例如，考虑以下代码：

```
class OuterClass {
    func button() -> UIButton {
        let button = UIButton()
        button.addTarget(self, action: #selector(didTapButton(_:)), for: .touchUpInside)
        return button
    }

    class InnerClass {
        @objc
        func didTapButton(_ sender: UIButton) {
            // 执行某些操作
        }
    }
}
```

这会生成预期的错误：`Cannot find 'didTapButton' in scope`。我不清楚这与 `MyTableCell` 示例在选择器作用域方面有何不同。如果 `self` **不是** `MyTableCell` 的实例，那么 `didTapButton(_:)` 如何对 `self` 来说是在作用域内的？这是 `#selector` 的问题吗？

##### [更新](#updated-23-december-2020)  _2020 年 12 月 23 日_

这并不完全准确。你 _可以_ 写成 `#selector(InnerClass.didTapButton(_:))`，这会成功编译，并且符合 [SE-0022](https://github.com/apple/swift-evolution/blob/main/proposals/0022-objc-selectors.md)。

其次，为什么 `self` 是一个 `(MyTableCell) -> () -> MyTableCell` 的实例，而 **不是** `() -> UIButton`？这是 Swift 中的错误吗？

我希望有人能回答这两个问题并解释发生了什么。如果是这样，我会更新这篇文章！

无论如何，在为存储属性使用自执行匿名闭包时，应该避免（或完全杜绝）引用 `self`！那个 `self` 可能不是你期望的 `self`。小心你自己。

##### [更新](#updated-22-december-2020)  _2020 年 12 月 22 日_

如果你将 `button` 声明为 `lazy var` 而不是 `let`，那么就会出现预期的行为。也就是说，在自执行匿名闭包中 `self` 是 `MyTableCell` 的实例，并且对 `addTarget(_:, action:, for:)` 的调用有效。（感谢 [@Geri_Borbas](https://twitter.com/Geri_Borbas/status/1341594268293586944)。）同样值得注意的是，在这种情况下，`MyTableCell` 的初始化方法会在 `button` 闭包执行 **之前** 被调用。然而，这使得情况更加令人困惑——使用 `let` 与使用 `lazy var` 产生了显著不同的行为，这完全不直观。

~~类型 `(MyTableCell) -> () -> MyTableCell` 似乎指向 `MyTableCell` 的初始化方法。（感谢 [@eneko](https://twitter.com/eneko/status/1341605571984642048)。）~~ 不，并非如此。

##### [更新](#updated-23-december-2020)  _2020 年 12 月 23 日_

感谢 [@elliottwil](https://twitter.com/elliottwil/status/1341632285200683009) 和 [Noah Gilmore](https://twitter.com/noahsark769/status/1341635028657180672) 揭示并调查了这里真正的根本问题。（[Nerd sniped](https://xkcd.com/356/)。😄）`self` 的类型解析为 `(MyTableCell) -> () -> MyTableCell` 是不幸的后果，原因是 `NSObject` 的实例方法 [`-[NSObject self]`](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418954-self?language=objc) 和 Swift 的[柯里化函数](https://oleb.net/blog/2014/07/swift-instance-methods-curried-functions/)。（请注意，[SE-0002](https://github.com/apple/swift-evolution/blob/main/proposals/0002-remove-currying.md) 移除了柯里化 `func` 声明语法，但未改变方法的语义。）

更新继续如下。

这里有多个层次的混淆。让我们逐一揭开。首先，让我们回顾一下有问题的代码：

```
class MyTableCell: UITableViewCell {
    let button: UIButton = {
        let button = UIButton()

        // self 是什么？
        button.addTarget(self, action: #selector(didTapButton(_:)), for: .touchUpInside)

        print(type(of: self)) // (MyTableCell) -> () -> MyTableCell

        return button
    }()
}
```

我们知道 `self` 的类型是 `(MyTableCell) -> () -> MyTableCell`，这是由于 `-[NSObject self]` 实例方法。并且这满足了对 `target` 参数 `Any?` 的（缺乏）类型约束。这回答了这个问题：为什么 `self` 是 `(MyTableCell) -> () -> MyTableCell` 的实例，而 **不是** `() -> UIButton`？我们可以通过打印到控制台来验证：

```
print(type(of: NSObject.`self`)) // prints (NSObject) -> () -> NSObject
```

请注意，`NSObject.self`（不带反引号）指的是[元类型](https://docs.swift.org/swift-book/ReferenceManual/Types.html#ID455) `NSObject`，**不是**[实例方法](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418954-self?language=objc) `-(instancetype)self`。因此，表达式 `type(of: NSObject.self)` 返回 `NSObject.Type`。因为 `self` 是一个保留关键字，我们必须用反引号括起来才能引用正确的“self”。（如果你曾尝试定义一个名为“default”的 `enum` case，你可能见过这种情况。）

我们可以在代码中明确这一点：

```
class MyTableCell: UITableViewCell {
    let button: UIButton = {
        let button = UIButton()

        // 使用 `self`
        button.addTarget(`self`, action: #selector(didTapButton(_:)), for: .touchUpInside)

        print(type(of: `self`)) // (MyTableCell) -> () -> MyTableCell

        return button
    }()
}
```

然后我们可以使其更加明确：

```
// Xcode 的文档弹出窗口正确地引用了声明 let `self`: MyTableCell
print(type(of: MyTableCell.`self`)) // let `self`: MyTableCell
```

通过这个改动，我们可以看到这显然是错误的。此外，Xcode 会根据地是否有反引号对“self”进行不同的语法高亮。

接下来，现在很明显了，这只发生在继承自 `NSObject` 的类中。因为我使用的是 `UITableViewCell`，所以起初我并没有考虑到这一点。例如，以下代码会产生错误：

```
class MyClass {
    let str: String = {
        print(self) // <-- Cannot find 'self' in scope
        return "String"
    }()
}
```

现在我们可以尝试回答我剩下的两个问题。

这是 `#selector` 的问题吗？不。这是 [SE-0022](https://github.com/apple/swift-evolution/blob/main/proposals/0022-objc-selectors.md) 中描述的 `#selector` 的预期行为。我们可以写成 `#selector(Self.didTapButton(_:))`，这等价于 `#selector(MyTableCell.didTapButton(_:))`。`#selector` 表达式无法针对 `target` 参数检查自身。

这是 Swift 中的错误吗？依我看来，**是的**。我认为正确的行为应该是：**不带**反引号使用 `self` 始终引用封闭类型（就像使用 `lazy var` 时发生的那样），而 **带**反引号使用 ``self`` 则引用 `-[NSObject self]`（你几乎从不想用这个）。Xcode 正确地对这两者进行语法高亮的事实表明，正确信息存在于某处。

```
class MyTableCell: UITableViewCell {
    let button: UIButton = {

        print(type(of: self)) // Bug: should be MyTableCell. Instead, same as `self` below.

        print(type(of: `self`)) // (MyTableCell) -> () -> MyTableCell

        return UIButton()
    }()
}
```

换句话说，在这个上下文中，这两个表达式是不同的：

```
// 引用 MyTableCell 的实例
self

// 引用 func `self`() -> Self
MyTableCell.`self`
```

然而，Swift 编译器将它们都当作 `func `self`() -> Self` 处理。

但是，还有最后一个问题。将表达式 `self`（不带反引号）纠正为引用封闭类型会引入另一个有趣的问题：初始化期间的操作顺序应该是什么？当使用 `let` 时，属性在封闭类型 **之前** 初始化。当使用 `lazy var` 时，属性在封闭类型 **之后** 初始化。我不是编译器专家，所以我不打算回答哪个更好。但如果不能在编译器中更改初始化顺序来修复此问题，那么我认为预期的行为是产生与非 `NSObject` 类相同的错误：“Cannot find 'self' in scope”。

##### [更新](#updated-24-december-2020)  _2020 年 12 月 24 日_

此错误在 [SR-4559](https://bugs.swift.org/browse/SR-4559) 和 [SR-4865](https://bugs.swift.org/browse/SR-4865)（重复）中被追踪。感谢 [Nolan Waite](https://bugs.swift.org/secure/ViewProfile.jspa?name=nolanw) 的分享。

##### [更新](#updated-05-november-2021)  _2021 年 11 月 05 日_

自 2021 年 9 月起，[SR-4559](https://bugs.swift.org/browse/SR-4559) 已被标记为已解决。[拉取请求在这里](https://github.com/apple/swift/pull/37992)，根据描述，修复方法是发出一个警告，指示 `self` 引用可能不是你意图中的那个。

该修复尚未包含在 Xcode 13.1 (13A1030d) 或 Xcode 13.2 beta (13C5066c) 中。不过，[最新版本的 SwiftLint](https://github.com/realm/SwiftLint/releases/tag/0.45.0) 包含[一个新规则](https://realm.github.io/SwiftLint/self_in_property_initialization.html)（`self_in_property_initialization`），用于针对此确切问题发出警告。

##### [更新](#updated-02-march-2022)  _2022 年 03 月 02 日_

好消息！从包含 Swift 5.6 的 [Xcode 13.3 beta](https://developer.apple.com/documentation/xcode-release-notes/xcode-13_3-release-notes) 开始，编译器现在会针对此问题发出警告。
