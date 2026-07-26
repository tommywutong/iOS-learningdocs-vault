---
title: path
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/path
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/path'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/path.json'
content_hash: 'sha256:a5929f2e1bf4de69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# path

<sub>Instance Property</sub>

The cookie’s path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var path: String { get }
```

## Discussion

The cookie will be sent with requests for this path in the cookie’s domain, and all paths that have this prefix. A path of `"/"` means the cookie will be sent for all URLs in the domain.

## See Also

### Getting cookie host properties

- [domain](domain.md) — The domain of the cookie.
- [portList](portlist.md) — The cookie’s port list.
