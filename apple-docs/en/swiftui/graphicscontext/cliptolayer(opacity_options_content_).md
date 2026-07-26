---
title: 'clipToLayer(opacity:options:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/cliptolayer(opacity:options:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/cliptolayer(opacity:options:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/cliptolayer%28opacity%3Aoptions%3Acontent%3A%29.json'
content_hash: 'sha256:3cd00f497028d426'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# clipToLayer(opacity:options:content:)

<sub>Instance Method</sub>

Adds a clip shape that you define in a new layer to the context’s array of clip shapes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func clipToLayer(opacity: Double = 1, options: GraphicsContext.ClipOptions = ClipOptions(), content: (inout GraphicsContext) throws -> Void) rethrows
```

## Parameters

- `opacity` — A value that SwiftUI uses to multiply the alpha channel of the rasterized layer that you define in the `content` closure. The alpha values that result define the clip shape.

- `options` — A set of options that tell SwiftUI how to interpret the clip shape. For example, you can invert the clip shape by setting the [inverse](clipoptions/inverse.md) option.

- `content` — A closure that receives as input a new [GraphicsContext](../graphicscontext.md), which represents a new transparency layer. The alpha channel of content that you draw into this context, multiplied by the `opacity` parameter, defines the clip shape.

## Discussion

Call this method to add a shape to the array of clip shapes that the context uses to define a clipping mask. Shapes that you add affect only subsequent drawing operations.

## See Also

### Masking

- [clip(to:style:options:)](<clip(to_style_options_).md>) — Adds a path to the context’s array of clip shapes.
- [clipBoundingRect](clipboundingrect.md) — The bounding rectangle of the intersection of all current clip shapes in the current user space.
- [ClipOptions](clipoptions.md) — Options that affect the use of clip shapes.
