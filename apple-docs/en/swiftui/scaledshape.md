---
title: ScaledShape
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scaledshape
source_url: 'https://developer.apple.com/documentation/swiftui/scaledshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scaledshape.json'
content_hash: 'sha256:a1c4d7de551e77e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScaledShape

<sub>Structure</sub>

A shape with a scale transform applied to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ScaledShape<Content> where Content : Shape
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

## Topics

### Creating a scaled shape

- [init(shape:scale:anchor:)](<scaledshape/init(shape_scale_anchor_).md>)

### Getting the shape’s characteristics

- [anchor](scaledshape/anchor.md)
- [scale](scaledshape/scale.md)
- [shape](scaledshape/shape.md)

### Supporting types

- [animatableData](scaledshape/animatabledata.md) — The data to animate.

## See Also

### Transforming a shape

- [RotatedShape](rotatedshape.md) — A shape with a rotation transform applied to it.
- [OffsetShape](offsetshape.md) — A shape with a translation offset transform applied to it.
- [TransformedShape](transformedshape.md) — A shape with an affine transform applied to it.
