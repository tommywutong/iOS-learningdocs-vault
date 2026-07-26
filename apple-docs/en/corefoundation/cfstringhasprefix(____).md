---
title: 'CFStringHasPrefix(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringhasprefix(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringhasprefix(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringhasprefix%28_%3A_%3A%29.json'
content_hash: 'sha256:81d3adcf17c7fbc1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringHasPrefix(_:_:)

<sub>Function</sub>

Determines if the character data of a string begin with a specified sequence of characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringHasPrefix(_ theString: CFString!, _ prefix: CFString!) -> Bool
```

## Parameters

- `theString` — The string to search.

- `prefix` — The prefix to search for.

## Return Value

`true` if `theString` begins with `prefix`, `false` if otherwise.

## See Also

### Comparing Strings

- [CFStringCompare](<cfstringcompare(______).md>) — Compares one string with another string.
- [CFStringCompareWithOptions](<cfstringcomparewithoptions(________).md>) — Compares a range of the characters in one string with that of another string.
- [CFStringCompareWithOptionsAndLocale](<cfstringcomparewithoptionsandlocale(__________).md>) — Compares a range of the characters in one string with another string using a given locale.
- [CFStringHasSuffix](<cfstringhassuffix(____).md>) — Determines if a string ends with a specified sequence of characters.
