---
title: 'transformEffect(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectcontent/transformeffect(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectcontent/transformeffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectcontent/transformeffect%28_%3A%29.json'
content_hash: 'sha256:e8da31477a724ccd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectContent](../hovereffectcontent.md)

# transformEffect(_:)

<sub>Instance Method</sub>

Applies an affine transformation to the view’s rendered output.

<sub>visionOS</sub>

```swift
func transformEffect(_ transform: CGAffineTransform) -> some HoverEffectContent

```

## Parameters

- `transform` — A [CGAffineTransform](../../corefoundation/cgaffinetransform.md) to apply to the view.

## Return Value

An effect that applies an affine transformation to the view’s rendered output.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of the view according to the provided [CGAffineTransform](../../corefoundation/cgaffinetransform.md).
