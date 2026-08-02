---
title: 通知编程主题
apple_id: 10000043i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2009-08-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Articles/Notifications.html
archived_at: '2026-07-15T07:17:17.005178Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [通知编程主题](Introduction.md)


[下一页](Notification%20Centers.md)[上一页](Introduction.md)

# 通知

_通知_封装了有关某个事件的信息，例如窗口获得焦点或网络连接关闭。需要知晓某个事件的对象（例如，需要知道其窗口即将关闭的文件）会向通知中心注册，表明它希望在该事件发生时收到通知。当事件确实发生时，通知会被发布到通知中心，通知中心随即将通知立即广播给所有已注册的对象。通知也可以选择放入通知队列中排队，由通知队列在延迟指定的通知、并按照你指定的条件将相似通知合并之后，再将通知发布到通知中心。

在对象之间传递信息的标准方式是[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)传递——一个对象调用另一个对象的方法。然而，消息传递要求发送消息的对象知道接收者是谁、它能响应哪些消息。有时，这种两个对象之间的紧密耦合并不理想——最显著的原因是它会把两个本来相互独立的子系统捆绑在一起。针对这类情况，引入了一种广播模型：对象发布一条通知，该通知通过一个 `NSNotificationCenter` 对象（简称通知中心）分发给相应的观察者。

一个 `NSNotification` 对象（即通知）包含一个名称、一个对象和一个可选的字典。名称是标识该通知的标签。对象是通知的发布者想要发送给该通知观察者的任意对象——通常就是发布通知的对象本身。字典可以包含有关事件的附加信息。

任何对象都可以发布通知。其他对象可以向通知中心注册为观察者，以便在通知发布时接收它们。通知中心负责把通知广播给已注册的观察者（如果有的话）。发布通知的对象、通知中包含的对象以及通知的观察者可以是不同的对象，也可以是同一个对象。发布通知的对象无需了解观察者的任何信息。另一方面，观察者至少需要知道通知的名称，以及字典（如果提供）中的键。

使用通知系统与使用[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)（delegation）类似，但有以下区别：

- 可以有任意数量的对象接收通知，而不仅限于委托对象。这意味着无法返回值。
- 对象可以从通知中心接收任意你指定的[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)，而不仅限于预定义的委托方法。
- 发布通知的对象甚至不需要知道观察者的存在。

[下一页](Notification%20Centers.md)[上一页](Introduction.md)
