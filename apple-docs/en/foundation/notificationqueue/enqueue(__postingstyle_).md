---
title: 'enqueue(_:postingStyle:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationqueue/enqueue(_:postingstyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationqueue/enqueue(_:postingstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationqueue/enqueue%28_%3Apostingstyle%3A%29.json'
content_hash: 'sha256:fe6a231112dffc13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationQueue](../notificationqueue.md)

# enqueue(_:postingStyle:)

<sub>Instance Method</sub>

Adds a notification to the notification queue with a specified posting style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enqueue(_ notification: Notification, postingStyle: NotificationQueue.PostingStyle)
```

## Parameters

- `notification` — The notification to add to the queue.

- `postingStyle` — The posting style for the notification. The posting style indicates when the notification queue should post the notification to its notification center.

## Discussion

This is a convenience method for calling [- enqueueNotification:postingStyle:coalesceMask:forModes:](<enqueue(__postingstyle_coalescemask_formodes_).md>) with coalescing criteria that will coalesce only notifications that match both the notification’s name and object and the runloop mode [NSDefaultRunLoopMode](../runloop/mode/default.md).

## See Also

### Managing Notifications

- [- enqueueNotification:postingStyle:coalesceMask:forModes:](<enqueue(__postingstyle_coalescemask_formodes_).md>) — Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
- [- dequeueNotificationsMatching:coalesceMask:](<dequeuenotifications(matching_coalescemask_).md>) — Removes all notifications from the queue that match a provided notification using provided matching criteria.
