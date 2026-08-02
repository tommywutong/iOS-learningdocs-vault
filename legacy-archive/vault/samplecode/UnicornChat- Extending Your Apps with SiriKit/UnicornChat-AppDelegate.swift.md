---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/UnicornChat_AppDelegate_swift.html
archived_at: '2026-07-18T03:27:33.092043Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](Document%20Revision%20History.md)[Previous](UnicornChat-ViewController.swift.md)

# UnicornChat/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The application delegate
*/

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([Any]?) -> Void) -> Bool {
        // implement to handle user activity created by Siri or by our SiriExtension

        return true
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](UnicornChat-ViewController.swift.md)

