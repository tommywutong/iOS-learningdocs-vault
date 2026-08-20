---
title: 'MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control
  events'
apple_id: TP40017322
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MPRemoteCommandSample/Listings/MPRemoteCommandSample_macOS_AppDelegate_swift.html
archived_at: '2026-07-27T06:57:10.480364Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPRemoteCommandSample: Using MPRemoteCommandCenter respond to remote control events](MPRemoteCommandSample-%20Using%20MPRemoteCommandCenter%20respond%20to%20remote%20control%20eve.md)


[Next](MPRemoteCommandSample-macOS-AssetPlaybackViewController.swift.md)[Previous](MPRemoteCommandSample-macOS-WindowController.swift.md)

# MPRemoteCommandSample-macOS/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The Application's AppDelegate.
 */

import Cocoa

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {

    // MARK: Properties

    /// The instance of `AssetPlaybackManager` that the app uses for managing playback.
    let assetPlaybackManager = AssetPlaybackManager()

    /// The instance of `RemoteCommandManager` that the app uses for managing remote command events.
    var remoteCommandManager: RemoteCommandManager!

    // MARK: Application Life Cycle Methods

    func applicationDidFinishLaunching(_ aNotification: Notification) {

        // Initializer the `RemoteCommandManager`.
        remoteCommandManager = RemoteCommandManager(assetPlaybackManager: assetPlaybackManager)

        // Always enable playback commands in MPRemoteCommandCenter.
        remoteCommandManager.activatePlaybackCommands(true)

        // Inject dependencies needed by the app.
        guard let splitViewController = NSApplication.shared().windows.first?.windowController?.contentViewController as? SplitViewController,
            let remoteCommandConfigurationViewController = splitViewController.splitViewItems.first?.viewController as? RemoteCommandConfigurationViewController,
            let assetPlaybackViewController = splitViewController.splitViewItems.last?.viewController as? AssetPlaybackViewController else { return }

        assetPlaybackViewController.assetPlaybackManager = assetPlaybackManager
        remoteCommandConfigurationViewController.remoteCommandDataSource = RemoteCommandDataSource(remoteCommandManager: remoteCommandManager)
    }

    func applicationWillTerminate(_ aNotification: Notification) {
        // Insert code here to tear down your application
    }
}
```

[Next](MPRemoteCommandSample-macOS-AssetPlaybackViewController.swift.md)[Previous](MPRemoteCommandSample-macOS-WindowController.swift.md)
