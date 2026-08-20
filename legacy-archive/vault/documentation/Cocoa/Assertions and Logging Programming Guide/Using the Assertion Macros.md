---
title: 断言与日志编程指南
apple_id: 10000014i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Assertions/Tasks/AssertMacros.html
archived_at: '2026-07-15T05:25:47.160641Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [断言与日志编程指南](Introduction%20to%20Assertions%20and%20Logging.md)


[下一页](Logging%20Messages.md)[上一页](How%20Assertions%20Work.md)

# 使用断言宏

本文档介绍如何使用 `Assert`（及相关）宏来对条件求值并创建断言。

你可以使用一系列宏来对条件求值——这些宏作为 NSAssertionHandler 的前端而存在。这些宏分为两类：一类用于 Objective-C 方法中，另一类用于 C 函数中。例如，`NSAssert` 用于方法内，`NSCAssert` 用于函数内。每个宏都有两个参数：条件（一个求值为真或假的表达式），以及描述失败原因的 NSString。如果 `printf` 风格的描述需要一个或多个参数，则可以使用其他宏。例如，如果需要一个参数，就在方法中使用 `NSAssert1`，如下所示：

```objc
NSAssert1((0 <= component) && (component <= 255),
        @"Value %i out of range!", component);
```

有关这些宏的更多详情，请参阅 [NSAssert](https://developer.apple.com/documentation/foundation/nsassert)。

你只应使用上述宏来创建断言——你很少需要直接调用 NSAssertionHandler 的方法。用于方法和函数内部的宏，会分别向当前断言处理器发送 `handleFailureInMethod:object:file:lineNumber:description:` 和 `handleFailureInFunction:file:lineNumber:description:` 消息。当前线程的断言处理器可通过 NSAssertionHandler 的 `currentHandler` 类方法获取。

如果定义了预处理宏 `NS_BLOCK_ASSERTIONS`，断言就不会被编译进代码。

[下一页](Logging%20Messages.md)[上一页](How%20Assertions%20Work.md)

