---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_DiscoverUserInfoWithEmailAddressSample_swift.html
archived_at: '2026-07-18T03:03:27.918523Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-DiscoverAllContactUserInfosSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-CKRecordZoneID.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/DiscoverUserInfoWithEmailAddressSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This sample shows how to get discoverable user information from an email address.
*/

import CloudKit

class DiscoverUserInfoWithEmailAddressSample: CodeSample {

    init() {
        super.init(
            title: "discoverUserInfoWithEmailAddress",
            className: "CKContainer",
            methodName: ".discoverUserInfoWithEmailAddress()",
            descriptionKey: "Discoverability.DiscoverUserInfoWithEmailAddress",
            inputs: [
                TextInput(label: "emailAddress", value: "", isRequired: true, type: .Email)
            ]
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        if let emailAddress = data["emailAddress"] as? String {

            let container = CKContainer.defaultContainer()

            container.discoverUserInfoWithEmailAddress(emailAddress) {
                (userInfo, nsError) in

                let results = Results()

                if let userInfo = userInfo {
                    results.items.append(userInfo)
                }

                completionHandler(results, nsError)
            }
        }

    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-DiscoverAllContactUserInfosSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-CKRecordZoneID.swift.md)

