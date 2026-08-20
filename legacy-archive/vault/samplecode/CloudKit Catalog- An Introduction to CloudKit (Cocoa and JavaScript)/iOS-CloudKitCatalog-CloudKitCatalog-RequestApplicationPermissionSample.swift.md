---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_RequestApplicationPermissionSample_swift.html
archived_at: '2026-07-18T03:03:29.113271Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-FetchRecordZoneSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-LocationFieldTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/RequestApplicationPermissionSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This sample shows how to request a user's permission to make them discoverable to other users
                of the app.
*/

import CloudKit

class PermissionStatus: Result {
    let summaryField: String? = nil
    let attribute: Attribute

    init(status: CKApplicationPermissionStatus) {
        let attribute = Attribute(key: "CKApplicationPermissionStatus")
        if status == .Granted {
            attribute.value = "Granted"
        } else {
            attribute.value = "Denied"
        }
        self.attribute = attribute
    }

    var attributeList: [AttributeGroup] {
        return [
            AttributeGroup(title: "Discoverability Status:", attributes: [ attribute ])
        ]
    }

}

class RequestApplicationPermissionSample: CodeSample {

    init() {
        super.init(
            title: "requestApplicationPermission",
            className: "CKContainer",
            methodName: ".requestApplicationPermission()",
            descriptionKey: "Discoverability.RequestApplicationPermission"
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        let container = CKContainer.defaultContainer()

        container.requestApplicationPermission(CKApplicationPermissions.UserDiscoverability) {

            (applicationPermissionStatus, nsError) in

            let results = Results()

            results.items = [ PermissionStatus(status: applicationPermissionStatus) ]

            completionHandler(results,nsError)
        }

    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-FetchRecordZoneSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-LocationFieldTableViewCell.swift.md)

