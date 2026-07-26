---
title: ninePartStretched()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/ninepartstretched()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/ninepartstretched()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/ninepartstretched%28%29.json'
content_hash: 'sha256:9f674964b84e7ea8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# ninePartStretched()

<sub>Type Method</sub>

Distorts an image by stretching it between two breakpoints.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func ninePartStretched() -> any CIFilter & CINinePartStretched
```

## Return Value

The distorted image.

## Discussion

This method applies the nine-part stretched filter to an image. This effect distorts an image by stretching an image to the breakpoint properties while distorting the image based on the grow amount.

The nine-part stretched filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`growAmount`** — A [CGPoint](../../corefoundation/cgpoint.md) representing the amount of stretching applied.
- **`breakpoint0`** — A [CGPoint](../../corefoundation/cgpoint.md) representing the lower-left corner of the image to retain before stretching begins.
- **`breakpoint1`** — A [CGPoint](../../corefoundation/cgpoint.md) representing the upper-right corner of the image to retain after stretching ends.

The following code creates a filter that results in a significantly warped image:

```swift
func ninePartStretch(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.ninePartStretched()
    filter.inputImage = inputImage
    filter.setDefaults()
    filter.breakpoint0 = CGPoint(x: 200, y: 200)
    filter.breakpoint1 = CGPoint(x: inputImage.extent.size.width-200, y: inputImage.extent.size.height - 200)
    filter.growAmount = CGPoint(x: 500, y: 500)
    return filter.outputImage!
}
```

![](../../../../attachments/1c46d64e7f107e3d4cadd6f729e972b0/media-4407340@2x.png)

<sub>Two images arranged horizontally. The left image contains a photograph of three hydrangea flowers with dark leaves in the background. An area inset by 200 pixels from all sides is highlighted using a rectangle. The image on the right shows the result of applying the nine part stretched filter. The area within the red rectangle has been stretched making the image larger. The areas outside of the rectangle have been warped to match the stretched area.</sub>

## See Also

### Filters

- [+ bumpDistortionFilter](<bumpdistortion().md>) — Distorts an image with a concave or convex bump.
- [+ bumpDistortionLinearFilter](<bumpdistortionlinear().md>) — Linearly distorts an image with a concave or convex bump.
- [+ circleSplashDistortionFilter](<circlesplashdistortion().md>) — Distorts an image with radiating circles to the periphery of the image.
- [+ circularWrapFilter](<circularwrap().md>) — Distorts an image by increasing the distance of the center of the image.
- [+ displacementDistortionFilter](<displacementdistortion().md>) — Applies the grayscale values of the second image to the first image.
- [+ drosteFilter](<droste().md>) — Stylizes an image with the Droste effect.
- [+ glassDistortionFilter](<glassdistortion().md>) — Distorts an image by applying a glass-like texture.
- [+ glassLozengeFilter](<glasslozenge().md>) — Creates a lozenge-shaped lens and distorts the image.
- [+ holeDistortionFilter](<holedistortion().md>) — Distorts an image with a circular area that pushes the image outward.
- [+ lightTunnelFilter](<lighttunnel().md>) — Distorts an image by generating a light tunnel.
- [+ ninePartTiledFilter](<nineparttiled().md>) — Distorts an image by tiling portions of it.
- [+ pinchDistortionFilter](<pinchdistortion().md>) — Distorts an image by creating a pinch effect with stronger distortion in the center.
- [+ stretchCropFilter](<stretchcrop().md>) — Distorts an image by stretching or cropping to fit a specified size.
- [+ torusLensDistortionFilter](<toruslensdistortion().md>) — Creates a torus-shaped lens to distort the image.
- [+ twirlDistortionFilter](<twirldistortion().md>) — Distorts an image by rotating pixels around a center point.
