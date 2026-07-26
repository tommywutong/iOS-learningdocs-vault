---
title: 'createCGImage(_:from:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/createcgimage(_:from:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/createcgimage(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/createcgimage%28_%3Afrom%3A%29.json'
content_hash: 'sha256:1eac1a8a055627e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# createCGImage(_:from:)

<sub>Instance Method</sub>

Creates a Core Graphics image from a region of a Core Image image instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func createCGImage(_ image: CIImage, from fromRect: CGRect) -> CGImage?
```

## Parameters

- `image` — A [CIImage](../ciimage.md) image instance for which to create a `CGImage`.

- `fromRect` — The `CGRect` region of the `image` to use. This region relative to the cartesean coordinate system of `image`. This region will be intersected with integralized and intersected with `image.extent`.

## Return Value

Returns a new `CGImage` instance. You are responsible for releasing the returned image when you no longer need it. The returned value will be `null` if the extent is empty or too big.

## Discussion

The color space of the created `CGImage` will be sRGB unless the receiving [CIContext](../cicontext.md) was created with a `kCIContextOutputColorSpace` option.

Normally the pixel format of the created CGImage will be 8 bits-per-component. It will be 16 bits-per-component float if the above color space is HDR.

## See Also

### Rendering Images

- [- createCGImage:fromRect:format:colorSpace:](<createcgimage(__from_format_colorspace_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling the pixel format and color space of the `CGImage`.
- [- createCGImage:fromRect:format:colorSpace:deferred:](<createcgimage(__from_format_colorspace_deferred_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling when the image is rendered.
- [- render:toBitmap:rowBytes:bounds:format:colorSpace:](<render(__tobitmap_rowbytes_bounds_format_colorspace_).md>) — Renders to the given bitmap.
- [- render:toCVPixelBuffer:](<render(__to_).md>) — Renders an image into a pixel buffer.
- [- render:toCVPixelBuffer:bounds:colorSpace:](<render(__to_bounds_colorspace_)-2k8l2.md>) — Renders a region of an image into a pixel buffer.
- [- render:toIOSurface:bounds:colorSpace:](<render(__to_bounds_colorspace_)-54b9l.md>) — Renders a region of an image into an IOSurface object.
- [- render:toMTLTexture:commandBuffer:bounds:colorSpace:](<render(__to_commandbuffer_bounds_colorspace_).md>) — Renders a region of an image to a Metal texture.
