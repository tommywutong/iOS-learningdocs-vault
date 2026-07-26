---
title: Resource creation
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/resource-creation
source_url: 'https://developer.apple.com/documentation/metal/resource-creation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/resource-creation.json'
content_hash: 'sha256:5f4fd58fa60ecd06'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [MTLDevice](mtldevice.md)

# Resource creation

<sub>API Collection</sub>

Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.

## Topics

### Working with resource heaps

- [- newHeapWithDescriptor:](<mtldevice/makeheap(descriptor_).md>) — Creates a new GPU heap instance.
- [- heapBufferSizeAndAlignWithLength:options:](<mtldevice/heapbuffersizeandalign(length_options_).md>) — Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [- heapTextureSizeAndAlignWithDescriptor:](<mtldevice/heaptexturesizeandalign(descriptor_).md>) — Returns the size and alignment, in bytes, of a texture if you create it from a heap.
- [- heapAccelerationStructureSizeAndAlignWithSize:](<mtldevice/heapaccelerationstructuresizeandalign(size_).md>) — Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.
- [- heapAccelerationStructureSizeAndAlignWithDescriptor:](<mtldevice/heapaccelerationstructuresizeandalign(descriptor_).md>) — Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.
- [MTLSizeAndAlign](mtlsizeandalign.md) — The size and alignment of a resource, in bytes.

### Creating buffers

- [maxBufferLength](mtldevice/maxbufferlength.md) — The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.
- [- newBufferWithLength:options:](<mtldevice/makebuffer(length_options_).md>) — Creates a buffer the method clears with zero values.
- [- newBufferWithBytes:length:options:](<mtldevice/makebuffer(bytes_length_options_).md>) — Allocates a new buffer of a given length and initializes its contents by copying existing data into it.
- [- newBufferWithBytesNoCopy:length:options:deallocator:](<mtldevice/makebuffer(bytesnocopy_length_options_deallocator_).md>) — Creates a buffer that wraps an existing contiguous memory allocation.

### Creating textures

- [- newTextureWithDescriptor:](<mtldevice/maketexture(descriptor_).md>) — Creates a new texture instance.
- [- newTextureWithDescriptor:iosurface:plane:](<mtldevice/maketexture(descriptor_iosurface_plane_).md>) — Creates a texture instance that uses I/O surface to store its underlying data.
- [- newSharedTextureWithDescriptor:](<mtldevice/makesharedtexture(descriptor_).md>) — Creates a texture that you can share across process boundaries.
- [- newSharedTextureWithHandle:](<mtldevice/makesharedtexture(handle_).md>) — Creates a texture that references a shared texture.
- [- minimumLinearTextureAlignmentForPixelFormat:](<mtldevice/minimumlineartexturealignment(for_).md>) — Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.
- [- minimumTextureBufferAlignmentForPixelFormat:](<mtldevice/minimumtexturebufferalignment(for_).md>) — Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.

### Creating samplers

- [- supportsTextureSampleCount:](<mtldevice/supportstexturesamplecount(__).md>) — Returns a Boolean value that indicates whether the GPU can sample a texture with a specific number of sample points.
- [- newSamplerStateWithDescriptor:](<mtldevice/makesamplerstate(descriptor_).md>) — Creates a sampler state instance.
- [getDefaultSamplePositions(sampleCount:)](<mtldevice/getdefaultsamplepositions(samplecount_).md>) — Returns the default sample locations based on the number of samples.

### Working with sparse textures

