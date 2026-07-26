---
title: RectangleCornerInsets
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/rectanglecornerinsets
source_url: 'https://developer.apple.com/documentation/swiftui/rectanglecornerinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rectanglecornerinsets.json'
content_hash: 'sha256:0b59c119e6f8d7dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RectangleCornerInsets

<sub>Structure</sub>

The inset sizes for the corners of a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct RectangleCornerInsets
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init()](<rectanglecornerinsets/init().md>)
- [init(topLeading:topTrailing:bottomLeading:bottomTrailing:)](<rectanglecornerinsets/init(topleading_toptrailing_bottomleading_bottomtrailing_).md>)

### Instance Properties

- [bottomLeading](rectanglecornerinsets/bottomleading.md) — The size of the bottom-leading corner inset.
- [bottomTrailing](rectanglecornerinsets/bottomtrailing.md) — The size of the bottom-trailing corner inset.
- [topLeading](rectanglecornerinsets/topleading.md) — The size of the top-leading corner inset.
- [topTrailing](rectanglecornerinsets/toptrailing.md) — The size of the top-trailing corner inset.

## See Also

### Creating rectangular shapes

- [Rectangle](rectangle.md) — A rectangular shape aligned inside the frame of the view containing it.
- [RoundedRectangle](roundedrectangle.md) — A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [RoundedCornerStyle](roundedcornerstyle.md) — Defines the shape of a rounded rectangle’s corners.
- [RoundedRectangularShape](roundedrectangularshape.md) — A protocol of [InsettableShape](insettableshape.md) that describes a rounded rectangular shape.
- [RoundedRectangularShapeCorners](roundedrectangularshapecorners.md) — A type describing the corner styles of a [RoundedRectangularShape](roundedrectangularshape.md).
- [UnevenRoundedRectangle](unevenroundedrectangle.md) — A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [RectangleCornerRadii](rectanglecornerradii.md) — Describes the corner radius values of a rounded rectangle with uneven corners.
- [ConcentricRectangle](concentricrectangle.md) — A shape whose corners you configure, individually or uniformly, to be squared, rounded, or concentric relative to a container shape’s corners.
