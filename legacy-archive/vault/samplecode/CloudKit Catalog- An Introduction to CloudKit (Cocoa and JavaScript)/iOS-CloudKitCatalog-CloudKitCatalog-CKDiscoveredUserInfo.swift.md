---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_CKDiscoveredUserInfo_swift.html
archived_at: '2026-07-18T03:03:27.143585Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-CKRecordZone.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-MainNavigationItem.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/CKDiscoveredUserInfo.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This extends CKDisoveredUserInfo to conform to the Result protocol.
*/

import CloudKit
extension CKDiscoveredUserInfo: Result {
    var attributeList: [AttributeGroup] {
        guard let displayContact = displayContact else {
            return [
                AttributeGroup(title: "No displayContact")
            ]
        }
        var contactType = "-"
        switch displayContact.contactType {
        case .Organization:
            contactType = "Organization"
        case .Person:
            contactType = "Person"
        }
        return [
            AttributeGroup(title: "Display Contact:", attributes: [
                Attribute(key: "identifier", value: displayContact.identifier),
                Attribute(key: "contactType", value: contactType),
                Attribute(key: "givenName", value: displayContact.givenName),
                Attribute(key: "familyName", value: displayContact.familyName)
            ])
        ]
    }

    var summaryField: String? {
        guard let displayContact = displayContact else { return userRecordID!.recordName }
        return displayContact.givenName + " " + displayContact.familyName

    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-CKRecordZone.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-MainNavigationItem.swift.md)

