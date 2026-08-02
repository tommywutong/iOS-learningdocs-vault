---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_ResultTableViewCell_swift.html
archived_at: '2026-07-18T03:03:29.198249Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-BooleanFieldTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-TextFieldTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/ResultTableViewCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A ResultTableViewCell contains a text label for a Result object's summaryField, 
                and a label marking its change state:
                modified=M, deleted=D, added=A.
*/

import UIKit

class ResultTableViewCell: UITableViewCell {

    // MARK: - Properties

    @IBOutlet weak var resultLabel: UILabel!
    @IBOutlet weak var changeLabel: UILabel!

    @IBOutlet weak var changeLabelWidthConstraint: NSLayoutConstraint!


}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-BooleanFieldTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-TextFieldTableViewCell.swift.md)

