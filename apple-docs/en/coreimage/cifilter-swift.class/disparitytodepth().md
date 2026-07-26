---
title: disparityToDepth()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/disparitytodepth()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/disparitytodepth()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/disparitytodepth%28%29.json'
content_hash: 'sha256:f58dd7e88f305d1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# disparityToDepth()

<sub>Type Method</sub>

Creates depth data from an image containing disparity data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func disparityToDepth() -> any CIFilter & CIDisparityToDepth
```

## Return Value

The modified image.

## Discussion

The method generates the disparity-to-depth filter. The filter converts a depth data image to disparity data. You can combine with other filters to create more sophisticated images.

The disparity-to-depth filter uses the following property:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).

The following code creates a filter that generates a disparity depth map image:

```swift
func disparityToDepth(inputImage: CIImage) -> CIImage {
    let disparityToDepthFilter = CIFilter.disparityToDepth()
    disparityToDepthFilter.inputImage = inputImage
    return disparityToDepthFilter.outputImage!
}
```

![](../../../../attachments/8761d9c43fb16e406df83e47481f3aee/media-3598059@2x.png)

<sub>Two photographs of a small dog sitting on grass. The photo on the left shows the dog in the foreground with good light and a soft blur of the background. In the photo on the right, a disparity-to-depth filter is applied, resulting in a depth map created from the photo on the left. The dog in the photo and the ground are replaced with white, and the background is replaced with gray.</sub>

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
- [+ exposureAdjustFilter](<exposureadjust().md>) — Adjusts an image’s exposure.
- [+ gammaAdjustFilter](<gammaadjust().md>) — Alters an image’s transition between black and white.
- [+ hueAdjustFilter](<hueadjust().md>) — Modifies an image’s hue.
- [+ linearToSRGBToneCurveFilter](<lineartosrgbtonecurve().md>) — Alters an image’s color intensity.
- [+ sRGBToneCurveToLinearFilter](<srgbtonecurvetolinear().md>) — Converts the colors in an image from sRGB to linear.
- [+ temperatureAndTintFilter](<temperatureandtint().md>) — Alters an image’s temperature and tint.
- [+ toneCurveFilter](<tonecurve().md>) — Alters an image’s tone curve according to a series of data points.
