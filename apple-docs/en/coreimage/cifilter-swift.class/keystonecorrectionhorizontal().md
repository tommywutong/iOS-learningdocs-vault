---
title: keystoneCorrectionHorizontal()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/keystonecorrectionhorizontal()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/keystonecorrectionhorizontal()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/keystonecorrectionhorizontal%28%29.json'
content_hash: 'sha256:196d17cb4c0c23f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# keystoneCorrectionHorizontal()

<sub>Type Method</sub>

Horizontally adjusts an image to remove distortion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func keystoneCorrectionHorizontal() -> any CIFilter & CIKeystoneCorrectionHorizontal
```

## Return Value

The adjusted image.

## Discussion

This method applies the keystone correction horizontal filter to an image. The effect applies a set of horizontal guides and simulated focal length to adjust the shape of the input image. This effect is commonly used when cropping an image to correct distortion. In the figure below, both vertical and horizontal adjustments are made, resulting in a trapezoid-shaped image.

The keystone correction horizontal filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`topLeft`** — A [CGPoint](../../corefoundation/cgpoint.md) in the input image mapped to the top-left corner of the output image.
- **`topRight`** — A [CGPoint](../../corefoundation/cgpoint.md) in the input image mapped to the top-right corner of the output image.
- **`bottomLeft`** — A [CGPoint](../../corefoundation/cgpoint.md) in the input image mapped to the bottom-left corner of the output image.
- **`bottomRight`** — A [CGPoint](../../corefoundation/cgpoint.md) in the input image mapped to the bottom-right corner of the output image.
- **`focalLength`** — A `float` representing the simulated focal length as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that distorts the image:

```swift
func keystoneCorrectionHorizontal(inputImage: CIImage) -> CIImage {    
    let keystoneCorrect = CIFilter.keystoneCorrectionHorizontal()
    keystoneCorrect.inputImage = inputImage
    keystoneCorrect.topLeft = CGPoint(x: 0, y: 2448)
    keystoneCorrect.topRight = CGPoint(x: 3264, y: 2248)
    keystoneCorrect.bottomLeft = CGPoint(x: 400, y: 0)
    keystoneCorrect.bottomRight = CGPoint(x: 3264, y: 150)
    keystoneCorrect.focalLength = 18
    return keystoneCorrect.outputImage!
}
```

![](../../../../attachments/b9b358c37e1ea6c948cc48dbdf1945f3/media-3582230@2x.png)

<sub>Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a horizontal keystone correction filter is applied, distorting the rectangular image so the left edge is smaller than the right edge.</sub>

## See Also

### Filters

- [+ bicubicScaleTransformFilter](<bicubicscaletransform().md>) — Produces a high-quality scaled version of an image.
- [+ edgePreserveUpsampleFilter](<edgepreserveupsample().md>) — Creates a high-quality upscaled image.
- [+ keystoneCorrectionCombinedFilter](<keystonecorrectioncombined().md>) — Adjusts the image vertically and horizontally to remove distortion.
- [+ keystoneCorrectionVerticalFilter](<keystonecorrectionvertical().md>) — Vertically adjusts an image to remove distortion.
- [+ lanczosScaleTransformFilter](<lanczosscaletransform().md>) — Creates a high-quality, scaled version of a source image.
- [+ perspectiveCorrectionFilter](<perspectivecorrection().md>) — Transforms an image’s perspective.
- [+ perspectiveRotateFilter](<perspectiverotate().md>) — Rotates an image in a 3D space.
- [+ perspectiveTransformFilter](<perspectivetransform().md>) — Alters an image’s geometry to adjust the perspective.
- [+ perspectiveTransformWithExtentFilter](<perspectivetransformwithextent().md>) — Alters an image’s geometry to adjust the perspective while applying constraints.
- [+ straightenFilter](<straighten().md>) — Rotates and crops an image.
