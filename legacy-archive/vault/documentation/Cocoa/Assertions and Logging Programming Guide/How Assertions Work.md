---
title: 断言与日志编程指南
apple_id: 10000014i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Assertions/Concepts/HowAssertionsWork.html
archived_at: '2026-07-15T05:25:46.142928Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [断言与日志编程指南](Introduction%20to%20Assertions%20and%20Logging.md)


[下一页](Using%20the%20Assertion%20Macros.md)[上一页](Introduction%20to%20Assertions%20and%20Logging.md)

# 断言的工作原理

在代码中，你使用断言宏来创建断言。这些宏会对某个条件求值，如果条件求值为假，就会将一个描述失败原因的字符串（可能还包括格式化到该字符串中的其他 `printf` 风格参数）传递给它们的 NSAssertionHandler。每个线程都有自己创建的一个 NSAssertionHandler 对象。当以断言方式被调用时，NSAssertionHandler 会打印一条错误消息，其中包含包含该断言的方法与类（或函数），然后引发一个 `NSInternalInconsistencyException`。

[下一页](Using%20the%20Assertion%20Macros.md)[上一页](Introduction%20to%20Assertions%20and%20Logging.md)

