---
title: 'offset(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/offset(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/offset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/offset%28_%3A%29.json'
content_hash: 'sha256:31e9cac81afb87c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# offset(_:)

<sub>Instance Method</sub>

Offset this view by the horizontal and vertical amount specified in the offset parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func offset(_ offset: CGSize) -> some View

```

## Parameters

- `offset` — The distance to offset this view.

## Return Value

A view that offsets this view by `offset`.

## Discussion

Use `offset(_:)` to shift the displayed contents by the amount specified in the `offset` parameter.

The original dimensions of the view aren’t changed by offsetting the contents; in the example below the gray border drawn by this view surrounds the original position of the text:

```swift
Text("Offset by passing CGSize()")
    .border(Color.green)
    .offset(CGSize(width: 20, height: 25))
    .border(Color.gray)
```

![A screenshot showing a view that offset from its original position a](../../../../attachments/ce41cfcb2217463d1da9217414eb5746/SwiftUI-View-offset@2x.png)

## See Also

### Adjusting a view’s position

- [Making fine adjustments to a view’s position](../making-fine-adjustments-to-a-view-s-position.md) — Shift the position of a view by applying the offset or position modifier.
- [position(_:)](<position(__).md>) — Positions the center of this view at the specified point in its parent’s coordinate space.
- [position(x:y:)](<position(x_y_).md>) — Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [offset(x:y:)](<offset(x_y_).md>) — Offset this view by the specified horizontal and vertical distances.
- [offset(z:)](<offset(z_).md>) — Brings a view forward in Z by the provided distance in points.
