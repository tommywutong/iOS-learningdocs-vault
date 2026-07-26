---
title: 'offset(z:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/offset(z:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/offset(z:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/offset%28z%3A%29.json'
content_hash: 'sha256:404e95bdde96ba6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# offset(z:)

<sub>Instance Method</sub>

Brings a view forward in Z by the provided distance in points.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func offset(z: CGFloat) -> some View

```

## Return Value

A view that is extruded forward in Z by `distance`.

## See Also

### Adjusting a view’s position

- [Making fine adjustments to a view’s position](../making-fine-adjustments-to-a-view-s-position.md) — Shift the position of a view by applying the offset or position modifier.
- [position(_:)](<position(__).md>) — Positions the center of this view at the specified point in its parent’s coordinate space.
- [position(x:y:)](<position(x_y_).md>) — Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [offset(_:)](<offset(__).md>) — Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [offset(x:y:)](<offset(x_y_).md>) — Offset this view by the specified horizontal and vertical distances.
