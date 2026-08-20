---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_BackgroundLayout_swift.html
archived_at: '2026-07-15T04:56:06.836498Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-DreamListViewControllerState.swift.md)[Previous](LucidDreams-AppDelegate.swift.md)

# LucidDreams/BackgroundLayout.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides a layout that allows you to put a background behind another
                layout.
*/

import CoreGraphics

/// A layout that diplays its background content behind its foreground content.
struct BackgroundLayout<Background: Layout, Foreground: Layout>: Layout where Background.Content == Foreground.Content {
    typealias Content = Background.Content

    var background: Background
    var foreground: Foreground

    mutating func layout(in rect: CGRect) {
        background.layout(in: rect)
        foreground.layout(in: rect)
    }

    var contents: [Content] {
        return background.contents + foreground.contents
    }
}

/**
    In this extension we define a methods that allow us to easily chain layouts
    together. For example, you can now take any `Layout` type and call
    `withBackground(backgroundLayout)` to get the same layout but with a background. 
    This is a convenient alternative to using initializer syntax if you're composing multiple
    layouts together.
*/
extension Layout {
    /// Returns a layout that shows `self` in front of `background`.
    func withBackground<Background: Layout>(_ background: Background) -> BackgroundLayout<Background, Self> where Background.Content == Content {
        return BackgroundLayout(background: background, foreground: self)
    }
}
```

[Next](LucidDreams-DreamListViewControllerState.swift.md)[Previous](LucidDreams-AppDelegate.swift.md)

