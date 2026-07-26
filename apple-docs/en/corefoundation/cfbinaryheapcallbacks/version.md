---
title: version
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbinaryheapcallbacks/version
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapcallbacks/version.json'
content_hash: 'sha256:e375b0f056bce03a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFBinaryHeapCallBacks](../cfbinaryheapcallbacks.md)

# version

<sub>Instance Property</sub>

The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var version: CFIndex
```

## See Also

### Callbacks

- [CFBinaryHeapApplierFunction](../cfbinaryheapapplierfunction.md) — Callback function used to apply a function to all members of a binary heap.
- [compare](compare.md) — The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [copyDescription](copydescription.md) — Callback function used to get a description of a value in a binary heap.
- [release](release.md) — Callback function used to release a value before it is removed from a binary heap.
- [retain](retain.md) — Callback function used to retain a value being added to a binary heap.
