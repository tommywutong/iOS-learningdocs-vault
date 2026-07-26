---
title: UIGraphicsDrawingActions
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsdrawingactions
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsdrawingactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsdrawingactions.json'
content_hash: 'sha256:e380b6d0dd518ec8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsDrawingActions

<sub>Type Alias</sub>

A closure that executes a set of drawing instructions that the renderer applies to the Core Graphics context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias UIGraphicsDrawingActions = (UIGraphicsRendererContext) -> Void
```

## Discussion

[UIGraphicsDrawingActions](uigraphicsdrawingactions.md) defines a block type that takes a [UIGraphicsRendererContext](uigraphicsrenderercontext.md) object as an argument and has no return value.

You provide a block of this type as an argument to the graphics drawing methods on [UIGraphicsRenderer](uigraphicsrenderer.md). Your block should use the provided renderer context to perform the drawing operations you want the renderer to execute.

## See Also

### Related Documentation

- [DrawingActions](uigraphicsimagerenderer/drawingactions.md) — A closure for drawing an image.
- [DrawingActions](uigraphicspdfrenderer/drawingactions.md) — A closure for drawing PDF content.

### Running the drawing actions

- [- runDrawingActions:completionActions:error:](<uigraphicsrenderer/rundrawingactions(__completionactions_).md>) — Performs drawing actions on a Core Graphics context that the renderer prepares.
