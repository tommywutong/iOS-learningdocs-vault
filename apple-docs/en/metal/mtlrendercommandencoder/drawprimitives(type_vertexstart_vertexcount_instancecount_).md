---
title: 'drawPrimitives(type:vertexStart:vertexCount:instanceCount:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/drawprimitives%28type%3Avertexstart%3Avertexcount%3Ainstancecount%3A%29.json'
content_hash: 'sha256:e67b7ff930308089'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# drawPrimitives(type:vertexStart:vertexCount:instanceCount:)

<sub>Instance Method</sub>

Encodes a draw command that renders multiple instances of a geometric primitive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawPrimitives(type primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)
```

## Parameters

- `primitiveType` — An [MTLPrimitiveType](../mtlprimitivetype.md) instance that represents how the command interprets vertex argument data. See the [- setVertexBuffer:offset:atIndex:](<setvertexbuffer(__offset_index_).md>) method and its siblings for more information about setting an entry in the vertex shader argument table for buffers.

- `vertexStart` — The lowest value the command passes to your vertex shader’s parameter with the `vertex_id` attribute. The command assigns each vertex a unique `vertex_id` value within its drawing instance that increases from `vertexStart` through `(vertexStart + vertexCount - 1)`. Your shader can use that value to identify a vertex in each drawing instance. For more information about the `vertex_id` argument attribute for vertex shaders, see the [Metal Shading Language Specification (PDF)](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

- `vertexCount` — An integer that represents the number of vertices of `primitiveType` the command draws per instance.

- `instanceCount` — An integer that represents the number of times the command draws `primitiveType` with `vertexCount` vertices. The command assigns each drawing instance a unique `instance_id` value that increases from `0` through `(instanceCount - 1)`. Your shader can use that value to identify which instance the vertex belongs to. For more information about the `instance_id` argument attribute for vertex shaders, the [Metal Shading Language Specification (PDF)](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## Discussion

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [MTLCommandBuffer](../mtlcommandbuffer.md).

## See Also

### Drawing with vertices

- [- drawPrimitives:vertexStart:vertexCount:](<drawprimitives(type_vertexstart_vertexcount_).md>) — Encodes a draw command that renders an instance of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:](<drawprimitives(type_vertexstart_vertexcount_instancecount_baseinstance_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive that starts with a custom instance identification number.
- [- drawPrimitives:indirectBuffer:indirectBufferOffset:](<drawprimitives(type_indirectbuffer_indirectbufferoffset_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.
