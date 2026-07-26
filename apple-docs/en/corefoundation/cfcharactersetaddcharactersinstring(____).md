---
title: 'CFCharacterSetAddCharactersInString(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetaddcharactersinstring(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetaddcharactersinstring(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetaddcharactersinstring%28_%3A_%3A%29.json'
content_hash: 'sha256:028fc643eaa46db3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetAddCharactersInString(_:_:)

<sub>Function</sub>

Adds the characters in a given string to a character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetAddCharactersInString(_ theSet: CFMutableCharacterSet!, _ theString: CFString!)
```

## Parameters

- `theSet` — The character set to modify.

- `theString` — A string containing the characters to add to `theSet`.

## See Also

### Adding Characters

- [CFCharacterSetAddCharactersInRange](<cfcharactersetaddcharactersinrange(____).md>) — Adds a given range to a character set.
