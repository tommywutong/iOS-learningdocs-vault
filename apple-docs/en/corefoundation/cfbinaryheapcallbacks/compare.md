---
title: compare
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbinaryheapcallbacks/compare
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/compare'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapcallbacks/compare.json'
content_hash: 'sha256:94e44803e85e0e46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFBinaryHeapCallBacks](../cfbinaryheapcallbacks.md)

# compare

<sub>Instance Property</sub>

The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!
```

## Parameters

- `ptr1` — First value to compare.

- `ptr2` — Second value to compare.

- `info` — Not used. Should always be `NULL`.

## Return Value

[kCFCompareLessThan](../cfcomparisonresult/comparelessthan.md) if `ptr1` is less than `ptr2`, [kCFCompareEqualTo](../cfcomparisonresult/compareequalto.md) if `ptr1` and `ptr2` are equal, or [kCFCompareGreaterThan](../cfcomparisonresult/comparegreaterthan.md) if `ptr1` is greater than `ptr2`.

## See Also

### Callbacks

- [CFBinaryHeapApplierFunction](../cfbinaryheapapplierfunction.md) — Callback function used to apply a function to all members of a binary heap.
- [copyDescription](copydescription.md) — Callback function used to get a description of a value in a binary heap.
- [release](release.md) — Callback function used to release a value before it is removed from a binary heap.
- [retain](retain.md) — Callback function used to retain a value being added to a binary heap.
- [version](version.md) — The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.
