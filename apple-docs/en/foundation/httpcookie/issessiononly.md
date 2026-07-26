---
title: isSessionOnly
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/issessiononly
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/issessiononly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/issessiononly.json'
content_hash: 'sha256:0e8a9deb4e16f32b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# isSessionOnly

<sub>Instance Property</sub>

A Boolean value that indicates whether the cookie should be discarded at the end of the session (regardless of expiration date).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSessionOnly: Bool { get }
```

## Discussion

This value is [true](../../swift/true.md) if the cookie should be discarded at the end of the session (regardless of expiration date), otherwise [false](../../swift/false.md).

## See Also

### Determining cookie lifespan

- [expiresDate](expiresdate.md) — The cookie’s expiration date.
