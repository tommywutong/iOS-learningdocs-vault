---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_TextDrawable_swift.html
archived_at: '2026-07-15T04:56:07.073430Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-DreamScene.swift.md)[Previous](LucidDreams-CollectionViewHeaderReusableView.swift.md)

# LucidDreams/TextDrawable.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Contains functionality to render an `AttributedString` as a `Drawable`.
*/

import UIKit

/// Draws text.
struct TextDrawable: Layout, Drawable {
    var text: String
    var frame: CGRect

    mutating func layout(in rect: CGRect) {
        frame = rect
    }

    func draw(in context: CGContext) {
        UIGraphicsPushContext(context)
        let attributedString = NSAttributedString(string: text, attributes: [NSFontAttributeName: UIFont.systemFont(ofSize: 40)])
        var frame = self.frame
        let height = min(attributedString.size().height, frame.size.height)
        frame.origin.y += 0.5 * frame.size.height - height
        frame.size.height = height
        attributedString.draw(in: frame)
        UIGraphicsPopContext()
    }

    typealias Content = Drawable
    var contents: [Content] {
        return [self]
    }
}
```

[Next](LucidDreams-DreamScene.swift.md)[Previous](LucidDreams-CollectionViewHeaderReusableView.swift.md)

