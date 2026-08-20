---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Buttons_CustomButton_swift.html
archived_at: '2026-07-18T03:00:35.484346Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Buttons-ButtonViewSubclassViewController.swift.md)[Previous](AccessibilityUIExamples-Buttons-ButtonBaseViewController.swift.md)

# AccessibilityUIExamples/Buttons/CustomButton.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An example demonstrating the preferred method of making an accessible,
 custom button by subclassing NSButton and implementing the NSAccessibilityButton protocol.
*/

import Cocoa

// Note that NSButton already conforms to protocol "NSAccessibilityButton".
class CustomButton: NSButton {

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
        image = NSImage(named: NSImage.Name(rawValue: ButtonImages.buttonUp))
        alternateImage = NSImage(named: NSImage.Name(rawValue: ButtonImages.buttonDown))

        // Track the mouse for enter and exit for proper highlighting.
        let trackingArea = NSTrackingArea(rect: bounds,
                                          options: [NSTrackingArea.Options.activeAlways, NSTrackingArea.Options.mouseEnteredAndExited],
                                          owner: self,
                                          userInfo: nil)
        addTrackingArea(trackingArea)
    }

    // MARK: - Mouse events

    override func mouseEntered(with event: NSEvent) {
        super.mouseEntered(with: event)
        image = NSImage(named: NSImage.Name(rawValue: ButtonImages.buttonHighlight))
    }

    override func mouseExited(with event: NSEvent) {
        super.mouseExited(with: event)
        image = NSImage(named: NSImage.Name(rawValue: ButtonImages.buttonUp))
    }

}

// MARK: - NSAccessibilityButton

extension CustomButton {

    /// - Tag: accessibilityLabel
    override func accessibilityLabel() -> String? {
        return NSLocalizedString("Play", comment: "accessibility label of the Play button")
    }

    override func accessibilityHelp() -> String {
        return NSLocalizedString("Increase press count.", comment: "accessibility help of the Play button")
    }

    // MARK: NSAccessibility

    override func accessibilityPerformPress() -> Bool {
        // User did control-option-space keyboard shortcut.
        performClick(nil)
        return true
    }

}
```

[Next](AccessibilityUIExamples-Buttons-ButtonViewSubclassViewController.swift.md)[Previous](AccessibilityUIExamples-Buttons-ButtonBaseViewController.swift.md)

