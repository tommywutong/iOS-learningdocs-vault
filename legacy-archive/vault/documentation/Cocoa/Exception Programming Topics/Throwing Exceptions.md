---
title: 异常编程主题
apple_id: 10000012i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Tasks/RaisingExceptions.html
archived_at: '2026-07-15T07:15:41.932270Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [异常编程主题](Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md)


[下一篇](Nesting%20Exception%20Handlers.md) [上一篇](Handling%20Exceptions.md)

# 抛出异常

程序检测到异常后，必须将异常传播给处理它的代码。这段代码称为异常处理器。传播异常的整个过程称为“抛出异常”（或“引发异常”）。要抛出（或引发）异常，需实例化一个 [NSException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/cl/NSException) 对象，然后对其执行以下两种操作之一：

- 将其用作 `@throw` 编译器指令的参数
- 向其发送 [raise](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/instm/NSException/raise) 消息

以下示例展示了如何使用 `@throw` 指令抛出异常（注释中给出了等效的 `raise` 方式）：

```objc
NSException* myException = [NSException
        exceptionWithName:@"FileNotFoundException"
        reason:@"File Not Found on System"
        userInfo:nil];
@throw myException;
// [myException raise]; /* 等同于上面的指令 */
```

`@throw` 与 `raise` 的一个重要区别是，后者只能发送给 `NSException` 对象，而 `@throw` 可以接受其他类型的对象作为参数（例如字符串对象）。Cocoa 应用程序应仅使用 `@throw` 抛出 `NSException` 对象。

通常，应在异常处理域内抛出或引发异常；异常处理域是由 `@try` 编译器指令标记的代码块。

有关详情，请参阅[处理异常](Handling%20Exceptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga2tslktk4yq)。

在异常处理域中，可以将局部异常处理器捕获的异常重新传播给更高层级的处理器，方法是再次向 `NSException` 对象发送 `raise` 消息，或通过另一条 `@throw` 指令使用该对象。请注意，在 `@catch` 异常处理块中，可以不显式指定异常对象而重新抛出异常，如下例所示：

```objc
@try {
    NSException *e = [NSException
        exceptionWithName:@"FileNotFoundException"
        reason:@"File Not Found on System"
        userInfo:nil];
    @throw e;
}
@catch(NSException *e) {
    @throw; // 隐式重新抛出 e
}
```

重新抛出的异常涉及一种微妙的行为：在 `@throw` 导致调用更高一层的异常处理器之前，会先执行与局部 `@catch` 异常处理器关联的 `@finally` 块。从某种意义上说，`@finally` 块会作为 `@throw` 语句的提前副作用而执行。这一行为会影响[内存管理](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)（请参阅[异常处理与内存管理](Handling%20Exceptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga2tslktk43q)）。

[下一篇](Nesting%20Exception%20Handlers.md) [上一篇](Handling%20Exceptions.md)
