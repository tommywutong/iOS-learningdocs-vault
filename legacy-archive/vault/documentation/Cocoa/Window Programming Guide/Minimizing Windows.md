---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/MiniaturizingWindows.html
archived_at: '2026-07-15T07:21:14.993452Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Using%20the%20Window%20Menu.md)[Previous](Saving%20a%20Window%E2%80%99s%20Position%20into%20the%20User%E2%80%99s%20Defaults.md)

# Minimizing Windows

When a user minimizes a window, it’s removed from the screen and replaced with a smaller counterpart in the Dock.

The [miniaturize:](https://developer.apple.com/documentation/appkit/nswindow/1419426-miniaturize) and [deminiaturize:](https://developer.apple.com/documentation/appkit/nswindow/1419334-deminiaturize) methods reduce and reconstitute a window, and [performMiniaturize:](https://developer.apple.com/documentation/appkit/nswindow/1419749-performminiaturize) simulates the user clicking the window’s minimize button. You can also set the image and title displayed in a freestanding mini-window by sending [setMiniwindowImage:](https://developer.apple.com/documentation/appkit/nswindow/1419185-miniwindowimage) and [setMiniwindowTitle:](https://developer.apple.com/documentation/appkit/nswindow/1419571-miniwindowtitle) messages to the [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) object.

[Next](Using%20the%20Window%20Menu.md)[Previous](Saving%20a%20Window%E2%80%99s%20Position%20into%20the%20User%E2%80%99s%20Defaults.md)

