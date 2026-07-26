---
title: makeMutablePixelBuffer()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositionrendercontext/makemutablepixelbuffer()
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/makemutablepixelbuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionrendercontext/makemutablepixelbuffer%28%29.json'
content_hash: 'sha256:3755fe89bede1bda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionRenderContext](../avvideocompositionrendercontext.md)

# makeMutablePixelBuffer()

<sub>Instance Method</sub>

Vends a CVMutablePixelBuffer to use for rendering. The buffer will have its kCVImageBufferCleanApertureKey and kCVImageBufferPixelAspectRatioKey attachments set to match the current composition processor properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeMutablePixelBuffer() throws -> CVMutablePixelBuffer
```

## Return Value

A CVMutablePixelBuffer to use for rendering.

## Discussion

> [!danger] Throws
> Insufficient memory or other system error.

## See Also

### Creating the pixel buffer

- [- newPixelBuffer](<newpixelbuffer().md>) — Returns a pixel buffer to use for rendering. _(deprecated)_
