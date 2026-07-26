---
title: 'render(_:to:bounds:colorSpace:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/render(_:to:bounds:colorspace:)-2k8l2'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/render(_:to:bounds:colorspace:)-2k8l2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/render%28_%3Ato%3Abounds%3Acolorspace%3A%29-2k8l2.json'
content_hash: 'sha256:9035c60e1284c49e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# render(_:to:bounds:colorSpace:)

<sub>Instance Method</sub>

Renders a region of an image into a pixel buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func render(_ image: CIImage, to buffer: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)
```

## Parameters

- `image` — A Core Image image object.

- `buffer` — The destination pixel buffer.

- `bounds` — The rectangle in the destination pixel buffer to draw into.

- `colorSpace` — The color space of the destination pixel buffer.

## See Also

### Rendering Images

- [- createCGImage:fromRect:](<createcgimage(__from_).md>) — Creates a Core Graphics image from a region of a Core Image image instance.
- [- createCGImage:fromRect:format:colorSpace:](<createcgimage(__from_format_colorspace_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling the pixel format and color space of the `CGImage`.
- [- createCGImage:fromRect:format:colorSpace:deferred:](<createcgimage(__from_format_colorspace_deferred_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling when the image is rendered.
- [- render:toBitmap:rowBytes:bounds:format:colorSpace:](<render(__tobitmap_rowbytes_bounds_format_colorspace_).md>) — Renders to the given bitmap.
- [- render:toCVPixelBuffer:](<render(__to_).md>) — Renders an image into a pixel buffer.
- [- render:toIOSurface:bounds:colorSpace:](<render(__to_bounds_colorspace_)-54b9l.md>) — Renders a region of an image into an IOSurface object.
- [- render:toMTLTexture:commandBuffer:bounds:colorSpace:](<render(__to_commandbuffer_bounds_colorspace_).md>) — Renders a region of an image to a Metal texture.
