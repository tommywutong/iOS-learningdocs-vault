---
title: contentsScale
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/contentsscale
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/contentsscale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/contentsscale.json'
content_hash: 'sha256:2556d33416fec290'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# contentsScale

<sub>Instance Property</sub>

The scale factor applied to the layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentsScale: CGFloat { get set }
```

## Discussion

This value defines the mapping between the logical coordinate space of the layer (measured in points) and the physical coordinate space (measured in pixels). Higher scale factors indicate that each point in the layer is represented by more than one pixel at render time. For example, if the scale factor is `2.0` and the layer’s bounds are 50 x 50 points, the size of the bitmap used to present the layer’s content is 100 x 100 pixels.

The default value of this property is 1.0. For layers attached to a view, the view changes the scale factor automatically to a value that is appropriate for the current screen. For layers you create and manage yourself, you must set the value of this property yourself based on the resolution of the screen and the content you are providing. Core Animation uses the value you specify as a cue to determine how to render your content.

## See Also

### Modifying the layer geometry

- [frame](frame.md) — The layer’s frame rectangle.
- [bounds](bounds.md) — The layer’s bounds rectangle. Animatable.
- [position](position.md) — The layer’s position in its superlayer’s coordinate space. Animatable.
- [zPosition](zposition.md) — The layer’s position on the z axis. Animatable.
- [anchorPointZ](anchorpointz.md) — The anchor point for the layer’s position along the z axis. Animatable.
- [anchorPoint](anchorpoint.md) — Defines the anchor point of the layer’s bounds rectangle. Animatable.
