---
title: highQualityRendering
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositionrendercontext/highqualityrendering
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/highqualityrendering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionrendercontext/highqualityrendering.json'
content_hash: 'sha256:1e3a5e347657b6bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionRenderContext](../avvideocompositionrendercontext.md)

# highQualityRendering

<sub>Instance Property</sub>

The rendering quality to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var highQualityRendering: Bool { get }
```

## Discussion

Specifies that the custom compositor should use higher quality, potentially slower algorithms.

Generally this property is [true](../../swift/true.md) for non-real-time use cases.

## See Also

### Getting the render settings

- [videoComposition](videocomposition.md) — The video composition being rendered.
- [renderScale](renderscale.md) — A scaling ratio that is applied when rendering frames.
- [renderTransform](rendertransform.md) — A transform to apply to the source image.
- [size](size.md) — The width and height for the rendering frames.
