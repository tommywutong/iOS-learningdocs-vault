---
title: 'scaleEffect(x:y:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectcontent/scaleeffect(x:y:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectcontent/scaleeffect(x:y:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectcontent/scaleeffect%28x%3Ay%3Aanchor%3A%29.json'
content_hash: 'sha256:badd524d066e2bad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectContent](../hovereffectcontent.md)

# scaleEffect(x:y:anchor:)

<sub>Instance Method</sub>

Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.

<sub>visionOS</sub>

```swift
func scaleEffect(x: CGFloat = 1.0, y: CGFloat = 1.0, anchor: UnitPoint = .center) -> some HoverEffectContent

```

## Parameters

- `x` — An amount that represents the horizontal amount to scale the view. The default value is `1.0`.

- `y` — An amount that represents the vertical amount to scale the view. The default value is `1.0`.

- `anchor` — The point with a default of [center](../unitpoint/center.md) that defines the location within the view from which to apply the transformation.

## Return Value

An effect that scales the view’s rendered output.
