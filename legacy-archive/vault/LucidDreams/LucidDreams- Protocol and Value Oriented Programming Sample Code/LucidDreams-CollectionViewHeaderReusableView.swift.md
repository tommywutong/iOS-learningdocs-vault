---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_CollectionViewHeaderReusableView_swift.html
archived_at: '2026-07-15T04:56:06.850650Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-TextDrawable.swift.md)[Previous](LucidDreams-CascadingLayout.swift.md)

# LucidDreams/CollectionViewHeaderReusableView.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Defines a simple header view that displays a title.
*/

import UIKit

/// A collection view reusable view that displays a title as a section header.
class CollectionViewHeaderReusableView: UICollectionReusableView {
    // MARK: Properties

    static let reuseIdentifier = "\(CollectionViewHeaderReusableView.self)"

    @IBOutlet var label: UILabel!

    private var _title: String! {
        didSet {
            label.text = _title
        }
    }

    var title: String {
        get { return _title }
        set { _title = newValue }
    }
}
```

[Next](LucidDreams-TextDrawable.swift.md)[Previous](LucidDreams-CascadingLayout.swift.md)

