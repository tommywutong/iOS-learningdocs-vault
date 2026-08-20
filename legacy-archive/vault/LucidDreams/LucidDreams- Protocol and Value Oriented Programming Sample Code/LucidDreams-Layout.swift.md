---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_Layout_swift.html
archived_at: '2026-07-15T04:56:07.041750Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-DreamListViewController.swift.md)[Previous](LucidDreams-RangeReplaceableCollection%2BIndexSet.swift.md)

# LucidDreams/Layout.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Defines the `Layout` protocol.
*/

import CoreGraphics

/// A type that can layout itself and its contents.
protocol Layout {
    /// Lay out this layout and all of its contained layouts within `rect`.
    mutating func layout(in rect: CGRect)

    /// The type of the leaf content elements in this layout.
    associatedtype Content

    /// Return all of the leaf content elements contained in this layout and its descendants.
    var contents: [Content] { get }
}
```

[Next](LucidDreams-DreamListViewController.swift.md)[Previous](LucidDreams-RangeReplaceableCollection%2BIndexSet.swift.md)

