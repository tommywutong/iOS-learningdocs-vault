---
title: 'stroke(_:with:style:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/stroke(_:with:style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/stroke(_:with:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/stroke%28_%3Awith%3Astyle%3A%29.json'
content_hash: 'sha256:7f02f88ff13e314e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# stroke(_:with:style:)

<sub>Instance Method</sub>

Draws a path into the context with a specified stroke style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stroke(_ path: Path, with shading: GraphicsContext.Shading, style: StrokeStyle)
```

## Parameters

- `path` — The path to outline.

- `shading` — The color or pattern to use when outlining the `path`.

- `style` — A style that indicates how to outline the path.

## Discussion

If you only need to control the style’s [lineWidth](../strokestyle/linewidth.md) property, use [stroke(_:with:lineWidth:)](<stroke(__with_linewidth_).md>) instead.

## See Also

### Drawing a path

- [stroke(_:with:lineWidth:)](<stroke(__with_linewidth_).md>) — Draws a path into the context with a specified line width.
- [fill(_:with:style:)](<fill(__with_style_).md>) — Draws a path into the context and fills the outlined region.
- [Shading](shading.md) — A color or pattern that you can use to outline or fill a path.
- [GradientOptions](gradientoptions.md) — Options that affect the rendering of color gradients.
