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
doc_path: '/documentation/foundation/nsmutablecharacterset/removecharacters(in:)-70nqp'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablecharacterset/removecharacters(in:)-70nqp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablecharacterset/removecharacters%28in%3A%29-70nqp.json'
content_hash: 'sha256:3124bd691c76884c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableCharacterSet](../nsmutablecharacterset.md)

# removeCharacters(in:)

<sub>Instance Method</sub>

Removes from the receiver the characters whose Unicode values are in a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeCharacters(in aRange: NSRange)
```

## Parameters

- `aRange` — The range of characters to remove. `aRange.location` is the value of the first character to remove; `aRange.location + aRange.length – 1` is the value of the last. If `aRange.length` is `0`, this method has no effect.

## See Also

### Adding and Removing Characters

- [- addCharactersInRange:](<addcharacters(in_)-4ppyw.md>) — Adds to the receiver the characters whose Unicode values are in a given range.
- [- addCharactersInString:](<addcharacters(in_)-7q02.md>) — Adds to the receiver the characters in a given string.
- [- removeCharactersInString:](<removecharacters(in_)-762gt.md>) — Removes from the receiver the characters in a given string.
