---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentFramework_WorkoutHistory_swift.html
archived_at: '2026-07-18T03:13:00.309503Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentFramework-WorkoutHistory%2BActiveWorkout.swift.md)[Previous](Projects-Ascent-AscentFramework-NSUserActivity%2BAscent.swift.md)

# Projects/Ascent/AscentFramework/WorkoutHistory.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A struct that wraps saving and restoring `Workout`s from shared user defaults.
*/

import Foundation

public struct WorkoutHistory {

    var workouts: [Workout]

    public var count: Int {
        return workouts.count
    }

    public subscript(index: Int) -> Workout {
        get {
            return workouts[index]
        }

        set(newValue) {
            workouts[index] = newValue
        }
    }

    public var last: Workout? {
        return workouts.last
    }

    // MARK: Initialization

    private init(workouts: [Workout]) {
        self.workouts = workouts
    }

    // MARK: Load and save

    public static func load() -> WorkoutHistory {
        var workouts = [Workout]()
        let defaults = WorkoutHistory.makeUserDefaults()

        if let savedWorkouts = defaults.object(forKey: "workouts") as? [[String: AnyObject]] {
            for dictionary in savedWorkouts {
                if let workout = Workout(dictionaryRepresentation: dictionary) {
                    workouts.append(workout)
                }
            }
        }

        return WorkoutHistory(workouts: workouts)
    }

    func save() {
        let workoutDictionaries: [[String: AnyObject]] = workouts.map { $0.dictionaryRepresentation }
        let defaults = WorkoutHistory.makeUserDefaults()

        defaults.set(workoutDictionaries as AnyObject, forKey: "workouts")
    }

    // MARK: Convenience

    private static func makeUserDefaults() -> UserDefaults {
        guard let defaults = UserDefaults(suiteName: "group.com.example.apple-samplecode.Ascent") else { fatalError("Unable to create user defaults object") }
        return defaults
    }
}


extension WorkoutHistory: Sequence {
    public typealias Iterator = AnyIterator<Workout>

    public func makeIterator() -> Iterator {
        var index = 0

        return Iterator {
            guard index < self.workouts.count else { return nil }

            let workout = self.workouts[index]
            index += 1

            return workout
        }
    }
}



extension WorkoutHistory: Equatable {}

public func ==(lhs: WorkoutHistory, rhs: WorkoutHistory) -> Bool {
    return lhs.workouts == rhs.workouts
}
```

[Next](Projects-Ascent-AscentFramework-WorkoutHistory%2BActiveWorkout.swift.md)[Previous](Projects-Ascent-AscentFramework-NSUserActivity%2BAscent.swift.md)

