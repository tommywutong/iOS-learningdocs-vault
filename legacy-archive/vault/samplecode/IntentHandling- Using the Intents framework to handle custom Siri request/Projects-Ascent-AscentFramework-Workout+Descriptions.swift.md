---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentFramework_Workout_Descriptions_swift.html
archived_at: '2026-07-18T03:13:00.407245Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentFramework-NSUserActivity%2BAscent.swift.md)[Previous](Projects-Ascent-AscentFramework-Workout.swift.md)

# Projects/Ascent/AscentFramework/Workout+Descriptions.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Extends `Workout` to provide descriptions of its properties that can be displayed to the user.
*/

import Foundation

extension Workout {
    private static let goalDurationFormatter: DateComponentsFormatter = {
        let formatter = DateComponentsFormatter()
        formatter.unitsStyle = .short

        return formatter
    }()

    public var climbDescription: String {
        switch (location, obstacle) {
            case (.indoor, .wall):
                return "Indoor wall climb"

            case (.indoor, .boulder):
                return "Indoor boulder climb"

            case (.outdoor, .wall):
                return "Outdoor wall climb"

            case (.outdoor, .boulder):
                return "Outdoor boulder climb"
        }
    }

    public var goalDescription: String {
        switch goal {
            case .open:
                return "No goal"

            case .timed(let duration):
                return Workout.goalDurationFormatter.string(from: duration)!
        }
    }

    public var stateDescription: String {
        switch state {
            case .active:
                return "Active"

            case .ended:
                return "Ended"

            case .paused:
                return "Paused"
        }
    }
}
```

[Next](Projects-Ascent-AscentFramework-NSUserActivity%2BAscent.swift.md)[Previous](Projects-Ascent-AscentFramework-Workout.swift.md)

