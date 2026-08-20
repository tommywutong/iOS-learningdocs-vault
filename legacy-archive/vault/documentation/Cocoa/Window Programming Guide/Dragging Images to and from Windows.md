---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/DraggingWindowImages.html
archived_at: '2026-07-15T07:21:13.354864Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Updating%20the%20Cursor%20Image%20in%20a%20Window.md)[Previous](Using%20Window%20Notifications%20and%20Delegate%20Methods.md)

# Dragging Images to and from Windows

The [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class defines some methods for image dragging, in case the user wants to drag an object into or out of a window. Although most dragging operations are initiated by and occur between view objects, the `NSWindow` class also defines an image-dragging method, [dragImage:at:offset:event:pasteboard:source:slideBack:](https://developer.apple.com/documentation/appkit/nswindow/1419224-drag). A window can also serve as the destination for dragging operations, registering the types it accepts with [registerForDraggedTypes:](https://developer.apple.com/documentation/appkit/nswindow/1419140-registerfordraggedtypes) and [unregisterDraggedTypes](https://developer.apple.com/documentation/appkit/nswindow/1419456-unregisterdraggedtypes).

[Next](Updating%20the%20Cursor%20Image%20in%20a%20Window.md)[Previous](Using%20Window%20Notifications%20and%20Delegate%20Methods.md)

