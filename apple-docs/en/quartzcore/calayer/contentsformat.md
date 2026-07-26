---
title: contentsFormat
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/contentsformat
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/contentsformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/contentsformat.json'
content_hash: 'sha256:8ce1ade47ebe8726'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# contentsFormat

<sub>Instance Property</sub>

A hint for the desired storage format of the layer contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentsFormat: CALayerContentsFormat { get set }
```

## Discussion

The default value of this property is [kCAContentsFormatRGBA8Uint](../calayercontentsformat/rgba8uint.md).

[UIView](../../uikit/uiview.md) and layer-backed [NSView](../../appkit/nsview.md) objects may change the value to a format appropriate for the current device.

## See Also

### Configuring the layer’s rendering behavior

- [opaque](isopaque.md) — A Boolean value indicating whether the layer contains completely opaque content.
- [edgeAntialiasingMask](edgeantialiasingmask.md) — A bitmask defining how the edges of the receiver are rasterized.
- [- contentsAreFlipped](<contentsareflipped().md>) — Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.
- [geometryFlipped](isgeometryflipped.md) — A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.
- [drawsAsynchronously](drawsasynchronously.md) — A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.
- [shouldRasterize](shouldrasterize.md) — A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [rasterizationScale](rasterizationscale.md) — The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [- renderInContext:](<render(in_).md>) — Renders the layer and its sublayers into the specified context.
