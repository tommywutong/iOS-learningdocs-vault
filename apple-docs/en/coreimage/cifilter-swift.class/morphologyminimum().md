---
title: morphologyMinimum()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/morphologyminimum()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/morphologyminimum()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/morphologyminimum%28%29.json'
content_hash: 'sha256:0c9c91897a583e17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# morphologyMinimum()

<sub>Type Method</sub>

Blurs a circular area by reducing contrasting pixels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func morphologyMinimum() -> any CIFilter & CIMorphologyMinimum
```

## Return Value

The blurred image.

## Discussion

This method applies the morphology minimum filter to an image. The effect targets a circular section of the image, calculating the median color values to find colors that make up more than half the working area. Using this calculation, the effect reduces the pixels with contrasting colors to take up less of the working area. The effect is then repeated throughout the image.

The morphology minimum filter uses the following properties:

- **`radius`** — A `float` representing the area of effect as an [NSNumber](../../foundation/nsnumber.md).
- **`inputImage`** — A [CIImage](../ciimage.md) representing the input image to apply the filter to.

The following code creates a filter that adds a blur that adds darkness to the input image:

```swift
    func morphologyMinimum(inputImage: CIImage) -> CIImage? {

        let morphologyMinimumFilter = CIFilter.morphologyMinimum()
        morphologyMinimumFilter.inputImage = inputImage
        morphologyMinimumFilter.radius = 5
        return morphologyMinimumFilter.outputImage
    }
```

![](../../../../attachments/f87f91b3540dad92df7b0c5e58e394f3/media-3544966@2x.png)

<sub>Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear and crisp. In the photo on the right, a morphology minimum blur has been applied, making the image hazy and the edges of the palm trees darker and less distinct.</sub>

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
- [+ morphologyRectangleMaximumFilter](<morphologyrectanglemaximum().md>) — Blurs a rectangular area by enlarging contrasting pixels.
- [+ morphologyRectangleMinimumFilter](<morphologyrectangleminimum().md>) — Blurs a rectangular area by reducing contrasting pixels.
- [+ motionBlurFilter](<motionblur().md>) — Creates motion blur on an image.
- [+ noiseReductionFilter](<noisereduction().md>) — Reduces noise by sharpening the edges of objects.
- [+ zoomBlurFilter](<zoomblur().md>) — Creates a zoom blur centered around a single point on the image.
