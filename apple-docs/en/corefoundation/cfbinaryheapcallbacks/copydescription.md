---
title: copyDescription
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbinaryheapcallbacks/copydescription
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/copydescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapcallbacks/copydescription.json'
content_hash: 'sha256:547f95b21b70e375'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFBinaryHeapCallBacks](../cfbinaryheapcallbacks.md)

# copyDescription

<sub>Instance Property</sub>

Callback function used to get a description of a value in a binary heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!
```

## Parameters

- `ptr` — The value to be described.

## Discussion

The callback used to create a descriptive string representation of each value in the binary heap. This is used by the [CFCopyDescription](<../cfcopydescription(__).md>) function. If this field is `NULL`, the binary heap constructs a `CFString` object describing the value based on its pointer value.

## See Also

### Callbacks

- [CFBinaryHeapApplierFunction](../cfbinaryheapapplierfunction.md) — Callback function used to apply a function to all members of a binary heap.
- [compare](compare.md) — The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [release](release.md) — Callback function used to release a value before it is removed from a binary heap.
- [retain](retain.md) — Callback function used to retain a value being added to a binary heap.
- [version](version.md) — The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.
