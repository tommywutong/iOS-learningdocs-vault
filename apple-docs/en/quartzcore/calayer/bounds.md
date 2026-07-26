---
title: bounds
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/bounds
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/bounds.json'
content_hash: 'sha256:15c09b07632cb7ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# bounds

<sub>Instance Property</sub>

The layer’s bounds rectangle. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bounds: CGRect { get set }
```

## Discussion

The bounds rectangle is the origin and size of the layer in its own coordinate space. When you create a new standalone layer, the default value for this property is an empty rectangle, which you must change before using the layer. The values of each coordinate in the rectangle are measured in points.

For more information about the relationship between the [frame](frame.md), [bounds](bounds.md), [anchorPoint](anchorpoint.md) and [position](position.md) properties, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

## See Also

### Modifying the layer geometry

- [frame](frame.md) — The layer’s frame rectangle.
- [position](position.md) — The layer’s position in its superlayer’s coordinate space. Animatable.
- [zPosition](zposition.md) — The layer’s position on the z axis. Animatable.
- [anchorPointZ](anchorpointz.md) — The anchor point for the layer’s position along the z axis. Animatable.
- [anchorPoint](anchorpoint.md) — Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [contentsScale](contentsscale.md) — The scale factor applied to the layer.
