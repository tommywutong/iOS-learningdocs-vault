---
title: 'perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/perspectiverotationeffect%28_%3Aaxis%3Aanchor%3Aanchorz%3Aperspective%3A%29.json'
content_hash: 'sha256:f1324271c8cffecf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)

<sub>Instance Method</sub>

Renders a view’s content as if it’s rotated in three dimensions around the specified axis.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func perspectiveRotationEffect(_ angle: Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint = .center, anchorZ: CGFloat = 0, perspective: CGFloat = 1) -> some View

```

## Parameters

- `angle` — The angle by which to rotate the view’s content.

- `axis` — The axis of rotation, specified as a tuple with named elements for each of the three spatial dimensions.

- `anchor` — A two dimensional unit point within the view about which to perform the rotation. The default value is [center](../unitpoint/center.md).

- `anchorZ` — The location on the z-axis around which to rotate the content. The default is `0`.

- `perspective` — The relative vanishing point for the rotation. The default is `1`.

## Return Value

A view with rotated content.

## Discussion

Use this method to create the effect of rotating a view in three dimensions around a specified axis of rotation. The modifier projects the rotated, two-dimensional content onto the original view’s plane. Use the `perspective` input to control the renderer’s vanishing point. The following example creates the appearance of rotating text 45˚ about the y-axis:

```swift
Text("Rotation by passing an angle in degrees")
    .perspectiveRotationEffect(
        .degrees(45),
        axis: (x: 0.0, y: 1.0, z: 0.0),
        anchor: .center,
        anchorZ: 0,
        perspective: 1)
    .border(Color.gray)
```

![](../../../../attachments/26dcde23639ed248bfc573a1a0986072/SwiftUI-View-rotation3DEffect@2x.png)

<sub>A screenshot of text in a grey box. The text says Rotation by passing an angle in degrees. The text is rendered in a way that makes it appear farther from the viewer on the right side and closer on the left, as if the text is angled to face someone sitting on the viewer’s right.</sub>

> [!important] Important
> To truly rotate a view in three dimensions, use a 3D rotation modifier without a perspective input like [rotation3DEffect(_:axis:anchor:)](<rotation3deffect(__axis_anchor_).md>).

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
- [rotation3DEffect(_:anchor:)](<rotation3deffect(__anchor_).md>) — Rotates the view’s content by the specified 3D rotation value.
- [rotation3DEffect(_:axis:anchor:)](<rotation3deffect(__axis_anchor_).md>) — Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [transformEffect(_:)](<transformeffect(__).md>) — Applies an affine transformation to this view’s rendered output.
- [transform3DEffect(_:)](<transform3deffect(__).md>) — Applies a 3D transformation to this view’s rendered output.
- [projectionEffect(_:)](<projectioneffect(__).md>) — Applies a projection transformation to this view’s rendered output.
- [ProjectionTransform](../projectiontransform.md)
- [ContentMode](../contentmode.md) — Constants that define how a view’s content fills the available space.
