---
title: saliencyMap()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/saliencymap()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/saliencymap()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/saliencymap%28%29.json'
content_hash: 'sha256:fe5f70a3e585efd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# saliencyMap()

<sub>Type Method</sub>

Creates a saliency map from an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func saliencyMap() -> any CIFilter & CISaliencyMap
```

## Return Value

The modified image.

## Discussion

This method applies the saliency map filter to an image. The effect generates a saliency map representation of the input image.

The saliency map filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).

The following code creates a filter that produces an image that’s easier for computers to analyze:

```swift
func saliencyMap(inputImage: CIImage) -> CIImage {
    let saliencyMapFilter = CIFilter.saliencyMap()
    saliencyMapFilter.inputImage = inputImage
    return saliencyMapFilter.outputImage!
}
```

![](../../../../attachments/0dbd0da7daa97279ebedb5cf5a2bf419/media-3624695@2x.png)

<sub>Two photographs of multiple sets of small purple flowers surrounded by other flowers. The photo on the left is clear and crisp. In the photo on the right, a saliency map filter is applied and the image is transformed to a black image with red highlighting the area of the flower.</sub>

## See Also

### Filters

- [+ blendWithAlphaMaskFilter](<blendwithalphamask().md>) — Blends two images by using an alpha mask image.
- [+ blendWithBlueMaskFilter](<blendwithbluemask().md>) — Blends two images by using a blue mask image.
- [+ blendWithMaskFilter](<blendwithmask().md>) — Blends two images by using a mask image.
- [+ blendWithRedMaskFilter](<blendwithredmask().md>) — Blends two images by using a red mask image.
- [+ bloomFilter](<bloom().md>) — Adjusts an image’s colors by applying a blur effect.
- [+ cannyEdgeDetectorFilter](<cannyedgedetector().md>) — Applies the Canny edge-detection algorithm to an image.
- [+ comicEffectFilter](<comiceffect().md>) — Creates an image with a comic book effect.
- [+ coreMLModelFilter](<coremlmodel().md>) — Filters an image with a Core ML model.
- [+ crystallizeFilter](<crystallize().md>) — Creates an image made with a series of colorful polygons.
- [+ depthOfFieldFilter](<depthoffield().md>) — Simulates a depth of field effect.
- [+ edgesFilter](<edges().md>) — Hilghlights edges of objects found within an image.
- [+ edgeWorkFilter](<edgework().md>) — Produces a black-and-white image that looks similar to a woodblock print.
- [+ gaborGradientsFilter](<gaborgradients().md>) — Highlights textures in an image.
- [+ gloomFilter](<gloom().md>) — Adjusts an image’s color by applying a gloom filter.
- [+ heightFieldFromMaskFilter](<heightfieldfrommask().md>) — Creates a realistic shaded height-field image.
