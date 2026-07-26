---
title: NotificationCenter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter.json'
content_hash: 'sha256:441719807c829835'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NotificationCenter

<sub>Class</sub>

A notification dispatch mechanism that enables the broadcast of information to registered observers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NotificationCenter
```

## Overview

Callers register with a notification center to receive one or both of the following:

- [NSNotification](nsnotification.md) objects, when working in Objective-C or with frameworks that only support [NSNotification](nsnotification.md). Objects register with a notification center to receive notifications ([NSNotification](nsnotification.md) objects) using the [- addObserver:selector:name:object:](<notificationcenter/addobserver(__selector_name_object_).md>) or [- addObserverForName:object:queue:usingBlock:](<notificationcenter/addobserver(forname_object_queue_using_).md>) methods, specifying a notification name and optionally a source object. When a caller adds itself as an observer, it specifies which notifications it should receive.
- [MainActorMessage](notificationcenter/mainactormessage.md) and [AsyncMessage](notificationcenter/asyncmessage.md) instances for use with Swift code, providing strong typing, appropriate actor isolation, and a more idiomatic Swift experience. Callers register with the notification center using the various flavors of the `addObserver(of:for:using:)` method, specifying either a message type or a convenience [MessageIdentifier](notificationcenter/messageidentifier.md) to identify the notification messages to receive. See [Notification center messages](notification-center-messages.md) for more information about this API.

Callers may add observers for many different notifications, or even the same notification name or message type as produced by different source objects.

Each running app has a [defaultCenter](notificationcenter/default.md) notification center, and you can create new notification centers to organize communications in particular contexts.

A notification center can deliver notifications only within a single program. On macOS, if you want to post a notification to other processes or receive notifications from other processes, use [DistributedNotificationCenter](distributednotificationcenter.md) instead.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [DistributedNotificationCenter](distributednotificationcenter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the default notification center

- [defaultCenter](notificationcenter/default.md) — The app’s default notification center.

### Adding and removing notification observers

- [- addObserverForName:object:queue:usingBlock:](<notificationcenter/addobserver(forname_object_queue_using_).md>) — Adds an entry to the notification center to receive notifications that passed to the provided block.
- [- addObserver:selector:name:object:](<notificationcenter/addobserver(__selector_name_object_).md>) — Adds an entry to the notification center to call the provided selector with the notification.
- [- removeObserver:name:object:](<notificationcenter/removeobserver(__name_object_).md>) — Removes matching entries from the notification center’s dispatch table.
- [- removeObserver:](<notificationcenter/removeobserver(__)-2yciv.md>) — Removes all entries specifying an observer from the notification center’s dispatch table.

### Posting notifications

- [- postNotification:](<notificationcenter/post(__)-3x2st.md>) — Posts a given notification to the notification center.
- [- postNotificationName:object:userInfo:](<notificationcenter/post(name_object_userinfo_).md>) — Creates a notification with a given name, sender, and information and posts it to the notification center.
- [- postNotificationName:object:](<notificationcenter/post(name_object_).md>) — Creates a notification with a given name and sender and posts it to the notification center.

### Receiving notifications as an asynchronous sequence

- [notifications(named:object:)](<notificationcenter/notifications(named_object_).md>) — Returns an asynchronous sequence of notifications produced by this center for a given notification name and optional source object.
- [Notifications](notificationcenter/notifications.md) — An asynchronous sequence of notifications generated by a notification center.

### Receiving notifications as a Combine publisher

- [publisher(for:object:)](<notificationcenter/publisher(for_object_).md>) — Returns a publisher that emits events when broadcasting notifications.
- [Publisher](notificationcenter/publisher.md) — A publisher that emits elements when broadcasting notifications.

### Using notification center with Swift actor isolation

- [Notification center messages](notification-center-messages.md) — Use Foundation’s notification center with Swift concurrency.

## See Also

### Notifications

- [Notification](notification.md) — A container for information broadcast through a notification center to all registered observers.
- [NotificationQueue](notificationqueue.md) — A notification center buffer.
