---
title: 'CFDictionaryGetCount(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionarygetcount(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarygetcount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarygetcount%28_%3A%29.json'
content_hash: 'sha256:357f23d5bc519672'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryGetCount(_:)

<sub>Function</sub>

Returns the number of key-value pairs in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryGetCount(_ theDict: CFDictionary!) -> CFIndex
```

## Parameters

- `theDict` — The dictionary to examine.

## Return Value

The number of number of key-value pairs in `theDict`.

## See Also

### Examining a dictionary

- [CFDictionaryContainsKey](<cfdictionarycontainskey(____).md>) — Returns a Boolean value that indicates whether a given key is in a dictionary.
- [CFDictionaryContainsValue](<cfdictionarycontainsvalue(____).md>) — Returns a Boolean value that indicates whether a given value is in a dictionary.
- [CFDictionaryGetCountOfKey](<cfdictionarygetcountofkey(____).md>) — Returns the number of times a key occurs in a dictionary.
- [CFDictionaryGetCountOfValue](<cfdictionarygetcountofvalue(____).md>) — Counts the number of times a given value occurs in the dictionary.
- [CFDictionaryGetKeysAndValues](<cfdictionarygetkeysandvalues(______).md>) — Fills two buffers with the keys and values from a dictionary.
- [CFDictionaryGetValue](<cfdictionarygetvalue(____).md>) — Returns the value associated with a given key.
- [CFDictionaryGetValueIfPresent](<cfdictionarygetvalueifpresent(______).md>) — Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.
