---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/CachingWindowImage.html
archived_at: '2026-07-15T07:21:12.894916Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Updating%20the%20Cursor%20Image%20in%20a%20Window.md)

# Caching Window Images

To support transitory drawing by views, the [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class defines methods that temporarily cache a portion of its raster image so that it can be restored later. This feature is useful for situations where highly dynamic drawing must be done over the otherwise static image of the window. For example, in a drawing program where the user drags lines and other shapes directly onto a canvas, it’s more efficient to restore the window’s cached image and draw anew over that than to have all the views send display instructions to the window server. For more information, see the method descriptions for [cacheImageInRect:](https://developer.apple.com/documentation/appkit/nswindow/1419410-cacheimageinrect), [restoreCachedImage](https://developer.apple.com/documentation/appkit/nswindow/1419156-restorecachedimage), and [discardCachedImage](https://developer.apple.com/documentation/appkit/nswindow/1419623-discardcachedimage).

[Next](Document%20Revision%20History.md)[Previous](Updating%20the%20Cursor%20Image%20in%20a%20Window.md)

