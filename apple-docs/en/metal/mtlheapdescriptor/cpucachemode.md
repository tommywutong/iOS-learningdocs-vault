---
title: cpuCacheMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheapdescriptor/cpucachemode
source_url: 'https://developer.apple.com/documentation/metal/mtlheapdescriptor/cpucachemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheapdescriptor/cpucachemode.json'
content_hash: 'sha256:b4f2b3c4312e225e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeapDescriptor](../mtlheapdescriptor.md)

# cpuCacheMode

<sub>Instance Property</sub>

The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var cpuCacheMode: MTLCPUCacheMode { get set }
```

## Discussion

This property’s default value is [MTLCPUCacheModeDefaultCache](../mtlcpucachemode/defaultcache.md).

The resources you allocate from a heap inherit that heap’s CPU cache mode.

## See Also

### Configuring a heap

- [type](type.md) — The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [storageMode](storagemode.md) — The storage mode for the heaps you create with this descriptor.
- [hazardTrackingMode](hazardtrackingmode.md) — The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [resourceOptions](resourceoptions.md) — The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [size](size.md) — The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [sparsePageSize](sparsepagesize.md) — The page size for any resources you allocate from the heaps you create with this descriptor.
