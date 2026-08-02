---
title: 'AVFoundationSimplePlayer-iOS: Using AVFoundation to Play Media'
apple_id: TP40016103
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AVFoundationSimplePlayer-iOS/Listings/Swift_AVFoundationSimplePlayer_iOS_PlayerView_swift.html
archived_at: '2026-07-18T03:00:16.009751Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVFoundationSimplePlayer-iOS: Using AVFoundation to Play Media](AVFoundationSimplePlayer-iOS-%20Using%20AVFoundation%20to%20Play%20Media.md)


[Next](Document%20Revision%20History.md)[Previous](Swift-AVFoundationSimplePlayer-iOS-AppDelegate.swift.md)

# Swift/AVFoundationSimplePlayer-iOS/PlayerView.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Player view backed by an AVPlayerLayer.
*/

import UIKit
import AVFoundation

/// A simple `UIView` subclass that is backed by an `AVPlayerLayer` layer.
class PlayerView: UIView {
    var player: AVPlayer? {
        get {
            return playerLayer.player
        }

        set {
            playerLayer.player = newValue
        }
    }

    var playerLayer: AVPlayerLayer {
        return layer as! AVPlayerLayer
    }

    override class var layerClass: AnyClass {
        return AVPlayerLayer.self
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Swift-AVFoundationSimplePlayer-iOS-AppDelegate.swift.md)

