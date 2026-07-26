---
title: AVVideoCompositionRenderContext
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositionrendercontext
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionrendercontext.json'
content_hash: 'sha256:91b3770ce2af3aa8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCompositionRenderContext

<sub>Class</sub>

An object that defines the context in which custom compositors render pixel buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVVideoCompositionRenderContext
```

## Overview

A render context provides size and scaling information and offers a service for efficiently providing pixel buffers from a managed pool of buffers.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating the pixel buffer

- [- newPixelBuffer](<avvideocompositionrendercontext/newpixelbuffer().md>) — Returns a pixel buffer to use for rendering. _(deprecated)_
- [makeMutablePixelBuffer()](<avvideocompositionrendercontext/makemutablepixelbuffer().md>) — Vends a CVMutablePixelBuffer to use for rendering. The buffer will have its kCVImageBufferCleanApertureKey and kCVImageBufferPixelAspectRatioKey attachments set to match the current composition processor properties.

### Getting the render settings

- [videoComposition](avvideocompositionrendercontext/videocomposition.md) — The video composition being rendered.
- [highQualityRendering](avvideocompositionrendercontext/highqualityrendering.md) — The rendering quality to use.
- [renderScale](avvideocompositionrendercontext/renderscale.md) — A scaling ratio that is applied when rendering frames.
- [renderTransform](avvideocompositionrendercontext/rendertransform.md) — A transform to apply to the source image.
- [size](avvideocompositionrendercontext/size.md) — The width and height for the rendering frames.

### Getting pixel and edge width information

- [edgeWidths](avvideocompositionrendercontext/edgewidths.md) — The width of the edge processing region on the left, top, right, and bottom edges, in pixels.
- [AVEdgeWidths](avedgewidths.md) — A structure that defines edge processing region widths.
- [pixelAspectRatio](avvideocompositionrendercontext/pixelaspectratio.md) — The pixel aspect ratio for rendered frames.
- [AVPixelAspectRatio](avpixelaspectratio.md) — A structure that defines a pixel aspect ratio for a rendering context.

## See Also

### Observing render context changes

- [- renderContextChanged:](<avvideocompositing/rendercontextchanged(__).md>) — Tells the compositor that the composition changed render contexts.
