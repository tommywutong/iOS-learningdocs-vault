---
title: Objective-C 面向对象编程
apple_id: TP40005149
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOP_ObjC/Articles/ooWhy.html
archived_at: '2026-07-15T07:17:21.852618Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 面向对象编程](Introduction.md)


[下一页](Object-Oriented%20Programming.md)[上一页](Introduction.md)

# 为什么选择 Objective-C？

选择 Objective-C 语言有多方面的原因。首要的一点是，它是一门面向对象语言。Cocoa 框架所封装的那类功能，只能通过面向对象技术来交付。其次，由于 Objective-C 是标准 ANSI C 的扩展，现有的 C 程序可以改造过来使用这些软件框架，当初投入的开发成果一点都不会丢失。因为 Objective-C 包含了 C，你在 Objective-C 中工作时可以享有 C 的全部好处。什么时候用面向对象的方式做事（比如定义一个新类），什么时候坚持过程式编程手法（比如不定义类，而是定义一个结构体和若干函数），完全由你决定。

此外，Objective-C 从根本上说是一门简单的语言。它语法量小、含义明确、易于学习。面向对象编程带着一套自成体系的术语，又强调抽象设计，对新手来说往往有一道陡峭的学习曲线。而像 Objective-C 这样组织得当的语言，能让你少费不少力气就成为熟练的面向对象程序员。

与其他基于 C 的面向对象语言相比，Objective-C 非常动态。编译器会保留大量关于对象自身的信息，供运行时使用。本来可能在编译期做出的决定，可以推迟到程序运行时再做。这种动态性给了 Objective-C 程序不同寻常的灵活性和能力。举例来说，它带来了两大好处，而这两点在其他名义上的面向对象语言中很难得到：

- Objective-C 支持一种开放风格的动态绑定，这种风格能够支撑起一套面向交互式用户界面的简单架构。消息不一定受限于接收者所属的类，甚至不一定受限于方法名，因此软件框架可以为运行时的用户选择留出余地，也让开发者在设计上有自由发挥的空间。（_动态绑定_、_消息_、_类_、_接收者_ 这类术语会在本文档后续内容中逐一解释。）
- 有了动态性，才能构建出精巧的开发工具。通往运行时系统的接口让你能拿到运行中应用的信息，于是就有可能开发出一类工具，用来监控、介入并揭示 Objective-C 应用底层的结构与活动。

[下一页](Object-Oriented%20Programming.md)[上一页](Introduction.md)

