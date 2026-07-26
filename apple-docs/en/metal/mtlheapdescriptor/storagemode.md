---
title: storageMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheapdescriptor/storagemode
source_url: 'https://developer.apple.com/documentation/metal/mtlheapdescriptor/storagemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheapdescriptor/storagemode.json'
content_hash: 'sha256:890eaa8709a784dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeapDescriptor](../mtlheapdescriptor.md)

# storageMode

<sub>Instance Property</sub>

The storage mode for the heaps you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var storageMode: MTLStorageMode { get set }
```

## Discussion

For devices with Apple silicon, you can create a heap with either the [MTLStorageModePrivate](../mtlstoragemode/private.md) or the [MTLStorageModeShared](../mtlstoragemode/shared.md) storage mode. However, you can only create heaps with private storage on macOS devices without Apple silicon.

The resources you allocate from a heap inherit that heap’s storage mode. This property’s default value is [MTLStorageModePrivate](../mtlstoragemode/private.md).

## See Also

### Configuring a heap

- [type](type.md) — The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [cpuCacheMode](cpucachemode.md) — The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [hazardTrackingMode](hazardtrackingmode.md) — The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [resourceOptions](resourceoptions.md) — The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [size](size.md) — The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [sparsePageSize](sparsepagesize.md) — The page size for any resources you allocate from the heaps you create with this descriptor.
