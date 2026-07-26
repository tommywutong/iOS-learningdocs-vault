---
title: Memory heaps
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/memory-heaps
source_url: 'https://developer.apple.com/documentation/metal/memory-heaps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/memory-heaps.json'
content_hash: 'sha256:ec05edc03407b6bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# Memory heaps

<sub>API Collection</sub>

Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.

## Overview

Use an [MTLHeap](mtlheap.md) to quickly create and destroy GPU resources. Heaps can also help your apps save memory by aliasing portions of it in multiple places.

Create a heap by calling an [MTLDevice](mtldevice.md) instance’s [- newHeapWithDescriptor:](<mtldevice/makeheap(descriptor_).md>) method.

> [!note] Note
> Metal only synchronizes resources that you create from a Metal heap and that have the [hazardTrackingMode](mtlheap/hazardtrackingmode.md) property set to [MTLHazardTrackingModeTracked](mtlhazardtrackingmode/tracked.md).

## Topics

### Resource memory allocation and management

- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md) — Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md) — Use events to synchronize access to resources allocated on a heap.
- [Implementing a multistage image filter using heaps and fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md) — Use fences to synchronize access to resources allocated on a heap.
- [MTLHeap](mtlheap.md) — A memory pool from which you can suballocate resources.
- [MTLHeapDescriptor](mtlheapdescriptor.md) — A configuration that customizes the behavior for a Metal memory heap.
- [MTLHeapType](mtlheaptype.md) — The options you use to choose the heap type.
- [MTLSizeAndAlign](mtlsizeandalign.md) — The size and alignment of a resource, in bytes.

## See Also

### Resources

- [Resource fundamentals](resource-fundamentals.md) — Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.
- [Buffers](buffers.md) — Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](textures.md) — Create and manage typed data your app uses to exchange information with its shader functions.
- [Resource loading](resource-loading.md) — Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource synchronization](resource-synchronization.md) — Prevent multiple commands that can access the same resources simultaneously by coordinating those reads and writes with barriers, fences, or events.
