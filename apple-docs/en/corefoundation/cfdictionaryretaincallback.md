---
title: CFDictionaryRetainCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionaryretaincallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryretaincallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryretaincallback.json'
content_hash: 'sha256:9c1243abcde7e9ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryRetainCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to retain a value or key being added to a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFDictionaryRetainCallBack = (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?
```

## Parameters

- `allocator` — The dictionary’s allocator.

- `value` — The value being added to the dictionary.

## Return Value

The value or key to store in the dictionary, which is usually the `value` parameter passed to this callback, but may be a different   value if a different value should be stored in the collection.

## Discussion

This callback is passed to [CFDictionaryCreate](<cfdictionarycreate(____________).md>) in a [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) and [CFDictionaryValueCallBacks](cfdictionaryvaluecallbacks.md) structure.

## See Also

### Callbacks

- [CFDictionaryApplierFunction](cfdictionaryapplierfunction.md) — Prototype of a callback function that may be applied to every key-value pair in a dictionary.
- [CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value or key in a dictionary.
- [CFDictionaryEqualCallBack](cfdictionaryequalcallback.md) — Prototype of a callback function used to determine if two values or keys in a dictionary are equal.
- [CFDictionaryHashCallBack](cfdictionaryhashcallback.md) — Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.
- [CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md) — Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.
