---
title: Objective-C 运行时编程指南
apple_id: TP40008048
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtInteracting.html
archived_at: '2026-07-15T07:17:29.379264Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 运行时编程指南](Introduction.md)


[下一页](Messaging.md)[上一页](Runtime%20Versions%20and%20Platforms.md)

# 与运行时交互

Objective-C 程序在三个不同层面上与运行时（runtime）系统交互：通过 Objective-C 源代码；通过 Foundation 框架中 `NSObject` 类定义的方法；以及通过直接调用运行时函数。

在大多数情况下，运行时系统会在幕后自动工作。你只要编写并编译 Objective-C 源代码，就已经在使用它了。

当你编译含有 Objective-C 类和方法的代码时，编译器会创建实现这门语言动态特性所需的数据结构和函数调用。这些数据结构记录了从类定义、分类定义和协议声明中获得的信息；它们包括 _[Objective-C 编程语言](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ 中 [定义类](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocDefiningClasses.html#//apple_ref/doc/uid/TP30001163-CH12) 和 [协议](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocProtocols.html#//apple_ref/doc/uid/TP30001163-CH15) 两处讨论过的类对象和协议对象，也包括方法选择器、实例变量模板以及其他从源代码中提炼出来的信息。最主要的运行时函数是负责发送消息的那一个，参见 [消息传递](Messaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgqwvgvzr)。它由源代码中的消息表达式调用。

Cocoa 中大多数对象都是 `NSObject` 类的子类，因此大多数对象都会继承它定义的方法。（一个显著的例外是 `NSProxy` 类；更多信息参见 [消息转发](Message%20Forwarding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqguwvgvzr)。）因此，它的方法确立了每个实例和每个类对象所固有的行为。不过在少数情况下，`NSObject` 类只是定义了某件事应该如何完成的模板，并不提供全部必要的代码。

例如，`NSObject` 类定义了一个 `description` 实例方法，返回一个描述类内容的字符串。它主要用于调试——GDB 的 `print-object` 命令打印的就是该方法返回的字符串。`NSObject` 对该方法的实现并不知道类里面有什么内容，所以它只返回一个包含对象名称和地址的字符串。`NSObject` 的子类可以实现该方法以返回更多细节。例如，Foundation 中的 `NSArray` 类会返回它所包含对象的描述列表。

`NSObject` 的一部分方法只是向运行时系统查询信息。这些方法让对象得以执行内省（introspection）。这类方法的例子有：`class` 方法，用于询问一个对象自己的类是什么；`isKindOfClass:` 和 `isMemberOfClass:`，用于检测对象在继承体系中的位置；`respondsToSelector:`，用于指明对象能否接受某个特定消息；`conformsToProtocol:`，用于指明对象是否声称实现了某个特定协议中定义的方法；以及 `methodForSelector:`，用于提供某个方法实现的地址。诸如此类的方法赋予对象自我内省的能力。

运行时系统是一个动态共享库，其公开接口由一组函数和数据结构组成，它们位于 `/usr/include/objc` 目录下的头文件中。这些函数中有许多能让你用纯 C 复现编写 Objective-C 代码时编译器所做的事情。另一些则构成了通过 `NSObject` 类方法对外提供的那些功能的基础。这些函数使人们得以开发运行时系统的其他接口，并制作出增强开发环境的工具；用 Objective-C 编程时并不需要它们。不过，其中少数运行时函数在编写 Objective-C 程序时偶尔也会有用。所有这些函数都记录在 _[Objective-C Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_ 中。

[下一页](Messaging.md)[上一页](Runtime%20Versions%20and%20Platforms.md)

