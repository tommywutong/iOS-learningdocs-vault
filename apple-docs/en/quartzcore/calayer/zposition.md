---
title: zPosition
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/zposition
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/zposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/zposition.json'
content_hash: 'sha256:49524c02148aa11e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# zPosition

<sub>Instance Property</sub>

The layer’s position on the z axis. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var zPosition: CGFloat { get set }
```

## Discussion

The default value of this property is `0`. Changing the value of this property changes the front-to-back ordering of layers onscreen. Higher values place this layer visually closer to the viewer than layers with lower values. This can affect the visibility of layers whose frame rectangles overlap.

The value of this property is measured in points. The range of this property is single-precision, floating-point `-`[greatestFiniteMagnitude](../../swift/float/greatestfinitemagnitude.md) to [greatestFiniteMagnitude](../../swift/float/greatestfinitemagnitude.md).

## See Also

### Modifying the layer geometry

- [frame](frame.md) — The layer’s frame rectangle.
- [bounds](bounds.md) — The layer’s bounds rectangle. Animatable.
- [position](position.md) — The layer’s position in its superlayer’s coordinate space. Animatable.
- [anchorPointZ](anchorpointz.md) — The anchor point for the layer’s position along the z axis. Animatable.
- [anchorPoint](anchorpoint.md) — Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [contentsScale](contentsscale.md) — The scale factor applied to the layer.
