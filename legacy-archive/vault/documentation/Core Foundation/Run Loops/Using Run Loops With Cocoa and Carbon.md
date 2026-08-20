---
title: Run Loops
apple_id: 10000135i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFRunLoops/Tasks/CocoaCarbonLoops.html
archived_at: '2026-07-15T07:22:50.009910Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Run Loops](Introduction%20to%20Run%20Loops.md)


[Next](Document%20Revision%20History.md)[Previous](Running%20the%20Run%20Loop.md)

# Using Run Loops With Cocoa and Carbon

Cocoa and Carbon each build upon CFRunLoop to implement their own higher-level event loop. Cocoa exposes its event loop through the NSApplication and NSRunLoop classes; Carbon exposes its event loop through the Carbon Event Manager.

When writing a Cocoa or Carbon application, you can add your sources, timers, and observers to their run loops and modes. Your objects will then get monitored as part of the regular application event loop. Use the NSRunLoop instance method `getCFRunLoop` to obtain the CFRunLoop corresponding to a Cocoa run loop. In Carbon applications, use the `GetCFRunLoopFromEventLoop` function.

Cocoa and Carbon automatically set up and run the run loop in the main thread of the application. If you spawn additional threads, you are responsible for managing and running their run loops.

Cocoa defines several of its own run loop modes for use with NSRunLoop objects. Cocoa defines `NSDefaultRunLoopMode` as its default run loop mode, but this is equivalent to Core Foundation’s `kCFRunLoopDefaultMode` and can be used interchangeably. Cocoa also defines the modes `NSModalPanelRunLoopMode` and `NSEventTrackingRunLoopMode` in which it runs the main thread’s run loop when a modal panel is up or during event-tracking operations, such as drag-and-drop operations, respectively. Both of these modes are members of the main thread’s set of common modes.

[Next](Document%20Revision%20History.md)[Previous](Running%20the%20Run%20Loop.md)

