---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/subscript(_:)-ftoi'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/subscript(_:)-ftoi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/subscript%28_%3A%29-ftoi.json'
content_hash: 'sha256:c6e7c8eab62a04a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns a discontiguous substring of this discontiguous attributed string using a set of ranges to indicate the discontiguous substring bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(indices: RangeSet<AttributedString.Index>) -> DiscontiguousAttributedSubstring { get set }
```

## Parameters

- `indices` — A set of ranges that indicate the bounds of the discontiguous substring to return.
