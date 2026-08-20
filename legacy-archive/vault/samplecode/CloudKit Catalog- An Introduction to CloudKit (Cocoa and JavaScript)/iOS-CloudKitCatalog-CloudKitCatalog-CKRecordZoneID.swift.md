---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_CKRecordZoneID_swift.html
archived_at: '2026-07-18T03:03:27.274637Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-DiscoverUserInfoWithEmailAddressSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-NestedAttributeTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/CKRecordZoneID.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This extends CKRecordZoneID to conform to the Result protocol.
*/

import CloudKit

extension CKRecordZoneID: Result {
    var summaryField: String? {
        return zoneName
    }

    var attributeList: [AttributeGroup] {
        return [
            AttributeGroup(title: "Record Zone ID:", attributes: [
                Attribute(key: "zoneName", value: zoneName),
                Attribute(key: "ownerName", value: ownerName)
            ])
        ]
    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-DiscoverUserInfoWithEmailAddressSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-NestedAttributeTableViewCell.swift.md)

