---
title: 'perspectiveRotationEffect(_:axis:anchor:perspective:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/perspectiverotationeffect(_:axis:anchor:perspective:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/perspectiverotationeffect(_:axis:anchor:perspective:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/perspectiverotationeffect%28_%3Aaxis%3Aanchor%3Aperspective%3A%29.json'
content_hash: 'sha256:6b55df03b6e9308e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# perspectiveRotationEffect(_:axis:anchor:perspective:)

<sub>Instance Method</sub>

Renders content as if it’s rotated in three dimensions around the specified axis.

<sub>visionOS</sub>

```swift
func perspectiveRotationEffect(_ angle: Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D = .back, perspective: CGFloat = 1) -> some VisualEffect

```

## Parameters

- `angle` — The angle by which to rotate the content.

- `axis` — The axis of rotation, specified as a tuple with named elements for each of the three spatial dimensions.

- `anchor` — A unit point within the content about which to perform the rotation. The default value is [center](../unitpoint3d/center.md).

- `perspective` — The relative vanishing point for the rotation. The default is `1`.

## Return Value

A rotation effect.

## Discussion

Use this method to create the effect of rotating content in three dimensions around a specified axis of rotation. The modifier projects two dimensional content onto the original content’s plane. Use the `perspective` input to control the renderer’s vanishing point. The following example creates the appearance of rotating text 45˚ about the y-axis:

```swift
Text("Rotation by passing an angle in degrees")
    .visualEffect { content, geometryProxy in
        content
            .perspectiveRotationEffect(
                .degrees(45),
                axis: (x: 0.0, y: 1.0, z: 0.0),
                anchor: .center,
                perspective: 1)
        }
    .border(Color.gray)
```

![](../../../../attachments/26dcde23639ed248bfc573a1a0986072/SwiftUI-View-rotation3DEffect@2x.png)

<sub>A screenshot of text in a grey box. The text says Rotation by passing an angle in degrees. The text is rendered in a way that makes it appear farther from the viewer on the right side and closer on the left, as if the text is angled to face someone sitting on the viewer’s right.</sub>

> [!important] Important
> To truly rotate content in three dimensions, use a 3D rotation effect without a perspective input like [rotation3DEffect(_:axis:anchor:)](<rotation3deffect(__axis_anchor_).md>).

## See Also

### Rotating

- [rotationEffect(_:anchor:)](<rotationeffect(__anchor_).md>) — Rotates content in two dimensions around the specified point.
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](<rotation3deffect(__axis_anchor_anchorz_perspective_).md>) — Renders content as if it’s rotated in three dimensions around the specified axis.
- [rotation3DEffect(_:anchor:)](<rotation3deffect(__anchor_).md>) — Rotates content by the specified 3D rotation value.
- [rotation3DEffect(_:axis:anchor:)](<rotation3deffect(__axis_anchor_).md>) — Rotates content by an angle about an axis that you specify as a rotation axis value.
