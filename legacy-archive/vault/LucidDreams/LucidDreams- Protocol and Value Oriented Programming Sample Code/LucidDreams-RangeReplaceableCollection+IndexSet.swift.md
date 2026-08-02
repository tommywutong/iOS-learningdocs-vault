---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_RangeReplaceableCollection_IndexSet_swift.html
archived_at: '2026-07-15T04:56:07.053856Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-Layout.swift.md)[Previous](LucidDreams-Drawable.swift.md)

# LucidDreams/RangeReplaceableCollection+IndexSet.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Adds functionality to any `RangeReplaceableCollection` that has `Int`
                indices the ability to be subscripted by an `IndexSet`, a Foundation
                type that stores integer indexes.
*/

import Foundation

extension RangeReplaceableCollection where Index == Int, IndexDistance == Int {
    /// Returns a collection with elements in `indexes`.
    subscript(indexes: IndexSet) -> Self {
        var new = Self()

        new.reserveCapacity(indexes.count)

        for idx in indexes {
            new.append(self[idx])
        }

        return new
    }
}
```

[Next](LucidDreams-Layout.swift.md)[Previous](LucidDreams-Drawable.swift.md)

