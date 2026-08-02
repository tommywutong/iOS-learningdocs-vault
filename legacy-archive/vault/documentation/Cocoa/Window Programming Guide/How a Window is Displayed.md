---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Concepts/HowWindowIsDisplayed.html
archived_at: '2026-07-15T07:21:09.359188Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](How%20Modal%20Windows%20Work.md)[Previous](How%20Windows%20Work.md)

# How a Window is Displayed

Displaying an [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) object begins with the drawing performed by its view objects, which accumulates in the window’s display buffer or appears immediately on the screen. Windows, like [NSView](https://developer.apple.com/documentation/appkit/nsview) objects, can be displayed unconditionally or merely marked as needing display, using the [display](https://developer.apple.com/documentation/appkit/nswindow/1419358-display) and [setViewsNeedDisplay:](https://developer.apple.com/documentation/appkit/nswindow/1419609-viewsneeddisplay) methods, respectively. A [displayIfNeeded](https://developer.apple.com/documentation/appkit/nswindow/1419096-displayifneeded) message causes the window’s views to display only if they’ve been marked as needing display. Normally, any time a view is marked as needing display, the window makes note of this fact and automatically displays itself shortly thereafter. This automatic display is typically performed on each pass through the event loop, but can be turned off using the [setAutodisplay:](https://developer.apple.com/documentation/appkit/nswindow/1419262-autodisplay) method. If you turn off autodisplay for a window, you’re then responsible for displaying it whenever necessary.

A window’s views can be drawn concurrently. You can use the methods [allowsConcurrentViewDrawing](https://developer.apple.com/documentation/appkit/nswindow/1419300-allowsconcurrentviewdrawing) and [setAllowsConcurrentViewDrawing:](https://developer.apple.com/documentation/appkit/nswindow/1419300-allowsconcurrentviewdrawing) to determine and set, respectively, whether or not a window draws its views concurrently. By default, a window’s views are drawn concurrently.

On each pass through the event loop, the application object invokes its [updateWindows](https://developer.apple.com/documentation/appkit/nsapplication/1428675-updatewindows) method, which sends an [update](https://developer.apple.com/documentation/appkit/nswindow/1419577-update) message to each window. Subclasses of `NSWindow` can override this method to examine the state of the application and change their own state or appearance accordingly—enabling or disabling menus, buttons, and other controls based on the object that’s selected, for example.

In addition to displaying itself on the screen, a window can print itself in its entirety, just as a view can. The [print:](https://developer.apple.com/documentation/appkit/nswindow/1419767-printwindow) method runs the application’s Print panel and causes the window’s frame view to print itself. [dataWithEPSInsideRect:](https://developer.apple.com/documentation/appkit/nswindow/1419128-datawitheps) behaves similarly. For additional information see _[Printing Programming Guide for Mac](../Printing%20Programming%20Guide%20for%20Mac/About%20Printing%20on%20the%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4dg2i)_.

[Next](How%20Modal%20Windows%20Work.md)[Previous](How%20Windows%20Work.md)

