---
title: 'ForceTouchCatalog: Using the Force Touch Trackpad API'
apple_id: TP40016148
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/ForceTouchCatalog/Listings/ForceTouchCatalog_ForceTouchCatalog_MasterViewController_swift.html
archived_at: '2026-07-18T03:08:48.695378Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ForceTouchCatalog: Using the Force Touch Trackpad API](ForceTouchCatalog-%20Using%20the%20Force%20Touch%20Trackpad%20API.md)


[Next](ForceTouchCatalog-SquireViewController.swift.md)[Previous](ForceTouchCatalog-ForceTouchCatalog-DrawingView.swift.md)

# ForceTouchCatalog/ForceTouchCatalog/MasterViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    View controller for the Master tab. Example of how to manually perform haptic feedback.
*/

import Cocoa

class MasterViewController: NSViewController {
    @IBOutlet weak var rotateableImage: NSImageView!

    @IBAction func sliderValueChanged(sender: NSSlider) {
        let rotationValue = CGFloat(sender.integerValue)
        rotateableImage.frameCenterRotation = rotationValue

        if rotationValue == 0 {
            NSHapticFeedbackManager.defaultPerformer().performFeedbackPattern(.Alignment, performanceTime: .Default)
        }
    }
}
```

[Next](ForceTouchCatalog-SquireViewController.swift.md)[Previous](ForceTouchCatalog-ForceTouchCatalog-DrawingView.swift.md)

