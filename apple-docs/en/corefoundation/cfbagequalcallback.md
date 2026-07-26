---
title: CFBagEqualCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbagequalcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagequalcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagequalcallback.json'
content_hash: 'sha256:f7428a12df03d565'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagEqualCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to determine if two values in a bag are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFBagEqualCallBack = (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean
```

## Parameters

- `value1` — A value in the bag.

- `value2` — Another value in the bag.

## Return Value

`true` if `value1` and `value2` are equal, `false` otherwise.

## Discussion

This callback is passed to [CFBagCreate](<cfbagcreate(________).md>) in a [CFBagCallBacks](cfbagcallbacks.md) structure.

## See Also

### Callbacks

- [CFBagApplierFunction](cfbagapplierfunction.md) — Prototype of a callback function that may be applied to every value in a bag.
- [CFBagCopyDescriptionCallBack](cfbagcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a bag.
- [CFBagHashCallBack](cfbaghashcallback.md) — Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFBagReleaseCallBack](cfbagreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a bag.
- [CFBagRetainCallBack](cfbagretaincallback.md) — Prototype of a callback function used to retain a value being added to a bag.
