---
title: paletteCentroid()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/palettecentroid()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/palettecentroid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/palettecentroid%28%29.json'
content_hash: 'sha256:f04ce54d428be2ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# paletteCentroid()

<sub>Type Method</sub>

Calculates the location of an image’s colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func paletteCentroid() -> any CIFilter & CIPaletteCentroid
```

## Return Value

The modified image.

## Discussion

This method applies the palette centroid filter to an image. The filter locates colors in the input image that the palette image defines and `outputImage.extent` provides the location of the colors of the image. You can combine with other filters to create more sophisticated images.

The palette centroid filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`paletteImage`** — An image that has the dimensions of _N_ x 1 where _N_ represents the amount of colors in the image, with type [CIImage](../ciimage.md).
- **`perceptual`** — A Boolean value that specifies if the filter applies the color palette in a perceptual color space.

The following code creates a filter that calculates the extent of the palette color:

```swift
func paletteCentroid(inputImage: CIImage, paletteImage: CIImage) -> CIImage {
    let paletteCentroidFilter = CIFilter.paletteCentroid()
    paletteCentroidFilter.inputImage = inputImage
    paletteCentroidFilter.paletteImage = paletteImage
    paletteCentroidFilter.perceptual = false
    return paletteCentroidFilter.outputImage!
}
```

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
- [+ colorPosterizeFilter](<colorposterize().md>) — Flattens an image’s colors.
- [+ convertLabToRGBFilter](<convertlabtorgb().md>) — Converts an image from CIELAB to RGB color space.
- [+ convertRGBtoLabFilter](<convertrgbtolab().md>) — Converts an image from RGB to CIELAB color space.
- [+ ditherFilter](<dither().md>) — Applies randomized noise to produce a processed look.
- [+ documentEnhancerFilter](<documentenhancer().md>) — Adjusts an image’s shadows and contrast.
- [+ falseColorFilter](<falsecolor().md>) — Replaces an image’s colors with specified colors.
- [+ LabDeltaE](<labdeltae().md>) — Compares an image’s color values.
