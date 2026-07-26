---
title: version
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/version
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/version.json'
content_hash: 'sha256:dbabfb55fefb873c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# version

<sub>Instance Property</sub>

The cookie’s version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var version: Int { get }
```

## Discussion

Version 0 maps to “old-style” Netscape cookies. Version 1 maps to [RFC 6265](https://tools.ietf.org/html/rfc6265) cookies.

## See Also

### Getting cookie metadata

- [name](name.md) — The cookie’s name.
- [value](value.md) — The cookie’s string value.
