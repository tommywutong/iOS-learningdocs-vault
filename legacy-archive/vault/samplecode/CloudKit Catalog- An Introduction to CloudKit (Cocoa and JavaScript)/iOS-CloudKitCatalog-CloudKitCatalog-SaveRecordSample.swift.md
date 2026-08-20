---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_SaveRecordSample_swift.html
archived_at: '2026-07-18T03:03:29.332659Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-ErrorViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-AttributeKeyTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/SaveRecordSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This code sample demonstrates how to save a record of type Items to the private database.
*/

import CloudKit
import UIKit

class SaveRecordSample: CodeSample {

    init() {
        super.init(
            title: "saveRecord",
            className: "CKDatabase",
            methodName: ".saveRecord()",
            descriptionKey: "Records.SaveRecord",
            inputs: [
                TextInput(label: "recordName", value: ""),
                TextInput(label: "zoneName", value: CKRecordZoneDefaultName),
                TextInput(label: "name", value: ""),
                LocationInput(label: "location"),
                ImageInput(label: "asset")
            ]
        )
    }

    func processResult(record: CKRecord?, error: NSError?, completionHandler: (Results, NSError!) -> Void) {
        let results = Results()

        if let record = record {
            results.items.append(record)
        }

        completionHandler(results, error)
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        if let recordName = data["recordName"] as? String, zoneName = data["zoneName"] as? String {

            let container = CKContainer.defaultContainer()
            let privateDB = container.privateCloudDatabase

            let recordType = "Items"

            var record: CKRecord
            if zoneName.isEmpty {
                if recordName.isEmpty {
                    record = CKRecord(recordType: recordType)
                } else {
                    let recordID = CKRecordID(recordName: recordName)
                    record = CKRecord(recordType: recordType, recordID: recordID)
                }
            } else {
                let zoneID = CKRecordZoneID(zoneName: zoneName, ownerName: CKOwnerDefaultName)
                if recordName.isEmpty {
                    record = CKRecord(recordType: recordType, zoneID: zoneID)
                } else {
                    let recordID = CKRecordID(recordName: recordName, zoneID: zoneID)
                    record = CKRecord(recordType: recordType, recordID: recordID)
                }
            }
            if let name = data["name"] as? String {
                record["name"] = name
            }
            if let location = data["location"] as? CLLocation {
                record["location"] = location
            }
            if let imageURL = data["asset"] as? NSURL {
                let asset = CKAsset(fileURL: imageURL)
                record["asset"] = asset
            }
            privateDB.saveRecord(record) {
                (rec, nsError) in

                if let error = nsError where error.code == 14 {
                    // In this case we are trying to overwrite an existing record so let's fetch it and modify it.
                    privateDB.fetchRecordWithID(record.recordID) {
                        (rec, nsError) in

                        if let rec = rec {
                            for key in record.allKeys() {
                                rec[key] = record[key]
                            }

                            privateDB.saveRecord(rec) {
                                (rec, nsError) in

                                self.processResult(rec, error: nsError, completionHandler: completionHandler)
                            }
                        }

                    }
                } else {

                    self.processResult(rec, error: nsError, completionHandler: completionHandler)

                }
            }
        }

    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-ErrorViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-AttributeKeyTableViewCell.swift.md)

