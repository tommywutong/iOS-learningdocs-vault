---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/subscript(_:)-2vqsz'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/subscript(_:)-2vqsz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/subscript%28_%3A%29-2vqsz.json'
content_hash: 'sha256:fce631bc3628a5e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns a substring of the attributed string using a range to indicate the substring bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(bounds: some RangeExpression<AttributedString.Index>) -> AttributedSubstring { get set }
```
