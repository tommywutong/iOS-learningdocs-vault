---
title: 'writeJPEGRepresentation(of:to:colorSpace:options:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/writejpegrepresentation(of:to:colorspace:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/writejpegrepresentation(of:to:colorspace:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/writejpegrepresentation%28of%3Ato%3Acolorspace%3Aoptions%3A%29.json'
content_hash: 'sha256:3b812c824b187ae3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# writeJPEGRepresentation(of:to:colorSpace:options:)

<sub>Instance Method</sub>

Renders the image and exports the resulting image data as a file in JPEG format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func writeJPEGRepresentation(of image: CIImage, to url: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any] = [:]) throws
```

## Parameters

- `image` — The image object to render.

- `url` — The file URL at which to write the output JPEG file.

- `colorSpace` — The color space in which to render the output image. This color space must conform to either the [CGColorSpaceModel.rgb](../../coregraphics/cgcolorspacemodel/rgb.md) or [CGColorSpaceModel.monochrome](../../coregraphics/cgcolorspacemodel/monochrome.md) model and must be compatible with the specified pixel format.

- `options` — A dictionary with additional options for export. Use the [kCGImageDestinationLossyCompressionQuality](../../imageio/kcgimagedestinationlossycompressionquality.md) key to specify JPEG compression level.

## Discussion

To render an image for export, the image’s contents must not be empty and its [extent](../ciimage/extent.md) dimensions must be finite. To export after applying a filter whose output has infinite extent, see the [- imageByClampingToExtent](<../ciimage/clampedtoextent().md>) method.

## See Also

### Rendering Images for Data or File Export

- [- TIFFRepresentationOfImage:format:colorSpace:options:](<tiffrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in TIFF format.
- [- JPEGRepresentationOfImage:colorSpace:options:](<jpegrepresentation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in JPEG format.
- [- PNGRepresentationOfImage:format:colorSpace:options:](<pngrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in PNG format.
- [- HEIFRepresentationOfImage:format:colorSpace:options:](<heifrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF format.
- [- HEIF10RepresentationOfImage:colorSpace:options:error:](<heif10representation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF10 format.
- [- OpenEXRRepresentationOfImage:options:error:](<openexrrepresentation(of_options_).md>) — Renders the image and exports the resulting image data in open EXR format.
- [- writeTIFFRepresentationOfImage:toURL:format:colorSpace:options:error:](<writetiffrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in TIFF format.
- [- writePNGRepresentationOfImage:toURL:format:colorSpace:options:error:](<writepngrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in PNG format.
- [- writeHEIFRepresentationOfImage:toURL:format:colorSpace:options:error:](<writeheifrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF format.
- [- writeHEIF10RepresentationOfImage:toURL:colorSpace:options:error:](<writeheif10representation(of_to_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF10 format.
- [- writeOpenEXRRepresentationOfImage:toURL:options:error:](<writeopenexrrepresentation(of_to_options_).md>) — Renders the image and exports the resulting image data as a file in open EXR format.
- [CIImageRepresentationOption](../ciimagerepresentationoption.md)
