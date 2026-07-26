---
title: 'scaleEffect(x:y:z:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/scaleeffect(x:y:z:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/scaleeffect(x:y:z:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/scaleeffect%28x%3Ay%3Az%3Aanchor%3A%29.json'
content_hash: 'sha256:1027f851b59492d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# scaleEffect(x:y:z:anchor:)

<sub>Instance Method</sub>

Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.

<sub>visionOS</sub>

```swift
@export(implementation) func scaleEffect(x: CGFloat = 1.0, y: CGFloat = 1.0, z: CGFloat = 1.0, anchor: UnitPoint3D = .center) -> some VisualEffect

```

## Parameters

- `x` — The horizontal scale factor for this view.

- `y` — The vertical scale factor for this view.

- `z` — The depth scale factor for this view.

- `anchor` — The anchor point about which to scale the view. Defaults to center.

## Return Value

An effect that scales this view by `x`,`y`, and `z`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling the contents. To change the dimensions of the view, use a modifier like `frame()` instead.

## See Also

### Scaling

- [scaleEffect(_:anchor:)](<scaleeffect(__anchor_).md>) — Scales this view uniformly by the specified factor, relative to an anchor point.
- [scaleEffect(x:y:anchor:)](<scaleeffect(x_y_anchor_).md>) — Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
