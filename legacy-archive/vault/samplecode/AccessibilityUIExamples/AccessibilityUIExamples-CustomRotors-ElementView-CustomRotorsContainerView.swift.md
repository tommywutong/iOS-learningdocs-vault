---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_CustomRotors_ElementView_CustomRotorsContainerView_swift.html
archived_at: '2026-07-18T03:00:35.701138Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Switches-ThreePositionSwitchViewController.swift.md)[Previous](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsElementView.swift.md)

# AccessibilityUIExamples/CustomRotors/ElementView/CustomRotorsContainerView.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An example demonstrating setup of an accessibility rotor to search for fruit buttons.
*/

import Cocoa

@available(OSX 10.13, *)
class CustomRotorsContainerView: NSView {

    weak var delegate: CustomRotorsElementViewDelegate?

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
        NSColor.lightGray.set()
        bounds.fill()
    }

    // MARK: - Accessibility

    override func isAccessibilityElement() -> Bool {
        return true
    }

    override func accessibilityRole() -> NSAccessibilityRole? {
        return NSAccessibilityRole.group
    }

    override func accessibilityLabel() -> String? {
        return NSLocalizedString("Fruit to Color", comment: "")
    }

    override func accessibilityCustomRotors() -> [NSAccessibilityCustomRotor] {
        return delegate!.createCustomRotors()
    }
}

@available(OSX 10.13, *)
protocol CustomRotorsElementViewDelegate : class {
    func createCustomRotors() -> [NSAccessibilityCustomRotor]
}
```

[Next](AccessibilityUIExamples-Switches-ThreePositionSwitchViewController.swift.md)[Previous](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsElementView.swift.md)

