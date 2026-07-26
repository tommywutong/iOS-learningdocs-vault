---
title: FillShapeView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fillshapeview
source_url: 'https://developer.apple.com/documentation/swiftui/fillshapeview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fillshapeview.json'
content_hash: 'sha256:d9dd992c8e38aca0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FillShapeView

<sub>Structure</sub>

A shape provider that fills its shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct FillShapeView<Content, Style, Background> where Content : Shape, Style : ShapeStyle, Background : View
```

## Overview

You do not create this type directly, it is the return type of `Shape.fill`.

## Relationships

- **Conforms To**: [ShapeView](shapeview.md), [View](view.md)

## Topics

### Creating a stroke shape view

- [init(shape:style:fillStyle:background:)](<fillshapeview/init(shape_style_fillstyle_background_).md>) — Create a FillShapeView.

### Getting shape view properties

- [background](fillshapeview/background.md) — The background shown beneath this view.
- [fillStyle](fillshapeview/fillstyle.md) — The fill style used when filling this view’s shape.
- [shape](fillshapeview/shape.md) — The shape that this type draws and provides for other drawing operations.
- [style](fillshapeview/style.md) — The style that fills this view’s shape.

## See Also

### Defining shape behavior

- [ShapeView](shapeview.md) — A view that provides a shape that you can use for drawing operations.
- [Shape](shape.md) — A 2D shape that you can use when drawing a view.
- [AnyShape](anyshape.md) — A type-erased shape value.
- [ShapeRole](shaperole.md) — Ways of styling a shape.
- [StrokeStyle](strokestyle.md) — The characteristics of a stroke that traces a path.
- [StrokeShapeView](strokeshapeview.md) — A shape provider that strokes its shape.
- [StrokeBorderShapeView](strokebordershapeview.md) — A shape provider that strokes the border of its shape.
- [FillStyle](fillstyle.md) — A style for rasterizing vector shapes.
