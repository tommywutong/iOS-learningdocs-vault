---
title: 'fill(_:with:style:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/fill(_:with:style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/fill(_:with:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/fill%28_%3Awith%3Astyle%3A%29.json'
content_hash: 'sha256:be197d85092f6208'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# fill(_:with:style:)

<sub>Instance Method</sub>

Draws a path into the context and fills the outlined region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fill(_ path: Path, with shading: GraphicsContext.Shading, style: FillStyle = FillStyle())
```

## Parameters

- `path` — The outline of the region to fill.

- `shading` — The color or pattern to use when filling the region bounded by `path`.

- `style` — A style that indicates how to rasterize the path.

## Discussion

The current drawing state of the context defines the full drawing operation. For example, the current transformation and clip shapes, and any styles applied to the result, affect the final result.

## See Also

### Drawing a path

- [stroke(_:with:lineWidth:)](<stroke(__with_linewidth_).md>) — Draws a path into the context with a specified line width.
- [stroke(_:with:style:)](<stroke(__with_style_).md>) — Draws a path into the context with a specified stroke style.
- [Shading](shading.md) — A color or pattern that you can use to outline or fill a path.
- [GradientOptions](gradientoptions.md) — Options that affect the rendering of color gradients.
