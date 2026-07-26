---
title: 'CFDictionaryAddValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionaryaddvalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryaddvalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryaddvalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:508cd254a95a792a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryAddValue(_:_:_:)

<sub>Function</sub>

Adds a key-value pair to a dictionary if the specified key is not already present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryAddValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theDict` — The dictionary to modify. If the dictionary is a fixed-capacity dictionary and it is full before this operation, the behavior is undefined.

- `key` — The key for the value to add to the dictionary—a CFType object or a pointer value. The `key` is retained by the dictionary using the retain callback provided when the dictionary was created, so must be of the type expected by the callback. If a key which matches `key` is already present in the dictionary, this function does nothing (“add if absent”).

- `value` — A CFType object or a pointer value to add to the dictionary. The `value` is retained by the dictionary using the retain callback provided when the dictionary was created, so must be of the type expected by the callback.

## See Also

### Modifying a Dictionary

- [CFDictionaryRemoveAllValues](<cfdictionaryremoveallvalues(__).md>) — Removes all the key-value pairs from a dictionary, making it empty.
- [CFDictionaryRemoveValue](<cfdictionaryremovevalue(____).md>) — Removes a key-value pair.
- [CFDictionaryReplaceValue](<cfdictionaryreplacevalue(______).md>) — Replaces a value corresponding to a given key.
- [CFDictionarySetValue](<cfdictionarysetvalue(______).md>) — Sets the value corresponding to a given key.
