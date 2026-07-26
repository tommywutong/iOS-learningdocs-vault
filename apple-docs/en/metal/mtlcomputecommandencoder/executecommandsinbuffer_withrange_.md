---
title: 'executeCommandsInBuffer:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/executecommandsinbuffer%3Awithrange%3A.json'
content_hash: 'sha256:eccc56dfdad2c027'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# executeCommandsInBuffer:withRange:

<sub>Instance Method</sub>

Encodes an instruction to run commands from an indirect buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) executeCommandsInBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) executionRange;
```

## Parameters

- `indirectCommandBuffer` — The [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance containing the commands to execute.

- `executionRange` — The range of commands to execute. The maximum length of the range is `16384` commands.

## See Also

### Dispatching from indirect command buffers

- [- dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:](<dispatchthreadgroups(indirectbuffer_indirectbufferoffset_threadsperthreadgroup_).md>) — Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.
- [executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:](executecommandsinbuffer_indirectbuffer_indirectbufferoffset_.md) — Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
