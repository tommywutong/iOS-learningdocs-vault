---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_DreamEffectLayout_swift.html
archived_at: '2026-07-15T04:56:06.916372Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-DecoratingLayout.swift.md)[Previous](LucidDreams-DreamDetailViewController.swift.md)

# LucidDreams/DreamEffectLayout.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Defines a layout that's used to lay out the `Dream` that's shown in
                the detail view.
*/

import CoreGraphics

/** 
    The layout used for the `Dream` preview functionality in `DreamPreviewHeaderReusableView`.
    This type composes multiple smaller layouts together to form its layout.
*/
struct DreamEffectLayout<ChildContent: Layout, Decoration: Layout, Effect: Layout>: Layout where
ChildContent.Content == Decoration.Content, ChildContent.Content == Effect.Content {
    typealias Content = ChildContent.Content

    private var content: ChildContent
    private var decoration: Decoration
    private var effects: [Effect]

    init(content: ChildContent, decoration: Decoration, effects: [Effect]) {
        self.content = content
        self.decoration = decoration
        self.effects = effects
    }

    mutating func layout(in rect: CGRect) {
        // Here we're composing many different layouts to achieve the desired layout.
        let stack = ZStackLayout(children: effects)

        /*
            Note the simple way to create a `BackgroundLayout` using the 
            `withBackground(...)` method.
        */
        let combinedDecoration = stack.withBackground(decoration)

        var decoratingLayout = DecoratingLayout(content: content, decoration: combinedDecoration)
        decoratingLayout.layout(in: rect)
    }

    var contents: [Content] {
        return content.contents + decoration.contents + effects.flatMap { $0.contents }
    }
}
```

[Next](LucidDreams-DecoratingLayout.swift.md)[Previous](LucidDreams-DreamDetailViewController.swift.md)

