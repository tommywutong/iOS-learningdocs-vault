---
title: 定时器编程主题
apple_id: 10000061i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2009-07-14'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Timers/Timers.html
archived_at: '2026-07-15T07:20:41.250731Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Timers.md)

# 定时器简介

定时器（timer）提供了一种执行延迟动作或周期性动作的手段。定时器会一直等待，直到指定的时间间隔过去，然后触发（fire），向指定的对象发送指定的消息。例如，你可以创建一个定时器，让它在一段时间之后向某个控制器对象发送消息，通知它更新某个特定的值。

定时器要与 `NSRunLoop` 对象配合工作。因此，它们并不提供实时机制——其精度是有限的。

关于定时器的总体介绍，请参阅 [定时器](Timers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydmlkciffemqsbjfea)。

使用定时器涉及好几个方面。创建定时器时，你必须对它进行配置，让它知道触发时该向哪个对象发送哪个消息。然后你必须把它与某个运行循环（run loop）关联起来，这样它才会触发——有些创建方法会自动替你完成这一步。最后，如果你创建的是重复定时器，那么在希望它停止触发时，你必须让它失效。

要进一步了解定时器的用法，请参阅 [使用定时器](Using%20Timers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydolkdjjbeuq2circq)。

[下一页](Timers.md)

