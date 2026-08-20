---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__OS_X__swift_CloudPhotos_MediaObjectToTitleTransformer_swift.html
archived_at: '2026-07-18T03:03:32.282125Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-MasterView.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-CloudPhotos-Bridging-Header.h.md)

# CloudPhotos (OS X).swift/CloudPhotos/MediaObjectToTitleTransformer.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 NSValueTransformer subclass for transforming MLMediaObject to it's name value.
 */

import Foundation
import MediaLibrary

class MediaObjectToTitleTransformer : ValueTransformer {
    func transformedValueClass() -> AnyClass {
        return NSString.self
    }

    func allowsReverseTransformation() -> Bool {
        return false
    }

    override func transformedValue(_ value: Any?) -> Any? {
        var title = String()

        guard value != nil else { return nil }

        let mediaObject = value as! MLMediaObject

        guard mediaObject.attributes["name"] != nil else {

            let url = mediaObject.url!

            // This URL might point outside the Pictures folder, so security scope it.
            if url.startAccessingSecurityScopedResource() {

                var imageTitleToUse : AnyObject?

                try! (url as NSURL).getPromisedItemResourceValue(&imageTitleToUse, forKey: URLResourceKey.localizedNameKey)
                url.stopAccessingSecurityScopedResource()

                title = imageTitleToUse as! String
            }
            return title
        }

        title = mediaObject.attributes["name"] as! String
        return title
    }
}
```

[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-MasterView.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-CloudPhotos-Bridging-Header.h.md)

