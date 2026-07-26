---
title: Reduction Filters
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/reduction-filters
source_url: 'https://developer.apple.com/documentation/coreimage/reduction-filters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/reduction-filters.json'
content_hash: 'sha256:a0169db6793c8dc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# Reduction Filters

<sub>API Collection</sub>

Create statistical information about an image.

## Topics

### Filters

- [+ areaAverageFilter](<cifilter-swift.class/areaaverage().md>) — Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [+ areaHistogramFilter](<cifilter-swift.class/areahistogram().md>) — Returns a histogram of a specified area of the image.
- [+ areaLogarithmicHistogramFilter](<cifilter-swift.class/arealogarithmichistogram().md>) — Returns a logarithmic histogram of a specified area of the image.
- [+ areaMaximumFilter](<cifilter-swift.class/areamaximum().md>) — Calculates the maximum color components of a specified area of the image.
- [+ areaMaximumAlphaFilter](<cifilter-swift.class/areamaximumalpha().md>) — Finds the pixel with the highest alpha value.
- [+ areaMinimumFilter](<cifilter-swift.class/areaminimum().md>) — Calculates the minimum color component values for a specified area of the image.
- [+ areaMinimumAlphaFilter](<cifilter-swift.class/areaminimumalpha().md>) — Calculates the pixel within a specified area that has the smallest alpha value.
- [+ areaMinMaxFilter](<cifilter-swift.class/areaminmax().md>) — Calculates minimum and maximum color components for a specified area of the image.
- [+ areaMinMaxRedFilter](<cifilter-swift.class/areaminmaxred().md>) — Calculates the minimum and maximum red component value.
- [+ columnAverageFilter](<cifilter-swift.class/columnaverage().md>) — Calculates the average color for a specified column of an image.
- [+ histogramDisplayFilter](<cifilter-swift.class/histogramdisplay().md>) — Generates a histogram map from the image.
- [+ KMeansFilter](<cifilter-swift.class/kmeans().md>) — Applies the k-means algorithm to find the most common colors in an image.
- [+ rowAverageFilter](<cifilter-swift.class/rowaverage().md>) — Calculates the average color for the specified row of pixels in an image.

### Protocols

- [CIAreaAverage](ciareaaverage.md)
- [CIAreaHistogram](ciareahistogram.md)
- [CIAreaLogarithmicHistogram](ciarealogarithmichistogram.md)
- [CIAreaMaximum](ciareamaximum.md)
- [CIAreaMaximumAlpha](ciareamaximumalpha.md)
- [CIAreaMinMax](ciareaminmax.md)
- [CIAreaMinMaxRed](ciareaminmaxred.md)
- [CIAreaMinimum](ciareaminimum.md)
- [CIAreaMinimumAlpha](ciareaminimumalpha.md)
- [CIAreaReductionFilter](ciareareductionfilter.md)
- [CIColumnAverage](cicolumnaverage.md)
- [CIHistogramDisplay](cihistogramdisplay.md)
- [CIKMeans](cikmeans.md)
- [CIRowAverage](cirowaverage.md)

## See Also

### Filter Catalog

- [Blur Filters](blur-filters.md) — Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color-adjustment-filters.md) — Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color-effect-filters.md) — Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite-operations.md) — Composite images by using a range of blend modes and compositing operators.
- [Convolution Filters](convolution-filters.md) — Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion-filters.md) — Apply distortion to images.
- [Generator Filters](generator-filters.md) — Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](geometry-adjustment-filters.md) — Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](gradient-filters.md) — Generate linear and radial gradients.
- [Halftone Effect Filters](halftone-effect-filters.md) — Simulate monochrome and CMYK halftone screens.
- [Sharpening Filters](sharpening-filters.md) — Apply sharpening to images.
- [Stylizing Filters](stylizing-filters.md) — Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile-effect-filters.md) — Produce tiled images from source images.
- [Transition Filters](transition-filters.md) — Transition between two images by using effects including page curl and swipe.
