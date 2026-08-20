---
title: 异常编程主题
apple_id: 10000012i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Articles/Exceptions64Bit.html
archived_at: '2026-07-15T07:15:36.903945Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [异常编程主题](Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md)


[下一篇](Document%20Revision%20History.md) [上一篇](Controlling%20a%20Program%E2%80%99s%20Response%20to%20Exceptions.md)

# 64 位可执行文件中的异常

Objective-C 运行时为 64 位可执行文件重新实现了异常机制，以提供零开销 `@try` 块以及与 C++ 异常的互操作性。

64 位进程进入零开销 `@try` 块时不会产生性能损失。这与 32 位进程的机制不同，后者会调用 `setjmp()` 并执行额外的“簿记”工作。不过，在 64 位可执行文件中抛出异常的开销要高得多。为了在 64 位环境中获得最佳性能，只应在绝对必要时抛出异常。

在 64 位进程中，Objective-C 异常（[NSException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/cl/NSException)）与 C++ 异常可以互操作。具体而言，异常机制展开异常时，会正确执行 C++ 析构函数和 Objective-C `@finally` 块。此外，默认捕获子句，即 `catch(...)` 和 `@catch(...)`，可以捕获并重新抛出任何异常。

另一方面，接收动态类型异常对象的 Objective-C 捕获子句（`@catch(id exception)`）可以捕获任何 Objective-C 异常，但无法捕获 C++ 异常。因此，为实现互操作性，应使用 `@catch(...)` 捕获所有异常，并使用 `@throw;` 重新抛出捕获到的异常。在 32 位环境中，`@catch(...)` 与 `@catch(id exception)` 的效果相同。

[下一篇](Document%20Revision%20History.md) [上一篇](Controlling%20a%20Program%E2%80%99s%20Response%20to%20Exceptions.md)
