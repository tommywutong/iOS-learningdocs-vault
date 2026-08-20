---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_InsetLayout_swift.html
archived_at: '2026-07-15T04:56:07.033259Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-DreamDetailViewController.swift.md)[Previous](LucidDreams-DreamCell.swift.md)

# LucidDreams/InsetLayout.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides an inset layout as well as convenience methods to create
                an inset layout.
*/

import UIKit

/// An layout that insets its child content.
struct InsetLayout<Child: Layout>: Layout {
    typealias Content = Child.Content

    var child: Child

    var insets: UIEdgeInsets

    /*
        This initializer is private because the canonical way to inset a layout
        is by using the `withInsets(...)` method family defined below.
    */
    fileprivate init(child: Child, insets: UIEdgeInsets) {
        self.child = child
        self.insets = insets
    }

    mutating func layout(in rect: CGRect) {
        let rect = UIEdgeInsetsInsetRect(rect, insets)

        child.layout(in: rect)
    }

    var contents: [Content] {
        return child.contents
    }
}

/**
    In this extension we define methods that allow us to easily chain layouts
    together. For example, you can now take any `Layout` type and call 
    `withInsets(top: 5)` to get the same layout but insetted by 5 points. This is
    a convenient alternative to using initializer syntax if you're composing multiple
    layouts together.
*/
extension Layout {
    /// Makes an inset layout.
    func withInsets(top: CGFloat = 0, left: CGFloat = 0, bottom: CGFloat = 0, right: CGFloat = 0) -> InsetLayout<Self> {
        let insets = UIEdgeInsets(top: top, left: left, bottom: bottom, right: right)

        return withInsets(insets)
    }

    /// Makes an inset layout.
    func withInsets(all insets: CGFloat) -> InsetLayout<Self> {
        return withInsets(top: insets, left: insets, bottom: insets, right: insets)
    }

    /// Makes an inset layout.
    func withInsets(_ insets: UIEdgeInsets) -> InsetLayout<Self> {
        return InsetLayout(child: self, insets: insets)
    }
}
```

[Next](LucidDreams-DreamDetailViewController.swift.md)[Previous](LucidDreams-DreamCell.swift.md)

