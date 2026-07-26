---
title: userInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexception/userinfo-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/nsexception/userinfo-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexception/userinfo-swift.property.json'
content_hash: 'sha256:5d221f875fe87cb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSException](../nsexception.md)

# userInfo

<sub>Instance Property</sub>

A dictionary containing application-specific data pertaining to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any]? { get }
```

## Discussion

`nil` if no application-specific data exists. As an example, if a method’s return value caused the exception to be raised, the return value might be available to the exception handler through this method.

## See Also

### Related Documentation

- [- initWithName:reason:userInfo:](<init(name_reason_userinfo_).md>) — Initializes and returns a newly allocated exception object.

### Querying an NSException Object

- [name](name-swift.property.md) — A string used to uniquely identify the receiver.
- [reason](reason-swift.property.md) — A string containing a “human-readable” reason for the receiver.
