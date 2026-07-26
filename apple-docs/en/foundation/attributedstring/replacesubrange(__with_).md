---
title: 'replaceSubrange(_:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/replacesubrange(_:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/replacesubrange(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/replacesubrange%28_%3Awith%3A%29.json'
content_hash: 'sha256:d8d610a3d385042c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# replaceSubrange(_:with:)

<sub>Instance Method</sub>

Replaces the contents in a range of the attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSubrange(_ range: some RangeExpression<AttributedString.Index>, with s: some AttributedStringProtocol)
```

## Parameters

- `range` — The range of the attributed string to replace.

- `s` — The string to insert in place of the replaced range.

## See Also

### Modifying an Attributed String

- [insert(_:at:)](<insert(__at_).md>) — Inserts the specified string at a specific index in the attributed string.
- [Index](index.md) — A type that represents the position of a character or code unit within an attributed string.
- [removeSubrange(_:)](<removesubrange(__).md>) — Removes a range of characters from the attributed string.
