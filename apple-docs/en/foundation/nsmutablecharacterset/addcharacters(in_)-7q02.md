---
title: 'addCharacters(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablecharacterset/addcharacters(in:)-7q02'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablecharacterset/addcharacters(in:)-7q02'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablecharacterset/addcharacters%28in%3A%29-7q02.json'
content_hash: 'sha256:976576a6047515e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableCharacterSet](../nsmutablecharacterset.md)

# addCharacters(in:)

<sub>Instance Method</sub>

Adds to the receiver the characters in a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addCharacters(in aString: String)
```

## Parameters

- `aString` — The characters to add to the receiver.

## Discussion

This method has no effect if `aString` is empty.

## See Also

### Adding and Removing Characters

- [- addCharactersInRange:](<addcharacters(in_)-4ppyw.md>) — Adds to the receiver the characters whose Unicode values are in a given range.
- [- removeCharactersInRange:](<removecharacters(in_)-70nqp.md>) — Removes from the receiver the characters whose Unicode values are in a given range.
- [- removeCharactersInString:](<removecharacters(in_)-762gt.md>) — Removes from the receiver the characters in a given string.
