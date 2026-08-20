---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_NavigationBar_swift.html
archived_at: '2026-07-18T03:03:28.871562Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-FetchUserRecordIDSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-MainMenuTableViewController.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/NavigationBar.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the navigation bar that contains NotificationBar as a subview.
*/

import UIKit
import CloudKit

class NavigationBar: UINavigationBar {

    var notificationBar: NotificationBar!

    required init?(coder aDecoder: NSCoder) {
        notificationBar = NotificationBar(coder: aDecoder)
        super.init(coder: aDecoder)
        barStyle = .Black
        barTintColor = UIColor(red: 0.25, green: 0.29, blue: 0.36, alpha: 1.0)
        tintColor = UIColor.whiteColor()

        addSubview(notificationBar)

        let leftConstraint = NSLayoutConstraint(item: self, attribute: .Leading, relatedBy: .Equal, toItem: notificationBar, attribute: .Leading, multiplier: 1.0, constant: 0.0)
        addConstraint(leftConstraint)

        let rightConstraint = NSLayoutConstraint(item: self, attribute: .Trailing, relatedBy: .Equal, toItem: notificationBar, attribute: .Trailing, multiplier: 1.0, constant: 0.0)
        addConstraint(rightConstraint)

        let topConstraint = NSLayoutConstraint(item: self, attribute: .Top, relatedBy: .Equal, toItem: notificationBar, attribute: .Top, multiplier: 1.0, constant: 0.0)
        addConstraint(topConstraint)

    }

    func showNotificationAlert(notification: CKNotification) {
        if notificationBar.notification == nil {
            notificationBar.notification = notification
            bringSubviewToFront(notificationBar)
            notificationBar.show()
        }
    }
}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-FetchUserRecordIDSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-MainMenuTableViewController.swift.md)

