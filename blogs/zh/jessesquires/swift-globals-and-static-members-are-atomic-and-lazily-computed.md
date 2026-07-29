---
title: Swift 全局与静态成员都是原子且惰性计算的
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/07/16/swift-globals-and-static-members-are-atomic-and-lazily-computed/'
original_language: en
published: 2020-07-16
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d217a24e951b65e9'
translated: true
---

> 原文：[Swift globals and static members are atomic and lazily computed](https://www.jessesquires.com/blog/2020/07/16/swift-globals-and-static-members-are-atomic-and-lazily-computed/)　·　Jesse Squires

前几天调试代码时，我想验证 Swift 中全局变量和静态成员的行为。我隐约记得在 Swift 早期，`static let` 成员和全局常量是原子（atomic）且惰性计算（lazily computed）的——这是相较于 Objective-C 的诸多改进之一。

通过一些示例代码和调试器很容易验证这一点，但我也想找到支持这个行为的文档。这些行为在《[Swift 编程语言](https://books.apple.com/us/book/the-swift-programming-language-swift-5-2/id881256329)》e-book 中有描述，现在这本书也能方便地在 [Swift.org](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html) 上阅览。

在属性（Properties）一章中，有关于[全局变量和局部变量](https://docs.swift.org/swift-book/LanguageGuide/Properties.html#ID263)的一节：

> 全局常量和变量始终以类似惰性存储属性的方式惰性计算。与惰性存储属性不同，全局常量和变量无需使用 `lazy` 修饰符标记。

还有关于[类型属性](https://docs.swift.org/swift-book/LanguageGuide/Properties.html#ID264)的一节：

> 存储类型属性在首次访问时惰性初始化。它们保证只会被初始化一次，即使在多个线程同时访问时也是如此，并且无需使用 `lazy` 修饰符标记。

这实际上赋予了 `static` 成员和全局变量与 Objective-C 中使用 [`dispatch_once`](https://developer.apple.com/documentation/dispatch/1447169-dispatch_once) 相同的行为。同样，你可以在调试器中轻松观察到这一点。

在 developer.apple.com 上还有一篇[旧的、原始的（但现已被放弃的）Swift 博客](https://developer.apple.com/swift/blog/?id=7)文章。这篇文章提供了实现这一行为的基本原理：

> Swift 采用了第三种方法，这是最理想的方式：它允许自定义初始化器，Swift 的启动时间随规模平稳扩展，没有全局初始化器来拖慢速度，并且执行顺序完全可预测。
>
> 全局变量（以及结构体和枚举的静态成员）的惰性初始化器在首次访问该全局变量时运行，并以 `dispatch_once` 方式启动，以确保初始化是原子的。这让你可以在代码中以很酷的方式使用 `dispatch_once`：只需声明一个带有初始化器并标记为 `private` 的全局变量。

（感谢 [Fran Depascuali](https://twitter.com/FranDepascuali/status/1283619124938244102) 在 Twitter 上指出这一点。）

### 原子性与线程安全……还是说不？

鉴于上述情况，有几点重要事项需要注意。原子性（atomicity）的概念不同于线程安全（thread-safety）的概念。原子性并不意味着线程安全，但如果某物是线程安全的，它必须是原子的。

原子性描述了读写变量时的完整性。来自 [Programming with Objective-C 存档文档](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/EncapsulatingData/EncapsulatingData.html)：

> **注意：** 属性的原子性不等同于对象的线程安全。
>
> 考虑一个 `XYZPerson` 对象，其中一个人的名字和姓氏都由一个线程使用原子访问器修改。如果另一个线程同时访问这两个名字，原子 getter 方法会返回完整的字符串（不会崩溃），但无法保证这些值相对于彼此是正确的名字。如果名字在修改前被访问，但姓氏在修改后被访问，你就会得到不一致、不匹配的一对名字。

原子性仅保证你不会读取或写入部分（垃圾）值。

然而，对于 Swift 中结构体、枚举和类上的全局**常量**（`let`）或 `static let` 成员，我们**可以**说它们是**线程安全的**，因为它们是原子的_而且_**不可变（immutable）**。

Swift 保证所有全局和 `static` 成员的原子性和同步初始化，但只有声明为 `let` 的那些成员在初始化后才是线程安全的，因为它们不可变。（我们知道不可变值可以安全地在多个线程间访问。）对于全局 `var` 声明或 `static var` 成员，我们不能声称它们是线程安全的，因为它们可能在初始化后跨线程被修改。

（感谢 [Joe Groff](https://twitter.com/jckarter/status/1283634305021796353) 确认这一点。）
