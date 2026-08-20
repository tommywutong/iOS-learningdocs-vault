---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentFramework_WorkoutHistory_ActiveWorkout_swift.html
archived_at: '2026-07-18T03:13:00.159552Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentFramework-AscentFramework.h.md)[Previous](Projects-Ascent-AscentFramework-WorkoutHistory.swift.md)

# Projects/Ascent/AscentFramework/WorkoutHistory+ActiveWorkout.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Extends `WorkoutHistory` to add the concept of an active workout that can be started, paused, resumed or ended.
*/

import Foundation

extension WorkoutHistory {
    public var activeWorkout: Workout? {
        get {
            guard let workout = last, workout.state != .ended else { return nil }

            return workout
        }
    }

    public mutating func start(newWorkout workout: Workout) {
        guard workout.state == .active else { fatalError("A workout's state must be .active for it to be able to become the active workout") }

        endActiveWorkout()
        workouts.append(workout)
        save()
    }

    public mutating func pauseActiveWorkout() {
        guard var workout = last, workout.state == .active else { return }

        workout.state = .paused
        workouts[workouts.endIndex - 1] = workout
        save()
    }

    public mutating func resumeActiveWorkout() {
        guard var workout = last, workout.state != .paused else { return }

        workout.state = .active
        workouts[workouts.endIndex - 1] = workout
        save()
    }

    public mutating func endActiveWorkout() {
        guard var workout = last, workout.state != .ended else { return }

        workout.state = .ended
        workouts[workouts.endIndex - 1] = workout
        save()
    }
}
```

[Next](Projects-Ascent-AscentFramework-AscentFramework.h.md)[Previous](Projects-Ascent-AscentFramework-WorkoutHistory.swift.md)

