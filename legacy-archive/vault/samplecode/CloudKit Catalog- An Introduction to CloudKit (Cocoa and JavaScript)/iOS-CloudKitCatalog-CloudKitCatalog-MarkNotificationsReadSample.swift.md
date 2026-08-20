---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_MarkNotificationsReadSample_swift.html
archived_at: '2026-07-18T03:03:28.826253Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-LocationFieldTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-ImageTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/MarkNotificationsReadSample.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This code sample contains a class to manage cached notification objects as well as a class for the
                code sample that marks newly added notifications as read.
*/

import CloudKit
import UIKit

class NotificationsCache {
    private var results: Results = Results(alwaysShowAsList: true)

    func addNotification(notification: CKNotification) {
        results.items.append(notification)
        results.added.insert(results.items.count - 1)
    }

    var addedIndices: Set<Int> {
        return results.added
    }

    var newNotificationIDs: [CKNotificationID] {
        var ids = [CKNotificationID]()
        for index in results.added {
            if let notification = results.items[index] as? CKNotification, id = notification.notificationID {
                ids.append(id)
            }
        }
        return ids
    }

    func markAsRead() {
        let notificationIDs = notificationIDsToBeMarkedAsRead
        for notificationID in notificationIDs {
            if let index = results.items.indexOf({ result in
                if let notification = result as? CKNotification {
                    return notification.notificationID == notificationID
                } else {
                    return false
                }
            }) {
                results.added.remove(index)
            }
        }
        UIApplication.sharedApplication().applicationIconBadgeNumber = results.added.count
    }

    var notificationIDsToBeMarkedAsRead: [CKNotificationID] = []

}

class MarkNotificationsReadSample: CodeSample {

    var cache = NotificationsCache()

    init() {
        super.init(
            title: "CKMarkNotificationsReadOperation",
            className: "CKMarkNotificationsReadOperation",
            methodName: ".init(notificationIDsToMarkRead:)",
            descriptionKey: "Notifications.MarkAsRead"
        )
    }

    override func run(completionHandler: (Results, NSError!) -> Void) {

        let ids = cache.newNotificationIDs
        var nsError: NSError?

        if ids.count > 0 {
            let operation = CKMarkNotificationsReadOperation(notificationIDsToMarkRead: ids)

            operation.markNotificationsReadCompletionBlock = {
                (notificationIDsMarkedRead, operationError) in

                if let notificationIDs = notificationIDsMarkedRead {
                    self.cache.notificationIDsToBeMarkedAsRead = notificationIDs
                    completionHandler(self.cache.results, nsError)
                }

                nsError = operationError
            }

            operation.start()

        } else {
            completionHandler(self.cache.results, nsError)
        }


    }

}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-LocationFieldTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-ImageTableViewCell.swift.md)

