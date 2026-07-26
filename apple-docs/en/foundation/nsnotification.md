---
title: NSNotification
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification.json'
content_hash: 'sha256:00053ec6edc642b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSNotification

<sub>Class</sub>

A container for information broadcast through a notification center to all registered observers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSNotification
```

## Overview

In Swift, this object bridges to [Notification](notification.md); use [NSNotification](nsnotification.md) when you need reference semantics or other Foundation-specific behavior.

A notification contains a name, an object, and an optional dictionary, and is broadcast to by instances of  [NotificationCenter](notificationcenter.md) or [DistributedNotificationCenter](distributednotificationcenter.md). The name is a tag identifying the notification. The object is any object that the poster of the notification wants to send to observers of that notification (typically, the object posting the notification). The dictionary stores other related objects, if any. [NSNotification](nsnotification.md) objects are immutable.

You don’t usually create your own notifications directly, but instead call the [NotificationCenter](notificationcenter.md) methods [- postNotificationName:object:](<notificationcenter/post(name_object_).md>) and [- postNotificationName:object:userInfo:](<notificationcenter/post(name_object_userinfo_).md>).

> [!important] Important
> The Swift overlay to the Foundation framework provides the [Notification](notification.md) structure, which bridges to the [NSNotification](nsnotification.md) class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

### Object Comparison

The objects of a notification are compared using pointer equality for local notifications. Distributed notifications use strings as their objects, and those strings are compared using [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>), because pointer equality doesn’t make sense across process boundaries.

### Creating Subclasses

You can subclass [NSNotification](nsnotification.md) to contain information in addition to the notification name, object, and dictionary. This extra data must be agreed upon between notifiers and observers.

[NotificationCenter](notificationcenter.md) is a class cluster with no instance variables. As such, you must subclass [NSNotification](nsnotification.md) and override the primitive methods [name](nsnotification/name-swift.property.md), [object](nsnotification/object.md), and [userInfo](nsnotification/userinfo.md). You can choose any designated initializer you like, but be sure that your initializer does not call [init](nsnotification/init.md) on `super` ([NSNotification](nsnotification.md) is not meant to be instantiated directly, and its `init` method raises an exception).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Notifications

- [- initWithCoder:](<nsnotification/init(coder_).md>) — Initializes a notification with the data from an unarchiver.
- [+ notificationWithName:object:](<nsnotification/init(name_object_).md>) — Returns a new notification object with a specified name and object.
- [- initWithName:object:userInfo:](<nsnotification/init(name_object_userinfo_).md>) — Initializes a notification with a specified name, object, and user information.
- [Name](nsnotification/name-swift.struct.md) — A structure that defines the name of a notification.

### Getting Notification Information

- [name](nsnotification/name-swift.property.md) — The name of the notification.
- [object](nsnotification/object.md) — The object associated with the notification.
- [userInfo](nsnotification/userinfo.md) — The user information dictionary associated with the notification.

## See Also

### Related Documentation

- [Notification Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)
