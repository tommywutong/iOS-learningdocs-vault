---
title: Run Loops
apple_id: 10000062i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputControl/Concepts/runloops.html
archived_at: '2026-07-15T07:16:04.013697Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Run Loops](Introduction%20to%20Run%20Loops.md)


[Next](Input%20Modes.md)[Previous](Introduction%20to%20Run%20Loops.md)

# Run Loops

Event-driven applications receive their events in a run loop. A run loop monitors sources of input to the application and dispatches control when sources become ready for processing. When processing is complete, control passes back to the run loop which then waits for the next event. Possible events include mouse and keyboard events from the window system, the arrival of data on ports, the firing of timers, and distributed object requests.

The NSRunLoop class declares the programmatic interface to objects that manage input sources, the objects from which the run loop receives information. There are two general types of input sources to a run loop: asynchronous (input arrives at unpredictable intervals) and synchronous (input arrives at regular intervals). NSPort objects represent asynchronous input sources, and NSTimer objects represent synchronous input sources.

Besides managing input sources, NSRunLoop also provides support for delayed actions that are event-driven rather than timer driven. NSWindow uses delayed actions to perform screen updates on dirty views. NSNotificationQueue uses them to post notifications queued with the modes `NSPostASAP` and `NSPostWhenIdle`. You can request a delayed action with the NSRunLoop method `performSelector:target:argument:order:modes:`; the indicated method is then sent to the target at the start of the next run loop.

In general, your application does not need to either create or explicitly manage NSRunLoop objects. Each NSThread, including the application’s main thread, has an NSRunLoop object automatically created for it. However, only the main thread in an application using the Application Kit automatically runs its run loop; additional threads (or Foundation Kit tools) have to explicitly run the run loop themselves. To access the current thread’s default run loop, use the NSRunLoop class method `currentRunLoop`.

When an NSRunLoop runs, it polls each of the sources for the input mode to determine if any need processing. Only one is processed per loop. If no input sources are processed, NSRunLoop waits for input from the operating system. The run loop waits until input arrives or a timeout—provided when starting the run loop—is exceeded. At this point, the NSRunLoop may either return or it may continue, depending on which method was used to run the loop.

[Next](Input%20Modes.md)[Previous](Introduction%20to%20Run%20Loops.md)

