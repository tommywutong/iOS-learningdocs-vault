---
title: RectangleCornerRadii
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/rectanglecornerradii
source_url: 'https://developer.apple.com/documentation/swiftui/rectanglecornerradii'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rectanglecornerradii.json'
content_hash: 'sha256:90103aa223cfa4f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RectangleCornerRadii

<sub>Structure</sub>

Describes the corner radius values of a rounded rectangle with uneven corners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct RectangleCornerRadii
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a set of radii

- [init(topLeading:bottomLeading:bottomTrailing:topTrailing:)](<rectanglecornerradii/init(topleading_bottomleading_bottomtrailing_toptrailing_).md>) — Creates a new set of corner radii for a rounded rectangle with uneven corners.

### Getting values for specific corners

- [topLeading](rectanglecornerradii/topleading.md) — The radius of the top-leading corner.
- [topTrailing](rectanglecornerradii/toptrailing.md) — The radius of the top-trailing corner.
- [bottomLeading](rectanglecornerradii/bottomleading.md) — The radius of the bottom-leading corner.
- [bottomTrailing](rectanglecornerradii/bottomtrailing.md) — The radius of the bottom-trailing corner.

### Subscripts

- [subscript(_:)](<rectanglecornerradii/subscript(__).md>) — Returns the corner radius for a certain corner.

## See Also

### Creating rectangular shapes

- [Rectangle](rectangle.md) — A rectangular shape aligned inside the frame of the view containing it.
- [RoundedRectangle](roundedrectangle.md) — A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [RoundedCornerStyle](roundedcornerstyle.md) — Defines the shape of a rounded rectangle’s corners.
- [RoundedRectangularShape](roundedrectangularshape.md) — A protocol of [InsettableShape](insettableshape.md) that describes a rounded rectangular shape.
- [RoundedRectangularShapeCorners](roundedrectangularshapecorners.md) — A type describing the corner styles of a [RoundedRectangularShape](roundedrectangularshape.md).
- [UnevenRoundedRectangle](unevenroundedrectangle.md) — A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [RectangleCornerInsets](rectanglecornerinsets.md) — The inset sizes for the corners of a rectangle.
- [ConcentricRectangle](concentricrectangle.md) — A shape whose corners you configure, individually or uniformly, to be squared, rounded, or concentric relative to a container shape’s corners.
