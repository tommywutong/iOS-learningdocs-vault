---
title: MTLIndirectCommandBuffer
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbuffer.json'
content_hash: 'sha256:34810dc2be5cf0e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIndirectCommandBuffer

<sub>Protocol</sub>

A command buffer containing reusable commands, encoded either on the CPU or GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLIndirectCommandBuffer : MTLResource
```

## Overview

Use an indirect command buffer to encode commands once and reuse them, and to encode commands on multiple CPU or GPU threads.

Don’t implement this protocol yourself; instead, create an [MTLIndirectCommandBufferDescriptor](mtlindirectcommandbufferdescriptor.md) instance, configure its properties, and tell the [MTLDevice](mtldevice.md) to create the indirect command buffer. See [Creating an indirect command buffer](creating-an-indirect-command-buffer.md).

## Relationships

- **Inherits From**: [MTLAllocation](mtlallocation.md), [MTLResource](mtlresource.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Determining the maximum number of commands

- [size](mtlindirectcommandbuffer/size.md) — The number of commands contained in the indirect command buffer.

### Retrieving commands

- [- indirectRenderCommandAtIndex:](<mtlindirectcommandbuffer/indirectrendercommandat(__).md>) — Gets the render command at the given index.
- [- indirectComputeCommandAtIndex:](<mtlindirectcommandbuffer/indirectcomputecommandat(__).md>) — Gets the compute command at the given index.
- [indirectComputeCommand(at:)](<mtlindirectcommandbuffer/indirectcomputecommand(at_).md>) — Gets the compute command at the given index.

### Resetting commands

- [reset(_:)](<mtlindirectcommandbuffer/reset(__).md>) — Resets a range of commands to their default state.

### Instance Properties

- [gpuResourceID](mtlindirectcommandbuffer/gpuresourceid.md)

## See Also

### Indirect command buffers

- [Creating an indirect command buffer](creating-an-indirect-command-buffer.md) — Configure a descriptor to specify the properties of an indirect command buffer.
- [Specifying drawing and dispatch arguments indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md) — Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Encoding indirect command buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md) — Reduce CPU overhead and simplify your command execution by reusing commands.
- [Encoding indirect command buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md) — Maximize CPU to GPU parallelization by generating render commands on the GPU.
- [MTLIndirectCommandBufferDescriptor](mtlindirectcommandbufferdescriptor.md) — A configuration you create to customize an indirect command buffer.
- [MTLIndirectCommandType](mtlindirectcommandtype.md) — The types of commands that you can encode into the indirect command buffer.
- [MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrange.md) — A range of commands in an indirect command buffer.
- [MTLIndirectCommandBufferExecutionRangeMake](<mtlindirectcommandbufferexecutionrangemake(____).md>) — Creates a command execution range.
