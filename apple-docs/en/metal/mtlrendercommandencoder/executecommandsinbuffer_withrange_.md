---
title: 'executeCommandsInBuffer:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer%3Awithrange%3A.json'
content_hash: 'sha256:08cab5a5defea1db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# executeCommandsInBuffer:withRange:

<sub>Instance Method</sub>

Encodes a command that runs a range of commands from an indirect command buffer (ICB).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) executeCommandsInBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) executionRange;
```

## Parameters

- `indirectCommandBuffer` — An [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance that contains other commands the current command runs.

- `executionRange` — A span of integers that represent the command entries in `buffer` the current command runs. The number of commands needs to be less than or equal to `0x4000` (`16,384`).

## See Also

### Running commands from indirect command buffers

- [executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:](executecommandsinbuffer_indirectbuffer_indirectbufferoffset_.md) — Encodes a command that runs an indirect range of commands from an indirect command buffer (ICB).
