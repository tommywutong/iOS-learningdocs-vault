---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Buttons_ButtonBaseViewController_swift.html
archived_at: '2026-07-18T03:00:35.201338Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Buttons-CustomButton.swift.md)[Previous](AccessibilityUIExamples-Buttons-CustomButtonView.swift.md)

# AccessibilityUIExamples/Buttons/ButtonBaseViewController.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
Base view controller for views with a single button and a "Press Count" text field.
*/

import Cocoa

class ButtonBaseViewController: NSViewController {

    var pressCount = 0

    @IBOutlet var pressCountTextField: NSTextField!
    @IBOutlet var button: NSView!

    // MARK: - View Controller Lifecycle

    override func viewDidLoad() {
        super.viewDidLoad()
        updatePressCountTextField()
    }

    fileprivate func updatePressCountTextField () {
        let formatter = NSLocalizedString("PressCountFormatter", comment: "Press count formatter")
        let numberString = NumberFormatter.localizedString(from: NSNumber(value: pressCount), number: NumberFormatter.Style.none)
        pressCountTextField.stringValue = String(format: formatter, numberString)
    }

    // MARK: - Actions

    @IBAction func pressButton(_ sender: Any) {
        pressCount += 1
        updatePressCountTextField()
    }

}
```

[Next](AccessibilityUIExamples-Buttons-CustomButton.swift.md)[Previous](AccessibilityUIExamples-Buttons-CustomButtonView.swift.md)

