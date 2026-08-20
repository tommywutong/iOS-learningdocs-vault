---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/SettingWindowCursorRects.html
archived_at: '2026-07-15T07:21:16.981328Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Caching%20Window%20Images.md)[Previous](Dragging%20Images%20to%20and%20from%20Windows.md)

# Updating the Cursor Image in a Window

You can change the cursor image when the cursor is within a specified area of a view in a window. To do this, use the `NSTrackingArea` class, along with the [cursorUpdate:](https://developer.apple.com/documentation/appkit/nsresponder/1525066-cursorupdate) method of the `NSResponder` class. For specifics, read [Using Tracking-Area Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/TrackingAreaObjects/TrackingAreaObjects.html#//apple_ref/doc/uid/10000060i-CH8) in _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_.

For details on the `NSTrackingArea` class itself, refer to _[NSTrackingArea Class Reference](https://developer.apple.com/documentation/appkit/nstrackingarea)_.

[Next](Caching%20Window%20Images.md)[Previous](Dragging%20Images%20to%20and%20from%20Windows.md)

