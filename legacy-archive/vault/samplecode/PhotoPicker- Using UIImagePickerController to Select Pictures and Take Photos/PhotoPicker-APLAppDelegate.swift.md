---
title: 'PhotoPicker: Using UIImagePickerController to Select Pictures and Take Photos'
apple_id: DTS40010196
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-01-11'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoPicker/Listings/PhotoPicker_APLAppDelegate_swift.html
archived_at: '2026-07-18T03:18:53.027529Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoPicker: Using UIImagePickerController to Select Pictures and Take Photos](PhotoPicker-%20Using%20UIImagePickerController%20to%20Select%20Pictures%20and%20Take%20Photos.md)


[Next](PhotoPicker-APLViewController.swift.md)[Previous](LICENSE.txt.md)

# PhotoPicker/APLAppDelegate.swift

```swift
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Standard application delegate.
*/

import UIKit

@UIApplicationMain
class APLAppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        return true
    }

    func applicationWillResignActive(_ application: UIApplication) {
        // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
        // Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.
        // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        // Called as part of the transition from the background to the inactive state; here you can undo many of the changes made on entering the background.
    }

    func applicationDidBecomeActive(_ application: UIApplication) {
        // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
    }

    func applicationWillTerminate(_ application: UIApplication) {
        // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
    }

}
```

[Next](PhotoPicker-APLViewController.swift.md)[Previous](LICENSE.txt.md)

