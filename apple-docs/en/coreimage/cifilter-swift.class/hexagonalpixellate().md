---
title: hexagonalPixellate()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/hexagonalpixellate()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/hexagonalpixellate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/hexagonalpixellate%28%29.json'
content_hash: 'sha256:7621c3781a014463'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# hexagonalPixellate()

<sub>Type Method</sub>

Creates an image made of a series of colorful hexagons.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func hexagonalPixellate() -> any CIFilter & CIHexagonalPixellate
```

## Return Value

The modified image.

## Discussion

This method applies the hexagonal pixelate filter to an image. The effect creates an image containing colored hexagons.

The hexagonal pixelate filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`center`** — A set of coordinates marking the center of the image as a [CGPoint](../../corefoundation/cgpoint.md).
- **`scale`** — A `float` representing the scale of the hexagons as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that results in an image made up of hexagons:

```swift
func hexagonalPixelate (inputImage: CIImage) -> CIImage {
    let hexagonalPixelateFilter = CIFilter.hexagonalPixellate()
    hexagonalPixelateFilter.inputImage = inputImage
    hexagonalPixelateFilter.center = CGPoint(x: 2016, y: 1512)
    hexagonalPixelateFilter.scale = 50
    return hexagonalPixelateFilter.outputImage!
}
```

![](../../../../attachments/5d2144f62d3ccb693aba751a6535a547/media-3600003@2x.png)

<sub>Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close up, in focus, with good light and no effects. In the photo on the right, the hexagonal pixelate filter is applied, resulting in a distorted image made of hexagons with less detail visible.</sub>

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
