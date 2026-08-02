---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/OpeningClosingWindows.html
archived_at: '2026-07-15T07:21:15.615675Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Window%20Layering%20and%20Types%20of%20Windows.md)[Previous](How%20Window%20Controllers%20Work.md)

# Opening and Closing Windows

This article describes how to open and close a window.

Opening a window—that is, making a window visible—is normally accomplished by placing the window into the application's window list by invoking one of the methods [makeKeyAndOrderFront:](https://developer.apple.com/documentation/appkit/nswindow/1419208-makekeyandorderfront), [orderFront:](https://developer.apple.com/documentation/appkit/nswindow/1419495-orderfront), etc., in [NSWindow](https://developer.apple.com/documentation/appkit/nswindow), and so on. Also, with certain bits set in Interface Builder, the window is shown when the [nib file](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34) is loaded in some cases.

Closing a window involves explicit use of either the [close](https://developer.apple.com/documentation/appkit/nswindow/1419662-close) method, which simply removes the window from the screen, or [performClose:](https://developer.apple.com/documentation/appkit/nswindow/1419288-performclose), which highlights the close button as though the user clicked it. Closing a window involves at least removing it from the screen but may include disposing of it altogether. The [setReleasedWhenClosed:](https://developer.apple.com/documentation/appkit/nswindow/1419062-releasedwhenclosed) method specifies whether a window releases itself when it receives a close message. A window’s [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) is also notified when it’s about to close, as described in [Using Window Notifications and Delegate Methods](Using%20Window%20Notifications%20and%20Delegate%20Methods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztslkciffeeq2cijda).

These methods hide a window without closing it. The method [orderOut:](https://developer.apple.com/documentation/appkit/nswindow/1419660-orderout) removes a window from the screen. You can also set a window to be removed from the screen automatically when its application isn’t active using [setHidesOnDeactivate:](https://developer.apple.com/documentation/appkit/nswindow/1419777-hidesondeactivate). The [isVisible](https://developer.apple.com/documentation/appkit/nswindow/1419132-visible) method returns whether a window is on or off the screen.

[Next](Window%20Layering%20and%20Types%20of%20Windows.md)[Previous](How%20Window%20Controllers%20Work.md)

