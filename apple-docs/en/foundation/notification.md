---
title: Notification
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notification
source_url: 'https://developer.apple.com/documentation/foundation/notification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notification.json'
content_hash: 'sha256:3d23adbba4f52d9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Notification

<sub>Structure</sub>

A container for information broadcast through a notification center to all registered observers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Notification
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ReferenceConvertible](referenceconvertible.md)

## Topics

### Creating a Notification

- [init(name:object:userInfo:)](<notification/init(name_object_userinfo_).md>) — Initializes a new notification.
- [Name](notification/name-swift.typealias.md) — An alias for a type used to represent the name of a notification.
- [Name](nsnotification/name-swift.struct.md) — A structure that defines the name of a notification.

### Getting Notification Information

- [name](notification/name-swift.property.md) — A tag identifying the notification.
- [object](notification/object.md) — An object that the poster wishes to send to observers.
- [userInfo](notification/userinfo.md) — Storage for values or objects related to this notification.

### Using Reference Types

- [NSNotification](nsnotification.md) — A container for information broadcast through a notification center to all registered observers.

### Operators

- [==(_:_:)](<notification/==(____).md>) — Compare two notifications for equality.

## See Also

### Notifications

- [NotificationCenter](notificationcenter.md) — A notification dispatch mechanism that enables the broadcast of information to registered observers.
- [NotificationQueue](notificationqueue.md) — A notification center buffer.
