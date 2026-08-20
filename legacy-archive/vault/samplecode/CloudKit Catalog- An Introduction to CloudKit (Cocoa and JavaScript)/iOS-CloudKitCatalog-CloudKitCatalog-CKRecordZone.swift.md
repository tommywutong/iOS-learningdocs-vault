---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_CKRecordZone_swift.html
archived_at: '2026-07-18T03:03:27.316459Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-MainMenuTableViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-CKDiscoveredUserInfo.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/CKRecordZone.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This extends CKRecordZone to conform to the Result protocol.
*/

import CloudKit

extension CKRecordZone: Result {
    var summaryField: String? {
        return zoneID.zoneName
    }
    var attributeList: [AttributeGroup] {
        return [
            AttributeGroup(title: "Record Zone:", attributes: [
                Attribute(key: "zoneID"),
                Attribute(key: "zoneName", value: zoneID.zoneName, isNested: true),
                Attribute(key: "ownerName", value: zoneID.ownerName, isNested: true),
                Attribute(key: "capabilities"),
                Attribute(key: "FetchChanges", value: capabilities.contains(.FetchChanges) ? "true" : "false", isNested: true),
                Attribute(key: "Atomic", value: capabilities.contains(.Atomic) ? "true" : "false", isNested: true)
            ])
        ]
    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-MainMenuTableViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-CKDiscoveredUserInfo.swift.md)

