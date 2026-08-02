---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_FetchAllSubscriptionsSample_swift.html
archived_at: '2026-07-18T03:03:28.140537Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-AttributeKeyTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-ResultsViewController.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/FetchAllSubscriptionsSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This code sample shows how to fetch all subscriptions from the private database.
*/

import CloudKit

class FetchAllSubscriptionsSample: CodeSample {

    init() {
        super.init(
            title: "fetchAllSubscriptionsWithCompletionHandler",
            className: "CKDatabase",
            methodName: ".fetchAllSubscriptionsWithCompletionHandler()",
            descriptionKey: "Subscriptions.FetchAllSubscriptions"
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        let container = CKContainer.defaultContainer()
        let privateDB = container.privateCloudDatabase

        privateDB.fetchAllSubscriptionsWithCompletionHandler {

            (subscriptions, nsError) in

            let results = Results(alwaysShowAsList: true)

            if let subscriptions = subscriptions {
                if subscriptions.count == 0 {
                    self.listHeading = "No Subscriptions"
                } else {
                    self.listHeading = "Subscriptions:"
                    for subscription in subscriptions {
                        results.items.append(subscription)
                    }
                }
            }

            completionHandler(results, nsError)
        }

    }



}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-AttributeKeyTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-ResultsViewController.swift.md)

