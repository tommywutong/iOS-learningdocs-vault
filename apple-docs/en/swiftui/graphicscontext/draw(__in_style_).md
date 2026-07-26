---
title: 'draw(_:in:style:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/draw(_:in:style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:in:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/draw%28_%3Ain%3Astyle%3A%29.json'
content_hash: 'sha256:04588e04927f22ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# draw(_:in:style:)

<sub>Instance Method</sub>

Draws a resolved image into the context, using the specified rectangle as a layout frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func draw(_ image: GraphicsContext.ResolvedImage, in rect: CGRect, style: FillStyle = FillStyle())
```

## Parameters

- `image` — The [ResolvedImage](resolvedimage.md) to draw. Get a resolved image from an [Image](../image.md) by calling [resolve(_:)](<resolve(__)-898z6.md>). Alternatively, you can call [draw(_:in:style:)](<draw(__in_style_)-blhz.md>) with an [Image](../image.md), and that method performs the resolution automatically.

- `rect` — The rectangle in the current user space to draw the image in.

- `style` — A fill style to use when rasterizing the image.

## Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the image.

## See Also

### Drawing images, text, and views

- [draw(_:in:)](<draw(__in_).md>) — Draws a resolved symbol into the context, using the specified rectangle as a layout frame.
- [draw(_:at:anchor:)](<draw(__at_anchor_).md>) — Draws a resolved image into the context, aligning an anchor within the image to a point in the context.
