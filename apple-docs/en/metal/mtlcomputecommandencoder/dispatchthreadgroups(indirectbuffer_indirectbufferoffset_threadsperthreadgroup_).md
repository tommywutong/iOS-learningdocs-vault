---
title: 'dispatchThreadgroups(indirectBuffer:indirectBufferOffset:threadsPerThreadgroup:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer:indirectbufferoffset:threadsperthreadgroup:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer:indirectbufferoffset:threadsperthreadgroup:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/dispatchthreadgroups%28indirectbuffer%3Aindirectbufferoffset%3Athreadsperthreadgroup%3A%29.json'
content_hash: 'sha256:b0b37fb93a269a59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# dispatchThreadgroups(indirectBuffer:indirectBufferOffset:threadsPerThreadgroup:)

<sub>Instance Method</sub>

Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dispatchThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)
```

## Parameters

- `indirectBuffer` — An [MTLBuffer](../mtlbuffer.md) instance providing compute parameters. Lay out the data in this buffer as described in the [MTLDispatchThreadgroupsIndirectArguments](../mtldispatchthreadgroupsindirectarguments.md) structure.

- `indirectBufferOffset` — Where the data begins, in bytes, from the start of the buffer. This value needs to be a multiple of `4`.

- `threadsPerThreadgroup` — The number of threads in one threadgroup, in each dimension.

## Discussion

The GPU fetches parameters from the indirect buffer just before the thread grid starts. This process lets the compute function run based on GPU feedback, without latency from data transfer between the CPU and the GPU.

## See Also

### Dispatching from indirect command buffers

- [executeCommandsInBuffer(_:range:)](<executecommandsinbuffer(__range_).md>) — Encodes an instruction to run commands from an indirect buffer.
- [executeCommandsInBuffer(_:indirectBuffer:offset:)](<executecommandsinbuffer(__indirectbuffer_offset_).md>) — Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [executeCommands(in:indirectBuffer:indirectBufferOffset:)](<executecommands(in_indirectbuffer_indirectbufferoffset_).md>) — Encodes an instruction to run commands from an indirect buffer, using another buffer to provide the command range.
- [executeCommands(in:with:)](<executecommands(in_with_).md>) — Encodes an instruction to run commands from an indirect buffer.
