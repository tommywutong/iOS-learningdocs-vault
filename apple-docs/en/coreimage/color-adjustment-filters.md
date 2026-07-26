---
title: Color Adjustment Filters
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/color-adjustment-filters
source_url: 'https://developer.apple.com/documentation/coreimage/color-adjustment-filters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/color-adjustment-filters.json'
content_hash: 'sha256:92cf0dd0c313ca25'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# Color Adjustment Filters

<sub>API Collection</sub>

Apply color transformations, including exposure, hue, and tint adjustments.

## Topics

### Filters

- [+ colorAbsoluteDifferenceFilter](<cifilter-swift.class/colorabsolutedifference().md>) — Calculates the absolute difference between each color component in the input images.
- [+ colorClampFilter](<cifilter-swift.class/colorclamp().md>) — Alters the colors in an image based on color components.
- [+ colorControlsFilter](<cifilter-swift.class/colorcontrols().md>) — Alters the brightness, contrast, and saturation of an image’s colors.
- [+ colorMatrixFilter](<cifilter-swift.class/colormatrix().md>) — Alters the colors in an image based on vectors provided.
- [+ colorPolynomialFilter](<cifilter-swift.class/colorpolynomial().md>) — Alters an image’s colors.
- [+ colorThresholdFilter](<cifilter-swift.class/colorthreshold().md>) — Compares the red, green, and blue components of the input image to a threshold and sets them to 1 or 0.
- [+ colorThresholdOtsuFilter](<cifilter-swift.class/colorthresholdotsu().md>) — Compares the red, green, and blue components of the input image against a threshold calculated using Otsu’s algorithm.
- [+ depthToDisparityFilter](<cifilter-swift.class/depthtodisparity().md>) — Converts from an image containing depth data to an image containing disparity data.
- [+ disparityToDepthFilter](<cifilter-swift.class/disparitytodepth().md>) — Creates depth data from an image containing disparity data.
- [+ exposureAdjustFilter](<cifilter-swift.class/exposureadjust().md>) — Adjusts an image’s exposure.
- [+ gammaAdjustFilter](<cifilter-swift.class/gammaadjust().md>) — Alters an image’s transition between black and white.
- [+ hueAdjustFilter](<cifilter-swift.class/hueadjust().md>) — Modifies an image’s hue.
- [+ linearToSRGBToneCurveFilter](<cifilter-swift.class/lineartosrgbtonecurve().md>) — Alters an image’s color intensity.
- [+ sRGBToneCurveToLinearFilter](<cifilter-swift.class/srgbtonecurvetolinear().md>) — Converts the colors in an image from sRGB to linear.
- [+ temperatureAndTintFilter](<cifilter-swift.class/temperatureandtint().md>) — Alters an image’s temperature and tint.
- [+ toneCurveFilter](<cifilter-swift.class/tonecurve().md>) — Alters an image’s tone curve according to a series of data points.
- [+ vibranceFilter](<cifilter-swift.class/vibrance().md>) — Adjusts an image’s vibrancy.
- [+ whitePointAdjustFilter](<cifilter-swift.class/whitepointadjust().md>) — Adjusts the image’s white-point.

### Protocols

- [CIColorAbsoluteDifference](cicolorabsolutedifference.md)
- [CIColorClamp](cicolorclamp.md) — The properties you use to configure a color clamp filter.
- [CIColorControls](cicolorcontrols.md) — The properties you use to configure a color controls filter.
- [CIColorMatrix](cicolormatrix.md) — The properties you use to configure a color matrix filter.
- [CIColorPolynomial](cicolorpolynomial.md) — The properties you use to configure a color polynomial filter.
- [CIColorThreshold](cicolorthreshold.md)
- [CIColorThresholdOtsu](cicolorthresholdotsu.md)
- [CIDepthToDisparity](cidepthtodisparity.md) — The properties you use to configure a depth-to-disparity filter.
- [CIDisparityToDepth](cidisparitytodepth.md) — The properties you use to configure a disparity-to-depth filter.
- [CIExposureAdjust](ciexposureadjust.md) — The properties you use to configure an exposure adjust filter.
- [CIGammaAdjust](cigammaadjust.md) — The properties you use to configure a gamma adjust filter.
- [CIHueAdjust](cihueadjust.md) — The properties you use to configure a hue adjust filter.
- [CILinearToSRGBToneCurve](cilineartosrgbtonecurve.md) — The properties you use to configure a linear-to-sRGB filter.
- [CISRGBToneCurveToLinear](cisrgbtonecurvetolinear.md) — The properties you use to configure an sRGB-to-linear filter.
- [CISystemToneMap](cisystemtonemap.md) — The protocol for the System Tone Map filter.
- [CITemperatureAndTint](citemperatureandtint.md) — The properties you use to configure a temperature and tint filter.
- [CIToneCurve](citonecurve.md) — The properties you use to configure a tone curve filter.
- [CIVibrance](civibrance.md) — The properties you use to configure a vibrance filter.
- [CIWhitePointAdjust](ciwhitepointadjust.md) — The properties you use to configure a white-point adjust filter.

## See Also

### Filter Catalog

- [Blur Filters](blur-filters.md) — Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Effect Filters](color-effect-filters.md) — Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite-operations.md) — Composite images by using a range of blend modes and compositing operators.
- [Convolution Filters](convolution-filters.md) — Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion-filters.md) — Apply distortion to images.
- [Generator Filters](generator-filters.md) — Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](geometry-adjustment-filters.md) — Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](gradient-filters.md) — Generate linear and radial gradients.
- [Halftone Effect Filters](halftone-effect-filters.md) — Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](reduction-filters.md) — Create statistical information about an image.
- [Sharpening Filters](sharpening-filters.md) — Apply sharpening to images.
- [Stylizing Filters](stylizing-filters.md) — Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile-effect-filters.md) — Produce tiled images from source images.
- [Transition Filters](transition-filters.md) — Transition between two images by using effects including page curl and swipe.
