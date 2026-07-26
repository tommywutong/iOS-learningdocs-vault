---
title: 'executeCommandsInBuffer(_:indirectBuffer:offset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer%28_%3Aindirectbuffer%3Aoffset%3A%29.json'
content_hash: 'sha256:03b495d1dfbe587a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# executeCommandsInBuffer(_:indirectBuffer:offset:)

<sub>Instance Method</sub>

Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func executeCommandsInBuffer(_ buffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: any MTLBuffer, offset: Int)
```

## Parameters

- `buffer` — The [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance containing the commands to execute.

- `indirectRangeBuffer` — An [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrange.md) structure. When running on Metal devices that belong to the [MTLGPUFamilyMac2](../mtlgpufamily/mac2.md) GPU family, the maximum value for the [length](../mtlindirectcommandbufferexecutionrange/length.md) property of that structure is 0x4000 (16,384). Metal devices that belong to an Apple silicon family, such as [MTLGPUFamilyApple10](../mtlgpufamily/apple10.md), don’t have this limitation.

- `offset` — The number of bytes from the start of `indirectRangeBuffer` containing the execution range to use. Align the offset on a multiple of `4`.

## See Also

### Dispatching from indirect command buffers

- [- dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:](<dispatchthreadgroups(indirectbuffer_indirectbufferoffset_threadsperthreadgroup_).md>) — Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [executeCommandsInBuffer(_:range:)](<executecommandsinbuffer(__range_).md>) — Encodes an instruction to run commands from an indirect buffer.
- [executeCommands(in:indirectBuffer:indirectBufferOffset:)](<executecommands(in_indirectbuffer_indirectbufferoffset_).md>) — Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [executeCommands(in:with:)](<executecommands(in_with_).md>) — Encodes an instruction to run commands from an indirect buffer.
