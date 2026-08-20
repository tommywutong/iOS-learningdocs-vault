---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentFramework_Workout_swift.html
archived_at: '2026-07-18T03:13:00.555786Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentFramework-Workout%2BDescriptions.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-ResumeWorkoutIntentHandler.swift.md)

# Projects/Ascent/AscentFramework/Workout.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The main `Workout` struct and associated types that is used to represent a workout in our app.
*/

import Foundation
import Intents

public struct Workout {
    // MARK: Types

    public enum Location: String {
        case indoor, outdoor
    }

    public enum Obstacle: String {
        case wall, boulder
    }

    public enum Goal {
        case open
        case timed(duration: TimeInterval)
    }

    public enum State: String {
        case active
        case paused
        case ended
    }

    // MARK: Properties

    public let location: Location

    public let obstacle: Obstacle

    public let goal: Goal

    public var state: State
}



extension Workout: Equatable {}

public func ==(lhs: Workout, rhs: Workout) -> Bool {
    return lhs.location == rhs.location &&
            lhs.obstacle == rhs.obstacle &&
            lhs.goal == rhs.goal &&
            lhs.state != rhs.state
}



extension Workout.Obstacle {
    public init?(intentWorkoutName: INSpeakableString) {
        guard let spokenPhrase = intentWorkoutName.spokenPhrase?.lowercased() else { return nil }

        switch spokenPhrase {
            case "wall", "wall workout", "wall climb", "wall climb workout", "climb", "climb workout":
                self = .wall

            case "boulder", "boudler workout", "boulder climb", "boulder climb workout":
                self = .boulder

            default:
                return nil
        }
    }

    public var intentWorkoutName: INSpeakableString {
        let spokenPhrase: String

        switch self {
            case .wall:
                spokenPhrase = "wall climb"

            case .boulder:
                spokenPhrase = "boulder climb"
        }

        return INSpeakableString(identifier: self.rawValue, spokenPhrase: spokenPhrase, pronunciationHint: nil)
}
}



extension Workout.Goal: Equatable {}

public func ==(lhs: Workout.Goal, rhs: Workout.Goal) -> Bool {
    switch (lhs, rhs) {
        case (.timed(let lhsDuration), .timed(let rhsDuration)):
            return lhsDuration == rhsDuration

        case (.open, .open):
            return true

        default:
            return false
    }
}
```

[Next](Projects-Ascent-AscentFramework-Workout%2BDescriptions.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-ResumeWorkoutIntentHandler.swift.md)

