---
title: object
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notification/object
source_url: 'https://developer.apple.com/documentation/foundation/notification/object'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notification/object.json'
content_hash: 'sha256:d96c0d376e6dabc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Notification](../notification.md)

# object

<sub>Instance Property</sub>

An object that the poster wishes to send to observers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var object: Any?
```

## Discussion

Typically this is the object that posted the notification.

## See Also

### Getting Notification Information

- [name](name-swift.property.md) — A tag identifying the notification.
- [userInfo](userinfo.md) — Storage for values or objects related to this notification.
