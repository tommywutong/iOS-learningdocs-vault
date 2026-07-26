---
title: 'init(charactersIn:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscharacterset/init(charactersin:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/init(charactersin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/init%28charactersin%3A%29.json'
content_hash: 'sha256:426df2baf174e615'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# init(charactersIn:)

<sub>Initializer</sub>

Returns a character set containing the characters in a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(charactersIn aString: String)
```

## Parameters

- `aString` — A string containing characters for the new character set.

## Return Value

A character set containing the characters in `aString`. Returns an empty character set if `aString` is empty.

## See Also

### Creating a Custom Character Set

- [- initWithCoder:](<init(coder_).md>)
- [+ characterSetWithRange:](<init(range_).md>) — Returns a character set containing characters with Unicode values in a given range.
- [NSOpenStepUnicodeReservedBase](../1560803-nsopenstepunicodereservedbase.md) — Specifies lower bound for a Unicode character range reserved for Apple’s corporate use.
