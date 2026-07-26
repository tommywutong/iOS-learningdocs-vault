---
title: AnyShape
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/anyshape
source_url: 'https://developer.apple.com/documentation/swiftui/anyshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anyshape.json'
content_hash: 'sha256:2aa5b34f5b277aae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnyShape

<sub>Structure</sub>

A type-erased shape value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnyShape
```

## Overview

You can use this type to dynamically switch between shape types:

```swift
struct MyClippedView: View {
    var isCircular: Bool

    var body: some View {
        OtherView().clipShape(isCircular ?
            AnyShape(Circle()) : AnyShape(Capsule()))
    }
}
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

## Topics

### Creating a shape

- [init(_:)](<anyshape/init(__).md>) — Create an any shape instance from a shape.

## See Also

### Defining shape behavior

- [ShapeView](shapeview.md) — A view that provides a shape that you can use for drawing operations.
- [Shape](shape.md) — A 2D shape that you can use when drawing a view.
- [ShapeRole](shaperole.md) — Ways of styling a shape.
- [StrokeStyle](strokestyle.md) — The characteristics of a stroke that traces a path.
- [StrokeShapeView](strokeshapeview.md) — A shape provider that strokes its shape.
- [StrokeBorderShapeView](strokebordershapeview.md) — A shape provider that strokes the border of its shape.
- [FillStyle](fillstyle.md) — A style for rasterizing vector shapes.
- [FillShapeView](fillshapeview.md) — A shape provider that fills its shape.
