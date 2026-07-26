---
title: fillColor
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cashapelayer/fillcolor
source_url: 'https://developer.apple.com/documentation/quartzcore/cashapelayer/fillcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cashapelayer/fillcolor.json'
content_hash: 'sha256:b0dbdbf9a64080f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAShapeLayer](../cashapelayer.md)

# fillColor

<sub>Instance Property</sub>

The color used to fill the shape’s path. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fillColor: CGColor? { get set }
```

## Discussion

Setting `fillColor` to `nil` results in no fill being rendered.

Default is opaque black.

## See Also

### Accessing Shape Style Properties

- [fillRule](fillrule.md) — The fill rule used when filling the shape’s path.
- [lineCap](linecap.md) — Specifies the line cap style for the shape’s path.
- [lineDashPattern](linedashpattern.md) — The dash pattern applied to the shape’s path when stroked.
- [lineDashPhase](linedashphase.md) — The dash phase applied to the shape’s path when stroked. Animatable.
- [lineJoin](linejoin.md) — Specifies the line join style for the shape’s path.
- [lineWidth](linewidth.md) — Specifies the line width of the shape’s path. Animatable.
- [miterLimit](miterlimit.md) — The miter limit used when stroking the shape’s path. Animatable.
- [strokeColor](strokecolor.md) — The color used to stroke the shape’s path. Animatable.
- [strokeStart](strokestart.md) — The relative location at which to begin stroking the path. Animatable.
- [strokeEnd](strokeend.md) — The relative location at which to stop stroking the path. Animatable.
