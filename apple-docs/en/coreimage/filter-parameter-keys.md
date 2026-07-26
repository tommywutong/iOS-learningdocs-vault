---
title: Filter Parameter Keys
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/filter-parameter-keys
source_url: 'https://developer.apple.com/documentation/coreimage/filter-parameter-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/filter-parameter-keys.json'
content_hash: 'sha256:6d259eb5564b9b8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md) · [CIFilter](cifilter-swift.class.md)

# Filter Parameter Keys

<sub>API Collection</sub>

Keys for input parameters to filters.

## Overview

These keys represent some of the most commonly used input parameters. A filter can use other kinds of input parameters.

## Topics

### Constants

- [kCIDynamicRangeConstrainedHigh](cidynamicrangeoption/constrainedhigh.md) — Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.
- [kCIDynamicRangeHigh](cidynamicrangeoption/high.md) — Use High dynamic range.
- [kCIDynamicRangeStandard](cidynamicrangeoption/standard.md) — Use Standard dynamic range.
- [kCIInputAmountKey](kciinputamountkey.md)
- [kCIInputAngleKey](kciinputanglekey.md) — The angle.
- [kCIInputAspectRatioKey](kciinputaspectratiokey.md) — Aspect Ratio.
- [kCIInputBackgroundImageKey](kciinputbackgroundimagekey.md) — A key for the [CIImage](ciimage.md) object to use as a background image.
- [kCIInputBacksideImageKey](kciinputbacksideimagekey.md) — A key to get or set the backside image for a transition Core Image filter.
- [kCIInputBiasVectorKey](kciinputbiasvectorkey.md) — A key to get or set the vector bias value of a Core Image filter.
- [kCIInputBrightnessKey](kciinputbrightnesskey.md) — Brightness level.
- [kCIInputCenterKey](kciinputcenterkey.md) — A key for a [CIVector](civector.md) object that specifies the center of the area, as _x_  and  _y_- coordinates, to be filtered.
- [kCIInputColorKey](kciinputcolorkey.md) — A key for a [CIColor](cicolor.md) object that specifies a color value.
- [kCIInputColor0Key](kciinputcolor0key.md) — A key to get or set a color value of a Core Image filter.
- [kCIInputColor1Key](kciinputcolor1key.md) — A key to get or set a color value of a Core Image filter.
- [kCIInputColorSpaceKey](kciinputcolorspacekey.md) — A key to get or set a color space value of a Core Image filter.
- [kCIInputContrastKey](kciinputcontrastkey.md) — A contrast level.
- [kCIInputCountKey](kciinputcountkey.md) — A key to get or set the scalar count value of a Core Image filter.
- [kCIInputDepthImageKey](kciinputdepthimagekey.md) — A key for an image with depth values.
- [kCIInputDisparityImageKey](kciinputdisparityimagekey.md) — A key for an image with disparity values.
- [kCIInputEVKey](kciinputevkey.md) — How many F-stops brighter or darker the image should be.
- [kCIInputExtentKey](kciinputextentkey.md) — A key for a [CIVector](civector.md) object that specifies a rectangle that defines the extent of the effect.
- [kCIInputExtrapolateKey](kciinputextrapolatekey.md) — A key to get or set the boolean behavior of a Core Image filter that specifies if the filter should extrapolate a table beyond the defined range.
- [kCIInputGradientImageKey](kciinputgradientimagekey.md) — A key for a [CIImage](ciimage.md) object that specifies an environment map with alpha. Typically, this image contains highlight and shadow.
- [kCIInputImageKey](kciinputimagekey.md) — A key for the [CIImage](ciimage.md) object to use as an input image. For filters that also use a background image, this key refers to the foreground image.
- [kCIInputIntensityKey](kciinputintensitykey.md) — An intensity value.
- [kCIInputMaskImageKey](kciinputmaskimagekey.md) — A key for a [CIImage](ciimage.md) object to use as a mask.
- [kCIInputMatteImageKey](kciinputmatteimagekey.md)
- [kCIInputPaletteImageKey](kciinputpaletteimagekey.md) — A key to get or set the palette image for a  Core Image filter.
- [kCIInputPerceptualKey](kciinputperceptualkey.md) — A key to get or set the boolean behavior of a Core Image filter that specifies if the filter should operate in linear or perceptual colors.
- [kCIInputPoint0Key](kciinputpoint0key.md) — A key to get or set the coordinate value of a Core Image filter.
The value for this key needs to be a [CIVector](civector.md) instance containing the `x,y` coordinate.
- [kCIInputPoint1Key](kciinputpoint1key.md) — A key to get or set a coordinate value of a Core Image filter.
The value for this key needs to be a [CIVector](civector.md) instance containing the `x,y` coordinate.
- [kCIInputRadiusKey](kciinputradiuskey.md) — The distance from the center of an effect.
- [kCIInputRadius0Key](kciinputradius0key.md) — A key to get or set the geometric radius value of a Core Image filter.
- [kCIInputRadius1Key](kciinputradius1key.md) — A key to get or set the geometric radius value of a Core Image filter.
- [kCIInputRefractionKey](kciinputrefractionkey.md) — The index of refraction to use.
- [kCIInputSaturationKey](kciinputsaturationkey.md) — The amount to adjust the saturation.
- [kCIInputScaleKey](kciinputscalekey.md) — The amount of scale to apply.
- [kCIInputShadingImageKey](kciinputshadingimagekey.md) — A key for a [CIImage](ciimage.md) object  that specifies an environment map with alpha values. Typically this image contains highlight and shadow.
- [kCIInputSharpnessKey](kciinputsharpnesskey.md) — Amount of sharpening to apply.
- [kCIInputTargetImageKey](kciinputtargetimagekey.md) — A key for a [CIImage](ciimage.md) object that is the target image for a transition.
- [kCIInputThresholdKey](kciinputthresholdkey.md) — A key to get or set the scalar threshold value of a Core Image filter.
- [kCIInputTimeKey](kciinputtimekey.md) — Specify a time.
- [kCIInputTransformKey](kciinputtransformkey.md) — Transformation to apply.
- [kCIInputVersionKey](kciinputversionkey.md) — Version Key
- [kCIInputWeightsKey](kciinputweightskey.md) — A key for a [CIVector](civector.md) object that describes a weight matrix for use with a convolution filter.
- [kCIInputWidthKey](kciinputwidthkey.md) — A key for a scalar value that specifies the width of the effect.
- [kCIOutputImageKey](kcioutputimagekey.md) — A key for the [CIImage](ciimage.md) object produced by a filter.

### Deprecated

- [kCIInputBaselineExposureKey](cirawfilteroption/baselineexposure.md) — The amount of baseline exposure applied. _(deprecated)_
- [kCIInputDisableGamutMapKey](cirawfilteroption/disablegamutmap.md) — Whether or not to disable gamut mapping. _(deprecated)_
- [kCIInputMoireAmountKey](cirawfilteroption/moireamount.md) — The amount of moiré reduction to apply. _(deprecated)_

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
- [RAW Image Options](raw-image-options.md) — Options for creating a [CIFilter](cifilter-swift.class.md) object from RAW image data.
