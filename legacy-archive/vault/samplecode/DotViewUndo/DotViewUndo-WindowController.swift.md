---
title: DotViewUndo
apple_id: DTS40008851
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/DotViewUndo/Listings/DotViewUndo_WindowController_swift.html
archived_at: '2026-07-18T03:07:06.960391Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DotViewUndo](DotViewUndo.md)


[Next](DotViewUndo-DotView.swift.md)[Previous](DotViewUndo-ViewController.swift.md)

# DotViewUndo/WindowController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A NSWindowController subclass to handle initial window configuration
 */

import Cocoa

class WindowController: NSWindowController {

    override func windowDidLoad() {
        super.windowDidLoad()
        self.window?.minSize = NSSize(width: 400, height: 300)
    }
}
```

[Next](DotViewUndo-DotView.swift.md)[Previous](DotViewUndo-ViewController.swift.md)

