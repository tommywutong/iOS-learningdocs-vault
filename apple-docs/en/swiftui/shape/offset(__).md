---
title: 'offset(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/offset(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/offset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/offset%28_%3A%29.json'
content_hash: 'sha256:19570818e8c41a15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# offset(_:)

<sub>Instance Method</sub>

Changes the relative position of this shape using the specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func offset(_ offset: CGPoint) -> OffsetShape<Self>
```

## Parameters

- `offset` — The amount, in points, by which you offset the shape. Negative numbers are to the left and up; positive numbers are to the right and down.

## Return Value

A shape offset by the specified amount.

## Discussion

The following example renders two circles. It places one circle at its default position. The second circle is outlined with a stroke, positioned on top of the first circle and offset by 100 points to the left and 50 points below.

```swift
Circle()
.overlay(
    Circle()
    .offset(CGPoint(x: -100, y: 50))
    .stroke()
)
```

## See Also

### Transforming a shape

- [trim(from:to:)](<trim(from_to_).md>) — Trims this shape by a fractional amount based on its representation as a path.
- [transform(_:)](<transform(__).md>) — Applies an affine transform to this shape.
- [size(_:)](<size(__).md>) — Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of `size`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [size(_:anchor:)](<size(__anchor_).md>) — Returns a new version of self representing the same shape, but within a rect of `size` instead of the container size.
- [size(width:height:)](<size(width_height_).md>) — Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of size `(width, height)`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [size(width:height:anchor:)](<size(width_height_anchor_).md>) — Returns a new version of self representing the same shape, but within a rect of `(width, height)` instead of the container size.
- [scale(_:anchor:)](<scale(__anchor_).md>) — Scales this shape without changing its bounding frame.
- [scale(x:y:anchor:)](<scale(x_y_anchor_).md>) — Scales this shape without changing its bounding frame.
- [rotation(_:anchor:)](<rotation(__anchor_).md>) — Rotates this shape around an anchor point at the angle you specify.
- [offset(x:y:)](<offset(x_y_).md>) — Changes the relative position of this shape using the specified point.
