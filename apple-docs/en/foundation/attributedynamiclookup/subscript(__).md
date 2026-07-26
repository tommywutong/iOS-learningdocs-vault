---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedynamiclookup/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedynamiclookup/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedynamiclookup/subscript%28_%3A%29.json'
content_hash: 'sha256:2b534ade9d1d2102'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeDynamicLookup](../attributedynamiclookup.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns an attributed string key that corresponds to a specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<T>(_: T.Type) -> T where T : AttributedStringKey { get }
```
