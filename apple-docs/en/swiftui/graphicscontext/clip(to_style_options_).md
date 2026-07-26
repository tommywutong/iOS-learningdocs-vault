---
title: 'clip(to:style:options:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/clip(to:style:options:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/clip(to:style:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/clip%28to%3Astyle%3Aoptions%3A%29.json'
content_hash: 'sha256:ab10c6b8f47c0698'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# clip(to:style:options:)

<sub>Instance Method</sub>

Adds a path to the context’s array of clip shapes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func clip(to path: Path, style: FillStyle = FillStyle(), options: GraphicsContext.ClipOptions = ClipOptions())
```

## Parameters

- `path` — A [Path](../path.md) that defines the shape of the clipping mask.

- `style` — A [FillStyle](../fillstyle.md) that defines how to rasterize the shape.

- `options` — Clip options that tell SwiftUI how to interpret the `path` as a clip shape. For example, you can invert the clip shape by setting the [inverse](clipoptions/inverse.md) option.

## Discussion

Call this method to add a shape to the array of clip shapes that the context uses to define a clipping mask. Shapes that you add affect only subsequent drawing operations.

## See Also

### Masking

- [clipToLayer(opacity:options:content:)](<cliptolayer(opacity_options_content_).md>) — Adds a clip shape that you define in a new layer to the context’s array of clip shapes.
- [clipBoundingRect](clipboundingrect.md) — The bounding rectangle of the intersection of all current clip shapes in the current user space.
- [ClipOptions](clipoptions.md) — Options that affect the use of clip shapes.
