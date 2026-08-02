---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/ResourceHeaps/ResourceHeaps.html
archived_at: '2026-07-15T08:16:54.134407Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Tessellation.md)

# Resource Heaps

__Available in:__ `iOS_GPUFamily1_v3`, `iOS_GPUFamily2_v3`, `iOS_GPUFamily3_v2`, `tvOS_GPUFamily1_v2`

Resource heaps allow Metal resources to be backed by the same memory allocation. These resources are created from a memory pool known as a _heap_ and they are tracked by a _fence_ that captures and manages GPU work dependencies. Resource heaps help your app reduce the cost of:

- __Resource creation.__ Resource creation may involve allocating new memory, mapping it into your process, and zero filling it. This cost is reduced by creating resources from a larger heap or from recycled resource memory backed by a heap.
- __Fixed memory budget.__ If some of your resources are not used for some time, the virtual memory may compress the resource memory to save space. This can cause extra time spent in making this resource memory available again for the next use. By using a small number of heaps, you can keep your allocations within a given memory budget, and ensure those resources are continually in use (which can help provide more consistent performance).
- __Transient resources.__ Transient resources are produced and consumed for each frame, but not all of these resources are used together at the same time. To reduce memory consumption, transient resources that are not used together can share the same memory backed by a heap.

A [MTLHeap](https://developer.apple.com/documentation/metal/mtlheap) object is a Metal resource that represents an abstract memory pool. Resources created from this heap are defined as either _aliasable_ or _non-aliasable_. Sub-allocated resources are _aliased_ when they share the same portion of heap memory as another aliased resource.

A [MTLHeap](https://developer.apple.com/documentation/metal/mtlheap) object is created by calling the [newHeapWithDescriptor:](https://developer.apple.com/documentation/metal/mtldevice/1649928-newheapwithdescriptor) method of a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object. A [MTLHeapDescriptor](https://developer.apple.com/documentation/metal/mtlheapdescriptor) object describes the storage mode, CPU cache mode, and byte size of a heap. All resources sub-allocated from the same heap share the same storage mode and CPU cache mode. The byte size of the heap must always be large enough to allocate enough memory for its resources.

A heap can be made purgeable after it has been created by calling the [setPurgeableState:](https://developer.apple.com/documentation/metal/mtlheap/1771281-setpurgeablestate) method. The heap purgeability state refers to its whole backing memory and affects all resources within the heap. Heaps are purgeable but their resources are not; sub-allocated resources only reflect the heap’s purgeability state. Purgeability may be useful for heaps that store only render targets.

Both [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) and [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) objects can be sub-allocated from a heap. To do so, call one of these two methods of a [MTLHeap](https://developer.apple.com/documentation/metal/mtlheap) object:

- [newBufferWithLength:options:](https://developer.apple.com/documentation/metal/mtlheap/1649571-makebuffer)
- [newTextureWithDescriptor:](https://developer.apple.com/documentation/metal/mtlheap/1649574-maketexture)

Each sub-allocated resource is defined as non-aliasable by default, which prevents future sub-allocated resources from using its memory. To make a sub-allocated resource aliasable, call the [makeAliasable](https://developer.apple.com/documentation/metal/mtlresource/1771705-makealiasable) method; this allows future sub-allocated resources to reuse its memory.

Aliasable sub-allocated resources are not destroyed and can still be used by command encoders. These resources hold a strong reference to their heap which is released only when the resource itself is destroyed, but not when it is made aliasable. Sub-allocated resources can be destroyed only after all command buffers referencing them have completed execution.

Listing 13-1 shows the use of a heap for simple resource sub-allocation.

__Listing 13-1__  Simple heap creation and resource sub-allocation

```
// Calculate the size and alignment of each resource
MTLSizeAndAlign albedoSizeAndAlign = [_device heapTextureSizeAndAlignWithTextureDescriptor:_albedoDescriptor];
MTLSizeAndAlign normalSizeAndAlign = [_device heapTextureSizeAndAlignWithTextureDescriptor:_normalDescriptor];
MTLSizeAndAlign glossSizeAndAlign  = [_device heapTextureSizeAndAlignWithTextureDescriptor:_glossDescriptor];

// Calculate a heap size that satisfies the size requirements of all three resources
NSUInteger heapSize = albedoSizeAndAlign.size + normalSizeAndAlign.size + glossSizeAndAlign.size;

// Create a heap descriptor
MTLHeapDescriptor* heapDescriptor = [MTLHeapDescriptor new];
heapDescriptor.cpuCacheMode = MTLCPUCacheModeDefaultCache;
heapDescriptor.storageMode = MTLStorageModePrivate;
heapDescriptor.size = heapSize;

// Create a heap
id <MTLHeap> heap = [_device newHeapWithDescriptor:heapDescriptor];

// Create sub-allocated resources from the heap
id <MTLTexture> albedoTexture = [_heap newTextureWithDescriptor:_albedoDescriptor];
id <MTLTexture> normalTexture = [_heap newTextureWithDescriptor:_normalDescriptor];
id <MTLTexture> glossTexture  = [_heap newTextureWithDescriptor:_glossDescriptor];
```


A [MTLFence](https://developer.apple.com/documentation/metal/mtlfence) object is used to track and manage sub-allocated resource dependencies across command encoders. Resource dependencies arise as resources are produced and consumed by different commands, regardless of whether those commands are encoded to the same queue or different queues. A fence captures GPU work up to a specific point in time; when the GPU encounters a fence, it must wait until all the captured work is completed before continuing execution.

A [MTLFence](https://developer.apple.com/documentation/metal/mtlfence) object is created by calling the [newFence](https://developer.apple.com/documentation/metal/mtldevice/1649923-makefence) method of a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object. A fence is mainly used for tracking purposes and only supports tracking within the GPU, not between the CPU and the GPU. The [MTLFence](https://developer.apple.com/documentation/metal/mtlfence) protocol does not provide any methods or completion handlers and you can only modify the [label](https://developer.apple.com/documentation/metal/mtlfence/1648531-label) property.

Both [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) and [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) objects can be tracked with a fence. To update a fence, call the [updateFence:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1649359-updatefence) or [updateFence:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1649789-updatefence) method for each command encoder, respectively. To wait for a fence, call the [waitForFence:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1649358-waitforfence) or [waitForFence:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1649790-waitforfence) method for each command encoder, respectively.

The fence is updated or evaluated when the command buffer is actually submitted to the hardware. This maintains global order and prevents deadlock.

Drivers may wait on fences at the beginning of a command encoder, and drivers may delay fence updates until the end of the command encoder. Therefore, you are not allowed to first update and then wait on the same fence in the same command encoder (however, you are allowed to first wait and then update). Producer-consumer relationships must be split across different command encoders.

A [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) object can be tracked with a fence at a finer granularity. The [MTLRenderStages](https://developer.apple.com/documentation/metal/mtlrenderstages) enum allows you to specify the render stage at which a fence is either updated or waited for, allowing for vertex and fragment commands to overlap execution. Call the [updateFence:afterStages:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1648377-updatefence) method to update a fence and call the [waitForFence:beforeStages:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1648378-waitforfence) method to wait for a fence.

Listing 13-2 shows the use of a fence for simple tracking.

__Listing 13-2__  Simple fence tracking

```
id <MTLFence> fence = [_device newFence];
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];

// Producer
id <MTLRenderCommandEncoder> renderCommandEncoder = [commandBuffer renderCommandEncoderWithDescriptor:_descriptor];
/* Draw using resources associated with 'fence' */
[renderCommandEncoder updateFence:fence afterStages:MTLRenderStageFragment];
[renderCommandEncoder endEncoding];

// Consumer
id <MTLComputeCommandEncoder> computeCommandEncoder = [commandBuffer computeCommandEncoder];
[computeCommandEncoder waitForFence:fence];
/* Dispatch using resources associated with 'fence' */
[computeCommandEncoder endEncoding];

[commandBuffer commit];
```

You cannot assume that two command encoders will complete if only the latter command encoder updates a fence. The consumer command encoder must explicitly wait on all command encoders that will conflict on the fence. (The GPU may start executing as many commands as it can, unless it encounters a fence.) Listing 13-3 shows the incorrect use of a fence that introduces a _race condition_.

__Listing 13-3__  Incorrect fence tracking

```
id <MTLFence> fence = [_device newFence];
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];

// Producer 1
id <MTLRenderCommandEncoder> producerCommandEncoder1 = [commandBuffer renderCommandEncoderWithDescriptor:_descriptor];
/* Draw using resources associated with 'fence' */
[producerCommandEncoder1 endEncoding];

// Producer 2
id <MTLComputeCommandEncoder> producerCommandEncoder2 = [commandBuffer computeCommandEncoder];
/* Encode */
[producerCommandEncoder2 updateFence:fence];
[producerCommandEncoder2 endEncoding];

// Race condition at consumption!
// producerCommandEncoder2 updated the fence and will have completed its work
// producerCommandEncoder1 did not update the fence and therefore there is no guarantee that it will have completed its work
// Consumer
id <MTLComputeCommandEncoder> computeCommandEncoder = [commandBuffer computeCommandEncoder];
[computeCommandEncoder waitForFence:fence];
/* Dispatch using resources associated with 'fence' */
[computeCommandEncoder endEncoding];

[commandBuffer commit];
```

You are still responsible for sequencing command buffer submission queues, as shown in Listing 13-4. However, fences do not allow you to control inter-queue command buffer sequencing.

__Listing 13-4__  Sequencing fences across command buffer submission queues

```
id <MTLFence> fence = [_device newFence];
id <MTLCommandBuffer> commandBuffer0 = [_commandQueue0 commandBuffer];
id <MTLCommandBuffer> commandBuffer1 = [_commandQueue1 commandBuffer];

// Producer
id <MTLRenderCommandEncoder> renderCommandEncoder = [commandBuffer0 renderCommandEncoderWithDescriptor:_descriptor];
/* Draw using resources associated with 'fence' */
[renderCommandEncoder updateFence:fence afterStages:MTLRenderStageFragment];
[renderCommandEncoder endEncoding];

// Consumer
id <MTLComputeCommandEncoder> computeCommandEncoder = [commandBuffer1 computeCommandEncoder];
[computeCommandEncoder waitForFence:fence];
/* Dispatch using resources associated with 'fence' */
[computeCommandEncoder endEncoding];

// Ensure 'commandBuffer0' is scheduled before 'commandBuffer1'
[commandBuffer0 addScheduledHandler:^(id <MTLCommandBuffer>) {
    [commandBuffer1 commit];
}];
[commandBuffer0 commit];
```


Some devices cannot alias sub-allocated resources arbitrarily; for example, compressible depth textures and MSAA textures. You should create a different heap for each type of render target: color, depth, stencil, and MSAA.

When making a sub-allocated resource aliasable, you must assume that this resource will alias against all future heap sub-allocations. If you later allocate non-aliasable resources, such as longer-lived textures, then those resources could alias against your temporary resources, and become very difficult to track correctly.

Tracking what aliases, and what does not, can be significantly easier if you keep at least two resource heaps: one for aliasable resources (for example, render targets), and one for non-aliasable resources (for example, asset textures or vertex buffers).

Creating or deleting many sub-allocated resources of different sizes may fragment memory. Defragmentation requires you to explicitly copy from the fragmented heap to another heap. Alternatively, you can create multiple heaps dedicated to sub-allocated resources of similar size.

Heaps can also be used a stack. When used as a stack, fragmentation cannot occur.

Fine-grained fences are difficult to manage and they reduce the tracking benefits of heaps. Avoid using a fence per sub-allocated resource; instead, use a single fence to track all sub-allocated resources with identical synchronization requirements.

Manual data hazard tracking is extended to resources created directly from a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object. Specify the new [MTLResourceHazardTrackingModeUntracked](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcehazardtrackingmodeuntracked) resource option when creating the resource, then track it with fences. Manual tracking may reduce the automatic tracking overhead of many read-only resources.

For an example of how to use heaps and fences, see the `MetalHeapsAndFences` sample.

[Next](Document%20Revision%20History.md)[Previous](Tessellation.md)

