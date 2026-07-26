---
title: anchorPoint
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/anchorpoint
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/anchorpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/anchorpoint.json'
content_hash: 'sha256:e57abf7aa7c82e97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# anchorPoint

<sub>Instance Property</sub>

Defines the anchor point of the layer’s bounds rectangle. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var anchorPoint: CGPoint { get set }
```

## Discussion

You specify the value for this property using the unit coordinate space. The default value of this property is (0.5, 0.5), which represents the center of the layer’s bounds rectangle. All geometric manipulations to the view occur about the specified point. For example, applying a rotation transform to a layer with the default anchor point causes the layer to rotate around its center. Changing the anchor point to a different location would cause the layer to rotate around that new point.

For more information about the relationship between the [frame](frame.md), [bounds](bounds.md), [anchorPoint](anchorpoint.md) and [position](position.md) properties, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

## See Also

### Modifying the layer geometry

- [frame](frame.md) — The layer’s frame rectangle.
- [bounds](bounds.md) — The layer’s bounds rectangle. Animatable.
- [position](position.md) — The layer’s position in its superlayer’s coordinate space. Animatable.
- [zPosition](zposition.md) — The layer’s position on the z axis. Animatable.
- [anchorPointZ](anchorpointz.md) — The anchor point for the layer’s position along the z axis. Animatable.
- [contentsScale](contentsscale.md) — The scale factor applied to the layer.
