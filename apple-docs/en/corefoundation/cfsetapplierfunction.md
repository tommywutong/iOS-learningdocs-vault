---
title: CFSetApplierFunction
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsetapplierfunction
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetapplierfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetapplierfunction.json'
content_hash: 'sha256:37486d9a5e0752a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetApplierFunction

<sub>Type Alias</sub>

Prototype of a callback function that may be applied to every value in a set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFSetApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `value` — The current value in a set.

- `context` — The program-defined context parameter given to the apply function.

## Discussion

This callback is passed to the [CFSetApplyFunction](<cfsetapplyfunction(______).md>) function which iterates over the values in a set and applies the behavior defined in the applier function to each value in a set.

## See Also

### Callbacks

- [CFSetCopyDescriptionCallBack](cfsetcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a set.
- [CFSetEqualCallBack](cfsetequalcallback.md) — Prototype of a callback function used to determine if two values in a set are equal.
- [CFSetHashCallBack](cfsethashcallback.md) — Prototype of a callback function called to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFSetReleaseCallBack](cfsetreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a set.
- [CFSetRetainCallBack](cfsetretaincallback.md) — Prototype of a callback function used to retain a value being added to a set.
