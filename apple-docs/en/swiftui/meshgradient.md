---
title: MeshGradient
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/meshgradient
source_url: 'https://developer.apple.com/documentation/swiftui/meshgradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/meshgradient.json'
content_hash: 'sha256:86054862762eda1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MeshGradient

<sub>Structure</sub>

A two-dimensional gradient defined by a 2D grid of positioned colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct MeshGradient
```

## Overview

Each vertex has a position, a color and four surrounding Bezier control points (leading, top, trailing, bottom) that define the tangents connecting the vertex with its four neighboring vertices. (Vertices on the corners or edges of the mesh have less than four neighbors, they ignore their extra control points.) Control points may either be specified explicitly or implicitly.

When rendering, a tessellated sequence of Bezier patches are created, and vertex colors are interpolated across each patch, either linearly, or via another set of cubic curves derived from how the colors change between neighbors – the latter typically gives smoother color transitions.

```swift
MeshGradient(width: 3, height: 3, points: [
    .init(0, 0), .init(0.5, 0), .init(1, 0),
    .init(0, 0.5), .init(0.5, 0.5), .init(1, 0.5),
    .init(0, 1), .init(0.5, 1), .init(1, 1)
], colors: [
    .red, .purple, .indigo,
    .orange, .white, .blue,
    .yellow, .green, .mint
])
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [ShapeStyle](shapestyle.md), [View](view.md)

## Topics

### Structures

- [BezierPoint](meshgradient/bezierpoint.md) — One location in a gradient mesh, along with the four Bezier control points surrounding it.

### Initializers

- [init(width:height:bezierPoints:colors:background:smoothsColors:colorSpace:)](<meshgradient/init(width_height_bezierpoints_colors_background_smoothscolors_colorspace_).md>) — Creates a new gradient mesh specified as a 2D grid of colored points, specifying the Bezier control points explicitly.
- [init(width:height:bezierPoints:resolvedColors:background:smoothsColors:colorSpace:)](<meshgradient/init(width_height_bezierpoints_resolvedcolors_background_smoothscolors_colorspace_).md>) — Creates a new gradient mesh specified as a 2D grid of colored points, specifying the Bezier control points explicitly, with already-resolved sRGB colors.
- [init(width:height:locations:colors:background:smoothsColors:colorSpace:)](<meshgradient/init(width_height_locations_colors_background_smoothscolors_colorspace_).md>) — Creates a new gradient mesh specified as a 2D grid of colored vertices.
- [init(width:height:points:colors:background:smoothsColors:colorSpace:)](<meshgradient/init(width_height_points_colors_background_smoothscolors_colorspace_).md>) — Creates a new gradient mesh specified as a 2D grid of colored points.
- [init(width:height:points:resolvedColors:background:smoothsColors:colorSpace:)](<meshgradient/init(width_height_points_resolvedcolors_background_smoothscolors_colorspace_).md>) — Creates a new gradient mesh specified as a 2D grid of colored points, with already-resolved sRGB colors.

### Instance Properties

- [background](meshgradient/background.md) — The background color, this fills any points outside the defined vertex mesh.
- [colorSpace](meshgradient/colorspace.md) — The color space in which to interpolate vertex colors.
- [colors](meshgradient/colors-swift.property.md) — The array of colors. Must contain `width x height` elements.
- [height](meshgradient/height.md) — The height of the mesh, i.e. the number of vertices per column.
- [locations](meshgradient/locations-swift.property.md) — The array of locations. Must contain `width x height` elements.
- [smoothsColors](meshgradient/smoothscolors.md) — Whether cubic (smooth) interpolation should be used for the colors in the mesh (rather than only for the shape of the mesh).
- [width](meshgradient/width.md) — The width of the mesh, i.e. the number of vertices per row.

### Enumerations

- [Colors](meshgradient/colors-swift.enum.md) — An array of colors.
- [Locations](meshgradient/locations-swift.enum.md) — An array of 2D locations and their control points.

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
- [Gradient](gradient.md) — A color gradient represented as an array of color stops, each having a parametric location value.
- [AnyGradient](anygradient.md) — A color gradient.
- [ShadowStyle](shadowstyle.md) — A style to use when rendering shadows.
- [Glass](glass.md) — A structure that defines the configuration of the Liquid Glass material.
