---
title: CFBinaryHeapApplierFunction
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbinaryheapapplierfunction
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapapplierfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapapplierfunction.json'
content_hash: 'sha256:9df57d987383d1ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBinaryHeapApplierFunction

<sub>Type Alias</sub>

Callback function used to apply a function to all members of a binary heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFBinaryHeapApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `val` — The current value from the binary heap.

- `context` — The program-defined context parameter given to the [CFBinaryHeapApplyFunction](<cfbinaryheapapplyfunction(______).md>) function.

## See Also

### Callbacks

- [compare](cfbinaryheapcallbacks/compare.md) — The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [copyDescription](cfbinaryheapcallbacks/copydescription.md) — Callback function used to get a description of a value in a binary heap.
- [release](cfbinaryheapcallbacks/release.md) — Callback function used to release a value before it is removed from a binary heap.
- [retain](cfbinaryheapcallbacks/retain.md) — Callback function used to retain a value being added to a binary heap.
- [version](cfbinaryheapcallbacks/version.md) — The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.
