---
title: FillStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fillstyle
source_url: 'https://developer.apple.com/documentation/swiftui/fillstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fillstyle.json'
content_hash: 'sha256:ce39d7f43639be56'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FillStyle

<sub>Structure</sub>

A style for rasterizing vector shapes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct FillStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a fill style

- [init(eoFill:antialiased:)](<fillstyle/init(eofill_antialiased_).md>) — Creates a new fill style with the specified settings.

### Setting fill style properties

- [isEOFilled](fillstyle/iseofilled.md) — A Boolean value that indicates whether to use the even-odd rule when rendering a shape.
- [isAntialiased](fillstyle/isantialiased.md) — A Boolean value that indicates whether to apply antialiasing to the edges of a shape.

## See Also

### Defining shape behavior

- [ShapeView](shapeview.md) — A view that provides a shape that you can use for drawing operations.
- [Shape](shape.md) — A 2D shape that you can use when drawing a view.
- [AnyShape](anyshape.md) — A type-erased shape value.
- [ShapeRole](shaperole.md) — Ways of styling a shape.
- [StrokeStyle](strokestyle.md) — The characteristics of a stroke that traces a path.
- [StrokeShapeView](strokeshapeview.md) — A shape provider that strokes its shape.
- [StrokeBorderShapeView](strokebordershapeview.md) — A shape provider that strokes the border of its shape.
- [FillShapeView](fillshapeview.md) — A shape provider that fills its shape.
