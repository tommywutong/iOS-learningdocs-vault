---
title: colorPosterize()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/colorposterize()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colorposterize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/colorposterize%28%29.json'
content_hash: 'sha256:4bee847b5958a2b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# colorPosterize()

<sub>Type Method</sub>

Flattens an image’s colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func colorPosterize() -> any CIFilter & CIColorPosterize
```

## Return Value

The modified image.

## Discussion

This method applies the color posterize filter to an image. The effect remaps red, green, and blue color components to a specified brightness value. The effect mimics the look of a silk-screened poster.

The color posterize filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **levels** — A `float` representing the brightness level as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that flattens the colors in the input image:

```swift
func colorPosterize(inputImage: CIImage) -> CIImage {
    let colorPosterizeFilter = CIFilter.colorPosterize()
    colorPosterizeFilter.inputImage = inputImage
    colorPosterizeFilter.levels = 6
    return colorPosterizeFilter.outputImage!
}
```

![](../../../../attachments/39be8ca534504185ee1958ed9bb3733a/media-3545025@2x.png)

<sub>Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close-up, in focus, with good light and no effects. In the photo on the right, a color posterize filter is applied, resulting in the image having less color variation.</sub>

## See Also

### Color Effect Filters

- [+ colorCrossPolynomialFilter](<colorcrosspolynomial().md>) — Adjusts an image’s color by applying polynomial cross-products.
- [+ colorCubeFilter](<colorcube().md>) — Adjusts an image’s pixels using a three-dimensional color table.
- [+ colorCubeWithColorSpaceFilter](<colorcubewithcolorspace().md>) — Adjusts an image’s pixels using a three-dimensional color table in specified color space.
- [+ colorCubesMixedWithMaskFilter](<colorcubesmixedwithmask().md>) — Alters an image’s pixels using a three-dimensional color tables and a mask image.
- [+ colorCurvesFilter](<colorcurves().md>) — Adjusts an image’s color curves.
- [+ colorInvertFilter](<colorinvert().md>) — Inverts an image’s colors.
- [+ colorMapFilter](<colormap().md>) — Performs a transformation of the input image colors to colors from a gradient image.
- [+ colorMonochromeFilter](<colormonochrome().md>) — Adjusts an image’s colors to shades of a single color.
- [+ convertLabToRGBFilter](<convertlabtorgb().md>) — Converts an image from CIELAB to RGB color space.
- [+ convertRGBtoLabFilter](<convertrgbtolab().md>) — Converts an image from RGB to CIELAB color space.
- [+ ditherFilter](<dither().md>) — Applies randomized noise to produce a processed look.
- [+ documentEnhancerFilter](<documentenhancer().md>) — Adjusts an image’s shadows and contrast.
- [+ falseColorFilter](<falsecolor().md>) — Replaces an image’s colors with specified colors.
- [+ LabDeltaE](<labdeltae().md>) — Compares an image’s color values.
- [+ maskToAlphaFilter](<masktoalpha().md>) — Converts an image to a white image with an alpha component.
