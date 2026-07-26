---
title: 'setFragmentBuffer(_:offset:at:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlindirectrendercommand/setfragmentbuffer(_:offset:at:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectrendercommand/setfragmentbuffer(_:offset:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectrendercommand/setfragmentbuffer%28_%3Aoffset%3Aat%3A%29.json'
content_hash: 'sha256:a493b6e69e2683ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectRenderCommand](../mtlindirectrendercommand.md)

# setFragmentBuffer(_:offset:at:)

<sub>Instance Method</sub>

Sets a fragment buffer argument for the command.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFragmentBuffer(_ buffer: any MTLBuffer, offset: Int, at index: Int)
```

## Parameters

- `buffer` — The buffer to set in the buffer argument table.

- `offset` — The location, in bytes relative to start of `buffer`, of the first byte of data for the fragment shader.

- `index` — An index in the buffer argument table. The maximum index is determined when you created the indirect command buffer.

## Discussion

You don’t need to call this method if you create an indirect command buffer with its [inheritBuffers](../mtlindirectcommandbufferdescriptor/inheritbuffers.md) equal to [true](../../swift/true.md). The command gets the arguments from the parent encoder when it runs.

If you need to pass other kinds of parameters to your shader, such as textures and samplers, create an argument buffer and pass it to the shader using this method.

## See Also

### Setting command arguments

- [- setRenderPipelineState:](<setrenderpipelinestate(__).md>) — Sets the render pipeline state for the command.
- [- setVertexBuffer:offset:atIndex:](<setvertexbuffer(__offset_at_).md>) — Sets a vertex buffer argument for the command.
