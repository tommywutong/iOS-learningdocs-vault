---
title: vignette()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/vignette()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/vignette()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/vignette%28%29.json'
content_hash: 'sha256:82063738d2047f25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# vignette()

<sub>Type Method</sub>

Gradually darkens an image’s edges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func vignette() -> any CIFilter & CIVignette
```

## Return Value

The modified image.

## Discussion

This method applies the vignette filter to an image. This is a preconfigured effect that reduces brightness of the image at the periphery.

The vignette filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`intensity`** — A `float` representing the intensity of the vignette effect as an [NSNumber](../../foundation/nsnumber.md).
- **`radius`** — A `float` representing the radius of the effect as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that darkens the edges of the input image:

```swift
func vignette(inputImage: CIImage ) -> CIImage {
    let vignetteFilter = CIFilter.vignette()
    vignetteFilter.inputImage = inputImage
    vignetteFilter.intensity = 4
    vignetteFilter.radius = 10
    return vignetteFilter.outputImage!
}
```

![](../../../../attachments/4d8fc4e34d77f0640e1d618ee6f839d0/media-3545014@2x.png)

<sub>Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close-up, in focus, with good light and no effects. In the photo on the right, a vignette filter is applied, resulting in a gradual reduction of an image’s brightness and reduction of saturation in the periphery. </sub>

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
