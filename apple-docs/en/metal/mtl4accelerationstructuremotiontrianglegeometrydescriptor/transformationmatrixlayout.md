---
title: transformationMatrixLayout
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixlayout
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixlayout.json'
content_hash: 'sha256:0db8015e64439c45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](../mtl4accelerationstructuremotiontrianglegeometrydescriptor.md)

# transformationMatrixLayout

<sub>Instance Property</sub>

Configures the layout for the transformation matrix in the transformation matrix buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var transformationMatrixLayout: MTLMatrixLayout { get set }
```

## Discussion

You can provide matrices in column-major or row-major form, and this property allows you to control how Metal interprets them.

Defaults to `MTLMatrixLayoutColumnMajor`.
