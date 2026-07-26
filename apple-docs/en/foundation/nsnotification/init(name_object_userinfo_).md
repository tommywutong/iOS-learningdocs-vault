---
title: 'init(name:object:userInfo:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsnotification/init(name:object:userinfo:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/init(name:object:userinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/init%28name%3Aobject%3Auserinfo%3A%29.json'
content_hash: 'sha256:7024644a4d95f53f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNotification](../nsnotification.md)

# init(name:object:userInfo:)

<sub>Initializer</sub>

Initializes a notification with a specified name, object, and user information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]? = nil)
```

## Parameters

- `name` — The name for the new notification. May not be `nil`.

- `object` — The object for the new notification.

- `userInfo` — The user information dictionary for the new notification. May be `nil`.

## See Also

### Creating Notifications

- [- initWithCoder:](<init(coder_).md>) — Initializes a notification with the data from an unarchiver.
- [+ notificationWithName:object:](<init(name_object_).md>) — Returns a new notification object with a specified name and object.
- [Name](name-swift.struct.md) — A structure that defines the name of a notification.
