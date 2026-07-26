---
title: 'drawIndexedPrimitives(primitiveType:indexCount:indexType:indexBuffer:indexBufferLength:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/drawindexedprimitives%28primitivetype%3Aindexcount%3Aindextype%3Aindexbuffer%3Aindexbufferlength%3A%29.json'
content_hash: 'sha256:a0ae859a9a970901'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# drawIndexedPrimitives(primitiveType:indexCount:indexType:indexBuffer:indexBufferLength:)

<sub>Instance Method</sub>

Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLGPUAddress, indexBufferLength: Int)
```

## Parameters

- `primitiveType` — A [MTLPrimitiveType](../mtlprimitivetype.md) representing how the command interprets vertex argument data.

- `indexCount` — An integer that represents the number of vertices the command reads from `indexBuffer`.

- `indexType` — A [MTLIndexType](../mtlindextype.md) instance that represents the index format.

- `indexBuffer` — GPUAddress of a [MTLBuffer](../mtlbuffer.md) instance that contains `indexCount` indices of `indexType` format. You are responsible for ensuring this address is aligned to 2 bytes if the `indexType` format is [MTLIndexTypeUInt16](../mtlindextype/uint16.md), and aligned to 4 bytes if the format is [MTLIndexTypeUInt32](../mtlindextype/uint32.md).

- `indexBufferLength` — An integer that represents the length of `indexBuffer`, in bytes. You are responsible for ensuring this this size is a multiple of 2 if the `indexType` format is [MTLIndexTypeUInt16](../mtlindextype/uint16.md), and a multiple of 4 if the format is [MTLIndexTypeUInt32](../mtlindextype/uint32.md). If this draw call causes Metal to read indices at or beyond the `indexBufferLength`, Metal continues to execute them assigning a value of `0` to the `vertex_id` attribute.

## Discussion

Use this method to perform indexed drawing, where an index buffer determines how Metal assembles primitives.

Metal imposes some restrictions on the index buffer’s address, which needs to be 2- or 4-byte aligned, and its length in bytes, which needs to be a multiple of 2 or 4, depending on whether the format of the index is [MTLIndexTypeUInt16](../mtlindextype/uint16.md) or [MTLIndexTypeUInt32](../mtlindextype/uint32.md).

Use an instance of [MTLResidencySet](../mtlresidencyset.md) to mark residency of the index buffer the `indexBuffer` parameter references.

## See Also

### Drawing with indexed vertices

- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:](<drawindexedprimitives(primitivetype_indexcount_indextype_indexbuffer_indexbufferlength_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:](<drawindexedprimitives(primitivetype_indexcount_indextype_indexbuffer_indexbufferlength_instancecount_basevertex_baseinstance_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.
- [- drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:](<drawindexedprimitives(primitivetype_indextype_indexbuffer_indexbufferlength_indirectbuffer_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.
