---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_FetchSubscriptionSample_swift.html
archived_at: '2026-07-18T03:03:28.369943Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-DeleteRecordSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-CodeSampleViewController.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/FetchSubscriptionSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This code sample demonstrates how to fetch a subscription by ID.
*/

import CloudKit

class FetchSubscriptionSample: CodeSample {


    init() {
        super.init(
            title: "fetchSubscriptionWithID",
            className: "CkDatabase",
            methodName: ".fetchSubscriptionWithID()",
            descriptionKey: "Subscriptions.FetchSubscription",
            inputs: [
                TextInput(label: "subscriptionID", value: "", isRequired: true)
            ]
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        if let subscriptionID = data["subscriptionID"] as? String {

            let container = CKContainer.defaultContainer()
            let privateDB = container.privateCloudDatabase

            privateDB.fetchSubscriptionWithID(subscriptionID) {

                (subscription, nsError) in

                let results = Results()

                if let subscription = subscription {
                    results.items.append(subscription)
                }

                completionHandler(results, nsError)
            }
        }

    }


}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-DeleteRecordSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-CodeSampleViewController.swift.md)

