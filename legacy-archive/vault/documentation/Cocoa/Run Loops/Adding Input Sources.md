---
title: Run Loops
apple_id: 10000062i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputControl/Tasks/addingsources.html
archived_at: '2026-07-15T07:16:05.013958Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Run Loops](Introduction%20to%20Run%20Loops.md)


[Next](Running%20the%20Run%20Loop.md)[Previous](Getting%20the%20Run%20Loop.md)

# Adding Input Sources

In most cases, input source objects add themselves to the current run loop as needed, but you can add them manually to get greater control over their behavior.

The NSTimer class method `scheduledTimerWithTimeInterval:invocation:repeats:`, for example, creates a new timer object and adds it to the `NSDefaultRunLoopMode` mode of the current run loop. If you instead create the timer with `timerWithTimeInterval:invocation:repeats:`, you must add it manually to the run loop with the NSRunLoop instance method `addTimer:forMode:`, which allows you to specify a different mode.

NSPort objects are usually used as part of an NSConnection, which automatically adds its receive port to the appropriate modes as needed. If you have a stand-alone port object, you can manually add it to the run loop with the NSRunLoop method `addPort:forMode:`.

[Next](Running%20the%20Run%20Loop.md)[Previous](Getting%20the%20Run%20Loop.md)

