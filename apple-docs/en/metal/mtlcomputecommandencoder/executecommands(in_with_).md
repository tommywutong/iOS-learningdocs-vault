---
title: 'executeCommands(in:with:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（14.0 起废弃）, iPadOS 13.0+（14.0 起废弃）, tvOS 13.0+（14.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlcomputecommandencoder/executecommands(in:with:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommands(in:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/executecommands%28in%3Awith%3A%29.json'
content_hash: 'sha256:b428bd149a49fac6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# executeCommands(in:with:)

<sub>Instance Method</sub>

Encodes an instruction to run commands from an indirect buffer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func executeCommands(in indirectCommandBuffer: any MTLIndirectCommandBuffer, with executionRange: NSRange)
```

## Parameters

- `indirectCommandBuffer` — The [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance containing the commands to execute.

- `executionRange` — The range of commands to execute. The maximum length of the range is `16384` commands.

## See Also

### Dispatching from indirect command buffers

- [- dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:](<dispatchthreadgroups(indirectbuffer_indirectbufferoffset_threadsperthreadgroup_).md>) — Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [executeCommandsInBuffer(_:range:)](<executecommandsinbuffer(__range_).md>) — Encodes an instruction to run commands from an indirect buffer.
- [executeCommandsInBuffer(_:indirectBuffer:offset:)](<executecommandsinbuffer(__indirectbuffer_offset_).md>) — Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [executeCommands(in:indirectBuffer:indirectBufferOffset:)](<executecommands(in_indirectbuffer_indirectbufferoffset_).md>) — Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
