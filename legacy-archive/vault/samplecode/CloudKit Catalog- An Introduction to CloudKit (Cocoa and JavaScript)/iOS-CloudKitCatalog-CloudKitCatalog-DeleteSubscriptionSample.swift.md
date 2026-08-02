---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_DeleteSubscriptionSample_swift.html
archived_at: '2026-07-18T03:03:27.813260Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-AttributeTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-ImageFieldTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/DeleteSubscriptionSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This code sample demonstrates how to delete a subscription by ID.
*/

import CloudKit

class SubscriptionIDResult: Result {
    let subscriptionID: String

    init(subscriptionID: String) {
        self.subscriptionID = subscriptionID
    }

    var summaryField: String? = nil

    var attributeList: [AttributeGroup] {
        return [
            AttributeGroup(title: "", attributes: [
                Attribute(key: "subscriptionID", value: subscriptionID)
            ])
        ]
    }

}

class DeleteSubscriptionSample: CodeSample {

    init() {
        super.init(
            title: "deleteSubscription",
            className: "CKDatabase",
            methodName: ".deleteSubscriptionWithID()",
            descriptionKey: "Subscriptions.DeleteSubscription",
            inputs: [
                TextInput(label: "subscriptionID", value: "", isRequired: true)
            ]
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        if let subscriptionID = data["subscriptionID"] as? String {

            let container = CKContainer.defaultContainer()
            let privateDB = container.privateCloudDatabase

            privateDB.deleteSubscriptionWithID(subscriptionID) {

                (subscriptionID, nsError) in

                let results = Results()

                if let subscriptionID = subscriptionID {
                    results.items.append(SubscriptionIDResult(subscriptionID: subscriptionID))
                }

                completionHandler(results, nsError)
            }

        }

    }


}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-AttributeTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-ImageFieldTableViewCell.swift.md)

