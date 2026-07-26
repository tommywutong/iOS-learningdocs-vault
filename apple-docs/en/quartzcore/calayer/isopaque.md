---
title: isOpaque
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/isopaque
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/isopaque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/isopaque.json'
content_hash: 'sha256:983e58ce05b8edc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# isOpaque

<sub>Instance Property</sub>

A Boolean value indicating whether the layer contains completely opaque content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isOpaque: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). If your app draws completely opaque content that fills the layer’s bounds, setting this property to [true](../../swift/true.md) lets the system optimize the rendering behavior for the layer. Specifically, when the layer creates the backing store for your drawing commands, Core Animation omits the alpha channel of that backing store. Doing so can improve the performance of compositing operations. If you set the value of this property to [true](../../swift/true.md), you must fill the layer’s bounds with opaque content.

Setting this property affects only the backing store managed by Core Animation. If you assign an image with an alpha channel to the layer’s [contents](contents.md) property, that image retains its alpha channel regardless of the value of this property.

## See Also

### Configuring the layer’s rendering behavior

- [edgeAntialiasingMask](edgeantialiasingmask.md) — A bitmask defining how the edges of the receiver are rasterized.
- [- contentsAreFlipped](<contentsareflipped().md>) — Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.
- [geometryFlipped](isgeometryflipped.md) — A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.
- [drawsAsynchronously](drawsasynchronously.md) — A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.
- [shouldRasterize](shouldrasterize.md) — A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [rasterizationScale](rasterizationscale.md) — The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [contentsFormat](contentsformat.md) — A hint for the desired storage format of the layer contents.
- [- renderInContext:](<render(in_).md>) — Renders the layer and its sublayers into the specified context.
