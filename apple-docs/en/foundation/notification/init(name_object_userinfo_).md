---
title: 'init(name:object:userInfo:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notification/init(name:object:userinfo:)'
source_url: 'https://developer.apple.com/documentation/foundation/notification/init(name:object:userinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notification/init%28name%3Aobject%3Auserinfo%3A%29.json'
content_hash: 'sha256:52213f76e1edb450'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Notification](../notification.md)

# init(name:object:userInfo:)

<sub>Initializer</sub>

Initializes a new notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(name: Notification.Name, object: Any? = nil, userInfo: [AnyHashable : Any]? = nil)
```

## Discussion

The default value for `userInfo` is nil.

## See Also

### Creating a Notification

- [Name](name-swift.typealias.md) — An alias for a type used to represent the name of a notification.
- [Name](../nsnotification/name-swift.struct.md) — A structure that defines the name of a notification.
