---
title: RotatedShape
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/rotatedshape
source_url: 'https://developer.apple.com/documentation/swiftui/rotatedshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rotatedshape.json'
content_hash: 'sha256:5c244828a768616b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RotatedShape

<sub>Structure</sub>

A shape with a rotation transform applied to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct RotatedShape<Content> where Content : Shape
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [InsettableShape](insettableshape.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

## Topics

### Creating a rotated shape

- [init(shape:angle:anchor:)](<rotatedshape/init(shape_angle_anchor_).md>)

### Getting the shape’s characteristics

- [anchor](rotatedshape/anchor.md)
- [angle](rotatedshape/angle.md)
- [shape](rotatedshape/shape.md)

### Supporting types

- [animatableData](rotatedshape/animatabledata.md) — The data to animate.

## See Also

### Transforming a shape

- [ScaledShape](scaledshape.md) — A shape with a scale transform applied to it.
- [OffsetShape](offsetshape.md) — A shape with a translation offset transform applied to it.
- [TransformedShape](transformedshape.md) — A shape with an affine transform applied to it.
