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
doc_path: '/documentation/metal/mtl4rendercommandencoder/executecommands(buffer:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/executecommands(buffer:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/executecommands%28buffer%3Arange%3A%29.json'
content_hash: 'sha256:7826cf10c2f5747d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# executeCommands(buffer:range:)

<sub>Instance Method</sub>

Encodes a command that runs a range of commands from an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func executeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer` — An [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance that contains other commands the current command runs.

- `range` — A span of integers that represent the command entries in buffer the current command runs.

## See Also

### Running commands from indirect command buffers

- [- executeCommandsInBuffer:indirectBuffer:](<executecommands(buffer_indirectbuffer_).md>) — Encodes a command that runs an indirect range of commands from an indirect command buffer.
