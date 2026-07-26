---
title: lineCap
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cashapelayer/linecap
source_url: 'https://developer.apple.com/documentation/quartzcore/cashapelayer/linecap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cashapelayer/linecap.json'
content_hash: 'sha256:e7cf856c5f6fea09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAShapeLayer](../cashapelayer.md)

# lineCap

<sub>Instance Property</sub>

Specifies the line cap style for the shape’s path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var lineCap: CAShapeLayerLineCap { get set }
```

## Discussion

The line cap style specifies the shape of the endpoints of an open path when stroked. The supported values are described in [Line Cap Values](../line-cap-values.md). The following figure shows the appearance of the available line cap styles.

![](../../../../attachments/5639a2a1fdd14a26edcf53a53ca3d86a/media-1965770.gif)

The default is [kCALineCapButt](../cashapelayerlinecap/butt.md).

## See Also

### Accessing Shape Style Properties

- [fillColor](fillcolor.md) — The color used to fill the shape’s path. Animatable.
- [fillRule](fillrule.md) — The fill rule used when filling the shape’s path.
- [lineDashPattern](linedashpattern.md) — The dash pattern applied to the shape’s path when stroked.
- [lineDashPhase](linedashphase.md) — The dash phase applied to the shape’s path when stroked. Animatable.
- [lineJoin](linejoin.md) — Specifies the line join style for the shape’s path.
- [lineWidth](linewidth.md) — Specifies the line width of the shape’s path. Animatable.
- [miterLimit](miterlimit.md) — The miter limit used when stroking the shape’s path. Animatable.
- [strokeColor](strokecolor.md) — The color used to stroke the shape’s path. Animatable.
- [strokeStart](strokestart.md) — The relative location at which to begin stroking the path. Animatable.
- [strokeEnd](strokeend.md) — The relative location at which to stop stroking the path. Animatable.
