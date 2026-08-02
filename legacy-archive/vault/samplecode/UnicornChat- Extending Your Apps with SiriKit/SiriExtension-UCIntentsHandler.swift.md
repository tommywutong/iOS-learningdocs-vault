---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/SiriExtension_UCIntentsHandler_swift.html
archived_at: '2026-07-18T03:27:32.901107Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](SiriUIExtension-IntentViewController.swift.md)[Previous](SiriExtension-UCSendMessageIntentHandler.swift.md)

# SiriExtension/UCIntentsHandler.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The main entry point to the Intents extension.
*/

import Intents

class UCIntentsHandler: INExtension {

    override func handler(for intent: INIntent) -> Any? {
        if intent is INSendMessageIntent {
            return UCSendMessageIntentHandler()
        }

        return nil
    }
}
```

[Next](SiriUIExtension-IntentViewController.swift.md)[Previous](SiriExtension-UCSendMessageIntentHandler.swift.md)

