---
title: 'drawIndexedPrimitives(type:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/drawindexedprimitives(type:indextype:indexbuffer:indexbufferoffset:indirectbuffer:indirectbufferoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawindexedprimitives(type:indextype:indexbuffer:indexbufferoffset:indirectbuffer:indirectbufferoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/drawindexedprimitives%28type%3Aindextype%3Aindexbuffer%3Aindexbufferoffset%3Aindirectbuffer%3Aindirectbufferoffset%3A%29.json'
content_hash: 'sha256:43d6687631d7a7fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# drawIndexedPrimitives(type:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:)

<sub>Instance Method</sub>

Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

## Parameters

- `primitiveType` — An [MTLPrimitiveType](../mtlprimitivetype.md) instance that represents how the command interprets vertex argument data. See the [- setVertexBuffer:offset:atIndex:](<setvertexbuffer(__offset_index_).md>) method and its siblings for more information about setting an entry in the vertex shader argument table for buffers.

- `indexType` — An [MTLIndexType](../mtlindextype.md) instance that represents the index’s format, including [MTLIndexTypeUInt16](../mtlindextype/uint16.md) and [MTLIndexTypeUInt32](../mtlindextype/uint32.md).

- `indexBuffer` — An [MTLBuffer](../mtlbuffer.md) instance that contains the vertex indices of the `indexType` format.

- `indexBufferOffset` — An integer that represents the location that’s a multiple of the index size from the start of `indexBuffer` where the vertex indices begin.

- `indirectBuffer` — An [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLDrawIndexedPrimitivesIndirectArguments](../mtldrawindexedprimitivesindirectarguments.md) structure.

- `indirectBufferOffset` — An integer that represents the location, in bytes, from the start of `indirectBuffer` where the indirect arguments structure begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

## Discussion

Indirect drawing methods may help your app avoid expensive latency costs. This is because the command reads arguments from an [MTLBuffer](../mtlbuffer.md) instance instead of using the CPU to pass parameters to the command.

You can complete a primitive and start a new one by passing a sentinel index value that’s the largest unsigned integer possible for `indexType`. For example, the largest unsigned integer for [MTLIndexTypeUInt16](../mtlindextype/uint16.md) and [MTLIndexTypeUInt32](../mtlindextype/uint32.md) is `0xFFFF` and `0xFFFFFFFF`, respectively. The command finishes the current primitive and begins drawing a new one each time the command reads a sentinel index value.

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [MTLCommandBuffer](../mtlcommandbuffer.md).

## See Also

### Drawing with indexed vertices

- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:](<drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_).md>) — Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.
- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:](<drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:](<drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_instancecount_basevertex_baseinstance_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.
