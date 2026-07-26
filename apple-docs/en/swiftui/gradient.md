---
title: Gradient
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gradient
source_url: 'https://developer.apple.com/documentation/swiftui/gradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gradient.json'
content_hash: 'sha256:ca78fffbf22d1f63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Gradient

<sub>Structure</sub>

A color gradient represented as an array of color stops, each having a parametric location value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Gradient
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ScaleRange](../charts/scalerange.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [ShapeStyle](shapestyle.md)

## Topics

### Creating a gradient from colors

- [init(colors:)](<gradient/init(colors_).md>) — Creates a gradient from an array of colors.

### Creating a gradient from stops

- [init(stops:)](<gradient/init(stops_).md>) — Creates a gradient from an array of color stops.
- [stops](gradient/stops.md) — The array of color stops.
- [Stop](gradient/stop.md) — One color stop in the gradient.

### Working with color spaces

- [colorSpace(_:)](<gradient/colorspace(__).md>) — Returns a version of the gradient that will use a specified color space for interpolating between its colors.
- [ColorSpace](gradient/colorspace.md) — A method of interpolating between the colors in a gradient.

## See Also

### Styling content

- [border(_:width:)](<view/border(__width_).md>) — Adds a border to this view with the specified style and width.
- [foregroundStyle(_:)](<view/foregroundstyle(__).md>) — Sets a view’s foreground elements to use a given style.
- [foregroundStyle(_:_:)](<view/foregroundstyle(____).md>) — Sets the primary and secondary levels of the foreground style in the child view.
- [foregroundStyle(_:_:_:)](<view/foregroundstyle(______).md>) — Sets the primary, secondary, and tertiary levels of the foreground style.
- [backgroundStyle(_:)](<view/backgroundstyle(__).md>) — Sets the specified style to render backgrounds within the view.
- [backgroundStyle](environmentvalues/backgroundstyle.md) — An optional style that overrides the default system background style when set.
- [ShapeStyle](shapestyle.md) — A color or pattern to use when rendering a shape.
- [AnyShapeStyle](anyshapestyle.md) — A type-erased ShapeStyle value.
- [MeshGradient](meshgradient.md) — A two-dimensional gradient defined by a 2D grid of positioned colors.
- [AnyGradient](anygradient.md) — A color gradient.
- [ShadowStyle](shadowstyle.md) — A style to use when rendering shadows.
- [Glass](glass.md) — A structure that defines the configuration of the Liquid Glass material.
