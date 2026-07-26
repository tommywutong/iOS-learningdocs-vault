---
title: sparsePageSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheapdescriptor/sparsepagesize
source_url: 'https://developer.apple.com/documentation/metal/mtlheapdescriptor/sparsepagesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheapdescriptor/sparsepagesize.json'
content_hash: 'sha256:6ad8e88a42ce5161'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeapDescriptor](../mtlheapdescriptor.md)

# sparsePageSize

<sub>Instance Property</sub>

The page size for any resources you allocate from the heaps you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sparsePageSize: MTLSparsePageSize { get set }
```

## Discussion

This property’s default value is 16 kilobytes ([MTLSparsePageSize16](../mtlsparsepagesize/size16.md)), which is a smaller page size option that can help reduce your app’s memory usage. However, you can reduce operational overhead for sparse textures with larger page sizes, such as [MTLSparsePageSize64](../mtlsparsepagesize/size64.md) and [MTLSparsePageSize256](../mtlsparsepagesize/size256.md). These operations include blit commands and the configuration of sparse texture mappings (see [Blit passes](../blit-passes.md) and [MTLResourceStateCommandEncoder](../mtlresourcestatecommandencoder.md), respectively).

## See Also

### Configuring a heap

- [type](type.md) — The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [storageMode](storagemode.md) — The storage mode for the heaps you create with this descriptor.
- [cpuCacheMode](cpucachemode.md) — The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [hazardTrackingMode](hazardtrackingmode.md) — The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [resourceOptions](resourceoptions.md) — The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [size](size.md) — The total amount of memory, in bytes, for the heaps you create with this descriptor.
