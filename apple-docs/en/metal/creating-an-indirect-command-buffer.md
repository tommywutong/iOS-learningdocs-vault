---
title: Creating an indirect command buffer
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/creating-an-indirect-command-buffer
source_url: 'https://developer.apple.com/documentation/metal/creating-an-indirect-command-buffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/creating-an-indirect-command-buffer.json'
content_hash: 'sha256:019faf5c290c9491'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Indirect command encoding](indirect-command-encoding.md)

# Creating an indirect command buffer

<sub>Article</sub>

Configure a descriptor to specify the properties of an indirect command buffer.

## Overview

An indirect command buffer stores encoded GPU commands persistently. Using an indirect command buffer, you can encode a command once and reuse it multiple times. You can also encode commands into an indirect command buffer simultaneously with multiple threads on the CPU or with a compute kernel on the GPU.

To create an indirect command buffer, first create an [MTLIndirectCommandBufferDescriptor](mtlindirectcommandbufferdescriptor.md) instance and configure the descriptor’s properties. Then call [- newIndirectCommandBufferWithDescriptor:maxCommandCount:options:](<mtldevice/makeindirectcommandbuffer(descriptor_maxcommandcount_options_).md>) on an [MTLDevice](mtldevice.md) instance to create the indirect command buffer.

## See Also

### Indirect command buffers

- [Specifying drawing and dispatch arguments indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md) — Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Encoding indirect command buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md) — Reduce CPU overhead and simplify your command execution by reusing commands.
- [Encoding indirect command buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md) — Maximize CPU to GPU parallelization by generating render commands on the GPU.
- [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md) — A command buffer containing reusable commands, encoded either on the CPU or GPU.
- [MTLIndirectCommandBufferDescriptor](mtlindirectcommandbufferdescriptor.md) — A configuration you create to customize an indirect command buffer.
- [MTLIndirectCommandType](mtlindirectcommandtype.md) — The types of commands that you can encode into the indirect command buffer.
- [MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrange.md) — A range of commands in an indirect command buffer.
- [MTLIndirectCommandBufferExecutionRangeMake](<mtlindirectcommandbufferexecutionrangemake(____).md>) — Creates a command execution range.
