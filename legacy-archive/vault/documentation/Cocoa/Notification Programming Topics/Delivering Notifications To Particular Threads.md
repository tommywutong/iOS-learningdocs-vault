---
title: 通知编程主题
apple_id: 10000043i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2009-08-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Articles/Threading.html
archived_at: '2026-07-15T07:17:17.029628Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [通知编程主题](Introduction.md)


[下一页](Document%20Revision%20History.md)[上一页](Posting%20a%20Notification.md)

# 向特定线程递送通知

常规通知中心在发布通知的线程上递送通知。分布式通知中心在主线程上递送通知。有时，你可能需要让通知递送到由你（而不是通知中心）决定的特定线程上。例如，如果一个运行在后台线程中的对象正在监听来自用户界面的通知（比如窗口关闭），你会希望在后台线程而不是主线程中接收这些通知。在这些情况下，你必须在通知递送到默认线程时将其捕获，并把它们重定向到适当的线程。

重定向通知的一种方法是使用自定义的通知队列（不是 `NSNotificationQueue` 对象）来保存在错误的线程上收到的任何通知，然后在正确的线程上处理它们。该技术的工作方式如下：你以正常方式注册通知。当通知到达时，你检查当前线程是否为应当处理该通知的线程。如果线程不对，你将通知存入队列，然后向正确的线程发送一个信号，表示有通知需要处理。另一个线程收到信号，从队列中取出通知并处理它。

要实现该技术，你的观察者对象需要具有以下值的实例变量：一个用于保存通知的[可变](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)数组、一个用于向正确线程发送信号的通信端口（一个 Mach 端口）、一个用于防止通知数组发生多线程冲突的锁，以及一个标识正确线程的值（一个 `NSThread` 对象）。你还需要用于设置这些变量、处理通知以及接收 Mach 消息的方法。以下是需要添加到观察者对象类中的必要定义。

```objc
@interface MyThreadedClass: NSObject
/* Threaded notification support. */
@property NSMutableArray *notifications;
@property NSThread *notificationThread;
@property NSLock *notificationLock;
@property NSMachPort *notificationPort;

- (void) setUpThreadingSupport;
- (void) handleMachMessage:(void *)msg;
- (void) processNotification:(NSNotification *)notification;
@end
```

在注册任何通知之前，你需要[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)这些属性。下面的方法初始化队列和锁对象，保存对当前线程对象的引用，并创建一个 Mach 通信端口，将其添加到当前线程的运行循环中。

```objc
- (void) setUpThreadingSupport {
    if (self.notifications) {
        return;
    }
    self.notifications      = [[NSMutableArray alloc] init];
    self.notificationLock   = [[NSLock alloc] init];
    self.notificationThread = [NSThread currentThread];

    self.notificationPort = [[NSMachPort alloc] init];
    [self.notificationPort setDelegate:self];
    [[NSRunLoop currentRunLoop] addPort:self.notificationPort
            forMode:(NSString __bridge *)kCFRunLoopCommonModes];
}
```

该方法运行后，任何发送到 `notificationPort` 的消息都会在首次运行该方法的线程的运行循环中被接收。如果 Mach 消息到达时接收线程的运行循环没有在运行，内核会保留该消息，直到下次进入运行循环。接收线程的运行循环将传入的消息发送给端口的[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)的 `handleMachMessage:` 方法。

在此实现中，发送到 `notificationPort` 的消息不包含任何信息。相反，线程之间传递的信息包含在通知数组中。当 Mach 消息到达时，`handleMachMessage:` 方法忽略消息的内容，只检查 `notifications` 数组中是否有需要处理的通知。通知会从数组中移除，并转发给真正的通知处理方法。由于同时发送过多端口消息时消息可能会被丢弃，`handleMachMessage:` 方法会对数组进行[迭代](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Enumeration.html#//apple_ref/doc/uid/TP40008195-CH17)，直到数组为空。该方法在访问通知数组时必须获取锁，以防止一个线程添加通知与另一个线程从数组中移除通知之间发生冲突。

```objc
- (void) handleMachMessage:(void *)msg {

    [self.notificationLock lock];

    while ([self.notifications count]) {
        NSNotification *notification = [self.notifications objectAtIndex:0];
        [self.notifications removeObjectAtIndex:0];
        [self.notificationLock unlock];
        [self processNotification:notification];
        [self.notificationLock lock];
    };

    [self.notificationLock unlock];
}
```

当通知递送到你的对象时，接收通知的方法必须判断它是否运行在正确的线程中。如果是正确的线程，则正常处理通知。如果是错误的线程，则将通知添加到队列中，并向通知端口发送信号。

```objc
- (void)processNotification:(NSNotification *)notification {

    if ([NSThread currentThread] != notificationThread) {
        // Forward the notification to the correct thread.
        [self.notificationLock lock];
        [self.notifications addObject:notification];
        [self.notificationLock unlock];
        [self.notificationPort sendBeforeDate:[NSDate date]
                components:nil
                from:nil
                reserved:0];
    }
    else {
        // Process the notification here;
    }
}
```

最后，要注册一个无论它在哪个线程上发布、都希望在当前线程上递送的通知，你必须通过调用 `setUpThreadingSupport` 来初始化对象的通知属性，然后以正常方式注册通知，并将专门的通知处理方法指定为[选择器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。

```objc
[self setupThreadingSupport];
[[NSNotificationCenter defaultCenter]
        addObserver:self
        selector:@selector(processNotification:)
        name:@"NotificationName"
        object:nil];
```

这一实现存在几个方面的局限。首先，该对象处理的所有线程化通知都必须经过同一个方法（`processNotification:`）。其次，每个对象都必须提供自己的实现和通信端口。一个更好但更复杂的实现，是将该行为泛化为 `NSNotificationCenter` 的子类，或者一个独立的类——它为每个线程维护一个通知队列，并能够向多个观察者对象和方法递送通知。

[下一页](Document%20Revision%20History.md)[上一页](Posting%20a%20Notification.md)
