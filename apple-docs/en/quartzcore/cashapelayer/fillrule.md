---
title: fillRule
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cashapelayer/fillrule
source_url: 'https://developer.apple.com/documentation/quartzcore/cashapelayer/fillrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cashapelayer/fillrule.json'
content_hash: 'sha256:ee2cb88a6744f1f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAShapeLayer](../cashapelayer.md)

# fillRule

<sub>Instance Property</sub>

The fill rule used when filling the shape’s path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fillRule: CAShapeLayerFillRule { get set }
```

## Discussion

The possible values are shown in [Shape Fill Mode Values](../shape-fill-mode-values.md). The default is [kCAFillRuleNonZero](../cashapelayerfillrule/nonzero.md). See [Winding Rules](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Paths/Paths.html#//apple_ref/doc/uid/TP40003290-CH206-BAJIJJGD) for examples of the two fill rules.

## See Also

### Accessing Shape Style Properties

- [fillColor](fillcolor.md) — The color used to fill the shape’s path. Animatable.
- [lineCap](linecap.md) — Specifies the line cap style for the shape’s path.
- [lineDashPattern](linedashpattern.md) — The dash pattern applied to the shape’s path when stroked.
- [lineDashPhase](linedashphase.md) — The dash phase applied to the shape’s path when stroked. Animatable.
- [lineJoin](linejoin.md) — Specifies the line join style for the shape’s path.
- [lineWidth](linewidth.md) — Specifies the line width of the shape’s path. Animatable.
- [miterLimit](miterlimit.md) — The miter limit used when stroking the shape’s path. Animatable.
- [strokeColor](strokecolor.md) — The color used to stroke the shape’s path. Animatable.
- [strokeStart](strokestart.md) — The relative location at which to begin stroking the path. Animatable.
- [strokeEnd](strokeend.md) — The relative location at which to stop stroking the path. Animatable.
