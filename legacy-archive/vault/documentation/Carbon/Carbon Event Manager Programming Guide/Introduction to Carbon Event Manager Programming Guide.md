---
title: Carbon Event Manager Programming Guide
apple_id: TP30000989
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon_Event_Manager/Intro/CarbonEventsIntro.html
archived_at: '2026-07-15T05:22:33.387135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Carbon%20Event%20Manager%20Concepts.md)

# Introduction to Carbon Event Manager Programming Guide

_Events_ are the foundation of all Carbon programming. Each time the user clicks the mouse, types a character from the keyboard, or chooses a command from a menu, you’re notified by means of an event. When one of your windows needs to be redrawn, moved, or resized, your application receives an event telling you to perform the operation. When your program becomes the active (foreground) application or moves to the background in favor of another, or when another application starts up or quits, you receive an event informing you of the fact. Just about everything a typical Carbon program does, whether interacting with the user or communicating with the system, takes place in response to an event.

The Carbon Event Manager is the preferred interface for handling events in Carbon applications. You can use this interface to handle events generated in response to user input as well as to create your own custom events.

Some of the types of events that the Carbon Event Manager can handle include the following:

- Window events: resizing, closing, activation, moving, window updates, and so on.
- Menu events: menu tracking and selection, keyboard shortcuts, and so on.
- Control events: activation, selection, dragging, changes in user focus, and so on.
- Mouse events: mouse-up, mouse-down, mouse movement, multiple clicks, multiple buttons, dragging, chording, rollover states, scroll wheel operation, and so on.
- Text and keyboard events: Unicode or Macintosh-encoded text input and raw keyboard presses.
- Application events: application activation, deactivation, requests to quit, and so on.
- Apple events: see [Dispatching Apple Events in Your Application](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/dispatch_aes_aepg/dispatch_aes_aepg.html#//apple_ref/doc/uid/TP40001449-CH204) in _[Apple Events Programming Guide](../../Apple%20Script/Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_ for details on how to process Apple events using the Carbon Event Manager.
- Volume events: insertion or ejection of CDs and disks.
- Tablet events: tablet proximity and movement.

The Carbon event model is simpler and more efficient than that used by the Classic Event Manager (sometimes referred to as the `WaitNextEvent` event model). Many standard responses to events are handled automatically, which means that you need to write code only when you want to override or augment the default actions. In addition, the Carbon Event Manager also provides replacements for custom definition procedure messages.

The Carbon Event Manager is available on Mac OS X (10.0) and later. It is also available on Mac OS 8.6 through Mac OS 9.1 when CarbonLib 1.1.1 or later is installed. Note that some Carbon Event Manager features are available only on later versions of Mac OS X.

Because event handling is so fundamental to applications, everyone writing Carbon applications should read this document. You should have some familiarity with Macintosh terminology and understand the basics of creating and manipulating the Mac OS user interface (windows, controls, menus, and so on).

[Next](Carbon%20Event%20Manager%20Concepts.md)

