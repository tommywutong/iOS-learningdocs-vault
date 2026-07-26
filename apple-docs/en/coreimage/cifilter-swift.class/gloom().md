---
title: gloom()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/gloom()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/gloom()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/gloom%28%29.json'
content_hash: 'sha256:ef72fd1ac97d68e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# gloom()

<sub>Type Method</sub>

Adjusts an image’s color by applying a gloom filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func gloom() -> any CIFilter & CIGloom
```

## Return Value

The modified image.

## Discussion

This method applies the gloom filter to an image. The effect reduces the highlights of the image resulting in the image looking dull.

The gloom filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **radius** — A `float` representing the area of effect as an [NSNumber](../../foundation/nsnumber.md).
- **intensity** — A `float` representing the desired strength of the effect as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that results in a darker image with a slight blur:

```swift
func gloom(inputImage: CIImage) -> CIImage {
    let gloomFilter = CIFilter.gloom()
    gloomFilter.inputImage = inputImage
    gloomFilter.radius = 3
    gloomFilter.intensity = 10
    return gloomFilter.outputImage!
}
```

![](../../../../attachments/fb89b34e882c8f37021b83d391b4358a/media-3599998@2x.png)

<sub>Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close up, in focus, with good light and no effects. In the photo on the right, the gloom filter is applied, resulting in the foliage in the background becoming darker and the image having a slight blur.</sub>

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
- [+ heightFieldFromMaskFilter](<heightfieldfrommask().md>) — Creates a realistic shaded height-field image.
- [+ hexagonalPixellateFilter](<hexagonalpixellate().md>) — Creates an image made of a series of colorful hexagons.
