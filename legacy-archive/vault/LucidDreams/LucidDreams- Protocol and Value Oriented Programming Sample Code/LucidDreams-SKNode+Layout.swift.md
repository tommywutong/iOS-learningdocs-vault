---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_SKNode_Layout_swift.html
archived_at: '2026-07-15T04:56:07.067226Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-FavoriteCreatureListViewController.swift.md)[Previous](LucidDreams-CreatureCell.swift.md)

# LucidDreams/SKNode+Layout.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Uses retroactive modeling to make `SKNode` a `Layout`.
*/

import UIKit
import SpriteKit

extension SKNode: Layout {
    typealias Content = SKNode

    func layout(in rect: CGRect) {
        // `SKNode` has a flipped coordinate system, so invert our Y coordinates.
        let height = parent?.frame.size.height ?? 0
        position = CGPoint(x: rect.midX, y: height - rect.midY)
    }

    var contents: [Content] {
        return [self]
    }
}

extension SKSpriteNode {
    override func layout(in rect: CGRect) {
        super.layout(in: rect)

        /*
            `SKSpriteNode`s have a settable size, so we'll update the node's size
            in addition to it's `position` (which is done in `SKNode`'s `layout(in:)`
            method).
        */
        size = rect.size
    }
}
```

[Next](LucidDreams-FavoriteCreatureListViewController.swift.md)[Previous](LucidDreams-CreatureCell.swift.md)

