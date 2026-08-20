---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Text_ProtectedTextViewController_swift.html
archived_at: '2026-07-18T03:00:38.708790Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Text-CoreTextColumnView.m.md)[Previous](AccessibilityUIExamples-Text-CoreTextView.swift.md)

# AccessibilityUIExamples/Text/ProtectedTextViewController.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
View controller demonstrating a text cell that protects its content from being read by
 accessibility clients by using the accessibilityProtectedContent attribute.
*/

import Cocoa

class ProtectedTextViewController: NSViewController {

    @IBOutlet var contentView: NSTextField!

    // MARK: - Actions

    @IBAction func protectionAction(_ sender: Any) {
        let shouldProtect = ((sender as AnyObject).state != NSControl.StateValue.off)

        /**
        If you pass in Yes for this, then the text content string will no longer be viewable by other applications.
        There is one exception and those are the system assistive software apps such as VoiceOver.

        To test protected content, use Xcode's "Accessibility Inspector",
        /and when set to protect and it's Inspection target button turns off.
        */
        contentView.setAccessibilityProtectedContent(shouldProtect)

        // Tell accessibility that we may have protected content for this app.
        NSAccessibilitySetMayContainProtectedContent(shouldProtect)
    }
}
```

[Next](AccessibilityUIExamples-Text-CoreTextColumnView.m.md)[Previous](AccessibilityUIExamples-Text-CoreTextView.swift.md)

