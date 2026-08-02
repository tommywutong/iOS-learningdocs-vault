---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Ascent_AscentIntentsExtension_IntentHandler_swift.html
archived_at: '2026-07-18T03:13:00.746144Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-AscentIntentsExtension-ResumeWorkoutIntentHandler.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-CancelWorkoutIntentHandler.swift.md)

# Projects/Ascent/AscentIntentsExtension/IntentHandler.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Types that conform to the `IntentHandler` protocol can be queried as to whether they can handle a specific type of `INIntent`.
*/

import Intents

protocol IntentHandler: class {

    func canHandle(_ intent: INIntent) -> Bool

}
```

[Next](Projects-Ascent-AscentIntentsExtension-ResumeWorkoutIntentHandler.swift.md)[Previous](Projects-Ascent-AscentIntentsExtension-CancelWorkoutIntentHandler.swift.md)

