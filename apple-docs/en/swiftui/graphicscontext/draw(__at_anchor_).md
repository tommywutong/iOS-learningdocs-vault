---
title: 'draw(_:at:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/draw(_:at:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:at:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/draw%28_%3Aat%3Aanchor%3A%29.json'
content_hash: 'sha256:fba208f47879596a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# draw(_:at:anchor:)

<sub>Instance Method</sub>

Draws a resolved image into the context, aligning an anchor within the image to a point in the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func draw(_ image: GraphicsContext.ResolvedImage, at point: CGPoint, anchor: UnitPoint = .center)
```

## Parameters

- `image` — The [ResolvedImage](resolvedimage.md) to draw. Get a resolved image from an [Image](../image.md) by calling [resolve(_:)](<resolve(__)-898z6.md>). Alternatively, you can call [draw(_:at:anchor:)](<draw(__at_anchor_)-7l217.md>) with an [Image](../image.md), and that method performs the resolution automatically.

- `point` — A point within the rectangle of the resolved image to anchor to a point in the context.

- `anchor` — A [UnitPoint](../unitpoint.md) within the context to align the image with. The default is [center](../unitpoint/center.md).

## Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the image.

## See Also

### Drawing images, text, and views

- [draw(_:in:)](<draw(__in_).md>) — Draws a resolved symbol into the context, using the specified rectangle as a layout frame.
- [draw(_:in:style:)](<draw(__in_style_).md>) — Draws a resolved image into the context, using the specified rectangle as a layout frame.
