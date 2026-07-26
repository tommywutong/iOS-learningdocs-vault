---
title: 'CFDictionaryGetKeysAndValues(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionarygetkeysandvalues(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarygetkeysandvalues(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarygetkeysandvalues%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:928227c563a4f732'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryGetKeysAndValues(_:_:_:)

<sub>Function</sub>

Fills two buffers with the keys and values from a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryGetKeysAndValues(_ theDict: CFDictionary!, _ keys: UnsafeMutablePointer<UnsafeRawPointer?>!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!)
```

## Parameters

- `theDict` — The dictionary to examine.

- `keys` — A C array of pointer-sized values that, on return, is filled with keys from the `theDict`. The keys and values C arrays are parallel to each other (that is, the items at the same indices form a key-value pair from the dictionary). This value must be a valid pointer to a C array of the appropriate type and size (that is, a size equal to the count of `theDict`), or `NULL` if the keys are not required. If the keys are Core Foundation objects, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

- `values` — A C array of pointer-sized values that, on return, is filled with values from the `theDict`. The keys and values C arrays are parallel to each other (that is, the items at the same indices form a key-value pair from the dictionary). This value must be a valid pointer to a C array of the appropriate type and size (that is, a size equal to the count of `theDict`), or `NULL` if the values are not required. If the values are Core Foundation objects, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining a dictionary

- [CFDictionaryContainsKey](<cfdictionarycontainskey(____).md>) — Returns a Boolean value that indicates whether a given key is in a dictionary.
- [CFDictionaryContainsValue](<cfdictionarycontainsvalue(____).md>) — Returns a Boolean value that indicates whether a given value is in a dictionary.
- [CFDictionaryGetCount](<cfdictionarygetcount(__).md>) — Returns the number of key-value pairs in a dictionary.
- [CFDictionaryGetCountOfKey](<cfdictionarygetcountofkey(____).md>) — Returns the number of times a key occurs in a dictionary.
- [CFDictionaryGetCountOfValue](<cfdictionarygetcountofvalue(____).md>) — Counts the number of times a given value occurs in the dictionary.
- [CFDictionaryGetValue](<cfdictionarygetvalue(____).md>) — Returns the value associated with a given key.
- [CFDictionaryGetValueIfPresent](<cfdictionarygetvalueifpresent(______).md>) — Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.
