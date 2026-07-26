---
title: cornerRadius
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/cornerradius
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/cornerradius'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/cornerradius.json'
content_hash: 'sha256:38b5b3079be97715'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# cornerRadius

<sub>Instance Property</sub>

The radius to use when drawing rounded corners for the layer’s background. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var cornerRadius: CGFloat { get set }
```

## Discussion

Setting the radius to a value greater than `0.0` causes the layer to begin drawing rounded corners on its background. By default, the corner radius does not apply to the image in the layer’s [contents](contents.md) property; it applies only to the background color and border of the layer. However, setting the [masksToBounds](maskstobounds.md) property to [true](../../swift/true.md) causes the content to be clipped to the rounded corners.

The default value of this property is `0.0`.

## See Also

### Modifying the layer’s appearance

- [contentsGravity](contentsgravity.md) — A constant that specifies how the layer’s contents are positioned or scaled within its bounds.
- [Contents Gravity Values](../contents-gravity-values.md) — The contents gravity constants specify the position of the content object when the layer bounds is larger than the bounds of the content object. They are used by the [contentsGravity](contentsgravity.md) property.
- [opacity](opacity.md) — The opacity of the receiver. Animatable.
- [hidden](ishidden.md) — A Boolean indicating whether the layer is displayed. Animatable.
- [masksToBounds](maskstobounds.md) — A Boolean indicating whether sublayers are clipped to the layer’s bounds. Animatable.
- [mask](mask.md) — An optional layer whose alpha channel is used to mask the layer’s content.
- [doubleSided](isdoublesided.md) — A Boolean indicating whether the layer displays its content when facing away from the viewer. Animatable.
- [maskedCorners](maskedcorners.md)
- [CACornerMask](../cacornermask.md)
- [borderWidth](borderwidth.md) — The width of the layer’s border. Animatable.
- [borderColor](bordercolor.md) — The color of the layer’s border. Animatable.
- [backgroundColor](backgroundcolor.md) — The background color of the receiver. Animatable.
- [shadowOpacity](shadowopacity.md) — The opacity of the layer’s shadow. Animatable.
- [shadowRadius](shadowradius.md) — The blur radius (in points) used to render the layer’s shadow. Animatable.
- [shadowOffset](shadowoffset.md) — The offset (in points) of the layer’s shadow. Animatable.
