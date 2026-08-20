---
title: Box Programming Topics
apple_id: 10000017i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2003-02-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Box/Tasks/SettingBoxSubviews.html
archived_at: '2026-07-15T07:11:22.356503Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Box Programming Topics](Introduction%20to%20Boxes.md)


[Next](Using%20a%20Box%20to%20Create%20a%20Separator.md)[Previous](Setting%20a%20Box%E2%80%99s%20Border%20Appearance.md)

# Setting a Box’s Subviews

To add a subview to a box, use the typical subview-adding methods, such as `addSubview:` and `replaceSubview:with:`. These NSViews are actually added to the NSBox’s content area, an NSView set within the NSBox’s frame. NSView’s subview-adding methods are redefined by NSBox to ensure that a subview is correctly placed in the view hierarchy. However, you should note that the `subviews` method isn’t redefined: It returns an NSArray containing a single object, the NSBox’s content view.

The size and location of the content area depends on the NSBox’s border type, title location, the size of the font used to draw the title, and an additional measure that you can set through the `setContentViewMargins:` method. When you create an NSBox, an instance of NSView is created and added (as a subview of the NSBox object) to fill the NSBox’s content area. If you replace this content view with an NSView of your own, your NSView will be resized to fit the content area. Similarly, as you resize an NSBox its content view is automatically resized to fill the content area.

[Next](Using%20a%20Box%20to%20Create%20a%20Separator.md)[Previous](Setting%20a%20Box%E2%80%99s%20Border%20Appearance.md)

