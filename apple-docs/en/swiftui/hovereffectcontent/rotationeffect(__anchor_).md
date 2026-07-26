---
title: 'rotationEffect(_:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/hovereffectcontent/rotationeffect(_:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectcontent/rotationeffect(_:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectcontent/rotationeffect%28_%3Aanchor%3A%29.json'
content_hash: 'sha256:b2402623b19ea349'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectContent](../hovereffectcontent.md)

# rotationEffect(_:anchor:)

<sub>Instance Method</sub>

Rotates content in two dimensions around the specified point.

<sub>visionOS</sub>

```swift
func rotationEffect(_ angle: Angle, anchor: UnitPoint = .center) -> some HoverEffectContent

```

## Parameters

- `angle` — The angle by which to rotate the content.

- `anchor` — A unit point within the content about which to perform the rotation. The default value is [center](../unitpoint/center.md).

## Return Value

A rotation effect.

## Discussion

This effect rotates the content around the axis that points out of the xy-plane. It has no effect on the content’s frame.
