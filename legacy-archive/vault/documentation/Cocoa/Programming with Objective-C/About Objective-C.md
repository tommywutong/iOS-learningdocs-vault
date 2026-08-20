---
title: 用 Objective-C 编程
apple_id: TP40011210
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html
archived_at: '2026-07-15T07:17:59.419329Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Defining%20Classes.md)

# 关于 Objective-C

Objective-C 是你在为 OS X 和 iOS 编写软件时所使用的主要编程语言。它是 C 编程语言的一个超集，提供了面向对象的能力和动态运行时。Objective-C 继承了 C 语言的语法、原始类型和流程控制语句，并添加了用于定义类和方法的语法。它还为对象关系图管理和对象字面量添加了语言级支持，同时提供动态类型和绑定，将许多职责延后到运行时才处理。

本文档介绍 Objective-C 语言，并提供了大量使用示例。你将学习如何创建自己的类来描述自定义对象，并了解如何使用 Cocoa 和 Cocoa Touch 提供的一些框架类。虽然框架类与语言本身是分开的，但它们的使用与 Objective-C 编程紧密交织在一起，许多语言层面的特性都依赖于这些类所提供的行为。

### 应用由一个对象网络构成

在为 OS X 或 iOS 构建应用时，你大部分时间都会用来处理对象。这些对象都是 Objective-C 类的实例，其中一些由 Cocoa 或 Cocoa Touch 提供，另一些则由你自己编写。

如果你在编写自己的类，首先要为该类提供一份描述，详细说明该类实例所面向的公共接口。这份接口包括用于封装相关数据的公共属性，以及一份方法列表。方法声明表明了一个对象可以接收的消息，并包含每次调用该方法时所需参数的信息。你还需要提供一份类实现，其中包含接口中所声明的每个方法的可执行代码。

### 分类扩展现有类

与其为了在现有类的基础上提供一些小的附加能力而创建一个全新的类，不如定义一个分类，为现有类添加自定义行为。你可以使用分类为任意类添加方法，包括那些你没有原始实现源代码的类，例如像 `NSString` 这样的框架类。

如果你确实拥有某个类的原始源代码，可以使用类扩展来添加新属性，或者修改现有属性的特性。类扩展常用于隐藏私有行为，这些行为要么仅供单个源代码文件内部使用，要么仅在自定义框架的私有实现内部使用。

### 协议定义消息传递约定

在一个 Objective-C 应用中，大部分工作都是通过对象之间相互发送消息来完成的。通常，这些消息由类接口中显式声明的方法来定义。不过，有时候能够定义一组并不直接与特定类绑定的相关方法会很有用。

Objective-C 使用协议来定义一组相关的方法，比如一个对象可能会在其[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)上调用的方法，这些方法可以是可选的，也可以是必需的。任何类都可以表明自己采纳了某个协议，这意味着它也必须为该协议中所有必需的方法提供实现。

### 值与集合通常表示为 Objective-C 对象

在 Objective-C 中，使用 Cocoa 或 Cocoa Touch 类来表示值是很常见的做法。`NSString` 类用于表示字符串，`NSNumber` 类用于表示整数或浮点数等不同类型的数字，`NSValue` 类则用于表示诸如 C 结构体之类的其他值。你也可以使用 C 语言定义的任意原始类型，比如 `int`、`float` 或 `char`。

集合通常表示为某个集合类的实例，比如 `NSArray`、`NSSet` 或 `NSDictionary`，它们各自用来收集其他 Objective-C 对象。

### Block 简化常见任务

Block 是 C、Objective-C 和 C++ 中引入的一项语言特性，用来表示一个工作单元；它们把一段代码连同其捕获的状态一起封装起来，这使得它们与其他编程语言中的闭包很相似。Block 常用于简化诸如集合枚举、排序和条件测试之类的常见任务。它们还能让你轻松使用 Grand Central Dispatch（GCD）之类的技术，为并发或异步执行安排任务。

