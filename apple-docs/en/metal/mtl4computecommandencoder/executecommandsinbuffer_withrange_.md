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
doc_path: '/documentation/metal/mtl4computecommandencoder/executecommandsinbuffer:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/executecommandsinbuffer:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/executecommandsinbuffer%3Awithrange%3A.json'
content_hash: 'sha256:0e5a8b7643cac23d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# executeCommandsInBuffer:withRange:

<sub>Instance Method</sub>

Encodes a command to execute a series of commands from an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) executeCommandsInBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) executionRange;
```

## Parameters

- `indirectCommandBuffer` — [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance containing the commands to execute.

- `executionRange` — The range of commands to execute.

## Discussion

Use this method to encode the execution of a range of Metal compute commands in the GPU timeline.

> [!note] Note
> If the `indirectCommandBuffer` parameter references any pipeline state objects, you are responsible for adding them to a [MTLResidencySet](../mtlresidencyset.md) instance in use when you commit the command buffer.
>
> An indirect compute command references a pipeline state when you pass it as an argument to the command’s [- setComputePipelineState:](<../mtlindirectcomputecommand/setcomputepipelinestate(__).md>) method during CPU encoding, or `set_compute_pipeline_state()` during GPU encoding.

## See Also

### Encoding indirect command buffers

- [- executeCommandsInBuffer:indirectBuffer:](<executecommands(buffer_indirectbuffer_).md>) — Encodes an instruction to execute commands from an indirect command buffer, using an indirect buffer for arguments.
