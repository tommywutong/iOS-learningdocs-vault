---
title: 异常编程主题
apple_id: 10000012i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Articles/ExceptionsAndCocoaFrameworks.html
archived_at: '2026-07-15T07:15:37.409854Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [异常编程主题](Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md)


[下一篇](Handling%20Exceptions.md) [上一篇](Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md)

# 异常与 Cocoa 框架

Cocoa 中的异常由 Foundation 框架中的 [NSException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/cl/NSException) 类对象表示。该类的方法允许你创建异常对象、使用这些对象引发（抛出）异常，以及获取与异常相关的调用返回地址。`NSException` 对象具有以下属性：

- [name](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/instm/NSException/name)：用于唯一标识异常的短字符串。名称是必需的。
- [reason](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/instm/NSException/reason)：包含异常“人类可读”原因的较长字符串。原因是必需的。
- 可选字典（[userInfo](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/instm/NSException/userInfo)），用于向异常处理器提供应用程序专用数据。例如，如果某方法的返回值导致异常被抛出，可以通过 `userInfo` 将该返回值传给异常处理器。

你可以提取异常对象中的信息，并在适当时通过警告对话框向用户显示，也可以借助 [NSError](https://developer.apple.com/documentation/foundation/nserror) 对象。有关此主题的信息，请参阅[处理异常](Handling%20Exceptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga2tslktk4yq)。

Cocoa 框架要求所有异常都是 `NSException` 或其子类的实例。请勿抛出其他类型的对象。

Cocoa 框架通常不具备异常安全性。一般而言，异常仅用于表示程序员错误，捕获到此类异常的程序应尽快退出。

[下一篇](Handling%20Exceptions.md) [上一篇](Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md)
