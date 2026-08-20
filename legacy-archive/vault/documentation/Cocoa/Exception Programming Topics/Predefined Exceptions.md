---
title: 异常编程主题
apple_id: 10000012i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Concepts/PredefinedExceptions.html
archived_at: '2026-07-15T07:15:37.910604Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [异常编程主题](Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md)


[下一篇](Controlling%20a%20Program%E2%80%99s%20Response%20to%20Exceptions.md) [上一篇](Uncaught%20Exceptions.md)

# 预定义异常

Cocoa 预定义了多个通用异常名称，用于标识可在自己的代码中处理、甚至可以引发和重新引发的异常。你还可以创建和使用自定义异常名称。通用异常名称是在 `NSException.h` 中定义的字符串常量，并记录在《[Foundation 常量参考](https://developer.apple.com/documentation/foundation/foundation_constants)》中。这些常量包括：

- `NSGenericException`
- `NSRangeException`
- `NSInvalidArgumentException`
- `NSInternalInconsistencyException`
- `NSObjectInaccessibleException`
- `NSObjectNotAvailableException`
- `NSDestinationInvalidException`
- `NSPortTimeoutException`
- `NSInvalidSendPortException`
- `NSInvalidReceivePortException`
- `NSPortSendException`
- `NSPortReceiveException`

除通用异常名称外，Cocoa 的一些子系统还定义了自己的异常名称，例如 `NSInconsistentArchiveException` 和 `NSFileHandleOperationException`。这些名称同样记录在《[Foundation 常量参考](https://developer.apple.com/documentation/foundation/foundation_constants)》中。

可以在异常处理器中将异常名称与这些预定义名称比较，以识别捕获到的异常。随后，你可以处理该异常；如果该异常不是所关注的类型，则可以重新引发它。请注意，所有预定义异常都以“NS”为前缀，因此创建新异常名称时应避免使用相同前缀。

[下一篇](Controlling%20a%20Program%E2%80%99s%20Response%20to%20Exceptions.md) [上一篇](Uncaught%20Exceptions.md)
