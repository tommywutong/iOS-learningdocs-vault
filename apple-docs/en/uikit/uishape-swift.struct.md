---
title: UIShape
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uishape-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uishape-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-swift.struct.json'
content_hash: 'sha256:146bac545eb508b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIShape

<sub>Structure</sub>

An abstract representation of a shape.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct UIShape
```

## Overview

A [UIShape](uishape-swift.struct.md) can represent different types of shapes, including:

- A simple shape like a rectangle or circle that resolves into a concrete shape according to context (like size and position)
- A Bézier path
- A dynamic shape that resolves using a custom closure

You typically use a [UIShape](uishape-swift.struct.md) with APIs like [UIHoverStyle](uihoverstyle.md) to represent the shape of an effect.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [UIShapeProvider](uishapeprovider-60loj.md)

## Topics

### Creating a hover shape

- [rect](uishape-swift.struct/rect.md) — Creates a rectangular shape.
- [capsule](uishape-swift.struct/capsule.md) — Creates a capsule shape, a rounded rectangle with a corner radius equal to half the length of the rectangle’s smallest edge.
- [circle](uishape-swift.struct/circle.md) — Creates a circular shape, with a radius equal to half the length of the frame rectangle’s smallest edge.
- [rect(cornerRadius:cornerCurve:maskedCorners:)](<uishape-swift.struct/rect(cornerradius_cornercurve_maskedcorners_).md>) — Creates a rectangular shape with rounded corners, using the provided corner radius, corner curve, and rectangle corners.
- [fixedRect(_:cornerRadius:cornerCurve:maskedCorners:)](<uishape-swift.struct/fixedrect(__cornerradius_cornercurve_maskedcorners_).md>) — Creates a fixed rectangular shape that uses the provided rectangle as its shape, regardless of the frame that contains it.
- [UICornerCurve](uicornercurve.md) — The corner curve to apply to a view.

### Creating a hover shape from a custom path

- [path(_:)](<uishape-swift.struct/path(__).md>) — Creates a shape with a custom Bézier path.

### Creating a dynamic hover shape

- [init(_:)](<uishape-swift.struct/init(__).md>) — Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [UIShapeProvider](uishapeprovider-60loj.md) — An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [ResolutionContext](uishape-swift.struct/resolutioncontext.md) — The context for resolving a dynamic shape.
- [Resolved](uishape-swift.struct/resolved.md) — A shape that has completely resolved based on a context.

### Creating a shape by applying insets

- [inset(by:)](<uishape-swift.struct/inset(by_)-5jxgl.md>) — Creates a new modified shape by applying the provided insets to this shape.
- [inset(by:)](<uishape-swift.struct/inset(by_)-7v5nk.md>) — Creates a new modified shape by applying the provided inset to this shape.

## See Also

### Specifying a hover shape

- [shape](uihoverstyle/shape-21npk.md) — The shape to use for the hover effect.
