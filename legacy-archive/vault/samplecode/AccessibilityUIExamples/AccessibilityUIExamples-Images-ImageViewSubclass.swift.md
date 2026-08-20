---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Images_ImageViewSubclass_swift.html
archived_at: '2026-07-18T03:00:36.321455Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Images-ImageViewLayerView.swift.md)[Previous](AccessibilityUIExamples-Images-CustomImageLayer.swift.md)

# AccessibilityUIExamples/Images/ImageViewSubclass.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An example demonstrating the preferred method of making an accessible, custom image by subclassing NSImageView.
*/

import Cocoa

/*
 IMPORTANT: This is not a template for developing a custom control.
 This sample is intended to demonstrate how to add accessibility to
 existing custom controls that are not implemented using the preferred methods.
 For information on how to create custom controls please visit http://developer.apple.com
*/

class ImageViewSubclass: NSImageView {

    required override init(frame frameRect: NSRect) {
        super.init(frame: frameRect)
    }

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
    }

    override func draw(_ dirtyRect: NSRect) {
        let name = "RedDot"
        let image = NSImage(named: NSImage.Name(rawValue: name))
        image?.draw(in: bounds, from: NSRect.zero, operation: NSCompositingOperation.sourceOver, fraction: 1.0)
    }

    // MARK: - NSAccessibility

    override func accessibilityLabel() -> String? {
        return NSLocalizedString("RedDot", comment: "accessibility label of the RedDot image")
    }

}
```

[Next](AccessibilityUIExamples-Images-ImageViewLayerView.swift.md)[Previous](AccessibilityUIExamples-Images-CustomImageLayer.swift.md)

