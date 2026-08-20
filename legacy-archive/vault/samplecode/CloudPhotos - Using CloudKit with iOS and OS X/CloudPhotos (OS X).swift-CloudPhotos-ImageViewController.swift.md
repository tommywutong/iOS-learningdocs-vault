---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__OS_X__swift_CloudPhotos_ImageViewController_swift.html
archived_at: '2026-07-18T03:03:31.729210Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-MediaObjectToImageTransformer.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-MasterView.swift.md)

# CloudPhotos (OS X).swift/CloudPhotos/ImageViewController.swift

```swift
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
View controller that shows the photo in a popover.
*/

import Cocoa
import Foundation

class ImageViewController : NSViewController {
    // MARK: - Properties

    var image: NSImage!
    @IBOutlet private weak var imageView: NSImageView!

    // MARK: - View Controller Lifecycle

    override func viewDidAppear() {
        super.viewDidAppear()

        guard image != nil else { return }

        imageView.image = image
    }
}
```

[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-MediaObjectToImageTransformer.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-MasterView.swift.md)

