---
title: 'CFStringHasSuffix(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringhassuffix(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringhassuffix(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringhassuffix%28_%3A_%3A%29.json'
content_hash: 'sha256:67e0bed38beb079b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringHasSuffix(_:_:)

<sub>Function</sub>

Determines if a string ends with a specified sequence of characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringHasSuffix(_ theString: CFString!, _ suffix: CFString!) -> Bool
```

## Parameters

- `theString` — The string to be evaluated.

- `suffix` — The suffix to search for.

## Return Value

`true` if `theString` ends with `suffix`, `false` otherwise.

## See Also

### Comparing Strings

- [CFStringCompare](<cfstringcompare(______).md>) — Compares one string with another string.
- [CFStringCompareWithOptions](<cfstringcomparewithoptions(________).md>) — Compares a range of the characters in one string with that of another string.
- [CFStringCompareWithOptionsAndLocale](<cfstringcomparewithoptionsandlocale(__________).md>) — Compares a range of the characters in one string with another string using a given locale.
- [CFStringHasPrefix](<cfstringhasprefix(____).md>) — Determines if the character data of a string begin with a specified sequence of characters.
