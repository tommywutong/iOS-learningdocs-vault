---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_CodeSampleGroup_swift.html
archived_at: '2026-07-18T03:03:27.452580Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-SubmenuTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-PerformQuerySample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/CodeSampleGroup.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A CodeSampleGroup is a list of related code samples.
*/

import UIKit

class CodeSampleGroup {

    // MARK: - Properties

    let title: String
    let icon: UIImage
    let codeSamples: [CodeSample]

    // MARK: - Initialization

    init(title: String, icon: UIImage, codeSamples: [CodeSample]) {
        self.title = title
        self.icon = icon
        self.codeSamples = codeSamples
    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-SubmenuTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-PerformQuerySample.swift.md)

