---
title: 'opacity(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectcontent/opacity(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectcontent/opacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectcontent/opacity%28_%3A%29.json'
content_hash: 'sha256:3d3a60b33a0ab0f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectContent](../hovereffectcontent.md)

# opacity(_:)

<sub>Instance Method</sub>

Sets the transparency of the view.

<sub>visionOS</sub>

```swift
func opacity(_ opacity: Double) -> some HoverEffectContent

```

## Parameters

- `opacity` — A value between 0 (fully transparent) and 1 (fully opaque).

## Return Value

An effect that sets the transparency of the view.

## Discussion

When applying the `opacity(_:)` effect to a view that has already had its opacity transformed, the effect of the underlying opacity transformation is multiplied.
