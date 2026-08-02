---
title: CircleView
apple_id: DTS40008882
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/CircleView/Listings/CircleView_WindowController_swift.html
archived_at: '2026-07-18T03:03:20.861193Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CircleView](CircleView.md)


[Next](CircleView-ViewController.swift.md)[Previous](README.md.md)

# CircleView/WindowController.swift

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
        self.window?.minSize = NSSize(width: 400, height: 450)
    }
}
```

[Next](CircleView-ViewController.swift.md)[Previous](README.md.md)

