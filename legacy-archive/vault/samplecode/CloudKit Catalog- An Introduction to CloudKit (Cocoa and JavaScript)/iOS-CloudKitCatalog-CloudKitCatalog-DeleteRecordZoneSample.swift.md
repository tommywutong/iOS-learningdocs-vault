---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_DeleteRecordZoneSample_swift.html
archived_at: '2026-07-18T03:03:27.759488Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-FormFieldTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-SubmenuTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/DeleteRecordZoneSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This sample demonstrates how to delete a record zone with the given name.
*/

import CloudKit

class DeleteRecordZoneSample: CodeSample {

    init() {
        super.init(
            title: "deleteRecordZoneWithID",
            className: "CKDatabase",
            methodName: ".deleteRecordZoneWithID()",
            descriptionKey: "Zones.DeleteRecordZone",
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

            privateDB.deleteRecordZoneWithID(zoneID) {
                (zoneID, nsError) in

                let results = Results()

                if let zoneID = zoneID {
                    results.items.append(zoneID)
                }

                completionHandler(results, nsError)
            }
        }

    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-FormFieldTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-SubmenuTableViewCell.swift.md)

