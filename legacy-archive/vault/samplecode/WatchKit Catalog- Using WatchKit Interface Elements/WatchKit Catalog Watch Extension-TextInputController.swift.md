---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_TextInputController_swift.html
archived_at: '2026-07-18T03:28:06.942341Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-InterfaceController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-DeviceDetailController.swift.md)

# WatchKit Catalog Watch Extension/TextInputController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller demonstrates using the Text Input Controller.
 */

import WatchKit
import WatchConnectivity

class TextInputController: WKInterfaceController {

    @IBAction func replyWithTextInputController() {

        let resultHandler = {(results: [Any]?) in
            print("Text Input Results: \(results)")
            if results?.first != nil {
                // Sends a non-nil result to the parent iOS application.
                WCSession.default().sendMessage(["TextInput" : (results?.first)!], replyHandler: { (replyMessage) in
                        print("Reply Info: \(replyMessage)")
                    }, errorHandler: { (error) in
                        print("Error: \(error.localizedDescription)")
                })
            }
        }

        // Using the WKTextInputMode enum, you can specify which aspects of the Text Input Controller are shown when presented.
        presentTextInputController(withSuggestions: ["Yes", "No", "Maybe"], allowedInputMode: .allowEmoji, completion: resultHandler)
    }

}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-InterfaceController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-DeviceDetailController.swift.md)

