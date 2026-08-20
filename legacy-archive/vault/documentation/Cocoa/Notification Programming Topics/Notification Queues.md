---
title: 通知编程主题
apple_id: 10000043i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2009-08-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Articles/NotificationQueues.html
archived_at: '2026-07-15T07:17:16.996887Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [通知编程主题](Introduction.md)


[下一页](Registering%20for%20a%20Notification.md)[上一页](Notification%20Centers.md)

# 通知队列

`NSNotificationQueue` 对象（简称_通知队列_）充当通知中心（`NSNotificationCenter` 的实例）的缓冲区。`NSNotificationQueue` 类为 Foundation Kit 的通知机制贡献了两个重要特性：通知的合并（coalescing）和异步发布。

使用 `NSNotificationCenter` 的 [postNotification:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/instm/NSNotificationCenter/postNotification:) 方法及其变体，你可以将通知发布到通知中心。然而，该方法的调用是同步的：发布对象必须等到通知中心将通知派发给所有观察者并返回之后，才能继续执行其线程。而通知队列则以通常的先进先出（FIFO）顺序保存通知（`NSNotification` 的实例）。当通知到达队列前端时，队列将其发布到通知中心，通知中心再把通知派发给所有注册为观察者的对象。

每个线程都有一个默认通知队列，它与进程的默认通知中心相关联。你也可以[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)自己的通知队列，每个中心和每个线程都可以拥有多个队列。

