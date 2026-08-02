---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_Drawable_swift.html
archived_at: '2026-07-15T04:56:06.878701Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-RangeReplaceableCollection%2BIndexSet.swift.md)[Previous](README.md.md)

# LucidDreams/Drawable.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Defines the `Drawable` protocol.
*/

import CoreGraphics

/// A type that can draw into a context.
protocol Drawable {
    func draw(in context: CGContext)
}
```

[Next](LucidDreams-RangeReplaceableCollection%2BIndexSet.swift.md)[Previous](README.md.md)

