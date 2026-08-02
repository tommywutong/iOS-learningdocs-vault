---
title: 'SpeedySloth: Using HealthKit to build a workout app for Apple Watch'
apple_id: TP40017338
resource_type: Sample Code
platform: watchOS
topic: null
technology: HealthKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SpeedySloth/Listings/SpeedySloth_SpeedySloth_AppDelegate_swift.html
archived_at: '2026-07-18T03:25:18.117898Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SpeedySloth: Using HealthKit to build a workout app for Apple Watch](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)


[Next](SpeedySloth-SpeedySloth-ConfigurationViewController.swift.md)[Previous](SpeedySloth-SpeedySloth-WorkoutViewController.swift.md)

# SpeedySloth/SpeedySloth/AppDelegate.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 UIApplication delegate.
 */

import UIKit
import HealthKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?


    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
        self.requestAccessToHealthKit()
        return true
    }

    private func requestAccessToHealthKit() {
        let healthStore = HKHealthStore()

        let allTypes = Set([HKObjectType.workoutType(),
                            HKObjectType.quantityType(forIdentifier: HKQuantityTypeIdentifier.activeEnergyBurned)!,
                            HKObjectType.quantityType(forIdentifier: HKQuantityTypeIdentifier.distanceCycling)!,
                            HKObjectType.quantityType(forIdentifier: HKQuantityTypeIdentifier.distanceWalkingRunning)!,
                            HKObjectType.quantityType(forIdentifier: HKQuantityTypeIdentifier.heartRate)!])

        healthStore.requestAuthorization(toShare: allTypes, read: allTypes) { (success, error) in
            if !success {
                print(error)
            }
        }
    }
}
```

[Next](SpeedySloth-SpeedySloth-ConfigurationViewController.swift.md)[Previous](SpeedySloth-SpeedySloth-WorkoutViewController.swift.md)

