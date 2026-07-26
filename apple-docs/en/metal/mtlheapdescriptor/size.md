---
title: size
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheapdescriptor/size
source_url: 'https://developer.apple.com/documentation/metal/mtlheapdescriptor/size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheapdescriptor/size.json'
content_hash: 'sha256:1a24c3bf983c23bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeapDescriptor](../mtlheapdescriptor.md)

# size

<sub>Instance Property</sub>

The total amount of memory, in bytes, for the heaps you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var size: Int { get set }
```

## Discussion

You can use various [MTLDevice](../mtldevice.md) methods to help you estimate an appropriate heap size, including the following:

- [- heapBufferSizeAndAlignWithLength:options:](<../mtldevice/heapbuffersizeandalign(length_options_).md>)
- [- heapTextureSizeAndAlignWithDescriptor:](<../mtldevice/heaptexturesizeandalign(descriptor_).md>)
- [- heapAccelerationStructureSizeAndAlignWithSize:](<../mtldevice/heapaccelerationstructuresizeandalign(size_).md>)
- [- heapAccelerationStructureSizeAndAlignWithDescriptor:](<../mtldevice/heapaccelerationstructuresizeandalign(descriptor_).md>)

> [!note] Note
> Metal may round a heap’s size to a page boundary.

This property’s default value is `0`.

## See Also

### Configuring a heap

- [type](type.md) — The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [storageMode](storagemode.md) — The storage mode for the heaps you create with this descriptor.
- [cpuCacheMode](cpucachemode.md) — The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [hazardTrackingMode](hazardtrackingmode.md) — The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [resourceOptions](resourceoptions.md) — The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [sparsePageSize](sparsepagesize.md) — The page size for any resources you allocate from the heaps you create with this descriptor.
