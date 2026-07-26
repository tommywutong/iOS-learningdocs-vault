---
title: 'CFDictionarySetValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionarysetvalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarysetvalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarysetvalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:cd2852edd9adf87f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionarySetValue(_:_:_:)

<sub>Function</sub>

Sets the value corresponding to a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionarySetValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theDict` — The dictionary to modify. If this parameter is a fixed-capacity dictionary and it is full before this operation, and the key does not exist in the dictionary, the behavior is undefined.

- `key` — The key of the value to set in `theDict`. If a key which matches `key` is already present in the dictionary, only the value for the key is changed (“add if absent, replace if present”). If no key matches `key`, the key-value pair is added to the dictionary. If a key-value pair is added, both `key` and `value` are retained by the dictionary, using the retain callback provided when `theDict` was created. `key` must be of the type expected by the key retain callback.

- `value` — The value to add to or replace in `theDict`. `value` is retained using the value retain callback provided when `theDict` was created, and the previous value if any is released. `value` must be of the type expected by the retain and release callbacks.

## See Also

### Modifying a Dictionary

- [CFDictionaryAddValue](<cfdictionaryaddvalue(______).md>) — Adds a key-value pair to a dictionary if the specified key is not already present.
- [CFDictionaryRemoveAllValues](<cfdictionaryremoveallvalues(__).md>) — Removes all the key-value pairs from a dictionary, making it empty.
- [CFDictionaryRemoveValue](<cfdictionaryremovevalue(____).md>) — Removes a key-value pair.
- [CFDictionaryReplaceValue](<cfdictionaryreplacevalue(______).md>) — Replaces a value corresponding to a given key.
