---
title: 'removeCharacters(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablecharacterset/removecharacters(in:)-762gt'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablecharacterset/removecharacters(in:)-762gt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablecharacterset/removecharacters%28in%3A%29-762gt.json'
content_hash: 'sha256:1d1d0c6956a2fef1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableCharacterSet](../nsmutablecharacterset.md)

# removeCharacters(in:)

<sub>Instance Method</sub>

Removes from the receiver the characters in a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeCharacters(in aString: String)
```

## Parameters

- `aString` — The characters to remove from the receiver.

## Discussion

This method has no effect if `aString` is empty.

## See Also

### Adding and Removing Characters

- [- addCharactersInRange:](<addcharacters(in_)-4ppyw.md>) — Adds to the receiver the characters whose Unicode values are in a given range.
- [- removeCharactersInRange:](<removecharacters(in_)-70nqp.md>) — Removes from the receiver the characters whose Unicode values are in a given range.
- [- addCharactersInString:](<addcharacters(in_)-7q02.md>) — Adds to the receiver the characters in a given string.
