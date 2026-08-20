---
title: 'AVReaderWriter: Offline Audio / Video Processing'
apple_id: DTS40011124
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ReaderWriter/Listings/Swift_AVReaderWriter_ResultViewController_swift.html
archived_at: '2026-07-18T03:21:58.669218Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVReaderWriter: Offline Audio / Video Processing](AVReaderWriter-%20Offline%20Audio%20-%20Video%20Processing.md)


[Next](Document%20Revision%20History.md)[Previous](Swift-AVReaderWriter-StartViewController.swift.md)

# Swift/AVReaderWriter/ResultViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Defines the view controller for the result scene.
*/

import UIKit
import AVKit
import AVFoundation

class ResultViewController: UIViewController {
    // MARK: Properties

    private static let embedSegueName = "playerViewController"

    let player = AVPlayer()

    var outputURL: NSURL? {
        // Update `playerViewController` with new output movie.
        didSet {
            let playerItem: AVPlayerItem?

            if let outputURL = outputURL {
                playerItem = AVPlayerItem(URL: outputURL)
            }
            else {
                playerItem = nil
            }

            player.replaceCurrentItemWithPlayerItem(playerItem)
        }
    }

    // MARK: Segue Handling

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == ResultViewController.embedSegueName {
            // This segue fires before `viewDidLoad()` is invoked.
            let playerViewController = segue.destinationViewController as! AVPlayerViewController

            playerViewController.player = player
        }
        else {
            // Stop playback when transitioning to next scene.
            player.pause()
        }
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Swift-AVReaderWriter-StartViewController.swift.md)

