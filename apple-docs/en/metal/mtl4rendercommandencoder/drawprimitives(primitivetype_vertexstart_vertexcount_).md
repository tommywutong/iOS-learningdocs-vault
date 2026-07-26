---
title: 'drawPrimitives(primitiveType:vertexStart:vertexCount:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/drawprimitives%28primitivetype%3Avertexstart%3Avertexcount%3A%29.json'
content_hash: 'sha256:1af601420f137722'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# drawPrimitives(primitiveType:vertexStart:vertexCount:)

<sub>Instance Method</sub>

Encodes a draw command that renders an instance of a geometric primitive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)
```

## Parameters

- `primitiveType` — A [MTLPrimitiveType](../mtlprimitivetype.md) representing how the command interprets vertex argument data.

- `vertexStart` — The lowest value the command passes to your vertex shader function’s parameter with the `[[vertex_id]]` attribute.

- `vertexCount` — An integer that represents the number of vertices of `primitiveType` the command draws.

## Discussion

This command assigns each vertex a unique `vertex_id` value that increases from `vertexStart` through `(vertexStart + vertexCount - 1)`.

Your vertex shader function can use this value to uniquely identify each vertex.

## See Also

### Drawing with vertices

- [- drawPrimitives:vertexStart:vertexCount:instanceCount:](<drawprimitives(primitivetype_vertexstart_vertexcount_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:](<drawprimitives(primitivetype_vertexstart_vertexcount_instancecount_baseinstance_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive, starting with a custom instance identification number.
- [- drawPrimitives:indirectBuffer:](<drawprimitives(primitivetype_indirectbuffer_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.
