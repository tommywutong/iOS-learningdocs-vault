---
title: 'render(_:toBitmap:rowBytes:bounds:format:colorSpace:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/render(_:tobitmap:rowbytes:bounds:format:colorspace:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/render(_:tobitmap:rowbytes:bounds:format:colorspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/render%28_%3Atobitmap%3Arowbytes%3Abounds%3Aformat%3Acolorspace%3A%29.json'
content_hash: 'sha256:78bc3b5370a8cd0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# render(_:toBitmap:rowBytes:bounds:format:colorSpace:)

<sub>Instance Method</sub>

Renders to the given bitmap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func render(_ image: CIImage, toBitmap data: UnsafeMutableRawPointer, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)
```

## Parameters

- `image` — A Core Image image object.

- `data` — Storage for the bitmap data.

- `rowBytes` — The bytes per row.

- `bounds` — The bounds of the bitmap data.

- `format` — The format of the bitmap data.

- `colorSpace` — The color space for the data. Pass `NULL` if you want to use the output color space of the context.

## See Also

### Rendering Images

- [- createCGImage:fromRect:](<createcgimage(__from_).md>) — Creates a Core Graphics image from a region of a Core Image image instance.
- [- createCGImage:fromRect:format:colorSpace:](<createcgimage(__from_format_colorspace_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling the pixel format and color space of the `CGImage`.
- [- createCGImage:fromRect:format:colorSpace:deferred:](<createcgimage(__from_format_colorspace_deferred_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling when the image is rendered.
- [- render:toCVPixelBuffer:](<render(__to_).md>) — Renders an image into a pixel buffer.
- [- render:toCVPixelBuffer:bounds:colorSpace:](<render(__to_bounds_colorspace_)-2k8l2.md>) — Renders a region of an image into a pixel buffer.
- [- render:toIOSurface:bounds:colorSpace:](<render(__to_bounds_colorspace_)-54b9l.md>) — Renders a region of an image into an IOSurface object.
- [- render:toMTLTexture:commandBuffer:bounds:colorSpace:](<render(__to_commandbuffer_bounds_colorspace_).md>) — Renders a region of an image to a Metal texture.
