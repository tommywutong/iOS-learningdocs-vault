---
title: 'PhotoTransitioning: Using UIViewPropertyAnimator to create a fully interative
  and interruptible custom view controller transition'
apple_id: TP40017554
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoTransitioning/Listings/Photo_Transitioning_AppDelegate_swift.html
archived_at: '2026-07-18T03:18:55.360640Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoTransitioning: Using UIViewPropertyAnimator to create a fully interative and interruptible custom view controller transition](PhotoTransitioning-%20Using%20UIViewPropertyAnimator%20to%20create%20a%20fully%20interative%20an.md)


[Next](Photo%20Transitioning-AssetTransitioning.swift.md)[Previous](Photo%20Transitioning-AssetCell.swift.md)

# Photo Transitioning/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The application delegate.
*/

import UIKit


@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    var navigationController: UINavigationController!

    var transitionController: AssetTransitionController!


    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]? = [:]) -> Bool {
        let window = UIWindow(frame: UIScreen.main.bounds)

        navigationController = UINavigationController(rootViewController: AssetViewController(layoutStyle: .grid))
        transitionController = AssetTransitionController(navigationController: navigationController)

        window.rootViewController = navigationController
        navigationController.delegate = transitionController

        window.makeKeyAndVisible()
        self.window = window

        return true
    }
}
```

[Next](Photo%20Transitioning-AssetTransitioning.swift.md)[Previous](Photo%20Transitioning-AssetCell.swift.md)

