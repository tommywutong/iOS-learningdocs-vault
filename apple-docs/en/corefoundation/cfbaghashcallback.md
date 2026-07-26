---
title: CFBagHashCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbaghashcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbaghashcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbaghashcallback.json'
content_hash: 'sha256:872502e8cc07cf81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagHashCallBack

<sub>Type Alias</sub>

Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFBagHashCallBack = (UnsafeRawPointer?) -> CFHashCode
```

## Parameters

- `value` — The value used to compute the hash code.

## Return Value

An integer that can be used as a table address in a hash table structure.

## Discussion

This callback is passed to [CFBagCreate](<cfbagcreate(________).md>) in a [CFBagCallBacks](cfbagcallbacks.md) structure.

## See Also

### Callbacks

- [CFBagApplierFunction](cfbagapplierfunction.md) — Prototype of a callback function that may be applied to every value in a bag.
- [CFBagCopyDescriptionCallBack](cfbagcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a bag.
- [CFBagEqualCallBack](cfbagequalcallback.md) — Prototype of a callback function used to determine if two values in a bag are equal.
- [CFBagReleaseCallBack](cfbagreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a bag.
- [CFBagRetainCallBack](cfbagretaincallback.md) — Prototype of a callback function used to retain a value being added to a bag.
