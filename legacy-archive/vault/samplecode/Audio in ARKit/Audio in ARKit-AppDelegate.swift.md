---
title: Audio in ARKit
apple_id: TP40017668
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: ARKit
published: '2018-03-28'
source_url: https://developer.apple.com/library/archive/samplecode/AudioInARKit/Listings/Audio_in_ARKit_AppDelegate_swift.html
archived_at: '2026-07-18T03:01:25.362315Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio in ARKit](Audio%20in%20ARKit.md)


[Next](Audio%20in%20ARKit-ARSCNView%2BHitTests.swift.md)[Previous](Audio%20in%20ARKit-ViewController.swift.md)

# Audio in ARKit/AppDelegate.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 App Delegate for the ARKit with audio sample.
 */

import UIKit
import ARKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
        guard ARWorldTrackingConfiguration.isSupported else {
            fatalError("""
                ARKit is not available on this device. For apps that require ARKit
                for core functionality, use the `arkit` key in the key in the
                `UIRequiredDeviceCapabilities` section of the Info.plist to prevent
                the app from installing. (If the app can't be installed, this error
                can't be triggered in a production scenario.)
                In apps where AR is an additive feature, use `isSupported` to
                determine whether to show UI for launching AR experiences.
                """) // For details, see https://developer.apple.com/documentation/arkit
        }

        return true
    }
}
```

[Next](Audio%20in%20ARKit-ARSCNView%2BHitTests.swift.md)[Previous](Audio%20in%20ARKit-ViewController.swift.md)

