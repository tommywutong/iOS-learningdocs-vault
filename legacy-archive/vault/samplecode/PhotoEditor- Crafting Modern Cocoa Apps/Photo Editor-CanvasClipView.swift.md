---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_CanvasClipView_swift.html
archived_at: '2026-07-18T03:18:48.878730Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-PhotoController.swift.md)[Previous](Photo%20Editor-PhotoDocument.swift.md)

# Photo Editor/CanvasClipView.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The CanvasClipView subclasses NSClipView to demonstrate how to center the contents inside the clip view.
 */

import Cocoa

class CanvasClipView: NSClipView {

    override func constrainBoundsRect(_ proposedBounds: NSRect) -> NSRect {

        // Be polite and ask the superclass's opinion first.
        var constrainedBounds = super.constrainBoundsRect(proposedBounds)

        if let document = documentView {
            let documentFrame = document.frame

            // If either document dimension is too small, then offset the clip bounds to  
            if proposedBounds.width > documentFrame.width {
                constrainedBounds.origin.x = -(proposedBounds.width - documentFrame.width) / 2.0
                constrainedBounds.origin.x -= (contentInsets.left - contentInsets.right) / 2.0
            }

            if proposedBounds.height > documentFrame.height {
                constrainedBounds.origin.y = -(proposedBounds.height - documentFrame.height) / 2.0
                constrainedBounds.origin.y -= (contentInsets.top - contentInsets.bottom) / (isFlipped ? 2.0 : -2.0)
            }
        }

        return constrainedBounds
    }

}
```

[Next](Photo%20Editor-PhotoController.swift.md)[Previous](Photo%20Editor-PhotoDocument.swift.md)

