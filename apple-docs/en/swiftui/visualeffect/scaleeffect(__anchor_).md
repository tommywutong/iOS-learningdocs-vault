---
title: 'scaleEffect(_:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/scaleeffect(_:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/scaleeffect(_:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/scaleeffect%28_%3Aanchor%3A%29.json'
content_hash: 'sha256:bdbfbe683b289722'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# scaleEffect(_:anchor:)

<sub>Instance Method</sub>

Scales this view uniformly by the specified factor, relative to an anchor point.

<sub>visionOS</sub>

```swift
@export(implementation) func scaleEffect(_ s: CGFloat, anchor: UnitPoint3D = .center) -> some VisualEffect

```

## Parameters

- `s` — The scale factor for this view.

- `anchor` — The anchor point about which to scale the view. Defaults to center.

## Return Value

An effect that scales this view by `s` in all dimensions.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling the contents. To change the dimensions of the view, use a modifier like `frame()` instead.

## See Also

### Scaling

- [scaleEffect(x:y:anchor:)](<scaleeffect(x_y_anchor_).md>) — Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [scaleEffect(x:y:z:anchor:)](<scaleeffect(x_y_z_anchor_).md>) — Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
