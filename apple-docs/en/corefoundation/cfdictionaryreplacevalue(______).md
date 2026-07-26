---
title: 'CFDictionaryReplaceValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionaryreplacevalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryreplacevalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryreplacevalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c2e23a8038ea5693'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryReplaceValue(_:_:_:)

<sub>Function</sub>

Replaces a value corresponding to a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryReplaceValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theDict` — The dictionary to modify.

- `key` — The key of the value to replace in `theDict`. If a key which matches `key` is present in the dictionary, the value is changed to the `value`, otherwise this function does nothing (“replace if present”).

- `value` — The new value for `key`. The `value` object is retained by `theDict` using the retain callback provided when `theDict` was created, and the old value is released. `value` must be of the type expected by the retain and release callbacks.

## See Also

### Modifying a Dictionary

- [CFDictionaryAddValue](<cfdictionaryaddvalue(______).md>) — Adds a key-value pair to a dictionary if the specified key is not already present.
- [CFDictionaryRemoveAllValues](<cfdictionaryremoveallvalues(__).md>) — Removes all the key-value pairs from a dictionary, making it empty.
- [CFDictionaryRemoveValue](<cfdictionaryremovevalue(____).md>) — Removes a key-value pair.
- [CFDictionarySetValue](<cfdictionarysetvalue(______).md>) — Sets the value corresponding to a given key.
