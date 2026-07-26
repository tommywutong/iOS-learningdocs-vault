---
title: newPixelBuffer()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.9+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avvideocompositionrendercontext/newpixelbuffer()
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/newpixelbuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionrendercontext/newpixelbuffer%28%29.json'
content_hash: 'sha256:b3ed1424a87749d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionRenderContext](../avvideocompositionrendercontext.md)

# newPixelBuffer()

<sub>Instance Method</sub>

Returns a pixel buffer to use for rendering.

> [!warning] Deprecated
> Use newReadOnlyPixelBuffer() instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func newPixelBuffer() -> CVPixelBuffer?
```

## Return Value

A [CVPixelBuffer](../../corevideo/cvpixelbuffer.md) to use for rendering.

## Discussion

The buffer’s [kCVImageBufferCleanApertureKey](../../corevideo/kcvimagebuffercleanaperturekey.md) and [kCVImageBufferPixelAspectRatioKey](../../corevideo/kcvimagebufferpixelaspectratiokey.md) attachments are set to match the current composition processor properties. You’re responsible for calling [CVBufferRelease](../../corevideo/cvbufferrelease.md) on the pixel buffer.

## See Also

### Creating the pixel buffer

- [makeMutablePixelBuffer()](<makemutablepixelbuffer().md>) — Vends a CVMutablePixelBuffer to use for rendering. The buffer will have its kCVImageBufferCleanApertureKey and kCVImageBufferPixelAspectRatioKey attachments set to match the current composition processor properties.
