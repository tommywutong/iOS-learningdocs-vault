---
title: 'removeSubrange(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/removesubrange(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/removesubrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/removesubrange%28_%3A%29.json'
content_hash: 'sha256:2faf8dad5803544a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# removeSubrange(_:)

<sub>Instance Method</sub>

Removes a range of characters from the attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeSubrange(_ range: some RangeExpression<AttributedString.Index>)
```

## Parameters

- `range` — The range to remove.

## See Also

### Modifying an Attributed String

- [insert(_:at:)](<insert(__at_).md>) — Inserts the specified string at a specific index in the attributed string.
- [Index](index.md) — A type that represents the position of a character or code unit within an attributed string.
- [replaceSubrange(_:with:)](<replacesubrange(__with_).md>) — Replaces the contents in a range of the attributed string.
