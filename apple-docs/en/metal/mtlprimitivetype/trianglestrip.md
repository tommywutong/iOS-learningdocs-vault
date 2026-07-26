---
title: MTLPrimitiveType.triangleStrip
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlprimitivetype/trianglestrip
source_url: 'https://developer.apple.com/documentation/metal/mtlprimitivetype/trianglestrip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlprimitivetype/trianglestrip.json'
content_hash: 'sha256:070195bdb53aa691'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPrimitiveType](../mtlprimitivetype.md)

# MTLPrimitiveType.triangleStrip

<sub>Case</sub>

For every three adjacent vertices, rasterize a triangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case triangleStrip
```

## See Also

### Geometric primitive types

- [MTLPrimitiveTypePoint](point.md) — Rasterize a point at each vertex. The vertex shader needs to provide `[[point_size]]`, or the point size is undefined.
- [MTLPrimitiveTypeLine](line.md) — Rasterize a line between each separate pair of vertices, resulting in a series of unconnected lines. If there are an odd number of vertices, the last vertex is ignored.
- [MTLPrimitiveTypeLineStrip](linestrip.md) — Rasterize a line between each pair of adjacent vertices, resulting in a series of connected lines (also called a polyline).
- [MTLPrimitiveTypeTriangle](triangle.md) — For every separate set of three vertices, rasterize a triangle. If the number of vertices is not a multiple of three, either one or two vertices is ignored.
