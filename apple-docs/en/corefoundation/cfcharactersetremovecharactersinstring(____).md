---
title: 'CFCharacterSetRemoveCharactersInString(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetremovecharactersinstring(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetremovecharactersinstring(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetremovecharactersinstring%28_%3A_%3A%29.json'
content_hash: 'sha256:e6f7760174c9a560'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetRemoveCharactersInString(_:_:)

<sub>Function</sub>

Removes the characters in a given string from a character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetRemoveCharactersInString(_ theSet: CFMutableCharacterSet!, _ theString: CFString!)
```

## Parameters

- `theSet` — The character set to modify.

- `theString` — A string containing the characters to remove from `theSet`.

## See Also

### Removing Characters

- [CFCharacterSetRemoveCharactersInRange](<cfcharactersetremovecharactersinrange(____).md>) — Removes a given range of Unicode characters from a character set.
