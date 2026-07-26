---
title: 'offset(x:y:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/offset(x:y:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/offset(x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/offset%28x%3Ay%3A%29.json'
content_hash: 'sha256:1f875c4313592181'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# offset(x:y:)

<sub>Instance Method</sub>

Offset this view by the specified horizontal and vertical distances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func offset(x: CGFloat = 0, y: CGFloat = 0) -> some View

```

## Parameters

- `x` — The horizontal distance to offset this view.

- `y` — The vertical distance to offset this view.

## Return Value

A view that offsets this view by `x` and `y`.

## Discussion

Use `offset(x:y:)` to shift the displayed contents by the amount specified in the `x` and `y` parameters.

The original dimensions of the view aren’t changed by offsetting the contents; in the example below the gray border drawn by this view surrounds the original position of the text:

```swift
Text("Offset by passing horizontal & vertical distance")
    .border(Color.green)
    .offset(x: 20, y: 50)
    .border(Color.gray)
```

![A screenshot showing a view that offset from its original position](../../../../attachments/2d9a124308ea31d3006f2d246939c0d1/swiftui-offset-xy@2x.png)

## See Also

### Adjusting a view’s position

- [Making fine adjustments to a view’s position](../making-fine-adjustments-to-a-view-s-position.md) — Shift the position of a view by applying the offset or position modifier.
- [position(_:)](<position(__).md>) — Positions the center of this view at the specified point in its parent’s coordinate space.
- [position(x:y:)](<position(x_y_).md>) — Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [offset(_:)](<offset(__).md>) — Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [offset(z:)](<offset(z_).md>) — Brings a view forward in Z by the provided distance in points.
