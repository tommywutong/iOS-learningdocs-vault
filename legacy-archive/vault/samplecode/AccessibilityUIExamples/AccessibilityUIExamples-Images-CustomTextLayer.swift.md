---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Images_CustomTextLayer_swift.html
archived_at: '2026-07-18T03:00:36.198458Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Images-ViewImageSubclass.swift.md)[Previous](AccessibilityUIExamples-RadioButtons-CustomRadioButtonsView.swift.md)

# AccessibilityUIExamples/Images/CustomTextLayer.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An example demonstrating adding accessibility to an NSView subclass that behaves like a label by implementing the NSAccessibilityStaticText protocol.
*/

import Cocoa

class CustomTextLayer: CATextLayer, NSAccessibilityStaticText {

    var parent: NSView!

    // MARK: NSAccessibilityStaticText

    func accessibilityFrame() -> NSRect {
        return NSAccessibilityFrameInView(parent, frame)
    }

    func accessibilityParent() -> Any? {
        return NSAccessibilityUnignoredAncestor(parent)
    }

    func accessibilityValue() -> String? {
        return string as? String
    }
}
```

[Next](AccessibilityUIExamples-Images-ViewImageSubclass.swift.md)[Previous](AccessibilityUIExamples-RadioButtons-CustomRadioButtonsView.swift.md)

