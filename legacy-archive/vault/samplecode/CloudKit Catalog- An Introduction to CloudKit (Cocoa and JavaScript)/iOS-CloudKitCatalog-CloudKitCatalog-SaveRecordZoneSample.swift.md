---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_SaveRecordZoneSample_swift.html
archived_at: '2026-07-18T03:03:29.387142Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-ImageFieldTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-FetchAllRecordZonesSample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/SaveRecordZoneSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This sample shows how to save a record zone with a provided zone name.
*/

import CloudKit

class SaveRecordZoneSample: CodeSample {

    init() {
        super.init(
            title: "saveRecordZone",
            className: "CKDatabase",
            methodName: ".saveRecordZone()",
            descriptionKey: "Zones.SaveRecordZone",
            inputs: [
                TextInput(label: "zoneName", value: "", isRequired: true)
            ]
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        if let zoneName = data["zoneName"] as? String {

            let container = CKContainer.defaultContainer()
            let privateDB = container.privateCloudDatabase

            privateDB.saveRecordZone(CKRecordZone(zoneName: zoneName)) {

                (recordZone, nsError) in

                let results = Results()

                if let recordZone = recordZone {
                    results.items.append(recordZone)
                }

                completionHandler(results, nsError)
            }
        }

    }


}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-ImageFieldTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-FetchAllRecordZonesSample.swift.md)

