---
title: 'executeCommandsInBuffer(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer%28_%3Arange%3A%29.json'
content_hash: 'sha256:9dce97d915eae9a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# executeCommandsInBuffer(_:range:)

<sub>Instance Method</sub>

Encodes a command that runs a range of commands from an indirect command buffer (ICB).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func executeCommandsInBuffer(_ buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer` — An [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance that contains other commands the current command runs.

- `range` — A span of integers that represent the command entries in `buffer` the current command runs. When running on Metal devices that belong to the [MTLGPUFamilyMac2](../mtlgpufamily/mac2.md) GPU family, the number of commands needs to be less than or equal to 0x4000 (16,384). Metal devices that belong to an Apple silicon family, such as [MTLGPUFamilyApple10](../mtlgpufamily/apple10.md), don’t have this limitation.

## See Also

### Running commands from indirect command buffers

- [executeCommandsInBuffer(_:indirectBuffer:offset:)](<executecommandsinbuffer(__indirectbuffer_offset_).md>) — Encodes a command that runs an indirect range of commands from an indirect command buffer (ICB).
