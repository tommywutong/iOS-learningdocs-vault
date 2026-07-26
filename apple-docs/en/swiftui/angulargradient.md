---
title: AngularGradient
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/angulargradient
source_url: 'https://developer.apple.com/documentation/swiftui/angulargradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/angulargradient.json'
content_hash: 'sha256:44dc43dc2df4e306'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AngularGradient

<sub>Structure</sub>

An angular gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct AngularGradient
```

## Overview

An angular gradient is also known as a “conic” gradient. This gradient applies the color function as the angle changes, relative to a center point and defined start and end angles. If `endAngle - startAngle > 2π`, the gradient only draws the last complete turn. If `endAngle - startAngle < 2π`, the gradient fills the missing area with the colors defined by gradient locations one and zero, transitioning between the two halfway across the missing area. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

When using an angular gradient as a shape style, you can also use [angularGradient(_:center:startAngle:endAngle:)](<shapestyle/angulargradient(__center_startangle_endangle_).md>), [conicGradient(_:center:angle:)](<shapestyle/conicgradient(__center_angle_).md>), or similar methods.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [ShapeStyle](shapestyle.md), [View](view.md)

## Topics

### Creating a full rotation angular gradient

- [init(gradient:center:angle:)](<angulargradient/init(gradient_center_angle_).md>) — Creates a conic gradient that completes a full turn.
- [init(colors:center:angle:)](<angulargradient/init(colors_center_angle_).md>) — Creates a conic gradient from a collection of colors that completes a full turn.
- [init(stops:center:angle:)](<angulargradient/init(stops_center_angle_).md>) — Creates a conic gradient from a collection of color stops that completes a full turn.

### Creating a partial rotation angular gradient

- [init(gradient:center:startAngle:endAngle:)](<angulargradient/init(gradient_center_startangle_endangle_).md>) — Creates an angular gradient.
- [init(colors:center:startAngle:endAngle:)](<angulargradient/init(colors_center_startangle_endangle_).md>) — Creates an angular gradient from a collection of colors.
- [init(stops:center:startAngle:endAngle:)](<angulargradient/init(stops_center_startangle_endangle_).md>) — Creates an angular gradient from a collection of color stops.

## See Also

### Supporting types

- [EllipticalGradient](ellipticalgradient.md) — A radial gradient that draws an ellipse.
- [LinearGradient](lineargradient.md) — A linear gradient.
- [RadialGradient](radialgradient.md) — A radial gradient.
- [Material](material.md) — A background material type.
- [ImagePaint](imagepaint.md) — A shape style that fills a shape by repeating a region of an image.
- [HierarchicalShapeStyle](hierarchicalshapestyle.md) — A shape style that maps to one of the numbered content styles.
- [HierarchicalShapeStyleModifier](hierarchicalshapestylemodifier.md) — Styles that you can apply to hierarchical shapes.
- [ForegroundStyle](foregroundstyle.md) — The foreground style in the current context.
- [BackgroundStyle](backgroundstyle.md) — The background style in the current context.
- [SelectionShapeStyle](selectionshapestyle.md) — A style used to visually indicate selection following platform conventional colors and behaviors.
- [SeparatorShapeStyle](separatorshapestyle.md) — A style appropriate for foreground separator or border lines.
- [TintShapeStyle](tintshapestyle.md) — A style that reflects the current tint color.
- [FillShapeStyle](fillshapestyle.md) — A shape style that displays one of the overlay fills.
- [LinkShapeStyle](linkshapestyle.md) — A style appropriate for links.
- [PlaceholderTextShapeStyle](placeholdertextshapestyle.md) — A style appropriate for placeholder text.
