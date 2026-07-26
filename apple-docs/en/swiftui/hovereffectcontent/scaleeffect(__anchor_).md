---
title: 'scaleEffect(_:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectcontent/scaleeffect(_:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectcontent/scaleeffect(_:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectcontent/scaleeffect%28_%3Aanchor%3A%29.json'
content_hash: 'sha256:5876bb71c4ce0af8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectContent](../hovereffectcontent.md)

# scaleEffect(_:anchor:)

<sub>Instance Method</sub>

Scales the view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.

<sub>visionOS</sub>

```swift
func scaleEffect(_ scale: CGFloat, anchor: UnitPoint = .center) -> some HoverEffectContent

```

## Parameters

- `scale` — The amount to scale the view in the view in both the horizontal and vertical directions.

- `anchor` — The point with a default of [center](../unitpoint/center.md) that defines the location within the view from which to apply the transformation.

## Return Value

An effect that scales the view’s rendered output.
