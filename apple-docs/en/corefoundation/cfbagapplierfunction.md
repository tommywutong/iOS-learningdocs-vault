---
title: CFBagApplierFunction
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbagapplierfunction
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagapplierfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagapplierfunction.json'
content_hash: 'sha256:92470b02c3f072df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagApplierFunction

<sub>Type Alias</sub>

Prototype of a callback function that may be applied to every value in a bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFBagApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `value` — The current value in a bag.

- `context` — The program-defined context parameter given to the apply   function.

## Discussion

This callback is passed to the [CFBagApplyFunction](<cfbagapplyfunction(______).md>) function which iterates over the values in a bag and applies the behavior defined in the applier function to each value in a bag.

## See Also

### Callbacks

- [CFBagCopyDescriptionCallBack](cfbagcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a bag.
- [CFBagEqualCallBack](cfbagequalcallback.md) — Prototype of a callback function used to determine if two values in a bag are equal.
- [CFBagHashCallBack](cfbaghashcallback.md) — Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFBagReleaseCallBack](cfbagreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a bag.
- [CFBagRetainCallBack](cfbagretaincallback.md) — Prototype of a callback function used to retain a value being added to a bag.
