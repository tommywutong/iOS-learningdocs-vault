---
title: kCICategoryDistortionEffect
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/kcicategorydistortioneffect
source_url: 'https://developer.apple.com/documentation/coreimage/kcicategorydistortioneffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/kcicategorydistortioneffect.json'
content_hash: 'sha256:ec32264d84cc52b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# kCICategoryDistortionEffect

<sub>Global Variable</sub>

A filter that reshapes an image by altering its geometry to create a 3D effect. Using distortion filters, you can displace portions of an image, apply lens effects, make a bulge in an image, and perform other operation to achieve an artistic effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCICategoryDistortionEffect: String
```

## See Also

### Constants

- [kCICategoryGeometryAdjustment](kcicategorygeometryadjustment.md) — A filter  that changes the geometry of an image. Some of these filters are used to warp an image to achieve an artistic effects, but these filters can also be used to correct problems in the source image. For example, you can apply an affine transform to straighten an image that is rotated with respect to the horizon.
- [kCICategoryCompositeOperation](kcicategorycompositeoperation.md) — A filter  operates on two image sources, using the color values of one image to operate on the other. Composite filters perform computations such as computing maximum values, minimum values, and multiplying values between input images. You can use compositing filters to add effects to an image, crop an image, and achieve a variety of other effects.
- [kCICategoryHalftoneEffect](kcicategoryhalftoneeffect.md) — A filter  that simulates a variety of halftone screens, to mimic the halftone process used in print media. The output of these filters has the familiar “newspaper” look of the various dot patterns. Filters are typically  named after the pattern created by the virtual halftone screen, such as circular screen or hatched screen.
- [kCICategoryColorAdjustment](kcicategorycoloradjustment.md) — The category for color adjustment filters.
- [kCICategoryColorEffect](kcicategorycoloreffect.md) — A filter  that modifies the color of an image to achieve an artistic effect. Examples of color effect filters include filters that change a color image to a sepia image or a monochrome image or that produces such effects as posterizing.
- [kCICategoryTransition](kcicategorytransition.md) — A filter  that provides a bridge between two or more images by applying a motion effect that defines how the pixels of a source image yield to that of the destination image.
- [kCICategoryTileEffect](kcicategorytileeffect.md) — A filter that typically applies an effect to an image and then create smaller versions of the image (tiles), which are then laid out to create a pattern that’s infinite in extent.
- [kCICategoryGenerator](kcicategorygenerator.md) — A filter that generates a pattern, such as a solid color, a checkerboard, or a star shine. The generated output is typically used as input to another filter.
- [kCICategoryReduction](kcicategoryreduction.md) — A filter that reduces image data. These filters are used to solve image analysis problems.
- [kCICategoryGradient](kcicategorygradient.md) — A filter that generates a fill whose color varies smoothly. Exactly how color varies depends on the type of gradient—linear, radial, or Gaussian.
- [kCICategoryStylize](kcicategorystylize.md) — A filter  that makes a photographic image look as if it was painted or sketched. These filters are typically used alone or in combination with other filters to achieve artistic effects.
- [kCICategorySharpen](kcicategorysharpen.md) — A filter  that sharpens images, increasing the contrast between the edges in an image. Examples of sharpen filters are unsharp mask and sharpen luminance.
- [kCICategoryBlur](kcicategoryblur.md) — A filter  that softens images, decreasing the contrast  between the edges in an image. Examples of blur filters are Gaussian blur and zoom blur.
- [kCICategoryVideo](kcicategoryvideo.md) — A filter that works on video images.
- [kCICategoryStillImage](kcicategorystillimage.md) — A filter  that works on still images.
