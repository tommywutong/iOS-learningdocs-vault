---
title: 'AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback'
apple_id: TP40016165
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/AVMetadataRecordPlay/Listings/Swift_AVMetadataRecordPlay_AssetGridViewCell_swift.html
archived_at: '2026-07-18T03:00:20.940239Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback](AVMetadataRecordPlay-%20Timed%20Metadata%20Capture%20Recording%20and%20Playback.md)


[Next](Swift-AVMetadataRecordPlay-PreviewView.swift.md)[Previous](Swift-AVMetadataRecordPlay-AssetGridViewController.swift.md)

# Swift/AVMetadataRecordPlay/AssetGridViewCell.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Thumbnail image collection view cell.
*/

import UIKit

class AssetGridViewCell: UICollectionViewCell {

    @IBOutlet private var imageView: UIImageView!

    var representedAssetIdentifier: String?

    var thumbnailImage: UIImage? {
        get {
            return imageView.image
        }
        set {
            imageView.image = newValue
        }
    }

    override func prepareForReuse() {
        super.prepareForReuse()
        imageView.image = nil
    }
}
```

[Next](Swift-AVMetadataRecordPlay-PreviewView.swift.md)[Previous](Swift-AVMetadataRecordPlay-AssetGridViewController.swift.md)

