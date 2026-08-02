---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentIntentsExtension_CancelWorkoutIntentHandler_swift.html
archived_at: '2026-07-18T03:13:00.603971Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentIntentsExtension-IntentHandler.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-Extension.swift.md)

# Projects/Ascent/AscentIntentsExtension/CancelWorkoutIntentHandler.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An object that implements the `IntentHandler` and `INCancelWorkoutIntentHandling` protocols to handle requests to cancel the current workout.
*/

import Intents
import AscentFramework

class CancelWorkoutIntentHandler: NSObject, IntentHandler, INCancelWorkoutIntentHandling {

    // MARK: IntentHandler

    func canHandle(_ intent: INIntent) -> Bool {
        return intent is INCancelWorkoutIntent
    }

    // MARK: Intent confirmation

    func confirm(cancelWorkout intent: INCancelWorkoutIntent, completion: @escaping (INCancelWorkoutIntentResponse) -> Void) {
        let workoutHistory = WorkoutHistory.load()
        let response: INCancelWorkoutIntentResponse

        if let workout = workoutHistory.activeWorkout, workout.state != .ended {
            response = INCancelWorkoutIntentResponse(code: .continueInApp, userActivity: nil)
        }
        else {
            response = INCancelWorkoutIntentResponse(code: .failureNoMatchingWorkout, userActivity: nil)
        }

        completion(response)
    }

    // MARK: Intent handling

    func handle(cancelWorkout intent: INCancelWorkoutIntent, completion: @escaping (INCancelWorkoutIntentResponse) -> Void) {
        var workoutHistory = WorkoutHistory.load()
        let response: INCancelWorkoutIntentResponse

        if let workout = workoutHistory.activeWorkout, workout.state == .ended {
            workoutHistory.endActiveWorkout()

            // Create a response with a `NSUserActivity` with the information needed to cancel a workout.
            let userActivity = NSUserActivity(ascentActivityType: .cancelWorkout)
            response = INCancelWorkoutIntentResponse(code: .continueInApp, userActivity: userActivity)
        }
        else {
            response = INCancelWorkoutIntentResponse(code: .failureNoMatchingWorkout, userActivity: nil)
        }

        completion(response)
    }
}
```

[Next](Projects-Ascent-AscentIntentsExtension-IntentHandler.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-Extension.swift.md)

