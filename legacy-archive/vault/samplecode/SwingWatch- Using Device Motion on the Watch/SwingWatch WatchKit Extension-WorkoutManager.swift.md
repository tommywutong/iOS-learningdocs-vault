---
title: 'SwingWatch: Using Device Motion on the Watch'
apple_id: TP40017286
resource_type: Sample Code
platform: watchOS
topic: null
technology: CoreMotion
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/SwingWatch/Listings/SwingWatch_WatchKit_Extension_WorkoutManager_swift.html
archived_at: '2026-07-18T03:25:52.092782Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SwingWatch: Using Device Motion on the Watch](SwingWatch-%20Using%20Device%20Motion%20on%20the%20Watch.md)


[Next](SwingWatch%20WatchKit%20Extension-MotionManager.swift.md)[Previous](SwingWatch%20WatchKit%20Extension-ExtensionDelegate.swift.md)

# SwingWatch WatchKit Extension/WorkoutManager.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class manages the HealthKit interactions and provides a delegate 
         to indicate changes in data.
 */

import Foundation
import HealthKit

/**
 `WorkoutManagerDelegate` exists to inform delegates of swing data changes.
 These updates can be used to populate the user interface.
 */
protocol WorkoutManagerDelegate: class {
    func didUpdateForehandSwingCount(_ manager: WorkoutManager, forehandCount: Int)
    func didUpdateBackhandSwingCount(_ manager: WorkoutManager, backhandCount: Int)
}

class WorkoutManager: MotionManagerDelegate {
    // MARK: Properties
    let motionManager = MotionManager()
    let healthStore = HKHealthStore()

    weak var delegate: WorkoutManagerDelegate?
    var session: HKWorkoutSession?

    // MARK: Initialization

    init() {
        motionManager.delegate = self
    }

    // MARK: WorkoutManager

    func startWorkout() {
        // If we have already started the workout, then do nothing.
        if (session != nil) {
            return
        }

        // Configure the workout session.
        let workoutConfiguration = HKWorkoutConfiguration()
        workoutConfiguration.activityType = .tennis
        workoutConfiguration.locationType = .outdoor

        do {
            session = try HKWorkoutSession(configuration: workoutConfiguration)
        } catch {
            fatalError("Unable to create the workout session!")
        }

        // Start the workout session and device motion updates.
        healthStore.start(session!)
        motionManager.startUpdates()
    }

    func stopWorkout() {
        // If we have already stopped the workout, then do nothing.
        if (session == nil) {
            return
        }

        // Stop the device motion updates and workout session.
        motionManager.stopUpdates()
        healthStore.end(session!)

        // Clear the workout session.
        session = nil
    }

    // MARK: MotionManagerDelegate

    func didUpdateForehandSwingCount(_ manager: MotionManager, forehandCount: Int) {
        delegate?.didUpdateForehandSwingCount(self, forehandCount: forehandCount)
    }

    func didUpdateBackhandSwingCount(_ manager: MotionManager, backhandCount: Int) {
        delegate?.didUpdateBackhandSwingCount(self, backhandCount: backhandCount)
    }
}
```

[Next](SwingWatch%20WatchKit%20Extension-MotionManager.swift.md)[Previous](SwingWatch%20WatchKit%20Extension-ExtensionDelegate.swift.md)

