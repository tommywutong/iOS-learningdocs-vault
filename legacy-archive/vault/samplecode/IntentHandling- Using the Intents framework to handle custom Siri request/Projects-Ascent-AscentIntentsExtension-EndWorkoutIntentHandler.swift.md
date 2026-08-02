---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentIntentsExtension_EndWorkoutIntentHandler_swift.html
archived_at: '2026-07-18T03:13:00.643151Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentIntentsExtension-Extension.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-PauseWorkoutIntentHandler.swift.md)

# Projects/Ascent/AscentIntentsExtension/EndWorkoutIntentHandler.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An object that implements the `IntentHandler` and `INEndWorkoutIntentHandling` protocols to handle requests to end the current workout.
*/

import Intents
import AscentFramework

class EndWorkoutIntentHandler: NSObject, IntentHandler, INEndWorkoutIntentHandling {

    // MARK: IntentHandler

    func canHandle(_ intent: INIntent) -> Bool {
        return intent is INEndWorkoutIntent
    }

    // MARK: Intent confirmation

    func confirm(endWorkout endWorkoutIntent: INEndWorkoutIntent, completion: @escaping (INEndWorkoutIntentResponse) -> Void) {
        let workoutHistory = WorkoutHistory.load()
        let response: INEndWorkoutIntentResponse

        if workoutHistory.activeWorkout != nil {
            response = INEndWorkoutIntentResponse(code: .continueInApp, userActivity: nil)
        }
        else {
            response = INEndWorkoutIntentResponse(code: .failureNoMatchingWorkout, userActivity: nil)
        }

        completion(response)
    }

    // MARK: Intent handling

    func handle(endWorkout endWorkoutIntent: INEndWorkoutIntent, completion: @escaping (INEndWorkoutIntentResponse) -> Void) {
        var workoutHistory = WorkoutHistory.load()
        let response: INEndWorkoutIntentResponse

        if workoutHistory.activeWorkout != nil {
            workoutHistory.endActiveWorkout()

            // Create a response with a `NSUserActivity` with the information needed to pause a workout.
            let userActivity = NSUserActivity(ascentActivityType: .endWorkout)
            response = INEndWorkoutIntentResponse(code: .continueInApp, userActivity: userActivity)
        }
        else {
            response = INEndWorkoutIntentResponse(code: .failureNoMatchingWorkout, userActivity: nil)
        }

        completion(response)
    }
}
```

[Next](Projects-Ascent-AscentIntentsExtension-Extension.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-PauseWorkoutIntentHandler.swift.md)

