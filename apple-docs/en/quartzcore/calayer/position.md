---
title: position
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/position
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/position'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/position.json'
content_hash: 'sha256:c647c25f1d6c9e84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# position

<sub>Instance Property</sub>

The layer’s position in its superlayer’s coordinate space. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var position: CGPoint { get set }
```

## Discussion

The value of this property is specified in points and is always specified relative to the value in the [anchorPoint](anchorpoint.md) property. For new standalone layers, the default position is set to (0.0, 0.0). Changing the [frame](frame.md) property also updates the value in this property.

For more information about the relationship between the [frame](frame.md), [bounds](bounds.md), [anchorPoint](anchorpoint.md) and [position](position.md) properties, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

## See Also

### Modifying the layer geometry

- [frame](frame.md) — The layer’s frame rectangle.
- [bounds](bounds.md) — The layer’s bounds rectangle. Animatable.
- [zPosition](zposition.md) — The layer’s position on the z axis. Animatable.
- [anchorPointZ](anchorpointz.md) — The anchor point for the layer’s position along the z axis. Animatable.
- [anchorPoint](anchorpoint.md) — Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [contentsScale](contentsscale.md) — The scale factor applied to the layer.
