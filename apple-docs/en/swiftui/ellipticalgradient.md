---
title: EllipticalGradient
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/ellipticalgradient
source_url: 'https://developer.apple.com/documentation/swiftui/ellipticalgradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/ellipticalgradient.json'
content_hash: 'sha256:2abd4107ce079888'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EllipticalGradient

<sub>Structure</sub>

A radial gradient that draws an ellipse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct EllipticalGradient
```

## Overview

The gradient maps its coordinate space to the unit space square in which its center and radii are defined, then stretches that square to fill its bounding rect, possibly also stretching the circular gradient to have elliptical contours.

For example, an elliptical gradient centered on the view, filling its bounds:

```swift
EllipticalGradient(gradient: .init(colors: [.red, .yellow]))
```

When using an elliptical gradient as a shape style, you can also use [ellipticalGradient(_:center:startRadiusFraction:endRadiusFraction:)](<shapestyle/ellipticalgradient(__center_startradiusfraction_endradiusfraction_).md>).

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [ShapeStyle](shapestyle.md), [View](view.md)

## Topics

### Creating an elliptical gradient

- [init(gradient:center:startRadiusFraction:endRadiusFraction:)](<ellipticalgradient/init(gradient_center_startradiusfraction_endradiusfraction_).md>) — Creates an elliptical gradient.
- [init(colors:center:startRadiusFraction:endRadiusFraction:)](<ellipticalgradient/init(colors_center_startradiusfraction_endradiusfraction_).md>) — Creates an elliptical gradient from a collection of colors.
- [init(stops:center:startRadiusFraction:endRadiusFraction:)](<ellipticalgradient/init(stops_center_startradiusfraction_endradiusfraction_).md>) — Creates an elliptical gradient from a collection of color stops.

## See Also

### Supporting types

- [AngularGradient](angulargradient.md) — An angular gradient.
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
