---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/SizingPlacingWindows.html
archived_at: '2026-07-15T07:21:18.582565Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Saving%20a%20Window%E2%80%99s%20Position%20into%20the%20User%E2%80%99s%20Defaults.md)[Previous](Setting%20Window%20Collection%20Behavior.md)

# Sizing and Placing Windows

This article describes how to control a window’s size and position, including how to set a window’s minimum and maximum size, how to constrain a window to the screen, how to cascade windows so their title bars remain visible, how to zoom a window as though the user pressed the zoom button, and how to center a window on the screen.

The [center](https://developer.apple.com/documentation/appkit/nswindow/1419090-center) method places a window in the most prominent location on the screen, one suitable for important messages and alert dialogs.

You can resize or reposition a window using [setFrame:display:](https://developer.apple.com/documentation/appkit/nswindow/1419753-setframe) or [setFrame:display:animate:](https://developer.apple.com/documentation/appkit/nswindow/1419519-setframe)—the former is equivalent to the latter with the animate flag `NO`. You might use these methods in particular to expand or contract a window to show or hide a subview (such as a control that may be exposed by clicking a disclosure triangle). If the animate argument in `setFrame:display:animate:` is `YES`, the method performs a smooth resize of the window, where the total time for the resize can be obtained by calling [animationResizeTime:](https://developer.apple.com/documentation/appkit/nswindow/1419655-animationresizetime).

The user can resize windows by clicking and dragging on the bottom right corner of the window. While the user is resizing the window, [inLiveResize](https://developer.apple.com/documentation/appkit/nswindow/1419378-inliveresize) will return `YES`. Otherwise, it returns `NO`. The user can generally reposition windows by dragging only the title bar. If you want users to be able to drag your window by clicking elsewhere, you should override [mouseDownCanMoveWindow](https://developer.apple.com/documentation/appkit/nsview/1483666-mousedowncanmovewindow) so that it returns `YES` in any views that you want to be draggable window regions. The methods [isMovable](https://developer.apple.com/documentation/appkit/nswindow/1419579-movable) and [setMovable:](https://developer.apple.com/documentation/appkit/nswindow/1419579-movable) determine whether the user can move the window by clicking in its title bar or background.

To keep the window’s top-left hand corner fixed when resizing, you must typically also reposition the origin, as illustrated in the following example.

```objc
- (IBAction)showAdditionalControls:sender
{
    NSRect frame = [myWindow frame];
    if (frame.size.width <= MIN_WIDTH_WITH_ADDITIONS)
        frame.size.width = MIN_WIDTH_WITH_ADDITIONS;
    frame.size.height += ADDITIONS_HEIGHT;
    frame.origin.y -= ADDITIONS_HEIGHT;
    [myWindow setFrame:frame display:YES animate:YES];
    // implementation continues...
```

Note that the window’s delegate does not receive [windowWillResize:toSize:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419292-windowwillresize) messages when the window is resized in this way. It is your responsibility to ensure that the window’s new size is acceptable.

The window’s delegate does receive [windowDidResize:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419567-windowdidresize) messages. You can implement `windowDidResize:` to add or remove subviews at suitable junctures. There are no additional flags to denote that the window is performing an animated resize operation (as distinct from a user-initiated resize). It is therefore up to you to capture relevant state information so that you can update the window contents appropriately in [windowDidResize:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419567-windowdidresize).

If you use the Cocoa document architecture, you can use the [setShouldCascadeWindows:](https://developer.apple.com/documentation/appkit/nswindowcontroller/1528177-shouldcascadewindows) method of [NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) to set whether the window, when it is displayed, should cascade in relation to other document windows (that is, have a slightly offset location so that the title bars of previously displayed windows are still visible). The default is true, so typically you have no additional work to perform.

If you are not using the document architecture, you can use the [cascadeTopLeftFromPoint:](https://developer.apple.com/documentation/appkit/nswindow/1419392-cascadetopleftfrompoint) method of [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) to cascade windows yourself. The method returns a point shifted from the top-left corner of the window that can be passed to a subsequent invocation of `cascadeTopLeftFromPoint:` to position the next window so the title bars of both windows are fully visible.

You use the [zoom:](https://developer.apple.com/documentation/appkit/nswindow/1419513-zoom) method to toggle the size and location of a window between its standard state, as determined by the application, and its user state: a new size and location the user may have set by moving or resizing the window.

You can use [setContentMinSize:](https://developer.apple.com/documentation/appkit/nswindow/1419670-contentminsize) and [setContentMaxSize:](https://developer.apple.com/documentation/appkit/nswindow/1419154-contentmaxsize) to limit the user’s ability to resize the window—note that you can still set it to any size programmatically. Similarly, you can use [setContentAspectRatio:](https://developer.apple.com/documentation/appkit/nswindow/1419148-contentaspectratio) to keep a window’s width and height at the same proportions as the user resizes it, and [setContentResizeIncrements:](https://developer.apple.com/documentation/appkit/nswindow/1419649-contentresizeincrements) to make the window resize in discrete amounts larger than a single pixel. (Aspect ratio and resize increments are mutually exclusive attributes.) In general, you should use the `setContent...` methods instead of those that affect the window’s frame ([setAspectRatio:](https://developer.apple.com/documentation/appkit/nswindow/1419507-aspectratio), [setMaxSize:](https://developer.apple.com/documentation/appkit/nswindow/1419595-maxsize), and so on). These are preferred because they avoid confusion for windows with toolbars, and also are typically a better model since you control the content of the window but not the frame.

You can use the [constrainFrameRect:toScreen:](https://developer.apple.com/documentation/appkit/nswindow/1419779-constrainframerect) method to adjust a proposed frame rectangle so that it lies on the screen in such a way that the user can move and resize a window. However, you should make sure your window fits onscreen before display. Note that any NSWindow with a title bar automatically constrains itself to the screen. The [cascadeTopLeftFromPoint:](https://developer.apple.com/documentation/appkit/nswindow/1419392-cascadetopleftfrompoint) method shifts the top left point by an amount that allows one window to be placed relative to another so that both their title bars are visible.

Additionally, when a window is about to be resized, the window’s delegate will be sent a [windowWillResize:toSize:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419292-windowwillresize) message. You can implement that method in your delegate to easily control your window’s size.

[Next](Saving%20a%20Window%E2%80%99s%20Position%20into%20the%20User%E2%80%99s%20Defaults.md)[Previous](Setting%20Window%20Collection%20Behavior.md)

