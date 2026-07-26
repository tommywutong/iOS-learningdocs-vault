---
title: release
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbinaryheapcallbacks/release
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapcallbacks/release.json'
content_hash: 'sha256:6d20dcc7b419cd45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFBinaryHeapCallBacks](../cfbinaryheapcallbacks.md)

# release

<sub>Instance Property</sub>

Callback function used to release a value before it is removed from a binary heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var release: ((CFAllocator?, UnsafeRawPointer?) -> Void)!
```

## Parameters

- `allocator` — The binary heap’s allocator.

- `ptr` — The value to release.

## Discussion

The callback used to remove a retain previously added for the binary heap from values as they are removed from the binary heap. If this field is `NULL`, the binary heap does nothing to release a value being removed.

## See Also

### Callbacks

- [CFBinaryHeapApplierFunction](../cfbinaryheapapplierfunction.md) — Callback function used to apply a function to all members of a binary heap.
- [compare](compare.md) — The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [copyDescription](copydescription.md) — Callback function used to get a description of a value in a binary heap.
- [retain](retain.md) — Callback function used to retain a value being added to a binary heap.
- [version](version.md) — The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.
