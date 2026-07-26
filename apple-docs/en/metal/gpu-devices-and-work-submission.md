---
title: GPU devices and work submission
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/gpu-devices-and-work-submission
source_url: 'https://developer.apple.com/documentation/metal/gpu-devices-and-work-submission'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/gpu-devices-and-work-submission.json'
content_hash: 'sha256:504be891e20f8c2d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# GPU devices and work submission

<sub>API Collection</sub>

Find any available GPU, submit work to it with command buffers, suspend work, and coordinate between multiple GPUs.

## Overview

You can use any available GPU’s [MTLDevice](mtldevice.md) instance in addition to the default instance that [MTLCreateSystemDefaultDevice](<mtlcreatesystemdefaultdevice().md>) returns. For each device instance, get its [MTLCommandQueue](mtlcommandqueue.md) instance, and create one or more [MTLCommandBuffer](mtlcommandbuffer.md) instances to send work to the GPU.

When the system suspends your app, use the command queue to finish command buffers already in progress. See [Preparing your Metal app to run in the background](preparing-your-metal-app-to-run-in-the-background.md) for more information.

## Topics

### Locating and inspecting a GPU device

- [Getting the default GPU](getting-the-default-gpu.md) — Select the system’s default GPU device on which to run your Metal code.
- [Detecting GPU features and Metal software versions](detecting-gpu-features-and-metal-software-versions.md) — Use the device object’s properties to determine how you perform tasks in Metal.
- [MTLCreateSystemDefaultDevice](<mtlcreatesystemdefaultdevice().md>) — Returns the device instance Metal selects as the default.
- [MTLDevice](mtldevice.md) — The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.
- [Multi-GPU systems](multi-gpu-systems.md) — Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.

### Submitting work to a GPU with Metal 4

- [MTL4CommandQueue](mtl4commandqueue.md) — An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.
- [MTL4CommandQueueDescriptor](mtl4commandqueuedescriptor.md) — Groups together parameters for the creation of a new command queue.
- [MTL4CommandQueueError](mtl4commandqueueerror-swift.struct.md)
- [Code](mtl4commandqueueerror-swift.struct/code.md) — Enumeration of kinds of errors that committing an array of command buffers instances can produce.
- [MTL4CommandQueueErrorDomain](mtl4commandqueueerrordomain.md)
- [MTL4CommandBuffer](mtl4commandbuffer.md) — Records a sequence of GPU commands.
- [MTL4CommandBufferOptions](mtl4commandbufferoptions.md) — Options to configure a command buffer before encoding work into it.
- [MTL4CommandEncoder](mtl4commandencoder.md) — An encoder that writes GPU commands into a command buffer.
- [MTL4RenderEncoderOptions](mtl4renderencoderoptions.md) — Custom render pass options you specify at encoder creation time.
- [MTL4ArgumentTable](mtl4argumenttable.md) — Provides a mechanism to manage and provide resource bindings for buffers, textures, sampler states and other Metal resources.
- [MTL4ArgumentTableDescriptor](mtl4argumenttabledescriptor.md) — Groups parameters for the creation of a Metal argument table.
- [MTL4CommandAllocator](mtl4commandallocator.md) — Manages the memory backing the encoding of GPU commands into command buffers.
- [MTL4CommandAllocatorDescriptor](mtl4commandallocatordescriptor.md) — Groups together parameters for creating a command allocator.
- [MTL4CommitOptions](mtl4commitoptions.md) — Represents options to configure a commit operation on a command queue.
- [MTL4CommitFeedback](mtl4commitfeedback.md) — Describes an object containing debug information from Metal to your app after completing a workload.
- [MTL4CommitFeedbackHandler](mtl4commitfeedbackhandler.md) — Defines the block signature for a callback Metal invokes to provide your app feedback after completing a workload.
- [MTL4CounterHeap](mtl4counterheap.md) — Represents an opaque, driver-controlled section of memory that can store GPU counter data.
- [MTL4CounterHeapDescriptor](mtl4counterheapdescriptor.md) — Groups together parameters for configuring a counter heap object at creation time.
- [MTL4CounterHeapType](mtl4counterheaptype.md) — Defines the type of a [MTL4CounterHeap](mtl4counterheap.md) and the contents of its entries.
- [MTL4TimestampHeapEntry](mtl4timestampheapentry.md) — Represents a timestamp data entry in a counter heap of type `MTL4CounterHeapTypeTimestamp`.
- [MTL4TimestampGranularity](mtl4timestampgranularity.md) — Provides a hint to the system about the desired accuracy when writing GPU counter timestamps.

### Submitting work to a GPU with Metal

- [Setting up a command structure](setting-up-a-command-structure.md) — Discover how Metal executes commands on a GPU.
- [MTLCommandQueue](mtlcommandqueue.md) — An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.
- [MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md) — A configuration that customizes the behavior for a new command queue.
- [MTLCommandBuffer](mtlcommandbuffer.md) — A container that stores a sequence of GPU commands that you encode into it.
- [MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md) — A configuration that customizes the behavior for a new command buffer.
- [MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md) — The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [MTLCommandEncoder](mtlcommandencoder.md) — An encoder that writes GPU commands into a command buffer.

### Suspending work on a GPU

- [Preparing your Metal app to run in the background](preparing-your-metal-app-to-run-in-the-background.md) — Prepare your app to move into the background by pausing future GPU use and ensuring previous work is scheduled.
