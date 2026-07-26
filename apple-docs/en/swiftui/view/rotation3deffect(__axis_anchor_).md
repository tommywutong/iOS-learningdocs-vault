---
title: 'rotation3DEffect(_:axis:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/rotation3deffect(_:axis:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/rotation3deffect(_:axis:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/rotation3deffect%28_%3Aaxis%3Aanchor%3A%29.json'
content_hash: 'sha256:10eef9b39d569368'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# rotation3DEffect(_:axis:anchor:)

<sub>Instance Method</sub>

Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func rotation3DEffect(_ angle: Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D = .center) -> some View

```

## Parameters

- `angle` — The angle by which to rotate the view’s content.

- `axis` — The axis of rotation, specified as a tuple with named elements for each of the three spatial dimensions.

- `anchor` — The unit point within the view about which to perform the rotation. The default value is [center](../unitpoint3d/center.md).

## Return Value

A view with rotated content.

## Discussion

> [!note] Note
> During an animation, the angle and each element of the axis is interpolated separately, which may cause undesirable results. To achieve more natural animations, consider using [rotation3DEffect(_:anchor:)](<rotation3deffect(__anchor_).md>)

This modifier rotates the view’s content without changing the view’s frame. The following code displays a 3D model with a rotation of 45° about the y-axis using the default anchor point at the center of the view:

```swift
Model3D(named: "robot")
    .rotation3DEffect(.degrees(45), axis: (x: 0, y: 1, z: 0))
```

> [!note] Note
> The following example is not equivalent to the previous. This example will use spherical linear interpolation during an animation.

```swift
let rotation = Rotation3D(
    angle: .init(degrees: 45),
    axis: RotationAxis3D(x: 0, y: 1, z: 0))
Model3D(named: "robot")
    .rotation3DEffect(rotation)
```

## See Also

### Scaling, rotating, or transforming a view

- [scaledToFill()](<scaledtofill().md>) — Scales this view to fill its parent.
- [scaledToFit()](<scaledtofit().md>) — Scales this view to fit its parent.
- [scaleEffect(_:anchor:)](<scaleeffect(__anchor_).md>) — Scales this view uniformly by the specified factor, relative to an anchor point.
- [scaleEffect(x:y:anchor:)](<scaleeffect(x_y_anchor_).md>) — Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [scaleEffect(x:y:z:anchor:)](<scaleeffect(x_y_z_anchor_).md>) — Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [aspectRatio(_:contentMode:)](<aspectratio(__contentmode_).md>) — Constrains this view’s dimensions to the specified aspect ratio.
- [rotationEffect(_:anchor:)](<rotationeffect(__anchor_).md>) — Rotates a view’s rendered output in two dimensions around the specified point.
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](<rotation3deffect(__axis_anchor_anchorz_perspective_).md>) — Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)](<perspectiverotationeffect(__axis_anchor_anchorz_perspective_).md>) — Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [rotation3DEffect(_:anchor:)](<rotation3deffect(__anchor_).md>) — Rotates the view’s content by the specified 3D rotation value.
- [transformEffect(_:)](<transformeffect(__).md>) — Applies an affine transformation to this view’s rendered output.
- [transform3DEffect(_:)](<transform3deffect(__).md>) — Applies a 3D transformation to this view’s rendered output.
- [projectionEffect(_:)](<projectioneffect(__).md>) — Applies a projection transformation to this view’s rendered output.
- [ProjectionTransform](../projectiontransform.md)
- [ContentMode](../contentmode.md) — Constants that define how a view’s content fills the available space.
