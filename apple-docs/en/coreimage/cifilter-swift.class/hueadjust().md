---
title: hueAdjust()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/hueadjust()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/hueadjust()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/hueadjust%28%29.json'
content_hash: 'sha256:5c092749f27551c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# hueAdjust()

<sub>Type Method</sub>

Modifies an image’s hue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func hueAdjust() -> any CIFilter & CIHueAdjust
```

## Return Value

The modified image.

## Discussion

This method applies the hue-adjust filter to an image. The effect changes the hue or color of the pixels by using the angle to modify the image’s color data.

The hue-adjust filter uses the following properties:

- **`angle`** — A `float` representing the angle in radians to adjust the current hue of the image as an [NSNumber](../../foundation/nsnumber.md).
- **`inputImage`** — An image with the type [CIImage](../ciimage.md).

The following code creates a filter that shifts the hue of the image by 5 radians.

```swift
func hueAdjust(inputImage: CIImage) -> CIImage {
    let hueAdjustFilter = CIFilter.hueAdjust()
    hueAdjustFilter.inputImage = inputImage
    hueAdjustFilter.angle = 5
    return hueAdjustFilter.outputImage!
}
```

![](../../../../attachments/4252b733bdd01d08fc471fb74af6900c/media-3544999@2x.png)

<sub>Two versions of a photograph side by side. The photo on the left shows a small bunch of flowers photographed close up, in focus, with good light and no effects. In the photo on the right, a hue adjust filter is applied, transforming the colors in the image to have a purple hue.</sub>

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
- [+ linearToSRGBToneCurveFilter](<lineartosrgbtonecurve().md>) — Alters an image’s color intensity.
- [+ sRGBToneCurveToLinearFilter](<srgbtonecurvetolinear().md>) — Converts the colors in an image from sRGB to linear.
- [+ temperatureAndTintFilter](<temperatureandtint().md>) — Alters an image’s temperature and tint.
- [+ toneCurveFilter](<tonecurve().md>) — Alters an image’s tone curve according to a series of data points.
