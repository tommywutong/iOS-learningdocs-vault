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
doc_path: '/documentation/metal/mtl4rendercommandencoder/executecommands(buffer:indirectbuffer:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/executecommands(buffer:indirectbuffer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/executecommands%28buffer%3Aindirectbuffer%3A%29.json'
content_hash: 'sha256:d6067d83d1998e82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# executeCommands(buffer:indirectBuffer:)

<sub>Instance Method</sub>

Encodes a command that runs an indirect range of commands from an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func executeCommands(buffer indirectCommandBuffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: MTLGPUAddress)
```

## Parameters

- `indirectCommandBuffer` — A [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance that contains other commands the current command runs.

- `indirectRangeBuffer` — GPUAddress of a [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrange.md) structure. This address requires 4-byte alignment.

## Discussion

Use this method to indicate to Metal the span of indices in the command buffer to execute indirectly via an [MTLBuffer](../mtlbuffer.md) instance you provide in the `indirectRangeBuffer` parameter. This allows you to calculate the span of commands Metal executes in the GPU timeline, enabling GPU-driven workflows.

Metal requires that the contents of this buffer match the layout of struct [MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrange.md), which specifies a location and a length within the indirect command buffer. You are responsible for ensuring the address of this buffer has 4-byte alignment.

Use an instance of [MTLResidencySet](../mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectRangeBuffer` parameter references.

> [!note] Note
> If the `indirectCommandBuffer` parameter references any pipeline state objects, you are responsible for adding them to a [MTLResidencySet](../mtlresidencyset.md) instance in use when you commit the command buffer.
>
> An indirect render command references a pipeline state when you pass it as an argument to the command’s [- setRenderPipelineState:](<../mtlindirectrendercommand/setrenderpipelinestate(__).md>) method during CPU encoding, or `set_render_pipeline_state()` during GPU encoding.

## See Also

### Running commands from indirect command buffers

- [executeCommands(buffer:range:)](<executecommands(buffer_range_).md>) — Encodes a command that runs a range of commands from an indirect command buffer.
