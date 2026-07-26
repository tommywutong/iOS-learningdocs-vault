---
title: CACornerMask
framework: Core Animation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cacornermask
source_url: 'https://developer.apple.com/documentation/quartzcore/cacornermask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cacornermask.json'
content_hash: 'sha256:0c9868fbf0036c39'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CACornerMask

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CACornerMask
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [init(rawValue:)](<cacornermask/init(rawvalue_).md>)
- [kCALayerMaxXMaxYCorner](cacornermask/layermaxxmaxycorner.md)
- [kCALayerMaxXMinYCorner](cacornermask/layermaxxminycorner.md)
- [kCALayerMinXMaxYCorner](cacornermask/layerminxmaxycorner.md)
- [kCALayerMinXMinYCorner](cacornermask/layerminxminycorner.md)

## See Also

### Modifying the layer’s appearance

- [contentsGravity](calayer/contentsgravity.md) — A constant that specifies how the layer’s contents are positioned or scaled within its bounds.
- [Contents Gravity Values](contents-gravity-values.md) — The contents gravity constants specify the position of the content object when the layer bounds is larger than the bounds of the content object. They are used by the [contentsGravity](calayer/contentsgravity.md) property.
- [opacity](calayer/opacity.md) — The opacity of the receiver. Animatable.
- [hidden](calayer/ishidden.md) — A Boolean indicating whether the layer is displayed. Animatable.
- [masksToBounds](calayer/maskstobounds.md) — A Boolean indicating whether sublayers are clipped to the layer’s bounds. Animatable.
- [mask](calayer/mask.md) — An optional layer whose alpha channel is used to mask the layer’s content.
- [doubleSided](calayer/isdoublesided.md) — A Boolean indicating whether the layer displays its content when facing away from the viewer. Animatable.
- [cornerRadius](calayer/cornerradius.md) — The radius to use when drawing rounded corners for the layer’s background. Animatable.
- [maskedCorners](calayer/maskedcorners.md)
- [borderWidth](calayer/borderwidth.md) — The width of the layer’s border. Animatable.
- [borderColor](calayer/bordercolor.md) — The color of the layer’s border. Animatable.
- [backgroundColor](calayer/backgroundcolor.md) — The background color of the receiver. Animatable.
- [shadowOpacity](calayer/shadowopacity.md) — The opacity of the layer’s shadow. Animatable.
- [shadowRadius](calayer/shadowradius.md) — The blur radius (in points) used to render the layer’s shadow. Animatable.
- [shadowOffset](calayer/shadowoffset.md) — The offset (in points) of the layer’s shadow. Animatable.
