---
title: 'rotation3DEffect(_:axis:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/rotation3deffect(_:axis:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/rotation3deffect(_:axis:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/rotation3deffect%28_%3Aaxis%3Aanchor%3A%29.json'
content_hash: 'sha256:aab98f9703fae98f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# rotation3DEffect(_:axis:anchor:)

<sub>Instance Method</sub>

Rotates content by an angle about an axis that you specify as a rotation axis value.

<sub>visionOS</sub>

```swift
@export(implementation) func rotation3DEffect(_ angle: Angle, axis: RotationAxis3D, anchor: UnitPoint3D = .center) -> some VisualEffect

```

## Parameters

- `angle` — The angle by which to rotate the view’s content.

- `axis` — The axis of rotation.

- `anchor` — The unit point within the content about which to perform the rotation. The default value is [center](../unitpoint3d/center.md).

## Return Value

A rotation effect.

## Discussion

This effect causes the content to appear rotated, but doesn’t change the content’s frame. The following code applies a rotation of 45° about the y-axis, using the default anchor point at the center of the content:

```swift
Model3D(named: "robot")
    .visualEffect { content, geometryProxy in
        content
            .rotation3DEffect(.degrees(45), axis: .y)
    }
```

## See Also

### Rotating

- [rotationEffect(_:anchor:)](<rotationeffect(__anchor_).md>) — Rotates content in two dimensions around the specified point.
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](<rotation3deffect(__axis_anchor_anchorz_perspective_).md>) — Renders content as if it’s rotated in three dimensions around the specified axis.
- [perspectiveRotationEffect(_:axis:anchor:perspective:)](<perspectiverotationeffect(__axis_anchor_perspective_).md>) — Renders content as if it’s rotated in three dimensions around the specified axis.
- [rotation3DEffect(_:anchor:)](<rotation3deffect(__anchor_).md>) — Rotates content by the specified 3D rotation value.
