---
title: 'executeCommands(in:indirectBuffer:indirectBufferOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（14.0 起废弃）, iPadOS 13.0+（14.0 起废弃）, tvOS 13.0+（14.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlcomputecommandencoder/executecommands(in:indirectbuffer:indirectbufferoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommands(in:indirectbuffer:indirectbufferoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/executecommands%28in%3Aindirectbuffer%3Aindirectbufferoffset%3A%29.json'
content_hash: 'sha256:09dc963931466606'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# executeCommands(in:indirectBuffer:indirectBufferOffset:)

<sub>Instance Method</sub>

Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func executeCommands(in indirectCommandbuffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

## Parameters

- `indirectCommandbuffer` — The [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance containing the commands to execute.

- `indirectRangeBuffer` — An indirect buffer containing the execution range, laid out in an [MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrange.md) instance. The maximum length of the range is `16384` commands.

- `indirectBufferOffset` — The number of bytes from the start of `indirectRangeBuffer` containing the execution range to use. Align the offset on a multiple of `4`.

## See Also

### Dispatching from indirect command buffers

- [- dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:](<dispatchthreadgroups(indirectbuffer_indirectbufferoffset_threadsperthreadgroup_).md>) — Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [executeCommandsInBuffer(_:range:)](<executecommandsinbuffer(__range_).md>) — Encodes an instruction to run commands from an indirect buffer.
- [executeCommandsInBuffer(_:indirectBuffer:offset:)](<executecommandsinbuffer(__indirectbuffer_offset_).md>) — Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [executeCommands(in:with:)](<executecommands(in_with_).md>) — Encodes an instruction to run commands from an indirect buffer.
