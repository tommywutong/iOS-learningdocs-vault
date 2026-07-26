---
title: CFDictionaryCopyDescriptionCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionarycopydescriptioncallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarycopydescriptioncallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarycopydescriptioncallback.json'
content_hash: 'sha256:53c72f384b489436'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryCopyDescriptionCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to get a description of a value or key in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFDictionaryCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

## Parameters

- `value` — The value to be described.

## Return Value

A text description of `value`.

## Discussion

This callback is passed to [CFDictionaryCreate](<cfdictionarycreate(____________).md>) in a [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) structure or [CFDictionaryValueCallBacks](cfdictionaryvaluecallbacks.md). This callback is used by the [CFCopyDescription](<cfcopydescription(__).md>) function.

## See Also

### Callbacks

- [CFDictionaryApplierFunction](cfdictionaryapplierfunction.md) — Prototype of a callback function that may be applied to every key-value pair in a dictionary.
- [CFDictionaryEqualCallBack](cfdictionaryequalcallback.md) — Prototype of a callback function used to determine if two values or keys in a dictionary are equal.
- [CFDictionaryHashCallBack](cfdictionaryhashcallback.md) — Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.
- [CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md) — Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.
- [CFDictionaryRetainCallBack](cfdictionaryretaincallback.md) — Prototype of a callback function used to retain a value or key being added to a dictionary.
