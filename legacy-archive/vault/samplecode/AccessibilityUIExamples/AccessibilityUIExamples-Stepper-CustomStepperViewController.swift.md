---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Stepper_CustomStepperViewController_swift.html
archived_at: '2026-07-18T03:00:37.496305Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Stepper-Bridging-Header.h.md)[Previous](AccessibilityUIExamples-Stepper-Shaders.metal.md)

# AccessibilityUIExamples/Stepper/CustomStepperViewController.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
View controller demonstrating an accessible, custom view subclass that behaves like a stepper.
*/

import Cocoa

class CustomStepperViewController: NSViewController {

    @IBOutlet var customStepper: CustomStepperView!
    @IBOutlet var volumeLevel: NSTextField!

    // MARK: - View Controller Lifecycle

    override func viewDidLoad() {
        super.viewDidLoad()

        customStepper.actionHandler = { self.pressStepper(self) }
        customStepper.actionHandler!()
    }

    fileprivate func updateVolumeLabel(volume: CGFloat) {
        let number = NSNumber(value: Float(volume / 100.0))
        let numberFormatter = NumberFormatter()
        numberFormatter.numberStyle = NumberFormatter.Style.percent
        numberFormatter.maximumFractionDigits = 0

        let stringFormatter = NSLocalizedString("VolumeFormatter", comment: "Formatter for volume")
        var label = numberFormatter.string(from: number)
        label = String(format:stringFormatter, label!)

        volumeLevel.stringValue = label!
    }

    fileprivate func pressStepper(_ sender: Any) {
        updateVolumeLabel(volume: customStepper.value)
    }

}
```

[Next](AccessibilityUIExamples-Stepper-Bridging-Header.h.md)[Previous](AccessibilityUIExamples-Stepper-Shaders.metal.md)

