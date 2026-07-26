---
title: 'replaceCharacters(in:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/replacecharacters(in:with:)-6oq9r'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/replacecharacters(in:with:)-6oq9r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/replacecharacters%28in%3Awith%3A%29-6oq9r.json'
content_hash: 'sha256:80f887c6ffca380e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# replaceCharacters(in:with:)

<sub>Instance Method</sub>

Replaces the characters in the given range with the characters of the given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceCharacters(in range: NSRange, with str: String)
```

## Parameters

- `range` — A range specifying the characters to replace.

- `str` — A string specifying the characters to replace those in `range`.

## Discussion

The new characters inherit the attributes of the first replaced character from `range`. Where the length of `range` is 0, the new characters inherit the attributes of the character preceding `range` if it has any, otherwise of the character following `range`.

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## See Also

### Changing Characters

- [- deleteCharactersInRange:](<deletecharacters(in_).md>) — Deletes the characters in the given range along with their associated attributes.
