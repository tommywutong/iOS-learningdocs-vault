---
title: resourceOptions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheapdescriptor/resourceoptions
source_url: 'https://developer.apple.com/documentation/metal/mtlheapdescriptor/resourceoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheapdescriptor/resourceoptions.json'
content_hash: 'sha256:4459232bba0b5248'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeapDescriptor](../mtlheapdescriptor.md)

# resourceOptions

<sub>Instance Property</sub>

The combined behavior for any resources you allocate from the heaps you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var resourceOptions: MTLResourceOptions { get set }
```

## Discussion

This property aggregates the values of [storageMode](storagemode.md), [cpuCacheMode](cpucachemode.md), and [hazardTrackingMode](hazardtrackingmode.md). Any modifications you make to this property affect the other properties, and vice versa.

## See Also

### Configuring a heap

- [type](type.md) — The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [storageMode](storagemode.md) — The storage mode for the heaps you create with this descriptor.
- [cpuCacheMode](cpucachemode.md) — The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [hazardTrackingMode](hazardtrackingmode.md) — The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [size](size.md) — The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [sparsePageSize](sparsepagesize.md) — The page size for any resources you allocate from the heaps you create with this descriptor.
