---
title: 'init(name:object:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsnotification/init(name:object:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/init(name:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/init%28name%3Aobject%3A%29.json'
content_hash: 'sha256:e4cb2542887b0e6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNotification](../nsnotification.md)

# init(name:object:)

<sub>Initializer</sub>

Returns a new notification object with a specified name and object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(name aName: NSNotification.Name, object anObject: Any?)
```

## Parameters

- `aName` — The name for the new notification. May not be `nil`.

- `anObject` — The object for the new notification.

## See Also

### Related Documentation

- [- postNotificationName:object:](<../notificationcenter/post(name_object_).md>) — Creates a notification with a given name and sender and posts it to the notification center.
- [Notification Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)

### Creating Notifications

- [- initWithCoder:](<init(coder_).md>) — Initializes a notification with the data from an unarchiver.
- [- initWithName:object:userInfo:](<init(name_object_userinfo_).md>) — Initializes a notification with a specified name, object, and user information.
- [Name](name-swift.struct.md) — A structure that defines the name of a notification.
