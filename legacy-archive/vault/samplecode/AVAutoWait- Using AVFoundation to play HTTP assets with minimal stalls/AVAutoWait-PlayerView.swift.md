---
title: 'AVAutoWait: Using AVFoundation to play HTTP assets with minimal stalls'
apple_id: TP40017477
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AVAutoWait/Listings/AVAutoWait_PlayerView_swift.html
archived_at: '2026-07-18T03:00:01.008225Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVAutoWait: Using AVFoundation to play HTTP assets with minimal stalls](AVAutoWait-%20Using%20AVFoundation%20to%20play%20HTTP%20assets%20with%20minimal%20stalls.md)


[Next](AVAutoWait-PlaybackViewController.swift.md)[Previous](AVAutoWait-AppDelegate.swift.md)

# AVAutoWait/PlayerView.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Simple UIView subclass containing an AVPlayerLayer
*/

import UIKit
import AVFoundation

/// A very simple view only containing an AVPlayerLayer.
class PlayerView: UIView {

    static override var layerClass: AnyClass {
        return AVPlayerLayer.self
    }

    var player : AVPlayer? {
        set {
            let playerLayer = layer as! AVPlayerLayer
            playerLayer.player = newValue
        }

        get {
            let playerLayer = layer as! AVPlayerLayer
            return playerLayer.player
        }
    }
}
```

[Next](AVAutoWait-PlaybackViewController.swift.md)[Previous](AVAutoWait-AppDelegate.swift.md)

