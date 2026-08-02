---
title: 异常编程主题
apple_id: 10000012i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Concepts/UncaughtExceptions.html
archived_at: '2026-07-15T07:15:38.411002Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [异常编程主题](Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md)


[下一篇](Predefined%20Exceptions.md) [上一篇](Nesting%20Exception%20Handlers.md)

# 未捕获的异常

如果异常未被捕获，它会被一个称为“未捕获异常处理器”的函数截获。未捕获异常处理器始终会使程序退出，但可以在退出前执行某些任务。

默认的未捕获异常处理器会在退出程序前向控制台记录一条消息。在 OS X 上，如果应用程序从 shell 启动，日志消息会发送到“终端”窗口。

你可以使用 [NSSetUncaughtExceptionHandler](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSSetUncaughtExceptionHandler) 函数将自定义函数设为未捕获异常处理器；还可以使用 [NSGetUncaughtExceptionHandler](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSGetUncaughtExceptionHandler) 函数获取当前的未捕获异常处理器。

[下一篇](Predefined%20Exceptions.md) [上一篇](Nesting%20Exception%20Handlers.md)
