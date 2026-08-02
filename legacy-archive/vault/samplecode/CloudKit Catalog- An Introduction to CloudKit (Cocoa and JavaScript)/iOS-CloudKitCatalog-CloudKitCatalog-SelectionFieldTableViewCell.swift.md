---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_SelectionFieldTableViewCell_swift.html
archived_at: '2026-07-18T03:03:29.465945Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-FetchAllRecordZonesSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-FetchRecordChangesSample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/SelectionFieldTableViewCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A SelectionFieldTableViewCell is a FormFieldTableViewCell which contains a dropdown list of items and a
                unique selected item.
*/

import UIKit

class SelectionFieldTableViewCell: FormFieldTableViewCell {

    // MARK: - Properties

    @IBOutlet weak var selectedItemLabel: UILabel!

    var selectionInput: SelectionInput!
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-FetchAllRecordZonesSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-FetchRecordChangesSample.swift.md)

