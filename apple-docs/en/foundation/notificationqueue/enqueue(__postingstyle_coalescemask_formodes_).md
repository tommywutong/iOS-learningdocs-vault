---
title: 'enqueue(_:postingStyle:coalesceMask:forModes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationqueue/enqueue(_:postingstyle:coalescemask:formodes:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationqueue/enqueue(_:postingstyle:coalescemask:formodes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationqueue/enqueue%28_%3Apostingstyle%3Acoalescemask%3Aformodes%3A%29.json'
content_hash: 'sha256:349d989e94d1c28d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationQueue](../notificationqueue.md)

# enqueue(_:postingStyle:coalesceMask:forModes:)

<sub>Instance Method</sub>

Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enqueue(_ notification: Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes modes: [RunLoop.Mode]?)
```

## Parameters

- `notification` — The notification to add to the queue.

- `postingStyle` — The posting style for the notification. The posting style indicates when the notification queue should post the notification to its notification center.

- `coalesceMask` — A mask indicating what criteria to use when matching attributes of `notification` to attributes of notifications in the queue. The mask is created by combining any of the constants [NSNotificationNoCoalescing](notificationcoalescing/none.md), [NSNotificationCoalescingOnName](notificationcoalescing/onname.md), and [NSNotificationCoalescingOnSender](notificationcoalescing/onsender.md).

- `modes` — The list of modes the notification may be posted in. The notification queue will only post the notification to its notification center if the run loop is in one of the modes provided in the array. This parameter may be `nil`, in which case it defaults to [NSDefaultRunLoopMode](../runloop/mode/default.md).

## See Also

### Managing Notifications

- [- enqueueNotification:postingStyle:](<enqueue(__postingstyle_).md>) — Adds a notification to the notification queue with a specified posting style.
- [- dequeueNotificationsMatching:coalesceMask:](<dequeuenotifications(matching_coalescemask_).md>) — Removes all notifications from the queue that match a provided notification using provided matching criteria.
