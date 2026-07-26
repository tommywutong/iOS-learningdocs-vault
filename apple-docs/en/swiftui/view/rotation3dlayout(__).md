---
title: 'rotation3DLayout(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/rotation3dlayout(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/rotation3dlayout(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/rotation3dlayout%28_%3A%29.json'
content_hash: 'sha256:eb89990f8e7b39a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# rotation3DLayout(_:)

<sub>Instance Method</sub>

Rotates a view with impacts to its frame in a containing layout

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func rotation3DLayout(_ rotation: Rotation3D) -> some View

```

## Parameters

- `rotation` — A rotation to apply to the view and its frame.

## Discussion

The following example will rotate the top plane by 45 degrees while adjusting its frame to account for this rotation. The VStack sizes to fit the rotated and standard models.

```swift
VStack {
    Model3D(named: "plane")
        .rotation3DLayout(Rotation3D(angle: .degrees(45), axis: .z))
    Model3D(named: "plane")
```

}

The layout system will use a bounding box that completely contains the rotated view, meaning this modifier can change the size of the view it is applied to.

## See Also

### Rotation and transformation

- [rotationEffect(_:anchor:)](<rotationeffect(__anchor_).md>) — Rotates a view’s rendered output in two dimensions around the specified point.
- [rotation3DEffect(_:anchor:)](<rotation3deffect(__anchor_).md>) — Rotates the view’s content by the specified 3D rotation value.
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](<rotation3deffect(__axis_anchor_anchorz_perspective_).md>) — Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [rotation3DEffect(_:axis:anchor:)](<rotation3deffect(__axis_anchor_).md>) — Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [rotation3DLayout(_:axis:)](<rotation3dlayout(__axis_).md>) — Rotates a view with impacts to its frame in a containing layout
- [perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)](<perspectiverotationeffect(__axis_anchor_anchorz_perspective_).md>) — Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [projectionEffect(_:)](<projectioneffect(__).md>) — Applies a projection transformation to this view’s rendered output.
- [transformEffect(_:)](<transformeffect(__).md>) — Applies an affine transformation to this view’s rendered output.
- [transform3DEffect(_:)](<transform3deffect(__).md>) — Applies a 3D transformation to this view’s rendered output.
