---
title: 'attributedSubstring(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/attributedsubstring(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/attributedsubstring(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/attributedsubstring%28from%3A%29.json'
content_hash: 'sha256:cf6d8d88748321b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# attributedSubstring(from:)

<sub>Instance Method</sub>

Returns an attributed string consisting of the characters and attributes within the specified range in the attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attributedSubstring(from range: NSRange) -> NSAttributedString
```

## Parameters

- `range` — The range from which to create a new attributed string. `aRange` must lie within the bounds of the receiver.

## Return Value

An `NSAttributedString` object consisting of the characters and attributes within `aRange` in the receiver.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `aRange` lies beyond the end of the receiver’s characters. This method treats the length of the string as a valid range value that returns an empty string.

## See Also

### Getting the characters

- [string](string.md) — The character contents of the attributed string as a string.
- [length](length.md) — The length of the attributed string.
