---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentIntentsExtension_PauseWorkoutIntentHandler_swift.html
archived_at: '2026-07-18T03:13:00.789467Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentIntentsExtension-EndWorkoutIntentHandler.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-StartWorkoutIntentHandler.swift.md)

# Projects/Ascent/AscentIntentsExtension/PauseWorkoutIntentHandler.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An object that implements the `IntentHandler` and `INOauseWorkoutIntentHandling` protocols to handle requests to pause the current workout.
*/

import Intents
import AscentFramework

class PauseWorkoutIntentHandler: NSObject, IntentHandler, INPauseWorkoutIntentHandling {

    // MARK: IntentHandler

    func canHandle(_ intent: INIntent) -> Bool {
        return intent is INPauseWorkoutIntent
    }

    // MARK: Intent confirmation

    func confirm(pauseWorkout pauseWorkoutIntent: INPauseWorkoutIntent, completion: @escaping (INPauseWorkoutIntentResponse) -> Void) {
        let workoutHistory = WorkoutHistory.load()
        let response: INPauseWorkoutIntentResponse

        if let workout = workoutHistory.activeWorkout, workout.state == .active {
            response = INPauseWorkoutIntentResponse(code: .continueInApp, userActivity: nil)
        }
        else {
            response = INPauseWorkoutIntentResponse(code: .failureNoMatchingWorkout, userActivity: nil)
        }

        completion(response)
    }

    // MARK: Intent handling

    func handle(pauseWorkout pauseWorkoutIntent: INPauseWorkoutIntent, completion: @escaping (INPauseWorkoutIntentResponse) -> Void) {
        var workoutHistory = WorkoutHistory.load()
        let response: INPauseWorkoutIntentResponse

        if let workout = workoutHistory.activeWorkout, workout.state == .active {
            workoutHistory.pauseActiveWorkout()

            // Create a response with a `NSUserActivity` with the information needed to pause a workout.
            let userActivity = NSUserActivity(ascentActivityType: .pauseWorkout)
            response = INPauseWorkoutIntentResponse(code: .continueInApp, userActivity: userActivity)
        }
        else {
            response = INPauseWorkoutIntentResponse(code: .failureNoMatchingWorkout, userActivity: nil)
        }

        completion(response)
    }
}
```

[Next](Projects-Ascent-AscentIntentsExtension-EndWorkoutIntentHandler.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-StartWorkoutIntentHandler.swift.md)

