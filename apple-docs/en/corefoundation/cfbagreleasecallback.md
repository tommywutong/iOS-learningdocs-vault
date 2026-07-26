---
title: CFBagReleaseCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbagreleasecallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagreleasecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagreleasecallback.json'
content_hash: 'sha256:c8cb61e2ef043f8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagReleaseCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to release a value before it’s removed from a bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFBagReleaseCallBack = (CFAllocator?, UnsafeRawPointer?) -> Void
```

## Parameters

- `allocator` — The bag’s allocator.

- `value` — The value being removed from the bag.

## Discussion

This callback is passed to [CFBagCreate](<cfbagcreate(________).md>) in a [CFBagCallBacks](cfbagcallbacks.md) structure.

## See Also

### Callbacks

- [CFBagApplierFunction](cfbagapplierfunction.md) — Prototype of a callback function that may be applied to every value in a bag.
- [CFBagCopyDescriptionCallBack](cfbagcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a bag.
- [CFBagEqualCallBack](cfbagequalcallback.md) — Prototype of a callback function used to determine if two values in a bag are equal.
- [CFBagHashCallBack](cfbaghashcallback.md) — Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFBagRetainCallBack](cfbagretaincallback.md) — Prototype of a callback function used to retain a value being added to a bag.
