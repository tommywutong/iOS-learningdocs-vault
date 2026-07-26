---
title: path
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cakeyframeanimation/path
source_url: 'https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/path'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cakeyframeanimation/path.json'
content_hash: 'sha256:431d333cf8d54d90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAKeyframeAnimation](../cakeyframeanimation.md)

# path

<sub>Instance Property</sub>

The path for a point-based property to follow.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var path: CGPath? { get set }
```

## Discussion

For layer properties that contain a [CGPoint](../../corefoundation/cgpoint.md) data type, the path object you assign to this property defines the values for that property over the length of the animation. If you specify a value for this property, any data in the [values](values.md) property is ignored.

Any timing values you specify for the animation are applied to the points used to create the path. Paths can contain points defining move-to, line-to, or curve-to segments. The end point of a line-to or curve-to segment defines the keyframe value. All other points between that end value and the previous value are then interpolated. Move-to segments do not define separate keyframe values.

How the animation proceeds along the path is dependent on the value in the [calculationMode](calculationmode.md) property. To achieve a smooth, constant velocity animation along the path, set the [calculationMode](calculationmode.md) property to [kCAAnimationPaced](../caanimationcalculationmode/paced.md) or [kCAAnimationCubicPaced](../caanimationcalculationmode/cubicpaced.md). To create an animation where the location value jumps from keyframe point to keyframe point (without interpolation in between), use the [kCAAnimationDiscrete](../caanimationcalculationmode/discrete.md) value. To animate along the path by interpolating values between points, use the [kCAAnimationLinear](../caanimationcalculationmode/linear.md) value.

## See Also

### Related Documentation

- [rotationMode](rotationmode.md) — Determines whether objects animating along the path rotate to match the path tangent.

### Providing keyframe values

- [values](values.md) — An array of objects that specify the keyframe values to use for the animation.
