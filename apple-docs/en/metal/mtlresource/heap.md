---
title: heap
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresource/heap
source_url: 'https://developer.apple.com/documentation/metal/mtlresource/heap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresource/heap.json'
content_hash: 'sha256:f5b059d942a29ae2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResource](../mtlresource.md)

# heap

<sub>Instance Property</sub>

The heap on which the resource is allocated, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var heap: (any MTLHeap)? { get }
```

## Discussion

This value is `nil` if the resource isn’t allocated on a heap.

## See Also

### Managing heap resources

- [heapOffset](heapoffset.md) — The distance, in bytes, from the beginning of the heap to the first byte of the resource, if you allocated the resource on a heap.
- [- makeAliasable](<makealiasable().md>) — Allows future heap resource allocations to alias against the resource’s memory, reusing it.
- [- isAliasable](<isaliasable().md>) — A Boolean value that indicates whether future heap resource allocations may alias against the resource’s memory.
