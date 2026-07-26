---
title: expiresDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/expiresdate
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/expiresdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/expiresdate.json'
content_hash: 'sha256:d4a4b369395ece2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# expiresDate

<sub>Instance Property</sub>

The cookie’s expiration date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var expiresDate: Date? { get }
```

## Discussion

This value is `nil` if there is no specific expiration date, as with session-only cookies. The expiration date is the date when the cookie should be deleted.

## See Also

### Determining cookie lifespan

- [sessionOnly](issessiononly.md) — A Boolean value that indicates whether the cookie should be discarded at the end of the session (regardless of expiration date).
