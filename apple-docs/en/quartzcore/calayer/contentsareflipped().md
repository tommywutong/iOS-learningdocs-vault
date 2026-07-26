---
title: contentsAreFlipped()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/contentsareflipped()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/contentsareflipped()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/contentsareflipped%28%29.json'
content_hash: 'sha256:c2d6810ceaa8f7a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# contentsAreFlipped()

<sub>Instance Method</sub>

Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func contentsAreFlipped() -> Bool
```

## Return Value

[true](../../swift/true.md) if the layer contents are implicitly flipped when rendered or [false](../../swift/false.md) if they are not. This method returns [false](../../swift/false.md) by default.

## Discussion

This method provides information about whether the layer’s contents are being flipped during drawing. You should not attempt to override this method and return a different value.

If the layer needs to flip its content, it returns [true](../../swift/true.md) from this method and applies a y-flip transform to the graphics context before passing it to the layer’s [- drawInContext:](<draw(in_).md>) method. Similarly, the layer converts any rectangles passed to its [- setNeedsDisplayInRect:](<setneedsdisplay(__).md>) into the flipped coordinate space.

## See Also

### Configuring the layer’s rendering behavior

- [opaque](isopaque.md) — A Boolean value indicating whether the layer contains completely opaque content.
- [edgeAntialiasingMask](edgeantialiasingmask.md) — A bitmask defining how the edges of the receiver are rasterized.
- [geometryFlipped](isgeometryflipped.md) — A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.
- [drawsAsynchronously](drawsasynchronously.md) — A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.
- [shouldRasterize](shouldrasterize.md) — A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [rasterizationScale](rasterizationscale.md) — The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [contentsFormat](contentsformat.md) — A hint for the desired storage format of the layer contents.
- [- renderInContext:](<render(in_).md>) — Renders the layer and its sublayers into the specified context.
