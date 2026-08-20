---
title: 将 SwiftUI 视图渲染为 HTML
source: worthdoingbadly (Zhuowei Zhang)
source_key: worthdoingbadly
source_url: 'https://worthdoingbadly.com/swiftui-html/'
original_language: en
published: 2019-06-15
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:469b1cf1237b65b2'
translated: true
---

> 原文：[Rendering SwiftUI views to HTML](https://worthdoingbadly.com/swiftui-html/)　·　worthdoingbadly (Zhuowei Zhang)

# 将 SwiftUI 视图渲染为 HTML

2019 年 6 月 15 日

我构建了一个[概念验证工具](https://github.com/zhuowei/marina)，用于将 SwiftUI 渲染为 HTML。虽然我无意将其发展成一个完整的 UI 框架，但在此过程中我学到了很多东西：我学会了如何使用 Swift 的泛型、声明式 UI 框架为何使用影子图（shadow graph），以及 Swift 的设计如何是对 C++ 理念的演进。

![Apple 的 SwiftUI 中 Landmarks 示例渲染为 HTML 后的截图](https://worthdoingbadly.com/assets/blog/swiftui-html/swiftui_renderingLandmarksSample.png)

# 什么是 SwiftUI？

[SwiftUI](https://developer.apple.com/tutorials/swiftui/tutorials) 是 Apple 在 WWDC 2019 上发布的新 UI 框架。

它是一个声明式框架——你只需创建一些结构体（struct）来告知框架要渲染什么，框架会处理布局和事件。当底层状态改变时，平台会智能地重新渲染你的视图。

它在概念上类似于 React：

- SwiftUI 和 React 都允许开发者使用函数式编程技术创建 UI，而无需担心管理状态
- SwiftUI 和 React 都扩展了它们的宿主语言，使创建 UI 更加容易：

    - React 向 JavaScript 添加了 JSX
    - SwiftUI 向 Swift 添加了两个新的语法特性：[函数构造器（function builders）](https://github.com/apple/swift-evolution/pull/1046) 和[属性装饰器（property decorators）](https://github.com/apple/swift-evolution/blob/master/proposals/0258-property-delegates.md)。

# 我构建了什么？

我想了解 SwiftUI 如何使用新的 Swift 语法，因此决定创建一个 [SwiftUI 到 HTML 的转换器](https://github.com/zhuowei/marina)。

我的目标是：

- 理解 SwiftUI 如何使用其新的语法特性
- 理解 SwiftUI 如何利用 Swift 类型系统
- 将 [SwiftUI 教程示例 App](https://developer.apple.com/tutorials/swiftui/handling-user-input) 的第一页渲染为 HTML
- 赶在 WWDC 结束之前完成 ;)

为了按时完成，我有意避开了许多特性：我的库是：

- **不打算成为一个完整的、兼容 SwiftUI 的框架**——这方面请参见 [@MaxDesiatov 的 Tokamak](https://twitter.com/maxdesiatov/status/1135627087790911489)。
- **不打算作为 HTML 模板库**——这方面请使用 [@dokun1 的 Vaux](https://github.com/dokun1/Vaux)。
- **没有实现 SwiftUI 中的样式特性**
- **不支持数据绑定或交互功能**——SwiftUI 使用复杂的渲染图来跟踪每个 UI 元素的状态；我不可能在一周内重新实现它。

# 重新实现 SwiftUI 的公开 API

第一个任务是重新实现 SwiftUI 的结构体，以便使用 SwiftUI 的程序能够编译。

这大部分是直接的：我只需查阅[文档](https://developer.apple.com/documentation/swiftui/view)和 Xcode 中的 API 细节，然后在我的文件中重新创建每个结构体。

例如，Text 结构体只是：

```
struct Text : View, MarinaTextAccess {
    var content:String
    var body:Never {
        fatalError("Text has no body")
    }
    init<S>(_ content: S) where S : StringProtocol {
        self.content = String(content)
    }
    init(verbatim content: String) {
        self.content = String(content)
    }
    func getContent() -> Any {
        return content
    }
    func color(_ color: Color?) -> Text {
        return self
    }
    func font(_ font: MarinaFont) -> Text {
        return self
    }
}
```

这足以让 Apple 的 Landmarks 演示编译通过。

# 编译错误

更困难的部分是诊断编译错误。

函数构造器对 Swift 来说是新的，并且它们处理编译器错误的能力不佳：我遇到了许多无意义的错误，例如：`'inout Bool' is not convertible to 'Bool'`。

为了绕过这个问题，我会注释掉部分代码，直到错误变得合理。

事实上，我仍然无法在我的实现中让 `buildIf` 正常工作：我不得不[修改 Landmarks](https://github.com/zhuowei/marina-sample-landmarks/commit/2c493a166cc36c0f1ff575ca8b9df499408e80cc#diff-19174e087c34a01189d0450674a76d7fR19) 使用 if/else 配对来代替。

Swift 开发者们正在努力改进使用函数构造器时的编译器消息，因此我相信未来构建 DSL 会容易得多。

# 输出 HTML：理解泛型

一旦视图层级结构由结构体描述完毕，我就需要从这些结构体输出 HTML。

这是最困难的部分，因为 SwiftUI 严重依赖泛型。我已经写了一年半的 Swift，但这是我第一次写尖括号。

在 Java 中，我可以通过 `instanceof` 检查每个节点的类型，然后进行强制转换来访问其值。

```
if (view instanceof Text) {
    emit(((Text)view).getText());
}
```

在 Swift 中，这行不通，因为 Swift 的泛型具有与 Java 不同的语义：

```
test.swift:7:18: error: protocol 'View' can only be used as a generic constraint because it has Self or associated type requirements
if let a = b as? View {
```

我尝试了许多方法：

- 带有类型约束的泛型函数：不起作用，因为没有动态分发
- 向 View 协议添加一个函数，并在每个继承的结构体中重写它：同样，结构体不像类那样具有动态分发，因此重写不起作用
- 使用 Mirror 通过反射访问值：对计算属性（如 `body`）不起作用。

最后，在阅读了许多关于类型擦除（type erasure）的文章之后，我找到了关键诀窍：

- 让我的每个结构体继承一个唯一的访问协议（access protocol）。

    - 例如，上面的 `Text` 结构体实现了 `MarinaTextAccess`。
- 该协议将包含一个 `getContent() -> Any` 方法
- 在我的渲染方法中，我只是：

    - [检查输入是否实现了该访问协议](https://github.com/zhuowei/marina/blob/master/marina_html.swift#L46)。这是可行的，因为访问协议没有关联类型（associated types）。
    - 如果匹配，则将其强制转换为该访问协议，并调用 getContent。
    - getContent 然后返回视图的内容，作为类型擦除的 `Any` 值。

这避免了关联类型的问题。但是，这意味着我的所有视图都以 Any 类型传递：我很想了解处理此问题的正确类型安全方法是什么。

使用这种方法，我[遍历](https://github.com/zhuowei/marina/blob/master/marina_html.swift#L35) SwiftUI 的视图层级结构，为每个节点输出 HTML。

# 我学到的：设计上的限制

我一直想知道为什么每个声明式 UI 框架都会创建输入元素的影子表示（shadow representation）：

- 对于 React，是影子 DOM (Shadow DOM)
- 对于 Flutter，是渲染树 (Render Tree)
- 对于 SwiftUI，是特性图 (Attribute Graph)

在实现了这个 SwiftUI 到 HTML 的转换器之后，我终于明白了：影子图是 UI 存储状态和分发事件的地方——这样用户代码就不需要担心这些非功能性的细节。

我意识到，如果没有影子图，我的库永远无法处理诸如点击之类的事件。

有趣的是，由不同开发者使用不同语言实现的三个框架，最终得出了相同的解决方案，因为问题本身限制了解的空间。

# 我学到的：应用代码 vs 库代码

这个练习的一个意想不到的结果是：我现在更好地理解了 Swift 和 Go 之间的比较。当然，我读过那些 [俯拾皆是](https://www.quora.com/How-does-Apples-new-programming-language-Swift-compare-against-Google-Go) 的 [Swift vs Go 的帖子](https://www.quora.com/How-does-Apples-new-programming-language-Swift-compare-against-Google-Go/answer/John-Forde-8) [和文章](https://opencredo.com/blogs/java-go-back/)：然而，直到这次我才真正理解：Swift 和 Go 是编程语言设计的两种不同方法的演进。

在编写这个 SwiftUI 到 HTML 的转换器之前，我在 Swift 中写了正好 0 对泛型尖括号。

作为一名 iOS App 开发者，我只是把 Swift 当作“没有分号的 Objective-C”来使用——我完全不需要与类型系统交互。因此，当我尝试实现一个严重依赖泛型的库时，我完全力不从心。

在 Swift 中，类型系统改善了库使用者的体验，但代价是增加了库实现者的复杂性。这造成了一个鸿沟，一些 App 开发者无法理解库，因为他们在日常的应用代码中从未遇到过诸如泛型这样的高级特性。

这让我想起了 C++ 模板。C++ 标准模板库 (STL) 使用模板，通过容器和智能指针使 C++ 对开发者来说易于使用。然而，我一行 STL 代码都看不懂。（我试过。）

由此，我意识到大多数编程语言设计都采取两种方法之一：

- 赋予库开发者巨大的权力来构建抽象，从而使应用代码变得非常简单

    - 但应用开发者无法掌握透过表象理解或编写库所需的技能

或者：

- 为库和应用设计一种简单的语言

    - 使应用代码更冗长，但允许任何人理解库

当然，C++ 属于第一类，而 Java 则采取第二种方法：

Java 代码有时因其冗长而受到嘲笑，但我可以打开任何文件——例如 [Android 的源代码](https://github.com/aosp-mirror/platform_frameworks_base/blob/master/core/java/android/widget/TextView.java)——然后立刻理解它，而无需学习特定于库开发的新编程技术。

我觉得最有趣的是，Swift 和 Go 代表了每种方法的优化版本：

- Swift，属于第一类，利用其类型系统让库能够提供更好的编译时诊断，使编写应用更加容易。
- Go，属于第二类，添加了深思熟虑的语言特性，例如内置并发（concurrency），在保持语言易懂的同时减少了冗长。

我非常喜欢 Swift 和 Go 都充分利用了其前身方法的优点，同时减轻了其缺点。这让我更加欣赏它们设计中的深思熟虑。

# 我学到的：总结

- Swift 函数构造器和属性装饰器
- Swift 泛型
- Swift 的设计理念

# 如何帮助

- 关于如何改进渲染代码以使其更类型安全，有什么建议吗？请告诉我 [@zhuowei](https://twitter.com/zhuowei)。

# 你可能喜欢的其他链接

- [Swift Evolution 关于函数构造器的 pull request](https://github.com/apple/swift-evolution/pull/1046)
- [Swift 包含函数构造器示例的 pull request](https://github.com/apple/swift/pull/25221)
- [Swift Evolution 关于属性委托的 pull request](https://github.com/apple/swift-evolution/blob/master/proposals/0258-property-delegates.md)
- [SwiftRocks 关于 SwiftUI 技巧的文章](https://swiftrocks.com/inside-swiftui-compiler-magic.html)
- [kateinoigakukun 关于 SwiftUI 如何利用 ABI 稳定性实现其魔法的文章](https://kateinoigakukun.hatenablog.com/entry/2019/06/09/081831)

[https://worthdoingbadly.com/swiftui-html/](https://worthdoingbadly.com/swiftui-html/)
