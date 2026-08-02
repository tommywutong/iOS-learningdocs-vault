---
title: 'LoopHealth: Using health documents and Activity rings in HealthKit and HealthKitUI'
apple_id: TP40017553
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: null
published: '2016-12-02'
source_url: https://developer.apple.com/library/archive/samplecode/LoopHealth/Listings/LoopHealth_AppDelegate_swift.html
archived_at: '2026-07-18T03:13:49.960363Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LoopHealth: Using health documents and Activity rings in HealthKit and HealthKitUI](LoopHealth-%20Using%20health%20documents%20and%20Activity%20rings%20in%20HealthKit%20and%20HealthKit.md)


[Next](LoopHealth-RecordsDetailViewController.swift.md)[Previous](LoopHealth-RecordsListTableViewController.swift.md)

# LoopHealth/AppDelegate.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom app delegate for the LoopHealth app. Manages an app-wide `HKHealthStore` instance.
 */

import UIKit
import HealthKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    // MARK: Properties

    var window: UIWindow?

    let healthStore: HKHealthStore

    // MARK: - Initializers

    override init() {
        guard HKHealthStore.isHealthDataAvailable() else { fatalError("This app requires a device that supports HealthKit") }

        healthStore = HKHealthStore()
    }

    // MARK: UIApplicationDelegate

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
        // Enumerate the view controller heirarchy, setting the health store where appropriate.
        window?.rootViewController?.enumerateHierarchy { viewController in
            guard var healthStoreContainer = viewController as? HealthStoreContainer else { return }
            healthStoreContainer.healthStore = healthStore
        }

        return true
    }
}
```

[Next](LoopHealth-RecordsDetailViewController.swift.md)[Previous](LoopHealth-RecordsListTableViewController.swift.md)

