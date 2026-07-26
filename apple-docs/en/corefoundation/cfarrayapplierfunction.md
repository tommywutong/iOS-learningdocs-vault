---
title: CFArrayApplierFunction
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfarrayapplierfunction
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayapplierfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayapplierfunction.json'
content_hash: 'sha256:1478f533d90a6f1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayApplierFunction

<sub>Type Alias</sub>

Prototype of a callback function that may be applied to every value in an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFArrayApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `value` — The current value in an array.

- `context` — The program-defined context parameter given to the applier   function.

## Discussion

This callback is passed to the [CFArrayApplyFunction](<cfarrayapplyfunction(________).md>) function, which iterates over the values in an array and applies the behavior defined in the applier function to each value in an array.

## See Also

### Callbacks

- [CFArrayCopyDescriptionCallBack](cfarraycopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in an array.
- [CFArrayEqualCallBack](cfarrayequalcallback.md) — Prototype of a callback function used to determine if two values in an array are equal.
- [CFArrayReleaseCallBack](cfarrayreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from an array.
- [CFArrayRetainCallBack](cfarrayretaincallback.md) — Prototype of a callback function used to retain a value being added to an array.
