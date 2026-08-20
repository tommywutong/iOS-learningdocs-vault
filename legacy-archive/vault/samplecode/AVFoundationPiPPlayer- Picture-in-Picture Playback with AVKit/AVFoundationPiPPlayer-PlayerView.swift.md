---
title: 'AVFoundationPiPPlayer: Picture-in-Picture Playback with AVKit'
apple_id: TP40016166
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2018-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/AVFoundationPiPPlayer/Listings/AVFoundationPiPPlayer_PlayerView_swift.html
archived_at: '2026-07-18T03:00:14.063182Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVFoundationPiPPlayer: Picture-in-Picture Playback with AVKit](AVFoundationPiPPlayer-%20Picture-in-Picture%20Playback%20with%20AVKit.md)


[Next](LICENSE.txt.md)[Previous](AVFoundationPiPPlayer-PlayerViewController.swift.md)

# AVFoundationPiPPlayer/PlayerView.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Player view  is a subclass of UIView used for playback.
*/

import UIKit
import AVFoundation

class PlayerView: UIView {
    // MARK: Properties

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

[Next](LICENSE.txt.md)[Previous](AVFoundationPiPPlayer-PlayerViewController.swift.md)

