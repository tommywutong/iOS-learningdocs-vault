---
title: comment
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/comment
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/comment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/comment.json'
content_hash: 'sha256:b129c301951f3584'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# comment

<sub>Instance Property</sub>

The cookie’s comment string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var comment: String? { get }
```

## Discussion

This value is `nil` if the cookie has no comment. You can present this string to the user, explaining the contents and purpose of this cookie.

## See Also

### Getting user-readable cookie metadata

- [commentURL](commenturl.md) — The cookie’s comment URL.
