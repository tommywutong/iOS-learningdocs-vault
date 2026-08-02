---
title: MotionGraphs
apple_id: DTS40012333
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreMotion
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/MotionGraphs/Listings/MotionGraphs_AppDelegate_swift.html
archived_at: '2026-07-18T03:16:01.617898Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MotionGraphs](MotionGraphs.md)


[Next](MotionGraphs-MotionGraphContainer.swift.md)[Previous](MotionGraphs-GyroscopeViewController.swift.md)

# MotionGraphs/AppDelegate.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate.
 */

import UIKit
import CoreMotion

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    let motionManager = CMMotionManager()

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        // Enumerate through the view controller hierarchy, setting the `motionManager`
        // property on those that conform to the `MotionGraphContainer` protocol.
        window?.rootViewController?.enumerateHierarchy { viewController in
            guard var container = viewController as? MotionGraphContainer else { return }
            container.motionManager = motionManager
        }

        return true
    }
}
```

[Next](MotionGraphs-MotionGraphContainer.swift.md)[Previous](MotionGraphs-GyroscopeViewController.swift.md)

