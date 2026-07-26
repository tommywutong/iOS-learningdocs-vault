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
doc_path: '/documentation/foundation/discontiguousattributedsubstring/subscript(_:)-6j670'
source_url: 'https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring/subscript(_:)-6j670'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/discontiguousattributedsubstring/subscript%28_%3A%29-6j670.json'
content_hash: 'sha256:b808a1f06d27ec81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DiscontiguousAttributedSubstring](../discontiguousattributedsubstring.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns a discontiguous substring of this discontiguous attributed string using a range to indicate the discontiguous substring bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(bounds: some RangeExpression<AttributedString.Index>) -> DiscontiguousAttributedSubstring { get }
```

## Parameters

- `bounds` — A range that indicates the bounds of the discontiguous substring to return.
