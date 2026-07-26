---
title: 'createCGImage(_:from:format:colorSpace:deferred:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/createcgimage(_:from:format:colorspace:deferred:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/createcgimage(_:from:format:colorspace:deferred:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/createcgimage%28_%3Afrom%3Aformat%3Acolorspace%3Adeferred%3A%29.json'
content_hash: 'sha256:618dc8142bdc3bbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# createCGImage(_:from:format:colorSpace:deferred:)

<sub>Instance Method</sub>

Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling when the image is rendered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func createCGImage(_ image: CIImage, from fromRect: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool) -> CGImage?
```

## Parameters

- `image` — A [CIImage](../ciimage.md) image instance for which to create a `CGImage`.

- `fromRect` — The `CGRect` region of the `image` to use. This region relative to the cartesean coordinate system of `image`. This region will be intersected with integralized and intersected with `image.extent`.

- `format` — A [CIFormat](../ciformat.md) to specify the pixel format of the created `CGImage`. For example, if `kCIFormatRGBX16` is specified, then the created `CGImage` will be 16 bits-per-component and opaque.

- `colorSpace` — The `CGColorSpace` for the output image. This color space must have either `CGColorSpaceModel.rgb` or `CGColorSpaceModel.monochrome` and be compatible with the specified pixel format.

- `deferred` — Controls when Core Image renders `image`. - True: rendering of `image` is deferred until the created `CGImage` rendered. - False: the `image` is rendered immediately.

## Return Value

Returns a new `CGImage` instance. You are responsible for releasing the returned image when you no longer need it. The returned value will be `null` if the extent is empty or too big.

## See Also

### Rendering Images

- [- createCGImage:fromRect:](<createcgimage(__from_).md>) — Creates a Core Graphics image from a region of a Core Image image instance.
- [- createCGImage:fromRect:format:colorSpace:](<createcgimage(__from_format_colorspace_).md>) — Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling the pixel format and color space of the `CGImage`.
- [- render:toBitmap:rowBytes:bounds:format:colorSpace:](<render(__tobitmap_rowbytes_bounds_format_colorspace_).md>) — Renders to the given bitmap.
- [- render:toCVPixelBuffer:](<render(__to_).md>) — Renders an image into a pixel buffer.
- [- render:toCVPixelBuffer:bounds:colorSpace:](<render(__to_bounds_colorspace_)-2k8l2.md>) — Renders a region of an image into a pixel buffer.
- [- render:toIOSurface:bounds:colorSpace:](<render(__to_bounds_colorspace_)-54b9l.md>) — Renders a region of an image into an IOSurface object.
- [- render:toMTLTexture:commandBuffer:bounds:colorSpace:](<render(__to_commandbuffer_bounds_colorspace_).md>) — Renders a region of an image to a Metal texture.
