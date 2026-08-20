---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__OS_X__swift_CloudPhotos_MediaObjectToLocationTransformer_swift.html
archived_at: '2026-07-18T03:03:32.199785Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-AppDelegate.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-WindowController.swift.md)

# CloudPhotos (OS X).swift/CloudPhotos/MediaObjectToLocationTransformer.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 NSValueTransformer subclass for transforming MLMediaObject to it's CLLocation value.
 */

import Foundation
import MediaLibrary

class MediaObjectToLocationTransformer : ValueTransformer {
    func transformedValueClass() -> AnyClass {
        return CLLocation.self
    }

    func allowsReverseTransformation() -> Bool {
        return false
    }

    override func transformedValue(_ value: Any?) -> Any? {
        guard value != nil else { return nil }

        let mediaObject = value as! MLMediaObject

        // Convert the latitude/longitude values from the media object to a CLLocation object.
        var returnLocation : CLLocation?
        if let latitude = mediaObject.attributes["latitude"] {
            if let longitude = mediaObject.attributes["longitude"] {
                returnLocation = CLLocation(latitude: (latitude as! NSNumber).doubleValue, longitude: (longitude as! NSNumber).doubleValue)
            }
        }

        return returnLocation
    }
}
```

[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-AppDelegate.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-WindowController.swift.md)

