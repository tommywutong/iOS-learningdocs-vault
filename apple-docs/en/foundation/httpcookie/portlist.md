---
title: portList
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/portlist
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/portlist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/portlist.json'
content_hash: 'sha256:0d5a13151f2126f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# portList

<sub>Instance Property</sub>

The cookie’s port list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var portList: [NSNumber]? { get }
```

## Discussion

The list of ports for the cookie, returned as an array of `NSNumber` objects containing integers. If the cookie has no port list, the value of this property is `nil` and the cookie will be sent to any port. Otherwise, the cookie is only sent to ports specified in the port list.

## See Also

### Getting cookie host properties

- [domain](domain.md) — The domain of the cookie.
- [path](path.md) — The cookie’s path.
