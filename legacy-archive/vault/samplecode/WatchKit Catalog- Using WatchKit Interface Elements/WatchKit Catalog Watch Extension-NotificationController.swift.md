---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_NotificationController_swift.html
archived_at: '2026-07-18T03:28:06.669791Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-LabelDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-TableRowController.swift.md)

# WatchKit Catalog Watch Extension/NotificationController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller handles displaying a custom or static notification.
 */

import WatchKit
import UserNotifications

class NotificationController : WKUserNotificationInterfaceController {

    override func willActivate() {
        // This method is called when the controller is about to be visible to the wearer.
        print("\(self) will activate")

        updateUserActivity("com.example.apple-samplecode.WatchKit-Catalog.notification", userInfo: ["Reason" : "Notification"], webpageURL: nil)
    }

    override func handleAction(withIdentifier identifier: String?, for notification: UNNotification) {
        print("notification received with identifier: \(identifier), notifiction: \(notification)")
    }
}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-LabelDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-TableRowController.swift.md)

