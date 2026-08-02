---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_FetchRecordZoneSample_swift.html
archived_at: '2026-07-18T03:03:28.332334Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-CKSubscription.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-RequestApplicationPermissionSample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/FetchRecordZoneSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This sample shows how to fetch a record zone with the given name.
*/

import CloudKit

class FetchRecordZoneSample: CodeSample {

    init() {
        super.init(
            title: "fetchRecordZoneWithID",
            className: "CKDatabase",
            methodName: ".fetchRecordZoneWithID()",
            descriptionKey: "Zones.FetchRecordZone",
            inputs: [
                TextInput(label: "zoneName", value: "", isRequired: true)
            ]
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        if let zoneName = data["zoneName"] as? String {

            let container = CKContainer.defaultContainer()
            let privateDB = container.privateCloudDatabase

            let zoneID = CKRecordZoneID(zoneName: zoneName, ownerName: CKOwnerDefaultName)

            privateDB.fetchRecordZoneWithID(zoneID) {

                (zone, nsError) in

                let results = Results()

                if let zone = zone {
                    results.items.append(zone)
                }

                completionHandler(results, nsError)
            }

        }

    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-CKSubscription.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-RequestApplicationPermissionSample.swift.md)

