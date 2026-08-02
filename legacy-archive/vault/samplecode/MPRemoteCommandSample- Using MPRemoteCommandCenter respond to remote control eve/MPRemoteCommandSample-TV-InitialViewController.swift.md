---
title: 'MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control
  events'
apple_id: TP40017322
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MPRemoteCommandSample/Listings/MPRemoteCommandSample_TV_InitialViewController_swift.html
archived_at: '2026-07-27T06:57:10.449710Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control events](MPRemoteCommandSample-%20Using%20MPRemoteCommandCenter%20respond%20to%20remote%20control%20eve.md)


[Next](LICENSE.txt.md)[Previous](MPRemoteCommandSample-TV-PlayerView.swift.md)

# MPRemoteCommandSample-TV/InitialViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    `InitialViewController` is the initial `UIViewController` that prepares an HLS asset for playback in a `PlayerViewController`.
 */

import UIKit
import AVFoundation

class InitialViewController: UIViewController {

    // MARK: Properties

    /// The instance of `AssetPlaybackManager` to use for playing an `Asset`.
    var assetPlaybackManager: AssetPlaybackManager!

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {

        guard segue.identifier == "presentPlayerViewControllerSegue", let playerViewController = segue.destination as? PlayerViewController else { return }

        // Create an `Asset` representing the HLS stream being used for playback.
        let url = URL(string: "https://devimages.apple.com.edgekey.net/streaming/examples/bipbop_16x9/bipbop_16x9_variant.m3u8")!
        let urlAsset = AVURLAsset(url: url)
        let asset = Asset(assetName: "Video Asset", urlAsset: urlAsset)

        // Set that `Asset` as the currently playing item.
        assetPlaybackManager.asset = asset

        // Provide the `PlayerView` of the destination `PlayerViewController` with the player for playback.
        playerViewController.playerView.player = assetPlaybackManager.player
    }
}
```

[Next](LICENSE.txt.md)[Previous](MPRemoteCommandSample-TV-PlayerView.swift.md)
