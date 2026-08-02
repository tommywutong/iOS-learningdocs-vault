---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_CustomRotors_ElementView_CustomRotorsElementLoadingToken_swift.html
archived_at: '2026-07-18T03:00:35.752140Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsPageView.swift.md)[Previous](AccessibilityUIExamples-CustomRotors-TextView-CustomRotorsTextViewController.swi.md)

# AccessibilityUIExamples/CustomRotors/ElementView/CustomRotorsElementLoadingToken.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An item result with a given item loader and custom label.
*/

import Cocoa

class CustomRotorsElementLoadingToken: NSObject, NSCoding, NSSecureCoding {
    var uniqueIdentifier = ""

    init(identifier: String) {
        uniqueIdentifier = identifier
    }

    static var supportsSecureCoding: Bool {
        return true
    }

    required init(coder aDecoder: NSCoder) {
        super.init()

        if let identifier = aDecoder.decodeObject(of: NSString.self, forKey: "uniqueIdentifier") as String? {
            uniqueIdentifier = identifier
        }
    }

    func encode(with aCoder: NSCoder) {
        aCoder.encode(uniqueIdentifier, forKey: "uniqueIdentifier")
    }

}
```

[Next](AccessibilityUIExamples-CustomRotors-ElementView-CustomRotorsPageView.swift.md)[Previous](AccessibilityUIExamples-CustomRotors-TextView-CustomRotorsTextViewController.swi.md)

