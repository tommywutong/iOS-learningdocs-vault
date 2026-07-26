---
title: RoundedRectangle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/roundedrectangle
source_url: 'https://developer.apple.com/documentation/swiftui/roundedrectangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/roundedrectangle.json'
content_hash: 'sha256:0f81b26f142fabc3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RoundedRectangle

<sub>Structure</sub>

A rectangular shape with rounded corners, aligned inside the frame of the view containing it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct RoundedRectangle
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [InsettableShape](insettableshape.md), [RoundedRectangularShape](roundedrectangularshape.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

## Topics

### Creating a rounded rectangle

- [init(cornerRadius:style:)](<roundedrectangle/init(cornerradius_style_).md>) — Creates a new rounded rectangle shape.
- [init(cornerSize:style:)](<roundedrectangle/init(cornersize_style_).md>) — Creates a new rounded rectangle shape.

### Getting the shape’s characteristics

- [cornerSize](roundedrectangle/cornersize.md) — The width and height of the rounded rectangle’s corners.
- [style](roundedrectangle/style.md) — The style of corners drawn by the rounded rectangle.

### Supporting types

- [animatableData](roundedrectangle/animatabledata.md) — The data to animate.

## See Also

### Creating rectangular shapes

- [Rectangle](rectangle.md) — A rectangular shape aligned inside the frame of the view containing it.
- [RoundedCornerStyle](roundedcornerstyle.md) — Defines the shape of a rounded rectangle’s corners.
- [RoundedRectangularShape](roundedrectangularshape.md) — A protocol of [InsettableShape](insettableshape.md) that describes a rounded rectangular shape.
- [RoundedRectangularShapeCorners](roundedrectangularshapecorners.md) — A type describing the corner styles of a [RoundedRectangularShape](roundedrectangularshape.md).
- [UnevenRoundedRectangle](unevenroundedrectangle.md) — A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [RectangleCornerRadii](rectanglecornerradii.md) — Describes the corner radius values of a rounded rectangle with uneven corners.
- [RectangleCornerInsets](rectanglecornerinsets.md) — The inset sizes for the corners of a rectangle.
- [ConcentricRectangle](concentricrectangle.md) — A shape whose corners you configure, individually or uniformly, to be squared, rounded, or concentric relative to a container shape’s corners.
