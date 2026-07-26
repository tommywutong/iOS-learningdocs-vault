---
title: Resource fundamentals
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/resource-fundamentals
source_url: 'https://developer.apple.com/documentation/metal/resource-fundamentals'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/resource-fundamentals.json'
content_hash: 'sha256:ea98dfe69ca192e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# Resource fundamentals

<sub>API Collection</sub>

Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.

## Overview

A _resource_ is a memory asset, such as an [MTLBuffer](mtlbuffer.md) or [MTLTexture](mtltexture.md), that a GPU can access (see [Buffers](buffers.md) and [Textures](textures.md)).

You can either allocate a resource from an [MTLDevice](mtldevice.md) instance or an [MTLHeap](mtlheap.md) instance (see [Memory heaps](memory-heaps.md)). Metal sets a resource’s [hazardTrackingMode](mtlresource/hazardtrackingmode.md) property to [MTLHazardTrackingModeDefault](mtlhazardtrackingmode/default.md) if you don’t select another tracking mode. The default value depends on what Metal instance creates the resource.

> [!important] Important
> The value of an [MTLResource](mtlresource.md) instance’s [hazardTrackingMode](mtlresource/hazardtrackingmode.md) property has no effect on the work you submit to an [MTL4CommandQueue](mtl4commandqueue.md) (see [Resource synchronization](resource-synchronization.md)) or resources that commands access through an argument buffer.

Each resource your app creates typically uses one of these storage modes:

- **[MTLStorageModePrivate](mtlstoragemode/private.md)** — Apps can only access resources in private storage from the GPU.
- **[MTLStorageModeShared](mtlstoragemode/shared.md)** — Apps can access resources in shared storage from both the CPU and the GPU.
- **[MTLStorageModeManaged](mtlstoragemode/managed.md)** — Apps can access resources in managed storage from both the CPU and the GPU, just like shared storage. However, the GPU backs resources in managed mode with memory in private storage.

Private mode resources give your app optimization opportunities that shared mode resources don’t. Managed mode resources also give your app the same opportunities and allow your to app access them from the CPU.

## Topics

### Resource management

- [Setting resource storage modes](setting-resource-storage-modes.md) — Set a storage mode that defines the memory location and access permissions of a resource.
- [Choosing a resource storage mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md) — Select an appropriate storage mode for your textures and buffers on Apple GPUs.
- [Choosing a resource storage mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md) — Select an appropriate storage mode for your textures and buffers on AMD and Intel GPUs.
- [Copying data to a private resource](copying-data-to-a-private-resource.md) — Use a blit command encoder to copy buffer or texture data to a private resource.
- [Synchronizing a managed resource in macOS](synchronizing-a-managed-resource-in-macos.md) — Manually synchronize memory for a Metal resource in apps.
- [Transferring data between connected GPUs](transferring-data-between-connected-gpus.md) — Use high-speed connections between GPUs to transfer data quickly.
- [Reducing the memory footprint of Metal apps](reducing-the-memory-footprint-of-metal-apps.md) — Learn best practices for using memory efficiently in iOS and tvOS.

### Residency sets

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md) — Organize your resources into groups and influence when they become accessible to the GPU.
- [MTLResidencySet](mtlresidencyset.md) — A collection of resource allocations that can move in and out of resident memory.
- [MTLResidencySetDescriptor](mtlresidencysetdescriptor.md) — A configuration that customizes the behavior for a residency set.

### View pools

- [MTLResourceViewPool](mtlresourceviewpool.md) — Contains views over resources of a specific type, and allows you to manage those views.
- [MTLResourceViewPoolDescriptor](mtlresourceviewpooldescriptor.md) — Provides parameters for creating a resource view pool.
- [MTLTextureViewPool](mtltextureviewpool.md) — A pool of lightweight texture views.
- [MTLTextureViewDescriptor](mtltextureviewdescriptor.md)

### Tensors

- [MTLTensor](mtltensor.md) — A resource representing a multi-dimensional array that you can use with machine learning workloads.
- [MTLTensorDescriptor](mtltensordescriptor.md) — A configuration type for creating new tensor instances.
- [MTLTensorExtents](mtltensorextents.md) — An integer array that holds per-dimension values such as tensor sizes, strides, or block factors
- [MTLTensorReferenceType](mtltensorreferencetype.md) — An object that represents a tensor in the shading language in a struct or array.
- [MTLTensorUsage](mtltensorusage.md) — The contexts in which you can use a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTLTensorBinding](mtltensorbinding.md) — An object that represents a tensor bound to a graphics or compute function or a machine learning function.
- [MTLTensorError](mtltensorerror-swift.struct.md)
- [Code](mtltensorerror-swift.struct/code.md) — The error codes that Metal can raise when you create a tensor.
- [MTLTensorDataType](mtltensordatatype.md) — The possible data types for the elements of a tensor.
- [MTLTensorDomain](mtltensordomain.md) — An error domain for errors that pertain to creating a tensor.
- [MTL_TENSOR_MAX_RANK](mtl_tensor_max_rank.md)

### Sparse resources

- [MTLBufferSparseTier](mtlbuffersparsetier.md) — Enumerates the different support levels for sparse buffers.
- [MTL4CopySparseBufferMappingOperation](mtl4copysparsebuffermappingoperation.md) — Groups together arguments for an operation to copy a sparse buffer mapping.
- [MTL4UpdateSparseBufferMappingOperation](mtl4updatesparsebuffermappingoperation.md) — Groups together arguments for an operation to update a sparse buffer mapping.
- [MTLTextureSparseTier](mtltexturesparsetier.md) — Enumerates the different support levels for sparse textures.
- [MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md) — Groups together arguments for an operation to copy a sparse texture mapping.
- [MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md) — Groups together arguments for an operation to update a sparse texture mapping.

### Common resource functionality

- [MTLGPUAddress](mtlgpuaddress.md) — A 64-bit unsigned integer type appropriate for storing GPU addresses.
- [MTLAllocation](mtlallocation.md) — A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.
- [MTLResource](mtlresource.md) — An allocation of memory accessible to a GPU.
- [MTLResourceOptions](mtlresourceoptions.md) — Optional arguments used to set the behavior of a resource.
- [MTLResourceUsage](mtlresourceusage.md) — Options that describe how a graphics or compute function uses an argument buffer’s resource.
- [MTLResourceID](mtlresourceid.md)

## See Also

### Resources

- [Buffers](buffers.md) — Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](textures.md) — Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory heaps](memory-heaps.md) — Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource loading](resource-loading.md) — Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource synchronization](resource-synchronization.md) — Prevent multiple commands that can access the same resources simultaneously by coordinating those reads and writes with barriers, fences, or events.
