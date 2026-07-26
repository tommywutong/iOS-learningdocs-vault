---
title: 'drawPrimitives(primitiveType:vertexStart:vertexCount:instanceCount:baseInstance:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:baseinstance:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:baseinstance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/drawprimitives%28primitivetype%3Avertexstart%3Avertexcount%3Ainstancecount%3Abaseinstance%3A%29.json'
content_hash: 'sha256:9cf292937caba6c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# drawPrimitives(primitiveType:vertexStart:vertexCount:instanceCount:baseInstance:)

<sub>Instance Method</sub>

Encodes a draw command that renders multiple instances of a geometric primitive, starting with a custom instance identification number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)
```

## Parameters

- `primitiveType` — A [MTLPrimitiveType](../mtlprimitivetype.md)  representing how the command interprets vertex argument data.

- `vertexStart` — The lowest value the command passes to your vertex shader function’s parameter with the `vertex_id` attribute.

- `vertexCount` — An integer that represents the number of vertices of `primitiveType` the command draws.

- `instanceCount` — An integer that represents the number of times the command draws `primitiveType` with `vertexCount` vertices.

- `baseInstance` — The lowest value the command passes to your vertex shader function’s parameter with the `instance_id` attribute.

## Discussion

The command assigns each vertex a unique `vertex_id` value within its drawing instance that increases from `vertexStart` through `(vertexStart + vertexCount - 1)`.

Additionally, the command assigns each drawing instance a unique `instance_id` value that increases from `baseInstance` through `(baseInstance + instanceCount - 1)`.

Your vertex shader can use the `vertex_id` value to uniquely identify each vertex in each drawing instance, and the `instance_id` value to identify which instance that vertex belongs to.

## See Also

### Drawing with vertices

- [- drawPrimitives:vertexStart:vertexCount:](<drawprimitives(primitivetype_vertexstart_vertexcount_).md>) — Encodes a draw command that renders an instance of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:](<drawprimitives(primitivetype_vertexstart_vertexcount_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive.
- [- drawPrimitives:indirectBuffer:](<drawprimitives(primitivetype_indirectbuffer_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.
