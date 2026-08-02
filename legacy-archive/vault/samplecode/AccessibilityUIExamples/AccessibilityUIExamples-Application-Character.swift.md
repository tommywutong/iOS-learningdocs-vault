---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Application_Character_swift.html
archived_at: '2026-07-18T03:00:34.842383Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Application-Example.swift.md)[Previous](AccessibilityUIExamples-Application-MasterViewController.swift.md)

# AccessibilityUIExamples/Application/Character.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
Helpful extension to Character.
*/

import Cocoa

extension Character {
    init?(_ ascii: Int) {
        guard let scalar = UnicodeScalar(ascii) else {
            return nil
        }
        self = Character(scalar)
    }
}
```

[Next](AccessibilityUIExamples-Application-Example.swift.md)[Previous](AccessibilityUIExamples-Application-MasterViewController.swift.md)

