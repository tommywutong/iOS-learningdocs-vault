---
title: Run Loops
apple_id: 10000062i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputControl/Concepts/modes.html
archived_at: '2026-07-15T07:16:03.503096Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Run Loops](Introduction%20to%20Run%20Loops.md)


[Next](Getting%20the%20Run%20Loop.md)[Previous](Run%20Loops.md)

# Input Modes

Run loops can be run in different modes. A mode, which is identified by an arbitrary string, defines a collection of input sources that is monitored while the run loop is in that mode. For example, you can have one mode that runs while the application is idle, waiting for all types of events to process, and another that only listens to a particular port, waiting for a response from a distributed object request. You do not want to handle keyboard events in the latter case, since the application has not finished processing an earlier event which caused the distributed object request to be made.

NSRunLoop defines this input mode:

| Input mode | Description |
| --- | --- |
| `NSDefaultRunLoopMode` | Use this mode to deal with input sources other than NSConnections. This is the most commonly used run loop mode. |

In addition, NSConnection defines this mode:

| Input mode | Description |
| --- | --- |
| `NSConnectionReplyMode` | Use this mode to indicate NSConnection objects waiting for replies. You rarely need to use this mode. |

And NSApplication defines these modes:

| Input mode | Description |
| --- | --- |
| `NSModalPanelRunLoopMode` | Use this mode when waiting for input from a modal panel, such as NSSavePanel or NSOpenPanel. |
| `NSEventTrackingRunLoopMode` | Use this mode for event tracking loops. |

You associate a list of input sources with each input mode. Sources are added with either the NSRunLoop methods `addPort:forMode:` or `addTimer:forMode:` or one of the convenience methods provided by NSConnection, NSPort, and NSTimer. Input sources can be added to multiple input modes.

You create additional modes by specifying a new mode name when adding an input source to that mode.

[Next](Getting%20the%20Run%20Loop.md)[Previous](Run%20Loops.md)

