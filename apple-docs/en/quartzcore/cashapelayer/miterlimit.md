---
title: miterLimit
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cashapelayer/miterlimit
source_url: 'https://developer.apple.com/documentation/quartzcore/cashapelayer/miterlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cashapelayer/miterlimit.json'
content_hash: 'sha256:67381bb5dfcd0f47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAShapeLayer](../cashapelayer.md)

# miterLimit

<sub>Instance Property</sub>

The miter limit used when stroking the shape’s path. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var miterLimit: CGFloat { get set }
```

## Discussion

If the current line join style is set to [kCALineJoinMiter](../cashapelayerlinejoin/miter.md) (see [lineJoin](linejoin.md)), the miter limit determines whether the lines should be joined with a bevel instead of a miter. The length of the miter is divided by the line width. If the result is greater than the miter limit, the path is drawn with a bevel.

Default is `10.0`.

## See Also

### Accessing Shape Style Properties

- [fillColor](fillcolor.md) — The color used to fill the shape’s path. Animatable.
- [fillRule](fillrule.md) — The fill rule used when filling the shape’s path.
- [lineCap](linecap.md) — Specifies the line cap style for the shape’s path.
- [lineDashPattern](linedashpattern.md) — The dash pattern applied to the shape’s path when stroked.
- [lineDashPhase](linedashphase.md) — The dash phase applied to the shape’s path when stroked. Animatable.
- [lineJoin](linejoin.md) — Specifies the line join style for the shape’s path.
- [lineWidth](linewidth.md) — Specifies the line width of the shape’s path. Animatable.
- [strokeColor](strokecolor.md) — The color used to stroke the shape’s path. Animatable.
- [strokeStart](strokestart.md) — The relative location at which to begin stroking the path. Animatable.
- [strokeEnd](strokeend.md) — The relative location at which to stop stroking the path. Animatable.
