---
title: InsettableShape
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/insettableshape
source_url: 'https://developer.apple.com/documentation/swiftui/insettableshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/insettableshape.json'
content_hash: 'sha256:16290f0880bfc785'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# InsettableShape

<sub>Protocol</sub>

A shape type that is able to inset itself to produce another shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol InsettableShape : Shape
```

## Relationships

- **Inherits From**: [Animatable](animatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

- **Inherited By**: [RoundedRectangularShape](roundedrectangularshape.md)

- **Conforming Types**: [ButtonBorderShape](buttonbordershape.md), [Capsule](capsule.md), [Circle](circle.md), [ContainerRelativeShape](containerrelativeshape.md), [Ellipse](ellipse.md), [OffsetShape](offsetshape.md), [Rectangle](rectangle.md), [RotatedShape](rotatedshape.md), [RoundedRectangle](roundedrectangle.md), [TextInputBorderShape](textinputbordershape.md), [UnevenRoundedRectangle](unevenroundedrectangle.md)

## Topics

### Setting the stroke border characteristics

- [strokeBorder(_:lineWidth:antialiased:)](<insettableshape/strokeborder(__linewidth_antialiased_).md>) — Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with `content`. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [strokeBorder(lineWidth:antialiased:)](<insettableshape/strokeborder(linewidth_antialiased_).md>) — Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with the foreground color. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [strokeBorder(_:style:antialiased:)](<insettableshape/strokeborder(__style_antialiased_).md>) — Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with `content`.
- [strokeBorder(style:antialiased:)](<insettableshape/strokeborder(style_antialiased_).md>) — Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with the foreground color.

### Setting the inset

- [inset(by:)](<insettableshape/inset(by_).md>) — Returns `self` inset by `amount`.
- [InsetShape](insettableshape/insetshape.md) — The type of the inset shape.

## See Also

### Setting a container shape

- [containerShape(_:)](<view/containershape(__).md>) — Sets the container shape to use for any container relative shape or concentric rectangle within this view.
- [ContainerRelativeShape](containerrelativeshape.md) — A shape whose dimensions the system calculates from an inset version of the current container shape.
