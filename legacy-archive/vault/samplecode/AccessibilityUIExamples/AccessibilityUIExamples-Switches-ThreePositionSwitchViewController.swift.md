---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Switches_ThreePositionSwitchViewController_swift.html
archived_at: '2026-07-18T03:00:37.790242Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Switches-ThreePositionSwitchView.m.md)[Previous](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsContainerView.swift.md)

# AccessibilityUIExamples/Switches/ThreePositionSwitchViewController.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
View controller demonstrating an accessible, custom three-position switch.
*/

import Cocoa

class ThreePositionSwitchViewController: NSViewController {

    @IBOutlet var currentValueLabel: NSTextField!
    @IBOutlet var threePositionSwitch: ThreePositionSwitchView!

    // MARK: - Actions

    @IBAction func changeSwitchValue(_ sender: Any) {
        if let senderSwitch = sender as? ThreePositionSwitchView,
            let description = senderSwitch.accessibilityValue() as? String {
                currentValueLabel.stringValue = description.uppercased()
        }
    }

}
```

[Next](AccessibilityUIExamples-Switches-ThreePositionSwitchView.m.md)[Previous](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsContainerView.swift.md)

