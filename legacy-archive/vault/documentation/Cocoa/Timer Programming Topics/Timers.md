---
title: 定时器编程主题
apple_id: 10000061i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2009-07-14'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Timers/Articles/timerConcepts.html
archived_at: '2026-07-15T07:20:40.251675Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [定时器编程主题](Introduction%20to%20Timers.md)


[下一页](Using%20Timers.md)[上一页](Introduction%20to%20Timers.md)

# 定时器

定时器（timer）要与 `NSRunLoop` 对象配合工作。因此，它们并不提供实时机制——其精度是有限的。如果你只是想在将来的某个时刻发送一条消息，不用定时器也能做到。

定时器由 `NSTimer` 对象表示。它们要与 `NSRunLoop` 对象配合工作。`NSRunLoop` 对象控制着等待输入的循环，它们借助定时器来确定自己最多应该等待多长时间。当定时器的时限到了之后，运行循环（run loop）就会触发（fire）该定时器（从而发出它的消息），然后再检查是否有新的输入。

只有当你注册定时器所用的那个运行循环模式正在运行时，定时器才会触发。对于用 Application Kit 或 UIKit 构建的应用程序，应用程序对象会替你运行主线程的运行循环。但在辅助线程上，你必须自己运行运行循环——详见 _[运行循环](../Run%20Loops/Introduction%20to%20Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3de2i)_。

每个运行循环定时器同一时间只能注册到一个运行循环中，不过在该运行循环内，它可以被添加到多个运行循环模式里。

定时器不是实时机制；只有当定时器所添加到的某个运行循环模式正在运行、并且有机会检查定时器的触发时间是否已过时，它才会触发。由于典型的运行循环要管理各式各样的输入源，定时器时间间隔的有效分辨率被限制在 50-100 毫秒这个量级。如果定时器的触发时间恰好落在运行循环处于某个并不监视该定时器的模式期间，或者落在一次长时间的回调过程中，那么定时器要等到运行循环下一次检查它时才会触发。因此，定时器实际触发的时间有可能远远晚于计划的触发时间。

重复定时器是按照计划的触发时间、而不是实际的触发时间来重新安排自己的下一次触发。例如，如果某个定时器被安排在某一时刻触发、此后每隔 5 秒触发一次，那么即使实际触发时间被推迟了，计划的触发时间也始终落在最初那些 5 秒的时间点上。如果触发时间延迟得太久，以至于跳过了一个或多个计划的触发时间，那么定时器在那段时间内只触发一次；触发之后，定时器会被重新安排到将来下一个计划的触发时间。

如果你只是想在将来的某个时刻发送一条消息，不用定时器也能做到。你可以使用 [performSelector:withObject:afterDelay:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/performSelector:withObject:afterDelay:) 及相关方法，直接在另一个对象上调用某个方法。某些变体（例如 [performSelectorOnMainThread:withObject:waitUntilDone:](https://developer.apple.com/documentation/objectivec/nsobject/1414900-performselector)）允许你在特定的线程上调用该方法。你也可以使用 [cancelPreviousPerformRequestsWithTarget:](https://developer.apple.com/documentation/objectivec/nsobject/1417611-cancelpreviousperformrequests) 及相关方法来取消一次延迟的消息发送。

[下一页](Using%20Timers.md)[上一页](Introduction%20to%20Timers.md)

