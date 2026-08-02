---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_CKNotification_swift.html
archived_at: '2026-07-18T03:03:27.184701Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-LoadingViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-DeleteRecordSample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/CKNotification.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This extends CKNotification to conform to the Result protocol.
*/

import CloudKit

extension CKNotification: Result {
    var summaryField: String? {
        let subscriptionID = self.subscriptionID ?? "unknown subscription"
        return alertBody ?? "\(notificationTypeString) notification for \(subscriptionID)."
    }

    var notificationTypeString: String {
        switch notificationType {
        case .Query:
            return "Query"
        case .ReadNotification:
            return "ReadNotification"
        case .RecordZone:
            return "RecordZone"
        }
    }

    var attributeList: [AttributeGroup] {
        return [
            AttributeGroup(title: "", attributes: [
                Attribute(key: "notificationID.hashValue", value: String(notificationID!.hashValue)),
                Attribute(key: "notificationType", value: notificationTypeString),
                Attribute(key: "alertBody", value: alertBody ?? "-"),
                Attribute(key: "soundName", value: soundName ?? "-"),
                Attribute(key: "badge", value: badge != nil ? String(badge) : "-"),
                Attribute(key: "category", value: category ?? "-"),
                Attribute(key: "subscriptionID", value: subscriptionID ?? "-")
            ])
        ]
    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-LoadingViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-DeleteRecordSample.swift.md)

