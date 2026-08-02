---
title: 'Animalify: Using Safari App Extensions to modify pages and communicate with
  native code'
apple_id: TP40017383
resource_type: Sample Code
platform: macOS
topic: null
technology: SafariServices
published: '2016-11-03'
source_url: https://developer.apple.com/library/archive/samplecode/Animalify/Listings/Animalify_Extension_SafariExtensionHandler_swift.html
archived_at: '2026-07-18T03:01:01.281236Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Animalify: Using Safari App Extensions to modify pages and communicate with native code](Animalify-%20Using%20Safari%20App%20Extensions%20to%20modify%20pages%20and%20communicate%20with%20nati.md)


[Next](Animalify-AppDelegate.swift.md)[Previous](Animalify%20Extension-script.js.md)

# Animalify Extension/SafariExtensionHandler.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The principal object for the Animalify Extension. This object receives messages from the content script injected by this extension into web pages, and responds with the words to replace and what to replace them with.
*/

import SafariServices

class SafariExtensionHandler: SFSafariExtensionHandler {

    override func messageReceived(withName messageName: String, from page: SFSafariPage, userInfo: [String : Any]? = nil) {
        if messageName == "GetWordsAndReplacements" {
            page.dispatchMessageToScript(withName: "WordsAndReplacements", userInfo: ["Bear": "🐻", "Fish": "🐠"]);
        }
    }

}
```

[Next](Animalify-AppDelegate.swift.md)[Previous](Animalify%20Extension-script.js.md)

