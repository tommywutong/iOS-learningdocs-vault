---
title: 'drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:basevertex:baseinstance:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:basevertex:baseinstance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/drawindexedprimitives%28type%3Aindexcount%3Aindextype%3Aindexbuffer%3Aindexbufferoffset%3Ainstancecount%3Abasevertex%3Abaseinstance%3A%29.json'
content_hash: 'sha256:62c8b23aa23decbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:)

<sub>Instance Method</sub>

Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)
```

## Parameters

- `primitiveType` — An [MTLPrimitiveType](../mtlprimitivetype.md) instance that represents how the command interprets vertex argument data. See the [- setVertexBuffer:offset:atIndex:](<setvertexbuffer(__offset_index_).md>) method and its siblings for more information about setting an entry in the vertex shader argument table for buffers.

- `indexCount` — An integer that represents the number of vertices the command reads from `indexBuffer` for each instance.

- `indexType` — An [MTLIndexType](../mtlindextype.md) instance that represents the index’s format, including [MTLIndexTypeUInt16](../mtlindextype/uint16.md) and [MTLIndexTypeUInt32](../mtlindextype/uint32.md).

- `indexBuffer` — An [MTLBuffer](../mtlbuffer.md) instance that contains the `indexCount` vertex indices of the `indexType` format.

- `indexBufferOffset` — An integer that represents the location that’s a multiple of the index size from the start of `indexBuffer` where the vertex indices begin.

- `instanceCount` — An integer that represents the number of times the command draws `primitiveType` with `indexCount` vertices.

- `baseVertex` — The lowest value the command passes to your vertex shader’s parameter with the `vertex_id` attribute. The command assigns each vertex a unique `vertex_id` value that increases from `baseVertex` through `(baseVertex + indexCount - 1)`. Your shader can use that value to identify each vertex in the `primitiveType` instance. For more information about the `vertex_id` argument attribute for vertex shaders, see the [Metal Shading Language Specification (PDF)](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

- `baseInstance` — The lowest value the command passes to your vertex shader’s parameter with the `instance_id` attribute. The command assigns each drawing instance a unique `instance_id` value that increases from `baseInstance` through `(baseInstance + instanceCount - 1)`. Your shader can use that value to identify which instance the vertex belongs to. For more information about the `instance_id` argument attribute for vertex shaders, see the [Metal Shading Language Specification (PDF)](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## Discussion

You can complete a primitive and start a new one by passing a sentinel index value that’s the largest unsigned integer possible for `indexType`. For example, the largest unsigned integer for [MTLIndexTypeUInt16](../mtlindextype/uint16.md) and [MTLIndexTypeUInt32](../mtlindextype/uint32.md) is `0xFFFF` and `0xFFFFFFFF`, respectively. The command finishes the current primitive and begins drawing a new one each time the command reads a sentinel index value.

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [MTLCommandBuffer](../mtlcommandbuffer.md).

## See Also

### Drawing with indexed vertices

- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:](<drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_).md>) — Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.
- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:](<drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [- drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:](<drawindexedprimitives(type_indextype_indexbuffer_indexbufferoffset_indirectbuffer_indirectbufferoffset_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.
