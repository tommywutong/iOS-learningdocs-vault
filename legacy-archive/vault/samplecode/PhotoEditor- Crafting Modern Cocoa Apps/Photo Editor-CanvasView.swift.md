---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_CanvasView_swift.html
archived_at: '2026-07-18T03:18:49.104403Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-Defaults.swift.md)[Previous](Photo%20Editor-WindowDraggableButton.swift.md)

# Photo Editor/CanvasView.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The CanvasView is a basic NSView subclass that demonstrates using updateLayer/wantsUpdateLayer by adding a drop shadow and a simple white fill color.
 */

import Cocoa

class CanvasView: NSView {

    override init(frame frameRect: NSRect) {
        super.init(frame: frameRect)
        commonSetup()
    }

    required init?(coder: NSCoder) {
        super.init(coder: coder)
        commonSetup()
    }

    private func commonSetup() {
        wantsLayer = true
        layerContentsRedrawPolicy = .onSetNeedsDisplay

        let shadow = NSShadow()
        shadow.shadowColor = NSColor(calibratedWhite: 0.0, alpha: 0.66)
        shadow.shadowBlurRadius = 4.0
        shadow.shadowOffset = NSSize(width: 0.0, height: 2.0)
        self.shadow = shadow
    }

    // Make the origin be the top left
    override var isFlipped: Bool {
        return true
    }

    override var isOpaque: Bool {
        return true
    }

    override var wantsUpdateLayer: Bool {
        return true
    }

    override func updateLayer() {
        layer?.backgroundColor = NSColor.white.cgColor
    }
}
```

[Next](Photo%20Editor-Defaults.swift.md)[Previous](Photo%20Editor-WindowDraggableButton.swift.md)

