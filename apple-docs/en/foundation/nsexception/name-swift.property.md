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
doc_path: /documentation/foundation/nsexception/name-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/nsexception/name-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexception/name-swift.property.json'
content_hash: 'sha256:90e6ab9dd7a40fe6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSException](../nsexception.md)

# name

<sub>Instance Property</sub>

A string used to uniquely identify the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: NSExceptionName { get }
```

## See Also

### Related Documentation

- [- initWithName:reason:userInfo:](<init(name_reason_userinfo_).md>) — Initializes and returns a newly allocated exception object.

### Querying an NSException Object

- [reason](reason-swift.property.md) — A string containing a “human-readable” reason for the receiver.
- [userInfo](userinfo-swift.property.md) — A dictionary containing application-specific data pertaining to the receiver.
