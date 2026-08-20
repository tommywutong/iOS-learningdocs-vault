---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_DataItem_ImageName_swift.html
archived_at: '2026-07-18T03:27:28.766984Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-DataItem%2BSampleData.swift.md)[Previous](UIKitCatalog-ControlsMenuViewController.swift.md)

# UIKitCatalog/DataItem+ImageName.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An extension of `DataItem` that provides string properties for a `DataItem`'s image name.
*/

import Foundation

extension DataItem {
    var imageName: String {
        switch group {
            case .Scenery:
                return "\(group.rawValue) \(number)"

            default:
                return "\(group.rawValue) \(number).jpg"
        }
    }

    var largeImageName: String {
        switch group {
            case .Scenery:
                return "\(group.rawValue) \(number) Large"

            default:
                return "\(group.rawValue) \(number) Large.jpg"
        }
    }
}
```

[Next](UIKitCatalog-DataItem%2BSampleData.swift.md)[Previous](UIKitCatalog-ControlsMenuViewController.swift.md)

