---
title: MTLHeapType.placement
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheaptype/placement
source_url: 'https://developer.apple.com/documentation/metal/mtlheaptype/placement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheaptype/placement.json'
content_hash: 'sha256:e986d03bbcdb8bd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeapType](../mtlheaptype.md)

# MTLHeapType.placement

<sub>Case</sub>

The app controls placement of resources on the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case placement
```

## Discussion

Use placement heaps when you need direct control over memory use and heap fragmentation. Typically, you use placement heaps for resources you keep for long time periods and rarely change.

## See Also

### Specifying the heap type

- [MTLHeapTypeAutomatic](automatic.md) — A heap that automatically places new resource allocations.
- [MTLHeapTypeSparse](sparse.md) — The heap contains sparse texture tiles.
