---
title: 'MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control
  events'
apple_id: TP40017322
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MPRemoteCommandSample/Listings/MPRemoteCommandSample_TV_PlayerViewController_swift.html
archived_at: '2026-07-27T06:57:10.383895Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control events](MPRemoteCommandSample-%20Using%20MPRemoteCommandCenter%20respond%20to%20remote%20control%20eve.md)


[Next](MPRemoteCommandSample-TV-AppDelegate.swift.md)[Previous](README.md.md)

# MPRemoteCommandSample-TV/PlayerViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    `PlayerViewController` is a subclass of `UIViewController` with a `PlayerView` as its `view` and is used to play the HLS asset
 */

import UIKit
import AVFoundation

class PlayerViewController: UIViewController {

    // MARK: Properties

    var playerView: PlayerView {
        get {
            return view as! PlayerView
        }
    }
}
```

[Next](MPRemoteCommandSample-TV-AppDelegate.swift.md)[Previous](README.md.md)
