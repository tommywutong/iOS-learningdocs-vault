---
title: 'drawPrimitives(primitiveType:indirectBuffer:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:indirectbuffer:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:indirectbuffer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/drawprimitives%28primitivetype%3Aindirectbuffer%3A%29.json'
content_hash: 'sha256:d21274626eb39187'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# drawPrimitives(primitiveType:indirectBuffer:)

<sub>Instance Method</sub>

Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawPrimitives(primitiveType: MTLPrimitiveType, indirectBuffer: MTLGPUAddress)
```

## Parameters

- `primitiveType` — A [MTLPrimitiveType](../mtlprimitivetype.md) representing how the command interprets vertex argument data.

- `indirectBuffer` — GPUAddress of a [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLDrawPrimitivesIndirectArguments](../mtldrawprimitivesindirectarguments.md) structure. You are responsible for ensuring that the alignment of this address is 4 bytes.

## Discussion

When you use this function, Metal reads the parameters to the draw command from an [MTLBuffer](../mtlbuffer.md) instance, allowing you to implement a GPU-driven workflow where a compute pipeline state determines the draw arguments.

You are responsible for ensuring that the address of the indirect buffer you provide to this method has 4-byte alignment.

Because this is a non-indexed draw call, Metal interprets the contents of the indirect buffer to match the layout of struct [MTLDrawPrimitivesIndirectArguments](../mtldrawprimitivesindirectarguments.md).

Use an instance of [MTLResidencySet](../mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectBuffer` parameter references.

## See Also

### Drawing with vertices

- [- drawPrimitives:vertexStart:vertexCount:](<drawprimitives(primitivetype_vertexstart_vertexcount_).md>) — Encodes a draw command that renders an instance of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:](<drawprimitives(primitivetype_vertexstart_vertexcount_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:](<drawprimitives(primitivetype_vertexstart_vertexcount_instancecount_baseinstance_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive, starting with a custom instance identification number.
