---
title: 'RawExpose: Using CIRAWFilter to Decode RAW Images'
apple_id: TP40017310
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreImage
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/RawExpose/Listings/RawExposeEmbedded_AlbumCollectionViewCell_swift.html
archived_at: '2026-07-18T03:21:56.734721Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RawExpose: Using CIRAWFilter to Decode RAW Images](RawExpose-%20Using%20CIRAWFilter%20to%20Decode%20RAW%20Images.md)


[Next](RawExposeEmbedded-LightboxCollectionViewController.swift.md)[Previous](RawExpose-%20Using%20CIRAWFilter%20to%20Decode%20RAW%20Images.md)

# RawExposeEmbedded/AlbumCollectionViewCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The collection view cell used in the album collection view.
*/

import UIKit

class AlbumCollectionViewCell: UICollectionViewCell {

    static let reuseIdentifier = "AlbumCollectionViewCell"

    @IBOutlet weak var imageView: UIImageView!

    @IBOutlet weak var label: UILabel!
}
```

[Next](RawExposeEmbedded-LightboxCollectionViewController.swift.md)[Previous](RawExpose-%20Using%20CIRAWFilter%20to%20Decode%20RAW%20Images.md)

