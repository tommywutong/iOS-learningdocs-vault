---
title: holeDistortion()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/holedistortion()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/holedistortion()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/holedistortion%28%29.json'
content_hash: 'sha256:172d3b46a4704301'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# holeDistortion()

<sub>Type Method</sub>

Distorts an image with a circular area that pushes the image outward.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func holeDistortion() -> any CIFilter & CIHoleDistortion
```

## Return Value

The distorted image.

## Discussion

This method applies the hole distortion filter to an image. This effect distorts the image by generating a circular area that displaces pixels in the image by pushing them outward from the hole defined by the radius.

The absolute threshold filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`center`** — A set of coordinates marking the center of the image as a [CGPoint](../../corefoundation/cgpoint.md).
- **`radius`** — A `float` representing the amount of pixels the filter uses to create the distortion as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that results in an image becoming distorted from the center outward:

```swift
func holeDistortion(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.holeDistortion()
    filter.inputImage = inputImage
    filter.radius = 300
    filter.center = CGPoint(x: 1791, y: 1344)
    return filter.outputImage!
}
```

![](../../../../attachments/f42bdbd7ac365ff3174e1012e7151701/media-4407309@2x.png)

<sub>Two images next to each other. The image on the left contains a black-and-white checkerboard pattern. The image on the right has the hole distortion filter applied. The center of the image has been replaced by a black circle and the pixels have been pushed out of place and stretched to make room for this.</sub>

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
- [+ lightTunnelFilter](<lighttunnel().md>) — Distorts an image by generating a light tunnel.
- [+ ninePartStretchedFilter](<ninepartstretched().md>) — Distorts an image by stretching it between two breakpoints.
- [+ ninePartTiledFilter](<nineparttiled().md>) — Distorts an image by tiling portions of it.
- [+ pinchDistortionFilter](<pinchdistortion().md>) — Distorts an image by creating a pinch effect with stronger distortion in the center.
- [+ stretchCropFilter](<stretchcrop().md>) — Distorts an image by stretching or cropping to fit a specified size.
- [+ torusLensDistortionFilter](<toruslensdistortion().md>) — Creates a torus-shaped lens to distort the image.
- [+ twirlDistortionFilter](<twirldistortion().md>) — Distorts an image by rotating pixels around a center point.
