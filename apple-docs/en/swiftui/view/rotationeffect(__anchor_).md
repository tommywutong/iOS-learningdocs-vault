---
title: 'rotationEffect(_:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/rotationeffect(_:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/rotationeffect(_:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/rotationeffect%28_%3Aanchor%3A%29.json'
content_hash: 'sha256:01835d01a6054695'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# rotationEffect(_:anchor:)

<sub>Instance Method</sub>

Rotates a view’s rendered output in two dimensions around the specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func rotationEffect(_ angle: Angle, anchor: UnitPoint = .center) -> some View

```

## Parameters

- `angle` — The angle by which to rotate the view.

- `anchor` — A unit point within the view about which to perform the rotation. The default value is [center](../unitpoint/center.md).

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content around the axis that points out of the xy-plane. It has no effect on the view’s frame. The following code rotates text by 22˚ and then draws a border around the modified view to show that the frame remains unchanged by the rotation modifier:

```swift
Text("Rotation by passing an angle in degrees")
    .rotationEffect(.degrees(22))
    .border(Color.gray)
```

![](../../../../attachments/b37c8f57cc3cc583b004f632134572e5/SwiftUI-View-rotationEffect@2x.png)

<sub>A screenshot of text and a wide grey box. The text says Rotation by passing an angle in degrees. The baseline of the text is rotated clockwise by 22 degrees relative to the box. The center of the box and the center of the text are aligned.</sub>

## See Also

### Scaling, rotating, or transforming a view

- [scaledToFill()](<scaledtofill().md>) — Scales this view to fill its parent.
- [scaledToFit()](<scaledtofit().md>) — Scales this view to fit its parent.
- [scaleEffect(_:anchor:)](<scaleeffect(__anchor_).md>) — Scales this view uniformly by the specified factor, relative to an anchor point.
- [scaleEffect(x:y:anchor:)](<scaleeffect(x_y_anchor_).md>) — Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [scaleEffect(x:y:z:anchor:)](<scaleeffect(x_y_z_anchor_).md>) — Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [aspectRatio(_:contentMode:)](<aspectratio(__contentmode_).md>) — Constrains this view’s dimensions to the specified aspect ratio.
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](<rotation3deffect(__axis_anchor_anchorz_perspective_).md>) — Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)](<perspectiverotationeffect(__axis_anchor_anchorz_perspective_).md>) — Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [rotation3DEffect(_:anchor:)](<rotation3deffect(__anchor_).md>) — Rotates the view’s content by the specified 3D rotation value.
- [rotation3DEffect(_:axis:anchor:)](<rotation3deffect(__axis_anchor_).md>) — Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [transformEffect(_:)](<transformeffect(__).md>) — Applies an affine transformation to this view’s rendered output.
- [transform3DEffect(_:)](<transform3deffect(__).md>) — Applies a 3D transformation to this view’s rendered output.
- [projectionEffect(_:)](<projectioneffect(__).md>) — Applies a projection transformation to this view’s rendered output.
- [ProjectionTransform](../projectiontransform.md)
- [ContentMode](../contentmode.md) — Constants that define how a view’s content fills the available space.
