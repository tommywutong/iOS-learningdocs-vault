---
title: MTLResidencySet
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencyset
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset.json'
content_hash: 'sha256:0054ed15b70754e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLResidencySet

<sub>Protocol</sub>

A collection of resource allocations that can move in and out of resident memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLResidencySet : NSObjectProtocol
```

## Overview

Residency sets are a way you can tell Metal which resource allocations, such as buffers, textures, and heaps, to make _resident_, or GPU-accessible. Adding allocations to a residency set requires less overhead than the equivalent methods of a command encoder. Residency sets also give you more control when Metal makes their allocations resident, and for how long they remain resident. However, residency sets don’t track hazards, so you need to account for hazards with fences and events.

You can change which [MTLAllocation](mtlallocation.md) instances are in a residency set at any time by:

1. Staging additions and removals with the [- addAllocation:](<mtlresidencyset/addallocation(__).md>) and [- removeAllocation:](<mtlresidencyset/removeallocation(__).md>) methods, respectively, or with their sibling methods
2. Applying staged changes by calling the residency set’s [- commit](<mtlresidencyset/commit().md>) method

Metal doesn’t synchronize the state of the residency set between the CPU and the GPU. This means you can add resource allocations to the set while the GPU is actively running a command buffer that’s accessing them.

> [!important] Important
> If there’s a resource in a residency set that the GPU no longer needs access to, you can remove that resource from the residency set, even while the GPU is actively accessing other resources from the same residency set.

Metal makes the union of all residency sets’ allocations resident. This means each resource allocation, such as a buffer, can have an entry in multiple residency sets at the same time. Removing an allocation from one residency set doesn’t affect its residency if it also has an entry in another residency set. So you can remove an entire residency set from a command queue and only remove the allocations from residency that are unique to that set. All other resource allocations remain in residency because at least one other residency set has an entry for each.

Alternatively, render and compute command encoders have the following methods that make resource allocations resident:

| [MTLRenderCommandEncoder](mtlrendercommandencoder.md) | [MTLComputeCommandEncoder](mtlcomputecommandencoder.md) |
|---|---|
| [- useResource:usage:stages:](<mtlrendercommandencoder/useresource(__usage_stages_).md>) | [- useResource:usage:](<mtlcomputecommandencoder/useresource(__usage_).md>) |
| [useResources(_:usage:stages:)](<mtlrendercommandencoder/useresources(__usage_stages_).md>) | [useResources(_:usage:)](<mtlcomputecommandencoder/useresources(__usage_).md>) |
| [- useHeap:stages:](<mtlrendercommandencoder/useheap(__stages_).md>) | [- useHeap:](<mtlcomputecommandencoder/useheap(__).md>) |
| [useHeaps(_:stages:)](<mtlrendercommandencoder/useheaps(__stages_).md>) | [useHeaps(_:)](<mtlcomputecommandencoder/useheaps(__).md>) |

These command encoder methods:

- Support hazard tracking to applicable resources (see [Resource fundamentals](resource-fundamentals.md))
- Require CPU overhead for each resource or heap, which scale up with each one you add
- Apply to a single command encoder, which means you need to call the methods again for the same resources for each command encoder

Residency sets, by contrast:

- Don’t support hazard tracking, which means you need to account for hazards with [MTLFence](mtlfence.md) and [MTLEvent](mtlevent.md) instances
- Require minimal CPU overhead by aggregating allocations at little to no cost for each resource or heap
- Can attach to a command buffer with a single call, which makes residency set’s allocations available to all of that command buffer’s encoders
- Can attach to a command queue with a single call

Metal attaches all of a command queue’s residency sets to a command buffer from that queue when you call the command buffer’s [- commit](<mtlcommandbuffer/commit().md>) method.

> [!important] Important
> Residency sets don’t support sparse heaps or sparse textures, and their methods aren’t thread-safe.

See [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md) for information about associating a residency set to command buffers and command queues.

### Create a residency set

Make a residency set by configuring an [MTLResidencySetDescriptor](mtlresidencysetdescriptor.md) instance and passing it to the [- newResidencySetWithDescriptor:error:](<mtldevice/makeresidencyset(descriptor_).md>) method of an [MTLDevice](mtldevice.md).

**Swift**

```swift
let setDescriptor = MTLResidencySetDescriptor()
setDescriptor.label = "Primary residency set"
setDescriptor.initialCapacity = 42

let residencySet = try device.makeResidencySet(descriptor: setDescriptor)
```

**Objective-C**

```objective-c
MTLResidencySetDescriptor *setDescriptor;
setDescriptor = [[MTLResidencySetDescriptor alloc] init];
setDescriptor.label = @"Primary residency set";
setDescriptor.initialCapacity = 42;

