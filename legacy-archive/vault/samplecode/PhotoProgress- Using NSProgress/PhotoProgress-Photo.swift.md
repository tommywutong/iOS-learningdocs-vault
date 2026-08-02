---
title: 'PhotoProgress: Using NSProgress'
apple_id: TP40016186
resource_type: Sample Code
platform: iOS
topic: null
technology: Foundation
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoProgress/Listings/PhotoProgress_Photo_swift.html
archived_at: '2026-07-18T03:18:53.654646Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoProgress: Using NSProgress](PhotoProgress-%20Using%20NSProgress.md)


[Next](PhotoProgress-PhotoFilter.swift.md)[Previous](PhotoProgress-PhotosViewController.swift.md)

# PhotoProgress/Photo.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
                Photo represents an image that can be imported.

*/

import UIKit

class Photo: NSObject {
    // MARK: Properties

    let imageURL: URL

    /// Marked "dynamic" so it is KVO observable.
    dynamic var image: UIImage?

    /// The photoImport is KVO observable for its progress.
    dynamic var photoImport: PhotoImport?

    // MARK: Initializers

    init(URL: Foundation.URL) {
        imageURL = (URL as NSURL).copy() as! Foundation.URL

        image = UIImage(named: "PhotoPlaceholder")
    }

    /// Kick off the import
    func startImport() -> Progress {
        let newImport = PhotoImport(URL: imageURL)

        newImport.completionHandler = { image, error in
            if let image = image {
                // The import is finished. Set our image to the result
                self.image = image
            }
            else {
                self.reportError(error!)
            }

            self.photoImport = nil
        }

        newImport.start()

        photoImport = newImport

        return newImport.progress
    }

    fileprivate func reportError(_ error: NSError) {
        if error.domain != NSCocoaErrorDomain || error.code != NSUserCancelledError {
            print("Error importing photo: \(error.localizedDescription)")
        }
    }

    /// Go back to the initial state.
    func reset() {
        image = UIImage(named: "PhotoPlaceholder")
        photoImport = nil
    }
}
```

[Next](PhotoProgress-PhotoFilter.swift.md)[Previous](PhotoProgress-PhotosViewController.swift.md)

