---
title: 'AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback'
apple_id: TP40016165
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/AVMetadataRecordPlay/Listings/Swift_AVMetadataRecordPlay_PreviewView_swift.html
archived_at: '2026-07-18T03:00:21.637527Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback](AVMetadataRecordPlay-%20Timed%20Metadata%20Capture%20Recording%20and%20Playback.md)


[Next](Document%20Revision%20History.md)[Previous](Swift-AVMetadataRecordPlay-AssetGridViewCell.swift.md)

# Swift/AVMetadataRecordPlay/PreviewView.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Camera preview view.
*/

import UIKit
import AVFoundation

class PreviewView: UIView {
    var videoPreviewLayer: AVCaptureVideoPreviewLayer {
        return layer as! AVCaptureVideoPreviewLayer
    }

    var session: AVCaptureSession? {
        get {
            return videoPreviewLayer.session
        }
        set {
            videoPreviewLayer.session = newValue
        }
    }

    // MARK: UIView

    override class var layerClass: AnyClass {
        return AVCaptureVideoPreviewLayer.self
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Swift-AVMetadataRecordPlay-AssetGridViewCell.swift.md)

