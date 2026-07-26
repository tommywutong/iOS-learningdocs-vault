---
title: MTLPrimitiveType.line
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlprimitivetype/line
source_url: 'https://developer.apple.com/documentation/metal/mtlprimitivetype/line'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlprimitivetype/line.json'
content_hash: 'sha256:09e3c73be70bc2da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPrimitiveType](../mtlprimitivetype.md)

# MTLPrimitiveType.line

<sub>Case</sub>

Rasterize a line between each separate pair of vertices, resulting in a series of unconnected lines. If there are an odd number of vertices, the last vertex is ignored.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case line
```

## See Also

### Geometric primitive types

- [MTLPrimitiveTypePoint](point.md) — Rasterize a point at each vertex. The vertex shader needs to provide `[[point_size]]`, or the point size is undefined.
- [MTLPrimitiveTypeLineStrip](linestrip.md) — Rasterize a line between each pair of adjacent vertices, resulting in a series of connected lines (also called a polyline).
- [MTLPrimitiveTypeTriangle](triangle.md) — For every separate set of three vertices, rasterize a triangle. If the number of vertices is not a multiple of three, either one or two vertices is ignored.
- [MTLPrimitiveTypeTriangleStrip](trianglestrip.md) — For every three adjacent vertices, rasterize a triangle.
