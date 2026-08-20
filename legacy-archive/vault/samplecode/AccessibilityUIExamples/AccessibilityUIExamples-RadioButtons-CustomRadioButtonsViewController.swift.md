---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_RadioButtons_CustomRadioButtonsViewController_swift.html
archived_at: '2026-07-18T03:00:37.028123Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-RadioButtons-CustomRadioButtonsView.swift.md)[Previous](AccessibilityUIExamples-Application-SplitViewController.swift.md)

# AccessibilityUIExamples/RadioButtons/CustomRadioButtonsViewController.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
View controller demonstrating accessibility provided by AppKit for NSButton.
*/

import Cocoa

class CustomRadioButtonsViewController: NSViewController {

    // MARK: - View Controller Lifecycle
    @IBOutlet var currentValueLabel: NSTextField!
    @IBOutlet var customRadios: CustomRadioButtonsView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // Allow the CustomButtonView to call our own action function.
        customRadios.actionHandler = { self.changeRadioValue(self) }
    }

    @IBAction func changeRadioValue(_ sender: Any) {
       currentValueLabel.stringValue = NSString(format: "(Radio selected = %ld)", customRadios.selectedButton + 1) as String
    }
}
```

[Next](AccessibilityUIExamples-RadioButtons-CustomRadioButtonsView.swift.md)[Previous](AccessibilityUIExamples-Application-SplitViewController.swift.md)

