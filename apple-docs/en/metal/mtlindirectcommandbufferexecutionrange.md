---
title: MTLIndirectCommandBufferExecutionRange
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandbufferexecutionrange
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbufferexecutionrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbufferexecutionrange.json'
content_hash: 'sha256:6118a46e9b4b9d54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIndirectCommandBufferExecutionRange

<sub>Structure</sub>

A range of commands in an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLIndirectCommandBufferExecutionRange
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a command execution range

- [init()](<mtlindirectcommandbufferexecutionrange/init().md>) — Initializes an empty command execution range.
- [init(location:length:)](<mtlindirectcommandbufferexecutionrange/init(location_length_).md>) — Initializes an command execution range.
- [MTLIndirectCommandBufferExecutionRangeMake](<mtlindirectcommandbufferexecutionrangemake(____).md>) — Creates a command execution range.

### Examining the range

- [location](mtlindirectcommandbufferexecutionrange/location.md) — The first index in the command execution range.
- [length](mtlindirectcommandbufferexecutionrange/length.md) — The number of items in the command execution range.

## See Also

### Indirect command buffers

- [Creating an indirect command buffer](creating-an-indirect-command-buffer.md) — Configure a descriptor to specify the properties of an indirect command buffer.
- [Specifying drawing and dispatch arguments indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md) — Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Encoding indirect command buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md) — Reduce CPU overhead and simplify your command execution by reusing commands.
- [Encoding indirect command buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md) — Maximize CPU to GPU parallelization by generating render commands on the GPU.
- [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md) — A command buffer containing reusable commands, encoded either on the CPU or GPU.
- [MTLIndirectCommandBufferDescriptor](mtlindirectcommandbufferdescriptor.md) — A configuration you create to customize an indirect command buffer.
- [MTLIndirectCommandType](mtlindirectcommandtype.md) — The types of commands that you can encode into the indirect command buffer.
- [MTLIndirectCommandBufferExecutionRangeMake](<mtlindirectcommandbufferexecutionrangemake(____).md>) — Creates a command execution range.
