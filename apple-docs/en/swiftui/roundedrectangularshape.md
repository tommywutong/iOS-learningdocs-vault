---
title: RoundedRectangularShape
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/roundedrectangularshape
source_url: 'https://developer.apple.com/documentation/swiftui/roundedrectangularshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/roundedrectangularshape.json'
content_hash: 'sha256:21cf7e3770a74f31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RoundedRectangularShape

<sub>Protocol</sub>

A protocol of [InsettableShape](insettableshape.md) that describes a rounded rectangular shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol RoundedRectangularShape : InsettableShape
```

## Overview

Conform your [InsettableShape](insettableshape.md) type to [RoundedRectangularShape](roundedrectangularshape.md) when your shape is a rounded rectangular with four corners and you want to expose information about the corners. For example, a custom triangle [Shape](shape.md) is not fit for such conformance, while a custom rectangle [Shape](shape.md) could benefit from providing the implementation, especially when the shape is used as a container shape in [containerShape(_:)](<view/containershape(__)-3br47.md>) to achieve concentricity.

System shapes like [Rectangle](rectangle.md), [RoundedRectangle](roundedrectangle.md), [UnevenRoundedRectangle](unevenroundedrectangle.md), [Capsule](capsule.md), and [Circle](circle.md) already provide default implementation for this protocol.

## Relationships

- **Inherits From**: [Animatable](animatable.md), [InsettableShape](insettableshape.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

- **Conforming Types**: [Capsule](capsule.md), [Circle](circle.md), [Rectangle](rectangle.md), [RoundedRectangle](roundedrectangle.md), [UnevenRoundedRectangle](unevenroundedrectangle.md)

## Topics

### Instance Methods

- [corners(in:)](<roundedrectangularshape/corners(in_).md>) — Resolved corners given a size. If the corner style of a shape is size-dependent, read the provided size and return values accordingly. This function could be called with a nil size when the size hasn’t been determined. In that case, return the best approximated value. For example, for a capsule shape, its corner radius is determined by the size. If size is not available, return `.fixed(.infinity)` to indicate that the corner should be as round as it could be.

### Type Aliases

- [Corners](roundedrectangularshape/corners.md)

## See Also

### Creating rectangular shapes

- [Rectangle](rectangle.md) — A rectangular shape aligned inside the frame of the view containing it.
- [RoundedRectangle](roundedrectangle.md) — A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [RoundedCornerStyle](roundedcornerstyle.md) — Defines the shape of a rounded rectangle’s corners.
- [RoundedRectangularShapeCorners](roundedrectangularshapecorners.md) — A type describing the corner styles of a [RoundedRectangularShape](roundedrectangularshape.md).
- [UnevenRoundedRectangle](unevenroundedrectangle.md) — A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [RectangleCornerRadii](rectanglecornerradii.md) — Describes the corner radius values of a rounded rectangle with uneven corners.
- [RectangleCornerInsets](rectanglecornerinsets.md) — The inset sizes for the corners of a rectangle.
- [ConcentricRectangle](concentricrectangle.md) — A shape whose corners you configure, individually or uniformly, to be squared, rounded, or concentric relative to a container shape’s corners.
