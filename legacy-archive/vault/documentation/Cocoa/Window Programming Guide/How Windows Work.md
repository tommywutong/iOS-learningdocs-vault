---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Concepts/HowWindowsWork.html
archived_at: '2026-07-15T07:21:09.859679Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](How%20a%20Window%20is%20Displayed.md)[Previous](Introduction.md)

# How Windows Work

The [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class defines objects that manage and coordinate the windows an application displays on the screen. A single `NSWindow` object corresponds to at most one onscreen window. The two principal functions of an `NSWindow` object are to provide an area in which [NSView](https://developer.apple.com/documentation/appkit/nsview) objects can be placed and to accept and distribute, to the appropriate views, events the user instigates through actions with the mouse and keyboard. Note that the term window sometimes refers to the Application Kit object and sometimes to the window server’s display device; which meaning is intended is made clear in context. AppKit also defines an abstract subclass of `NSWindow`—[NSPanel](https://developer.apple.com/documentation/appkit/nspanel)—that adds behavior more appropriate for auxiliary windows.

An `NSWindow` object is defined by a frame rectangle that encloses the entire window, including its title bar, border, and other peripheral elements (such as the resize control), and by a content rectangle that encloses just its content area. Both rectangles are specified in the screen coordinate system and are restricted to integer values. The frame rectangle establishes the window’s base coordinate system. This coordinate system is always aligned with and measured in the same increments as the screen coordinate system (in other words, the base coordinate system can’t be rotated or scaled). The origin of the base coordinate system is the bottom-left corner of the window’s frame rectangle.

Typically, you create windows using Interface Builder, which allows you to position them, set many of their attributes, and lay out their views. The programmatic work you do with windows more often involves bringing them on and off the screen; changing dynamic attributes such as the window’s title; running modal windows to restrict user input; and assigning a [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) that can monitor certain of the window’s actions, such as closing, zooming, and resizing.

You can also create a window programmatically with one of its [initializers](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MultipleInitializers.html#//apple_ref/doc/uid/TP40008195-CH33) by specifying, among other attributes, the size and location of its content rectangle. The frame rectangle is derived from the dimensions of the content rectangle.

When it’s created, a window automatically creates two views: an opaque frame view that fills the frame rectangle and draws the border, title bar, other peripheral elements, and background, and a transparent content view that fills the content rectangle. The frame view and its peripheral elements are private objects that your application can’t access directly. The content view is the “highest” accessible view in the window; you can replace the default content view with a view of your own creation using the [setContentView:](https://developer.apple.com/documentation/appkit/nswindow/1419160-contentview) method. The window determines the placement of the content view; you can’t position it using the [NSView](https://developer.apple.com/documentation/appkit/nsview) methods that begin with `setFrame`; you must use the `NSWindow` class’s placement methods, as described in [Opening and Closing Windows](Opening%20and%20Closing%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdmlkdjjbegq2divda).

You add other views to the window as subviews of the content view or as subviews of any of the content view’s subviews, and so on, via the [addSubview:](https://developer.apple.com/documentation/appkit/nsview/1483783-addsubview) method of `NSView`. This tree of views is called the window’s view hierarchy. When a window is told to display itself, it does so by sending `display...` messages to the top-level view in its view hierarchy. Because displaying is carried out in a determined order, the content view (which is drawn first) may be wholly or partially obscured by its subviews, and these subviews may be obscured by their subviews (and so on).

[Next](How%20a%20Window%20is%20Displayed.md)[Previous](Introduction.md)

