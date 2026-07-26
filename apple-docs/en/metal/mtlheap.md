---
title: MTLHeap
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheap
source_url: 'https://developer.apple.com/documentation/metal/mtlheap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap.json'
content_hash: 'sha256:7ce45bf2ebeda31d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLHeap

<sub>Protocol</sub>

A memory pool from which you can suballocate resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLHeap : MTLAllocation
```

## Overview

Don’t implement this protocol yourself; instead, to create a heap, configure an [MTLHeapDescriptor](mtlheapdescriptor.md) instance and call the [- newHeapWithDescriptor:](<mtldevice/makeheap(descriptor_).md>) method of an [MTLDevice](mtldevice.md) instance.

You suballocate resources from a heap and make them _aliasable_ or _non-aliasable_. A sub-allocated resource is non-aliased by default, preventing future resources allocated from the heap from using its memory. Resources are _aliased_ when they share the same memory allocation on a heap.

All resources sub-allocated from the same heap share the same storage mode and CPU cache mode. You can make heaps purgeable, but not the resources allocated from the heap; they can only reflect the heap’s purgeability state.

## Relationships

- **Inherits From**: [MTLAllocation](mtlallocation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Naming and identifying a heap

- [label](mtlheap/label.md) — A string that identifies the heap.

### Creating buffers from a heap

- [- newBufferWithLength:options:](<mtlheap/makebuffer(length_options_).md>) — Creates a buffer on the heap.
- [- newBufferWithLength:options:offset:](<mtlheap/makebuffer(length_options_offset_).md>) — Creates a buffer at a specified offset on the heap.

### Creating textures from a heap

- [- newTextureWithDescriptor:](<mtlheap/maketexture(descriptor_).md>) — Creates a texture on the heap.
- [- newTextureWithDescriptor:offset:](<mtlheap/maketexture(descriptor_offset_).md>) — Creates a texture at a specified offset on the heap.

### Creating acceleration structure from a heap

- [- newAccelerationStructureWithSize:](<mtlheap/makeaccelerationstructure(size_).md>)
- [- newAccelerationStructureWithSize:offset:](<mtlheap/makeaccelerationstructure(size_offset_).md>)
- [- newAccelerationStructureWithDescriptor:](<mtlheap/makeaccelerationstructure(descriptor_).md>)
- [- newAccelerationStructureWithDescriptor:offset:](<mtlheap/makeaccelerationstructure(descriptor_offset_).md>)

### Configuring a heap’s purgeable state

- [- setPurgeableState:](<mtlheap/setpurgeablestate(__).md>) — Sets the purgeable state of the heap.

### Checking a heap’s size information

- [- maxAvailableSizeWithAlignment:](<mtlheap/maxavailablesize(alignment_).md>) — The maximum size of a resource, in bytes, that can be currently allocated from the heap.
- [size](mtlheap/size.md) — The total size of the heap, in bytes.
- [usedSize](mtlheap/usedsize.md) — The size of all resources currently in the heap, in bytes.
- [currentAllocatedSize](mtlheap/currentallocatedsize.md) — The size, in bytes, of the current heap allocation.

### Checking a heap’s permanent configuration

- [device](mtlheap/device.md) — The device object that created the heap.
- [type](mtlheap/type.md) — The heap’s type.
- [storageMode](mtlheap/storagemode.md) — The heap’s storage mode.
- [cpuCacheMode](mtlheap/cpucachemode.md) — The heap’s CPU cache mode.
- [hazardTrackingMode](mtlheap/hazardtrackingmode.md) — The heap’s hazard tracking mode.
- [resourceOptions](mtlheap/resourceoptions.md) — The options for resources created by the heap.

## See Also

### Resource memory allocation and management

- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md) — Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md) — Use events to synchronize access to resources allocated on a heap.
- [Implementing a multistage image filter using heaps and fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md) — Use fences to synchronize access to resources allocated on a heap.
- [MTLHeapDescriptor](mtlheapdescriptor.md) — A configuration that customizes the behavior for a Metal memory heap.
- [MTLHeapType](mtlheaptype.md) — The options you use to choose the heap type.
- [MTLSizeAndAlign](mtlsizeandalign.md) — The size and alignment of a resource, in bytes.
