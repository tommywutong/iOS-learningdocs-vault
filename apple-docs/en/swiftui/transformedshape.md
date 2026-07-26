---
title: TransformedShape
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transformedshape
source_url: 'https://developer.apple.com/documentation/swiftui/transformedshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transformedshape.json'
content_hash: 'sha256:c971dad063aecc34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TransformedShape

<sub>Structure</sub>

A shape with an affine transform applied to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct TransformedShape<Content> where Content : Shape
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

## Topics

### Creating a transformed shape

- [init(shape:transform:)](<transformedshape/init(shape_transform_).md>)

### Getting the shape’s characteristics

- [shape](transformedshape/shape.md)
- [transform](transformedshape/transform.md)

## See Also

### Transforming a shape

- [ScaledShape](scaledshape.md) — A shape with a scale transform applied to it.
- [RotatedShape](rotatedshape.md) — A shape with a rotation transform applied to it.
- [OffsetShape](offsetshape.md) — A shape with a translation offset transform applied to it.
