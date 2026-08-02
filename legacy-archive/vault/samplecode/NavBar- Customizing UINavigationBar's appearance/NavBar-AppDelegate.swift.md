---
title: 'NavBar: Customizing UINavigationBar''s appearance'
apple_id: DTS40007418
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2017-12-07'
source_url: https://developer.apple.com/library/archive/samplecode/NavBar/Listings/NavBar_AppDelegate_swift.html
archived_at: '2026-07-18T03:16:52.763869Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NavBar: Customizing UINavigationBar's appearance](NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md)


[Next](NavBar-ExtendedNavBar-ExtendedNavBarViewController.swift.md)[Previous](NavBar-CitiesDataSource.swift.md)

# NavBar/AppDelegate.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate class.
 */

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, UINavigationControllerDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]?) -> Bool {
        (window!.rootViewController as! UINavigationController).delegate = self

        return true
    }

    // MARK: - UINavigationControllerDelegate

    /**  
     *  Force the navigation controller to defer to the topViewController for
     *  its supportedInterfaceOrientations.  This allows some of the demos
     *  to rotate into landscape while keeping the rest in portrait.
     */
    func navigationControllerSupportedInterfaceOrientations(_ navigationController: UINavigationController) -> UIInterfaceOrientationMask {
        return navigationController.topViewController!.supportedInterfaceOrientations
    }
}
```

[Next](NavBar-ExtendedNavBar-ExtendedNavBarViewController.swift.md)[Previous](NavBar-CitiesDataSource.swift.md)

