---
title: 'setRenderPipelineState(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlindirectrendercommand/setrenderpipelinestate(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectrendercommand/setrenderpipelinestate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectrendercommand/setrenderpipelinestate%28_%3A%29.json'
content_hash: 'sha256:a3f93a3aa0dbb811'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectRenderCommand](../mtlindirectrendercommand.md)

# setRenderPipelineState(_:)

<sub>Instance Method</sub>

Sets the render pipeline state for the command.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setRenderPipelineState(_ pipelineState: any MTLRenderPipelineState)
```

## Parameters

- `pipelineState` — The rendering pipeline state object to use.

## Discussion

You don’t need to call this method if you create an indirect command buffer with its [inheritPipelineState](../mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) property equal to [true](../../swift/true.md). The command gets the pipeline state from the parent encoder when it runs.

If you created the indirect command buffer with [inheritPipelineState](../mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) set to [false](../../swift/false.md), you need to set the pipeline state prior to encoding the drawing command.

## See Also

### Setting command arguments

- [- setVertexBuffer:offset:atIndex:](<setvertexbuffer(__offset_at_).md>) — Sets a vertex buffer argument for the command.
- [- setFragmentBuffer:offset:atIndex:](<setfragmentbuffer(__offset_at_).md>) — Sets a fragment buffer argument for the command.
