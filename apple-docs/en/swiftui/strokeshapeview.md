---
title: StrokeShapeView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/strokeshapeview
source_url: 'https://developer.apple.com/documentation/swiftui/strokeshapeview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/strokeshapeview.json'
content_hash: 'sha256:313113ee2e8be3fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# StrokeShapeView

<sub>Structure</sub>

A shape provider that strokes its shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct StrokeShapeView<Content, Style, Background> where Content : Shape, Style : ShapeStyle, Background : View
```

## Overview

You don’t create this type directly; it’s the return type of `Shape.stroke`.

## Relationships

- **Conforms To**: [ShapeView](shapeview.md), [View](view.md)

## Topics

### Creating a stroke shape view

- [init(shape:style:strokeStyle:isAntialiased:background:)](<strokeshapeview/init(shape_style_strokestyle_isantialiased_background_).md>) — Create a StrokeShapeView.

### Getting shape view properties

- [background](strokeshapeview/background.md) — The background shown beneath this view.
- [isAntialiased](strokeshapeview/isantialiased.md) — Whether this shape should be drawn antialiased.
- [shape](strokeshapeview/shape.md) — The shape that this type draws and provides for other drawing operations.
- [strokeStyle](strokeshapeview/strokestyle.md) — The stroke style used when stroking this view’s shape.
- [style](strokeshapeview/style.md) — The style that strokes this view’s shape.

## See Also

### Defining shape behavior

- [ShapeView](shapeview.md) — A view that provides a shape that you can use for drawing operations.
- [Shape](shape.md) — A 2D shape that you can use when drawing a view.
- [AnyShape](anyshape.md) — A type-erased shape value.
- [ShapeRole](shaperole.md) — Ways of styling a shape.
- [StrokeStyle](strokestyle.md) — The characteristics of a stroke that traces a path.
- [StrokeBorderShapeView](strokebordershapeview.md) — A shape provider that strokes the border of its shape.
- [FillStyle](fillstyle.md) — A style for rasterizing vector shapes.
- [FillShapeView](fillshapeview.md) — A shape provider that fills its shape.