NSError *error;
id<MTLResidencySet> residencySet;
residencySet = [device newResidencySetWithDescriptor:setDescriptor
                                               error:&error];
```

### Add allocations to a residency set

Add individual resource allocations to a residency set by calling [- addAllocation:](<mtlresidencyset/addallocation(__).md>), or add multiple allocations with [addAllocations(_:)](<mtlresidencyset/addallocations(__).md>).

**Swift**

```swift
let residencySet = try device.makeResidencySet(descriptor: setDescriptor)

residencySet.addAllocation(buffer0)
residencySet.addAllocation(buffer1)
residencySet.addAllocation(texture0)
residencySet.addAllocation(texture1)
residencySet.addAllocation(heap)

let allocations = [buffer2,
                   texture2,
                   argumentBufferHeap,
                   textureHeap]

residencySet.addAllocations(allocations)
```

**Objective-C**

```objective-c
[residencySet addAllocation:buffer0];
[residencySet addAllocation:buffer1];
[residencySet addAllocation:texture0];
[residencySet addAllocation:texture1];
[residencySet addAllocation:heap];

id<MTLAllocation> allocations[] = {
    buffer2,
    texture2,
    argumentBufferHeap,
    textureHeap
};

[residencySet addAllocations:allocations
                       count:4];
```

The residency set can handle redundant entries for the same allocation because it ignores duplicates that already have an entry in the set.

> [!important] Important
> Adding a resource, such as a buffer or texture, that originates from a heap to a residency set makes its entire heap resident.

### Remove allocations from a residency set

Remove individual resource allocations from a residency set by calling [- removeAllocation:](<mtlresidencyset/removeallocation(__).md>), or remove multiple allocations with [removeAllocations(_:)](<mtlresidencyset/removeallocations(__).md>).

**Swift**

```swift
residencySet.removeAllocation(buffer1)
residencySet.removeAllocations( [argumentBufferHeap, textureHeap] )
```

**Objective-C**

```objective-c
[residencySet removeAllocation:buffer1];

id<MTLAllocation> deallocations[] = {
    argumentBufferHeap,
    textureHeap
};

[residencySet removeAllocations: deallocations
                          count:2];
[residencySet commit];
```

Like the methods that add resource allocations to the set, these methods aggregate removals with little CPU overhead. So you can call the methods multiple times without adversely affecting runtime performance.

### Commit the changes to a residency set

Apply the updates to a residency set by calling its [- commit](<mtlresidencyset/commit().md>) method.

**Swift**

```objective-c
residencySet.commit()
```

**Objective-C**

```swift
[residencySet commit];
```

A residency set’s addition and removal methods don’t take effect until you call this method.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Adding allocations

- [- addAllocation:](<mtlresidencyset/addallocation(__).md>) — Stages a single resource to join the residency set’s list of allocations.
- [addAllocations(_:)](<mtlresidencyset/addallocations(__).md>) — Stages multiple resources to join the residency set’s list of allocations.

### Removing allocations

- [- removeAllAllocations](<mtlresidencyset/removeallallocations().md>) — Stages all the resources in the residency set to leave its list of allocations.
- [- removeAllocation:](<mtlresidencyset/removeallocation(__).md>) — Stages a single resource to leave the residency set’s list of allocations.
- [removeAllocations(_:)](<mtlresidencyset/removeallocations(__).md>) — Stages multiple resources to leave the residency set’s list of allocations.

### Finalizing pending allocation changes

- [- commit](<mtlresidencyset/commit().md>) — Applies any pending additions to and removals from the residency set.

### Requesting residency for the allocations

- [- requestResidency](<mtlresidencyset/requestresidency().md>) — Tells Metal to do as much preparatory work as it can, with the system’s current conditions, to make the set’s resource allocations resident.

### Releasing the allocations from residency

- [- endResidency](<mtlresidencyset/endresidency().md>) — Informs Metal that the residency set’s allocations no longer need to be resident, and that it can reuse the memory for other allocations.

### Inspecting a residency set

- [label](mtlresidencyset/label.md) — An optional name that can help you identify the residency set.
- [device](mtlresidencyset/device.md) — The Metal device that owns the residency set.
- [- containsAllocation:](<mtlresidencyset/containsallocation(__).md>) — Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.
- [allAllocations](mtlresidencyset/allallocations.md) — The residency set’s current list of resource allocations.
- [allocationCount](mtlresidencyset/allocationcount.md) — The number of resource allocations in the residency set.
- [allocatedSize](mtlresidencyset/allocatedsize.md) — The amount of resident memory, in bytes, the residency set’s resource allocations consume.

## See Also

### Residency sets

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md) — Organize your resources into groups and influence when they become accessible to the GPU.
- [MTLResidencySetDescriptor](mtlresidencysetdescriptor.md) — A configuration that customizes the behavior for a residency set.
