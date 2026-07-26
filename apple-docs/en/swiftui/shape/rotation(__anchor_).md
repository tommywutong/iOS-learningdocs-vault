---
title: 'rotation(_:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/rotation(_:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/rotation(_:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/rotation%28_%3Aanchor%3A%29.json'
content_hash: 'sha256:8e44d72b8460416a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# rotation(_:anchor:)

<sub>Instance Method</sub>

Rotates this shape around an anchor point at the angle you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func rotation(_ angle: Angle, anchor: UnitPoint = .center) -> RotatedShape<Self>
```

## Parameters

- `angle` — The angle of rotation to apply. Positive angles rotate clockwise; negative angles rotate counterclockwise.

- `anchor` — The point to rotate the shape around.

## Return Value

A rotated shape.

## Discussion

The following example rotates a square by 45 degrees to the right to create a diamond shape:

```swift
RoundedRectangle(cornerRadius: 10)
.rotation(Angle(degrees: 45))
.aspectRatio(1.0, contentMode: .fit)
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
- [offset(_:)](<offset(__).md>) — Changes the relative position of this shape using the specified point.
- [offset(x:y:)](<offset(x_y_).md>) — Changes the relative position of this shape using the specified point.
