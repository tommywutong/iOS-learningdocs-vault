---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_FetchRecordSample_swift.html
archived_at: '2026-07-18T03:03:28.273744Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-FetchRecordChangesSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-DiscoverUserInfoWithUserRecordIDSample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/FetchRecordSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This sample demonstrates how to fetch a record by ID.
*/

import CloudKit

class FetchRecordSample: CodeSample {

    init() {
        super.init(
            title: "fetchRecordWithID",
            className: "CKDatabase",
            methodName: ".fetchRecordWithID()",
            descriptionKey: "Records.FetchRecord",
            inputs: [
                TextInput(label: "recordName", value: "", isRequired: true),
                TextInput(label: "zoneName", value: CKRecordZoneDefaultName, isRequired: true)
            ]
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        if let zoneName = data["zoneName"] as? String, recordName = data["recordName"] as? String {

            let container = CKContainer.defaultContainer()
            let privateDB = container.privateCloudDatabase

            let zoneID = CKRecordZoneID(zoneName: zoneName, ownerName: CKOwnerDefaultName)
            let recordID = CKRecordID(recordName: recordName, zoneID: zoneID)

            privateDB.fetchRecordWithID(recordID) {
                (record, nsError) in

                let results = Results()

                if let record = record {
                    results.items.append(record)
                }

                completionHandler(results, nsError)
            }
        }

    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-FetchRecordChangesSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-DiscoverUserInfoWithUserRecordIDSample.swift.md)

