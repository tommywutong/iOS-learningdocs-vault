---
title: MTLPrimitiveType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlprimitivetype
source_url: 'https://developer.apple.com/documentation/metal/mtlprimitivetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlprimitivetype.json'
content_hash: 'sha256:95acce9a2ed8abd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPrimitiveType

<sub>Enumeration</sub>

The geometric primitive type for drawing commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLPrimitiveType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Geometric primitive types

- [MTLPrimitiveTypePoint](mtlprimitivetype/point.md) — Rasterize a point at each vertex. The vertex shader needs to provide `[[point_size]]`, or the point size is undefined.
- [MTLPrimitiveTypeLine](mtlprimitivetype/line.md) — Rasterize a line between each separate pair of vertices, resulting in a series of unconnected lines. If there are an odd number of vertices, the last vertex is ignored.
- [MTLPrimitiveTypeLineStrip](mtlprimitivetype/linestrip.md) — Rasterize a line between each pair of adjacent vertices, resulting in a series of connected lines (also called a polyline).
- [MTLPrimitiveTypeTriangle](mtlprimitivetype/triangle.md) — For every separate set of three vertices, rasterize a triangle. If the number of vertices is not a multiple of three, either one or two vertices is ignored.
- [MTLPrimitiveTypeTriangleStrip](mtlprimitivetype/trianglestrip.md) — For every three adjacent vertices, rasterize a triangle.

### Initializers

- [init(rawValue:)](<mtlprimitivetype/init(rawvalue_).md>)

## See Also

### Encoding a render pass

- [MTL4RenderCommandEncoder](mtl4rendercommandencoder.md) — Encodes configuration and draw commands for a single render pass into a command buffer.
- [MTLRenderCommandEncoder](mtlrendercommandencoder.md) — Encodes configuration and draw commands for a single render pass into a command buffer.
- [MTL4RenderEncoderOptions](mtl4renderencoderoptions.md) — Custom render pass options you specify at encoder creation time.
- [MTLTriangleFillMode](mtltrianglefillmode.md) — Specifies how to rasterize triangle and triangle strip primitives.
- [MTLWinding](mtlwinding.md) — The vertex winding rule that determines a front-facing primitive.
- [MTLCullMode](mtlcullmode.md) — The mode that determines whether to perform culling and which type of primitive to cull.
- [MTLIndexType](mtlindextype.md) — The index type for an index buffer that references vertices of geometric primitives.
- [MTLDepthClipMode](mtldepthclipmode.md) — The mode that determines how to deal with fragments outside of the near or far planes.
- [MTLVisibilityResultMode](mtlvisibilityresultmode.md) — The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.
- [MTLVisibilityResultType](mtlvisibilityresulttype.md) — This enumeration controls if Metal accumulates visibility results between render encoders or resets them.
