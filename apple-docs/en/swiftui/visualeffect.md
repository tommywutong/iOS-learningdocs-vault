---
title: VisualEffect
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/visualeffect
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect.json'
content_hash: 'sha256:b97795af26868568'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# VisualEffect

<sub>Protocol</sub>

Visual Effects change the visual appearance of a view without changing its ancestors or descendents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol VisualEffect : Sendable, Animatable
```

## Overview

Because effects do not impact layout, they are safe to use in situations where layout modification is not allowed. For example, effects may be applied as a function of position, accessed through a geometry proxy:

```swift
var body: some View {
    ContentRow()
        .visualEffect { content, geometryProxy in
            content.offset(x: geometryProxy.frame(in: .global).origin.y)
        }
}
```

You don’t conform to this protocol yourself. Instead, visual effects are created by calling modifier functions (such as `.offset(x:y:)` on other effects, as seen in the example above.

## Relationships

- **Inherits From**: [Animatable](animatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [EmptyVisualEffect](emptyvisualeffect.md), [ModifiedContent](modifiedcontent.md)

## Topics

### Adjusting Color

- [brightness(_:)](<visualeffect/brightness(__).md>) — Brightens the view by the specified amount.
- [colorEffect(_:isEnabled:)](<visualeffect/coloreffect(__isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [contrast(_:)](<visualeffect/contrast(__).md>) — Sets the contrast and separation between similar colors in the view.
- [grayscale(_:)](<visualeffect/grayscale(__).md>) — Adds a grayscale effect to the view.
- [hueRotation(_:)](<visualeffect/huerotation(__).md>) — Applies a hue rotation effect to the view.
- [saturation(_:)](<visualeffect/saturation(__).md>) — Adjusts the color saturation of the view.
- [opacity(_:)](<visualeffect/opacity(__).md>) — Sets the transparency of the view.

### Scaling

- [scaleEffect(_:anchor:)](<visualeffect/scaleeffect(__anchor_).md>) — Scales this view uniformly by the specified factor, relative to an anchor point.
- [scaleEffect(x:y:anchor:)](<visualeffect/scaleeffect(x_y_anchor_).md>) — Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [scaleEffect(x:y:z:anchor:)](<visualeffect/scaleeffect(x_y_z_anchor_).md>) — Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.

### Rotating

- [rotationEffect(_:anchor:)](<visualeffect/rotationeffect(__anchor_).md>) — Rotates content in two dimensions around the specified point.
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](<visualeffect/rotation3deffect(__axis_anchor_anchorz_perspective_).md>) — Renders content as if it’s rotated in three dimensions around the specified axis.
- [perspectiveRotationEffect(_:axis:anchor:perspective:)](<visualeffect/perspectiverotationeffect(__axis_anchor_perspective_).md>) — Renders content as if it’s rotated in three dimensions around the specified axis.
- [rotation3DEffect(_:anchor:)](<visualeffect/rotation3deffect(__anchor_).md>) — Rotates content by the specified 3D rotation value.
- [rotation3DEffect(_:axis:anchor:)](<visualeffect/rotation3deffect(__axis_anchor_).md>) — Rotates content by an angle about an axis that you specify as a rotation axis value.

### Translating

- [offset(_:)](<visualeffect/offset(__).md>) — Offsets the view by the horizontal and vertical amount specified in the offset parameter.
- [offset(x:y:)](<visualeffect/offset(x_y_).md>) — Offsets the view by the specified horizontal and vertical distances.
- [offset(z:)](<visualeffect/offset(z_).md>) — Brings a view forward in Z by the provided distance in points.

### Applying a transform

- [transform3DEffect(_:)](<visualeffect/transform3deffect(__).md>) — Applies a 3D transformation to this view’s rendered output.
- [transformEffect(_:)](<visualeffect/transformeffect(__).md>) — Applies an affine transformation to the view’s rendered output.

### Applying other effects

- [blur(radius:opaque:)](<visualeffect/blur(radius_opaque_).md>) — Applies a Gaussian blur to the view.
- [distortionEffect(_:maxSampleOffset:isEnabled:)](<visualeffect/distortioneffect(__maxsampleoffset_isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [layerEffect(_:maxSampleOffset:isEnabled:)](<visualeffect/layereffect(__maxsampleoffset_isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a filter on the raster layer created from `self`.

### Instance Methods

- [blendMode(_:)](<visualeffect/blendmode(__).md>) — Sets the blend mode for compositing this view with overlapping views.

## See Also

### Applying effects based on geometry

- [visualEffect(_:)](<view/visualeffect(__).md>) — Applies effects to this view, while providing access to layout information through a geometry proxy.
- [visualEffect3D(_:)](<view/visualeffect3d(__).md>) — Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [EmptyVisualEffect](emptyvisualeffect.md) — The base visual effect that you apply additional effect to.
