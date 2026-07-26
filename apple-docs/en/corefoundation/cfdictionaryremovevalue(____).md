---
title: 'CFDictionaryRemoveValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionaryremovevalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryremovevalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryremovevalue%28_%3A_%3A%29.json'
content_hash: 'sha256:83a826994e2afa5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryRemoveValue(_:_:)

<sub>Function</sub>

Removes a key-value pair.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryRemoveValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!)
```

## Parameters

- `theDict` — The dictionary to modify.

- `key` — The key of the value to remove from `theDict`. If a key which matches `key` is present in `theDict`, the key-value pair is removed from the dictionary, otherwise this function does nothing (“remove if present”).

## See Also

### Modifying a Dictionary

- [CFDictionaryAddValue](<cfdictionaryaddvalue(______).md>) — Adds a key-value pair to a dictionary if the specified key is not already present.
- [CFDictionaryRemoveAllValues](<cfdictionaryremoveallvalues(__).md>) — Removes all the key-value pairs from a dictionary, making it empty.
- [CFDictionaryReplaceValue](<cfdictionaryreplacevalue(______).md>) — Replaces a value corresponding to a given key.
- [CFDictionarySetValue](<cfdictionarysetvalue(______).md>) — Sets the value corresponding to a given key.
