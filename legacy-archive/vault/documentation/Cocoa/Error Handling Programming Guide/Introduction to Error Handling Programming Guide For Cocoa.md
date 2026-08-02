---
title: 错误处理编程指南
apple_id: TP40001806
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-01-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/ErrorHandling/ErrorHandling.html
archived_at: '2026-07-15T07:15:23.624945Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Error%20Objects%2C%20Domains%2C%20and%20Codes.md)

# Cocoa 错误处理编程指南简介

每个程序都必须处理运行时出现的错误。例如，程序可能无法打开文件，也可能无法解析 XML 文档。遇到这类错误时，程序通常需要告知用户，并且有时还可以尝试绕过导致错误的问题。

[Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9)（以及 Cocoa Touch）为开发者提供了完成这些任务的编程工具：Foundation 中的 [NSError](https://developer.apple.com/documentation/foundation/nserror) 类，以及 Application Kit 中支持应用程序错误处理的新方法和机制。`NSError` 对象封装了特定错误的信息，包括错误来源域（子系统）以及在错误警告中显示的本地化字符串。应用程序还提供了一套架构，使其中的不同对象能够完善错误对象中的信息，并可能从错误中恢复。

阅读本文档可了解 `NSError` API 及其架构，以及如何使用它们。

《Cocoa 错误处理编程指南》包含以下文章：

- [错误对象、域和代码](Error%20Objects%2C%20Domains%2C%20and%20Codes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgiwugssci5ausqsk)介绍 `NSError` 对象的属性，尤其是它的域和错误代码，并讨论错误对象的“用户信息”字典中可能包含的内容，包括本地化消息字符串和底层错误。
- [使用和创建错误对象](Using%20and%20Creating%20Error%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgqwueqkkjfeuoq2d)说明如何评估错误、如何使用 `NSError` 对象显示错误消息，以及如何实现通过引用返回 `NSError` 对象的方法。
- [错误响应者与错误恢复](Error%20Responders%20and%20Error%20Recovery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgmwueqkkinbesrsd)介绍 Application Kit 架构如何沿应用程序中的对象链向上传递错误对象，让每个对象在错误呈现之前都有机会对其进行自定义；同时讨论恢复尝试器的作用——当用户请求恢复时，由它尝试从错误中恢复。
- [处理接收到的错误](Handling%20Received%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqguwueqkkiveecssd)讨论如何在错误响应者对象链中处理并自定义接收到的错误。
- [从错误中恢复](Recovering%20From%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgywueq2jircuor2g)说明尝试执行用户所请求错误恢复的过程。

与 iOS 相关的两章是[错误对象、域和代码](Error%20Objects%2C%20Domains%2C%20and%20Codes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgiwugssci5ausqsk)和[使用和创建错误对象](Using%20and%20Creating%20Error%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbwfvbuqmrqgqwueqkkjfeuoq2d)。

《[Mac 基于文档的应用编程指南](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20Mac/About%20the%20Cocoa%20Document%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzz)》中的“[文档架构支持可靠的错误处理](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20Mac/Core%20App%20Behaviors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzzfvbuqnjnknltgmq)”为重写带引用传递 [NSError](https://developer.apple.com/documentation/foundation/nserror) 参数方法的子类提供了实用建议。

《对话框类型及其使用时机》就 OS X 警告的形式和内容提供了建议。《iOS 人机界面指南》则为 iOS 警告提供了类似建议。在编写错误消息之前，应查阅这些指南。此外，还可参阅以下讨论 Cocoa 编程中错误处理及错误消息呈现相关主题的文档：

- 《[断言与日志编程指南](../Assertions%20and%20Logging%20Programming%20Guide/Introduction%20to%20Assertions%20and%20Logging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayti2i)》（两个平台）
- 《[对话框与特殊面板](../Dialogs%20and%20Special%20Panels/Introduction%20to%20Dialogs%20and%20Special%20Panels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3tc2i)》（OS X 警告）
- 《[表单编程主题](../Sheet%20Programming%20Topics/Introduction%20to%20Sheets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayde2i)》（OS X）
- 《[UIAlertView 类参考](https://developer.apple.com/documentation/uikit/uialertview)》（iOS）

《[异常编程主题](../Exception%20Programming%20Topics/Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayte2i)》讨论如何抛出和处理异常。《[Objective-C 编程语言](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)》中的[异常处理](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocExceptionHandling.html#//apple_ref/doc/uid/TP30001163-CH13)介绍了异常处理中使用的编译器指令 `@try`、`@catch`、`@throw` 和 `@finally`。

[下一页](Error%20Objects%2C%20Domains%2C%20and%20Codes.md)
