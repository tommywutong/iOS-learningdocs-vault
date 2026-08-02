---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_CanvasScrollView_swift.html
archived_at: '2026-07-18T03:18:49.010027Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-WindowDraggableButton.swift.md)[Previous](Photo%20Editor-Photo.swift.md)

# Photo Editor/CanvasScrollView.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The CanvasScrollView exists just as a starting example of how to manually do drag and drop.
*/

import Cocoa

class CanvasScrollView: NSScrollView {

    override init(frame frameRect: NSRect) {
        super.init(frame: frameRect)
        commonSetup()
    }

    required init?(coder: NSCoder) {
        super.init(coder: coder)
        commonSetup()
    }

    private func commonSetup() {
        register(forDraggedTypes: [NSURLPboardType, NSFilesPromisePboardType])
    }

    // MARK: - Dragging destination support

    override func draggingEntered(_ sender: NSDraggingInfo) -> NSDragOperation {
        sender.draggingFormation = .stack // This is one possible representation for Drag Flocking
        return .copy
    }

    override func draggingExited(_ sender: NSDraggingInfo?) {
        sender?.draggingFormation = .default
    }

    override func prepareForDragOperation(_ sender: NSDraggingInfo) -> Bool {
        sender.animatesToDestination = true
        return true
    }

    override func performDragOperation(_ sender: NSDraggingInfo) -> Bool {
        // We perform no actual action here, but this is where you'd act upon a drag operation
        return true
    }

}
```

[Next](Photo%20Editor-WindowDraggableButton.swift.md)[Previous](Photo%20Editor-Photo.swift.md)

