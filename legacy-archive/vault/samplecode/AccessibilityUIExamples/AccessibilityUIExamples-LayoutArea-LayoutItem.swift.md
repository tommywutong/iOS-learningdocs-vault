---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_LayoutArea_LayoutItem_swift.html
archived_at: '2026-07-18T03:00:36.584866Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-LayoutArea-CustomLayoutAreaView.swift.md)[Previous](AccessibilityUIExamples-LayoutArea-CustomLayoutAreaViewController.swift.md)

# AccessibilityUIExamples/LayoutArea/LayoutItem.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
The object representing the accessibility element for the CustomLayoutAreaView.
*/

import Cocoa

class LayoutItem: NSAccessibilityElement, NSAccessibilityLayoutItem {

    var zOrder = 0

    override func accessibilityIdentifier() -> String {
        return accessibilityLabel()!
    }

   var bounds: NSRect = .zero {
        didSet {
            let minSize = CustomLayoutAreaView.LayoutInfo.LayoutItemHandleSize * 3
            if bounds.size.height < minSize {
                bounds.size.height = minSize
            }
            if bounds.size.width < minSize {
                bounds.size.width = minSize
            }

            if let parent = accessibilityParent() as? CustomLayoutAreaView {
                if !(oldValue.origin == bounds.origin) && parent.selectedLayoutItem == self {
                    // A layout item was moved (bounds changed).
                    NSAccessibilityPostNotification(accessibilityParent, NSAccessibilityNotificationName.selectedChildrenMoved)
                }
            }
        }
    }

}

// MARK: -

extension LayoutItem {

    // MARK: NSAccessibilityLayoutItem

    override func setAccessibilityFrame(_ accessibilityFrame: NSRect) {
        var newFrame = accessibilityFrame
        if let parentView = accessibilityParent() as? CustomLayoutAreaView {
            let window = parentView.window
            newFrame = (window?.convertFromScreen(newFrame))!
            newFrame = parentView.convert(newFrame, from:nil)
            bounds = newFrame
            parentView.needsDisplay = true
        }
    }

    // MARK: NSAccessibilityElement

    override func accessibilityParent() -> Any? {
        return super.accessibilityParent()
    }

    override func accessibilityFrame() -> NSRect {
        var result = NSRect.zero
        if let accessibilityParent = accessibilityParent() as? CustomLayoutAreaView {
            result = NSAccessibilityFrameInView(accessibilityParent, bounds)
        }
        return result
    }

    override func isAccessibilityFocused() -> Bool {
        var isFocused = false
        if let accessibilityParent = accessibilityParent() as? CustomLayoutAreaView {
            if accessibilityParent.selectedLayoutItem != nil {
                isFocused = accessibilityParent.selectedLayoutItem == self
            }
        }
        return isFocused
    }

    // MARK: NSAccessibility

    override func setAccessibilityFocused(_ accessibilityFocused: Bool) {
        guard let accessibilityParent = accessibilityParent() as? CustomLayoutAreaView else { return }

        if accessibilityFocused {
            accessibilityParent.selectedLayoutItem = self
        } else {
            if let layoutItem = accessibilityParent.accessibilityFocusedUIElement as? LayoutItem {
                if layoutItem == self {
                    accessibilityParent.selectedLayoutItem = self
                }
            }
        }
    }

}
```

[Next](AccessibilityUIExamples-LayoutArea-CustomLayoutAreaView.swift.md)[Previous](AccessibilityUIExamples-LayoutArea-CustomLayoutAreaViewController.swift.md)

