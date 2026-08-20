---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_ZStackLayout_swift.html
archived_at: '2026-07-15T04:56:07.092026Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-Dream%2BDiff.swift.md)[Previous](LucidDreams-EffectCollectionViewCell.swift.md)

# LucidDreams/ZStackLayout.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides a stack layout in the z axis.
*/

import CoreGraphics

/// A layout that renders content on top of each other in the z dimension.
struct ZStackLayout<Child: Layout>: Layout {
    typealias Content = Child.Content

    var children: [Child]

    mutating func layout(in rect: CGRect) {
        for index in children.indices {
            /*
                The same rect is used for each layout——the important part for the
                `ZStackLayout` is that it returns its child's contents in the correct
                order.
            */
            children[index].layout(in: rect)
        }
    }

    var contents: [Content] {
        return children.flatMap { $0.contents }
    }
}
```

[Next](LucidDreams-Dream%2BDiff.swift.md)[Previous](LucidDreams-EffectCollectionViewCell.swift.md)

