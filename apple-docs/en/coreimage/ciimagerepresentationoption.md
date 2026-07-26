---
title: CIImageRepresentationOption
framework: Core Image
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimagerepresentationoption
source_url: 'https://developer.apple.com/documentation/coreimage/ciimagerepresentationoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimagerepresentationoption.json'
content_hash: 'sha256:eb7fbfb0725c7e41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIImageRepresentationOption

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CIImageRepresentationOption
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<ciimagerepresentationoption/init(rawvalue_).md>)

### Type Properties

- [kCIImageRepresentationAVDepthData](ciimagerepresentationoption/avdepthdata.md) — The depth data representation of an image.
- [kCIImageRepresentationAVPortraitEffectsMatte](ciimagerepresentationoption/avportraiteffectsmatte.md)
- [kCIImageRepresentationAVSemanticSegmentationMattes](ciimagerepresentationoption/avsemanticsegmentationmattes.md)
- [kCIImageRepresentationDepthImage](ciimagerepresentationoption/depthimage.md) — `options` dictionary key for image export methods to output depth data.
- [kCIImageRepresentationDisparityImage](ciimagerepresentationoption/disparityimage.md) — `options` dictionary key for image export methods to output disparity data.
- [kCIImageRepresentationPortraitEffectsMatteImage](ciimagerepresentationoption/portraiteffectsmatteimage.md)
- [kCIImageRepresentationSemanticSegmentationGlassesMatteImage](ciimagerepresentationoption/semanticsegmentationglassesmatteimage.md)
- [kCIImageRepresentationSemanticSegmentationHairMatteImage](ciimagerepresentationoption/semanticsegmentationhairmatteimage.md)
- [kCIImageRepresentationSemanticSegmentationSkinMatteImage](ciimagerepresentationoption/semanticsegmentationskinmatteimage.md)
- [kCIImageRepresentationSemanticSegmentationSkyMatteImage](ciimagerepresentationoption/semanticsegmentationskymatteimage.md)
- [kCIImageRepresentationSemanticSegmentationTeethMatteImage](ciimagerepresentationoption/semanticsegmentationteethmatteimage.md)
- [kCIImageRepresentationHDRImage](ciimagerepresentationoption/hdrimage.md)
- [kCIImageRepresentationHDRGainMapAsRGB](ciimagerepresentationoption/hdrgainmapasrgb.md) — An optional key and value to request the gain map channel to be color instead of monochrome.
- [kCIImageRepresentationHDRGainMapImage](ciimagerepresentationoption/hdrgainmapimage.md) — An optional key and value to save a gain map channel to a JPEG or HEIF.

## See Also

### Rendering Images for Data or File Export

- [- TIFFRepresentationOfImage:format:colorSpace:options:](<cicontext/tiffrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in TIFF format.
- [- JPEGRepresentationOfImage:colorSpace:options:](<cicontext/jpegrepresentation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in JPEG format.
- [- PNGRepresentationOfImage:format:colorSpace:options:](<cicontext/pngrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in PNG format.
- [- HEIFRepresentationOfImage:format:colorSpace:options:](<cicontext/heifrepresentation(of_format_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF format.
- [- HEIF10RepresentationOfImage:colorSpace:options:error:](<cicontext/heif10representation(of_colorspace_options_).md>) — Renders the image and exports the resulting image data in HEIF10 format.
- [- OpenEXRRepresentationOfImage:options:error:](<cicontext/openexrrepresentation(of_options_).md>) — Renders the image and exports the resulting image data in open EXR format.
- [- writeTIFFRepresentationOfImage:toURL:format:colorSpace:options:error:](<cicontext/writetiffrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in TIFF format.
- [- writeJPEGRepresentationOfImage:toURL:colorSpace:options:error:](<cicontext/writejpegrepresentation(of_to_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in JPEG format.
- [- writePNGRepresentationOfImage:toURL:format:colorSpace:options:error:](<cicontext/writepngrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in PNG format.
- [- writeHEIFRepresentationOfImage:toURL:format:colorSpace:options:error:](<cicontext/writeheifrepresentation(of_to_format_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF format.
- [- writeHEIF10RepresentationOfImage:toURL:colorSpace:options:error:](<cicontext/writeheif10representation(of_to_colorspace_options_).md>) — Renders the image and exports the resulting image data as a file in HEIF10 format.
- [- writeOpenEXRRepresentationOfImage:toURL:options:error:](<cicontext/writeopenexrrepresentation(of_to_options_).md>) — Renders the image and exports the resulting image data as a file in open EXR format.
