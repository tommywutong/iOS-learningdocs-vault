---
title: heapOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresource/heapoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlresource/heapoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresource/heapoffset.json'
content_hash: 'sha256:dc6300054085427f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResource](../mtlresource.md)

# heapOffset

<sub>Instance Property</sub>

The distance, in bytes, from the beginning of the heap to the first byte of the resource, if you allocated the resource on a heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var heapOffset: Int { get }
```

## Discussion

If the heap is not a placement heap ([MTLHeapTypePlacement](../mtlheaptype/placement.md)), the value is always `0` and should be ignored.

## See Also

### Managing heap resources

- [heap](heap.md) — The heap on which the resource is allocated, if any.
- [- makeAliasable](<makealiasable().md>) — Allows future heap resource allocations to alias against the resource’s memory, reusing it.
- [- isAliasable](<isaliasable().md>) — A Boolean value that indicates whether future heap resource allocations may alias against the resource’s memory.
