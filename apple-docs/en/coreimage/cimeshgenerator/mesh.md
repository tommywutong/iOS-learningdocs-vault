---
title: mesh
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cimeshgenerator/mesh
source_url: 'https://developer.apple.com/documentation/coreimage/cimeshgenerator/mesh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cimeshgenerator/mesh.json'
content_hash: 'sha256:9f4ca5085f6638cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIMeshGenerator](../cimeshgenerator.md)

# mesh

<sub>Instance Property</sub>

An array that describes the mesh to render.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mesh: [Any] { get set }
```

## Discussion

Specify the mesh as an array of line segments. Each line segment is stored as a [CIVector](../civector.md) instance that describes the line as a start point and an end point.

## See Also

### Instance Properties

- [color](color.md) — The color of the rendered mesh.
- [width](width.md) — The width of the effect.
