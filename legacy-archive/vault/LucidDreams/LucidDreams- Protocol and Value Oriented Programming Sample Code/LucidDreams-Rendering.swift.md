---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_Rendering_swift.html
archived_at: '2026-07-15T04:56:07.060140Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-ImageDrawable.swift.md)[Previous](LucidDreams-DreamListViewController.swift.md)

# LucidDreams/Rendering.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides the `makeImages(from:completion:)` function that turns dreams
                into images. Note that we're using the `MultiPaneLayout` type to lay
                out the text and images.
*/

import UIKit

/// Makes a single image from a dream.
private func makeImage(from dream: Dream) -> UIImage {
    let size = CGSize(width: 500, height: 200)
    UIGraphicsBeginImageContext(size)

    defer { UIGraphicsEndImageContext() }

    let context = UIGraphicsGetCurrentContext()!

    let content = TextDrawable(text: dream.description, frame: .zero)
    let decoration = ImageDrawable(image: dream.creature.image, frame: .zero)
    let accessories = Array(repeatElement(decoration, count: dream.numberOfCreatures))

    /*
        Here we're re-using one of our layouts to render an image that looks like
        the view layout we have in the app.
    */
    var multiPaneLayout = MultiPaneLayout(content: content, accessories: accessories)
    multiPaneLayout.layout(in: CGRect(origin: .zero, size: size))

    let drawables = multiPaneLayout.contents
    for drawable in drawables {
        drawable.draw(in: context)
    }

    return UIGraphicsGetImageFromCurrentImageContext()!
}

/**
    Creates an array of images from an array of dreams. This is called when the
    user shares dreams in the `DreamListViewController`.
*/
func makeImages(from dreams: [Dream], completion: @escaping ([UIImage]) -> Void) {
    let backgroundQueue = DispatchQueue(label: "com.example.apple-samplecode.LucidDreams.renderer.background")

    backgroundQueue.async {
        let images = dreams.map { makeImage(from: $0) }

        DispatchQueue.main.async {
            completion(images)
        }
    }
}
```

[Next](LucidDreams-ImageDrawable.swift.md)[Previous](LucidDreams-DreamListViewController.swift.md)

