---
title: 'deleteCharacters(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/deletecharacters(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/deletecharacters(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/deletecharacters%28in%3A%29.json'
content_hash: 'sha256:3281ce9fb65e1a74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# deleteCharacters(in:)

<sub>Instance Method</sub>

Deletes the characters in the given range along with their associated attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deleteCharacters(in range: NSRange)
```

## Parameters

- `range` — A range specifying the characters to delete.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## See Also

### Related Documentation

- [- replaceCharactersInRange:withAttributedString:](<replacecharacters(in_with_)-1uaw7.md>) — Replaces the characters and attributes in a given range with the characters and attributes of the given attributed string.

### Changing Characters

- [- replaceCharactersInRange:withString:](<replacecharacters(in_with_)-6oq9r.md>) — Replaces the characters in the given range with the characters of the given string.
