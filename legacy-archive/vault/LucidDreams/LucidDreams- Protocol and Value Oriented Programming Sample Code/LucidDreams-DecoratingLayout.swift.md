---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_DecoratingLayout_swift.html
archived_at: '2026-07-15T04:56:06.870951Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-CreatureCollectionViewCell.swift.md)[Previous](LucidDreams-DreamEffectLayout.swift.md)

# LucidDreams/DecoratingLayout.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides the `DecoratingLayout` used throughout the application and
                WWDC presentation. This lays out a decoration view on the left with
                a content view on the right.
*/

import CoreGraphics

/**
    `DecoratingLayout` shows a decoration layout on the left with its content on
    the right. This is the type that is focused on during the WWDC session. One
    very interesting aspect to this layout is that it's composed of other layouts
    like `InsetLayout`!
*/
struct DecoratingLayout<
    ChildContent: Layout, Decoration: Layout>: Layout where ChildContent.Content == Decoration.Content
 {
    typealias Content = ChildContent.Content

    var content: InsetLayout<ChildContent>
    var decoration: InsetLayout<Decoration>

    init(content: ChildContent, decoration: Decoration) {
        self.content = content.withInsets(all: 5)
        self.decoration = decoration.withInsets(top: 5, bottom: 5, right: 5)
    }

    mutating func layout(in rect: CGRect) {
        let contentRect = self.contentRect(in: rect)
        let decorationRect = self.decorationRect(in: rect)

        content.layout(in: contentRect)
        decoration.layout(in: decorationRect)
    }

    func contentRect(in rect: CGRect) -> CGRect {
        var dstRect = rect
        dstRect.origin.x = rect.size.width / 3
        dstRect.size.width *= 2/3
        return dstRect
    }

    func decorationRect(in rect: CGRect) -> CGRect {
        var dstRect = rect
        dstRect.size.width /= 3
        return dstRect
    }

    var contents: [Content] {
        return decoration.contents + content.contents
    }
}
```

[Next](LucidDreams-CreatureCollectionViewCell.swift.md)[Previous](LucidDreams-DreamEffectLayout.swift.md)

