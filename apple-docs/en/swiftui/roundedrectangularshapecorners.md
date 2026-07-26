---
title: RoundedRectangularShapeCorners
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/roundedrectangularshapecorners
source_url: 'https://developer.apple.com/documentation/swiftui/roundedrectangularshapecorners'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/roundedrectangularshapecorners.json'
content_hash: 'sha256:6f78d5ed4395df39'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RoundedRectangularShapeCorners

<sub>Structure</sub>

A type describing the corner styles of a [RoundedRectangularShape](roundedrectangularshape.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RoundedRectangularShapeCorners
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(all:)](<roundedrectangularshapecorners/init(all_).md>) — Create corner styles with all corner having the same style.
- [init(topLeading:topTrailing:bottomLeading:bottomTrailing:)](<roundedrectangularshapecorners/init(topleading_toptrailing_bottomleading_bottomtrailing_).md>) — Create corner styles with per-corner styles.

### Instance Properties

- [bottomLeading](roundedrectangularshapecorners/bottomleading.md) — The bottom leading corner style.
- [bottomTrailing](roundedrectangularshapecorners/bottomtrailing.md) — The bottom trailing corner style
- [topLeading](roundedrectangularshapecorners/topleading.md) — The top leading corner style.
- [topTrailing](roundedrectangularshapecorners/toptrailing.md) — The top trailing corner style.

### Subscripts

- [subscript(_:)](<roundedrectangularshapecorners/subscript(__).md>) — Returns the corner style for a provided corner.

### Type Properties

- [concentric](roundedrectangularshapecorners/concentric.md) — Corner styles will be concentric with its container, varying the radius as needed in all four corners.

### Type Methods

- [concentric(minimum:)](<roundedrectangularshapecorners/concentric(minimum_).md>) — Corner styles will be concentric with its container, varying the radius as needed in all four corners but never going below zero, or the provided minimum corner style, if provided.
- [fixed(_:)](<roundedrectangularshapecorners/fixed(__).md>) — Corner styles with fixed radius in all four corners.

## See Also

### Creating rectangular shapes

- [Rectangle](rectangle.md) — A rectangular shape aligned inside the frame of the view containing it.
- [RoundedRectangle](roundedrectangle.md) — A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [RoundedCornerStyle](roundedcornerstyle.md) — Defines the shape of a rounded rectangle’s corners.
- [RoundedRectangularShape](roundedrectangularshape.md) — A protocol of [InsettableShape](insettableshape.md) that describes a rounded rectangular shape.
- [UnevenRoundedRectangle](unevenroundedrectangle.md) — A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [RectangleCornerRadii](rectanglecornerradii.md) — Describes the corner radius values of a rounded rectangle with uneven corners.
- [RectangleCornerInsets](rectanglecornerinsets.md) — The inset sizes for the corners of a rectangle.
- [ConcentricRectangle](concentricrectangle.md) — A shape whose corners you configure, individually or uniformly, to be squared, rounded, or concentric relative to a container shape’s corners.
