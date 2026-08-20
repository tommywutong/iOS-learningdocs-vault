---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/UsingWindowNotDel.html
archived_at: '2026-07-15T07:21:19.469060Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Dragging%20Images%20to%20and%20from%20Windows.md)[Previous](Using%20the%20Window%E2%80%99s%20Field%20Editor.md)

# Using Window Notifications and Delegate Methods

The [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class offers observers a rich set of [notifications](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35), which it broadcasts on such occurrences as gaining or losing key or main window status, minimizing, moving or resizing, becoming exposed, and closing. Each notification is matched to a [delegate method](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14), so a window’s delegate is automatically registered for all notifications that it has methods for. The `NSWindow` class also offers its delegate a few other methods, such as [windowShouldClose:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419380-windowshouldclose), which requests approval to close, [windowWillResize:toSize:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419292-windowwillresize), which allows the delegate to constrain the window’s size, [windowWillUseStandardFrame:defaultFrame:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419684-windowwillusestandardframe), which allows the delegate to set the window frame for zooming, and [windowWillReturnFieldEditor:toObject:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419416-windowwillreturnfieldeditor), which gives the delegate a chance to modify the field editor or substitute a different editor. See the individual notification and delegate method descriptions for more information.

[Next](Dragging%20Images%20to%20and%20from%20Windows.md)[Previous](Using%20the%20Window%E2%80%99s%20Field%20Editor.md)

