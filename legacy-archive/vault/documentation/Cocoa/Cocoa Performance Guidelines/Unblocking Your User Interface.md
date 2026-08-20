---
title: Cocoa Performance Guidelines
apple_id: TP40001448
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2009-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaPerformance/Articles/UnblockUI.html
archived_at: '2026-07-15T07:13:19.697529Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Performance Guidelines](Introduction%20to%20Cocoa%20Performance%20Guidelines.md)


[Next](Using%20Views%20Effectively.md)[Previous](General%20Recommendations.md)

# Unblocking Your User Interface

In a Cocoa application, the main thread runs the user interface, that is, all drawing and all events are handled on the main thread. If your application performs any lengthy synchronous operations on that thread, your user interface can become unresponsive and trigger the spinning cursor. To avoid this, you should shorten the amount of time consumed by those operations, defer their execution, or move them to secondary threads.

If you have operations that can be deferred or broken into chunks and performed incrementally, doing so can help performance. Operations that are iterative or modular in nature, such as scratch calculations, can usually be performed in small chunks. By performing a few of these calculations at idle time using asynchronous [notifications](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35), you can avoid blocking your main thread. To register for idle time notifications, you would simply post a notification object to the default queue and ask for it to be dispatched at idle time, as shown in the following example:

```
NSNotification* myNotification = [NSNotification notificationWithName:@"MyIdleNotification" object:myIdleHandlerObject];

[[NSNotificationQueue defaultQueue] enqueueNotification:myNotification postingStyle:NSPostWhenIdle];
```

Timers offer another way to do small amounts of work at more regular intervals. The advantage of timers is that they fire at a known time. The disadvantage is that they fire regardless of how busy your application is, which could still cause a perceptible delay. For information on how to set up a timer, see _[Timer Programming Topics](../Timer%20Programming%20Topics/Introduction%20to%20Timers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3dc2i)_.

Another way to defer an operation is to hook into the run loops of your application’s threads. By adding a CFRunLoopObserver to a run loop, you can receive notifications at certain points in the execution of that run loop. For example, you can be notified before timers are processed, before input sources are processed, or before or after the run loop sleeps.

To create a run loop observer, you must first define a callback function of type `CFRunLoopObserverCallBack`. The following code shows a sample implementation of this method. The `info` parameter contains data you want passed to your handler when it is called, which in this case is an instance of the fictional MyObject.

```
void MyRunLoopObserver(CFRunLoopObserverRef observer,
                            CFRunLoopActivity activity,
                            void* info)
{
    MyObject* theObject = (MyObject*)info;

    // Perform your tasks here.
}
```

After you define your callback function, you need to create the run loop observer and install it on the current run loop. The following code shows you how to do this from a Cocoa method. The code requests that the callback function be run before any timers are processed or before the run loop goes to sleep. Note that the last parameter to `CFRunLoopObserverCreate` is the `self` variable, which is assumed to be the instance of MyObject that the callback handler expects.

```objc
- (void) installRunLoopObserver
{
    CFRunLoopObserverRef myObserver = NULL;
    int myActivities = kCFRunLoopBeforeTimers | kCFRunLoopBeforeWaiting;

    // Create the observer reference.
    myObserver = CFRunLoopObserverCreate(NULL,
                            myActivities,
                            YES,        /* repeat */
                            0,
                            &MyRunLoopObserver,
                            (void*)self);

    if (myObserver)
    {
        // Now add it to the current run loop
        CFRunLoopAddObserver(CFRunLoopGetCurrent(),
                            myObserver,
                            kCFRunLoopCommonModes);
    }
}
```


Secondary threads are an excellent way to perform lengthy operations without blocking your user interface. If your application performs several sequential operations, you could also create a worker thread to handle new requests as they arise. The advantage of threads is that they can offer significant performance gains, especially on multiprocessor systems. The disadvantage is that you must plan carefully to make sure two or more threads do not try to manipulate the same data at the same time.

For more information about creating and managing threads, see _[Threading Programming Guide](../Threading%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2i)_.

[Next](Using%20Views%20Effectively.md)[Previous](General%20Recommendations.md)

