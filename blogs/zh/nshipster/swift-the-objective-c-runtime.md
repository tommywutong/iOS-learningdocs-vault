---
title: Swift 与 Objective-C 运行时
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/swift-objc-runtime/'
original_language: en
published: 2015-01-26
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:31e103f1b6672ded'
translated: true
---

> 原文：[Swift & the Objective-C Runtime](https://nshipster.com/swift-objc-runtime/)　·　NSHipster (Mattt)

# [Swift & the Objective-C Runtime](https://nshipster.com/swift-objc-runtime/)

作者：[Nate Cook](https://nshipster.com/authors/nate-cook/)　2015 年 1 月 26 日

即使不写一行 Objective-C 代码，每个 Swift App 也在 Objective-C 运行时内部执行，这开启了一个动态分发和关联运行时操控的世界。当然，情况未必始终如此——等到纯 Swift 的框架出现时，可能会催生纯 Swift 的运行时。但只要 Objective-C 运行时还在我们身边，就让我们充分发挥它的潜力吧。

本周我们以全新的 Swift 视角，审视两项运行时技术，这两项技术曾在 Objective-C 还是唯一玩法的 NSHipster 文章中介绍过：[关联对象（associated objects）](https://nshipster.com/associated-objects/) 和 [方法交叉（method swizzling）](https://nshipster.com/method-swizzling/)。

> _注意：_ 本文主要介绍这些技术在 Swift 中的使用——如需完整解读，请参考原始文章。

## 关联对象（Associated Objects）

Swift 的扩展（extension）为扩展现有 Cocoa 类的功能提供了极大的灵活性，但它们和 Objective-C 的分类（category）一样有局限性。也就是说，你无法通过扩展（extension）向现有类添加属性。

幸运的是，Objective-C 的 _关联对象（associated objects）_ 可以救场。例如，要为项目中的所有视图控制器添加一个 `descriptiveName` 属性，我们只需在底层 `get` 和 `set` 代码块中使用 `objc_get/setAssociatedObject()` 添加一个计算属性：

```
extension UIViewController {
    private struct AssociatedKeys {
        static var DescriptiveName = "nsh_DescriptiveName"
    }

    var descriptiveName: String? {
        get {
            return objc_getAssociatedObject(self, &AssociatedKeys.DescriptiveName) as? String
        }

        set {
            if let newValue = newValue {
                objc_setAssociatedObject(
                    self,
                    &AssociatedKeys.DescriptiveName,
                    newValue as NSString?,
                    .OBJC_ASSOCIATION_RETAIN_NONATOMIC
                )
            }
        }
    }
}
```

> 注意在私有的嵌套 `struct` 中使用 `static var`——这种模式创建了我们所需的静态关联对象键（associated object key），但不会污染全局命名空间。

## 方法交叉（Method Swizzling）

有时是为了方便，有时是为了绕开框架中的 bug，有时则是因为别无他法——你需要修改现有类方法的行为。方法交叉（method swizzling）允许你交换两个方法的实现，本质上是用你自己的实现来覆盖现有方法，同时保留原始实现。

在本例中，我们交叉了 `UIViewController` 的 `viewWillAppear` 方法，以便在视图即将出现在屏幕上时打印一条消息。交叉操作发生在特殊的类方法 `initialize` 中（参见下方的说明）；替换的实现位于 `nsh_viewWillAppear` 方法中：

```
extension UIViewController {
    public override class func initialize() {
        struct Static {
            static var token: dispatch_once_t = 0
        }

        // 确保这不是子类
        if self !== UIViewController.self {
            return
        }

        dispatch_once(&Static.token) {
            let originalSelector = Selector("viewWillAppear:")
            let swizzledSelector = Selector("nsh_viewWillAppear:")

            let originalMethod = class_getInstanceMethod(self, originalSelector)
            let swizzledMethod = class_getInstanceMethod(self, swizzledSelector)

            let didAddMethod = class_addMethod(self, originalSelector, method_getImplementation(swizzledMethod), method_getTypeEncoding(swizzledMethod))

            if didAddMethod {
                class_replaceMethod(self, swizzledSelector, method_getImplementation(originalMethod), method_getTypeEncoding(originalMethod))
            } else {
                method_exchangeImplementations(originalMethod, swizzledMethod);
            }
        }
    }

    // MARK: - 方法交叉

    func nsh_viewWillAppear(animated: Bool) {
        self.nsh_viewWillAppear(animated)
        if let name = self.descriptiveName {
            print("viewWillAppear: \(name)")
        } else {
            print("viewWillAppear: \(self)")
        }
    }
}
```

### load 对比 initialize（Swift 版）

Objective-C 运行时在加载和初始化 App 进程中的类时，通常会自动调用两个类方法：`load` 和 `initialize`。在关于[方法交叉（method swizzling）](https://nshipster.com/method-swizzling/)的完整文章中，Mattt 写道，为了安全性和一致性，交叉操作 _始终_ 应该在 `load()` 中进行。`load` 每个类只调用一次，并且会在每个被加载的类上调用。另一方面，一个 `initialize` 方法可能在一个类及其所有子类上被调用（对于 `UIViewController` 来说很可能存在子类），或者如果某个特定类从未被发送消息，则根本不会被调用。

不幸的是，在 Swift 中实现的 `load` 类方法 _从未_ 被运行时调用，这让那项建议变得不可行。相反，我们只能退而求其次，从以下选项中做出选择：

- **在 `initialize` 中实现方法交叉（method swizzling）**   
  只要在执行时检查类型，并用 `dispatch_once`（无论如何你都应该这么做）包装交叉操作，这样做是安全的。
- **在 App 委托中实现方法交叉（method swizzling）**  
  不通过类扩展（extension）添加方法交叉，而是直接在 App 委托中添加一个方法，在调用 `application(_:didFinishLaunchingWithOptions:)` 时执行。根据你修改的类而定，这样做可能已经足够，并且能保证你的代码每次都会执行。

---

最后，请记住，调整 Objective-C 运行时应该更多地是最后的手段，而不是出发的起点。修改你的代码所依赖的框架，以及你运行的任何第三方代码，是迅速破坏整个栈稳定性的方式。请谨慎行事！
