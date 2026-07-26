---
title: 'executeCommands(buffer:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/executecommands(buffer:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/executecommands(buffer:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/executecommands%28buffer%3Arange%3A%29.json'
content_hash: 'sha256:e22ab239c33d0efb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# executeCommands(buffer:range:)

<sub>Instance Method</sub>

Encodes a command to execute commands from an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func executeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer` — An [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance that contains other commands the current command runs.

- `range` — A span of integers that represent the command entries in buffer the current command runs.

## See Also

### Encoding indirect command buffers

- [- executeCommandsInBuffer:indirectBuffer:](<executecommands(buffer_indirectbuffer_).md>) — Encodes an instruction to execute commands from an indirect command buffer, using an indirect buffer for arguments.
