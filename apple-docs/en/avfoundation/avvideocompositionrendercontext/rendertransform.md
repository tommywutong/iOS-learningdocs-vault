---
title: renderTransform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositionrendercontext/rendertransform
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/rendertransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionrendercontext/rendertransform.json'
content_hash: 'sha256:4268f27eaea13f8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionRenderContext](../avvideocompositionrendercontext.md)

# renderTransform

<sub>Instance Property</sub>

A transform to apply to the source image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var renderTransform: CGAffineTransform { get }
```

## Discussion

The transform to apply to the source image incorporating the [renderScale](renderscale.md), [pixelAspectRatio](pixelaspectratio.md), and [edgeWidths](edgewidths.md).

The coordinate system origin is the top left corner of the buffer.

## See Also

### Getting the render settings

- [videoComposition](videocomposition.md) — The video composition being rendered.
- [highQualityRendering](highqualityrendering.md) — The rendering quality to use.
- [renderScale](renderscale.md) — A scaling ratio that is applied when rendering frames.
- [size](size.md) — The width and height for the rendering frames.
