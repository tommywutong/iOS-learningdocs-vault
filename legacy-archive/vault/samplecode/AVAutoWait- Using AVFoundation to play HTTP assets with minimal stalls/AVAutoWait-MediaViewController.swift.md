---
title: 'AVAutoWait: Using AVFoundation to play HTTP assets with minimal stalls'
apple_id: TP40017477
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AVAutoWait/Listings/AVAutoWait_MediaViewController_swift.html
archived_at: '2026-07-18T03:00:00.691655Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVAutoWait: Using AVFoundation to play HTTP assets with minimal stalls](AVAutoWait-%20Using%20AVFoundation%20to%20play%20HTTP%20assets%20with%20minimal%20stalls.md)


[Next](Document%20Revision%20History.md)[Previous](AVAutoWait-PlaybackDetailsViewController.swift.md)

# AVAutoWait/MediaViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    View controller that displays a single selected media item.
*/

import UIKit
import AVFoundation

/// View controller that combines both a `PlaybackViewController` and a `PlaybackDetailsViewController`.
class MediaViewController: UIViewController {
    // MARK: Properties

    @IBOutlet var stackView: UIStackView!

    private var playbackViewController: PlaybackViewController!
    private var playbackDetailsViewController: PlaybackDetailsViewController!
    private let player = AVPlayer()

    var mediaURL: URL? {
        didSet {
            // Create a new item for our AVPlayer
            updatePlayerItem()
        }
    }

    // MARK: UIViewController

    override func viewDidLoad() {
        super.viewDidLoad()

        // Make sure our AVPlayer has an AVPlayerItem if we already got a URL
        updatePlayerItem()

        // Setup sub-view controllers.
        // 1) A PlaybackViewController for the video and playback controls.
        playbackViewController = storyboard?.instantiateViewController(withIdentifier: "Playback") as! PlaybackViewController
        playbackViewController.player = player

        // 2) A PlaybackDetailsViewController for property values.
        playbackDetailsViewController = storyboard?.instantiateViewController(withIdentifier: "PlaybackDetails") as! PlaybackDetailsViewController
        playbackDetailsViewController.player = player

        // Add both new views to our stackView.
        stackView.addArrangedSubview(playbackViewController.view)
        stackView.addArrangedSubview(playbackDetailsViewController.view)
    }

    // MARK: Convenience

    private func updatePlayerItem() {
        if let mediaURL = mediaURL {
            player.replaceCurrentItem(with: AVPlayerItem(url: mediaURL))
        }
        else {
            player.replaceCurrentItem(with: nil)
        }
    }

}
```

[Next](Document%20Revision%20History.md)[Previous](AVAutoWait-PlaybackDetailsViewController.swift.md)

