---
title: CFDictionaryHashCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionaryhashcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryhashcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryhashcallback.json'
content_hash: 'sha256:42d240b9fef83b27'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryHashCallBack

<sub>Type Alias</sub>

Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFDictionaryHashCallBack = (UnsafeRawPointer?) -> CFHashCode
```

## Parameters

- `value` — The value used to compute the hash code.

## Return Value

An integer that can be used as a table address in a hash table structure.

## Discussion

This callback is passed to [CFDictionaryCreate](<cfdictionarycreate(____________).md>) in a [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) structure.

## See Also

### Callbacks

- [CFDictionaryApplierFunction](cfdictionaryapplierfunction.md) — Prototype of a callback function that may be applied to every key-value pair in a dictionary.
- [CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value or key in a dictionary.
- [CFDictionaryEqualCallBack](cfdictionaryequalcallback.md) — Prototype of a callback function used to determine if two values or keys in a dictionary are equal.
- [CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md) — Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.
- [CFDictionaryRetainCallBack](cfdictionaryretaincallback.md) — Prototype of a callback function used to retain a value or key being added to a dictionary.
