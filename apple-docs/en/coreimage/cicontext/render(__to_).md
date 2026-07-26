---
title: 'render(_:to:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/render(_:to:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/render(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/render%28_%3Ato%3A%29.json'
content_hash: 'sha256:373757b8dd3b45de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# render(_:to:)

<sub>Instance Method</sub>

Renders an image into a pixel buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func render(_ image: CIImage, to buffer: CVPixelBuffer)
```

## Parameters

- `image` — A Core Image image object.

- `buffer` — The destination pixel buffer.

## See Also

### Rendering Images

- [- createCGImage:fromRect:](<createcgimage(__from_).md>) — Creates a Core Graphics image from a region of a Core Image image instance.
- [- createCGImage:fromRect:format:colorSpace:](<createcgimage(__from_format_colorspace_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling the pixel format and color space of the `CGImage`.
- [- createCGImage:fromRect:format:colorSpace:deferred:](<createcgimage(__from_format_colorspace_deferred_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling when the image is rendered.
- [- render:toBitmap:rowBytes:bounds:format:colorSpace:](<render(__tobitmap_rowbytes_bounds_format_colorspace_).md>) — Renders to the given bitmap.
- [- render:toCVPixelBuffer:bounds:colorSpace:](<render(__to_bounds_colorspace_)-2k8l2.md>) — Renders a region of an image into a pixel buffer.
- [- render:toIOSurface:bounds:colorSpace:](<render(__to_bounds_colorspace_)-54b9l.md>) — Renders a region of an image into an IOSurface object.
- [- render:toMTLTexture:commandBuffer:bounds:colorSpace:](<render(__to_commandbuffer_bounds_colorspace_).md>) — Renders a region of an image to a Metal texture.
