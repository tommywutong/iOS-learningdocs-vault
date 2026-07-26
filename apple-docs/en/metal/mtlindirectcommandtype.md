---
title: MTLIndirectCommandType
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandtype
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandtype.json'
content_hash: 'sha256:886e7859d9417042'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIndirectCommandType

<sub>Structure</sub>

The types of commands that you can encode into the indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLIndirectCommandType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Creating a set of command types

- [init(rawValue:)](<mtlindirectcommandtype/init(rawvalue_).md>) — Initializes the set of command types from a raw integer value.

### Specifying command types

- [MTLIndirectCommandTypeDraw](mtlindirectcommandtype/draw.md) — A draw call command.
- [MTLIndirectCommandTypeDrawIndexed](mtlindirectcommandtype/drawindexed.md) — An indexed draw call command.
- [MTLIndirectCommandTypeDrawPatches](mtlindirectcommandtype/drawpatches.md) — A draw call command for tessellated patches.
- [MTLIndirectCommandTypeDrawIndexedPatches](mtlindirectcommandtype/drawindexedpatches.md) — An indexed draw call command for tessellated patches.
- [MTLIndirectCommandTypeConcurrentDispatch](mtlindirectcommandtype/concurrentdispatch.md) — A compute command using a grid aligned to threadgroup boundaries.
- [MTLIndirectCommandTypeConcurrentDispatchThreads](mtlindirectcommandtype/concurrentdispatchthreads.md) — A compute command using an arbitrarily sized grid.

### Type Properties

- [MTLIndirectCommandTypeDrawMeshThreadgroups](mtlindirectcommandtype/drawmeshthreadgroups.md)
- [MTLIndirectCommandTypeDrawMeshThreads](mtlindirectcommandtype/drawmeshthreads.md)

## See Also

### Indirect command buffers

- [Creating an indirect command buffer](creating-an-indirect-command-buffer.md) — Configure a descriptor to specify the properties of an indirect command buffer.
- [Specifying drawing and dispatch arguments indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md) — Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Encoding indirect command buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md) — Reduce CPU overhead and simplify your command execution by reusing commands.
- [Encoding indirect command buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md) — Maximize CPU to GPU parallelization by generating render commands on the GPU.
- [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md) — A command buffer containing reusable commands, encoded either on the CPU or GPU.
- [MTLIndirectCommandBufferDescriptor](mtlindirectcommandbufferdescriptor.md) — A configuration you create to customize an indirect command buffer.
- [MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrange.md) — A range of commands in an indirect command buffer.
- [MTLIndirectCommandBufferExecutionRangeMake](<mtlindirectcommandbufferexecutionrangemake(____).md>) — Creates a command execution range.
