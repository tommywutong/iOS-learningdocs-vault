---
title: temperatureAndTint()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/temperatureandtint()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/temperatureandtint()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/temperatureandtint%28%29.json'
content_hash: 'sha256:f413e52e9f08eccc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# temperatureAndTint()

<sub>Type Method</sub>

Alters an image’s temperature and tint.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint
```

## Return Value

The modified image.

## Discussion

This method applies the image temperature and tint filter to an image. The effect adjusts the white balance of the input image to match the `targetNeutral` property, resulting in a cooler or warmer tone image.

The temperature and tint filter uses the following properties:

- **`neutral`** — A `vector` containing the source white point as a [CIVector](../civector.md).
- **`targetNeutral`** — A vector containing the desired white point as a [CIVector](../civector.md).
- **`inputImage`** — An image with the type [CIImage](../ciimage.md).

The following code creates a filter that adds an orange hue to the input image:

```swift
func tempatureAndTint(inputImage: CIImage) -> CIImage {
    let tempatureAndTintFilter = CIFilter.temperatureAndTint()
    tempatureAndTintFilter.inputImage = inputImage
    tempatureAndTintFilter.neutral = CIVector(x: 11500, y: 10)
    tempatureAndTintFilter.targetNeutral = CIVector(x: 4000, y: 0)
    return tempatureAndTintFilter.outputImage!
}
```

![](../../../../attachments/6d6bbf21f7ffb12672085daa6eb5b656/media-3545008@2x.png)

<sub>Two versions of a photograph side by side. The photo on the left shows a small bunch of flowers photographed close up, in focus, with good light and no effects. In the photo on the right, a temperature and tint filter is applied, resulting in a orange hue applied to the image.</sub>

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
- [+ sRGBToneCurveToLinearFilter](<srgbtonecurvetolinear().md>) — Converts the colors in an image from sRGB to linear.
- [+ toneCurveFilter](<tonecurve().md>) — Alters an image’s tone curve according to a series of data points.
