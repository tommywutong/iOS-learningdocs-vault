---
title: 'AVFoundationPiPPlayer: Picture-in-Picture Playback with AVKit'
apple_id: TP40016166
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2018-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/AVFoundationPiPPlayer/Listings/AVFoundationPiPPlayer_AppDelegate_swift.html
archived_at: '2026-07-18T03:00:13.860737Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVFoundationPiPPlayer: Picture-in-Picture Playback with AVKit](AVFoundationPiPPlayer-%20Picture-in-Picture%20Playback%20with%20AVKit.md)


[Next](AVFoundationPiPPlayer-PlayerViewController.swift.md)[Previous](README.md.md)

# AVFoundationPiPPlayer/AppDelegate.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Main entry point to the application which sets up AVAudioSession for picture in picture.
*/

import UIKit
import AVFoundation

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    // MARK: Properties

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
        /*
            Setup audio session for picture in picture playback.
            Application has to be configured correctly to be able to initiate picture in picture.
            This configuration involves:

            1. Setting UIBackgroundMode to audio under the project settings.

            2. Setting audio session category to AVAudioSessionCategoryPlayback or AVAudioSessionCategoryPlayAndRecord (as appropriate)

            If an application is not configured correctly, AVPictureInPictureController.pictureInPicturePossible
            returns false.
        */
        let audioSession = AVAudioSession.sharedInstance()

        do {
            try audioSession.setCategory(AVAudioSessionCategoryPlayback)
        } catch {
            print("Audio session setCategory failed")
        }

        return true
    }
}
```

[Next](AVFoundationPiPPlayer-PlayerViewController.swift.md)[Previous](README.md.md)

