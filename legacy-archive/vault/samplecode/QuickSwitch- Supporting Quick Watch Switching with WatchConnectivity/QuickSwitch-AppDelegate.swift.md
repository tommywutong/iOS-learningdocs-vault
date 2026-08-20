---
title: 'QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity'
apple_id: TP40016647
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: WatchConnectivity
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/QuickSwitch/Listings/QuickSwitch_AppDelegate_swift.html
archived_at: '2026-07-18T03:21:46.122142Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity](QuickSwitch-%20Supporting%20Quick%20Watch%20Switching%20with%20WatchConnectivity.md)


[Next](Shared-WatchConnectivityManager.swift.md)[Previous](QuickSwitch-ViewController.swift.md)

# QuickSwitch/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The application delegate.
*/

import UIKit
import WatchConnectivity

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    // MARK: Properties

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]?) -> Bool {
        if WCSession.isSupported() {
            let defaultSession = WCSession.default()
            defaultSession.delegate = WatchConnectivityManager.sharedConnectivityManager
            defaultSession.activate()
        }

        return true
    }
}
```

[Next](Shared-WatchConnectivityManager.swift.md)[Previous](QuickSwitch-ViewController.swift.md)

