---
title: 'executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer:indirectbuffer:indirectbufferoffset:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer:indirectbuffer:indirectbufferoffset:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer%3Aindirectbuffer%3Aindirectbufferoffset%3A.json'
content_hash: 'sha256:05bc3f8c2fb67021'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:

<sub>Instance Method</sub>

Encodes a command that runs an indirect range of commands from an indirect command buffer (ICB).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) executeCommandsInBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandbuffer indirectBuffer:(id<MTLBuffer>) indirectRangeBuffer indirectBufferOffset:(NSUInteger) indirectBufferOffset;
```

## Parameters

- `indirectCommandbuffer` — An [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance that contains other commands the current command runs.

- `indirectRangeBuffer` — An [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrange.md) structure. The [length](../mtlindirectcommandbufferexecutionrange/length.md) property of that structure needs to be less than or equal to `0x4000` (`16,384`).

- `indirectBufferOffset` — An integer that represents the location, in bytes, from the start of `indirectRangeBuffer` where the execution range structure begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

## See Also

### Running commands from indirect command buffers

- [executeCommandsInBuffer:withRange:](executecommandsinbuffer_withrange_.md) — Encodes a command that runs a range of commands from an indirect command buffer (ICB).
