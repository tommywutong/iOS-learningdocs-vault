---
title: 'CFDictionaryGetCountOfValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionarygetcountofvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarygetcountofvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarygetcountofvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:1576a695651187ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryGetCountOfValue(_:_:)

<sub>Function</sub>

Counts the number of times a given value occurs in the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryGetCountOfValue(_ theDict: CFDictionary!, _ value: UnsafeRawPointer!) -> CFIndex
```

## Parameters

- `theDict` — The dictionary to examine.

- `value` — The value for which to find matches in `theDict`. The value equal callback provided when the dictionary was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in the dictionary, is not understood by the equal callback, the behavior is undefined.

## Return Value

The number of times the `value` occurs in `theDict`.

## See Also

### Examining a dictionary

- [CFDictionaryContainsKey](<cfdictionarycontainskey(____).md>) — Returns a Boolean value that indicates whether a given key is in a dictionary.
- [CFDictionaryContainsValue](<cfdictionarycontainsvalue(____).md>) — Returns a Boolean value that indicates whether a given value is in a dictionary.
- [CFDictionaryGetCount](<cfdictionarygetcount(__).md>) — Returns the number of key-value pairs in a dictionary.
- [CFDictionaryGetCountOfKey](<cfdictionarygetcountofkey(____).md>) — Returns the number of times a key occurs in a dictionary.
- [CFDictionaryGetKeysAndValues](<cfdictionarygetkeysandvalues(______).md>) — Fills two buffers with the keys and values from a dictionary.
- [CFDictionaryGetValue](<cfdictionarygetvalue(____).md>) — Returns the value associated with a given key.
- [CFDictionaryGetValueIfPresent](<cfdictionarygetvalueifpresent(______).md>) — Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.
