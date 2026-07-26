---
title: CFBagRetainCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbagretaincallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagretaincallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagretaincallback.json'
content_hash: 'sha256:e9730408857e999a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagRetainCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to retain a value being added to a bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFBagRetainCallBack = (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?
```

## Parameters

- `allocator` — The bag’s allocator.

- `value` — The value being added to the bag.

## Return Value

The value to store in the bag, which is usually the `value` parameter passed to this callback, but may be a different   value if a different value should be stored in the collection.

## Discussion

This callback is passed to [CFBagCreate](<cfbagcreate(________).md>) in a [CFBagCallBacks](cfbagcallbacks.md) structure.

## See Also

### Callbacks

- [CFBagApplierFunction](cfbagapplierfunction.md) — Prototype of a callback function that may be applied to every value in a bag.
- [CFBagCopyDescriptionCallBack](cfbagcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a bag.
- [CFBagEqualCallBack](cfbagequalcallback.md) — Prototype of a callback function used to determine if two values in a bag are equal.
- [CFBagHashCallBack](cfbaghashcallback.md) — Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFBagReleaseCallBack](cfbagreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a bag.
