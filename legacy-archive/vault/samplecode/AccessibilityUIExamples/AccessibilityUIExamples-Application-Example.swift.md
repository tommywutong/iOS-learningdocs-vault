---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Application_Example_swift.html
archived_at: '2026-07-18T03:00:34.956642Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Application-SplitViewController.swift.md)[Previous](AccessibilityUIExamples-Application-Character.swift.md)

# AccessibilityUIExamples/Application/Example.swift

```
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
Object to describe an accessibility example.
*/

import Foundation

class Example: NSObject {
    var name = ""
    var desc = ""
    var viewControllerIdentifier = ""

    init(name: String, description: String, viewControllerIdentifier: String) {
        self.name = name
        self.desc = description
        self.viewControllerIdentifier = viewControllerIdentifier
        super.init()
    }

}
```

[Next](AccessibilityUIExamples-Application-SplitViewController.swift.md)[Previous](AccessibilityUIExamples-Application-Character.swift.md)

