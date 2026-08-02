---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Concepts/WindowLevel.html
archived_at: '2026-07-15T07:21:11.860955Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Setting%20Window%20Collection%20Behavior.md)[Previous](Window%20Layering%20and%20Types%20of%20Windows.md)

# Window Layers and Levels

Windows can be placed on the screen in three dimensions. Besides horizontal and vertical placement, windows are layered back-to-front within distinct levels. Each application and document window exists in its own layer, so documents from different applications can be interleaved. Clicking a window to bring it to the front doesn’t disturb the layering order of any other window. A window’s depth in the layers is determined by when the window was last accessed. When a user clicks an inactive document or chooses it from the Window menu, only that document and any open utility windows should be brought to the front.

Windows are ordered within several distinct levels. _Window levels_ group windows of similar type and purpose so that the more “important” ones (such as alert panels) appear in front of those lesser importance. A window’s level serves as a high-order bit to determine its position with regard to other windows. Windows can be reordered with respect to each other within a given level; a given window, however, cannot be layered above other windows in a higher level.

There are a number of predefined window levels, specified by constants defined by the `NSWindow` class. The levels you typically use are: [NSNormalWindowLevel](https://developer.apple.com/documentation/appkit/nsnormalwindowlevel), which specifies the default level; [NSFloatingWindowLevel](https://developer.apple.com/documentation/appkit/nswindow/level/1419352-floating), which specifies the level for floating palettes; and [NSScreenSaverWindowLevel](https://developer.apple.com/documentation/appkit/nswindow/level/1419693-screensaver), which specifies the level for a screen saver window. You might also use [NSStatusWindowLevel](https://developer.apple.com/documentation/appkit/nswindow/level/1419545-statusbar) for a status window, or [NSModalPanelWindowLevel](https://developer.apple.com/documentation/appkit/nsmodalpanelwindowlevel) for a modal panel. If you need to implement your own popup menus you use [NSPopUpMenuWindowLevel](https://developer.apple.com/documentation/appkit/nspopupmenuwindowlevel). The remaining two levels, [NSTornOffMenuWindowLevel](https://developer.apple.com/documentation/appkit/nstornoffmenuwindowlevel) and [NSMainMenuWindowLevel](https://developer.apple.com/documentation/appkit/nswindow/level/1419432-mainmenu), are reserved for system use.

You can use the [orderWindow:relativeTo:](https://developer.apple.com/documentation/appkit/nswindow/1419672-orderwindow) method to order a window within its level in front of or in back of another window. You more typically use convenience methods to specify ordering, such as [makeKeyAndOrderFront:](https://developer.apple.com/documentation/appkit/nswindow/1419208-makekeyandorderfront) (which also affects status), [orderFront:](https://developer.apple.com/documentation/appkit/nswindow/1419495-orderfront), and [orderBack:](https://developer.apple.com/documentation/appkit/nswindow/1419204-orderback), as well as [orderOut:](https://developer.apple.com/documentation/appkit/nswindow/1419660-orderout), which removes a window from the screen. You use the [isVisible](https://developer.apple.com/documentation/appkit/nswindow/1419132-visible) method to determine whether a window is on or off the screen. You can also set a window to be removed from the screen automatically when its application isn’t active using [setHidesOnDeactivate:](https://developer.apple.com/documentation/appkit/nswindow/1419777-hidesondeactivate).

Typically you should have no need to programmatically set the level of a window, since Cocoa automatically determines the appropriate level for a window based on its characteristics. A utility panel, for example, is automatically assigned to [NSFloatingWindowLevel](https://developer.apple.com/documentation/appkit/nswindow/level/1419352-floating). You can nevertheless set a window’s level using the [setLevel:](https://developer.apple.com/documentation/appkit/nswindow/1419511-level) method; for example, you can set the level of a standard window to [NSFloatingWindowLevel](https://developer.apple.com/documentation/appkit/nswindow/level/1419352-floating) if you want a utility window that looks like a standard window (for example to act as an inspector). This has two disadvantages, however: firstly, it may violate the human interface guidelines; secondly, if you assign a window to a floating level, you must ensure that you also set it to hide on deactivation of your application or reset its level when your application is hidden. Cocoa automatically takes care of the latter aspect for you if you use default window configurations.

There is currently no level specified to allow you to place a window above a screen saver window. If you need to do this (for example, to show an alert while a screen saver is running), you can set the window’s level to be greater than that of the screen saver, as shown in the following example.

```
[aWindow setLevel:NSScreenSaverWindowLevel + 1];
```

Other than this specific case, you are discouraged from setting windows in custom levels since this may lead to unexpected behavior.

[Next](Setting%20Window%20Collection%20Behavior.md)[Previous](Window%20Layering%20and%20Types%20of%20Windows.md)

