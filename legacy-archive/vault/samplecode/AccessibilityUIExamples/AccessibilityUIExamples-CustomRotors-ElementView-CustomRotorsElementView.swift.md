---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_CustomRotors_ElementView_CustomRotorsElementView_swift.html
archived_at: '2026-07-18T03:00:35.886422Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsContainerView.swift.md)[Previous](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsElementViewControll.md)

# AccessibilityUIExamples/CustomRotors/ElementView/CustomRotorsElementView.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An example demonstrating setup of an accessibility rotor to search for fruit buttons.
*/

import Cocoa

/*
 IMPORTANT: This is not a template for developing a custom control.
 This sample is intended to demonstrate how to add accessibility to
 existing custom controls that are not implemented using the preferred methods.
 For information on how to create custom controls please visit http://developer.apple.com
*/

class CustomRotorsElementView: NSView {

    // MARK: - View Lifecycle

    required override init(frame frameRect: NSRect) {
        super.init(frame: frameRect)
        commonInit()
    }

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        commonInit()
    }

    fileprivate func commonInit() {
        //•• needed?
    }

    // MARK: - Accessibility

    override func isAccessibilityElement() -> Bool {
        NSLog("CustomRotorsElementView: accessibilityLabel")
        return true
    }

    override func accessibilityRole() -> String? {
        NSLog("CustomRotorsElementView: accessibilityRole")
        return NSAccessibilityGroupRole
    }

}
```

[Next](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsContainerView.swift.md)[Previous](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsElementViewControll.md)

