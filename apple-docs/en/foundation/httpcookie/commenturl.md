---
title: commentURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/commenturl
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/commenturl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/commenturl.json'
content_hash: 'sha256:75399be0b9bc2be8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# commentURL

<sub>Instance Property</sub>

The cookie’s comment URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var commentURL: URL? { get }
```

## Discussion

This value is `nil` if the cookie has no comment URL. This value specifies a URL that can be presented to the user as a link for further information about this cookie.

## See Also

### Getting user-readable cookie metadata

- [comment](comment.md) — The cookie’s comment string.
