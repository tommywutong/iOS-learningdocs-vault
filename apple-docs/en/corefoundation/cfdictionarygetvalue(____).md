---
title: 'CFDictionaryGetValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionarygetvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarygetvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarygetvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:8c33a572bd5772a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryGetValue(_:_:)

<sub>Function</sub>

Returns the value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryGetValue(_ theDict: CFDictionary!, _ key: UnsafeRawPointer!) -> UnsafeRawPointer!
```

## Parameters

- `theDict` — The dictionary to examine.

- `key` — The key for which to find a match in `theDict`. The key hash and equal callbacks provided when the dictionary was created are used to compare. If the hash callback was `NULL`, the key is treated as a pointer and converted to an integer. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `key`, or any of the keys in `theDict`, is not understood by the equal callback, the behavior is undefined.

## Return Value

The value associated with `key` in `theDict`, or `NULL` if no key-value pair matching `key` exists. Since `NULL` is also a valid value in some dictionaries, use [CFDictionaryGetValueIfPresent](<cfdictionarygetvalueifpresent(______).md>) to distinguish between a value that is not found, and a `NULL` value. If the value is a Core Foundation object, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining a dictionary

- [CFDictionaryContainsKey](<cfdictionarycontainskey(____).md>) — Returns a Boolean value that indicates whether a given key is in a dictionary.
- [CFDictionaryContainsValue](<cfdictionarycontainsvalue(____).md>) — Returns a Boolean value that indicates whether a given value is in a dictionary.
- [CFDictionaryGetCount](<cfdictionarygetcount(__).md>) — Returns the number of key-value pairs in a dictionary.
- [CFDictionaryGetCountOfKey](<cfdictionarygetcountofkey(____).md>) — Returns the number of times a key occurs in a dictionary.
- [CFDictionaryGetCountOfValue](<cfdictionarygetcountofvalue(____).md>) — Counts the number of times a given value occurs in the dictionary.
- [CFDictionaryGetKeysAndValues](<cfdictionarygetkeysandvalues(______).md>) — Fills two buffers with the keys and values from a dictionary.
- [CFDictionaryGetValueIfPresent](<cfdictionarygetvalueifpresent(______).md>) — Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.
