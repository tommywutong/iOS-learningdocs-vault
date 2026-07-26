---
title: MTLHeapType.automatic
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheaptype/automatic
source_url: 'https://developer.apple.com/documentation/metal/mtlheaptype/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheaptype/automatic.json'
content_hash: 'sha256:2fda18ed60280266'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeapType](../mtlheaptype.md)

# MTLHeapType.automatic

<sub>Case</sub>

A heap that automatically places new resource allocations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case automatic
```

## Discussion

In an automatic heap, Metal automatically determines the locations of resources allocated by the heap, with a layout specific to the GPU. Automatic heaps may perform better than manually placing resources in the heap ([MTLHeapTypePlacement](placement.md)).

Use automatic heaps when the heap primarily contains temporary resources that you write to often.

## See Also

### Specifying the heap type

- [MTLHeapTypePlacement](placement.md) — The app controls placement of resources on the heap.
- [MTLHeapTypeSparse](sparse.md) — The heap contains sparse texture tiles.
