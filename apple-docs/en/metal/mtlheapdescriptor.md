---
title: MTLHeapDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheapdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlheapdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheapdescriptor.json'
content_hash: 'sha256:990f7bf660729200'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLHeapDescriptor

<sub>Class</sub>

A configuration that customizes the behavior for a Metal memory heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLHeapDescriptor
```

## Overview

Create an [MTLHeap](mtlheap.md) by configuring an [MTLHeapDescriptor](mtlheapdescriptor.md) instance’s properties and passing it to the [- newHeapWithDescriptor:](<mtldevice/makeheap(descriptor_).md>) method of an [MTLDevice](mtldevice.md).

Each new heap inherits the descriptor’s configuration as you create it, which means you can modify and reuse a descriptor to create other heaps.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring a heap

- [type](mtlheapdescriptor/type.md) — The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [storageMode](mtlheapdescriptor/storagemode.md) — The storage mode for the heaps you create with this descriptor.
- [cpuCacheMode](mtlheapdescriptor/cpucachemode.md) — The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [hazardTrackingMode](mtlheapdescriptor/hazardtrackingmode.md) — The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [resourceOptions](mtlheapdescriptor/resourceoptions.md) — The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [size](mtlheapdescriptor/size.md) — The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [sparsePageSize](mtlheapdescriptor/sparsepagesize.md) — The page size for any resources you allocate from the heaps you create with this descriptor.

### Instance Properties

- [maxCompatiblePlacementSparsePageSize](mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) — Specifies the largest sparse page size that the Metal heap supports.

## See Also

### Resource memory allocation and management

- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md) — Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md) — Use events to synchronize access to resources allocated on a heap.
- [Implementing a multistage image filter using heaps and fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md) — Use fences to synchronize access to resources allocated on a heap.
- [MTLHeap](mtlheap.md) — A memory pool from which you can suballocate resources.
- [MTLHeapType](mtlheaptype.md) — The options you use to choose the heap type.
- [MTLSizeAndAlign](mtlsizeandalign.md) — The size and alignment of a resource, in bytes.
