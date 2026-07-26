---
title: 'drawPrimitives(type:indirectBuffer:indirectBufferOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/drawprimitives(type:indirectbuffer:indirectbufferoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawprimitives(type:indirectbuffer:indirectbufferoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/drawprimitives%28type%3Aindirectbuffer%3Aindirectbufferoffset%3A%29.json'
content_hash: 'sha256:90617ef835c17101'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# drawPrimitives(type:indirectBuffer:indirectBufferOffset:)

<sub>Instance Method</sub>

Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawPrimitives(type primitiveType: MTLPrimitiveType, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

## Parameters

- `primitiveType` — An [MTLPrimitiveType](../mtlprimitivetype.md) instance that represents how the command interprets vertex argument data. See the [- setVertexBuffer:offset:atIndex:](<setvertexbuffer(__offset_index_).md>) method and its siblings for more information about setting an entry in the vertex shader argument table for buffers.

- `indirectBuffer` — An [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLDrawPrimitivesIndirectArguments](../mtldrawprimitivesindirectarguments.md) structure.

- `indirectBufferOffset` — An integer that represents the location, in bytes, from the start of `indirectBuffer` where the indirect arguments structure begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

## Discussion

Indirect drawing methods may help your app avoid expensive latency costs. This is because the command reads arguments from an [MTLBuffer](../mtlbuffer.md) instance instead of using the CPU to pass parameters to the command.

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [MTLCommandBuffer](../mtlcommandbuffer.md).

## See Also

### Drawing with vertices

- [- drawPrimitives:vertexStart:vertexCount:](<drawprimitives(type_vertexstart_vertexcount_).md>) — Encodes a draw command that renders an instance of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:](<drawprimitives(type_vertexstart_vertexcount_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:](<drawprimitives(type_vertexstart_vertexcount_instancecount_baseinstance_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive that starts with a custom instance identification number.
