---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/UsingWindowsMenu.html
archived_at: '2026-07-15T07:21:20.086174Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Setting%20a%20Window%E2%80%99s%20Appearance.md)[Previous](Minimizing%20Windows.md)

# Using the Window Menu

Most Cocoa applications include the Window menu, which displays the titles of various of the application’s windows. When you change a window’s title, this change is automatically reflected in the Window menu. This menu automatically lists windows that have a title bar and are resizable and that can become the main window (as described in [Window Layering and Types of Windows](Window%20Layering%20and%20Types%20of%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztmlkcineuirskizea)). Typically you can rely on the automatic updating provided by Cocoa. In rare circumstances, however, you might want to modify the default behavior.

You can exclude a window that would otherwise be listed in the Window menu by sending it a [setExcludedFromWindowsMenu:](https://developer.apple.com/documentation/appkit/nswindow/1419175-isexcludedfromwindowsmenu)`YES` message. Since they cannot become main, [NSPanel](https://developer.apple.com/documentation/appkit/nspanel) objects are excluded from the Windows menu. Instances of subclasses of `NSPanel` can be included in the menu by returning `NO` from its [isExcludedFromWindowsMenu](https://developer.apple.com/documentation/appkit/nswindow/1419175-excludedfromwindowsmenu) method and `YES` from its [canBecomeMainWindow](https://developer.apple.com/documentation/appkit/nswindow/1419162-canbecomemain) method. If you change a window’s configuration such that it should be added to or removed from the Window menu, you can update the Window menu by sending the shared application instance [addWindowsItem:title:filename:](https://developer.apple.com/documentation/appkit/nsapplication/1428660-addwindowsitem) or [removeWindowsItem:](https://developer.apple.com/documentation/appkit/nsapplication/1428625-removewindowsitem).

[Next](Setting%20a%20Window%E2%80%99s%20Appearance.md)[Previous](Minimizing%20Windows.md)