- [- sparseTileSizeWithTextureType:pixelFormat:sampleCount:sparsePageSize:](<mtldevice/sparsetilesize(texturetype_pixelformat_samplecount_sparsepagesize_).md>) — Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.
- [- sparseTileSizeWithTextureType:pixelFormat:sampleCount:](<mtldevice/sparsetilesize(with_pixelformat_samplecount_).md>) — Returns the dimensions of a sparse tile for a texture.
- [- sparseTileSizeInBytesForSparsePageSize:](<mtldevice/sparsetilesizeinbytes(sparsepagesize_).md>) — Returns the size, in bytes, of a sparse tile the GPU device creates with a specific page size.
- [sparseTileSizeInBytes](mtldevice/sparsetilesizeinbytes.md) — Returns the size, in bytes, of a sparse tile the GPU device creates using a default page size.
- [- convertSparsePixelRegions:toTileRegions:withTileSize:alignmentMode:numRegions:](<mtldevice/convertsparsepixelregions(__totileregions_withtilesize_alignmentmode_numregions_).md>) — Converts a list of sparse pixel regions to tile regions.
- [- convertSparseTileRegions:toPixelRegions:withTileSize:numRegions:](<mtldevice/convertsparsetileregions(__topixelregions_withtilesize_numregions_).md>) — Converts a list of sparse tile regions to pixel regions.
- [MTLSparsePageSize](mtlsparsepagesize.md) — The page size options, in kilobytes, for sparse textures.
- [MTLSparseTextureRegionAlignmentMode](mtlsparsetextureregionalignmentmode.md) — Options used when converting between a pixel-based region within a texture to a tile-based region.

### Creating acceleration structures for ray tracing

- [- newAccelerationStructureWithDescriptor:](<mtldevice/makeaccelerationstructure(descriptor_).md>) — Creates a new ray-tracing acceleration structure from a descriptor.
- [- newAccelerationStructureWithSize:](<mtldevice/makeaccelerationstructure(size_).md>) — Creates a new acceleration structure with a specific size.
- [- accelerationStructureSizesWithDescriptor:](<mtldevice/accelerationstructuresizes(descriptor_).md>) — Returns the buffer sizes the GPU device needs to build, refit, and store an acceleration structure.
- [MTLAccelerationStructureSizes](mtlaccelerationstructuresizes.md) — The expected sizes for a ray-tracing acceleration structure.

### Creating argument buffer encoders

- [argumentBuffersSupport](mtldevice/argumentbufferssupport.md) — Returns the GPU device’s support tier for argument buffers.
- [maxArgumentBufferSamplerCount](mtldevice/maxargumentbuffersamplercount.md) — The maximum number of unique argument buffer samplers per app.
- [- newArgumentEncoderWithArguments:](<mtldevice/makeargumentencoder(arguments_).md>) — Creates a new argument encoder for an array of arguments.
- [- newArgumentEncoderWithBufferBinding:](<mtldevice/makeargumentencoder(bufferbinding_).md>) — Creates a new argument encoder for a buffer binding.

### Creating fences and events

- [- newFence](<mtldevice/makefence().md>) — Creates a new memory fence instance.
- [- newEvent](<mtldevice/makeevent().md>) — Creates a new event instance that you can use to synchronize commands and resources within the same GPU device.
- [- newSharedEvent](<mtldevice/makesharedevent().md>) — Creates a new shared event instance that you can use to synchronize commands and resources across different GPU devices.
- [- newSharedEventWithHandle:](<mtldevice/makesharedevent(handle_).md>) — Recreates a shared event from a handle.

### Creating rasterization rate maps

- [- supportsRasterizationRateMapWithLayerCount:](<mtldevice/supportsrasterizationratemap(layercount_).md>) — Returns a Boolean value that indicates whether the GPU can create a rasterization rate map with a specific number of layers.
- [- newRasterizationRateMapWithDescriptor:](<mtldevice/makerasterizationratemap(descriptor_).md>) — Creates a rasterization rate map instance.

## See Also

### Working with GPU devices

- [Device inspection](device-inspection.md) — Locate and identify a GPU and the features it supports, and sample its counters.
- [Work submission](work-submission.md) — Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.
- [Pipeline state creation](pipeline-state-creation.md) — Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.
- [Shader library and archive creation](shader-library-and-archive-creation.md) — Create static and dynamic shader libraries, and binary shader archives.
