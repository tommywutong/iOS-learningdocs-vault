---
title: 'pngRepresentation(of:format:colorSpace:options:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/pngrepresentation(of:format:colorspace:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/pngrepresentation(of:format:colorspace:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/pngrepresentation%28of%3Aformat%3Acolorspace%3Aoptions%3A%29.json'
content_hash: 'sha256:ec55b0e829c83a23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# pngRepresentation(of:format:colorSpace:options:)

<sub>Instance Method</sub>

Renders the image and exports the resulting image data in PNG format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pngRepresentation(of image: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any] = [:]) -> Data?
```

## Parameters

- `image` — The image object to render.

- `format` — The pixel format for the output image.

- `colorSpace` — The color space in which to render the output image. This color space must conform to either the [CGColorSpaceModel.rgb](../../coregraphics/cgcolorspacemodel/rgb.md) or [CGColorSpaceModel.monochrome](../../coregraphics/cgcolorspacemodel/monochrome.md) model and must be compatible with the specified pixel format.

- `options` — No options keys are supported at this time.

## Return Value

A data representation of the rendered image in PNG format, or `nil` if the image could not be rendered.

## Discussion

To render an image for export, the image’s contents must not be empty and its [extent](../ciimage/extent.md) dimensions must be finite. To export after applying a filter whose output has infinite extent, see the [- imageByClampingToExtent](<../ciimage/clampedtoextent().md>) method.

## See Also

### Rendering Images for Data or File Export

- [- TIFFRepresentationOfImage:format:colorSpace:options:](<tiffrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in TIFF format.
- [- JPEGRepresentationOfImage:colorSpace:options:](<jpegrepresentation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in JPEG format.
- [- HEIFRepresentationOfImage:format:colorSpace:options:](<heifrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF format.
- [- HEIF10RepresentationOfImage:colorSpace:options:error:](<heif10representation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF10 format.
- [- OpenEXRRepresentationOfImage:options:error:](<openexrrepresentation(of_options_).md>) — Renders the image and exports the resulting image data in open EXR format.
- [- writeTIFFRepresentationOfImage:toURL:format:colorSpace:options:error:](<writetiffrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in TIFF format.
- [- writeJPEGRepresentationOfImage:toURL:colorSpace:options:error:](<writejpegrepresentation(of_to_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in JPEG format.
- [- writePNGRepresentationOfImage:toURL:format:colorSpace:options:error:](<writepngrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in PNG format.
- [- writeHEIFRepresentationOfImage:toURL:format:colorSpace:options:error:](<writeheifrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF format.
- [- writeHEIF10RepresentationOfImage:toURL:colorSpace:options:error:](<writeheif10representation(of_to_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF10 format.
- [- writeOpenEXRRepresentationOfImage:toURL:options:error:](<writeopenexrrepresentation(of_to_options_).md>) — Renders the image and exports the resulting image data as a file in open EXR format.
- [CIImageRepresentationOption](../ciimagerepresentationoption.md)
