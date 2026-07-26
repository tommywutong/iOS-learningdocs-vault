---
title: 'insert(_:at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/insert(_:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/insert(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/insert%28_%3Aat%3A%29.json'
content_hash: 'sha256:5d4be06498abbe33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# insert(_:at:)

<sub>Instance Method</sub>

Inserts the specified string at a specific index in the attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert(_ s: some AttributedStringProtocol, at index: AttributedString.Index)
```

## Parameters

- `s` — The string to insert.

- `index` — The index that indicates where to insert the string.

## See Also

### Modifying an Attributed String

- [Index](index.md) — A type that represents the position of a character or code unit within an attributed string.
- [removeSubrange(_:)](<removesubrange(__).md>) — Removes a range of characters from the attributed string.
- [replaceSubrange(_:with:)](<replacesubrange(__with_).md>) — Replaces the contents in a range of the attributed string.
