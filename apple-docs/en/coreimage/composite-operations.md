---
title: Composite Operations
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/composite-operations
source_url: 'https://developer.apple.com/documentation/coreimage/composite-operations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/composite-operations.json'
content_hash: 'sha256:11d003544d065cb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# Composite Operations

<sub>API Collection</sub>

Composite images by using a range of blend modes and compositing operators.

## Topics

### Filters

- [+ additionCompositingFilter](<cifilter-swift.class/additioncompositing().md>) — Blends colors from two images by addition.
- [+ colorBlendModeFilter](<cifilter-swift.class/colorblendmode().md>) — Blends color from two images using the luminance values from the background image and the hue and saturation values from the input image.
- [+ colorBurnBlendModeFilter](<cifilter-swift.class/colorburnblendmode().md>) — Blends color from two images while darkening the image.
- [+ colorDodgeBlendModeFilter](<cifilter-swift.class/colordodgeblendmode().md>) — Blends color from two images using dodging.
- [+ darkenBlendModeFilter](<cifilter-swift.class/darkenblendmode().md>) — Blends colors from two images while darkening lighter pixels.
- [+ differenceBlendModeFilter](<cifilter-swift.class/differenceblendmode().md>) — Subtracts color values to blend colors.
- [+ divideBlendModeFilter](<cifilter-swift.class/divideblendmode().md>) — Divides color values to blend colors.
- [+ exclusionBlendModeFilter](<cifilter-swift.class/exclusionblendmode().md>) — Subtracts color values to blend colors with less contrast.
- [+ hardLightBlendModeFilter](<cifilter-swift.class/hardlightblendmode().md>) — Blends colors of two images by screening and multiplying.
- [+ hueBlendModeFilter](<cifilter-swift.class/hueblendmode().md>) — Blends colors of two images by computing the sum of image color values.
- [+ lightenBlendModeFilter](<cifilter-swift.class/lightenblendmode().md>) — Blends colors from two images by brightening colors.
- [+ linearBurnBlendModeFilter](<cifilter-swift.class/linearburnblendmode().md>) — Blends color from two images while increasing contrast.
- [+ linearDodgeBlendModeFilter](<cifilter-swift.class/lineardodgeblendmode().md>) — Blends colors of two images with dodging.
- [+ linearLightBlendModeFilter](<cifilter-swift.class/linearlightblendmode().md>) — A combination of linear burn and linear dodge blend modes.
- [+ luminosityBlendModeFilter](<cifilter-swift.class/luminosityblendmode().md>) — Blends color from two images by calculating the color, hue, and saturation.
- [+ minimumCompositingFilter](<cifilter-swift.class/minimumcompositing().md>) — Blends colors from two images by computing minimum values.
- [+ maximumCompositingFilter](<cifilter-swift.class/maximumcompositing().md>) — Applies a maximum compositing filter to an image.
- [+ multiplyBlendModeFilter](<cifilter-swift.class/multiplyblendmode().md>) — Blends colors from two images by multiplying color components.
- [+ multiplyCompositingFilter](<cifilter-swift.class/multiplycompositing().md>) — Blurs the colors of two images by multiplying color components.
- [+ overlayBlendModeFilter](<cifilter-swift.class/overlayblendmode().md>) — Blends colors by overlaying images.
- [+ pinLightBlendModeFilter](<cifilter-swift.class/pinlightblendmode().md>) — Blends colors of two images by replacing brighter colors.
- [+ saturationBlendModeFilter](<cifilter-swift.class/saturationblendmode().md>) — Blends the colors and saturation values of two images.
- [+ screenBlendModeFilter](<cifilter-swift.class/screenblendmode().md>) — Blends colors of two images by multiplying colors.
- [+ softLightBlendModeFilter](<cifilter-swift.class/softlightblendmode().md>) — Blurs the colors of two images by calculating luminance.
- [+ sourceAtopCompositingFilter](<cifilter-swift.class/sourceatopcompositing().md>) — Overlaps two images to create one cropped image.
- [+ sourceInCompositingFilter](<cifilter-swift.class/sourceincompositing().md>) — Subtracts non-overlapping areas of two images, resulting in one image.
- [+ sourceOutCompositingFilter](<cifilter-swift.class/sourceoutcompositing().md>) — Subtracts overlapping area of two images to create the output image.
- [+ sourceOverCompositingFilter](<cifilter-swift.class/sourceovercompositing().md>) — Places one image over a second image.
- [+ subtractBlendModeFilter](<cifilter-swift.class/subtractblendmode().md>) — Blends colors by subtracting color values from two images.
- [+ vividLightBlendModeFilter](<cifilter-swift.class/vividlightblendmode().md>) — A combination of color-burn and color-dodge blend modes.

### Protocols

- [CICompositeOperation](cicompositeoperation.md) — The properties you use to configure a composite operation filter.

## See Also

### Filter Catalog

- [Blur Filters](blur-filters.md) — Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color-adjustment-filters.md) — Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color-effect-filters.md) — Apply color effects, including photo effects, dithering, and color maps.
- [Convolution Filters](convolution-filters.md) — Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion-filters.md) — Apply distortion to images.
- [Generator Filters](generator-filters.md) — Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](geometry-adjustment-filters.md) — Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](gradient-filters.md) — Generate linear and radial gradients.
- [Halftone Effect Filters](halftone-effect-filters.md) — Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](reduction-filters.md) — Create statistical information about an image.
- [Sharpening Filters](sharpening-filters.md) — Apply sharpening to images.
- [Stylizing Filters](stylizing-filters.md) — Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile-effect-filters.md) — Produce tiled images from source images.
- [Transition Filters](transition-filters.md) — Transition between two images by using effects including page curl and swipe.
