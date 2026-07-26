---
title: hazardTrackingMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheapdescriptor/hazardtrackingmode
source_url: 'https://developer.apple.com/documentation/metal/mtlheapdescriptor/hazardtrackingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheapdescriptor/hazardtrackingmode.json'
content_hash: 'sha256:8657526f769104b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeapDescriptor](../mtlheapdescriptor.md)

# hazardTrackingMode

<sub>Instance Property</sub>

The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var hazardTrackingMode: MTLHazardTrackingMode { get set }
```

## Discussion

This property’s default value is [MTLHazardTrackingModeDefault](../mtlhazardtrackingmode/default.md), which is equivalent to [MTLHazardTrackingModeUntracked](../mtlhazardtrackingmode/untracked.md) for a heap.

The resources you allocate from a heap inherit that heap’s hazard tracking mode.

## See Also

### Configuring a heap

- [type](type.md) — The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [storageMode](storagemode.md) — The storage mode for the heaps you create with this descriptor.
- [cpuCacheMode](cpucachemode.md) — The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [resourceOptions](resourceoptions.md) — The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [size](size.md) — The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [sparsePageSize](sparsepagesize.md) — The page size for any resources you allocate from the heaps you create with this descriptor.
