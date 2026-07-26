---
title: Geometry Adjustment Filters
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/geometry-adjustment-filters
source_url: 'https://developer.apple.com/documentation/coreimage/geometry-adjustment-filters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/geometry-adjustment-filters.json'
content_hash: 'sha256:fedfb02eeccc8613'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# Geometry Adjustment Filters

<sub>API Collection</sub>

Translate, scale, and rotate images in 2D and 3D.

## Topics

### Filters

- [+ bicubicScaleTransformFilter](<cifilter-swift.class/bicubicscaletransform().md>) — Produces a high-quality scaled version of an image.
- [+ edgePreserveUpsampleFilter](<cifilter-swift.class/edgepreserveupsample().md>) — Creates a high-quality upscaled image.
- [+ keystoneCorrectionCombinedFilter](<cifilter-swift.class/keystonecorrectioncombined().md>) — Adjusts the image vertically and horizontally to remove distortion.
- [+ keystoneCorrectionHorizontalFilter](<cifilter-swift.class/keystonecorrectionhorizontal().md>) — Horizontally adjusts an image to remove distortion.
- [+ keystoneCorrectionVerticalFilter](<cifilter-swift.class/keystonecorrectionvertical().md>) — Vertically adjusts an image to remove distortion.
- [+ lanczosScaleTransformFilter](<cifilter-swift.class/lanczosscaletransform().md>) — Creates a high-quality, scaled version of a source image.
- [+ perspectiveCorrectionFilter](<cifilter-swift.class/perspectivecorrection().md>) — Transforms an image’s perspective.
- [+ perspectiveRotateFilter](<cifilter-swift.class/perspectiverotate().md>) — Rotates an image in a 3D space.
- [+ perspectiveTransformFilter](<cifilter-swift.class/perspectivetransform().md>) — Alters an image’s geometry to adjust the perspective.
- [+ perspectiveTransformWithExtentFilter](<cifilter-swift.class/perspectivetransformwithextent().md>) — Alters an image’s geometry to adjust the perspective while applying constraints.
- [+ straightenFilter](<cifilter-swift.class/straighten().md>) — Rotates and crops an image.

### Protocols

- [CIBicubicScaleTransform](cibicubicscaletransform.md) — The properties you use to configure a bicubic scale transform filter.
- [CIEdgePreserveUpsample](ciedgepreserveupsample.md) — The properties you use to configure an edge preserve upsample filter.
- [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md) — The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md) — The properties you use to configure a keystone correction combined filter.
- [CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md) — The properties you use to configure a keystone correction horizontal filter.
- [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md) — The properties you use to configure a keystone correction vertical filter.
- [CILanczosScaleTransform](cilanczosscaletransform.md) — The properties you use to configure a Lanczos scale transform filter.
- [CIPerspectiveCorrection](ciperspectivecorrection.md) — The properties you use to configure a perspective correction filter.
- [CIPerspectiveRotate](ciperspectiverotate.md) — The properties you use to configure a perspective rotate filter.
- [CIPerspectiveTransform](ciperspectivetransform.md) — The properties you use to configure a perspective transform filter.
- [CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md) — The properties you use to configure a perspective transform with extent filter.
- [CIStraighten](cistraighten.md) — The properties you use to configure a straighten filter.

## See Also

### Filter Catalog

- [Blur Filters](blur-filters.md) — Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color-adjustment-filters.md) — Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color-effect-filters.md) — Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite-operations.md) — Composite images by using a range of blend modes and compositing operators.
- [Convolution Filters](convolution-filters.md) — Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion-filters.md) — Apply distortion to images.
- [Generator Filters](generator-filters.md) — Generate barcode, geometric, and special-effect images.
- [Gradient Filters](gradient-filters.md) — Generate linear and radial gradients.
- [Halftone Effect Filters](halftone-effect-filters.md) — Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](reduction-filters.md) — Create statistical information about an image.
- [Sharpening Filters](sharpening-filters.md) — Apply sharpening to images.
- [Stylizing Filters](stylizing-filters.md) — Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile-effect-filters.md) — Produce tiled images from source images.
- [Transition Filters](transition-filters.md) — Transition between two images by using effects including page curl and swipe.
