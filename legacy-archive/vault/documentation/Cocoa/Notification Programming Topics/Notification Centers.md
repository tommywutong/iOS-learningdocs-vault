---
title: 通知编程主题
apple_id: 10000043i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2009-08-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Articles/NotificationCenters.html
archived_at: '2026-07-15T07:17:16.989260Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [通知编程主题](Introduction.md)


[下一页](Notification%20Queues.md)[上一页](Notifications.md)

# 通知中心

_通知中心_管理通知的发送和接收。它会将满足特定条件的通知告知所有观察者。通知信息封装在 `NSNotification` 对象中。客户端对象向通知中心注册，成为其他对象发布的特定通知的观察者。当某个事件发生时，对象会向通知中心发布相应的通知。（有关发布通知的更多信息，请参阅[发布通知](Posting%20a%20Notification.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdilkdivduurseizdq)。）通知中心向每个已注册的观察者派发一条[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)，并将通知作为唯一的参数传入。发布对象和观察对象可以是同一个对象。

[Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) 包含两种类型的通知中心：

- `NSNotificationCenter` 类管理单个进程内的通知。
- `NSDistributedNotificationCenter` 类管理同一台计算机上多个进程之间的通知。

每个进程都有一个默认通知中心，可通过 `NSNotificationCenter +defaultCenter` [类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)访问。该通知中心处理单个进程内的通知。对于同一台机器上进程之间的通信，使用分布式通知中心（参见 [NSDistributedNotificationCenter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiytmljrgeytgojr)）。

通知中心以同步方式向观察者递送通知。换句话说，发布通知时，控制权要等所有观察者都接收并处理完通知后才会返回给发布者。要以异步方式发送通知，请使用通知队列，详见[通知队列](Notification%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiytolkdjjbegrkdjjbq)。

在多线程应用中，通知总是在发布它的线程中递送，这可能与观察者注册时所在的线程不同。

每个进程都有一个默认的分布式通知中心，可通过 `NSDistributedNotificationCenter +defaultCenter` [类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)访问。该分布式通知中心处理可在单台机器上的进程之间发送的通知。对于不同机器上进程之间的通信，使用分布式对象（参见 _[分布式对象编程主题](../Distributed%20Objects%20Programming%20Topics/Introduction%20to%20Distributed%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyde2i)_）。

发布分布式通知是一项开销很大的操作。通知会被发送到一个系统级服务器，再由该服务器分发给所有有对象注册了分布式通知的进程。从发布通知到通知到达另一个进程之间的延迟是不确定的。事实上，如果发布的通知过多、服务器的队列被填满，通知可能会被丢弃。

分布式通知通过进程的运行循环（run loop）递送。进程必须以某种“通用”模式运行运行循环（例如 `NSDefaultRunLoopMode`），才能接收分布式通知。如果接收进程是多线程的，不要指望通知会到达主线程。通知通常会递送到主线程的运行循环，但其他线程也可能收到通知。

常规通知中心允许观察任意对象，而分布式通知中心仅限于观察字符串对象。因为发布对象和观察者可能位于不同的进程中，通知无法包含指向任意对象的指针。因此，分布式通知中心要求通知使用字符串作为通知对象。通知的匹配基于该字符串，而不是对象指针。

[下一页](Notification%20Queues.md)[上一页](Notifications.md)
