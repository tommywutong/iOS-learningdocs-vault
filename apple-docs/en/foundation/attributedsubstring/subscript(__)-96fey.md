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
doc_path: '/documentation/foundation/attributedsubstring/subscript(_:)-96fey'
source_url: 'https://developer.apple.com/documentation/foundation/attributedsubstring/subscript(_:)-96fey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedsubstring/subscript%28_%3A%29-96fey.json'
content_hash: 'sha256:67800dc63bc74bd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedSubstring](../attributedsubstring.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns a substring of the attributed substring that a range indicates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(bounds: some RangeExpression<AttributedString.Index>) -> AttributedSubstring { get }
```
