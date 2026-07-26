---
title: frame
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/frame
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/frame'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/frame.json'
content_hash: 'sha256:8a7eb21aa657ac7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# frame

<sub>Instance Property</sub>

The layer’s frame rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var frame: CGRect { get set }
```

## Discussion

The frame rectangle is position and size of the layer specified in the superlayer’s coordinate space. For layers, the frame rectangle is a computed property that is derived from the values in the[bounds](bounds.md), [anchorPoint](anchorpoint.md) and [position](position.md) properties. When you assign a new value to this property, the layer changes its [position](position.md) and [bounds](bounds.md) properties to match the rectangle you specified. The values of each coordinate in the rectangle are measured in points.

Do not set the frame if the [transform](transform.md) property applies a rotation transform that is not a multiple of 90 degrees.

For more information about the relationship between the [frame](frame.md), [bounds](bounds.md), [anchorPoint](anchorpoint.md) and [position](position.md) properties, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

> [!note] Note
> The `frame` property is not directly animatable. Instead you should animate the appropriate combination of the [bounds](bounds.md), [anchorPoint](anchorpoint.md) and [position](position.md) properties to achieve the desired result.

## See Also

### Modifying the layer geometry

- [bounds](bounds.md) — The layer’s bounds rectangle. Animatable.
- [position](position.md) — The layer’s position in its superlayer’s coordinate space. Animatable.
- [zPosition](zposition.md) — The layer’s position on the z axis. Animatable.
- [anchorPointZ](anchorpointz.md) — The anchor point for the layer’s position along the z axis. Animatable.
- [anchorPoint](anchorpoint.md) — Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [contentsScale](contentsscale.md) — The scale factor applied to the layer.
