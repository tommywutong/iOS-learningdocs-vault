---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_BooleanFieldTableViewCell_swift.html
archived_at: '2026-07-18T03:03:27.101628Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-TableView.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-ResultTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/BooleanFieldTableViewCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A BooleanFieldTableViewCell is a FormFieldTableViewCell with a UISwitch to toggle a boolean value.
*/

import UIKit

class BooleanFieldTableViewCell: FormFieldTableViewCell {

    // MARK: - Properties

    @IBOutlet weak var booleanField: UISwitch!

    var booleanInput: BooleanInput!

    // MARK: - Actions


    @IBAction func changeValue(sender: UISwitch) {
        booleanInput.value = sender.on
    }

}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-TableView.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-ResultTableViewCell.swift.md)

