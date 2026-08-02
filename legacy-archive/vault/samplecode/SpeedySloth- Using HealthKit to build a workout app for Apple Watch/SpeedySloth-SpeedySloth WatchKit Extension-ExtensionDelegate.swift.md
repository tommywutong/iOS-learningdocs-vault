---
title: 'SpeedySloth: Using HealthKit to build a workout app for Apple Watch'
apple_id: TP40017338
resource_type: Sample Code
platform: watchOS
topic: null
technology: HealthKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SpeedySloth/Listings/SpeedySloth_SpeedySloth_WatchKit_Extension_ExtensionDelegate_swift.html
archived_at: '2026-07-18T03:25:18.277960Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SpeedySloth: Using HealthKit to build a workout app for Apple Watch](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)


[Next](SpeedySloth-SpeedySloth%20WatchKit%20Extension-HKQuantityTypeExtension.swift.md)[Previous](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)

# SpeedySloth/SpeedySloth WatchKit Extension/ExtensionDelegate.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Watch Kit Extension delegate.
 */

import WatchKit
import HealthKit

class ExtensionDelegate: NSObject, WKExtensionDelegate {
    // MARK: WKExtensionDelegate

    func handle(_ workoutConfiguration: HKWorkoutConfiguration) {
        WKInterfaceController.reloadRootControllers(withNames: ["WorkoutInterfaceController"], contexts: [workoutConfiguration])
    }
}
```

[Next](SpeedySloth-SpeedySloth%20WatchKit%20Extension-HKQuantityTypeExtension.swift.md)[Previous](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)

