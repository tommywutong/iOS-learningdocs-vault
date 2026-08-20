---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_FetchAllRecordZonesSample_swift.html
archived_at: '2026-07-18T03:03:28.089923Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-SaveRecordZoneSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-SelectionFieldTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/FetchAllRecordZonesSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This sample demonstrates how to fetch all record zones of the private database.
*/

import CloudKit

class FetchAllRecordZonesSample: CodeSample {

    init() {
        super.init(
            title: "fetchAllRecordZonesWithCompletionHandler",
            className: "CKDatabase",
            methodName: ".fetchAllRecordZonesWithCompletionHandler()",
            descriptionKey: "Zones.FetchAllRecordZones"
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        let container = CKContainer.defaultContainer()
        let privateDB = container.privateCloudDatabase

        privateDB.fetchAllRecordZonesWithCompletionHandler {
            (zones, nsError) in

            let results = Results(alwaysShowAsList: true)

            if let zones = zones where zones.count > 0 {
                for zone in zones {
                    results.items.append(zone)
                }
                self.listHeading = "Zones:"
            } else {
                self.listHeading = "No Zones"
            }

            completionHandler(results, nsError)

        }

    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-SaveRecordZoneSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-SelectionFieldTableViewCell.swift.md)

