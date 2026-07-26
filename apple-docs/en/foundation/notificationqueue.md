---
title: NotificationQueue
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationqueue
source_url: 'https://developer.apple.com/documentation/foundation/notificationqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationqueue.json'
content_hash: 'sha256:1f8223825612fae5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NotificationQueue

<sub>Class</sub>

A notification center buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NotificationQueue
```

## Overview

Whereas a notification center distributes notifications when posted, notifications placed into the queue can be delayed until the end of the current pass through the run loop or until the run loop is idle. Duplicate notifications can be coalesced so that only one notification is sent although multiple notifications are posted.

A notification queue maintains notifications in first in, first out (FIFO) order. When a notification moves to the front of the queue, the queue posts it to the notification center, which in turn dispatches the notification to all objects registered as observers.

Every thread has a default notification queue, which is associated with the default notification center for the process. You can create your own notification queues and have multiple queues per center and thread.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Notification Queues

- [- initWithNotificationCenter:](<notificationqueue/init(notificationcenter_).md>) — Initializes and returns a notification queue for the specified notification center.

### Getting the Default Queue

- [defaultQueue](notificationqueue/default.md) — Returns the default notification queue for the current thread.

### Managing Notifications

- [- enqueueNotification:postingStyle:coalesceMask:forModes:](<notificationqueue/enqueue(__postingstyle_coalescemask_formodes_).md>) — Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
- [- enqueueNotification:postingStyle:](<notificationqueue/enqueue(__postingstyle_).md>) — Adds a notification to the notification queue with a specified posting style.
- [- dequeueNotificationsMatching:coalesceMask:](<notificationqueue/dequeuenotifications(matching_coalescemask_).md>) — Removes all notifications from the queue that match a provided notification using provided matching criteria.

### Constants

- [NotificationCoalescing](notificationqueue/notificationcoalescing.md) — The constants that specify how notifications are coalesced.
- [PostingStyle](notificationqueue/postingstyle.md) — The constants that specify when notifications are posted.

## See Also

### Notifications

- [Notification](notification.md) — A container for information broadcast through a notification center to all registered observers.
- [NotificationCenter](notificationcenter.md) — A notification dispatch mechanism that enables the broadcast of information to registered observers.
