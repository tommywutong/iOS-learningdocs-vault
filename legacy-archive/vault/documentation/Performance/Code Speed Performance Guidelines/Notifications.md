---
title: Code Speed Performance Guidelines
apple_id: 10000150i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeSpeed/Articles/Notifications.html
archived_at: '2026-07-18T01:47:04.974371Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Speed Performance Guidelines](Introduction%20to%20Code%20Speed%20Performance%20Guidelines.md)


[Next](Tuning%20for%20Specific%20Hardware.md)[Previous](Accelerating%20Critical%20Code.md)

# Notifications

Notifications are a simple way to communicate changes within your application or to another application. However, you should carefully consider the performance implications of using notifications and avoid their overuse.

The fewer notifications you send, the smaller the impact on your application’s performance. Depending on the implementation, the cost to dispatch a single notification could be very high. For example, in the case of Core Foundation and Cocoa notifications, the code that posts a notification must wait until all observers finish processing the notification. If there are numerous observers, or each performs a significant amount of work, the delay could be significant.

Another case where delivery cost for notifications is high is distributed notifications. If multiple processes register to receive a notification, the delivery of that notification might require bringing idle processes back into memory to handle it. This action has an effect both on CPU usage and on memory usage as processes are paged in to respond to the notification.

When you define your notification handler methods, be as efficient as possible at handling the notification and returning control to the notification center. Remember that most Core Foundation and Cocoa notifications occur synchronously. If you initiate a lengthy operation in the middle of your notification handler, you delay the receipt of the notification by other handlers and might further delay the event that triggered the notification.

If you must perform additional work upon receiving a notification, consider deferring that work until later. Set a flag, use a timer, or do anything you can to return control back to the poster of the notification as quickly as possible.

If your application is an observer for distributed notifications, and you do not want to receive those notifications when your application is not frontmost, be sure to specify that information when you register for the notification. Receiving notifications when your application is not frontmost can have a negative impact on performance because it might involve bringing your application back into memory to handle the notification. The distributed notification centers implemented by Core Foundation and Cocoa both give you the option to hold or drop notifications that come in while your application is inactive.

For more information about options for receiving distributed notifications, see the documentation for the `CFNotificationCenterAddObserver` method of Core Foundation or the `addObserver:selector:name:object:suspensionBehavior:` method of Cocoa’s NSDistributedNotificationCenter class.

If you find that the Cocoa or Core Foundation notification systems are inadequate for your performance needs, try using the Darwin notification system instead. The Darwin layer defines a basic set of notifications that allow fast communication among multiple processes. Notifications can be delivered automatically using a mach port, signal, or file descriptor. Although the system is much simpler than the ones offered by Core Foundation and Cocoa, it is also extremely lightweight and fast.

Another important feature of the Darwin notification system is the ability for clients to receive notifications manually. Unlike most notification mechanisms, which interrupt the observer to deliver the notification, your application can choose when it wants to receive Darwin notifications. If you are using notifications simply to communicate changes, this feature can offer tremendous performance advantages over the automatic delivery of notifications. For example, this is an excellent mechanism for notifying an application that a set of shared data has been modified and needs to be recached. You would not want to use this mechanism to respond to the occurrence of a specific event.

For more information about using Darwin notifications, see the [notify](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/notify.3.html#//apple_ref/doc/man/3/notify) man page. For API reference information, see also _[Darwin Notification API Reference](https://developer.apple.com/documentation/darwinnotify/darwin_notification_api)_ and the `notify.h` header file

[Next](Tuning%20for%20Specific%20Hardware.md)[Previous](Accelerating%20Critical%20Code.md)

