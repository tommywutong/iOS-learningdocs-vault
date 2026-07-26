---
title: MTLCommandBuffer
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer.json'
content_hash: 'sha256:07d2724fdf5a95e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommandBuffer

<sub>Protocol</sub>

A container that stores a sequence of GPU commands that you encode into it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLCommandBuffer : NSObjectProtocol
```

## Overview

A command buffer represents a chunk of work for the GPU that stores the commands you encode to it, as well as any resources those commands need. You primarily use a command buffer to:

- Create command encoders and call their methods to add commands to the buffer
- Optionally reserve a place for the command buffer in its command queue by _enqueuing_ the command buffer, even before you encode any commands into it
- Submit, or commit_,_ the contents of the command buffer to the command queue that creates it to run on the GPU device the queue represents

Create a command encoder from an [MTLCommandQueue](mtlcommandqueue.md) instance by calling its [- commandBuffer](<mtlcommandqueue/makecommandbuffer().md>) method. Typically, you create one or more command queues when your app launches and then keep them throughout your app’s lifetime.

To add commands to an [MTLCommandBuffer](mtlcommandbuffer.md) instance, create an encoder from one of its factory methods, including:

- An [MTLRenderCommandEncoder](mtlrendercommandencoder.md) instance by calling [- renderCommandEncoderWithDescriptor:](<mtlcommandbuffer/makerendercommandencoder(descriptor_).md>)
- An [MTLComputeCommandEncoder](mtlcomputecommandencoder.md) instance by calling [- computeCommandEncoderWithDispatchType:](<mtlcommandbuffer/makecomputecommandencoder(dispatchtype_).md>)
- An [MTLBlitCommandEncoder](mtlblitcommandencoder.md) instance by calling [- blitCommandEncoder](<mtlcommandbuffer/makeblitcommandencoder().md>) or [- blitCommandEncoderWithDescriptor:](<mtlcommandbuffer/makeblitcommandencoder(descriptor_).md>)
- An [MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md) instance by calling [- parallelRenderCommandEncoderWithDescriptor:](<mtlcommandbuffer/makeparallelrendercommandencoder(descriptor_).md>)

> [!note] Note
> All encoders inherit additional methods from the [MTLCommandEncoder](mtlcommandencoder.md).

You can use only a single encoder at a time to add commands to a command buffer. To start using a different command encoder, first signal that you’re done with the current encoder by calling its [- endEncoding](<mtlcommandencoder/endencoding().md>) method. Then create another command encoder from the command buffer and continue adding commands to the buffer with the new encoder.

Repeat the process until you finish encoding commands to the command buffer and are ready to run the buffer’s contents on the GPU. Then submit the command buffer to the command queue that you used to create it by calling the command buffer’s [- commit](<mtlcommandbuffer/commit().md>) method. After an app commits a command buffer, you check its [status](mtlcommandbuffer/status.md) property or block a thread by calling its [- waitUntilScheduled](<mtlcommandbuffer/waituntilscheduled().md>) or [- waitUntilCompleted](<mtlcommandbuffer/waituntilcompleted().md>) methods.

You also have the option to reserve a place for the command buffer in its command queue by calling the command buffer’s [- enqueue](<mtlcommandbuffer/enqueue().md>) method. You can call this method exactly once at any time before you commit the buffer to the queue. If you don’t enqueue a command buffer, it implicitly enqueues itself when you commit it. Each command queue ensures the order that you enqueue its command buffers is the same order the queue schedules them to run on the GPU.

> [!tip] Tip
> Establish an order of execution for multiple command buffers you encode in parallel by first calling their [- enqueue](<mtlcommandbuffer/enqueue().md>) methods in that order.

For example, a multithreaded app might set the GPU’s execution order for a sequence of related subtasks by:

1. Creating a command buffer for each subtask
2. Enqueuing the command buffers in the proper order on a single thread
3. Encoding commands to each buffer on a separate thread and then committing it

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating command encoders

- [Command encoder factory methods](command-encoder-factory-methods.md) — A command encoder defines the actions of a single pass, such as GPU commands that draw, compute, or quickly copy resource data.

### Attaching residency sets

- [- useResidencySet:](<mtlcommandbuffer/useresidencyset(__).md>) — Applies a residency set to a command buffer.
- [useResidencySets(_:)](<mtlcommandbuffer/useresidencysets(__).md>) — Applies multiple residency sets to a command buffer.

### Synchronizing passes with events

- [- encodeWaitForEvent:value:](<mtlcommandbuffer/encodewaitforevent(__value_).md>) — Encodes a command into the command buffer that pauses the GPU from running the buffer’s subsequent passes until the event equals or exceeds a value.
- [- encodeSignalEvent:value:](<mtlcommandbuffer/encodesignalevent(__value_).md>) — Encodes a command that updates an event’s value, which can clear the GPU to run passes from other command buffers waiting for the event.

### Presenting a drawable

- [- presentDrawable:](<mtlcommandbuffer/present(__).md>) — Presents a drawable as early as possible.
- [- presentDrawable:atTime:](<mtlcommandbuffer/present(__attime_).md>) — Presents a drawable at a specific time.
- [- presentDrawable:afterMinimumDuration:](<mtlcommandbuffer/present(__afterminimumduration_).md>) — Presents a drawable after the system presents the previous drawable for an amount of time.

### Registering state change handlers

- [- addScheduledHandler:](<mtlcommandbuffer/addscheduledhandler(__).md>) — Registers a completion handler the GPU device calls immediately after it schedules the command buffer to run on the GPU.
- [- addCompletedHandler:](<mtlcommandbuffer/addcompletedhandler(__).md>) — Registers a completion handler the GPU device calls immediately after the GPU finishes running the commands in the command buffer.
- [MTLCommandBufferHandler](mtlcommandbufferhandler.md) — A completion handler signature a GPU device calls when it finishes scheduling a command buffer, or when the GPU finishes running it.

### Submitting a command buffer

- [- enqueue](<mtlcommandbuffer/enqueue().md>) — Reserves the next available place for the command buffer in its command queue.
- [- commit](<mtlcommandbuffer/commit().md>) — Submits the command buffer to run on the GPU.

### Waiting for state changes

- [- waitUntilScheduled](<mtlcommandbuffer/waituntilscheduled().md>) — Blocks the current thread until the command queue schedules the buffer.
- [- waitUntilCompleted](<mtlcommandbuffer/waituntilcompleted().md>) — Blocks the current thread until the GPU finishes executing the command buffer and all of its completion handlers.

### Troubleshooting a command buffer

- [status](mtlcommandbuffer/status.md) — The command buffer’s current state.
- [MTLCommandBufferStatus](mtlcommandbufferstatus.md) — The discrete states for a command buffer that represent its life cycle stages.
- [Command buffer debugging](command-buffer-debugging.md) — Properties and methods for programmatically debugging runtime issues with a command buffer.

### Instance Methods

- [completed()](<mtlcommandbuffer/completed().md>)
- [scheduled()](<mtlcommandbuffer/scheduled().md>)

## See Also

### Submitting work to a GPU with Metal

- [Setting up a command structure](setting-up-a-command-structure.md) — Discover how Metal executes commands on a GPU.
- [MTLCommandQueue](mtlcommandqueue.md) — An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.
- [MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md) — A configuration that customizes the behavior for a new command queue.
- [MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md) — A configuration that customizes the behavior for a new command buffer.
- [MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md) — The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [MTLCommandEncoder](mtlcommandencoder.md) — An encoder that writes GPU commands into a command buffer.