使用 `NSNotificationQueue` 的 [enqueueNotification:postingStyle:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationQueue/Description.html#//apple_ref/occ/instm/NSNotificationQueue/enqueueNotification:postingStyle:) 和 [enqueueNotification:postingStyle:coalesceMask:forModes:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationQueue/Description.html#//apple_ref/occ/instm/NSNotificationQueue/enqueueNotification:postingStyle:coalesceMask:forModes:) 方法，你可以通过将通知放入队列，在当前线程上异步发布通知。这些方法在将通知放入队列后会立即返回到调用对象。

通知队列的清空以及其中通知的发布，取决于入队方法中指定的发布样式（posting style）和运行循环模式。mode 参数指定队列将在哪种运行循环模式下被清空。例如，如果你指定 `NSModalPanelRunLoopMode`，通知只会在运行循环处于该模式时被发布。如果运行循环当前不在该模式下，通知会一直等待，直到下次进入该模式。更多信息请参阅[运行循环模式](../Threading%20Programming%20Guide/Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknltcmq)。

向通知队列发布通知可以使用三种不同的样式：`NSPostASAP`、`NSPostWhenIdle` 和 `NSPostNow`。以下各节将对这些样式进行说明。

以 `NSPostASAP` 样式排入队列的任何通知，都会在当前这一轮运行循环结束时被发布到通知中心——前提是当前的运行循环模式与请求的模式一致。（如果请求的模式与当前模式不同，通知会在进入请求的模式时发布。）由于运行循环在每轮迭代中可能进行多次调出（callout），通知不一定会当前调出一退出、控制权返回运行循环时就立刻递送——其他调出可能会先发生，例如定时器或输入源触发，或者其他异步通知被递送。

`NSPostASAP` 发布样式通常用于开销较大的资源，例如显示服务器（display server）。当许多客户端在运行循环的一次调出期间往窗口缓冲区上绘制时，每次绘制操作后都将缓冲区刷新到显示服务器的开销很大。在这种情况下，每个 `draw...` 方法都会入队一条诸如 “FlushTheServer” 的通知，指定按名称和对象合并，并使用 `NSPostASAP` 发布样式。这样，运行循环结束时只会派发其中一条通知，窗口缓冲区也只会被刷新一次。

以 `NSPostWhenIdle` 样式排入队列的通知，只会在运行循环处于等待状态时被发布。在该状态下，运行循环的输入通道中没有任何内容，无论是定时器还是其他异步事件。使用 `NSPostWhenIdle` 样式排队的一个典型例子是：当用户输入文本时，程序在某处显示文本的字节大小。在用户每输入一个字符后就更新文本大小，开销会非常大（而且没什么用），尤其是用户输入很快的时候。在这种情况下，程序会在每次输入字符后入队一条诸如 “ChangeTheDisplayedSize” 的通知，开启合并并使用 `NSPostWhenIdle` 发布样式。当用户停止输入时，队列中那条唯一的 “ChangeTheDisplayedSize” 通知（因为合并）会在运行循环进入等待状态时被发布，显示随之更新。注意，即将退出的运行循环（当其所有输入通道都已失效时会发生）并不处于等待状态，因此不会发布通知。

以 `NSPostNow` 排入队列的通知会在合并之后立即发布到通知中心。当你不需要异步调用行为时，可以用 `NSPostNow` 入队通知（或者用 [postNotification:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/instm/NSNotificationCenter/postNotification:) 发布）。在许多编程场景中，同步行为不仅是允许的，而且是可取的：你希望通知中心在派发完成后才返回，以便确定观察对象已经接收并处理了通知。当然，当队列中存在你希望通过合并来移除的相似通知时，应当使用带 `NSPostNow` 的 `enqueueNotification...`，而不是使用 `postNotification:`。

在某些情况下，你可能希望在某个事件至少发生一次时发布一条通知，但即使该事件发生了多次，也最多只发布一条通知。例如，在一个以离散数据包接收数据的应用中，你可能希望在收到一个数据包时发布一条通知，表示数据需要处理。然而，如果在给定的时间段内到达多个数据包，你不希望发布多条通知。而且，发布这些通知的对象可能无法得知是否还有更多数据包即将到来，也无法得知发布方法是否会在循环中被调用。

在某些情况下，可以简单地设置一个布尔标志（无论是对象的实例变量还是全局变量），表示事件已经发生，并在标志被清除之前阻止发布后续通知。但如果做不到这一点，在这种情况下你就不能直接使用 `NSNotificationCenter`，因为它的行为是同步的——通知在返回之前就会被发布，因此没有机会“忽略”重复的通知；而且 `NSNotificationCenter` 实例也无法得知是否还有更多通知即将到来。

因此，与其将通知发布到通知中心，不如将通知添加到 `NSNotificationQueue` 实例中，并指定适当的_合并_（coalescing）选项。合并是一个过程，它会从队列中移除与之前已入队的某条通知在某种程度上相似的通知。你通过在 [enqueueNotification:postingStyle:coalesceMask:forModes:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationQueue/Description.html#//apple_ref/occ/instm/NSNotificationQueue/enqueueNotification:postingStyle:coalesceMask:forModes:) 方法的第三个参数中指定以下一个或多个常量，来表明相似性的判定标准。

|  |  |
| --- | --- |
| [NSNotificationNoCoalescing](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSNotificationNoCoalescing) |  |
| [NSNotificationCoalescingOnName](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSNotificationCoalescingOnName) |  |
| [NSNotificationCoalescingOnSender](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSNotificationCoalescingOnSender) |  |

你可以对 `NSNotificationCoalescingOnName` 和 `NSNotificationCoalescingOnSender` 常量执行按位或（bitwise-OR）运算，以同时按通知名称和通知对象进行合并。下面的示例说明了如何使用队列来确保：在给定的事件循环周期内，所有名为 `MyNotificationName` 的通知都被合并为一条通知。

```objc
// MyNotificationName defined globally
NSString *MyNotificationName = @"MyNotification";

id object = <#The object associated with the notification#>;
NSNotification *myNotification =
        [NSNotification notificationWithName:MyNotificationName object:object]
[[NSNotificationQueue defaultQueue]
        enqueueNotification:myNotification
        postingStyle:NSPostWhenIdle
        coalesceMask:NSNotificationCoalescingOnName
        forModes:nil];
```

[下一页](Registering%20for%20a%20Notification.md)[上一页](Notification%20Centers.md)
