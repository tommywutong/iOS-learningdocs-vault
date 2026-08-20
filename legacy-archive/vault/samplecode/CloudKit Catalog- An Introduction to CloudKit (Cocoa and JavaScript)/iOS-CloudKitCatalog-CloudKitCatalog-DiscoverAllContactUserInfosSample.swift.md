---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_DiscoverAllContactUserInfosSample_swift.html
archived_at: '2026-07-18T03:03:27.862501Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-SaveSubscriptionSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-DiscoverUserInfoWithEmailAddressSample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/DiscoverAllContactUserInfosSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This sample demonstrates how to get the discoverable user information of each user of the app
                in the signed in user's address book.
*/

import CloudKit

class DiscoverAllContactUserInfosSample: CodeSample {

    init() {
        super.init(
            title: "discoverAllContactUserInfosWithCompletionHandler",
            className: "CKContainer",
            methodName: ".discoverAllContactUserInfosWithCompletionHandler()",
            descriptionKey: "Discoverability.DiscoverAllContactUserInfos"
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        let container = CKContainer.defaultContainer()

        container.discoverAllContactUserInfosWithCompletionHandler {
            (userInfos, nsError) in

            let results = Results(alwaysShowAsList: true)

            if let userInfos = userInfos where userInfos.count > 0 {
                for userInfo in userInfos {
                    results.items.append(userInfo)
                }
                self.listHeading = "Discovered User Infos:"
            } else {
                self.listHeading = "No Discoverable Users Found"
            }

            completionHandler(results, nsError)

        }

    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-SaveSubscriptionSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-DiscoverUserInfoWithEmailAddressSample.swift.md)

