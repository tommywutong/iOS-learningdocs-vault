---
title: 'resetCommands(buffer:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/resetcommands(buffer:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/resetcommands(buffer:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/resetcommands%28buffer%3Arange%3A%29.json'
content_hash: 'sha256:77007c0cf0854191'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# resetCommands(buffer:range:)

<sub>Instance Method</sub>

Encodes a command that resets a range of commands in an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func resetCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer` — An [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) the command resets.

- `range` — A range of commands within `buffer`.
