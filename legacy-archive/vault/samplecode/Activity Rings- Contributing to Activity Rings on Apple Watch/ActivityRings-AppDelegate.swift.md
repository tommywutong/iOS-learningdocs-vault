---
title: 'Activity Rings: Contributing to Activity Rings on Apple Watch'
apple_id: TP40016623
resource_type: Sample Code
platform: watchOS|iOS
topic: User Experience
technology: HealthKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ActivityRings/Listings/ActivityRings_AppDelegate_swift.html
archived_at: '2026-07-18T03:00:42.621726Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Activity Rings: Contributing to Activity Rings on Apple Watch](Activity%20Rings-%20Contributing%20to%20Activity%20Rings%20on%20Apple%20Watch.md)


[Next](LICENSE.txt.md)[Previous](ActivityRings-ViewController.swift.md)

# ActivityRings/AppDelegate.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The application delegate.
*/

import UIKit
import HealthKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?
    let healthStore: HKHealthStore = HKHealthStore()

    func applicationShouldRequestHealthAuthorization(_ application: UIApplication) {
        healthStore.handleAuthorizationForExtension { success, error in
            if let error = error, !success {
                print("You didn't allow HealthKit to access these read/write data types. In your app, try to handle this error gracefully when a user decides not to provide access. The error was: \(error.localizedDescription). If you're using a simulator, try it on a device.")
            }
        }
    }
}
```

[Next](LICENSE.txt.md)[Previous](ActivityRings-ViewController.swift.md)

