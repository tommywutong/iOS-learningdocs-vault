---
title: 'append(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/append(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/append%28_%3A%29.json'
content_hash: 'sha256:7b514b1f6b45819a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# append(_:)

<sub>Instance Method</sub>

Adds the characters and attributes of a given attributed string to the end of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func append(_ attrString: NSAttributedString)
```

## Parameters

- `attrString` — The string whose characters and attributes are added.

## See Also

### Changing Characters and Attributes

- [- insertAttributedString:atIndex:](<insert(__at_).md>) — Inserts the characters and attributes of the given attributed string into the receiver at the given index.
- [- replaceCharactersInRange:withAttributedString:](<replacecharacters(in_with_)-1uaw7.md>) — Replaces the characters and attributes in a given range with the characters and attributes of the given attributed string.
- [- setAttributedString:](<setattributedstring(__).md>) — Replaces the receiver’s entire contents with the characters and attributes of the given attributed string.
