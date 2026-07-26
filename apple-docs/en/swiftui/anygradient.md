---
title: AnyGradient
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/anygradient
source_url: 'https://developer.apple.com/documentation/swiftui/anygradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anygradient.json'
content_hash: 'sha256:eea55364628b0194'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnyGradient

<sub>Structure</sub>

A color gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnyGradient
```

## Overview

When used as a [ShapeStyle](shapestyle.md), this type draws a linear gradient with start-point [0.5, 0] and end-point [0.5, 1].

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ScaleRange](../charts/scalerange.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [ShapeStyle](shapestyle.md)

## Topics

### Creating a gradient

- [init(_:)](<anygradient/init(__).md>) — Creates a new instance from the specified gradient.

### Working with color spaces

- [colorSpace(_:)](<anygradient/colorspace(__).md>) — Returns a version of the gradient that will use a specified color space for interpolating between its colors.

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
- [MeshGradient](meshgradient.md) — A two-dimensional gradient defined by a 2D grid of positioned colors.
- [ShadowStyle](shadowstyle.md) — A style to use when rendering shadows.
- [Glass](glass.md) — A structure that defines the configuration of the Liquid Glass material.
