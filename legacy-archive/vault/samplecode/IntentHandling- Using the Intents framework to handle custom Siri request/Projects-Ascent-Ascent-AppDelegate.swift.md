---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_Ascent_AppDelegate_swift.html
archived_at: '2026-07-18T03:13:00.922647Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-Ascent-WorkoutsController.swift.md)[Previous](Projects-Payments-PaymentsIntentsExtension-IntentsExtension.swift.md)

# Projects/Ascent/Ascent/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The application delegate.
*/

import UIKit
import Intents
import AscentFramework

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([Any]?) -> Void) -> Bool {
        // Pass the activity to the `WorkoutsController` to handle.
        if let navigationController = window?.rootViewController as? UINavigationController {
            restorationHandler(navigationController.viewControllers)
        }

        return true
    }
}
```

[Next](Projects-Ascent-Ascent-WorkoutsController.swift.md)[Previous](Projects-Payments-PaymentsIntentsExtension-IntentsExtension.swift.md)

