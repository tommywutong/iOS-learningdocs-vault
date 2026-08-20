---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Outline_CustomOutlineViewAccessibilityRowElement_swift.html
archived_at: '2026-07-18T03:00:36.732046Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-LayoutArea-CustomLayoutAreaView%2BMeasurements.swift.md)[Previous](AccessibilityUIExamples-Outline-OutlineViewNode.swift.md)

# AccessibilityUIExamples/Outline/CustomOutlineViewAccessibilityRowElement.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
NSAccessibilityElement subclass for outline view items.
*/

import Cocoa

class CustomOutlineViewAccessibilityRowElement: NSAccessibilityElement {

    var disclosureTriangleCenterPoint = CGPoint()
    var canDisclose = false

    /**
     Override activation point to calculate it's position in screen coordinates relative to it's parent.
     This is necessary to support the window moving.
     */
    override func accessibilityActivationPoint() -> NSPoint {
        var result = NSPoint()
        if let parentView = accessibilityParent() as? CustomOutlineView {
            result = NSAccessibilityPointInView(parentView, disclosureTriangleCenterPoint)
        }
        return result
    }

    /** Override accessibilityDisclosed setter to update the the node this element represents
    This allows an accessibility client to expand or collapse a row in an outline
    (rather than just being able to read that state)
    VoiceOver, for example, exposes this via the Control+Command+\ command.
    */
    override func setAccessibilityDisclosed(_ accessibilityDisclosed: Bool) {
        if let parentView = accessibilityParent() as? CustomOutlineView {
            super.setAccessibilityDisclosed(accessibilityDisclosed)
            parentView.setExpandedStatus(expanded: accessibilityDisclosed, rowIndex: accessibilityIndex())
        }
    }

    // Disallow calling accessibilityDisclosed setter on elements that can't disclose (leaf nodes).
    override func isAccessibilitySelectorAllowed(_ selector: Selector) -> Bool {
        if selector == #selector(setAccessibilityDisclosed) {
            return canDisclose
        }
        return super.isAccessibilitySelectorAllowed(selector)
    }

    override func accessibilityRole() -> NSAccessibilityRole? {
        return NSAccessibilityRole.row
    }

    override func accessibilitySubrole() -> NSAccessibilitySubrole? {
        return NSAccessibilitySubrole.outlineRow
    }
}
```

[Next](AccessibilityUIExamples-LayoutArea-CustomLayoutAreaView%2BMeasurements.swift.md)[Previous](AccessibilityUIExamples-Outline-OutlineViewNode.swift.md)

