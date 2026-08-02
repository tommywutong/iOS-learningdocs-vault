---
title: 'AppChat: Using Peek and Pop APIs'
apple_id: TP40017298
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppChat/Listings/AppChat_AppDelegate_swift.html
archived_at: '2026-07-18T03:01:05.443181Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppChat: Using Peek and Pop APIs](AppChat-%20Using%20Peek%20and%20Pop%20APIs.md)


[Next](AppChat-ChatReplyDismissAnimator.swift.md)[Previous](AppChat-ChatReplyInteractionController.swift.md)

# AppChat/AppDelegate.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The app delegate.
 */

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?
    var rootViewController: UIViewController? {
        return window?.rootViewController
    }

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        var performAdditionalHandling = true

        window?.makeKeyAndVisible()
        if let shortcutItem = launchOptions?[.shortcutItem] as? UIApplicationShortcutItem, let rootViewController = rootViewController {
            let didHandleShortcutItem = ShortcutItemHandler.handle(shortcutItem, with: rootViewController)
            performAdditionalHandling = !didHandleShortcutItem
        }

        ShortcutItemHandler.updateDynamicShortcutItems(for: application)

        return performAdditionalHandling
    }

    func application(_ application: UIApplication, performActionFor shortcutItem: UIApplicationShortcutItem, completionHandler: @escaping (Bool) -> Void) {
        var didHandleShortcutItem = false

        if let rootViewController = rootViewController {
            didHandleShortcutItem = ShortcutItemHandler.handle(shortcutItem, with: rootViewController)
        }

        completionHandler(didHandleShortcutItem)
    }
}

extension UIApplication {
    func present(alert: UIAlertController, animated: Bool = true) {
        UIApplication.shared.keyWindow?.rootViewController?.present(alert, animated: animated)
    }
}
```

[Next](AppChat-ChatReplyDismissAnimator.swift.md)[Previous](AppChat-ChatReplyInteractionController.swift.md)

