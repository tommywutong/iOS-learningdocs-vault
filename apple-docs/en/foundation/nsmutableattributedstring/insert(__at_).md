---
title: 'insert(_:at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/insert(_:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/insert(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/insert%28_%3Aat%3A%29.json'
content_hash: 'sha256:11958cc01742baa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# insert(_:at:)

<sub>Instance Method</sub>

Inserts the characters and attributes of the given attributed string into the receiver at the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func insert(_ attrString: NSAttributedString, at loc: Int)
```

## Parameters

- `attrString` — The string whose characters and attributes are inserted.

- `loc` — The index at which the characters and attributes are inserted.

## Discussion

The new characters and attributes begin at the given index and the existing characters and attributes from the index to the end of the receiver are shifted by the length of the attributed string. Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `loc` lies beyond the end of the receiver’s characters.

## See Also

### Changing Characters and Attributes

- [- appendAttributedString:](<append(__).md>) — Adds the characters and attributes of a given attributed string to the end of the receiver.
- [- replaceCharactersInRange:withAttributedString:](<replacecharacters(in_with_)-1uaw7.md>) — Replaces the characters and attributes in a given range with the characters and attributes of the given attributed string.
- [- setAttributedString:](<setattributedstring(__).md>) — Replaces the receiver’s entire contents with the characters and attributes of the given attributed string.
