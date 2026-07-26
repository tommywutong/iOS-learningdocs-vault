---
title: 'CFCharacterSetAddCharactersInRange(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetaddcharactersinrange(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetaddcharactersinrange(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetaddcharactersinrange%28_%3A_%3A%29.json'
content_hash: 'sha256:ea015bee9dafc110'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetAddCharactersInRange(_:_:)

<sub>Function</sub>

Adds a given range to a character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetAddCharactersInRange(_ theSet: CFMutableCharacterSet!, _ theRange: CFRange)
```

## Parameters

- `theSet` — The character set to modify.

- `theRange` — The range to add to the character set. The range is specified in 32-bits in UTF-32 format, and must lie within the valid Unicode character range (from `0x00000` to `0x10FFFF`).

## See Also

### Adding Characters

- [CFCharacterSetAddCharactersInString](<cfcharactersetaddcharactersinstring(____).md>) — Adds the characters in a given string to a character set.
