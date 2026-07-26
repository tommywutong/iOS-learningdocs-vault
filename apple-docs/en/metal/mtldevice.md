---
title: MTLDevice
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice
source_url: 'https://developer.apple.com/documentation/metal/mtldevice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice.json'
content_hash: 'sha256:8830148fe731dafe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDevice

<sub>Protocol</sub>

The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLDevice : NSObjectProtocol, Sendable
```

## Overview

You can get the default [MTLDevice](mtldevice.md) at runtime by calling [MTLCreateSystemDefaultDevice](<mtlcreatesystemdefaultdevice().md>) (see [Getting the default GPU](getting-the-default-gpu.md)). Each Metal device instance represents a GPU and is the main starting point for your app’s interaction with it. With a Metal device instance, you can inspect a GPU’s features and capabilities (see [Device inspection](device-inspection.md)) and create subsidiary type instances with its factory methods.

- Buffers, textures, and other resources store, synchronize, and pass data between the GPU and CPU (see [Resource fundamentals](resource-fundamentals.md)).
- Input/Output command queues efficiently load resources from the file system (see [Resource loading](resource-loading.md)).
- Command queues create command encoders and schedule work for the GPU, including rendering and compute commands (see [Render passes](render-passes.md) and [Compute passes](compute-passes.md)).
- Pipeline states store render or compute pipeline configurations — which can be expensive to create — so that you can reuse them, potentially many times.

If your app uses more than one GPU (see [Multi-GPU systems](multi-gpu-systems.md)), ensure that instances of these types only interact with others from the same device. For example, your app can pass a texture to a command encoder that comes from the same Metal device, but not to another device.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Working with GPU devices

- [Device inspection](device-inspection.md) — Locate and identify a GPU and the features it supports, and sample its counters.
- [Work submission](work-submission.md) — Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.
- [Pipeline state creation](pipeline-state-creation.md) — Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.
- [Resource creation](resource-creation.md) — Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.
- [Shader library and archive creation](shader-library-and-archive-creation.md) — Create static and dynamic shader libraries, and binary shader archives.

### Instance Properties

- [maximumConcurrentCompilationTaskCount](mtldevice/maximumconcurrentcompilationtaskcount.md) — The maximum number of concurrent compilation tasks the device is running.
- [shouldMaximizeConcurrentCompilation](mtldevice/shouldmaximizeconcurrentcompilation.md) — A Boolean value that indicates whether the device uses additional CPU threads for compilation tasks.
- [supportsPlacementSparse](mtldevice/supportsplacementsparse.md) — A Boolean value that indicates whether the device supports placement sparse resources.

### Instance Methods

- [- functionHandleWithFunction:](<mtldevice/functionhandle(function_)-4bw39.md>)
- [- functionHandleWithBinaryFunction:](<mtldevice/functionhandle(function_)-w9ia.md>) — Get the function handle for the specified binary-linked function from the pipeline state.
- [- newArchiveWithURL:error:](<mtldevice/makearchive(url_).md>) — Creates a new archive from data available at an `NSURL` address.
- [- newArgumentTableWithDescriptor:error:](<mtldevice/makeargumenttable(descriptor_).md>) — Creates a new argument table from an argument table descriptor.
- [- newBufferWithLength:options:placementSparsePageSize:](<mtldevice/makebuffer(length_options_placementsparsepagesize_).md>) — Creates a new placement sparse buffer of a specific length.
- [- newCommandAllocator](<mtldevice/makecommandallocator().md>) — Creates a new command allocator.
- [- newCommandAllocatorWithDescriptor:error:](<mtldevice/makecommandallocator(descriptor_).md>) — Creates a new command allocator from a command allocator descriptor.
- [- newCommandBuffer](<mtldevice/makecommandbuffer().md>) — Creates a new command buffer.
- [- newCommandQueueWithDescriptor:](<mtldevice/makecommandqueue(descriptor_).md>) — Creates a command queue with the provided configuration.
- [- newCompilerWithDescriptor:error:](<mtldevice/makecompiler(descriptor_).md>) — Creates a new compiler from a compiler descriptor.
- [- newCounterHeapWithDescriptor:error:](<mtldevice/makecounterheap(descriptor_).md>) — Creates a new counter heap configured from a counter heap descriptor.
- [- newLogStateWithDescriptor:error:](<mtldevice/makelogstate(descriptor_).md>) — Creates a shader log state with the provided configuration.
- [- newMTL4CommandQueue](<mtldevice/makemtl4commandqueue().md>) — Creates a new command queue.
- [- newMTL4CommandQueueWithDescriptor:error:](<mtldevice/makemtl4commandqueue(descriptor_).md>) — Creates a new command queue from a queue descriptor.
- [- newPipelineDataSetSerializerWithDescriptor:](<mtldevice/makepipelinedatasetserializer(descriptor_).md>) — Creates a new pipeline data set serializer instance from a descriptor.
- [- newTensorWithDescriptor:error:](<mtldevice/maketensor(descriptor_).md>) — Creates a tensor with the specified descriptor.
- [- newTensorWithDescriptor:attachments:error:](<mtldevice/maketensor(descriptor_attachments_).md>) — Creates a tensor with the specified descriptor and per-plane buffer backing storage. _(beta)_
- [- newTextureViewPoolWithDescriptor:error:](<mtldevice/maketextureviewpool(descriptor_).md>) — Creates a new texture view pool from a resource view pool descriptor.
- [- queryTimestampFrequency](<mtldevice/querytimestampfrequency().md>) — Queries the frequency of the GPU timestamp in ticks per second.
- [- sizeOfCounterHeapEntry:](<mtldevice/size(ofcounterheapentry_).md>) — Returns the size, in bytes, of each entry in a counter heap of a specific counter heap type when your app resolves it into a usable format.
- [- tensorSizeAndAlignWithDescriptor:](<mtldevice/tensorsizeandalign(descriptor_).md>) — Determines the size and alignment required to hold the data of a tensor you create with a descriptor in a buffer.

## See Also

### Locating and inspecting a GPU device

- [Getting the default GPU](getting-the-default-gpu.md) — Select the system’s default GPU device on which to run your Metal code.
- [Detecting GPU features and Metal software versions](detecting-gpu-features-and-metal-software-versions.md) — Use the device object’s properties to determine how you perform tasks in Metal.
- [MTLCreateSystemDefaultDevice](<mtlcreatesystemdefaultdevice().md>) — Returns the device instance Metal selects as the default.
- [Multi-GPU systems](multi-gpu-systems.md) — Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.
