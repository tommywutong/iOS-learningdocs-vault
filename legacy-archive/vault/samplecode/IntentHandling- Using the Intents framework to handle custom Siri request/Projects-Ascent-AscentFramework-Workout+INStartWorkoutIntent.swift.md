---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentFramework_Workout_INStartWorkoutIntent_swift.html
archived_at: '2026-07-18T03:13:00.510220Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentFramework-Workout%2BDictionaryRepresentation.swift.md)[Previous](Projects-Ascent-AscentFramework-AscentFramework.h.md)

# Projects/Ascent/AscentFramework/Workout+INStartWorkoutIntent.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Extends `Workout` to add a failable initializer that accepts an `INStartWorkoutIntent`.
*/

import Intents

extension Workout {
    public init?(startWorkoutIntent intent: INStartWorkoutIntent) {
        switch intent.workoutLocationType {
            case .outdoor, .unknown:
                self.location = .outdoor

            case .indoor:
                self.location = .indoor
        }

        guard let workoutName = intent.workoutName, let obstacle = Obstacle(intentWorkoutName: workoutName) else { return nil }
        self.obstacle = obstacle

        if let isOpenEnded = intent.isOpenEnded, isOpenEnded || intent.goalValue == nil {
            self.goal = .open
        }
        else if let goalValue = intent.goalValue, let duration = TimeInterval(workoutGoalValue: goalValue, workoutGoalUnitType: intent.workoutGoalUnitType) {
            self.goal = .timed(duration: duration)
        }
        else {
            return nil
        }

        self.state = .active
    }
}



extension TimeInterval {
    init?(workoutGoalValue: Double, workoutGoalUnitType: INWorkoutGoalUnitType) {
        switch workoutGoalUnitType {
            case .second:
                self = workoutGoalValue

            case .minute:
                self = workoutGoalValue * 60.0

            case .hour:
                self = workoutGoalValue * 60.0 * 60.0

            default:
                return nil
        }
    }
}
```

[Next](Projects-Ascent-AscentFramework-Workout%2BDictionaryRepresentation.swift.md)[Previous](Projects-Ascent-AscentFramework-AscentFramework.h.md)

