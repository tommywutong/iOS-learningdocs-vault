---
title: DotView
apple_id: DTS40008850
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/DotView/Listings/DotView_WindowController_swift.html
archived_at: '2026-07-18T03:07:06.564711Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DotView](DotView.md)


[Next](DotView-ViewController.swift.md)[Previous](DotView-DotView.swift.md)

# DotView/WindowController.swift

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

[Next](DotView-ViewController.swift.md)[Previous](DotView-DotView.swift.md)

