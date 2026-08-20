---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_MainNavigationItem_swift.html
archived_at: '2026-07-18T03:03:28.788035Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-CKDiscoveredUserInfo.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-CKRecord.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/MainNavigationItem.swift

```
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the navigation item that holds the CloudKit logo as its titleView.
*/

import UIKit

class MainNavigationItem: UINavigationItem {
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        titleView = UIImageView(image: UIImage(named: "Title"))
    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-CKDiscoveredUserInfo.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-CKRecord.swift.md)

