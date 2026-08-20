---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_CustomRotors_ElementView_CustomRotorsPageView_swift.html
archived_at: '2026-07-18T03:00:35.931497Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsElementViewControll.md)[Previous](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsElementLoadingToken.md)

# AccessibilityUIExamples/CustomRotors/ElementView/CustomRotorsPageView.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An example demonstrating setup of an accessibility rotor to search for fruit buttons..
*/

import Cocoa

@available(OSX 10.13, *)
class CustomRotorsPageView: NSView {

    var contentView = NSView()

    // MARK: - View Lifecycle

    required override init(frame frameRect: NSRect) {
        super.init(frame: frameRect)
    }

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
    }

    // MARK: - Drawing

    override func draw(_ dirtyRect: NSRect) {
        // Draw the outline background.
        NSColor.yellow.set()
        bounds.fill()
    }

    // MAR: - Accessibility

    override func isAccessibilityElement() -> Bool {
        return true
    }

    override func accessibilityRole() -> NSAccessibilityRole? {
        return NSAccessibilityRole.pageRole
    }

}
```

[Next](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsElementViewControll.md)[Previous](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsElementLoadingToken.md)

