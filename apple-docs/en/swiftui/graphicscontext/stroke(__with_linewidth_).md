---
title: 'stroke(_:with:lineWidth:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/stroke(_:with:linewidth:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/stroke(_:with:linewidth:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/stroke%28_%3Awith%3Alinewidth%3A%29.json'
content_hash: 'sha256:f1cfbcd44f9edc01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# stroke(_:with:lineWidth:)

<sub>Instance Method</sub>

Draws a path into the context with a specified line width.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stroke(_ path: Path, with shading: GraphicsContext.Shading, lineWidth: CGFloat = 1)
```

## Parameters

- `path` — The path to outline.

- `shading` — The color or pattern to use when outlining the `path`.

- `lineWidth` — The width of the stroke, which defaults to `1`.

## Discussion

When you call this method, all [StrokeStyle](../strokestyle.md) properties other than [lineWidth](../strokestyle/linewidth.md) take their default values. To control other style properties, use [stroke(_:with:style:)](<stroke(__with_style_).md>) instead.

## See Also

### Drawing a path

- [stroke(_:with:style:)](<stroke(__with_style_).md>) — Draws a path into the context with a specified stroke style.
- [fill(_:with:style:)](<fill(__with_style_).md>) — Draws a path into the context and fills the outlined region.
- [Shading](shading.md) — A color or pattern that you can use to outline or fill a path.
- [GradientOptions](gradientoptions.md) — Options that affect the rendering of color gradients.
