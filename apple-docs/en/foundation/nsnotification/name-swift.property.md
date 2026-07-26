---
title: name
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.property.json'
content_hash: 'sha256:c3b810ba463784a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNotification](../nsnotification.md)

# name

<sub>Instance Property</sub>

The name of the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: NSNotification.Name { get }
```

## Discussion

Typically you use this property to find out what kind of notification you are dealing with when you receive a notification.

### Special Considerations

Notification names can be any string. To avoid name collisions, you might want to use a prefix that’s specific to your application.

## See Also

### Getting Notification Information

- [object](object.md) — The object associated with the notification.
- [userInfo](userinfo.md) — The user information dictionary associated with the notification.
