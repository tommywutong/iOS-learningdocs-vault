---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentIntentsExtension_Extension_swift.html
archived_at: '2026-07-18T03:13:00.702422Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentIntentsExtension-CancelWorkoutIntentHandler.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-EndWorkoutIntentHandler.swift.md)

# Projects/Ascent/AscentIntentsExtension/Extension.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The main extension entry point.
*/

import Intents

class Extension: INExtension {

    let intentHandlers: [IntentHandler] = [
        StartWorkoutIntentHandler(),
        PauseWorkoutIntentHandler(),
        ResumeWorkoutIntentHandler(),
        CancelWorkoutIntentHandler(),
        EndWorkoutIntentHandler()
    ]

    // MARK: INIntentHandlerProviding

    override func handler(for intent: INIntent) -> Any {
        for handler in intentHandlers where handler.canHandle(intent) {
            return handler
        }

        fatalError("Unexpected intent type")
    }
}
```

[Next](Projects-Ascent-AscentIntentsExtension-CancelWorkoutIntentHandler.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-EndWorkoutIntentHandler.swift.md)

