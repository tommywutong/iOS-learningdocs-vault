---
title: RadialGradient
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/radialgradient
source_url: 'https://developer.apple.com/documentation/swiftui/radialgradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/radialgradient.json'
content_hash: 'sha256:66bc52eda90fd49c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RadialGradient

<sub>Structure</sub>

A radial gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct RadialGradient
```

## Overview

The gradient applies the color function as the distance from a center point, scaled to fit within the defined start and end radii. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

When using a radial gradient as a shape style, you can also use [radialGradient(_:center:startRadius:endRadius:)](<shapestyle/radialgradient(__center_startradius_endradius_).md>).

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [ShapeStyle](shapestyle.md), [View](view.md)

## Topics

### Creating a radial gradient

- [init(gradient:center:startRadius:endRadius:)](<radialgradient/init(gradient_center_startradius_endradius_).md>) — Creates a radial gradient from a base gradient.
- [init(colors:center:startRadius:endRadius:)](<radialgradient/init(colors_center_startradius_endradius_).md>) — Creates a radial gradient from a collection of colors.
- [init(stops:center:startRadius:endRadius:)](<radialgradient/init(stops_center_startradius_endradius_).md>) — Creates a radial gradient from a collection of color stops.

## See Also

### Supporting types

- [AngularGradient](angulargradient.md) — An angular gradient.
- [EllipticalGradient](ellipticalgradient.md) — A radial gradient that draws an ellipse.
- [LinearGradient](lineargradient.md) — A linear gradient.
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
