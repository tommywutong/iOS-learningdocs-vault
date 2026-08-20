---
title: NEHotspotConfiguration Sample
apple_id: TP40017679
resource_type: Sample Code
platform: iOS
topic: Networking, Internet, & Web
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/NEHotspotConfigurationSample/Listings/NEHotspotConfigurationSample_AppDelegate_swift.html
archived_at: '2026-07-18T03:16:44.306687Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NEHotspotConfiguration Sample](NEHotspotConfiguration%20Sample.md)


[Next](NEHotspotConfigurationSample-AddViewController.swift.md)[Previous](NEHotspotConfigurationSample-HotspotsViewController.swift.md)

# NEHotspotConfigurationSample/AppDelegate.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Main app controller.
 */

import UIKit

@UIApplicationMain
class AppDelegate : UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    /// A reference to the ‘model’ object that represents our hotspot
    /// configurations.

    var manager: HotspotManager! = nil

    func application(_ application: UIApplication, willFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {

        // Create and retain our model-level controller.  This vends hotspot
        // data in a way that’s easier for our view controller to use.

        self.manager = HotspotManager()

        // Create the main view controller (HotspotsViewController), inject
        // our manager into that, and then use it as the root of our navigation
        // hierarchy.

        let mainStoryboard = UIStoryboard(name: "Main", bundle: nil)
        let hotspots = mainStoryboard.instantiateViewController(withIdentifier: "hotspots") as! HotspotsViewController
        hotspots.manager = self.manager
        (self.window!.rootViewController! as! UINavigationController).viewControllers = [ hotspots ]

        return true
    }
}
```

[Next](NEHotspotConfigurationSample-AddViewController.swift.md)[Previous](NEHotspotConfigurationSample-HotspotsViewController.swift.md)

