---
title: 断言与日志编程指南
apple_id: 10000014i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Assertions/Tasks/LoggingMessages.html
archived_at: '2026-07-15T05:25:47.811187Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [断言与日志编程指南](Introduction%20to%20Assertions%20and%20Logging.md)


[下一页](Using%20a%20Custom%20Assertion%20Handler.md)[上一页](Using%20the%20Assertion%20Macros.md)

# 记录日志消息

你可以使用 `NSLog` 和 `NSLogv` 函数来记录错误和提示性消息。这些消息会被写入 `stderr`。

该消息由一个时间戳和进程 ID 作为前缀，附加在你传入的字符串之前组成。你可以通过一个格式字符串与一个或多个要插入其中的参数来组合出这个字符串。这些函数所支持的格式说明符，是 NSString 格式化能力所理解的那一套（不一定与 `printf` 所理解的格式转义符和标志集合相同）。例如，以下代码片段输出了一个由 NSString 和 `int` 参数构造而成的字符串。

```objc
int recNum;
NSString *recName;
/* ... */
NSLog( @"Record %d is %@", recNum, recName );
```

有关各种格式说明符的说明，请参阅 [格式化字符串对象](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943)。

一般来说，你应该使用 `NSLog` 函数，而不是直接调用 `NSLogv`。如果你确实要直接调用 `NSLogv`，则必须先调用标准 C 宏 `va_start` 准备好所需的可变参数列表。使用完毕后，你必须同样调用标准 C 宏 `va_end` 来结束该列表。

[下一页](Using%20a%20Custom%20Assertion%20Handler.md)[上一页](Using%20the%20Assertion%20Macros.md)

