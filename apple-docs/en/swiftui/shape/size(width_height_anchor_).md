---
title: 'size(width:height:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/size(width:height:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/size(width:height:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/size%28width%3Aheight%3Aanchor%3A%29.json'
content_hash: 'sha256:31f0e673e9404a48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# size(width:height:anchor:)

<sub>Instance Method</sub>

Returns a new version of self representing the same shape, but within a rect of `(width, height)` instead of the container size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func size(width: CGFloat, height: CGFloat, anchor: UnitPoint) -> some Shape

```

## Parameters

- `width` — The width to constrain the shape to.

- `height` — The height to constrain the shape to.

- `anchor` — The anchor to use to determine how to position the new shape.

## Return Value

A new shape constrained to the given `size`, and positioned using `anchor`.

## Discussion

The `anchor` parameter determines how the shape will be positioned within the container when the path’s bounds and the container’s bounds are not equal. This does not affect the layout properties of any views created from the shape (e.g. by filling it).

## See Also

### Transforming a shape

- [trim(from:to:)](<trim(from_to_).md>) — Trims this shape by a fractional amount based on its representation as a path.
- [transform(_:)](<transform(__).md>) — Applies an affine transform to this shape.
- [size(_:)](<size(__).md>) — Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of `size`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [size(_:anchor:)](<size(__anchor_).md>) — Returns a new version of self representing the same shape, but within a rect of `size` instead of the container size.
- [size(width:height:)](<size(width_height_).md>) — Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of size `(width, height)`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [scale(_:anchor:)](<scale(__anchor_).md>) — Scales this shape without changing its bounding frame.
- [scale(x:y:anchor:)](<scale(x_y_anchor_).md>) — Scales this shape without changing its bounding frame.
- [rotation(_:anchor:)](<rotation(__anchor_).md>) — Rotates this shape around an anchor point at the angle you specify.
- [offset(_:)](<offset(__).md>) — Changes the relative position of this shape using the specified point.
- [offset(x:y:)](<offset(x_y_).md>) — Changes the relative position of this shape using the specified point.
