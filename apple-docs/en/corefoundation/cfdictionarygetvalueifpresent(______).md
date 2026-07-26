---
title: 'CFDictionaryGetValueIfPresent(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionarygetvalueifpresent(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarygetvalueifpresent(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarygetvalueifpresent%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a95fa65445c35a3c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryGetValueIfPresent(_:_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryGetValueIfPresent(_ theDict: CFDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool
```

## Parameters

- `theDict` — The dictionary to examine.

- `key` — The key for which to find a match in `theDict`. The key hash and equal callbacks provided when the dictionary was created are used to compare. If the hash callback was `NULL`, `key` is treated as a pointer and converted to an integer. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `key`, or any of the keys in `theDict`, is not understood by the equal callback, the behavior is undefined.

- `value` — A pointer to memory which, on return, is filled with the pointer-sized value if a matching key is found. If no key match is found, the contents of the storage pointed to by this parameter are undefined. This value may be `NULL`, in which case the value from the dictionary is not returned (but the return value of this function still indicates whether or not the key-value pair was present). If the value is a Core Foundation object, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Return Value

`true` if a matching key was found, otherwise `false`.

## See Also

### Examining a dictionary

- [CFDictionaryContainsKey](<cfdictionarycontainskey(____).md>) — Returns a Boolean value that indicates whether a given key is in a dictionary.
- [CFDictionaryContainsValue](<cfdictionarycontainsvalue(____).md>) — Returns a Boolean value that indicates whether a given value is in a dictionary.
- [CFDictionaryGetCount](<cfdictionarygetcount(__).md>) — Returns the number of key-value pairs in a dictionary.
- [CFDictionaryGetCountOfKey](<cfdictionarygetcountofkey(____).md>) — Returns the number of times a key occurs in a dictionary.
- [CFDictionaryGetCountOfValue](<cfdictionarygetcountofvalue(____).md>) — Counts the number of times a given value occurs in the dictionary.
- [CFDictionaryGetKeysAndValues](<cfdictionarygetkeysandvalues(______).md>) — Fills two buffers with the keys and values from a dictionary.
- [CFDictionaryGetValue](<cfdictionarygetvalue(____).md>) — Returns the value associated with a given key.
