---
title: anchorPointZ
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/anchorpointz
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/anchorpointz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/anchorpointz.json'
content_hash: 'sha256:615663ba9d4fa304'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# anchorPointZ

<sub>Instance Property</sub>

The anchor point for the layer’s position along the z axis. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var anchorPointZ: CGFloat { get set }
```

## Discussion

This property specifies the anchor point on the z axis around which geometric manipulations occur. The point is expressed as a distance (measured in points) along the z axis. The default value of this property is `0`.

## See Also

### Modifying the layer geometry

- [frame](frame.md) — The layer’s frame rectangle.
- [bounds](bounds.md) — The layer’s bounds rectangle. Animatable.
- [position](position.md) — The layer’s position in its superlayer’s coordinate space. Animatable.
- [zPosition](zposition.md) — The layer’s position on the z axis. Animatable.
- [anchorPoint](anchorpoint.md) — Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [contentsScale](contentsscale.md) — The scale factor applied to the layer.
