---
title: 'position(x:y:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/position(x:y:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/position(x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/position%28x%3Ay%3A%29.json'
content_hash: 'sha256:e17835059054f1df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# position(x:y:)

<sub>Instance Method</sub>

Positions the center of this view at the specified coordinates in its parent’s coordinate space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func position(x: CGFloat = 0, y: CGFloat = 0) -> some View

```

## Parameters

- `x` — The x-coordinate at which to place the center of this view.

- `y` — The y-coordinate at which to place the center of this view.

## Return Value

A view that fixes the center of this view at `x` and `y`.

## Discussion

Use the `position(x:y:)` modifier to place the center of a view at a specific coordinate in the parent view using an `x` and `y` offset.

```swift
Text("Position by passing the x and y coordinates")
    .position(x: 175, y: 100)
    .border(Color.gray)
```

## See Also

### Adjusting a view’s position

- [Making fine adjustments to a view’s position](../making-fine-adjustments-to-a-view-s-position.md) — Shift the position of a view by applying the offset or position modifier.
- [position(_:)](<position(__).md>) — Positions the center of this view at the specified point in its parent’s coordinate space.
- [offset(_:)](<offset(__).md>) — Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [offset(x:y:)](<offset(x_y_).md>) — Offset this view by the specified horizontal and vertical distances.
- [offset(z:)](<offset(z_).md>) — Brings a view forward in Z by the provided distance in points.
