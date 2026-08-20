---
title: Objective-C 运行时编程指南
apple_id: TP40008048
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:17:29.414322Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Runtime%20Versions%20and%20Platforms.md)

# 简介

Objective-C 语言尽可能把决策从编译期和链接期推迟到运行期。只要有可能，它就会以动态的方式完成工作。这意味着这门语言不仅需要一个编译器，还需要一个运行时（runtime）系统来执行编译后的代码。运行时系统对 Objective-C 语言而言就像一种操作系统，正是它让这门语言得以运转。

本文档考察 `NSObject` 类，以及 Objective-C 程序与运行时系统交互的方式。具体来说，它会探讨在运行时动态加载新类、以及把消息转发给其他对象的范式。此外，它还会介绍如何在程序运行期间获取有关对象的信息。

阅读本文档可以帮助你理解 Objective-C 运行时系统的工作原理，以及如何加以利用。不过通常来说，编写一个 Cocoa 应用程序并不太需要你了解和掌握这些内容。

本文档包含以下各章：

- [运行时版本与平台](Runtime%20Versions%20and%20Platforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgywvgvzr)
- [与运行时交互](Interacting%20with%20the%20Runtime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgmwvgvzr)
- [消息传递](Messaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgqwvgvzr)
- [动态方法解析](Dynamic%20Method%20Resolution.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgiwvgvzr)
- [消息转发](Message%20Forwarding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqguwvgvzr)
- [类型编码](Type%20Encodings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgawvgvzr)
- [声明属性](Declared%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgewvgvzr)

_[Objective-C Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_ 介绍了 Objective-C 运行时支持库的数据结构和函数。你的程序可以通过这些接口与 Objective-C 运行时系统交互。例如，你可以添加类或方法，也可以获取已加载类的全部类定义列表。

_[使用 Objective-C 编程](../Programming%20with%20Objective-C/About%20Objective-C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjq)_ 介绍了 Objective-C 语言本身。

_[Objective-C Release Notes](https://developer.apple.com/library/archive/releasenotes/Cocoa/RN-ObjectiveC/index.html#//apple_ref/doc/uid/TP40004309)_ 介绍了近期 OS X 发布版本中 Objective-C 运行时的部分变化。

[下一页](Runtime%20Versions%20and%20Platforms.md)

