---
title: 'Exhibition: An Adaptive OS X App'
apple_id: TP40016178
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/Exhibition/Listings/Exhibition_AppDelegate_swift.html
archived_at: '2026-07-18T03:08:00.492861Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Exhibition: An Adaptive OS X App](Exhibition-%20An%20Adaptive%20OS%20X%20App.md)


[Next](Exhibition-ImageCollection.swift.md)[Previous](Exhibition-GalleryWindowController.swift.md)

# Exhibition/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The application delegate. Creates and holds onto the main window controller.
*/


import Cocoa

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {
    // MARK: Properties

    let galleryWindowController = GalleryWindowController()

    // MARK: Life Cycle

    override func awakeFromNib() {
        galleryWindowController.showWindow(nil)
    }
}
```

[Next](Exhibition-ImageCollection.swift.md)[Previous](Exhibition-GalleryWindowController.swift.md)

