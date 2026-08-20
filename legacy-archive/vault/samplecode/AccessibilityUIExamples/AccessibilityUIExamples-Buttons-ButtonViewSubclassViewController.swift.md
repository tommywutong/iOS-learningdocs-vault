---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Buttons_ButtonViewSubclassViewController_swift.html
archived_at: '2026-07-18T03:00:35.357501Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Buttons-ButtonSubclassViewController.swift.md)[Previous](AccessibilityUIExamples-Buttons-CustomButton.swift.md)

# AccessibilityUIExamples/Buttons/ButtonViewSubclassViewController.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
View controller demonstrating an accessible, custom NSView subclass that behaves like a button.
*/

import Cocoa

class ButtonViewSubclassViewController: ButtonBaseViewController {

    // MARK: - View Controller Lifecycle

    @IBOutlet var customButton: CustomButtonView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // Allow the CustomButtonView to call our own action function.
        customButton.actionHandler = { self.pressButton(self) }
    }

}
```

[Next](AccessibilityUIExamples-Buttons-ButtonSubclassViewController.swift.md)[Previous](AccessibilityUIExamples-Buttons-CustomButton.swift.md)

