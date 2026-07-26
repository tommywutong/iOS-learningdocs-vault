---
title: drawsAsynchronously
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/drawsasynchronously
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/drawsasynchronously'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/drawsasynchronously.json'
content_hash: 'sha256:03f399b3ef8a9dc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# drawsAsynchronously

<sub>Instance Property</sub>

A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var drawsAsynchronously: Bool { get set }
```

## Discussion

When this property is set to [true](../../swift/true.md), the graphics context used to draw the layer’s contents queues drawing commands and executes them on a background thread rather than executing them synchronously. Performing these commands asynchronously can improve performance in some apps. However, you should always measure the actual performance benefits before enabling this capability.

The default value for this property is [false](../../swift/false.md).

## See Also

### Configuring the layer’s rendering behavior

- [opaque](isopaque.md) — A Boolean value indicating whether the layer contains completely opaque content.
- [edgeAntialiasingMask](edgeantialiasingmask.md) — A bitmask defining how the edges of the receiver are rasterized.
- [- contentsAreFlipped](<contentsareflipped().md>) — Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.
- [geometryFlipped](isgeometryflipped.md) — A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.
- [shouldRasterize](shouldrasterize.md) — A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [rasterizationScale](rasterizationscale.md) — The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [contentsFormat](contentsformat.md) — A hint for the desired storage format of the layer contents.
- [- renderInContext:](<render(in_).md>) — Renders the layer and its sublayers into the specified context.
