---
title: Buffers
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/buffers
source_url: 'https://developer.apple.com/documentation/metal/buffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/buffers.json'
content_hash: 'sha256:938f63d07a1875d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# Buffers

<sub>API Collection</sub>

Create and manage untyped data your app uses to exchange information with its shader functions.

## Overview

Each [MTLBuffer](mtlbuffer.md) instance represents a general purpose, typeless memory allocation that your app uses to send and retrieve data from a shader. Your app decides how to use and interpret the buffer’s underlying bytes.

You create buffers from either an [MTLDevice](mtldevice.md) or [MTLHeap](mtlheap.md) instance.

**Swift**

```swift
let deviceBuffer = device.makeBuffer(length: bufferSize,
                                     options: .storageModeShared)

let heapBuffer = heap.makeBuffer(length: bufferSize,
                                 options: .storageModePrivate)
```

**Objective-C**

```objective-c
id <MTLBuffer> deviceBuffer = [device newBufferWithLength: bufferSize
                                                  options: MTLResourceStorageModeShared];

id <MTLBuffer> heapBuffer = [heap newBufferWithLength:bufferSize
                                              options:MTLResourceStorageModePrivate];
```

**C++**

```cpp
// Metal-CPP
MTL::Buffer* pDeviceBuffer = pDevice->newBuffer(bufferSize,
                                                MTL::ResourceStorageModeShared);

MTL::Buffer* pHeapBuffer = pHeap->newBuffer(bufferSize,
                                            MTL::ResourceStorageModePrivate);
```

Buffers inherently support the [MTLResource](mtlresource.md) protocol’s properties and methods, including [storageMode](mtlresource/storagemode.md), which controls how the GPU handles its memory (see [Resource fundamentals](resource-fundamentals.md)).

## Topics

### General purpose buffers

- [MTLBuffer](mtlbuffer.md) — A resource that stores data in a format defined by your app.

### Argument buffers

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md) — Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md) — Create argument buffers to organize related resources.
- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md) — Optimize resource performance within an argument buffer.
- [Indexing argument buffers](indexing-argument-buffers.md) — Assign resource indices within an argument buffer.
- [Rendering terrain dynamically with argument buffers](rendering-terrain-dynamically-with-argument-buffers.md) — Use argument buffers to render terrain in real time with a GPU-driven pipeline.
- [Encoding argument buffers on the GPU](encoding-argument-buffers-on-the-gpu.md) — Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md) — Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [MTLArgumentDescriptor](mtlargumentdescriptor.md) — A representation of an argument within an argument buffer.
- [MTLArgumentEncoder](mtlargumentencoder.md) — An interface you can use to encode argument data into an argument buffer.
- [MTLAttributeStrideStatic](mtlattributestridestatic.md)

### Model I/O interoperability

- [MTKMesh](../metalkit/mtkmesh.md) — A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKMeshBuffer](../metalkit/mtkmeshbuffer.md) — A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKMeshBufferAllocator](../metalkit/mtkmeshbufferallocator.md) — An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKSubmesh](../metalkit/mtksubmesh.md) — A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [MTKModelError](../metalkit/mtkmodelerror.md) — Constants used to declare Model Errors.
- [MTKMetalVertexFormatFromModelIO(_:)](<../metalkit/mtkmetalvertexformatfrommodelio(__).md>) — Returns a converted Metal vertex format.
- [MTKModelIOVertexFormatFromMetal(_:)](<../metalkit/mtkmodeliovertexformatfrommetal(__).md>) — Returns a converted Model I/O vertex format.
- [MTKMetalVertexDescriptorFromModelIO(_:)](<../metalkit/mtkmetalvertexdescriptorfrommodelio(__).md>) — Returns a partially converted Metal vertex descriptor.
- [MTKModelIOVertexDescriptorFromMetal(_:)](<../metalkit/mtkmodeliovertexdescriptorfrommetal(__).md>) — Returns a partially converted Model I/O vertex descriptor.

## See Also

### Resources

- [Resource fundamentals](resource-fundamentals.md) — Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.
- [Textures](textures.md) — Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory heaps](memory-heaps.md) — Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource loading](resource-loading.md) — Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource synchronization](resource-synchronization.md) — Prevent multiple commands that can access the same resources simultaneously by coordinating those reads and writes with barriers, fences, or events.
