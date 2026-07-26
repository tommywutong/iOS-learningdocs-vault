---
title: Work submission
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/work-submission
source_url: 'https://developer.apple.com/documentation/metal/work-submission'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/work-submission.json'
content_hash: 'sha256:f7a0a546daa7ddb1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [MTLDevice](mtldevice.md)

# Work submission

<sub>API Collection</sub>

Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.

## Topics

### Creating command queues

- [- newCommandQueue](<mtldevice/makecommandqueue().md>) — Creates a queue you use to submit rendering and computation commands to a GPU.
- [- newCommandQueueWithMaxCommandBufferCount:](<mtldevice/makecommandqueue(maxcommandbuffercount_).md>) — Creates a queue you use to submit rendering and computation commands to a GPU that has a fixed number of uncompleted command buffers.

### Creating residency sets

- [- newResidencySetWithDescriptor:error:](<mtldevice/makeresidencyset(descriptor_).md>) — Creates a residency set, which can move resources in and out of memory residency.

### Creating I/O command queues

- [- newIOCommandQueueWithDescriptor:error:](<mtldevice/makeiocommandqueue(descriptor_).md>) — Creates an input/output command queue you use to submit commands that load assets from the file system into GPU resources or system memory.

### Creating I/O file handles

- [- newIOFileHandleWithURL:error:](<mtldevice/makeiofilehandle(url_).md>) — Creates an input/output file handle instance that represents a file at a URL.
- [- newIOFileHandleWithURL:compressionMethod:error:](<mtldevice/makeiofilehandle(url_compressionmethod_).md>) — Creates an input/output file handle instance that represents a compressed file at a URL.
- [- newIOHandleWithURL:error:](<mtldevice/makeiohandle(url_).md>) — Creates an input/output file handle instance that represents a file at a URL. _(deprecated)_
- [- newIOHandleWithURL:compressionMethod:error:](<mtldevice/makeiohandle(url_compressionmethod_).md>) — Creates an input/output file handle instance that represents a compressed file at a URL. _(deprecated)_

### Creating indirect command buffers

- [- newIndirectCommandBufferWithDescriptor:maxCommandCount:options:](<mtldevice/makeindirectcommandbuffer(descriptor_maxcommandcount_options_).md>) — Creates an indirect command buffer instance.

## See Also

### Working with GPU devices

- [Device inspection](device-inspection.md) — Locate and identify a GPU and the features it supports, and sample its counters.
- [Pipeline state creation](pipeline-state-creation.md) — Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.
- [Resource creation](resource-creation.md) — Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.
- [Shader library and archive creation](shader-library-and-archive-creation.md) — Create static and dynamic shader libraries, and binary shader archives.
