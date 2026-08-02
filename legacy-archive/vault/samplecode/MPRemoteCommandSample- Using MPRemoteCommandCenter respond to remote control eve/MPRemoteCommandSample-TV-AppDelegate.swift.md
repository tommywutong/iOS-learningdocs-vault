---
title: 'MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control
  events'
apple_id: TP40017322
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MPRemoteCommandSample/Listings/MPRemoteCommandSample_TV_AppDelegate_swift.html
archived_at: '2026-07-27T06:57:10.393094Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control events](MPRemoteCommandSample-%20Using%20MPRemoteCommandCenter%20respond%20to%20remote%20control%20eve.md)


[Next](MPRemoteCommandSample-TV-PlayerView.swift.md)[Previous](MPRemoteCommandSample-TV-PlayerViewController.swift.md)

# MPRemoteCommandSample-TV/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The Application's AppDelegate, contains basic `AVAudioSession` setup.
 */

import UIKit
import AVFoundation

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    // MARK: Properties

    var window: UIWindow?

    /// The instance of `AssetPlaybackManager` that the app uses for managing playback.
    let assetPlaybackManager = AssetPlaybackManager()

    /// The instance of `RemoteCommandManager` that the app uses for managing remote command events.
    var remoteCommandManager: RemoteCommandManager!

    // MARK: Application Life Cycle

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

        // Initializer the `RemoteCommandManager`.
        remoteCommandManager = RemoteCommandManager(assetPlaybackManager: assetPlaybackManager)

        // Always enable playback commands in MPRemoteCommandCenter.
        remoteCommandManager.activateRemoteCommands(true)

        // Setup AVAudioSession.
        let audioSession = AVAudioSession.sharedInstance()

        do {
            try audioSession.setCategory(AVAudioSessionCategoryPlayback, mode: AVAudioSessionModeDefault)
        } catch {
            print("An error occured setting the audio session category: \(error)")
        }

        // Set the AVAudioSession as active.
        do {
            try audioSession.setActive(true, with: [])
        } catch {
            print("An Error occured activating the audio session: \(error)")
        }

        // Inject dependencies needed by the app.

        guard let initialViewController = window?.rootViewController as? InitialViewController else { return true }

        initialViewController.assetPlaybackManager = assetPlaybackManager

        return true
    }
}
```

[Next](MPRemoteCommandSample-TV-PlayerView.swift.md)[Previous](MPRemoteCommandSample-TV-PlayerViewController.swift.md)