### 错误对象用于处理运行时问题

尽管 Objective-C 包含用于异常处理的语法，Cocoa 和 Cocoa Touch 只将异常用于编程错误（比如数组越界访问），这些错误应该在应用发布之前就修复好。

其他所有的错误——包括诸如磁盘空间不足或无法访问某个 web 服务之类的运行时问题——都由 `NSError` 类的实例来表示。你的应用应该对错误有所规划，并决定如何最好地处理它们，以便在出现问题时依然能呈现尽可能好的用户体验。

### Objective-C 代码遵循既定约定

在编写 Objective-C 代码时，你应该牢记一些既定的编码约定。例如，方法名以小写字母开头，多个单词时使用驼峰式写法，比如 `doSomething` 或 `doSomethingElse`。不过重要的不仅仅是大小写规则，你还应该确保代码尽可能可读，这意味着方法名应该具有表达力，但又不能过于冗长。

此外，如果你想利用语言或框架特性，还有一些约定是必须遵循的。举例来说，属性的存取方法必须遵循严格的命名约定，才能配合诸如[键值编码](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25)（KVC）或[键值观察](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16)（KVO）之类的技术使用。

如果你刚开始接触 OS X 或 iOS 开发，建议你在阅读本文档之前先通读 _[Start Developing iOS Apps Today (Retired)](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/index.html#//apple_ref/doc/uid/TP40011343)_ 或 _[Start Developing Mac Apps Today](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapOSX/index.html#//apple_ref/doc/uid/TP40012262)_，以便对 iOS 和 OS X 的应用开发流程有一个大致的了解。此外，你还应该熟悉 Xcode，然后再尝试完成本文档大多数章节末尾的练习。Xcode 是用来为 iOS 和 OS X 构建应用的集成开发环境（IDE）；你将用它来编写代码、设计应用的用户界面、测试应用并调试问题。

虽然最好对 C 语言或某种基于 C 的语言（比如 Java 或 C#）有一定了解，但本文档确实包含了一些基本 C 语言特性（比如流程控制语句）的内联示例。如果你了解另一种更高层次的编程语言，比如 Ruby 或 Python，你应该也能跟上本文档的内容。

本文档对一般的面向对象编程原则给予了合理的介绍，尤其是这些原则在 Objective-C 语境下的应用，但假定你至少对基本的面向对象概念有最基本的了解。如果你对这些概念还不熟悉，应该先阅读 _[Objective-C 编程概念](../../General/Concepts%20in%20Objective-C%20Programming/About%20the%20Basic%20Programming%20Concepts%20for%20Cocoa%20and%20Cocoa%20Touch.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmjq)_ 中的相关章节。

本文档的内容适用于 Xcode 4.4 或更高版本，并假定你的目标平台是 OS X v10.7 或更高版本，或者 iOS 5 或更高版本。有关 Xcode 的更多信息，请参阅 _[Xcode 概览](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/index.html#//apple_ref/doc/uid/TP40010215)_。有关语言特性可用性的信息，请参阅 _[Objective-C 特性可用性索引](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/ObjCAvailabilityIndex/index.html#//apple_ref/doc/uid/TP40012243)_。

Objective-C 应用使用引用计数来决定对象的生命周期。在大多数情况下，编译器的自动引用计数（ARC）特性会替你处理这一切。如果你无法利用 ARC，或者需要转换或维护那些手动管理对象内存的遗留代码，应该阅读 _[高级内存管理编程指南](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_。

除了编译器之外，Objective-C 语言还使用一套运行时系统来实现其动态和面向对象的特性。虽然你通常不需要担心 Objective-C 是如何"运作"的，但你也可以直接与这套运行时系统交互，具体描述见 _[Objective-C Runtime Programming Guide](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_ 和 _[Objective-C Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_。

[下一页](Defining%20Classes.md)

