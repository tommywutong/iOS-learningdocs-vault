---
title: 'heif10Representation(of:colorSpace:options:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/heif10representation(of:colorspace:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/heif10representation(of:colorspace:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/heif10representation%28of%3Acolorspace%3Aoptions%3A%29.json'
content_hash: 'sha256:bbf8add8121af8aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# heif10Representation(of:colorSpace:options:)

<sub>Instance Method</sub>

Renders the image and exports the resulting image data in HEIF10 format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func heif10Representation(of image: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any] = [:]) throws -> Data
```

## Parameters

- `image` — The image object to render.

- `colorSpace` — The color space in which to render the output image.

- `options` — A dictionary with additional options for export.

## See Also

### Rendering Images for Data or File Export

- [- TIFFRepresentationOfImage:format:colorSpace:options:](<tiffrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in TIFF format.
- [- JPEGRepresentationOfImage:colorSpace:options:](<jpegrepresentation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in JPEG format.
- [- PNGRepresentationOfImage:format:colorSpace:options:](<pngrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in PNG format.
- [- HEIFRepresentationOfImage:format:colorSpace:options:](<heifrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF format.
- [- OpenEXRRepresentationOfImage:options:error:](<openexrrepresentation(of_options_).md>) — Renders the image and exports the resulting image data in open EXR format.
- [- writeTIFFRepresentationOfImage:toURL:format:colorSpace:options:error:](<writetiffrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in TIFF format.
- [- writeJPEGRepresentationOfImage:toURL:colorSpace:options:error:](<writejpegrepresentation(of_to_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in JPEG format.
- [- writePNGRepresentationOfImage:toURL:format:colorSpace:options:error:](<writepngrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in PNG format.
- [- writeHEIFRepresentationOfImage:toURL:format:colorSpace:options:error:](<writeheifrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF format.
- [- writeHEIF10RepresentationOfImage:toURL:colorSpace:options:error:](<writeheif10representation(of_to_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF10 format.
- [- writeOpenEXRRepresentationOfImage:toURL:options:error:](<writeopenexrrepresentation(of_to_options_).md>) — Renders the image and exports the resulting image data as a file in open EXR format.
- [CIImageRepresentationOption](../ciimagerepresentationoption.md)
