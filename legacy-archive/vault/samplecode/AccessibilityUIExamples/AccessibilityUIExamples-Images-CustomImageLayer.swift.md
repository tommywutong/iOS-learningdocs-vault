---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Images_CustomImageLayer_swift.html
archived_at: '2026-07-18T03:00:36.150032Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Images-ImageViewSubclass.swift.md)[Previous](AccessibilityUIExamples-Images-ViewImageSubclass.swift.md)

# AccessibilityUIExamples/Images/CustomImageLayer.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An example demonstrating adding accessibility to a CALayer subclass that behaves like an image by implementing the NSAccessibilityImage protocol.
*/

import Cocoa
import QuartzCore

class CustomImageLayer: CALayer, NSAccessibilityImage {

    var parent: NSView!
    var titleElement: CustomTextLayer!

    // MARK: NSAccessibilityImage

    func accessibilityFrame() -> NSRect {
        return NSAccessibilityFrameInView(parent, frame)
    }

    func accessibilityParent() -> Any? {
        return NSAccessibilityUnignoredAncestor(parent)
    }

    func accessibilityLabel() -> String? {
        return titleElement.string as? String
    }

    func accessibilityTitleUIElement() -> Any? {
        return titleElement
    }

}
```

[Next](AccessibilityUIExamples-Images-ImageViewSubclass.swift.md)[Previous](AccessibilityUIExamples-Images-ViewImageSubclass.swift.md)

