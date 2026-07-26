---
title: 'init(coder:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsnotification/init(coder:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/init%28coder%3A%29.json'
content_hash: 'sha256:3fafc804a185e8ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNotification](../nsnotification.md)

# init(coder:)

<sub>Initializer</sub>

Initializes a notification with the data from an unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(coder: NSCoder)
```

## See Also

### Creating Notifications

- [+ notificationWithName:object:](<init(name_object_).md>) — Returns a new notification object with a specified name and object.
- [- initWithName:object:userInfo:](<init(name_object_userinfo_).md>) — Initializes a notification with a specified name, object, and user information.
- [Name](name-swift.struct.md) — A structure that defines the name of a notification.
