---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_DataItem_swift.html
archived_at: '2026-07-18T03:27:28.858361Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-AlertsViewController.swift.md)[Previous](UIKitCatalog-TextEntryMenuViewController.swift.md)

# UIKitCatalog/DataItem.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A struct used throughout the sample to represent example data.
*/

import Foundation

struct DataItem: Equatable {
    // MARK: Types

    enum Group: String {
        case Scenery
        case Iceland
        case Lola
        case Baby

        static let allGroups: [Group] = [.Scenery, .Iceland, .Lola, .Baby]
    }

    // MARK: Properties

    let group: Group

    let number: Int

    let title: String

    var identifier: String {
        return "\(group.rawValue).\(number)"
    }

    var displayURL: URL {
        var components = URLComponents()
        components.scheme = "uikitcatalog"
        components.path = "dataItem"
        components.queryItems = [URLQueryItem(name: "identifier", value: identifier)]

        return components.url!
    }

    var imageURL: URL {
        let mainBundle = Bundle.main
        guard let imageURL = mainBundle.url(forResource: imageName, withExtension: nil) else { fatalError("Error determining local image URL.") }

        return imageURL
    }
}

// MARK: Equatable

func ==(lhs: DataItem, rhs: DataItem)-> Bool {
    // Two `DataItem`s are considered equal if their identifiers and titles match.
    return lhs.identifier == rhs.identifier && lhs.title == rhs.title
}
```

[Next](UIKitCatalog-AlertsViewController.swift.md)[Previous](UIKitCatalog-TextEntryMenuViewController.swift.md)

