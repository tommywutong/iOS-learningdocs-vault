---
title: 'transform(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/transform(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/transform(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/transform%28_%3A%29.json'
content_hash: 'sha256:4dbde8981f3388dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# transform(_:)

<sub>Instance Method</sub>

Applies an affine transform to this shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func transform(_ transform: CGAffineTransform) -> TransformedShape<Self>
```

## Parameters

- `transform` — The affine transformation matrix to apply to this shape.

## Return Value

A transformed shape, based on its matrix values.

## Discussion

Affine transforms present a mathematical approach to applying combinations of rotation, scaling, translation, and skew to shapes.

## See Also

### Transforming a shape

- [trim(from:to:)](<trim(from_to_).md>) — Trims this shape by a fractional amount based on its representation as a path.
- [size(_:)](<size(__).md>) — Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of `size`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [size(_:anchor:)](<size(__anchor_).md>) — Returns a new version of self representing the same shape, but within a rect of `size` instead of the container size.
- [size(width:height:)](<size(width_height_).md>) — Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of size `(width, height)`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [size(width:height:anchor:)](<size(width_height_anchor_).md>) — Returns a new version of self representing the same shape, but within a rect of `(width, height)` instead of the container size.
- [scale(_:anchor:)](<scale(__anchor_).md>) — Scales this shape without changing its bounding frame.
- [scale(x:y:anchor:)](<scale(x_y_anchor_).md>) — Scales this shape without changing its bounding frame.
- [rotation(_:anchor:)](<rotation(__anchor_).md>) — Rotates this shape around an anchor point at the angle you specify.
- [offset(_:)](<offset(__).md>) — Changes the relative position of this shape using the specified point.
- [offset(x:y:)](<offset(x_y_).md>) — Changes the relative position of this shape using the specified point.
