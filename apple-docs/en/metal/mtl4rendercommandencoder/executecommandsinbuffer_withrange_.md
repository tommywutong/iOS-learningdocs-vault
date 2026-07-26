---
title: 'executeCommandsInBuffer:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/executecommandsinbuffer:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/executecommandsinbuffer:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/executecommandsinbuffer%3Awithrange%3A.json'
content_hash: 'sha256:031fc720abf2f13f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# executeCommandsInBuffer:withRange:

<sub>Instance Method</sub>

Encodes a command that runs a range of commands from an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) executeCommandsInBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) executionRange;
```

## Parameters

- `indirectCommandBuffer` — A [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance containing other commands that the current command runs.

- `executionRange` — A span of integers that represent the command entries in the buffer that the current command runs.

## Discussion

Use this method to encode the execution of a range of Metal render commands in the GPU timeline.

> [!note] Note
> If the `indirectCommandBuffer` parameter references any pipeline state objects, you are responsible for adding them to a [MTLResidencySet](../mtlresidencyset.md) instance in use when you commit the command buffer.
>
> An indirect render command references a pipeline state when you pass it as an argument to the command’s [- setRenderPipelineState:](<../mtlindirectrendercommand/setrenderpipelinestate(__).md>) method during CPU encoding, or `set_render_pipeline_state()` during GPU encoding.

## See Also

### Running commands from indirect command buffers

- [- executeCommandsInBuffer:indirectBuffer:](<executecommands(buffer_indirectbuffer_).md>) — Encodes a command that runs an indirect range of commands from an indirect command buffer.
