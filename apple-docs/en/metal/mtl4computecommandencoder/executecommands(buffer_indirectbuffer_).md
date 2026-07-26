---
title: 'executeCommands(buffer:indirectBuffer:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/executecommands(buffer:indirectbuffer:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/executecommands(buffer:indirectbuffer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/executecommands%28buffer%3Aindirectbuffer%3A%29.json'
content_hash: 'sha256:d38b916a49424c0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# executeCommands(buffer:indirectBuffer:)

<sub>Instance Method</sub>

Encodes an instruction to execute commands from an indirect command buffer, using an indirect buffer for arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func executeCommands(buffer indirectCommandbuffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: MTLGPUAddress)
```

## Parameters

- `indirectCommandbuffer` — [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance containing the commands to execute.

- `indirectRangeBuffer` — GPUAddress of a [MTLBuffer](../mtlbuffer.md) containing the execution range. Lay out the data in this buffer as described in the [MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrange.md) structure. This address requires 4-byte alignment.

## Discussion

Use this method to indicate to Metal the span of indices in the command buffer to execute indirectly via an [MTLBuffer](../mtlbuffer.md) instance you provide in the `indirectRangeBuffer` parameter. This allows you to calculate the span of commands Metal executes in the GPU timeline, enabling GPU-driven workflows.

Metal requires that the contents of this buffer match the layout of struct [MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrange.md), which specifies a location and a length within the indirect command buffer. You are responsible for ensuring the address of this buffer has 4-byte alignment.

Use an instance of [MTLResidencySet](../mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectRangeBuffer` parameter references.

> [!note] Note
> If the `indirectCommandBuffer` parameter references any pipeline state objects, you are responsible for adding them to a [MTLResidencySet](../mtlresidencyset.md) instance in use when you commit the command buffer.
>
> An indirect compute command references a pipeline state when you pass it as an argument to the command’s [- setComputePipelineState:](<../mtlindirectcomputecommand/setcomputepipelinestate(__).md>) method during CPU encoding, or `set_compute_pipeline_state()` during GPU encoding.

## See Also

### Encoding indirect command buffers

- [executeCommands(buffer:range:)](<executecommands(buffer_range_).md>) — Encodes a command to execute commands from an indirect command buffer.
