---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentIntentsExtension_ResumeWorkoutIntentHandler_swift.html
archived_at: '2026-07-18T03:13:00.832734Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentFramework-Workout.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-IntentHandler.swift.md)

# Projects/Ascent/AscentIntentsExtension/ResumeWorkoutIntentHandler.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An object that implements the `IntentHandler` and `INResumeWorkoutIntentHandling` protocols to handle requests to resume the current workout.
*/

import Intents
import AscentFramework

class ResumeWorkoutIntentHandler: NSObject, IntentHandler, INResumeWorkoutIntentHandling {

    // MARK: IntentHandler

    func canHandle(_ intent: INIntent) -> Bool {
        return intent is INResumeWorkoutIntent
    }

    // MARK: Intent confirmation

    func confirm(resumeWorkout resumeWorkoutIntent: INResumeWorkoutIntent, completion: @escaping (INResumeWorkoutIntentResponse) -> Void) {
        let workoutHistory = WorkoutHistory.load()
        let response: INResumeWorkoutIntentResponse

        if let workout = workoutHistory.activeWorkout, workout.state == .paused {
            response = INResumeWorkoutIntentResponse(code: .continueInApp, userActivity: nil)
        }
        else {
            response = INResumeWorkoutIntentResponse(code: .failureNoMatchingWorkout, userActivity: nil)
        }

        completion(response)
    }

    // MARK: Intent handling

    func handle(resumeWorkout resumeWorkoutIntent: INResumeWorkoutIntent, completion: @escaping (INResumeWorkoutIntentResponse) -> Void) {
        var workoutHistory = WorkoutHistory.load()
        let response: INResumeWorkoutIntentResponse

        if let workout = workoutHistory.activeWorkout, workout.state == .paused {
            workoutHistory.resumeActiveWorkout()

            // Create a response with a `NSUserActivity` with the information needed to pause a workout.
            let userActivity = NSUserActivity(ascentActivityType: .resumeWorkout)
            response = INResumeWorkoutIntentResponse(code: .continueInApp, userActivity: userActivity)
        }
        else {
            response = INResumeWorkoutIntentResponse(code: .failureNoMatchingWorkout, userActivity: nil)
        }

        completion(response)
    }
}
```

[Next](Projects-Ascent-AscentFramework-Workout.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-IntentHandler.swift.md)

