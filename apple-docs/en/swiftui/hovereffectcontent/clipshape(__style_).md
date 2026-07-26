---
title: 'clipShape(_:style:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectcontent/clipshape(_:style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectcontent/clipshape(_:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectcontent/clipshape%28_%3Astyle%3A%29.json'
content_hash: 'sha256:b21fc1c02722826e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectContent](../hovereffectcontent.md)

# clipShape(_:style:)

<sub>Instance Method</sub>

Sets a clipping shape for the view.

<sub>visionOS</sub>

```swift
func clipShape<S>(_ shape: S, style: FillStyle = FillStyle()) -> some HoverEffectContent where S : Shape

```

## Parameters

- `shape` — The clipping shape to use for the view. The `shape` fills the view’s frame, while maintaining its aspect ratio.

- `style` — The fill style to use when rasterizing `shape`.

## Return Value

An effect that sets the clip shape of a view.

## Discussion

Use `clipShape(_:style:)` to clip the view’s rendered output to the provided shape. By applying a clipping shape, you preserve the parts of the view covered by the shape, while eliminating other parts of the view. The clipping shape itself isn’t visible.
