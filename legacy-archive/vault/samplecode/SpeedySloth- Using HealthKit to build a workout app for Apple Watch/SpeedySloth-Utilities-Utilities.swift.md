---
title: 'SpeedySloth: Using HealthKit to build a workout app for Apple Watch'
apple_id: TP40017338
resource_type: Sample Code
platform: watchOS
topic: null
technology: HealthKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SpeedySloth/Listings/SpeedySloth_Utilities_Utilities_swift.html
archived_at: '2026-07-18T03:25:18.620416Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SpeedySloth: Using HealthKit to build a workout app for Apple Watch](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)


[Next](SpeedySloth-SpeedySloth-WorkoutViewController.swift.md)[Previous](SpeedySloth-SpeedySloth%20WatchKit%20Extension-WorkoutInterfaceController.swift.md)

# SpeedySloth/Utilities/Utilities.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utilites for workout management and string formatting.
 */

import Foundation
import HealthKit

func computeDurationOfWorkout(withEvents workoutEvents: [HKWorkoutEvent]?, startDate: Date?, endDate: Date?) -> TimeInterval {
    var duration = 0.0

    if var lastDate = startDate {
        var paused = false

        if let events = workoutEvents {
            for event in events {
                switch event.type {
                    case .pause:
                        duration += event.date.timeIntervalSince(lastDate)
                        paused = true

                    case .resume:
                        lastDate = event.date
                        paused = false

                    default:
                        continue
                }
            }
        }

        if !paused {
            if let end = endDate {
                duration += end.timeIntervalSince(lastDate)
            } else {
                duration += NSDate().timeIntervalSince(lastDate)
            }
        }
    }

    print("\(duration)")
    return duration
}

func format(energy: HKQuantity) -> String {
    return String(format: "%.1f Calories", energy.doubleValue(for: HKUnit.kilocalorie()))
}

func format(distance: HKQuantity) -> String {
    return String(format: "%.1f Meters", distance.doubleValue(for: HKUnit.meter()))
}

func format(duration: TimeInterval) -> String {
    let durationFormatter = DateComponentsFormatter()
    durationFormatter.unitsStyle = .positional
    durationFormatter.allowedUnits = [.second, .minute, .hour]
    durationFormatter.zeroFormattingBehavior = .pad

    if let string = durationFormatter.string(from: duration) {
        return string
    } else {
        return ""
    }
}

func format(activityType: HKWorkoutActivityType) -> String {
    let formattedType : String

    switch activityType {
        case .walking:
            formattedType = "Walking"

        case .running:
            formattedType = "Running"

        case .hiking:
            formattedType = "Hiking"

        default:
            formattedType = "Workout"
    }

    return formattedType
}

func format(locationType: HKWorkoutSessionLocationType) -> String {
    let formattedType : String

    switch locationType {
        case .indoor:
            formattedType = "Indoor"

        case .outdoor:
            formattedType = "Outdoor"

        case .unknown:
            formattedType = "Unknown"
    }

    return formattedType
}
```

[Next](SpeedySloth-SpeedySloth-WorkoutViewController.swift.md)[Previous](SpeedySloth-SpeedySloth%20WatchKit%20Extension-WorkoutInterfaceController.swift.md)

