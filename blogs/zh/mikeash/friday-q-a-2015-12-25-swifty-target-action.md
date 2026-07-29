---
title: 'Friday Q&A 2015-12-25: Swifty 版 Target/Action'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-12-25-swifty-targetaction.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2cbb7a7be784c112'
translated: true
---

> 原文：[Friday Q&A 2015-12-25: Swifty Target/Action](https://www.mikeash.com/pyblog/friday-qa-2015-12-25-swifty-targetaction.html)　·　mikeash.com Friday Q&A

发布于 2015-12-25 15:11 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2016-01-29: Swift 结构体存储](https://www.mikeash.com/pyblog/friday-qa-2016-01-29-swift-struct-storage.html)  
上一篇：[Friday Q&A 2015-12-11: Swift 弱引用](https://www.mikeash.com/pyblog/friday-qa-2015-12-11-swift-weak-references.html)  
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2015-12-25: Swifty 版 Target/Action

作者：[Mike Ash](https://www.mikeash.com/)

**概述**  
target/action 系统非常适合菜单项这类东西，因为它们可能会根据上下文命令许多不同的对象。例如，粘贴菜单项会连接到响应者链中恰好实现了 `paste:` 方法的那个对象。

但当你需要在代码中设置 target 和 action，而目标对象始终只有一个时，它的表现就不那么好了——这常见于按钮、文本字段（text field）以及其他类似的控制（control）。这最终成了一种[字符串类型](http://c2.com/cgi/wiki?StringlyTyped)编程的练习，而且往往容易出错。它还会迫使你把 action 单独实现，即使它很简单并且很自然地适合内联。

实现一个接受函数作为其 action 的纯 Swift 控制很简单，但对于实际代码，我们仍然需要与 Cocoa 打交道。目标是调整 `NSControl`，使其允许将函数设置为 target，同时仍能与 target/action 系统共存。

`NSControl` 没有任何合适的钩子来拦截 action 的发送，因此我们将转而利用现有的 target/action 机制。这需要一个适配器对象来充当 target。当它收到 action 时，会接着调用传递给它的函数。

**首次尝试**  
让我们开始写一些代码。下面是一个适配器对象，它持有一个函数，并在其 action 方法被调用时调用该函数：

```
    class ActionTrampoline: NSObject {
        var action: NSControl -> Void

        init(action: NSControl -> Void) {
            self.action = action
        }

        @objc func action(sender: NSControl) {
            action(sender)
        }
    }
```

下面是对 `NSControl` 的一个扩展，它封装了 trampoline 的创建并将其设置为 target：

```
    extension NSControl {
        @nonobjc func setAction(action: NSControl -> Void) {
            let trampoline = ActionTrampoline(action: action)
            self.target = trampoline
            self.action = "action:"
        }
    }
```

（`@nonobjc` 注解允许它与 `NSControl` 上的 Objective-C `action` 属性共存。如果没有它，这个方法就需要一个不同的名称。）

让我们试试看：

```
    let button = NSButton()
    button.setAction({ print("Action from \($0)") })
    button.sendAction(button.action, to: button.target)
```

哎呀，什么都没发生。

**延长 Trampoline 的生命周期**  
第一次尝试没有成功，因为 `target` 是一个弱属性（weak property）。不存在对 `trampoline` 的强引用（strong reference）来让它保持存活，因此它会被立即释放。随后对 `sendAction` 的调用将 action 发送给了 `nil`，所以没有任何效果。

我们需要延长 trampoline 的生命周期。我们可以把它返回给调用者，并要求它们在某个地方保留它，但这会很不方便。更好的方法是将 trampoline 的生命周期与控制的生命周期绑定。我们可以使用关联对象（associated objects）来实现这一点。

首先，我们定义一个键来用于关联对象 API。这比在 Objective-C 中稍微不方便一些，因为 Swift 对获取变量的地址不是很友好，而且实际上并不能保证使用 `&` 作用于变量所产生的指针是一致的。这段代码没有尝试使用全局变量的地址，而是简单地分配了一点内存并使用该地址：

```
    let NSControlActionFunctionAssociatedObjectKey = UnsafeMutablePointer<Int8>.alloc(1)
```

然后，`NSControl` 扩展使用 `objc_setAssociatedObject` 将 `trampoline` 附加到控制上。虽然这个值从未被取回，但仅仅是设置它就足以确保只要控制存活，该 trampoline 就保持存活：

```
    extension NSControl {
        @nonobjc func setAction(action: NSControl -> Void) {
            let trampoline = ActionTrampoline(action: action)
            self.target = trampoline
            self.action = "action:"

            objc_setAssociatedObject(self, NSControlActionFunctionAssociatedObjectKey, trampoline, .OBJC_ASSOCIATION_RETAIN)
        }
    }
```

让我们再试一次：

```
    let button = NSButton()
    button.setAction({ print("Action from \($0)") })
    button.sendAction(button.action, to: button.target)
```

这次成功了！

```
    Action from <NSButton: 0x7fe1019124d0>
```

**使其泛型化**  
第一个版本工作正常，但类型不太对。函数的参数总是 `NSControl`。这意味着虽然上面的测试代码有效，但下面这段不行：

```
    button.setAction({ print("Action from \($0.title)") })
```

这会编译失败，因为 `NSControl` 没有 `title` 属性。我们知道参数实际上是一个 `NSButton`，但编译器不知道这一点。在 Objective-C 中，我们只需在方法中声明正确的类型，编译器就必须信任我们。在 Swift 中，我们必须教育编译器了解这些类型。

我们可以让 `setAction` 成为泛型（generic），像这样：

```
    func setAction<T>(action: T -> Void) { ...
```

但这要求传入的函数有显式类型，所以 `$0` 不再起作用。你需要写类似这样的代码：

```
    button.setAction({ (sender: NSButton) in ...
```

让类型推断为我们工作会好得多。

Swift 的 `Self` 类型正是为此目的而存在的。`Self` 表示 `self` 的实际类型，就像 `instancetype` 在 Objective-C 中的作用一样。例如：

```
    extension NSControl {
        func frobnitz() -> Self {
            Swift.print("Frobbing \(self)")
            return self
        }
    }

    button.frobnitz().title = "hello"
```

让我们在 `NSControl` 扩展中使用它来使其泛型化：

```
    extension NSControl {
        @nonobjc func setAction(action: Self -> Void) {
```

哎呀，不行：

```
    error: 'Self' is only available in a protocol or as the result of a method in a class; did you mean 'NSControl'?
```

幸运的是，错误信息提示了一种前进的方法：把这个方法放到一个协议（protocol）里。从一个空协议开始：

```
    protocol NSControlActionFunctionProtocol {}
```

顺便也把关联对象键的名字改成适合其新位置的样子：

```
    let NSControlActionFunctionProtocolAssociatedObjectKey = UnsafeMutablePointer<Int8>.alloc(1)
```

我们需要一个泛型版本的 `ActionTrampoline`。这与原始版本非常相似，但 `action` 的实现需要一个强转（forced cast），因为 `@objc` 方法不允许引用泛型类型：

```
    class ActionTrampoline<T>: NSObject {
        var action: T -> Void

        init(action: T -> Void) {
            self.action = action
        }

        @objc func action(sender: NSControl) {
            action(sender as! T)
        }
    }
```

方法的实现基本上与之前相同，只是将 `NSControl` 替换为 `Self`。将扩展约束为 `Self: NSControl` 让我们可以在 `self` 上使用所有 `NSControl` 的方法和属性，比如 `target` 和 `action`：

```
    extension NSControlActionFunctionProtocol where Self: NSControl {
        func setAction(action: Self -> Void) {
            let trampoline = ActionTrampoline(action: action)
            self.target = trampoline
            self.action = "action:"
            objc_setAssociatedObject(self, NSControlActionFunctionProtocolAssociatedObjectKey, trampoline, .OBJC_ASSOCIATION_RETAIN)
        }
    }
```

最后，我们需要让 `NSControl` 在一个扩展里遵循这个协议。由于协议本身是空的，这个扩展也可以为空：

```
    extension NSControl: NSControlActionFunctionProtocol {}
```

让我们试试看！

```
    let button = NSButton()
    button.setAction({ (button: NSButton) in
        print("Action from \(button.title)")
    })
    button.sendAction(button.action, to: button.target)
```

输出：

```
    Action from Button
```

成功了！

**UIKit 版本**  
将这段代码用于 UIKit 是容易的。`UIControl` 可以为多种不同的事件拥有多个 target，所以我们只需要允许将事件作为参数传入，并使用 `addTarget` 来添加 trampoline：

```
    class ActionTrampoline<T>: NSObject {
        var action: T -> Void

        init(action: T -> Void) {
            self.action = action
        }

        @objc func action(sender: UIControl) {
            print(sender)
            action(sender as! T)
        }
    }

    let NSControlActionFunctionProtocolAssociatedObjectKey = UnsafeMutablePointer<Int8>.alloc(1)

    protocol NSControlActionFunctionProtocol {}
    extension NSControlActionFunctionProtocol where Self: UIControl {
        func addAction(events: UIControlEvents, _ action: Self -> Void) {
            let trampoline = ActionTrampoline(action: action)
            self.addTarget(trampoline, action: "action:", forControlEvents: events)
            objc_setAssociatedObject(self, NSControlActionFunctionProtocolAssociatedObjectKey, trampoline, .OBJC_ASSOCIATION_RETAIN)
        }
    }
    extension UIControl: NSControlActionFunctionProtocol {}
```

测试一下：

```
    let button = UIButton()
    button.addAction([.TouchUpInside], { (button: UIButton) in
        print("Action from \(button.titleLabel?.text)")
    })
    button.sendActionsForControlEvents([.TouchUpInside])

    Action from nil
```

显然 `UIButton` 不会像 `NSButton` 那样默认设置标题。不过，成功了！

**关于保留循环（retain cycle）的说明**  
使用这个调用很容易产生保留循环（retain cycle）。例如：

```
    button.addAction({ _ in
        self.doSomething()
    })
```

如果你持有对 `button` 的强引用（注意：即使你将 `button` 声明为 `weak`，如果你持有对包含它的视图或它的窗口的强引用，你也会间接持有对它的强引用），那么这将创建一个循环并导致你的对象泄露。

与循环的通常情况一样，解决办法是将 `self` 捕获为弱引用（weak）或无主引用（unowned）：

```
    button.addAction({ [weak self] _ in
        self?.doSomething()
    })
```

可选链（optional chaining）保持代码体易于阅读。或者，如果你确信在 `self` 被销毁之后，这个 action 绝对、永远不会被调用，则可以使用 `[unowned self]` 来获得一个无需进行 `nil` 检查的弱引用，因为如果 `self` 提前销毁，它会导致明显的失败。

**结论**  
为 Cocoa target/action 制作一个 Swift 风格的适配器相当直接。内存管理意味着我们需要稍微费点力气来保持 trampoline 对象的存活，但关联对象解决了这个问题。创建一个参数在 `self` 类型上是泛型的方法需要一些繁琐的操作，但协议扩展使其成为可能。

今天就到这里。新年我会带着更多好东西回来。Friday Q&A 由读者的想法驱动，所以如果你有任何希望在 2016 年或之后看到的话题，请[发送给我](mailto:mike@mikeash.com)！

你喜欢这篇文章吗？我在销售这些文章的全集！第二卷和第三卷现已上市！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-12-25-swifty-targetaction.html)

添加你的想法，发表评论：

垃圾邮件和跑题帖子将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
