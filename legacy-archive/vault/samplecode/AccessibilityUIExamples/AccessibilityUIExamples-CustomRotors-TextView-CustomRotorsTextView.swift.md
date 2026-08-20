---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_CustomRotors_TextView_CustomRotorsTextView_swift.html
archived_at: '2026-07-18T03:00:36.102548Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-CustomRotors-TextView-CustomRotorsTextViewController.swi.md)[Previous](AccessibilityUIExamples-LayoutArea-CustomLayoutAreaView.swift.md)

# AccessibilityUIExamples/CustomRotors/TextView/CustomRotorsTextView.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An example demonstrating setup of accessibility rotors to search for various text attributes on an text view.
*/

import Cocoa

@available(OSX 10.13, *)
class CustomRotorsTextView: NSTextView {

    weak var rotorDelegate: CustomRotorsTextViewDelegate?

    // MARK: Accessibility

    override func accessibilityCustomRotors() -> [NSAccessibilityCustomRotor] {
        return rotorDelegate?.createCustomRotors() ?? []
    }
}

// MARK: -

@available(OSX 10.13, *)
protocol CustomRotorsTextViewDelegate : class {
    func createCustomRotors() -> [NSAccessibilityCustomRotor]
}
```

[Next](AccessibilityUIExamples-CustomRotors-TextView-CustomRotorsTextViewController.swi.md)[Previous](AccessibilityUIExamples-LayoutArea-CustomLayoutAreaView.swift.md)

