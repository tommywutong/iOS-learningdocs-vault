---
title: Cocoa Performance Guidelines
apple_id: TP40001448
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2009-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaPerformance/Articles/Notifications.html
archived_at: '2026-07-15T07:13:18.697861Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Performance Guidelines](Introduction%20to%20Cocoa%20Performance%20Guidelines.md)


[Next](Document%20Revision%20History.md)[Previous](String%20Management.md)

# Notifications

The Cocoa [notification](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35) mechanism gives you a way of communicating changes to any number of other objects. An important feature of notifications is that the code sending the notification does not have to know anything about what is done with that notification. The interested objects decide how they want to respond, if at all.

The Cocoa frameworks use notifications to communicate important status information to your application. You can use these notifications as hooks to perform important tasks. For example, Cocoa sends the `NSApplicationDidFinishLaunchingNotification` notification to give you a chance to perform any secondary initialization of your application data structures after your application is up and running.

As with the Cocoa frameworks, you define your own notifications and use them to communicate important status information to other objects within your program. However, you should be careful not to overuse the notification mechanism. The following sections describe the performance issues related to notifications and guide you towards using them properly.

An important rule with notifications is to be picky about which notifications you handle. All notifications, whether posted synchronously or asynchronously, are eventually dispatched to the registered observers synchronously by the local NSNotificationCenter object. If there are a large number of observers or each observer does a lot of work while handling the notification, your program could experience a significant delay.

When you register to receive notifications, you should always try specify a valid notification name and object. Although you can specify `nil` for the notification name, doing so causes you to receive all notifications, which can cause a noticeable drop in performance. Specifying a valid name reduces the number of notifications that are dispatched to your handler. Similarly, if you specify a valid object with the notification, you further filter the number of notifications you receive and reduce the performance penalty.

When you define your notification handler methods, be as efficient as possible at handling the notification and returning control to the notification center. Remember that notifications occur synchronously. If you initiate a lengthy operation in the middle of your notification handler, you delay the receipt of the notification by other handlers and further delay the event that triggered the notification.

If you must perform additional work upon receiving a notification, consider deferring that work until later using a timer or by passing it to a worker thread. For more information, see [Unblocking Your User Interface](Unblocking%20Your%20User%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbsfvbegskhjjcuosi).

Adding and removing observers from a notification center involves updating the dispatch tables maintained by that object. If your application creates a number of short-lived objects, you should avoid handling notifications in these objects if possible. If you really need to dispatch notifications to short-lived objects, consider creating an intermediary observer object to act as a liaison between the notification center and your objects.

An intermediary observer object can be tuned to your particular data structures much more effectively than the default NSNotificationCenter object. Your intermediary would maintain a list of your short-lived objects and should be able to add those objects to its internal data structures quickly. Upon receiving a notification from the notification center, you could then asynchronously pass that notification to your short-lived objects using the `makeObjectsPerformSelector:withObject:` method.

As you design your application, do not simply assume that you should send a notification to communicate with interested parties. You should also consider alternatives such as [key-value](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25) observing, key-value binding, and [delegation](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14).

Key-value binding and key-value observing were introduced in OS X version 10.3 and provide a way of loosely coupling data. With key-value observing, you can request to be notified when the properties of another object change. Unlike regular notifications, there is no performance penalty for unobserved changes. There is also no need for the observed object to post a notification because the key-value observing system can do it for you automatically, although you can still choose do it manually.

Another technique that has existed in Cocoa for many years is the notion of delegation. If you have an object that generates notifications, you can assign a delegate to that object. Rather than post notifications to the notification center, you instead call the methods of the delegate, which can perform whatever tasks it requires. In the case where only one object is interested in the notifications anyway, this technique is preferred.

For more information about key-value observing, see _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_.

[Next](Document%20Revision%20History.md)[Previous](String%20Management.md)

