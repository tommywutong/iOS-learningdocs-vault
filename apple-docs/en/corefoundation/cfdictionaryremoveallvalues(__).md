---
title: 'CFDictionaryRemoveAllValues(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionaryremoveallvalues(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryremoveallvalues(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryremoveallvalues%28_%3A%29.json'
content_hash: 'sha256:8d2e43822f41ca28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryRemoveAllValues(_:)

<sub>Function</sub>

Removes all the key-value pairs from a dictionary, making it empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryRemoveAllValues(_ theDict: CFMutableDictionary!)
```

## Parameters

- `theDict` — The dictionary to modify.

## See Also

### Modifying a Dictionary

- [CFDictionaryAddValue](<cfdictionaryaddvalue(______).md>) — Adds a key-value pair to a dictionary if the specified key is not already present.
- [CFDictionaryRemoveValue](<cfdictionaryremovevalue(____).md>) — Removes a key-value pair.
- [CFDictionaryReplaceValue](<cfdictionaryreplacevalue(______).md>) — Replaces a value corresponding to a given key.
- [CFDictionarySetValue](<cfdictionarysetvalue(______).md>) — Sets the value corresponding to a given key.
