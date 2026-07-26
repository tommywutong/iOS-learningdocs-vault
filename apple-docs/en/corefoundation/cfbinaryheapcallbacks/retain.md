---
title: retain
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbinaryheapcallbacks/retain
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapcallbacks/retain.json'
content_hash: 'sha256:f4c76bd3bc3fe342'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFBinaryHeapCallBacks](../cfbinaryheapcallbacks.md)

# retain

<sub>Instance Property</sub>

Callback function used to retain a value being added to a binary heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!
```

## Parameters

- `allocator` — The binary heap’s allocator.

- `ptr` — The value to retain.

## Return Value

The value to store in the binary heap, which is usually the `ptr` parameter passed to this callback, but may be a different   value if a different value should be stored in the binary heap.

## Discussion

The callback used to add a retain for the binary heap on values as they are put into the binary heap. This callback returns the value to use as the value in the binary heap, which is usually the value parameter passed to this callback, but may be a different value if a different value should be added to the binary heap. If this field is `NULL`, the binary heap does nothing to retain a value being added.

## See Also

### Callbacks

- [CFBinaryHeapApplierFunction](../cfbinaryheapapplierfunction.md) — Callback function used to apply a function to all members of a binary heap.
- [compare](compare.md) — The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [copyDescription](copydescription.md) — Callback function used to get a description of a value in a binary heap.
- [release](release.md) — Callback function used to release a value before it is removed from a binary heap.
- [version](version.md) — The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.
