---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_ImageDrawable_swift.html
archived_at: '2026-07-15T04:56:07.026497Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-UIVIew%2BLayout.swift.md)[Previous](LucidDreams-Rendering.swift.md)

# LucidDreams/ImageDrawable.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Contains functionality to render a `UIImage` as a `Drawable`.
*/

import UIKit

/// Draws an image.
struct ImageDrawable: Layout, Drawable {
    var image: UIImage
    var frame: CGRect

    mutating func layout(in rect: CGRect) {
        frame = rect
    }

    func draw(in context: CGContext) {
        UIGraphicsPushContext(context)
        image.draw(in: frame)
        UIGraphicsPopContext()
    }

    typealias Content = Drawable
    var contents: [Content] {
        return [self]
    }
}
```

[Next](LucidDreams-UIVIew%2BLayout.swift.md)[Previous](LucidDreams-Rendering.swift.md)

