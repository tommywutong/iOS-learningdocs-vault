---
title: Run Loops
apple_id: 10000062i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputControl/Tasks/gettingrunloops.html
archived_at: '2026-07-15T07:16:05.513287Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Run Loops](Introduction%20to%20Run%20Loops.md)


[Next](Adding%20Input%20Sources.md)[Previous](Input%20Modes.md)

# Getting the Run Loop

When using an application built using the Application Kit, a run loop is created and run automatically. If you need to access this run loop, use the NSRunLoop class method `currentRunLoop`.

Additional run loops are created for each additional NSThread and also can be accessed by invoking `currentRunLoop` from each thread. These run loops do not have any input sources and are not running when the thread begins. You must add input sources to them and start the run loop yourself.

[Next](Adding%20Input%20Sources.md)[Previous](Input%20Modes.md)

