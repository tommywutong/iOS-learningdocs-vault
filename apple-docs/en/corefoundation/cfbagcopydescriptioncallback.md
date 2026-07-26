---
title: CFBagCopyDescriptionCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbagcopydescriptioncallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagcopydescriptioncallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagcopydescriptioncallback.json'
content_hash: 'sha256:a43df7253b251038'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagCopyDescriptionCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to get a description of a value in a bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFBagCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

## Parameters

- `value` — The value to be described.

## Return Value

A textual description of `value`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This callback is passed to [CFBagCreate](<cfbagcreate(________).md>) in a [CFBagCallBacks](cfbagcallbacks.md) structure. This callback is used by the [CFCopyDescription](<cfcopydescription(__).md>) function.

## See Also

### Callbacks

- [CFBagApplierFunction](cfbagapplierfunction.md) — Prototype of a callback function that may be applied to every value in a bag.
- [CFBagEqualCallBack](cfbagequalcallback.md) — Prototype of a callback function used to determine if two values in a bag are equal.
- [CFBagHashCallBack](cfbaghashcallback.md) — Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFBagReleaseCallBack](cfbagreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a bag.
- [CFBagRetainCallBack](cfbagretaincallback.md) — Prototype of a callback function used to retain a value being added to a bag.
