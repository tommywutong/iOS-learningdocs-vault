---
title: 'SpeedySloth: Using HealthKit to build a workout app for Apple Watch'
apple_id: TP40017338
resource_type: Sample Code
platform: watchOS
topic: null
technology: HealthKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SpeedySloth/Listings/SpeedySloth_SpeedySloth_WatchKit_Extension_ConfigurationInterfaceController_swift.html
archived_at: '2026-07-18T03:25:18.217753Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SpeedySloth: Using HealthKit to build a workout app for Apple Watch](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)


[Next](SpeedySloth-SpeedySloth%20WatchKit%20Extension-ParentConnector.swift.md)[Previous](SpeedySloth-SpeedySloth%20WatchKit%20Extension-SummaryInterfaceController.swift.md)

# SpeedySloth/SpeedySloth WatchKit Extension/ConfigurationInterfaceController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Interface controller for the configuration screen.
 */

import WatchKit
import Foundation
import HealthKit

class ConfigurationInterfaceController: WKInterfaceController {
    // MARK: Properties

    var selectedActivityType: HKWorkoutActivityType

    var selectedLocationType: HKWorkoutSessionLocationType

    let activityTypes: [HKWorkoutActivityType] = [.walking, .running, .hiking]

    let locationTypes: [HKWorkoutSessionLocationType] = [.unknown, .indoor, .outdoor]

    // MARK: IB Outlets

    @IBOutlet var activityTypePicker: WKInterfacePicker!

    @IBOutlet var locationTypePicker: WKInterfacePicker!

    // MARK: Initialization

    override init() {
        selectedActivityType = activityTypes[0]
        selectedLocationType = locationTypes[0]

        super.init()
    }

    // MARK: Interface Controller Overrides

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)

        // Populate the activity type picker
        let activityTypePickerItems: [WKPickerItem] = activityTypes.map {type in
            let pickerItem = WKPickerItem()
            pickerItem.title = format(activityType: type)
            return pickerItem
        }
        activityTypePicker.setItems(activityTypePickerItems)

        // Populate the location type picker
        let locationTypePickerItems: [WKPickerItem] = locationTypes.map {type in
            let pickerItem = WKPickerItem()
            pickerItem.title = format(locationType: type)
            return pickerItem
        }
        locationTypePicker.setItems(locationTypePickerItems)

        setTitle("Speedy Sloth")
    }

    // MARK: IB Actions

    @IBAction func activityTypePickerSelectedItemChanged(value: Int) {
        selectedActivityType = activityTypes[value]
    }

    @IBAction func locationTypePickerSelectedItemChanged(value: Int) {
        selectedLocationType = locationTypes[value]
    }

    @IBAction func didTapStartButton() {
        // Create workout configuration
        let workoutConfiguration = HKWorkoutConfiguration()
        workoutConfiguration.activityType = selectedActivityType
        workoutConfiguration.locationType = selectedLocationType

        // Pass configuration to next interface controller
        WKInterfaceController.reloadRootControllers(withNames: ["WorkoutInterfaceController"], contexts: [workoutConfiguration])
    }

}
```

[Next](SpeedySloth-SpeedySloth%20WatchKit%20Extension-ParentConnector.swift.md)[Previous](SpeedySloth-SpeedySloth%20WatchKit%20Extension-SummaryInterfaceController.swift.md)

