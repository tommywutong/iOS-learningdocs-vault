---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Introduction/introObjectiveC.html
archived_at: '2026-07-15T07:17:31.942122Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Objects%2C%20Classes%2C%20and%20Messaging.md)

# 简介

Objective-C 语言是一门简单的计算机语言，旨在支持精巧的面向对象编程。Objective-C 被定义为对标准 ANSI C 语言的一组小巧但强大的扩展。它对 C 的扩充大多基于 Smalltalk——最早的面向对象编程语言之一。Objective-C 的设计目标是让 C 具备完整的面向对象编程能力，并且以一种简单直接的方式实现这一点。

大多数面向对象开发环境由若干部分组成：

- 一门面向对象编程语言
- 一个对象库
- 一套开发工具
- 一个运行时环境

本文档讲的是开发环境的第一个组成部分——编程语言。本文档也为学习第二个组成部分打下基础，也就是 Objective-C 应用程序[框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)——它们统称为 _Cocoa_。运行时环境则在另一份文档中单独介绍，即 _[Objective-C 运行时编程指南](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_。

本文档适合以下读者：

- 想学习 Objective-C 编程的人
- 想了解 Cocoa 应用程序框架基础的人

本文档既介绍了 Objective-C 所基于的面向对象模型，又完整记录了该语言本身。它着重讲解 Objective-C 对 C 的扩展，而不是 C 语言本身。

由于本文档不是一份讲解 C 的文档，它假定读者已经对 C 有一定了解。不过，Objective-C 中的面向对象编程与 ANSI C 中的 _过程式编程_ 有很大不同，因此即便你不是一位经验丰富的 C 程序员，也不会因此受阻。

以下各章介绍了 Objective-C 在标准 C 基础上添加的全部特性。

- [对象、类与消息传递](Objects%2C%20Classes%2C%20and%20Messaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfvjvomi)
- [定义类](Defining%20a%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjsfvjvomi)
- [协议](Protocols.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjvfvjvomi)
- [声明属性](Declared%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomi)
- [分类与扩展](Categories%20and%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrqfvjvomi)
- [关联引用](Associative%20References.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrufvjvomi)
- [快速枚举](Fast%20Enumeration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjyfvjvomi)
- [启用静态行为](Enabling%20Static%20Behavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjwfvjvomi)
- [选择器](Selectors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrtfvjvomi)
- [异常处理](Exception%20Handling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjtfvjvomi)
- [线程](Threading.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjzfvjvomi)

本文档末尾的术语表给出了 Objective-C 和面向对象编程中特有术语的定义。

本文档对等宽字体和斜体字体做了特殊约定。等宽字体表示应当照原样输入的单词或字符（按其出现的样子输入）。斜体表示代表其他内容、可以替换的单词。例如，以下语法：

`@interface`_ClassName_`(`_CategoryName_`)`

意思是 `@interface` 和两个括号是必需的，但类名和分类名可以由你自行选择。

在示例代码中，省略号表示被省去的部分，这些部分往往篇幅不小：

```objc
- (void)encodeWithCoder:(NSCoder *)coder
{
    [super encodeWithCoder:coder];
    ...
}
```


如果你从未使用过面向对象编程来创建应用程序，应当阅读 _[Objective-C 面向对象编程](../Object-Oriented%20Programming%20with%20Objective-C/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbz)_。如果你使用过 C++ 和 Java 等其他面向对象开发环境，也应当考虑阅读该文档，因为它们的许多预期和约定与 Objective-C 不同。_[Objective-C 面向对象编程](../Object-Oriented%20Programming%20with%20Objective-C/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbz)_ 旨在帮助你从 Objective-C 开发者的视角熟悉面向对象开发。它阐明了面向对象设计的一些内涵，让你体会到编写面向对象程序究竟是什么样子。

_[Objective-C 运行时编程指南](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_ 介绍了 Objective-C 运行时的各个方面以及如何使用它。

_[Objective-C 运行时参考](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_ 介绍了 Objective-C 运行时支持库的数据结构和函数。你的程序可以使用这些接口与 Objective-C 运行时系统交互。例如，你可以添加类或方法，或者获取已加载的所有类定义的列表。

Objective-C 支持三种内存管理机制：自动垃圾回收和引用计数：

- _自动引用计数_（ARC），由编译器推断对象的生命周期。
- _手动引用计数_（MRC，有时也称为 MRR，即"手动 retain/release"），由你自己最终负责确定对象的生命周期。

  手动引用计数在 _[高级内存管理编程指南](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_ 中介绍。
- _垃圾回收_，你把确定对象生命周期的职责交给一个自动的"回收器"。

  垃圾回收在 _[垃圾回收编程指南](../Garbage%20Collection%20Programming%20Guide/Introduction%20to%20Garbage%20Collection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzr)_ 中介绍。（iOS 不提供该功能——你无法通过 iOS 开发者中心访问该文档。）

[下一页](Objects%2C%20Classes%2C%20and%20Messaging.md)

