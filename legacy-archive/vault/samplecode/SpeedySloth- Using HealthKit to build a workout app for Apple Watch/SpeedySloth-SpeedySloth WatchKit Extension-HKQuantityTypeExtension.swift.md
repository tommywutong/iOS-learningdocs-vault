---
title: 'SpeedySloth: Using HealthKit to build a workout app for Apple Watch'
apple_id: TP40017338
resource_type: Sample Code
platform: watchOS
topic: null
technology: HealthKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SpeedySloth/Listings/SpeedySloth_SpeedySloth_WatchKit_Extension_HKQuantityTypeExtension_swift.html
archived_at: '2026-07-18T03:25:18.318516Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SpeedySloth: Using HealthKit to build a workout app for Apple Watch](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)


[Next](SpeedySloth-SpeedySloth%20WatchKit%20Extension-SummaryInterfaceController.swift.md)[Previous](SpeedySloth-SpeedySloth%20WatchKit%20Extension-ExtensionDelegate.swift.md)

# SpeedySloth/SpeedySloth WatchKit Extension/HKQuantityTypeExtension.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utilites for quantity types.
 */

import Foundation
import HealthKit

extension HKQuantityType {
    static func distanceWalkingRunning() -> HKQuantityType {
        return HKObjectType.quantityType(forIdentifier: HKQuantityTypeIdentifier.distanceWalkingRunning)!
    }

    static func distanceCycling() -> HKQuantityType {
        return HKObjectType.quantityType(forIdentifier: HKQuantityTypeIdentifier.distanceCycling)!
    }

    static func activeEnergyBurned() -> HKQuantityType {
        return HKObjectType.quantityType(forIdentifier: HKQuantityTypeIdentifier.activeEnergyBurned)!
    }

    static func heartRate() -> HKQuantityType {
        return HKObjectType.quantityType(forIdentifier: HKQuantityTypeIdentifier.heartRate)!
    }
}
```

[Next](SpeedySloth-SpeedySloth%20WatchKit%20Extension-SummaryInterfaceController.swift.md)[Previous](SpeedySloth-SpeedySloth%20WatchKit%20Extension-ExtensionDelegate.swift.md)

