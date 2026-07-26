---
title: 'executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer:indirectbuffer:indirectbufferoffset:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer:indirectbuffer:indirectbufferoffset:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer%3Aindirectbuffer%3Aindirectbufferoffset%3A.json'
content_hash: 'sha256:eb42aef59311fcf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:

<sub>Instance Method</sub>

Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) executeCommandsInBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandbuffer indirectBuffer:(id<MTLBuffer>) indirectRangeBuffer indirectBufferOffset:(NSUInteger) indirectBufferOffset;
```

## Parameters

- `indirectCommandbuffer` — The [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance containing the commands to execute.

- `indirectRangeBuffer` — An indirect buffer containing the execution range, laid out in an [MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrange.md) instance. The maximum length of the range is `16384` commands.

- `indirectBufferOffset` — The number of bytes from the start of `indirectRangeBuffer` containing the execution range to use. Align the offset on a multiple of `4`.

## See Also

### Dispatching from indirect command buffers

- [- dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:](<dispatchthreadgroups(indirectbuffer_indirectbufferoffset_threadsperthreadgroup_).md>) — Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [executeCommandsInBuffer:withRange:](executecommandsinbuffer_withrange_.md) — Encodes an instruction to run commands from an indirect buffer.
