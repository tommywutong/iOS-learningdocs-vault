---
title: isGeometryFlipped
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/isgeometryflipped
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/isgeometryflipped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/isgeometryflipped.json'
content_hash: 'sha256:402f6676506a9245'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# isGeometryFlipped

<sub>Instance Property</sub>

A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isGeometryFlipped: Bool { get set }
```

## Discussion

If the layer is providing the backing for a layer-backed view, the view is responsible for managing the value in this property. For standalone layers, this property controls whether geometry values for the layer are interpreted using the standard or flipped coordinate system. The value of this property does not affect the rendering of the layer’s content.

The default value of this property is [false](../../swift/false.md).

## See Also

### Configuring the layer’s rendering behavior

- [opaque](isopaque.md) — A Boolean value indicating whether the layer contains completely opaque content.
- [edgeAntialiasingMask](edgeantialiasingmask.md) — A bitmask defining how the edges of the receiver are rasterized.
- [- contentsAreFlipped](<contentsareflipped().md>) — Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.
- [drawsAsynchronously](drawsasynchronously.md) — A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.
- [shouldRasterize](shouldrasterize.md) — A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [rasterizationScale](rasterizationscale.md) — The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [contentsFormat](contentsformat.md) — A hint for the desired storage format of the layer contents.
- [- renderInContext:](<render(in_).md>) — Renders the layer and its sublayers into the specified context.
