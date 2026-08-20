---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/HandlingWindowEvents.html
archived_at: '2026-07-15T07:21:13.862958Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Using%20Keyboard%20Interface%20Control%20in%20Windows.md)[Previous](Setting%20Attributes%20for%20the%20Window%E2%80%99s%20Image.md)

# Handling Events in Windows

As described in _[NSResponder Class Reference](https://developer.apple.com/documentation/appkit/nsresponder)_, most events coming into an application make their way to a window in a [sendEvent:](https://developer.apple.com/documentation/appkit/nswindow/1419228-sendevent) message. A key event is directed at the key window, while a mouse event is directed at whatever window lies under the pointer. If an event affects the window directly—resizing or moving it, for example—it performs the appropriate operation itself and sends messages to its delegate informing it of its intentions, thus allowing your application to intercede. The window sends other events up its responder chain from the appropriate starting point: the first responder for a key event, the view under the pointer for a mouse event. These events are then typically handled by some view object in the window. See _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_ for more information on how to intercept and handle events.

[Next](Using%20Keyboard%20Interface%20Control%20in%20Windows.md)[Previous](Setting%20Attributes%20for%20the%20Window%E2%80%99s%20Image.md)

