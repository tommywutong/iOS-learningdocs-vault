---
title: 通知编程主题
apple_id: 10000043i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2009-08-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Articles/Posting.html
archived_at: '2026-07-15T07:17:17.012015Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [通知编程主题](Introduction.md)


[下一页](Delivering%20Notifications%20To%20Particular%20Threads.md)[上一页](Registering%20for%20a%20Notification.md)

# 发布通知

你可以在自己的应用内部发布通知，也可以让通知对其他应用可用。前者请参阅[发布本地通知](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdiljzg43daoi)，后者请参阅[发布分布式通知](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdiljzg42donq)。

你可以用 `notificationWithName:object:` 或 `notificationWithName:object:userInfo:` 来[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)通知对象，然后使用 `postNotification:` 实例方法将通知对象发布到通知中心。`NSNotification` 对象是[不可变的](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)，因此一旦创建就无法修改。

不过，通常你不会直接创建自己的通知。`NSNotificationCenter` 类的 `postNotificationName:object:` 和 `postNotificationName:object:userInfo:` 方法让你无需先创建通知即可方便地发布通知。

在每种情况下，你通常会将通知发布到进程的默认通知中心。你可以使用 `defaultCenter` [类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)获取默认对象。

作为使用通知中心发布通知的示例，考虑[注册本地通知](Registering%20for%20a%20Notification.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdgljzha2dqmi)中的例子。你有一个可以对文本执行多种转换（例如从 RTF 转为 ASCII）的程序。这些转换由一类对象（`Converter`）处理，它们可以在程序运行期间被添加或移除。你的程序中可能有其他对象希望在转换器被添加或移除时收到通知，但 `Converter` 对象不需要知道这些对象是谁、它们做什么。因此你声明两个通知：`"ConverterAdded"` 和 `"ConverterRemoved"`，并在相应事件发生时发布它们。

当用户安装或移除一个转换器时，它会向通知中心发送以下[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)之一：

```objc
[[NSNotificationCenter defaultCenter]
    postNotificationName:@"ConverterAdded" object:self];
```

或者：

```objc
[[NSNotificationCenter defaultCenter]
    postNotificationName:@"ConverterRemoved" object:self];
```

通知中心随后会找出哪些对象（如果有的话）对这些通知感兴趣，并通知它们。

如果观察者还关注其他对象（除了通知名称和被观察对象之外），可以将它们放入通知的可选字典中，或者使用 `postNotificationName:object:userInfo:`。

发布分布式通知与发布本地通知大体相同。你可以手动[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一个 `NSNotification` 对象并用 `postNotification:` 发布，也可以使用 `NSDistributedNotificationCenter` 的便捷方法之一。唯一的区别是：通知对象必须是一个字符串对象，且可选的 user-info 字典只能包含[属性列表](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44)对象，例如 `NSString` 和 `NSNumber`。

给定通知的观察者可能处于挂起状态，不会立即处理通知。如果发布通知的对象想要确保所有观察者立即收到通知（例如，当通知是服务器即将关闭的警告时），它可以用 _deliverImmediately:YES_ 调用 `postNotificationName:object:userInfo:deliverImmediately:`。通知中心会像观察者以 `NSNotificationSuspensionBehaviorDeliverImmediately` 注册那样递送该通知（详见[注册分布式通知](Registering%20for%20a%20Notification.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdgljzha2dqnq)）。不过，递送并不能得到保证。例如，接收通知的进程可能太忙，无法处理和接受已入队的通知。在这种情况下，通知会被丢弃。

[下一页](Delivering%20Notifications%20To%20Particular%20Threads.md)[上一页](Registering%20for%20a%20Notification.md)
