---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_PhotoSplitViewController_swift.html
archived_at: '2026-07-18T03:18:49.572128Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-SidebarViewController.swift.md)[Previous](Photo%20Editor-CanvasImageView.swift.md)

# Photo Editor/PhotoSplitViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 PhotoSplitViewController allows us to easily access the child controllers as specific types.
*/

import Cocoa

class PhotoSplitViewController: NSSplitViewController {

    // This method is less generic than our protocol-based approach, but sometimes necessary. 
    // Here we assume that at least one child must conform to the desired type; the use of an implicitly-unwrapped optional results in a runtime error if this isn't true.

    var sidebarController: SidebarViewController! {
        return childViewControllers.lazy.filter { $0 is SidebarViewController }.first as? SidebarViewController
    }

    var canvasController: CanvasViewController! {
        return childViewControllers.lazy.filter { $0 is CanvasViewController }.first as? CanvasViewController
    }

}
```

[Next](Photo%20Editor-SidebarViewController.swift.md)[Previous](Photo%20Editor-CanvasImageView.swift.md)

