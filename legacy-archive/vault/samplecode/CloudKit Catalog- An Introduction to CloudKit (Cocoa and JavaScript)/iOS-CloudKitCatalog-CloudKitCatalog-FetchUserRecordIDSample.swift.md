---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_FetchUserRecordIDSample_swift.html
archived_at: '2026-07-18T03:03:28.421619Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-SubmenuTableViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-NavigationBar.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/FetchUserRecordIDSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This sample shows how to fetch the signed in user's user record ID.
*/

import CloudKit

class FetchUserRecordIDSample: CodeSample {

    init() {
        super.init(
            title: "fetchUserRecordIDWithCompletionHandler",
            className: "CKContainer",
            methodName: ".fetchUserRecordIDWithCompletionHandler()",
            descriptionKey: "Discoverability.FetchUserRecordID"
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        let container = CKContainer.defaultContainer()

        container.fetchUserRecordIDWithCompletionHandler {
            (recordID, nsError) in

            let results = Results()

            if let recordID = recordID {
                results.items.append(recordID)
            }

            completionHandler(results, nsError)
        }

    }

}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-SubmenuTableViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-NavigationBar.swift.md)

