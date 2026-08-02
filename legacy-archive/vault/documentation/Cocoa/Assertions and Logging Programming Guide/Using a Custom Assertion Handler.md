---
title: 断言与日志编程指南
apple_id: 10000014i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Assertions/Tasks/UsingCustomAssertHndler.html
archived_at: '2026-07-15T05:25:48.166277Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [断言与日志编程指南](Introduction%20to%20Assertions%20and%20Logging.md)


[下一页](Document%20Revision%20History.md)[上一页](Logging%20Messages.md)

# 使用自定义断言处理器

在某些情况下，你可能希望定义自己的断言处理器，将错误消息打印到不同的错误控制台，或者引发自定义异常，而不是使用通用的 `NSInternalInconsistencyException`。要实现这些功能，你必须定义 NSAssertionHandler 的一个子类，并重写其 `handleFailureInMethod:object:file:lineNumber:description:` 和 `handleFailureInFunction:file:lineNumber:description:` 方法，分别用于处理方法和函数中的断言。

要将你的断言处理器添加到某个线程，你必须将该断言处理器添加到该线程的属性字典中。使用当前 NSThread 的 `threadDictionary` 方法来获取该字典，然后使用键 `NSAssertionHandler` 将你的断言处理器对象添加到字典中。这项技术可用于在任何线程（包括主线程）上指定自定义断言处理器。你必须在想要修改的那个线程中执行这些步骤——一个线程无法修改另一个线程的线程属性字典。

通常，你应该在创建线程后立即将断言处理器添加到线程字典中。不过，默认的断言处理器要到遇到断言宏时才会创建，并且你随时可以替换线程字典中已有的断言处理器。如果你的断言处理器已经存在于线程字典中，它就会被用来代替默认的断言处理器。

[下一页](Document%20Revision%20History.md)[上一页](Logging%20Messages.md)

