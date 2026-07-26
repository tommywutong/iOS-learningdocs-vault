---
title: CFDictionaryApplierFunction
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionaryapplierfunction
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryapplierfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryapplierfunction.json'
content_hash: 'sha256:f5a292d9e716673f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryApplierFunction

<sub>Type Alias</sub>

Prototype of a callback function that may be applied to every key-value pair in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFDictionaryApplierFunction = (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `key` — The key associated with the current key-value pair.

- `value` — The value associated with the current key-value pair.

- `context` — The program-defined context parameter given to the apply   function.

## Discussion

This callback is passed to the [CFDictionaryApplyFunction](<cfdictionaryapplyfunction(______).md>) function which iterates over the key-value pairs in a dictionary and applies the behavior defined in the applier function to each key-value pair in a dictionary.

## See Also

### Callbacks

- [CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value or key in a dictionary.
- [CFDictionaryEqualCallBack](cfdictionaryequalcallback.md) — Prototype of a callback function used to determine if two values or keys in a dictionary are equal.
- [CFDictionaryHashCallBack](cfdictionaryhashcallback.md) — Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.
- [CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md) — Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.
- [CFDictionaryRetainCallBack](cfdictionaryretaincallback.md) — Prototype of a callback function used to retain a value or key being added to a dictionary.
