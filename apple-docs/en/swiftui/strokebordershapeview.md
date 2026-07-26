---
title: StrokeBorderShapeView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/strokebordershapeview
source_url: 'https://developer.apple.com/documentation/swiftui/strokebordershapeview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/strokebordershapeview.json'
content_hash: 'sha256:cd6947aa8366c1f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# StrokeBorderShapeView

<sub>Structure</sub>

A shape provider that strokes the border of its shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct StrokeBorderShapeView<Content, Style, Background> where Content : InsettableShape, Style : ShapeStyle, Background : View
```

## Overview

You don’t create this type directly; it’s the return type of `Shape.strokeBorder`.

## Relationships

- **Conforms To**: [ShapeView](shapeview.md), [View](view.md)

## Topics

### Creating a stroke border shape view

- [init(shape:style:strokeStyle:isAntialiased:background:)](<strokebordershapeview/init(shape_style_strokestyle_isantialiased_background_).md>) — Create a stroke border shape.

### Getting shape view properties

- [background](strokebordershapeview/background.md) — The background shown beneath this view.
- [isAntialiased](strokebordershapeview/isantialiased.md) — Whether this shape should be drawn antialiased.
- [shape](strokebordershapeview/shape.md) — The shape that this type draws and provides for other drawing operations.
- [strokeStyle](strokebordershapeview/strokestyle.md) — The stroke style used when stroking this view’s shape.
- [style](strokebordershapeview/style.md) — The style that strokes the border of this view’s shape.

## See Also

### Defining shape behavior

- [ShapeView](shapeview.md) — A view that provides a shape that you can use for drawing operations.
- [Shape](shape.md) — A 2D shape that you can use when drawing a view.
- [AnyShape](anyshape.md) — A type-erased shape value.
- [ShapeRole](shaperole.md) — Ways of styling a shape.
- [StrokeStyle](strokestyle.md) — The characteristics of a stroke that traces a path.
- [StrokeShapeView](strokeshapeview.md) — A shape provider that strokes its shape.
- [FillStyle](fillstyle.md) — A style for rasterizing vector shapes.
- [FillShapeView](fillshapeview.md) — A shape provider that fills its shape.
