---
title: RAW Image Options
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/raw-image-options
source_url: 'https://developer.apple.com/documentation/coreimage/raw-image-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/raw-image-options.json'
content_hash: 'sha256:b047a7b0bea29262'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md) · [CIFilter](cifilter-swift.class.md)

# RAW Image Options

<sub>API Collection</sub>

Options for creating a [CIFilter](cifilter-swift.class.md) object from RAW image data.

## Overview

You can also use the key [kCIInputEVKey](kciinputevkey.md) for RAW images.

## Topics

### Constants

- [kCIInputDecoderVersionKey](cirawfilteroption/decoderversion.md) — A key for the version number of the method to be used for decoding. A newly initialized object defaults to the newest available decoder version for the given image type. You can request an alternative, older version to maintain compatibility with older releases. Must be one of the values listed for the [kCISupportedDecoderVersionsKey](cirawfilteroption/supporteddecoderversions.md) key, otherwise a `nil` output image is generated. The associated value must be an `NSNumber` object that specifies an integer value in range of `0` to the current decoder version. When you request a specific version of the decoder, Core Image produces an image that is _visually_ the same across different versions of the operating system. Core Image, however, does not guarantee that  the same bits are produced across different versions of the operating system. That’s because the rounding behavior of floating-point arithmetic can vary due to differences in compilers or hardware. Note that this option has no effect if the image used for initialization is not RAW. _(deprecated)_
- [kCISupportedDecoderVersionsKey](cirawfilteroption/supporteddecoderversions.md) — A key for the supported decoder versions. _(deprecated)_
- [kCIInputBoostKey](cirawfilteroption/boostamount.md) — A key for the amount of boost to apply to an image. _(deprecated)_
- [kCIInputNeutralChromaticityXKey](cirawfilteroption/neutralchromaticityx.md) — The x value of the chromaticity. _(deprecated)_
- [kCIInputNeutralChromaticityYKey](cirawfilteroption/neutralchromaticityy.md) — The y value of the chromaticity. _(deprecated)_
- [kCIInputNeutralTemperatureKey](cirawfilteroption/neutraltemperature.md) — A key for neutral temperature. _(deprecated)_
- [kCIInputNeutralTintKey](cirawfilteroption/neutraltint.md) — A key for the neutral tint. _(deprecated)_
- [kCIInputNeutralLocationKey](cirawfilteroption/neutrallocation.md) — A key for the neutral position. Use this key to set the location in geometric coordinates of the unrotated output image that should be used as neutral. You cannot query this value; it is undefined for reading. The associated value is a two-element [CIVector](civector.md) object that specifies the location (`x`, `y`). _(deprecated)_
- [kCIInputScaleFactorKey](cirawfilteroption/scalefactor.md) — A key for the scale factor. _(deprecated)_
- [kCIInputAllowDraftModeKey](cirawfilteroption/allowdraftmode.md) — A key for allowing draft mode. _(deprecated)_
- [kCIInputIgnoreImageOrientationKey](cirawfilteroption/ignoreimageorientation.md) — A key for specifying whether to ignore the image orientation _(deprecated)_
- [kCIInputImageOrientationKey](cirawfilteroption/imageorientation.md) — A key for the image orientation. _(deprecated)_
- [kCIInputEnableSharpeningKey](cirawfilteroption/enablesharpening.md) — A key for the sharpening state. _(deprecated)_
- [kCIInputEnableChromaticNoiseTrackingKey](cirawfilteroption/enablechromaticnoisetracking.md) — A key for progressive chromatic noise tracking (based on ISO and exposure time). _(deprecated)_
- [kCIInputNoiseReductionAmountKey](cirawfilteroption/noisereductionamount.md) — A key for the amount to reduce noise in the image. _(deprecated)_
- [kCIInputEnableVendorLensCorrectionKey](cirawfilteroption/enablevendorlenscorrection.md) — A key for whether to automatically correct for image distortion from known lenses. _(deprecated)_
- [kCIInputLuminanceNoiseReductionAmountKey](cirawfilteroption/luminancenoisereductionamount.md) — A key for the amount of noise reduction to apply to luminance data in the image. _(deprecated)_
- [kCIInputColorNoiseReductionAmountKey](cirawfilteroption/colornoisereductionamount.md) — A key for the amount of noise reduction to apply to color data in the image. _(deprecated)_
- [kCIInputNoiseReductionSharpnessAmountKey](cirawfilteroption/noisereductionsharpnessamount.md) — A key for the amount of sharpness enhancement to apply during noise reduction. _(deprecated)_
- [kCIInputNoiseReductionContrastAmountKey](cirawfilteroption/noisereductioncontrastamount.md) — A key for the amount of contrast enhancement to apply during noise reduction. _(deprecated)_
- [kCIInputNoiseReductionDetailAmountKey](cirawfilteroption/noisereductiondetailamount.md) — A key for the amount of detail enhancement to apply during noise reduction. _(deprecated)_
- [kCIInputBoostShadowAmountKey](cirawfilteroption/boostshadowamount.md) — A key for the amount to boost the shadow areas of the image. _(deprecated)_
- [kCIInputBiasKey](kciinputbiaskey.md) — Simple bias value.
- [kCIInputLinearSpaceFilter](cirawfilteroption/linearspacefilter.md) — A key for the filter to apply to the image while it is temporarily in a linear color space as part of  RAW image processing. The associated value must be a [CIFilter](cifilter-swift.class.md) object. _(deprecated)_
- [kCIOutputNativeSizeKey](cirawfilteroption/outputnativesize.md) — A key for the full native size of the original, non-transformed RAW image. The associated value is a [CIVector](civector.md) object whose X and Y values are the image’s width and height. This key is read-only. _(deprecated)_
- [kCIActiveKeys](cirawfilteroption/activekeys.md) — A key for the set of input keys available for use. _(deprecated)_

## See Also

### Constants

- [Filter Attribute Keys](filter-attribute-keys.md) — Attributes for a filter and its parameters.
- [Data Type Attributes](data-type-attributes.md) — Numeric data types.
- [Vector Quantity Attributes](vector-quantity-attributes.md) — Vector data types.
- [Color Attribute Keys](color-attribute-keys.md) — Color types.
- [Image Attribute Keys](image-attribute-keys.md) — Image Types
- [Filter Category Keys](filter-category-keys.md) — Categories of filters.
- [Options for Applying a Filter](options-for-applying-a-filter.md) — Options that control the application of a custom Core Image filter.
- [User Interface Control Options](user-interface-control-options.md) — Sets of controls for various user scenarios.
- [User Interface Options](user-interface-options.md) — Keys or values for the size of the input parameter controls for a filter view.
- [Filter Parameter Keys](filter-parameter-keys.md) — Keys for input parameters to filters.
