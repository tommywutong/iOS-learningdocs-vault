---
title: sRGBToneCurveToLinear()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/srgbtonecurvetolinear()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/srgbtonecurvetolinear()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/srgbtonecurvetolinear%28%29.json'
content_hash: 'sha256:17c4bae226aa5da4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# sRGBToneCurveToLinear()

<sub>Type Method</sub>

Converts the colors in an image from sRGB to linear.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func sRGBToneCurveToLinear() -> any CIFilter & CISRGBToneCurveToLinear
```

## Return Value

The modified image.

## Discussion

This method applies the sRGB-tone-curve-to-linear filter to an image. The effect converts an image in sRGB space to linear color space.

The sRGB-tone-curve-to-linear filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).

The following code creates a filter that converts from sRGB to linear color space.

```swift
func sRGBToLinear(inputImage: CIImage) -> CIImage {
    let sRGBToLinearFilter = CIFilter.sRGBToneCurveToLinear()
    sRGBToLinearFilter.inputImage = inputImage
    return sRGBToLinearFilter.outputImage!
}
```

![](../../../../attachments/72ef711ef6c57190f761df92ef484e52/media-4333632@2x.png)

<sub>Two versions of a photograph side by side. The photo on the left shows the Golden Gate Bridge against a clear sky. In the photo on the right, a sRGB-to-linear tone curve filter is applied, and the image is considerably darker.</sub>

## See Also

### Filters

- [+ colorAbsoluteDifferenceFilter](<colorabsolutedifference().md>) — Calculates the absolute difference between each color component in the input images.
- [+ colorClampFilter](<colorclamp().md>) — Alters the colors in an image based on color components.
- [+ colorControlsFilter](<colorcontrols().md>) — Alters the brightness, contrast, and saturation of an image’s colors.
- [+ colorMatrixFilter](<colormatrix().md>) — Alters the colors in an image based on vectors provided.
- [+ colorPolynomialFilter](<colorpolynomial().md>) — Alters an image’s colors.
- [+ colorThresholdFilter](<colorthreshold().md>) — Compares the red, green, and blue components of the input image to a threshold and sets them to 1 or 0.
- [+ colorThresholdOtsuFilter](<colorthresholdotsu().md>) — Compares the red, green, and blue components of the input image against a threshold calculated using Otsu’s algorithm.
- [+ depthToDisparityFilter](<depthtodisparity().md>) — Converts from an image containing depth data to an image containing disparity data.
- [+ disparityToDepthFilter](<disparitytodepth().md>) — Creates depth data from an image containing disparity data.
- [+ exposureAdjustFilter](<exposureadjust().md>) — Adjusts an image’s exposure.
- [+ gammaAdjustFilter](<gammaadjust().md>) — Alters an image’s transition between black and white.
- [+ hueAdjustFilter](<hueadjust().md>) — Modifies an image’s hue.
- [+ linearToSRGBToneCurveFilter](<lineartosrgbtonecurve().md>) — Alters an image’s color intensity.
- [+ temperatureAndTintFilter](<temperatureandtint().md>) — Alters an image’s temperature and tint.
- [+ toneCurveFilter](<tonecurve().md>) — Alters an image’s tone curve according to a series of data points.
