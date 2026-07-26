---
title: strokeStart
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cashapelayer/strokestart
source_url: 'https://developer.apple.com/documentation/quartzcore/cashapelayer/strokestart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cashapelayer/strokestart.json'
content_hash: 'sha256:dd25574e2f3e9ae1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAShapeLayer](../cashapelayer.md)

# strokeStart

<sub>Instance Property</sub>

The relative location at which to begin stroking the path. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var strokeStart: CGFloat { get set }
```

## Discussion

The value of this property must be in the range 0.0 to 1.0. The default value of this property is 0.0.

Combined with the [strokeEnd](strokeend.md) property, this property defines the subregion of the path to stroke. The value in this property indicates the relative point along the path at which to begin stroking while the [strokeEnd](strokeend.md) property defines the end point. A value of 0.0 represents the beginning of the path while a value of 1.0 represents the end of the path. Values in between are interpreted linearly along the path length.

## See Also

### Accessing Shape Style Properties

- [fillColor](fillcolor.md) — The color used to fill the shape’s path. Animatable.
- [fillRule](fillrule.md) — The fill rule used when filling the shape’s path.
- [lineCap](linecap.md) — Specifies the line cap style for the shape’s path.
- [lineDashPattern](linedashpattern.md) — The dash pattern applied to the shape’s path when stroked.
- [lineDashPhase](linedashphase.md) — The dash phase applied to the shape’s path when stroked. Animatable.
- [lineJoin](linejoin.md) — Specifies the line join style for the shape’s path.
- [lineWidth](linewidth.md) — Specifies the line width of the shape’s path. Animatable.
- [miterLimit](miterlimit.md) — The miter limit used when stroking the shape’s path. Animatable.
- [strokeColor](strokecolor.md) — The color used to stroke the shape’s path. Animatable.
- [strokeEnd](strokeend.md) — The relative location at which to stop stroking the path. Animatable.
