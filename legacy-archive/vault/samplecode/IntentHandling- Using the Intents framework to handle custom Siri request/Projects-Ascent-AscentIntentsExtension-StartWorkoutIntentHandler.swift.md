---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentIntentsExtension_StartWorkoutIntentHandler_swift.html
archived_at: '2026-07-18T03:13:00.871465Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentIntentsExtension-PauseWorkoutIntentHandler.swift.md)[Previous](Projects-Ascent-Ascent-WorkoutsController.swift.md)

# Projects/Ascent/AscentIntentsExtension/StartWorkoutIntentHandler.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An object that implements the `IntentHandler` and `INStartWorkoutIntentHandling` protocols to handle requests to start a new workout.
*/

import Intents
import AscentFramework

class StartWorkoutIntentHandler: NSObject, IntentHandler, INStartWorkoutIntentHandling {

    // MARK: IntentHandler

    func canHandle(_ intent: INIntent) -> Bool {
        return intent is INStartWorkoutIntent
    }

    // MARK: Parameter resolution

    func resolveWorkoutName(forStartWorkout intent: INStartWorkoutIntent, with completion: @escaping (INSpeakableStringResolutionResult) -> Void) {
        let result: INSpeakableStringResolutionResult
        let workoutHistory = WorkoutHistory.load()

        if let name = intent.workoutName {
            // Try to determine the obstacle (wall or boulder) from the supplied workout name.
            if Workout.Obstacle(intentWorkoutName: name) != nil {
                result = INSpeakableStringResolutionResult.success(with: name)
            }
            else {
                result = INSpeakableStringResolutionResult.needsValue()
            }
        }
        else if let lastWorkout = workoutHistory.last {
            // A name hasn't been supplied so suggest the last obstacle.
            result = INSpeakableStringResolutionResult.confirmationRequired(with: lastWorkout.obstacle.intentWorkoutName)
        }
        else {
            result = INSpeakableStringResolutionResult.needsValue()
        }

        completion(result)
    }

    func resolveWorkoutGoalUnitType(forStartWorkout intent: INStartWorkoutIntent, with completion: @escaping (INWorkoutGoalUnitTypeResolutionResult) -> Void) {
        let result: INWorkoutGoalUnitTypeResolutionResult

        // Allow time based or open goals.
        switch intent.workoutGoalUnitType {
            case .hour, .minute, .second, .unknown:
                result = INWorkoutGoalUnitTypeResolutionResult.success(with: intent.workoutGoalUnitType)

            default:
                result = INWorkoutGoalUnitTypeResolutionResult.unsupported()
        }

        completion(result)
    }

    // MARK: Intent confirmation

    func confirm(startWorkout intent: INStartWorkoutIntent, completion: @escaping (INStartWorkoutIntentResponse) -> Void) {
        let response: INStartWorkoutIntentResponse

        // Validate the intent by attempting create a `Workout` with it.
        if Workout(startWorkoutIntent: intent) != nil {
            response = INStartWorkoutIntentResponse(code: .continueInApp, userActivity: nil)
        }
        else {
            response = INStartWorkoutIntentResponse(code: .failure, userActivity: nil)
        }

        completion(response)
    }

    // MARK: Intent handling

    func handle(startWorkout intent: INStartWorkoutIntent, completion: @escaping (INStartWorkoutIntentResponse) -> Void) {
        let response: INStartWorkoutIntentResponse

        if let workout = Workout(startWorkoutIntent: intent) {
            // Create a response with a `NSUserActivity` that contains the information needed to start a workout.
            let userActivity = NSUserActivity(ascentActivityType: .start(workout))
            response = INStartWorkoutIntentResponse(code: .continueInApp, userActivity: userActivity)
        }
        else {
            response = INStartWorkoutIntentResponse(code: .failure, userActivity: nil)
        }

        completion(response)
    }
}
```

[Next](Projects-Ascent-AscentIntentsExtension-PauseWorkoutIntentHandler.swift.md)[Previous](Projects-Ascent-Ascent-WorkoutsController.swift.md)

