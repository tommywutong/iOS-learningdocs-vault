---
title: 'SpeedySloth: Using HealthKit to build a workout app for Apple Watch'
apple_id: TP40017338
resource_type: Sample Code
platform: watchOS
topic: null
technology: HealthKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SpeedySloth/Listings/SpeedySloth_SpeedySloth_ConfigurationViewController_swift.html
archived_at: '2026-07-18T03:25:18.161418Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SpeedySloth: Using HealthKit to build a workout app for Apple Watch](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)


[Next](README.md.md)[Previous](SpeedySloth-SpeedySloth-AppDelegate.swift.md)

# SpeedySloth/SpeedySloth/ConfigurationViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller for the configuration screen.
 */

import UIKit
import HealthKit

class ConfigurationViewController: UIViewController, UIPickerViewDataSource, UIPickerViewDelegate {
    // MARK: Properties

    var selectedActivityType: HKWorkoutActivityType

    var selectedLocationType: HKWorkoutSessionLocationType

    let activityTypes: [HKWorkoutActivityType] = [.walking, .running, .hiking]
    let locationTypes: [HKWorkoutSessionLocationType] = [.unknown, .indoor, .outdoor]

    // MARK: IBOutlets


    @IBOutlet var activityTypePicker: UIPickerView!
    @IBOutlet var locationTypePicker: UIPickerView!

    // MARK: Initialization

    required init?(coder: NSCoder) {
        selectedActivityType = activityTypes[0]
        selectedLocationType = locationTypes[0]

        super.init(coder: coder)
    }

    // MARK: UIPickerViewDataSource

    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }

    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        if pickerView == activityTypePicker {
            return activityTypes.count
        } else if pickerView == locationTypePicker {
            return locationTypes.count
        }

        return 0
    }

    // MARK: UIPickerViewDelegate

    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        if pickerView == activityTypePicker {
            return format(activityType: activityTypes[row])
        } else if pickerView == locationTypePicker {
            return format(locationType: locationTypes[row])
        }

        return nil
    }

    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        if pickerView == activityTypePicker {
            selectedActivityType = activityTypes[row]
        } else if pickerView == locationTypePicker {
            selectedLocationType = locationTypes[row]
        }
    }

    @IBAction func didTapStartButton() {
        let workoutConfiguration = HKWorkoutConfiguration()
        workoutConfiguration.activityType = selectedActivityType
        workoutConfiguration.locationType = selectedLocationType

        if let workoutViewController = storyboard?.instantiateViewController(withIdentifier: "WorkoutViewController") as? WorkoutViewController {
            workoutViewController.configuration = workoutConfiguration
            present(workoutViewController, animated: true, completion:nil)
        }
    }
}
```

[Next](README.md.md)[Previous](SpeedySloth-SpeedySloth-AppDelegate.swift.md)

