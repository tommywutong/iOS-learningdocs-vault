---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_SidebarClipView_swift.html
archived_at: '2026-07-18T03:18:49.667077Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-Photo.swift.md)[Previous](Photo%20Editor-CanvasViewController.swift.md)

# Photo Editor/SidebarClipView.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The SidebarClipView allows a view under the contentInsets to still be clicked on.
 */

import Cocoa

class SidebarClipView: NSClipView {

    weak var accessoryView: NSView?

    // NSClipView's hitTest normally is limited to views within the contentInset area. We want to allow the search field (or whatever accessory view) to still be interacted with, and explicitly check for it.
    override func hitTest(_ point: NSPoint) -> NSView? {
        if let accessoryView = accessoryView {
            let localPoint = convert(point, from: superview)
            if accessoryView.frame.contains(localPoint) {
                return accessoryView.hitTest(localPoint)
            }
        }

        return super.hitTest(point)
    }

}
```

[Next](Photo%20Editor-Photo.swift.md)[Previous](Photo%20Editor-CanvasViewController.swift.md)

