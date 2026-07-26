---
title: 'executeCommandsInBuffer(_:indirectBuffer:offset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer%28_%3Aindirectbuffer%3Aoffset%3A%29.json'
content_hash: 'sha256:08bf936af5607186'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# executeCommandsInBuffer(_:indirectBuffer:offset:)

<sub>Instance Method</sub>

Encodes a command that runs an indirect range of commands from an indirect command buffer (ICB).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func executeCommandsInBuffer(_ buffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: any MTLBuffer, offset: Int)
```

## Parameters

- `buffer` — An [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance that contains other commands the current command runs.

- `indirectRangeBuffer` — An [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrange.md) structure. When running on Metal devices that belong to the [MTLGPUFamilyMac2](../mtlgpufamily/mac2.md) GPU family, the maximum value for the [length](../mtlindirectcommandbufferexecutionrange/length.md) property of that structure is 0x4000 (16,384). Metal devices that belong to an Apple silicon family, such as [MTLGPUFamilyApple10](../mtlgpufamily/apple10.md), don’t have this limitation.

- `offset` — An integer that represents the location, in bytes, from the start of `indirectRangeBuffer` where the execution range structure begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

## See Also

### Running commands from indirect command buffers

- [executeCommandsInBuffer(_:range:)](<executecommandsinbuffer(__range_).md>) — Encodes a command that runs a range of commands from an indirect command buffer (ICB).
