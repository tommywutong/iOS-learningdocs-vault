---
title: 'rotation3DEffect(_:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/rotation3deffect(_:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/rotation3deffect(_:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/rotation3deffect%28_%3Aanchor%3A%29.json'
content_hash: 'sha256:b36de54ce42a87ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# rotation3DEffect(_:anchor:)

<sub>Instance Method</sub>

Rotates content by the specified 3D rotation value.

<sub>visionOS</sub>

```swift
@export(implementation) func rotation3DEffect(_ rotation: Rotation3D, anchor: UnitPoint3D = .center) -> some VisualEffect

```

## Parameters

- `rotation` — A rotation to apply to the content.

- `anchor` — The unit point within the content about which to perform the rotation. The default value is [center](../unitpoint3d/center.md).

## Return Value

A rotation effect.

## Discussion

This effect causes the content to appear rotated, but doesn’t change the content’s frame. The following code applies a rotation of 45° about the y-axis, using the default anchor point at the center of the content:

```swift
Model3D(named: "robot")
    .visualEffect { content, geometryProxy in
        content
            .rotation3DEffect(Rotation3D(angle: .degrees(45), axis: .y))
    }
```

During an animation, this modifier uses spherical linear interpolation, which produces more natural animations, but doesn’t support rotations over 360 degrees. To specify angles over 360 degrees, consider using `View/rotation3DEffect(_:axis:anchor:)-4enag`.

## See Also

### Rotating

- [rotationEffect(_:anchor:)](<rotationeffect(__anchor_).md>) — Rotates content in two dimensions around the specified point.
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](<rotation3deffect(__axis_anchor_anchorz_perspective_).md>) — Renders content as if it’s rotated in three dimensions around the specified axis.
- [perspectiveRotationEffect(_:axis:anchor:perspective:)](<perspectiverotationeffect(__axis_anchor_perspective_).md>) — Renders content as if it’s rotated in three dimensions around the specified axis.
- [rotation3DEffect(_:axis:anchor:)](<rotation3deffect(__axis_anchor_).md>) — Rotates content by an angle about an axis that you specify as a rotation axis value.
