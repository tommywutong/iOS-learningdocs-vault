---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Switches_TwoPositionSwitchViewController_swift.html
archived_at: '2026-07-18T03:00:37.967552Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Switches-TwoPositionSwitchView.swift.md)[Previous](AccessibilityUIExamples-Switches-ThreePositionSwitchView.m.md)

# AccessibilityUIExamples/Switches/TwoPositionSwitchViewController.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
View controller demonstrating an accessible, custom two-position switch.
*/

import Cocoa

class TwoPositionSwitchViewController: NSViewController {

    @IBOutlet var placeHolderView: NSView!
    var twoPositionSwitch: TwoPositionSwitchView!

    // MARK: - View Controller Lifecycle

    override func viewDidLoad() {
        super.viewDidLoad()

        twoPositionSwitch = TwoPositionSwitchView(frame: placeHolderView.frame)
        placeHolderView.addSubview(twoPositionSwitch)
    }

}
```

[Next](AccessibilityUIExamples-Switches-TwoPositionSwitchView.swift.md)[Previous](AccessibilityUIExamples-Switches-ThreePositionSwitchView.m.md)

