---
title: CIRAWFilter
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirawfilter
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter.json'
content_hash: 'sha256:76399055477ad777'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIRAWFilter

<sub>Class</sub>

A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIRAWFilter
```

## Overview

Use this class to generate a [CIImage](ciimage.md) object based on the configuration parameters you provide.

You can use this object in conjunction with other Core Image classes—such as [CIFilter](cifilter-swift.class.md) and [CIContext](cicontext.md)—to take advantage of the built-in Core Image filters when processing images or writing custom filters.

You can also query this object to find out about the supported camera models, decoders, and filters.

## Relationships

- **Inherits From**: [CIFilter](cifilter-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a filter

- [+ filterWithCVPixelBuffer:properties:](<cirawfilter/init(cvpixelbuffer_properties_)-6209q.md>) — Creates a RAW filter from the pixel buffer and its properties that you specify.
- [+ filterWithImageData:identifierHint:](<cirawfilter/init(imagedata_identifierhint_).md>) — Creates a RAW filter from the image data and type hint that you specify.
- [+ filterWithImageURL:](<cirawfilter/init(imageurl_).md>) — Creates a RAW filter from the image at the URL location that you specify.

### Inspecting supported camera models, decoders, and filters

- [supportedCameraModels](cirawfilter/supportedcameramodels.md) — An array containing the names of all supported camera models.
- [supportedDecoderVersions](cirawfilter/supporteddecoderversions.md) — An array of all supported decoder versions for the given image type.
- [CIRAWDecoderVersion](cirawdecoderversion.md)
- [colorNoiseReductionSupported](cirawfilter/iscolornoisereductionsupported.md) — A Boolean that indicates if the current image supports color noise reduction adjustments.
- [contrastSupported](cirawfilter/iscontrastsupported.md) — A Boolean that indicates if the current image supports contrast adjustments.
- [detailSupported](cirawfilter/isdetailsupported.md) — A Boolean that indicates if the current image supports detail enhancement adjustments.
- [lensCorrectionSupported](cirawfilter/islenscorrectionsupported.md) — A Boolean that indicates if you can enable lens correction for the current image.
- [localToneMapSupported](cirawfilter/islocaltonemapsupported.md) — A Boolean that indicates if the current image supports local tone curve adjustments.
- [luminanceNoiseReductionSupported](cirawfilter/isluminancenoisereductionsupported.md) — A Boolean that indicates if the current image supports luminance noise reduction adjustments.
- [moireReductionSupported](cirawfilter/ismoirereductionsupported.md) — A Boolean that indicates if the current image supports moire artifact reduction adjustments.
- [sharpnessSupported](cirawfilter/issharpnesssupported.md) — A Boolean that indicates if the current image supports sharpness adjustments.
- [nativeSize](cirawfilter/nativesize.md) — The full native size of the unscaled image.

### Configuring a filter

- [baselineExposure](cirawfilter/baselineexposure.md) — A value that indicates the baseline exposure to apply to the image.
- [boostAmount](cirawfilter/boostamount.md) — A value that indicates the amount of global tone curve to apply to the image.
- [boostShadowAmount](cirawfilter/boostshadowamount.md) — A value that indicates the amount to boost the shadow areas of the image.
- [colorNoiseReductionAmount](cirawfilter/colornoisereductionamount.md) — A value that indicates the amount of chroma noise reduction to apply to the image.
- [contrastAmount](cirawfilter/contrastamount.md) — A value that indicates the amount of local contrast to apply to the edges of the image.
- [decoderVersion](cirawfilter/decoderversion.md) — A value that indicates the decoder version to use.
- [detailAmount](cirawfilter/detailamount.md) — A value that indicates the amount of detail enhancement to apply to the edges of the image.
- [exposure](cirawfilter/exposure.md) — A value that indicates the amount of exposure to apply to the image.
- [extendedDynamicRangeAmount](cirawfilter/extendeddynamicrangeamount.md) — A value that indicates the amount of extended dynamic range (EDR) to apply to the image.
- [draftModeEnabled](cirawfilter/isdraftmodeenabled.md) — A Boolean that indicates whether to enable draft mode.
- [gamutMappingEnabled](cirawfilter/isgamutmappingenabled.md) — A Boolean that indicates whether to enable gamut mapping.
- [lensCorrectionEnabled](cirawfilter/islenscorrectionenabled.md) — A Boolean that indicates whether to enable lens correction.
- [linearSpaceFilter](cirawfilter/linearspacefilter.md) — An optional filter you can apply to the RAW image while it’s in linear space.
- [localToneMapAmount](cirawfilter/localtonemapamount.md) — A value that indicates the amount of local tone curve to apply to the image.
- [luminanceNoiseReductionAmount](cirawfilter/luminancenoisereductionamount.md) — A value that indicates the amount of luminance noise reduction to apply to the image.
- [moireReductionAmount](cirawfilter/moirereductionamount.md) — A value that indicates the amount of moire artifact reduction to apply to high frequency areas of the image.
- [neutralChromaticity](cirawfilter/neutralchromaticity.md) — A value that indicates the amount of white balance based on chromaticity values to apply to the image.
- [neutralLocation](cirawfilter/neutrallocation.md) — A value that indicates the amount of white balance based on pixel coordinates to apply to the image.
- [neutralTemperature](cirawfilter/neutraltemperature.md) — A value that indicates the amount of white balance based on temperature values to apply to the image.
- [neutralTint](cirawfilter/neutraltint.md) — A value that indicates the amount of white balance based on tint values to apply to the image.
- [orientation](cirawfilter/orientation.md) — A value that indicates the orientation of the image.
- [portraitEffectsMatte](cirawfilter/portraiteffectsmatte.md) — An optional auxiliary image that represents the portrait effects matte of the image.
- [previewImage](cirawfilter/previewimage.md) — An optional auxiliary image that represents a preview of the original image.
- [properties](cirawfilter/properties.md) — A dictionary that contains properties of the image source.
- [scaleFactor](cirawfilter/scalefactor.md) — A value that indicates the desired scale factor to draw the output image.
- [semanticSegmentationGlassesMatte](cirawfilter/semanticsegmentationglassesmatte.md) — An optional auxiliary image that represents the semantic segmentation glasses matte of the image.
- [semanticSegmentationHairMatte](cirawfilter/semanticsegmentationhairmatte.md) — An optional auxiliary image that represents the semantic segmentation hair matte of the image.
- [semanticSegmentationSkinMatte](cirawfilter/semanticsegmentationskinmatte.md) — An optional auxiliary image that represents the semantic segmentation skin matte of the image.
- [semanticSegmentationSkyMatte](cirawfilter/semanticsegmentationskymatte.md) — An optional auxiliary image that represents the semantic segmentation sky matte of the image.
- [semanticSegmentationTeethMatte](cirawfilter/semanticsegmentationteethmatte.md) — An optional auxiliary image that represents the semantic segmentation teeth matte of the image.
- [shadowBias](cirawfilter/shadowbias.md) — A value that indicates the amount to subtract from the shadows in the image.
- [sharpnessAmount](cirawfilter/sharpnessamount.md) — A value that indicates the amount of sharpness to apply to the edges of the image.

### Initializers

- [init(CVPixelBuffer:properties:)](<cirawfilter/init(cvpixelbuffer_properties_)-6321o.md>)

### Instance Properties

- [despeckleAmount](cirawfilter/despeckleamount.md)
- [despeckleSupported](cirawfilter/isdespecklesupported.md)
- [highlightRecoveryEnabled](cirawfilter/ishighlightrecoveryenabled.md)
- [highlightRecoverySupported](cirawfilter/ishighlightrecoverysupported.md)

### Type Methods

- [+ supportedCameraModelsWithVersion:](<cirawfilter/supportedcameramodels(with_).md>) _(beta)_

## See Also

### Filters

- [CIFilter](cifilter-swift.class.md) — An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [CIColor](cicolor.md) — The Core Image class that defines a color object.
- [CIVector](civector.md) — The Core Image class that defines a vector object.
