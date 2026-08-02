---
title: 'MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control
  events'
apple_id: TP40017322
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MPRemoteCommandSample/Listings/MPRemoteCommandSample_TV_PlayerView_swift.html
archived_at: '2026-07-27T06:57:10.398613Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control events](MPRemoteCommandSample-%20Using%20MPRemoteCommandCenter%20respond%20to%20remote%20control%20eve.md)


[Next](MPRemoteCommandSample-TV-InitialViewController.swift.md)[Previous](MPRemoteCommandSample-TV-AppDelegate.swift.md)

# MPRemoteCommandSample-TV/PlayerView.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    `PlayerView` is a subclass of `UIView` with a layerClass of `AVPlayerLayer`.
 */

import UIKit
import AVFoundation

class PlayerView: UIView {

    // MARK: Properties

    /// The `AVPlayer` associated with the `AVPlayerLayer` of `PlayerView`.
    var player: AVPlayer? {
        get {
            return playerLayer().player
        }

        set {
            playerLayer().player = newValue
        }
    }

    override class var layerClass: AnyClass {
        return AVPlayerLayer.self
    }

    /// This is a convenience method for easily getting the layer associated with the `PlayerView` casted as an `AVPlayerLayer`.
    func playerLayer() -> AVPlayerLayer {
        return layer as! AVPlayerLayer
    }

}
```

[Next](MPRemoteCommandSample-TV-InitialViewController.swift.md)[Previous](MPRemoteCommandSample-TV-AppDelegate.swift.md)
