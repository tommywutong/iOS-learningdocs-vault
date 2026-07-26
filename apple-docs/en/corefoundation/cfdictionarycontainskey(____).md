---
title: 'CFDictionaryContainsKey(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionarycontainskey(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarycontainskey(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarycontainskey%28_%3A_%3A%29.json'
content_hash: 'sha256:221c03a0071688cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryContainsKey(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a given key is in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryContainsKey(_ theDict: CFDictionary!, _ key: UnsafeRawPointer!) -> Bool
```

## Parameters

- `theDict` — The dictionary to examine.

- `key` — The key for which to find matches in `theDict`. The key hash and equal callbacks provided when the dictionary was created, are used to compare. If the hash callback is `NULL`, `key` is treated as a pointer and converted to an integer. If the equal callback is `NULL`, pointer equality (in C, ==) is used. If `key`, or any of the keys in the dictionary, is not understood by the equal callback, the behavior is undefined.

## Return Value

`true` if `key` is in the dictionary, otherwise `false`.

## See Also

### Examining a dictionary

- [CFDictionaryContainsValue](<cfdictionarycontainsvalue(____).md>) — Returns a Boolean value that indicates whether a given value is in a dictionary.
- [CFDictionaryGetCount](<cfdictionarygetcount(__).md>) — Returns the number of key-value pairs in a dictionary.
- [CFDictionaryGetCountOfKey](<cfdictionarygetcountofkey(____).md>) — Returns the number of times a key occurs in a dictionary.
- [CFDictionaryGetCountOfValue](<cfdictionarygetcountofvalue(____).md>) — Counts the number of times a given value occurs in the dictionary.
- [CFDictionaryGetKeysAndValues](<cfdictionarygetkeysandvalues(______).md>) — Fills two buffers with the keys and values from a dictionary.
- [CFDictionaryGetValue](<cfdictionarygetvalue(____).md>) — Returns the value associated with a given key.
- [CFDictionaryGetValueIfPresent](<cfdictionarygetvalueifpresent(______).md>) — Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.
