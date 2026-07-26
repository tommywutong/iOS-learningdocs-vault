---
title: 'writeHEIF10Representation(of:to:colorSpace:options:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/writeheif10representation(of:to:colorspace:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/writeheif10representation(of:to:colorspace:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/writeheif10representation%28of%3Ato%3Acolorspace%3Aoptions%3A%29.json'
content_hash: 'sha256:0dff13b70efbb183'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# writeHEIF10Representation(of:to:colorSpace:options:)

<sub>Instance Method</sub>

Renders the image and exports the resulting image data as a file in HEIF10 format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func writeHEIF10Representation(of image: CIImage, to url: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any] = [:]) throws
```

## Parameters

- `image` — The image object to render.

- `url` — The file URL at which to write the output HEIF file.

- `colorSpace` — The color space in which to render the output image.

- `options` — A dictionary with additional options for export.

## See Also

### Rendering Images for Data or File Export

- [- TIFFRepresentationOfImage:format:colorSpace:options:](<tiffrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in TIFF format.
- [- JPEGRepresentationOfImage:colorSpace:options:](<jpegrepresentation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in JPEG format.
- [- PNGRepresentationOfImage:format:colorSpace:options:](<pngrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in PNG format.
- [- HEIFRepresentationOfImage:format:colorSpace:options:](<heifrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF format.
- [- HEIF10RepresentationOfImage:colorSpace:options:error:](<heif10representation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF10 format.
- [- OpenEXRRepresentationOfImage:options:error:](<openexrrepresentation(of_options_).md>) — Renders the image and exports the resulting image data in open EXR format.
- [- writeTIFFRepresentationOfImage:toURL:format:colorSpace:options:error:](<writetiffrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in TIFF format.
- [- writeJPEGRepresentationOfImage:toURL:colorSpace:options:error:](<writejpegrepresentation(of_to_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in JPEG format.
- [- writePNGRepresentationOfImage:toURL:format:colorSpace:options:error:](<writepngrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in PNG format.
- [- writeHEIFRepresentationOfImage:toURL:format:colorSpace:options:error:](<writeheifrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF format.
- [- writeOpenEXRRepresentationOfImage:toURL:options:error:](<writeopenexrrepresentation(of_to_options_).md>) — Renders the image and exports the resulting image data as a file in open EXR format.
- [CIImageRepresentationOption](../ciimagerepresentationoption.md)
