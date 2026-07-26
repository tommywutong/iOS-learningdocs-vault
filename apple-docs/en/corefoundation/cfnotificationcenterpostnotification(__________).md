---
title: 'CFNotificationCenterPostNotification(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnotificationcenterpostnotification(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationcenterpostnotification(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationcenterpostnotification%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:68eaa4937c858140'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNotificationCenterPostNotification(_:_:_:_:_:)

<sub>Function</sub>

Posts a notification for an object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNotificationCenterPostNotification(_ center: CFNotificationCenter!, _ name: CFNotificationName!, _ object: UnsafeRawPointer!, _ userInfo: CFDictionary!, _ deliverImmediately: Bool)
```

## Parameters

- `center` — The notification center to post the notification.

- `name` — The name of the notification to post. This value must not be `NULL`.

- `object` — The object posting the notification. If `NULL`, the notification is sent only to observers that are observing all objects. In other words, only observers that registered for the notification with a `NULL` value for `object` will receive the notification. If you want to allow your clients to register for notifications using Cocoa APIs (see [NotificationCenter](../foundation/notificationcenter.md)), then `object` must be a Core Foundation or Cocoa object. For distributed notifications, `object` must be a CFString object. If `center` is a Darwin notification center, this value is ignored.

- `userInfo` — A dictionary passed to observers. You populate this dictionary with additional information describing the notification. For distributed notifications, the dictionary must contain only property list objects. This value may be `NULL`. If `center` is a Darwin notification center, this value is ignored.

- `deliverImmediately` — If `true`, the notification is delivered to all observers immediately, even if some observers are in suspended (background) applications and they requested different suspension behavior when registering for the notification. If `false`, each observer’s requested suspension behavior is respected. If `center` is a Darwin notification center, this value is ignored.

## See Also

### Posting a Notification

- [CFNotificationCenterPostNotificationWithOptions](<cfnotificationcenterpostnotificationwithoptions(__________).md>) — Posts a notification for an object using specified options.
