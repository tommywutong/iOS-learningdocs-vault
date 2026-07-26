---
title: 'scale(x:y:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/scale(x:y:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/scale(x:y:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/scale%28x%3Ay%3Aanchor%3A%29.json'
content_hash: 'sha256:50f929518bd882e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# scale(x:y:anchor:)

<sub>Instance Method</sub>

Scales this shape without changing its bounding frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func scale(x: CGFloat = 1, y: CGFloat = 1, anchor: UnitPoint = .center) -> ScaledShape<Self>
```

## Parameters

- `x` — The multiplication factor used to resize this shape along its x-axis.

- `y` — The multiplication factor used to resize this shape along its y-axis.

## Return Value

A scaled form of this shape.

## Discussion

Both the `x` and `y` multiplication factors halve their respective dimension’s size when set to `0.5`, maintain their existing size when set to `1`, double their size when set to `2`, and so forth.

## See Also

### Transforming a shape

- [trim(from:to:)](<trim(from_to_).md>) — Trims this shape by a fractional amount based on its representation as a path.
- [transform(_:)](<transform(__).md>) — Applies an affine transform to this shape.
- [size(_:)](<size(__).md>) — Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of `size`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [size(_:anchor:)](<size(__anchor_).md>) — Returns a new version of self representing the same shape, but within a rect of `size` instead of the container size.
- [size(width:height:)](<size(width_height_).md>) — Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of size `(width, height)`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [size(width:height:anchor:)](<size(width_height_anchor_).md>) — Returns a new version of self representing the same shape, but within a rect of `(width, height)` instead of the container size.
- [scale(_:anchor:)](<scale(__anchor_).md>) — Scales this shape without changing its bounding frame.
- [rotation(_:anchor:)](<rotation(__anchor_).md>) — Rotates this shape around an anchor point at the angle you specify.
- [offset(_:)](<offset(__).md>) — Changes the relative position of this shape using the specified point.
- [offset(x:y:)](<offset(x_y_).md>) — Changes the relative position of this shape using the specified point.
