---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_SearchField_CustomSearchField_swift.html
archived_at: '2026-07-18T03:00:37.303574Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Outline-CustomOutlineView.m.md)[Previous](AccessibilityUIExamples-SearchField-CustomSearchFieldViewController.swift.md)

# AccessibilityUIExamples/SearchField/CustomSearchField.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An example demonstrating adding accessibility to an NSSearchField subclass that
 shows how to use the NSAccessibilitySharedFocusElementsAttribute
*/

import Cocoa

// IMPORTANT: This is not a template for developing a custom control.
// This sample is intended to demonstrate how to add accessibility to
// existing custom controls that are not implemented using the preferred methods.
// For information on how to create custom controls please visit http://developer.apple.com

class CustomSearchField: NSSearchField {

    // So we can inform the delegate of our search results (focused elements).
    weak var sharedFocusDelegate: SharedFocusSearchFieldDelegate?

    // MARK: - Accessibility

    // Returns array of elements with which this element shares keyboard focus.ell
    override func accessibilitySharedFocusElements() -> [Any]? {
        return sharedFocusDelegate?.accessibilitySharedFocusElementsForSearchFieldCell()
    }

}

// MARK: - SharedFocusSearchFieldDelegate

protocol SharedFocusSearchFieldDelegate : class {
    func accessibilitySharedFocusElementsForSearchFieldCell() -> [Any]
}
```

[Next](AccessibilityUIExamples-Outline-CustomOutlineView.m.md)[Previous](AccessibilityUIExamples-SearchField-CustomSearchFieldViewController.swift.md)

