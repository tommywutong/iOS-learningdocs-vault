---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentFramework_NSUserActivity_Ascent_swift.html
archived_at: '2026-07-18T03:13:00.095728Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentFramework-WorkoutHistory.swift.md)[Previous](Projects-Ascent-AscentFramework-Workout%2BDescriptions.swift.md)

# Projects/Ascent/AscentFramework/NSUserActivity+Ascent.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Extends NSUserActivity to more easily encapsulate types of activity a user would perform with a workout.
*/

import Foundation

extension NSUserActivity {
    // MARK: Types

    public enum AscentActivityType {
        case start(Workout)
        case pauseWorkout
        case resumeWorkout
        case cancelWorkout
        case endWorkout
    }

    // MARK: Computed properties

    public var ascentActivityType: AscentActivityType? {
        switch activityType {
            case "com.example.apple-samplecode.Ascent.startWorkout":
                guard let dictionary = userInfo?["workout"] as? [String: AnyObject] else { return nil }
                guard let workout = Workout(dictionaryRepresentation: dictionary) else { return nil }
                return .start(workout)

            case "com.example.apple-samplecode.Ascent.pauseWorkout":
                return .pauseWorkout

            case "com.example.apple-samplecode.Ascent.resumeWorkout":
                return .resumeWorkout

            case "com.example.apple-samplecode.Ascent.cancelWorkout":
                return .cancelWorkout

            case "com.example.apple-samplecode.Ascent.endWorkout":
                return .endWorkout

            default:
                return nil
        }
    }

    // MARK: Initialization

    public convenience init(ascentActivityType: AscentActivityType) {
        switch ascentActivityType {
            case .start(let workout):
                self.init(activityType: "com.example.apple-samplecode.Ascent.startWorkout")
                userInfo = ["workout": workout.dictionaryRepresentation as AnyObject]

            case .pauseWorkout:
                self.init(activityType: "com.example.apple-samplecode.Ascent.pauseWorkout")

            case .resumeWorkout:
                self.init(activityType: "com.example.apple-samplecode.Ascent.resumeWorkout")

            case .cancelWorkout:
                self.init(activityType: "com.example.apple-samplecode.Ascent.cancelWorkout")

            case .endWorkout:
                self.init(activityType: "com.example.apple-samplecode.Ascent.endWorkout")
        }
    }
}
```

[Next](Projects-Ascent-AscentFramework-WorkoutHistory.swift.md)[Previous](Projects-Ascent-AscentFramework-Workout%2BDescriptions.swift.md)

