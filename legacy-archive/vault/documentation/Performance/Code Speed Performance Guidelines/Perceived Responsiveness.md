---
title: Code Speed Performance Guidelines
apple_id: 10000150i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeSpeed/Articles/PerceivedResponse.html
archived_at: '2026-07-18T01:47:05.911904Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Speed Performance Guidelines](Introduction%20to%20Code%20Speed%20Performance%20Guidelines.md)


[Next](Detecting%20Polling%20Behavior.md)[Previous](Impedance%20Mismatches.md)

# Perceived Responsiveness

The reason for improving application performance is to make an application seem more responsive to the user. But sometimes there is only so much you can do to improve the actual performance of your code. In situations like that, improving the perceived responsiveness of your application can satisfy the user just as if you had made the actual improvements.

Launch time is an important place to make your application seem fast, as it is the one time when the user typically waits for your application code to finish. The best way to make your application seem fast is to display your menu bar and main window as fast as possible.

When an application is launched, it is put into its initial state. In most cases the application need only make itself ready for the user. Rather than spend your time loading resources and initializing subsystems, find ways to defer your initialization code until the subsystems that need it are actually used. Not only does this reduce the amount of startup overhead for your application, it keeps your memory footprint low.

For information on improving launch-time performance, see _[Launch Time Performance Guidelines](../Launch%20Time%20Performance%20Guidelines/Introduction%20to%20Launch%20Time%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2dq2i)_ in Performance Documentation.

If your application needs to perform a lengthy operation, try to do so in a way that does not restrict the user from performing other actions. Using multiple threads to perform tasks in the background is one way to make sure your user interface is responsive. Having multiple threads can also allow your application to take advantage of multiple processors to improve performance.

Using threads is not without its costs, however. Threads add to your application’s memory footprint because of the space required for the thread’s stack. Background threads need to communicate with your main thread or with other threads in situations where there might be resource contentions. You may need to use locks to ensure that each of your application’s threads do not interfere with each other. These operations can be costly in their own right and should be used where there is a definite performance advantage.

An alternative to using threads is to use timers, which can call your code at fixed intervals to perform the operation. Timers have much less overhead than threads and are especially useful for operations that can be broken down into small chunks and executed incrementally over a longer period of time. Timers do suffer from the same resource restrictions as threads however. If the operation requires exclusive access to any resources, your code must use a lock to protect those resources until it is done with them.

For information on using threads, see _[Threading Programming Guide](../../Cocoa/Threading%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2i)_.

One way to tell if your application is unresponsive is to count how often you see the spinning cursor appear. OS X displays the spinning cursor automatically when your application fails to process an event within a few seconds. The spinning cursor is a way to let the user know that your application is busy. It is also a way to let you know that your application may be taking too long to do something.

The reasons for seeing the spinning cursor vary and can range from processing large amounts of data to waiting for a response from the network. The best way to find out what’s happening is to launch Spin Control and leave it running while you test your application. Spin Control samples your application whenever the spinning cursor appears. You can use the data gathered by Spin Control to find where your application was spending its time when it was unresponsive and correct the problem.

When processing large data sets, there are several techniques to avoid the spinning cursor. One technique is to do your processing on a separate thread of execution. This is the most general approach since it can be applied to most data sets. However, it does require extra overhead and communications to manage the thread. If the data can be factored into small chunks, you might have your application process a chunk at a time when no events are pending.

If your application is waiting for a response from a function call, you may be using the wrong function. Look through the API documentation for functions that perform the same task asynchronously.

[Next](Detecting%20Polling%20Behavior.md)[Previous](Impedance%20Mismatches.md)

