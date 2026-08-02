---
title: 'SpeedySloth: Using HealthKit to build a workout app for Apple Watch'
apple_id: TP40017338
resource_type: Sample Code
platform: watchOS
topic: null
technology: HealthKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SpeedySloth/Listings/SpeedySloth_SpeedySloth_WatchKit_Extension_SummaryInterfaceController_swift.html
archived_at: '2026-07-18T03:25:18.403992Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SpeedySloth: Using HealthKit to build a workout app for Apple Watch](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)


[Next](SpeedySloth-SpeedySloth%20WatchKit%20Extension-ConfigurationInterfaceController.swif.md)[Previous](SpeedySloth-SpeedySloth%20WatchKit%20Extension-HKQuantityTypeExtension.swift.md)

# SpeedySloth/SpeedySloth WatchKit Extension/SummaryInterfaceController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Interface controller for the workout summary screen.
 */

import WatchKit
import Foundation
import HealthKit

class SummaryInterfaceController: WKInterfaceController {
    // MARK: Properties
    var workout: HKWorkout?

    // MARK: IB Outlets

    @IBOutlet var workoutLabel: WKInterfaceLabel!

    @IBOutlet var durationLabel: WKInterfaceLabel!

    @IBOutlet var caloriesLabel: WKInterfaceLabel!

    @IBOutlet var distanceLabel: WKInterfaceLabel!

    // MARK: Interface Controller Overrides

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)

        workout = context as? HKWorkout

        setTitle("Summary")
    }

    override func willActivate() {
        super.willActivate()

        guard let workout = workout else { return }

        workoutLabel.setText("\(format(activityType: workout.workoutActivityType))")
        caloriesLabel.setText(format(energy: workout.totalEnergyBurned!))
        distanceLabel.setText(format(distance: workout.totalDistance!))

        let duration = computeDurationOfWorkout(withEvents: workout.workoutEvents, startDate: workout.startDate, endDate: workout.endDate)
        durationLabel.setText(format(duration: duration))
    }

    @IBAction func didTapDoneButton() {
        WKInterfaceController.reloadRootControllers(withNames: ["ConfigurationInterfaceController"], contexts: nil)
    }
}
```

[Next](SpeedySloth-SpeedySloth%20WatchKit%20Extension-ConfigurationInterfaceController.swif.md)[Previous](SpeedySloth-SpeedySloth%20WatchKit%20Extension-HKQuantityTypeExtension.swift.md)

