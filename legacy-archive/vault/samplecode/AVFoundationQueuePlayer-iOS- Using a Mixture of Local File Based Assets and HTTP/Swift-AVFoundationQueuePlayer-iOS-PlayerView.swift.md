---
title: 'AVFoundationQueuePlayer-iOS: Using a Mixture of Local File Based Assets and
  HTTP Live Streaming Assets with AVFoundation'
apple_id: TP40016104
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AVFoundationQueuePlayer-iOS/Listings/Swift_AVFoundationQueuePlayer_iOS_PlayerView_swift.html
archived_at: '2026-07-18T03:00:15.148402Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVFoundationQueuePlayer-iOS: Using a Mixture of Local File Based Assets and HTTP Live Streaming Assets with AVFoundation](AVFoundationQueuePlayer-iOS-%20Using%20a%20Mixture%20of%20Local%20File%20Based%20Assets%20and%20HTTP.md)


[Next](Document%20Revision%20History.md)[Previous](Swift-AVFoundationQueuePlayer-iOS-QueuedItemCollectionViewCell.swift.md)

# Swift/AVFoundationQueuePlayer-iOS/PlayerView.swift

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

[Next](Document%20Revision%20History.md)[Previous](Swift-AVFoundationQueuePlayer-iOS-QueuedItemCollectionViewCell.swift.md)

