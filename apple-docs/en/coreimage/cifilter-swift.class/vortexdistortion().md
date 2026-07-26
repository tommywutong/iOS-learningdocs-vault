---
title: vortexDistortion()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/vortexdistortion()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/vortexdistortion()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/vortexdistortion%28%29.json'
content_hash: 'sha256:c981dc9086d22b33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# vortexDistortion()

<sub>Type Method</sub>

Distorts an image by using a vortex effect created by rotating pixels around a point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func vortexDistortion() -> any CIFilter & CIVortexDistortion
```

## Return Value

The distorted image.

## Discussion

This method applies the vortex distortion filter to an image. This effect distorts an image by rotating pixels around the defined center to simulate a vortex. You can specify the number of rotations to control the strength of the effect.

The vortex distortion filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`angle`** — A `float` representing the angle of the vortex, in radians, as an [NSNumber](../../foundation/nsnumber.md).
- **`center`** — A set of coordinates marking the center of the image as a [CGPoint](../../corefoundation/cgpoint.md).
- **`radius`** — A `float` representing the amount of pixels the filter uses to create the distortion as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that results in a small vortex effect:

```swift
func vortexDistort(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.vortexDistortion()
    filter.inputImage = inputImage
    filter.radius = 700
    filter.angle = 56.54866776461628
    filter.center = CGPoint(x: 1124, y: 778)
    return filter.outputImage!
}
```

![](../../../../attachments/932220d9af42464e22c6af5e828fddc4/media-4407301@2x.png)

<sub>Two images next to each other. The image on the left contains a black-and-white checkerboard pattern. The image on the right has the vortex distortion filter applied. The center of the image appears to be tightly twisted with the amount of twist decreasing very quickly towards the edge of the image.</sub>

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
- [+ ninePartStretchedFilter](<ninepartstretched().md>) — Distorts an image by stretching it between two breakpoints.
- [+ ninePartTiledFilter](<nineparttiled().md>) — Distorts an image by tiling portions of it.
- [+ pinchDistortionFilter](<pinchdistortion().md>) — Distorts an image by creating a pinch effect with stronger distortion in the center.
- [+ stretchCropFilter](<stretchcrop().md>) — Distorts an image by stretching or cropping to fit a specified size.
- [+ torusLensDistortionFilter](<toruslensdistortion().md>) — Creates a torus-shaped lens to distort the image.
