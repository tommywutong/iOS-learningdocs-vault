---
title: edgeAntialiasingMask
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/edgeantialiasingmask
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/edgeantialiasingmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/edgeantialiasingmask.json'
content_hash: 'sha256:42971a70f3fbcc88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# edgeAntialiasingMask

<sub>Instance Property</sub>

A bitmask defining how the edges of the receiver are rasterized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var edgeAntialiasingMask: CAEdgeAntialiasingMask { get set }
```

## Discussion

This property specifies which edges of the layer are antialiased and is a combination of the constants defined in [CAEdgeAntialiasingMask](../caedgeantialiasingmask.md). You can enable or disable antialiasing for each edge (top, left, bottom, right) separately. By default antialiasing is enabled for all edges.

Typically, you would use this property to disable antialiasing for edges that abut edges of other layers, to eliminate the seams that would otherwise occur.

## See Also

### Configuring the layer’s rendering behavior

- [opaque](isopaque.md) — A Boolean value indicating whether the layer contains completely opaque content.
- [- contentsAreFlipped](<contentsareflipped().md>) — Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.
- [geometryFlipped](isgeometryflipped.md) — A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.
- [drawsAsynchronously](drawsasynchronously.md) — A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.
- [shouldRasterize](shouldrasterize.md) — A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [rasterizationScale](rasterizationscale.md) — The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [contentsFormat](contentsformat.md) — A hint for the desired storage format of the layer contents.
- [- renderInContext:](<render(in_).md>) — Renders the layer and its sublayers into the specified context.
