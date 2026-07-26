---
title: allowsEdgeAntialiasing
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/allowsedgeantialiasing
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/allowsedgeantialiasing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/allowsedgeantialiasing.json'
content_hash: 'sha256:ae376106c6bea398'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# allowsEdgeAntialiasing

<sub>Instance Property</sub>

A Boolean indicating whether the layer is allowed to perform edge antialiasing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allowsEdgeAntialiasing: Bool { get set }
```

## Discussion

When the value is [true](../../swift/true.md), the layer is allowed to antialias its edges, as requested by the value in the layer’s [edgeAntialiasingMask](edgeantialiasingmask.md) property. The default value is read from the boolean `UIViewEdgeAntialiasing` property in the main bundle’s `Info.plist` file. If no value is found, the default value is [false](../../swift/false.md).

## See Also

### Related Documentation

- [edgeAntialiasingMask](edgeantialiasingmask.md) — A bitmask defining how the edges of the receiver are rasterized.

### Modifying the layer’s appearance

- [contentsGravity](contentsgravity.md) — A constant that specifies how the layer’s contents are positioned or scaled within its bounds.
- [Contents Gravity Values](../contents-gravity-values.md) — The contents gravity constants specify the position of the content object when the layer bounds is larger than the bounds of the content object. They are used by the [contentsGravity](contentsgravity.md) property.
- [opacity](opacity.md) — The opacity of the receiver. Animatable.
- [hidden](ishidden.md) — A Boolean indicating whether the layer is displayed. Animatable.
- [masksToBounds](maskstobounds.md) — A Boolean indicating whether sublayers are clipped to the layer’s bounds. Animatable.
- [mask](mask.md) — An optional layer whose alpha channel is used to mask the layer’s content.
- [doubleSided](isdoublesided.md) — A Boolean indicating whether the layer displays its content when facing away from the viewer. Animatable.
- [cornerRadius](cornerradius.md) — The radius to use when drawing rounded corners for the layer’s background. Animatable.
- [maskedCorners](maskedcorners.md)
- [CACornerMask](../cacornermask.md)
- [borderWidth](borderwidth.md) — The width of the layer’s border. Animatable.
- [borderColor](bordercolor.md) — The color of the layer’s border. Animatable.
- [backgroundColor](backgroundcolor.md) — The background color of the receiver. Animatable.
- [shadowOpacity](shadowopacity.md) — The opacity of the layer’s shadow. Animatable.
- [shadowRadius](shadowradius.md) — The blur radius (in points) used to render the layer’s shadow. Animatable.
