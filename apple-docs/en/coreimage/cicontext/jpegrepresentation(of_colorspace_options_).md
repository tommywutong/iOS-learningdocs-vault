---
title: 'jpegRepresentation(of:colorSpace:options:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/jpegrepresentation(of:colorspace:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/jpegrepresentation(of:colorspace:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/jpegrepresentation%28of%3Acolorspace%3Aoptions%3A%29.json'
content_hash: 'sha256:c254e00f5e3da8e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# jpegRepresentation(of:colorSpace:options:)

<sub>Instance Method</sub>

Renders the image and exports the resulting image data in JPEG format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func jpegRepresentation(of image: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any] = [:]) -> Data?
```

## Parameters

- `image` — The image object to render.

- `colorSpace` — The color space in which to render the output image. This color space must conform to either the [CGColorSpaceModel.rgb](../../coregraphics/cgcolorspacemodel/rgb.md) or [CGColorSpaceModel.monochrome](../../coregraphics/cgcolorspacemodel/monochrome.md) model and must be compatible with the specified pixel format.

- `options` — A dictionary with additional options for export. Use the [kCGImageDestinationLossyCompressionQuality](../../imageio/kcgimagedestinationlossycompressionquality.md) key to specify JPEG compression level.  Other supported keys include [kCIImageRepresentationAVDepthData](../ciimagerepresentationoption/avdepthdata.md), [kCIImageRepresentationDepthImage](../ciimagerepresentationoption/depthimage.md), and [kCIImageRepresentationDisparityImage](../ciimagerepresentationoption/disparityimage.md).

## Return Value

A data representation of the rendered image in JPEG format, or `nil` if the image could not be rendered.

## Discussion

To render an image for export, the image’s contents must not be empty and its [extent](../ciimage/extent.md) dimensions must be finite. To export after applying a filter whose output has infinite extent, see the [- imageByClampingToExtent](<../ciimage/clampedtoextent().md>) method.

## See Also

### Rendering Images for Data or File Export

- [- TIFFRepresentationOfImage:format:colorSpace:options:](<tiffrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in TIFF format.
- [- PNGRepresentationOfImage:format:colorSpace:options:](<pngrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in PNG format.
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
