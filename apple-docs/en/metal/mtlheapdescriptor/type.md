---
title: type
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheapdescriptor/type
source_url: 'https://developer.apple.com/documentation/metal/mtlheapdescriptor/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheapdescriptor/type.json'
content_hash: 'sha256:3a3aca70b279262a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeapDescriptor](../mtlheapdescriptor.md)

# type

<sub>Instance Property</sub>

The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var type: MTLHeapType { get set }
```

## Discussion

This property’s default value is [MTLHeapTypeAutomatic](../mtlheaptype/automatic.md).

## See Also

### Configuring a heap

- [storageMode](storagemode.md) — The storage mode for the heaps you create with this descriptor.
- [cpuCacheMode](cpucachemode.md) — The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [hazardTrackingMode](hazardtrackingmode.md) — The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [resourceOptions](resourceoptions.md) — The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [size](size.md) — The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [sparsePageSize](sparsepagesize.md) — The page size for any resources you allocate from the heaps you create with this descriptor.
