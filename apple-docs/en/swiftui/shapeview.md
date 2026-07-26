---
title: ShapeView
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shapeview
source_url: 'https://developer.apple.com/documentation/swiftui/shapeview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapeview.json'
content_hash: 'sha256:140718dd688988c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ShapeView

<sub>Protocol</sub>

A view that provides a shape that you can use for drawing operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated protocol ShapeView<Content> : View
```

## Overview

Use this type with the drawing methods on [Shape](shape.md) to apply multiple fills and/or strokes to a shape. For example, the following code applies a fill and stroke to a capsule shape:

```swift
Capsule()
    .fill(.yellow)
    .stroke(.blue, lineWidth: 8)
```

## Relationships

- **Inherits From**: [View](view.md)

- **Conforming Types**: [FillShapeView](fillshapeview.md), [StrokeBorderShapeView](strokebordershapeview.md), [StrokeShapeView](strokeshapeview.md)

## Topics

### Getting the shape

- [shape](shapeview/shape.md) — The shape that this type draws and provides for other drawing operations.
- [Content](shapeview/content.md) — The type of shape this can provide.

### Modify the shape

- [fill(_:style:)](<shapeview/fill(__style_).md>) — Fills this shape with a color or gradient.
- [stroke(_:style:antialiased:)](<shapeview/stroke(__style_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:lineWidth:antialiased:)](<shapeview/stroke(__linewidth_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [strokeBorder(_:style:antialiased:)](<shapeview/strokeborder(__style_antialiased_).md>) — Returns a view that’s the result of insetting this view by half of its style’s line width.
- [strokeBorder(_:lineWidth:antialiased:)](<shapeview/strokeborder(__linewidth_antialiased_).md>) — Returns a view that’s the result of filling an inner stroke of this view with the content you supply.

## See Also

### Defining shape behavior

- [Shape](shape.md) — A 2D shape that you can use when drawing a view.
- [AnyShape](anyshape.md) — A type-erased shape value.
- [ShapeRole](shaperole.md) — Ways of styling a shape.
- [StrokeStyle](strokestyle.md) — The characteristics of a stroke that traces a path.
- [StrokeShapeView](strokeshapeview.md) — A shape provider that strokes its shape.
- [StrokeBorderShapeView](strokebordershapeview.md) — A shape provider that strokes the border of its shape.
- [FillStyle](fillstyle.md) — A style for rasterizing vector shapes.
- [FillShapeView](fillshapeview.md) — A shape provider that fills its shape.
