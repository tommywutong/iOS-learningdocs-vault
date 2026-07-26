---
title: ProjectionTransform
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/projectiontransform
source_url: 'https://developer.apple.com/documentation/swiftui/projectiontransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/projectiontransform.json'
content_hash: 'sha256:ac20202737c1a42e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ProjectionTransform

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ProjectionTransform
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a transform

- [init()](<projectiontransform/init().md>)
- [init(_:)](<projectiontransform/init(__).md>)

### Getting transform characteristics

- [isAffine](projectiontransform/isaffine.md)
- [isIdentity](projectiontransform/isidentity.md)

### Manipulating transforms

- [invert()](<projectiontransform/invert().md>)
- [inverted()](<projectiontransform/inverted().md>)
- [concatenating(_:)](<projectiontransform/concatenating(__).md>)

### Accessing the transform’s coefficients

- [m11](projectiontransform/m11.md)
- [m12](projectiontransform/m12.md)
- [m13](projectiontransform/m13.md)
- [m21](projectiontransform/m21.md)
- [m22](projectiontransform/m22.md)
- [m23](projectiontransform/m23.md)
- [m31](projectiontransform/m31.md)
- [m32](projectiontransform/m32.md)
- [m33](projectiontransform/m33.md)

## See Also

### Scaling, rotating, or transforming a view

- [scaledToFill()](<view/scaledtofill().md>) — Scales this view to fill its parent.
- [scaledToFit()](<view/scaledtofit().md>) — Scales this view to fit its parent.
- [scaleEffect(_:anchor:)](<view/scaleeffect(__anchor_).md>) — Scales this view uniformly by the specified factor, relative to an anchor point.
- [scaleEffect(x:y:anchor:)](<view/scaleeffect(x_y_anchor_).md>) — Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [scaleEffect(x:y:z:anchor:)](<view/scaleeffect(x_y_z_anchor_).md>) — Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [aspectRatio(_:contentMode:)](<view/aspectratio(__contentmode_).md>) — Constrains this view’s dimensions to the specified aspect ratio.
- [rotationEffect(_:anchor:)](<view/rotationeffect(__anchor_).md>) — Rotates a view’s rendered output in two dimensions around the specified point.
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](<view/rotation3deffect(__axis_anchor_anchorz_perspective_).md>) — Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)](<view/perspectiverotationeffect(__axis_anchor_anchorz_perspective_).md>) — Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [rotation3DEffect(_:anchor:)](<view/rotation3deffect(__anchor_).md>) — Rotates the view’s content by the specified 3D rotation value.
- [rotation3DEffect(_:axis:anchor:)](<view/rotation3deffect(__axis_anchor_).md>) — Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [transformEffect(_:)](<view/transformeffect(__).md>) — Applies an affine transformation to this view’s rendered output.
- [transform3DEffect(_:)](<view/transform3deffect(__).md>) — Applies a 3D transformation to this view’s rendered output.
- [projectionEffect(_:)](<view/projectioneffect(__).md>) — Applies a projection transformation to this view’s rendered output.
- [ContentMode](contentmode.md) — Constants that define how a view’s content fills the available space.
