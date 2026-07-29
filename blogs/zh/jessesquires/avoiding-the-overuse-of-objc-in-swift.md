---
title: '避免在 Swift 中过度使用 @objc'
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2016/06/04/avoiding-objc-in-swift/'
original_language: en
published: 2016-06-04
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f85b9444e74a12b2'
translated: true
---

> 原文：[Avoiding the overuse of @objc in Swift](https://www.jessesquires.com/blog/2016/06/04/avoiding-objc-in-swift/)　·　Jesse Squires

几天前，我（终于！）在将一个项目更新到 Swift 2.2，并在改用提案 [SE-0022](https://github.com/apple/swift-evolution/blob/master/proposals/0022-objc-selectors.md) 引入的新 `#selector` 语法时遇到了几个问题。如果在协议扩展（protocol extension）中使用 `#selector`，则该协议必须声明为 `@objc`。而以前的 `Selector("method:")` 语法没有这个要求。

### 使用协议扩展配置视图控制器

为了写这篇帖子，我从正在开发的项目中简化了代码，但所有的核心思想都保持不变。我在 Swift 中经常使用的一个模式是，为可重用的配置编写协议和扩展，尤其是在 UIKit 中。

假设我们有一组视图控制器，它们都需要一个视图模型（view model）和一个“取消”按钮。每个控制器都需要在点击“取消”时能够执行自己的代码。我们可能会写出这样的代码：

```
struct ViewModel {
    let title: String
}

protocol ViewControllerType: class {
    var viewModel: ViewModel { get set }

    func didTapCancelButton(sender: UIBarButtonItem)
}
```

如果只写到这里，那么每个控制器都必须自己添加取消按钮并完成连接。这会产生大量样板代码。我们可以通过一个扩展（extension）来改善这一点（这里使用旧的 `Selector("")` 语法）：

```
extension ViewControllerType where Self: UIViewController {
    func configureNavigationItem() {
        navigationItem.leftBarButtonItem = UIBarButtonItem(
            barButtonSystemItem: .Cancel,
            target: self,
            action: Selector("didTapCancelButton:"))
    }
}
```

现在，每个遵守该协议的控制器都可以在 `viewDidLoad()` 里调用 `configureNavigationItem()`，这要好得多。我们的控制器可能看起来像这样：

```
class MyViewController: UIViewController, ViewControllerType {
    var viewModel = ViewModel(title: "Title")

    override func viewDidLoad() {
        super.viewDidLoad()
        configureNavigationItem()
    }

    func didTapCancelButton(sender: UIBarButtonItem) {
        // 处理点击事件
    }
}
```

这个例子相当简单，但你可以想象我们可以使用这种策略来应用更复杂的配置。

将上面的代码片段（snippet）更新到 Swift 2.2 后，我们得到了以下代码：

```
extension ViewControllerType where Self: UIViewController {
    func configureNavigationItem() {
        navigationItem.leftBarButtonItem = UIBarButtonItem(
            barButtonSystemItem: .Cancel,
            target: self,
            action: #selector(didTapCancelButton(_:)))
    }
}
```

现在我们遇到了一个问题，一个新的编译器错误。

```
Argument of '#selector' refers to a method that is not exposed to Objective-C.

Fix-it   Add '@objc' to expose this method to Objective-C
```

### 当 `@objc` 试图毁掉一切时

由于种种原因，我们不能简单地将 `@objc` 添加到原始 `ViewControllerType` 协议中的这个方法上。一旦我们这么做，整个协议都需要标记为 `@objc`，这意味着：

- 该协议所继承的任何协议都需要标记为 `@objc`。
- 任何 _继承自该协议_ 的协议现在都会自动成为 `@objc`。
- 我们在协议中使用了结构体（`ViewModel`），而结构体无法在 Objective-C 中表达。

在此之前，这个代码库中仅有的几处 `@objc` 都被限定在普通的 target-action 选择器（selector）上。我们可能还没有在编写 _纯 Swift^TM_ 应用，因为它的底层仍然是 [Cocoa](http://inessential.com/2016/05/25/oldie_complains_about_the_old_old_ways)，但我们仍然可以利用 Swift 的许多强大特性——除非我们在太多地方开始引入 `@objc`。

这里的例子很简单，但想象一个更复杂的对象图，它大量使用了 Swift 的值类型（value types），并且有一个包含三个协议的层次结构，而这个协议正好处在中间。按照 fix-it 的建议引入 `@objc` 将会在我们的 App 中 _造成全面的破坏_。如果我们放任不管，`@objc` 的暴政将从我们的 Swift 代码中驱逐所有美感，让一切变得面目可憎。它会毁掉一切。

但希望还是有的。

### 阻止 `@objc` 让一切变得糟糕

我们不必让 `@objc` 在我们的代码库中蔓延，把我们的 Swift 代码变成仅仅是“换了新语法的 Objective-C”。

这个协议是可以拆解的——把所有 `@objc` 代码分离到它自己的协议中，然后通过协议组合（protocol composition）将它们重新合并起来。实际上，我们完全可以让编译器满意，同时避免改动 _任何_ 视图控制器的代码。

我们将协议拆分成两个：`ViewModelConfigurable` 和 `NavigationItemConfigurable`。我们之前对 `ViewControllerType` 的扩展可以转而移入 `NavigationItemConfigurable`。

```
protocol ViewModelConfigurable {
    var viewModel: ViewModel { get set }
}

@objc protocol NavigationItemConfigurable: class {
    func didTapCancelButton(_ sender: UIBarButtonItem)
}

extension NavigationItemConfigurable where Self: UIViewController {
    func configureNavigationItem() {
        navigationItem.leftBarButtonItem = UIBarButtonItem(
            barButtonSystemItem: .cancel,
            target: self,
            action: #selector(didTapCancelButton(_:)))
    }
}
```

最后，我们可以将原始的 `ViewControllerType` 协议定义为一个 `typealias`。

```
typealias ViewControllerType = ViewModelConfigurable & NavigationItemConfigurable
```

现在，一切都能像迁移到 Swift 2.2 之前一样正常工作，而我们上面定义的原始视图控制器也无需改动。没有任何东西被破坏。如果你也遇到过类似的情况，或者你通常想要收束 `@objc` 的使用范围（_这本就是你该做的_），那么我强烈推荐采用这个策略。

### 答案并非总是显而易见

现在回过头看，我觉得“废话”，这当然是解决问题的最佳且“最 Swift”的方式。然而，当 Xcode 突然开始朝你大喊大叫，快速应用 fix-it 又让 _其他一切_ 开始崩溃时，这样的解决方案并不总是能立刻想到——尤其迁移 Swift 版本时，Xcode 提供的 fix-it 通常都是对的。

最后，在做出这个改变后，我意识到这实际上是一个普遍适用、也更好的解决方案。从一开始就没有理由把它做成一个单一协议。`ViewModelConfigurable` 和 `NavigationItemConfigurable` 协议拥有各自不同的职责。协议组合自始至终都是最优雅、最合适的设计。
