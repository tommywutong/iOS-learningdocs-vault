---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Application_WindowController_swift.html
archived_at: '2026-07-18T03:00:35.152853Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Application-AppDelegate.swift.md)[Previous](AccessibilityUIExamples-TransientUI-TransientUIViewController.swift.md)

# AccessibilityUIExamples/Application/WindowController.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
The sample's main window controller.
*/

import Cocoa
import Foundation

class WindowController: NSWindowController {
    override func windowDidLoad() {
        super.windowDidLoad()

        // Let the window accept (and distribute) mouse-moved events.
        window?.acceptsMouseMovedEvents = true

        // Window is not transparent to mouse events.
        window?.ignoresMouseEvents = false
    }

}
```

[Next](AccessibilityUIExamples-Application-AppDelegate.swift.md)[Previous](AccessibilityUIExamples-TransientUI-TransientUIViewController.swift.md)

