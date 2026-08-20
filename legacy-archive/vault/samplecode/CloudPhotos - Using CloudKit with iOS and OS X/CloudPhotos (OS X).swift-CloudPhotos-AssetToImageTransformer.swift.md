---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__OS_X__swift_CloudPhotos_AssetToImageTransformer_swift.html
archived_at: '2026-07-18T03:03:31.353934Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-PhotoView.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-CloudPhoto.swift.md)

# CloudPhotos (OS X).swift/CloudPhotos/AssetToImageTransformer.swift

```swift
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Value transformer to change a CKAsset to an image.
*/

import Foundation

// We use this value transformer to help us bind our table cell view's image to the CKAsset image.
//
class AssetToImageTransformer : ValueTransformer {
    func transformedValueClass() -> AnyClass {
        return NSImage.self
    }

    func allowsReverseTransformation() -> Bool {
        return false
    }

    override func transformedValue(_ value: Any?) -> Any? {
        // Update the photo.
        if value != nil {
            let photo = value as! CloudPhoto
            let imageData = photo.photoImage

            return imageData
        }
        return nil
    }
}
```

[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-PhotoView.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-CloudPhoto.swift.md)

