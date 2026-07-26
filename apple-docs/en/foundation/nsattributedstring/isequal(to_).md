---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/isequal%28to%3A%29.json'
content_hash: 'sha256:127df38c8fab7244'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the attributed string is equal to the specified string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to other: NSAttributedString) -> Bool
```

## Parameters

- `other` — The attributed string with which to compare the receiver.

## Return Value

[true](../../swift/true.md) if the text and attributes in the current string and `otherString` are the same, otherwise [false](../../swift/false.md).

## Discussion

This method performs a character-by-character comparison of the string and its attributes. The character and its attributes must be the same in both strings for the method to return [true](../../swift/true.md). In attributed strings with many attributes, such a comparison is unlikely to yield an exact match [true](../../swift/true.md).
