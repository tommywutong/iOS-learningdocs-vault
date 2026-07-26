---
title: boxBlur()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/boxblur()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/boxblur()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/boxblur%28%29.json'
content_hash: 'sha256:f86b27efb760b979'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# boxBlur()

<sub>Type Method</sub>

Applies a square-shaped blur to an area of an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func boxBlur() -> any CIFilter & CIBoxBlur
```

## Return Value

The blurred image.

## Discussion

This method applies the box blur filter to an image. The effect targets a square area and calculates the median color value of the pixels to create the output image. The `radius` is the width of a square area with a larger area, resulting in a stronger blur effect on the output image.

The box blur filter uses the following properties:

- **`radius`** — A `float` representing the area of effect as a [NSNumber](../../foundation/nsnumber.md).
- **`inputImage`** — A [CIImage](../ciimage.md) representing the input image to apply the filter to.

The following code creates a filter that results in less detail in the input image:

```swift
    func boxBlur(inputImage: CIImage) -> CIImage? {

        let boxBlurFilter = CIFilter.boxBlur()
        boxBlurFilter.inputImage = inputImage
        boxBlurFilter.radius = 10
        return boxBlurFilter.outputImage
    }
```

![](../../../../attachments/a4415b346213b41113657f0b0d8a9c7f/media-3544956@2x.png)

<sub>Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear and crisp. In the photo on the right, a box blur filter has been applied, resulting in an image with slightly less detail.</sub>

## See Also

### Filters

- [+ bokehBlurFilter](<bokehblur().md>) — Applies a bokeh effect to an image.
- [+ discBlurFilter](<discblur().md>) — Applies a circle-shaped blur to an area of an image.
- [+ gaussianBlurFilter](<gaussianblur().md>) — Blurs an image with a Gaussian distribution pattern.
- [+ maskedVariableBlurFilter](<maskedvariableblur().md>) — Blurs a specified portion of an image.
- [+ medianFilter](<median().md>) — Calculates the median of an image to refine detail.
- [+ morphologyGradientFilter](<morphologygradient().md>) — Detects and highlights edges of objects.
- [+ morphologyMaximumFilter](<morphologymaximum().md>) — Blurs a circular area by enlarging contrasting pixels.
- [+ morphologyMinimumFilter](<morphologyminimum().md>) — Blurs a circular area by reducing contrasting pixels.
- [+ morphologyRectangleMaximumFilter](<morphologyrectanglemaximum().md>) — Blurs a rectangular area by enlarging contrasting pixels.
- [+ morphologyRectangleMinimumFilter](<morphologyrectangleminimum().md>) — Blurs a rectangular area by reducing contrasting pixels.
- [+ motionBlurFilter](<motionblur().md>) — Creates motion blur on an image.
- [+ noiseReductionFilter](<noisereduction().md>) — Reduces noise by sharpening the edges of objects.
- [+ zoomBlurFilter](<zoomblur().md>) — Creates a zoom blur centered around a single point on the image.
