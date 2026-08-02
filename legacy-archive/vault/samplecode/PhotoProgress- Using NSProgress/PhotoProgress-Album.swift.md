---
title: 'PhotoProgress: Using NSProgress'
apple_id: TP40016186
resource_type: Sample Code
platform: iOS
topic: null
technology: Foundation
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoProgress/Listings/PhotoProgress_Album_swift.html
archived_at: '2026-07-18T03:18:53.350902Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoProgress: Using NSProgress](PhotoProgress-%20Using%20NSProgress.md)


[Next](PhotoProgress-PhotosViewController.swift.md)[Previous](PhotoProgress-PhotoDownload.swift.md)

# PhotoProgress/Album.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
                Album has an array of Photos loaded from the application bundle

*/

import UIKit

class Album: NSObject {
    // MARK: Properties

    let photos: [Photo]

    // MARK: Initializers

    override init () {
        guard let imageURLs = Bundle.main.urls(forResourcesWithExtension: "jpg", subdirectory: "Photos") else {
            fatalError("Unable to load photos")
        }

        photos = imageURLs.map { Photo(URL: $0) }
    }

    func importPhotos() -> Progress {
        let progress = Progress()
        progress.totalUnitCount = Int64(photos.count)

        for photo in photos {
            let importProgress = photo.startImport()

            progress.addChild(importProgress, withPendingUnitCount: 1)
        }

        return progress
    }

    func resetPhotos() {
        for photo in photos {
            photo.reset()
        }
    }
}
```

[Next](PhotoProgress-PhotosViewController.swift.md)[Previous](PhotoProgress-PhotoDownload.swift.md)

