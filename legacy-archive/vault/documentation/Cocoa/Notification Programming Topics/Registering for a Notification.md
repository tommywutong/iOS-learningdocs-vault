---
title: 通知编程主题
apple_id: 10000043i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2009-08-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Articles/Registering.html
archived_at: '2026-07-15T07:17:17.019997Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [通知编程主题](Introduction.md)


[下一页](Posting%20a%20Notification.md)[上一页](Notification%20Queues.md)

# 注册通知

你可以注册来自你自己应用内部或其他应用的通知。前者请参阅[注册本地通知](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdgljzha2dqmi)，后者请参阅[注册分布式通知](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdgljzha2dqnq)。当你的对象被[释放](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)时，必须注销通知，相关内容请参阅[注销观察者](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdgljzha4dinq)。

你可以通过调用通知中心的 `addObserver:selector:name:object:` 方法来注册一个对象以接收通知，其中要指定观察者、通知中心应发送给观察者的[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)、它想要接收的通知名称，以及关注哪个对象。你不必同时指定名称和对象。如果只指定对象，观察者将收到所有包含该对象的通知。如果只指定通知名称，那么每次该通知发布时观察者都会收到它，而不管与之关联的对象是什么。

观察者可以注册为对同一通知接收多条消息。在这种情况下，观察者将收到它为该通知注册接收的所有消息，但接收这些消息的顺序无法确定。

如果你后来决定某个观察者不再需要接收通知（例如，观察者即将被释放），可以使用 `removeObserver:` 或 `removeObserver:name:object:` 方法将该观察者从通知中心的观察者列表中移除。

通常，你会向进程的默认通知中心注册对象。你可以使用 `defaultCenter` 类[方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)获取默认对象。

作为使用通知中心接收通知的示例，假设你想在任意窗口成为主窗口（main window）时执行某项操作（例如，你正在为一个检查器面板实现[控制器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)）。你可以像下面的示例那样，将你的客户端对象注册为观察者：

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
    selector:@selector(aWindowBecameMain:)
    name:NSWindowDidBecomeMainNotification object:nil];
```

通过将 `nil` 作为要观察的对象传入，当任何对象发布 [NSWindowDidBecomeMainNotification](https://developer.apple.com/documentation/appkit/nswindow/1419448-didbecomemainnotification) 通知时，客户端对象（`self`）都会收到通知。

当窗口成为主窗口时，它会向通知中心发布一条 `NSWindowDidBecomeMainNotification`。通知中心通过调用观察者在 `addObserver:selector:name:object:` 的 [selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) 参数中指定的方法，来通知所有对该通知感兴趣的观察者。在我们这个示例观察者中，选择器是 `aWindowBecameMain:`。`aWindowBecameMain:` 方法可能具有如下的实现：

```objc
- (void)aWindowBecameMain:(NSNotification *)notification {

    NSWindow *theWindow = [notification object];
    MyDocument = (MyDocument *)[[theWindow windowController] document];

    // Retrieve information about the document and update the panel.
}
```

`NSWindow` 对象不需要了解你的检查器面板的任何信息。

对象通过向 `NSDistributedNotificationCenter` 对象发送 `addObserver:selector:name:object:suspensionBehavior:` 方法，将自己注册为通知的接收者，其中要指定通知应发送的[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)、它想要接收的通知名称、要匹配的标识字符串（_object_ 参数），以及通知递送被挂起时应遵循的行为。

因为发布对象和观察者可能位于不同的进程中，通知无法包含指向任意对象的指针。因此，`NSDistributedNotificationCenter` 类要求通知使用 `NSString` 对象作为 _object_ 参数。通知的匹配基于该字符串，而不是对象指针。你应当查阅发布通知的对象的文档，看它使用什么作为其标识字符串。

当一个进程不再希望立即接收通知时，它可以挂起通知递送。这通常在应用被隐藏或置于后台时进行。（当应用不处于活跃状态时，`NSApplication` 对象会自动挂起递送。）`addObserver` 方法中的 _suspensionBehavior_ 参数标识在递送被挂起期间应如何处理到达的通知。共有四种不同类型的挂起行为，各自适用于不同的场景。

| 挂起行为 | 说明 |
| --- | --- |
| `NSNotificationSuspensionBehaviorDrop` | 在收到 `setSuspended:NO` 消息之前，服务器不会将任何具有该名称和对象的通知入队。 |
| `NSNotificationSuspensionBehaviorCoalesce` | 服务器只将指定名称和对象的最后一条通知入队；较早的通知会被丢弃。在挂起行为不是显式参数的便捷方法中，`NSNotificationSuspensionBehaviorCoalesce` 是默认值。 |
| `NSNotificationSuspensionBehaviorHold` | 服务器保留所有匹配的通知，直到队列被填满（队列大小由服务器决定），此时服务器可能会冲刷已入队的通知。 |
| `NSNotificationSuspensionBehaviorDeliverImmediately` | 无论服务器是否收到过 `setSuspended:YES` 消息，它都会递送与该注册匹配的通知。当一条具有此挂起行为的通知被匹配时，其效果是首先冲刷所有已入队的通知。其效果相当于：在应用处于挂起状态时服务器收到了 `setSuspended:NO`，随后递送该通知，然后再转换回先前的挂起或未挂起状态。 |

你可以通过向分布式通知中心发送 `setSuspended:YES` 来挂起通知。在通知被挂起期间，通知服务器会按照观察者在注册接收通知时指定的挂起行为，来处理发往该进程的通知。当进程恢复通知递送时，所有已入队的通知会立即被递送。在使用 Application Kit 的应用中，当应用不处于活跃状态时，`NSApplication` 对象会自动挂起通知递送。

请注意，发往以 `NSNotificationSuspensionBehaviorDeliverImmediately` 注册的观察者的通知，在递送时会自动冲刷队列，导致所有已入队的通知也在那时一并被递送。

挂起状态可以被通知的发布者覆盖。如果通知很紧急，例如服务器即将关闭的警告，发布者可以通过以 _deliverImmediately_ 参数为 `YES` 调用 `NSDistributedNotificationCenter postNotificationName:object:userInfo:deliverImmediately:` 方法发布通知，强制通知立即递送给所有观察者。

在观察通知的对象被[释放](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)之前，它必须告知通知中心停止向它发送通知。否则，下一条通知将被发送给一个已不存在的对象，程序会崩溃。你可以发送以下消息，将对象完全移除为本地通知的观察者，而不管它为多少对象和通知注册过自己：

```objc
[[NSNotificationCenter defaultCenter] removeObserver:self];
```

对于分布式通知的观察者，发送：

```objc
[[NSDistributedNotificationCenter defaultCenter] removeObserver:self];
```

使用指定通知名称和被观察对象的、更具体的 `removeObserver...` 方法，可以有选择地为特定通知注销对象。

[下一页](Posting%20a%20Notification.md)[上一页](Notification%20Queues.md)
