---
title: circleSplashDistortion()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/circlesplashdistortion()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/circlesplashdistortion()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/circlesplashdistortion%28%29.json'
content_hash: 'sha256:8c01b626d3f9835e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# circleSplashDistortion()

<sub>Type Method</sub>

Distorts an image with radiating circles to the periphery of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func circleSplashDistortion() -> any CIFilter & CICircleSplashDistortion
```

## Return Value

The distorted image.

## Discussion

This method applies the circle splash distortion filter to an image. This effect distorts the pixels starting at the circumference of a circle and emanating outward.

The circle splash distortion filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`radius`** — A `float` representing the amount in pixels the filter uses to create the distortion as an [NSNumber](../../foundation/nsnumber.md).
- **`center`** — A [CGPoint](../../corefoundation/cgpoint.md) representing the center of the image.

The following code creates a filter that results in a ripple effect applied to the image:

```swift
func circularSplash(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.circleSplashDistortion()
    filter.inputImage = inputImage
    filter.center = CGPoint(x: 50.0, y: 50.0)
    filter.radius = 2.0
    return filter.outputImage!
}
```

![](../../../../attachments/a1a41d94e5b1e030ee121ab50708ac7c/media-4407306@2x.png)

<sub>On the left, an image with a checkerboard pattern. On the right, the same image but with a circle splash distortion applied. The center of the image contains a checkerboard pattern with larger squares than the original. This is surrounded by stretched black and white stripes radiating out to the edge of the image.</sub>

## See Also

### Filters

- [+ bumpDistortionFilter](<bumpdistortion().md>) — Distorts an image with a concave or convex bump.
- [+ bumpDistortionLinearFilter](<bumpdistortionlinear().md>) — Linearly distorts an image with a concave or convex bump.
- [+ circularWrapFilter](<circularwrap().md>) — Distorts an image by increasing the distance of the center of the image.
- [+ displacementDistortionFilter](<displacementdistortion().md>) — Applies the grayscale values of the second image to the first image.
- [+ drosteFilter](<droste().md>) — Stylizes an image with the Droste effect.
- [+ glassDistortionFilter](<glassdistortion().md>) — Distorts an image by applying a glass-like texture.
- [+ glassLozengeFilter](<glasslozenge().md>) — Creates a lozenge-shaped lens and distorts the image.
- [+ holeDistortionFilter](<holedistortion().md>) — Distorts an image with a circular area that pushes the image outward.
- [+ lightTunnelFilter](<lighttunnel().md>) — Distorts an image by generating a light tunnel.
- [+ ninePartStretchedFilter](<ninepartstretched().md>) — Distorts an image by stretching it between two breakpoints.
- [+ ninePartTiledFilter](<nineparttiled().md>) — Distorts an image by tiling portions of it.
- [+ pinchDistortionFilter](<pinchdistortion().md>) — Distorts an image by creating a pinch effect with stronger distortion in the center.
- [+ stretchCropFilter](<stretchcrop().md>) — Distorts an image by stretching or cropping to fit a specified size.
- [+ torusLensDistortionFilter](<toruslensdistortion().md>) — Creates a torus-shaped lens to distort the image.
- [+ twirlDistortionFilter](<twirldistortion().md>) — Distorts an image by rotating pixels around a center point.
