---
title: 'CFCharacterSetRemoveCharactersInRange(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetremovecharactersinrange(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetremovecharactersinrange(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetremovecharactersinrange%28_%3A_%3A%29.json'
content_hash: 'sha256:8d2f934a821bc95d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetRemoveCharactersInRange(_:_:)

<sub>Function</sub>

Removes a given range of Unicode characters from a character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetRemoveCharactersInRange(_ theSet: CFMutableCharacterSet!, _ theRange: CFRange)
```

## Parameters

- `theSet` — The character set to modify.

- `theRange` — The range to remove from the character set. The range is specified in 32-bits in UTF-32 format, and must lie within the valid Unicode character range (from `0x00000` to `0x10FFFF`).

## See Also

### Removing Characters

- [CFCharacterSetRemoveCharactersInString](<cfcharactersetremovecharactersinstring(____).md>) — Removes the characters in a given string from a character set.
