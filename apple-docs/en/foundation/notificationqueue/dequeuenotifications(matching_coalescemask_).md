---
title: 'dequeueNotifications(matching:coalesceMask:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationqueue/dequeuenotifications(matching:coalescemask:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationqueue/dequeuenotifications(matching:coalescemask:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationqueue/dequeuenotifications%28matching%3Acoalescemask%3A%29.json'
content_hash: 'sha256:34e816521f5ec7ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationQueue](../notificationqueue.md)

# dequeueNotifications(matching:coalesceMask:)

<sub>Instance Method</sub>

Removes all notifications from the queue that match a provided notification using provided matching criteria.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dequeueNotifications(matching notification: Notification, coalesceMask: Int)
```

## Parameters

- `notification` — The notification used for matching notifications to remove from the notification queue.

- `coalesceMask` — A mask indicating what criteria to use when matching attributes of `notification` to attributes of notifications in the queue. The mask is created by combining any of the constants [NSNotificationNoCoalescing](notificationcoalescing/none.md), [NSNotificationCoalescingOnName](notificationcoalescing/onname.md), and [NSNotificationCoalescingOnSender](notificationcoalescing/onsender.md).

## See Also

### Managing Notifications

- [- enqueueNotification:postingStyle:coalesceMask:forModes:](<enqueue(__postingstyle_coalescemask_formodes_).md>) — Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
- [- enqueueNotification:postingStyle:](<enqueue(__postingstyle_).md>) — Adds a notification to the notification queue with a specified posting style.
