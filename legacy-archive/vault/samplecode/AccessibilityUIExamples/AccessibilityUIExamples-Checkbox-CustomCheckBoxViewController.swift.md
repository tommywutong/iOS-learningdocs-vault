---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Checkbox_CustomCheckBoxViewController_swift.html
archived_at: '2026-07-18T03:00:35.538412Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Checkbox-CustomCheckBoxView.swift.md)[Previous](AccessibilityUIExamples-Checkbox-CustomCheckBoxView.m.md)

# AccessibilityUIExamples/Checkbox/CustomCheckBoxViewController.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
View controller demonstrating accessibility provided by AppKit for NSButton.
*/

import Cocoa

class CustomCheckBoxViewController: NSViewController {

    // MARK: - View Controller Lifecycle
    @IBOutlet var currentValueLabel: NSTextField!
    @IBOutlet var customCheckbox: CustomCheckBoxView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // Allow the CustomCheckBoxView to call our own action function.
        customCheckbox.actionHandler = { self.changeCheckBoxValue(self) }
    }

    func changeCheckBoxValue(_ sender: Any) {
        currentValueLabel.stringValue = NSString(format: "(State = %@)", customCheckbox.checked ? "checked" : "unchecked") as String
    }
}
```

[Next](AccessibilityUIExamples-Checkbox-CustomCheckBoxView.swift.md)[Previous](AccessibilityUIExamples-Checkbox-CustomCheckBoxView.m.md)

