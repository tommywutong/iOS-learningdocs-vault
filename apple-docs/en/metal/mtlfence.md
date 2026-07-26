---
title: MTLFence
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfence
source_url: 'https://developer.apple.com/documentation/metal/mtlfence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfence.json'
content_hash: 'sha256:583d0668a2a3cff4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFence

<sub>Protocol</sub>

A synchronization mechanism that orders memory operations between GPU passes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLFence : NSObjectProtocol, Sendable
```

## Overview

Create a fence by calling the [- newFence](<mtldevice/makefence().md>) method.

A fence instructs the GPU to finish running specific stages of a pass before starting stages from another pass. This is useful when a pass needs to wait before loading data from a resource until after another pass stores data to that resource. For example, to synchronize two passes where one modifies a texture and another reads it, use a fence with the following steps:

1. Encode the producing pass and update a fence after the commands that modify the texture.
2. Encode the consuming pass and wait for the same fence before the commands that read from that texture.

Apple family GPUs can update and respond to fences on a per-stage basis. This means a GPU can delay running the commands for specific stages that need to wait for another pass while it runs other stages from the same pass. For example, a GPU can run the vertex stage of a pass while the fragment stage waits until another pass updates a fence. For more information about Apple family GPUs, see the [- supportsFamily:](<mtldevice/supportsfamily(__).md>) method, and the [Metal feature set tables PDF](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) or the equivalent [Metal feature set tables spreadsheet](https://developer.apple.com/metal/Metal-Feature-Set-Tables.zip).

The following encoder types support the [- updateFence:afterEncoderStages:](<mtl4commandencoder/updatefence(__afterencoderstages_).md>) and [- waitForFence:beforeEncoderStages:](<mtl4commandencoder/waitforfence(__beforeencoderstages_).md>) methods by conforming to the [MTL4CommandEncoder](mtl4commandencoder.md) protocol:

- [MTL4RenderCommandEncoder](mtl4rendercommandencoder.md)
- [MTL4ComputeCommandEncoder](mtl4computecommandencoder.md)
- [MTL4MachineLearningCommandEncoder](mtl4machinelearningcommandencoder.md)

The encoder types that inherit the [MTLCommandEncoder](mtlcommandencoder.md) protocol each have methods for updating and waiting for fences.

| Encoder types | Update fence methods | Wait for fence methods |
|---|---|---|
| [MTLRenderCommandEncoder](mtlrendercommandencoder.md) | [- updateFence:afterStages:](<mtlrendercommandencoder/updatefence(__after_).md>) | [- waitForFence:beforeStages:](<mtlrendercommandencoder/waitforfence(__before_).md>) |
| [MTLComputeCommandEncoder](mtlcomputecommandencoder.md) | [- updateFence:](<mtlcomputecommandencoder/updatefence(__).md>) | [- waitForFence:](<mtlcomputecommandencoder/waitforfence(__).md>) |
| [MTLBlitCommandEncoder](mtlblitcommandencoder.md) | [- updateFence:](<mtlblitcommandencoder/updatefence(__).md>) | [- waitForFence:](<mtlblitcommandencoder/waitforfence(__).md>) |
| [MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md) | [- updateFence:](<mtlaccelerationstructurecommandencoder/updatefence(__).md>) | [- waitForFence:](<mtlaccelerationstructurecommandencoder/waitforfence(__).md>) |
| [MTLResourceStateCommandEncoder](mtlresourcestatecommandencoder.md) | [- updateFence:](<mtlresourcestatecommandencoder/update(__).md>) | [- waitForFence:](<mtlresourcestatecommandencoder/wait(for_).md>) |

> [!note] Note
> Earlier versions of Metal support hazard tracking for work you encode and commit with [MTLCommandEncoder](mtlcommandencoder.md), [MTLCommandBuffer](mtlcommandbuffer.md), and [MTLCommandQueue](mtlcommandqueue.md) instances, which means you don’t need to synchronize memory operations for resources with a [hazardTrackingMode](mtlresource/hazardtrackingmode.md) property that’s equal to [MTLResourceHazardTrackingModeTracked](mtlresourceoptions/hazardtrackingmodetracked.md).

### Submit producing passes before consuming passes

Send producing passes that update a fence to a queue before submitting consuming passes that wait for a fence. When encoding the producing and consuming passes into the same command buffer, encode the producing passes before the consuming passes. When submitting the producing and consuming passes in different command buffers, commit the command buffers with the producing passes before those with the consuming passes.

> [!note] Note
> When submitting multiple command buffers to an [MTL4CommandQueue](mtl4commandqueue.md) at the same time, such as with its [commit:count:options:](mtl4commandqueue/commit_count_options_.md) method, the method commits the command buffers in array order.

Fences can synchronize passes you submit to different queues, including [MTL4CommandQueue](mtl4commandqueue.md), [MTLCommandQueue](mtlcommandqueue.md), or a combination of both.

> [!tip] Tip
> Consider synchronizing passes that you submit to different queues with an [MTLEvent](mtlevent.md) instance instead.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying a fence

- [device](mtlfence/device.md) — The device object that created the fence.
- [label](mtlfence/label.md) — A string that identifies the fence.

### Selecting render stages

- [MTLRenderStages](mtlrenderstages.md) — The stages in a render pass that triggers a synchronization command.

## See Also

### Synchronizing with barriers and fences

- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md) — Block GPU stages in the a pass from running until other stages in the same pass finish.
- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md) — Block GPU stages in a pass until another pass unblocks it by signaling a fence.
- [Synchronizing passes with consumer barriers](synchronizing-passes-with-consumer-barriers.md) — Block GPU stages in a pass, and all subsequent passes, from running until stages from earlier passes finish.
- [Synchronizing passes with producer barriers](synchronizing-passes-with-producer-barriers.md) — Block GPU stages in subsequent passes from running until stages in a pass, and earlier passes, finish.
- [Synchronizing CPU and GPU work](synchronizing-cpu-and-gpu-work.md) — Avoid stalls between CPU and GPU work by using multiple instances of a resource.
- [Implementing a multistage image filter using heaps and fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md) — Use fences to synchronize access to resources allocated on a heap.
- [MTLStages](mtlstages.md) — The segments of command execution within the Metal pass types.
- [MTLRenderStages](mtlrenderstages.md) — The stages in a render pass that triggers a synchronization command.
- [MTLBarrierScope](mtlbarrierscope.md) — Describes the types of resources that a barrier operates on.
- [MTL4VisibilityOptions](mtl4visibilityoptions.md) — Memory consistency options for synchronization commands.
