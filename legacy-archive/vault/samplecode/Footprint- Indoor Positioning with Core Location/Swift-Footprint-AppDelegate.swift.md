---
title: 'Footprint: Indoor Positioning with Core Location'
apple_id: TP40014457
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreLocation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/footprint/Listings/Swift_Footprint_AppDelegate_swift.html
archived_at: '2026-07-18T03:29:11.040514Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Footprint: Indoor Positioning with Core Location](Footprint-%20Indoor%20Positioning%20with%20Core%20Location.md)


[Next](Swift-Footprint-FloorplanOverlayRenderer.swift.md)[Previous](Swift-Footprint-VisibleMapRegionDelegate.swift.md)

# Swift/Footprint/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Main application delegate.
*/

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?


    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        return true
    }

    func applicationWillResignActive(_ application: UIApplication) {
        /*  
            Sent when the application is about to move from active to inactive
            state. This can occur for certain types of temporary interruptions
            (such as an incoming phone call or SMS message) or when the user
            quits the application and it begins the transition to the background
            state. Use this method to pause ongoing tasks, disable timers, and
            throttle down OpenGL ES frame rates. Games should use this method to
            pause the game.
        */
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        /* 
            Use this method to release shared resources, save user data, 
            invalidate timers, and store enough application state information to
            restore your application to its current state in case it is 
            terminated later. If your application supports background execution,
            this method is called instead of applicationWillTerminate: when the
            user quits.
        */
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        /*
            Called as part of the transition from the background to the inactive
            state; here you can undo many of the changes made on entering the
            background.
        */
    }

    func applicationDidBecomeActive(_ application: UIApplication) {
        /*
            Restart any tasks that were paused (or not yet started) while the
            application was inactive. If the application was previously in the
            background, optionally refresh the user interface.
        */
    }

    func applicationWillTerminate(_ application: UIApplication) {
        /*
            Called when the application is about to terminate. Save data if
            appropriate. See also applicationDidEnterBackground:.
        */
    }


}
```

[Next](Swift-Footprint-FloorplanOverlayRenderer.swift.md)[Previous](Swift-Footprint-VisibleMapRegionDelegate.swift.md)

