---
title: 'init(rawValue:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiestringpolicy/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestringpolicy/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestringpolicy/init%28rawvalue%3A%29.json'
content_hash: 'sha256:0e89861e16f9e861'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStringPolicy](../httpcookiestringpolicy.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates an HTTP cookie string policy from the given raw string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(rawValue: String)
```

## Discussion

URL Loading System ignores any policy with a raw value other than the predefined policy values: `strict` and `lax`.
