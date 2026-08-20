---
title: Example app using Photos framework
apple_id: TP40014575
resource_type: Sample Code
platform: tvOS|iOS
topic: User Experience
technology: Photos
published: '2017-02-24'
source_url: https://developer.apple.com/library/archive/samplecode/UsingPhotosFramework/Listings/Shared_GridViewCell_swift.html
archived_at: '2026-07-18T03:27:38.548315Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Example app using Photos framework](Example%20app%20using%20Photos%20framework.md)


[Next](Shared-AppDelegate.swift.md)[Previous](README.md.md)

# Shared/GridViewCell.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Collection view cell for displaying an asset.
 */


import UIKit

class GridViewCell: UICollectionViewCell {

    @IBOutlet var imageView: UIImageView!
    @IBOutlet var livePhotoBadgeImageView: UIImageView!

    var representedAssetIdentifier: String!

    var thumbnailImage: UIImage! {
        didSet {
            imageView.image = thumbnailImage
        }
    }
    var livePhotoBadgeImage: UIImage! {
        didSet {
            livePhotoBadgeImageView.image = livePhotoBadgeImage
        }
    }

    override func prepareForReuse() {
        super.prepareForReuse()
        imageView.image = nil
        livePhotoBadgeImageView.image = nil
    }
}
```

[Next](Shared-AppDelegate.swift.md)[Previous](README.md.md)

