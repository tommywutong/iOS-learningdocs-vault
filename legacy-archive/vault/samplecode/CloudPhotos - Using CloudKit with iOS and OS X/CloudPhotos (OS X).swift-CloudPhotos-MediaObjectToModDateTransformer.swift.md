---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__OS_X__swift_CloudPhotos_MediaObjectToModDateTransformer_swift.html
archived_at: '2026-07-18T03:03:32.238115Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](README.md.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-PhotoView.swift.md)

# CloudPhotos (OS X).swift/CloudPhotos/MediaObjectToModDateTransformer.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 NSValueTransformer subclass for transforming MLMediaObject to it's modification date value.
 */

import Foundation
import MediaLibrary

class MediaObjectToModDateTransformer : ValueTransformer {
    func transformedValueClass() -> AnyClass {
        return CLLocation.self
    }

    func allowsReverseTransformation() -> Bool {
        return false
    }

    override func transformedValue(_ value: Any?) -> Any? {
        guard value != nil else { return nil }

        let mediaObject = value as! MLMediaObject
        let returnDate = mediaObject.attributes["modificationDate"]
        return returnDate
    }
}
```

[Next](README.md.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-PhotoView.swift.md)

