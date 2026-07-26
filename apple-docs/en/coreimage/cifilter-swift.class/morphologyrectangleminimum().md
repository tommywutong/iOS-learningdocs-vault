---
title: morphologyRectangleMinimum()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/morphologyrectangleminimum()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/morphologyrectangleminimum()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/morphologyrectangleminimum%28%29.json'
content_hash: 'sha256:08349a03ad03daea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# morphologyRectangleMinimum()

<sub>Type Method</sub>

Blurs a rectangular area by reducing contrasting pixels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func morphologyRectangleMinimum() -> any CIFilter & CIMorphologyRectangleMinimum
```

## Return Value

The blurred image.

## Discussion

This method applies the morphology rectangle minimum filter to an image. The effect targets a rectangular section of the image, calculating the median color values to find colors that make up more than half the working area. Using this calculation, the effect reduces the pixels with contrasting colors to take up more of the less area. The effect is then repeated throughout the image.

The morphology rectangle minimum filter uses the following properties:

- **width** — A `float` representing the width in pixels of the working area as an [NSNumber](../../foundation/nsnumber.md).
- **height** — A `float` representing the height in pixels of the working area as an [NSNumber](../../foundation/nsnumber.md).
- **inputImage** — A [CIImage](../ciimage.md) representing the input image to apply the filter to.

The following code creates a filter that adds an intense blur to the palm trees input image:

```swift
    func morphologyRectangleMinimum(inputImage: CIImage) -> CIImage? {

        let morphologyRectangleMinimumFilter = CIFilter.morphologyRectangleMinimum()
        morphologyRectangleMinimumFilter.inputImage = inputImage
        morphologyRectangleMinimumFilter.width = 5
        morphologyRectangleMinimumFilter.height = 5
        return morphologyRectangleMinimumFilter.outputImage
    }
```

![](../../../../attachments/766ac889f685325ebd5b9c57d324d8ad/media-3544957@2x.png)

<sub>Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear and crisp. In the photo on the right, a morphology rectangle minimum blur has been applied, resulting in the image becoming hazy and the palm trees darker and less distinct.</sub>

## See Also

### Filters

- [+ bokehBlurFilter](<bokehblur().md>) — Applies a bokeh effect to an image.
- [+ boxBlurFilter](<boxblur().md>) — Applies a square-shaped blur to an area of an image.
- [+ discBlurFilter](<discblur().md>) — Applies a circle-shaped blur to an area of an image.
- [+ gaussianBlurFilter](<gaussianblur().md>) — Blurs an image with a Gaussian distribution pattern.
- [+ maskedVariableBlurFilter](<maskedvariableblur().md>) — Blurs a specified portion of an image.
- [+ medianFilter](<median().md>) — Calculates the median of an image to refine detail.
- [+ morphologyGradientFilter](<morphologygradient().md>) — Detects and highlights edges of objects.
- [+ morphologyMaximumFilter](<morphologymaximum().md>) — Blurs a circular area by enlarging contrasting pixels.
- [+ morphologyMinimumFilter](<morphologyminimum().md>) — Blurs a circular area by reducing contrasting pixels.
- [+ morphologyRectangleMaximumFilter](<morphologyrectanglemaximum().md>) — Blurs a rectangular area by enlarging contrasting pixels.
- [+ motionBlurFilter](<motionblur().md>) — Creates motion blur on an image.
- [+ noiseReductionFilter](<noisereduction().md>) — Reduces noise by sharpening the edges of objects.
- [+ zoomBlurFilter](<zoomblur().md>) — Creates a zoom blur centered around a single point on the image.
