---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_DeleteRecordSample_swift.html
archived_at: '2026-07-18T03:03:27.713560Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-CKNotification.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-FetchSubscriptionSample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/DeleteRecordSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This code sample shows how to delete a record by ID.
*/

import CloudKit

class DeleteRecordSample: CodeSample {

    init() {
        super.init(
            title: "deleteRecordWithID",
            className: "CKDatabase",
            methodName: ".deleteRecordWithID()",
            descriptionKey: "Records.DeleteRecord",
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

            privateDB.deleteRecordWithID(recordID) {
                (recordID, nsError) in

                let results = Results()

                if let recordID = recordID {
                    results.items.append(recordID)
                }

                completionHandler(results, nsError)
            }
        }

    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-CKNotification.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-FetchSubscriptionSample.swift.md)

