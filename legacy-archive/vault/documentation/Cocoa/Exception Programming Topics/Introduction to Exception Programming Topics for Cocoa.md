---
title: 异常编程主题
apple_id: 10000012i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Exceptions.html
archived_at: '2026-07-15T07:15:38.417010Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一篇](Exceptions%20and%20the%20Cocoa%20Frameworks.md)

# Cocoa 异常编程主题简介

本文档讨论如何抛出和处理异常，即中断程序正常执行流程的特殊状况。用于异常处理的 Objective-C 指令和 Foundation API 可在 iOS 和 OS X 上使用。

对于 Cocoa 应用程序中的预期错误，建议使用错误对象（[NSError](https://developer.apple.com/documentation/foundation/nserror)）和 Cocoa 错误传递机制来传达，而不是使用异常。有关更多信息，请参阅《[错误处理编程指南](../Error%20Handling%20Programming%20Guide/Introduction%20to%20Error%20Handling%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbw)》。

本文档包含以下文章：

- [异常与 Cocoa 框架](Exceptions%20and%20the%20Cocoa%20Frameworks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tanbvfvjvomi)介绍 `NSException` 对象及其在 Cocoa 框架中的常规用法。
- [处理异常](Handling%20Exceptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga2tslkcijbuqr2kjffa)介绍如何使用编译器指令 `@try`、`@catch` 和 `@finally` 处理异常。
- [抛出异常](Throwing%20Exceptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga2tqlkcijbugrsjijda)介绍如何抛出（引发）异常。
- [嵌套异常处理器](Nesting%20Exception%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga3dalkdjjbeersejfda)介绍异常处理器的嵌套方式。
- [预定义异常](Predefined%20Exceptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga2tolkcineuoscfinaq)介绍在何处查找 Cocoa 定义的异常。
- [未捕获的异常](Uncaught%20Exceptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga2tmlkciffeirchi5ca)介绍异常未被异常处理器捕获时会发生什么。
- [控制程序对异常的响应](Controlling%20a%20Program%E2%80%99s%20Response%20to%20Exceptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq3tglkcijbuqr2kjffa)介绍如何使用 Exception Handling 框架监控和控制 Cocoa 程序响应各类异常的行为。
- [64 位可执行文件中的异常](Exceptions%20in%2064-Bit%20Executables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tanbufvjvomi)介绍零开销 `@try` 块以及 64 位可执行文件中的 C++ 互操作性。

有关产生、处理预期运行时错误以及从中恢复的信息，请参阅《[错误处理编程指南](../Error%20Handling%20Programming%20Guide/Introduction%20to%20Error%20Handling%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbw)》。另请参阅相关文档《[断言与日志记录编程指南](../Assertions%20and%20Logging%20Programming%20Guide/Introduction%20to%20Assertions%20and%20Logging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayti2i)》，了解 Foundation 框架对创建断言和记录错误信息的支持。

[下一篇](Exceptions%20and%20the%20Cocoa%20Frameworks.md)
