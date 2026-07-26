---
title: 'scaleEffect(x:y:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/scaleeffect(x:y:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/scaleeffect(x:y:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/scaleeffect%28x%3Ay%3Aanchor%3A%29.json'
content_hash: 'sha256:a0c098431affb10a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# scaleEffect(x:y:anchor:)

<sub>Instance Method</sub>

Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scaleEffect(x: CGFloat = 1.0, y: CGFloat = 1.0, anchor: UnitPoint = .center) -> some VisualEffect

```

## Parameters

- `x` — An amount that represents the horizontal amount to scale the view. The default value is `1.0`.

- `y` — An amount that represents the vertical amount to scale the view. The default value is `1.0`.

- `anchor` — The point with a default of [center](../unitpoint/center.md) that defines the location within the view from which to apply the transformation.

## Return Value

An effect that scales the view’s rendered output.

## See Also

### Scaling

- [scaleEffect(_:anchor:)](<scaleeffect(__anchor_).md>) — Scales this view uniformly by the specified factor, relative to an anchor point.
- [scaleEffect(x:y:z:anchor:)](<scaleeffect(x_y_z_anchor_).md>) — Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
