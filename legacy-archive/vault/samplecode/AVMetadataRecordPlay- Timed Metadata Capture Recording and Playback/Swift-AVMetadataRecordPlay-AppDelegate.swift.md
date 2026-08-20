---
title: 'AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback'
apple_id: TP40016165
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/AVMetadataRecordPlay/Listings/Swift_AVMetadataRecordPlay_AppDelegate_swift.html
archived_at: '2026-07-18T03:00:20.903178Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback](AVMetadataRecordPlay-%20Timed%20Metadata%20Capture%20Recording%20and%20Playback.md)


[Next](Swift-AVMetadataRecordPlay-AssetGridViewController.swift.md)[Previous](Swift-AVMetadataRecordPlay-PlayerViewController.swift.md)

# Swift/AVMetadataRecordPlay/AppDelegate.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Application delegate.
*/

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
        // We use the device orientation to set the video orientation of the video preview,
        // and to set the orientation of still images and recorded videos.

        // Inform the device that we want to use the device orientation.
        UIDevice.current.beginGeneratingDeviceOrientationNotifications()
        return true
    }

    func applicationWillTerminate(_ application: UIApplication) {
        // Inform the device that we no longer require access the device orientation.
        UIDevice.current.endGeneratingDeviceOrientationNotifications()
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        // Inform the device that we want to use the device orientation again.
        UIDevice.current.beginGeneratingDeviceOrientationNotifications()
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        // Let the device power down the accelerometer if not used elsewhere while backgrounded.
        UIDevice.current.endGeneratingDeviceOrientationNotifications()
    }
}
```

[Next](Swift-AVMetadataRecordPlay-AssetGridViewController.swift.md)[Previous](Swift-AVMetadataRecordPlay-PlayerViewController.swift.md)

