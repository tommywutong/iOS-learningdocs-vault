---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_AppDelegate_swift.html
archived_at: '2026-07-18T03:28:06.091289Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](LICENSE.txt.md)[Previous](README.md.md)

# WatchKit Catalog/AppDelegate.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate which creates the window and root view controller.
 */

import UIKit
import WatchConnectivity

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, WCSessionDelegate {

    func applicationDidFinishLaunching(_ application: UIApplication) {
        if WCSession.isSupported() {
            WCSession.default().delegate = self
            WCSession.default().activate()
        }
    }

    func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([Any]?) -> Swift.Void) -> Bool {
        print("Handoff dictionary: \(userActivity.userInfo)")

        return true
    }

    func session(_ session: WCSession, didReceiveMessage message: [String : Any], replyHandler: @escaping ([String : Any]) -> Swift.Void) {
        /*
             Because this method is likely to be called when the app is in the
             background, begin a background task. Starting a background task ensures
             that your app is not suspended before it has a chance to send its reply.
         */

        let application = UIApplication.shared

        var identifier = UIBackgroundTaskInvalid;
        // The "endBlock" ensures that the background task is ended and the identifier is reset.
        let endBlock = {
            if identifier != UIBackgroundTaskInvalid {
                application.endBackgroundTask(identifier)
            }
            identifier = UIBackgroundTaskInvalid
        };

        identifier = application.beginBackgroundTask(expirationHandler: endBlock)

        // Re-assign the "reply" block to include a call to "endBlock" after "reply" is called.
        let replyHandler = {(replyInfo: [String : Any]) in
            replyHandler(replyInfo)

            endBlock();
        }

        // Receives text input result from the WatchKit app extension.
        print("Message: \(message)")

        // Sends a confirmation message to the WatchKit app extension that the text input result was received.
        replyHandler(["Confirmation" : "Text was received."])
    }

    func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: Error?) {

    }

    func sessionDidBecomeInactive(_ session: WCSession) {

    }

    func sessionDidDeactivate(_ session: WCSession) {

    }

}
```

[Next](LICENSE.txt.md)[Previous](README.md.md)

