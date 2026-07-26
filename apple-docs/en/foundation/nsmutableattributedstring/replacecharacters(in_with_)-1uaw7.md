---
title: 'replaceCharacters(in:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/replacecharacters(in:with:)-1uaw7'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/replacecharacters(in:with:)-1uaw7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/replacecharacters%28in%3Awith%3A%29-1uaw7.json'
content_hash: 'sha256:192774666a89a737'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# replaceCharacters(in:with:)

<sub>Instance Method</sub>

Replaces the characters and attributes in a given range with the characters and attributes of the given attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceCharacters(in range: NSRange, with attrString: NSAttributedString)
```

## Parameters

- `range` — The range of characters and attributes replaced.

- `attrString` — The attributed string whose characters and attributes replace those in the specified range.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## See Also

### Changing Characters and Attributes

- [- appendAttributedString:](<append(__).md>) — Adds the characters and attributes of a given attributed string to the end of the receiver.
- [- insertAttributedString:atIndex:](<insert(__at_).md>) — Inserts the characters and attributes of the given attributed string into the receiver at the given index.
- [- setAttributedString:](<setattributedstring(__).md>) — Replaces the receiver’s entire contents with the characters and attributes of the given attributed string.
