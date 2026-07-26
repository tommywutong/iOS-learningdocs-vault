---
title: Stylizing Filters
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/stylizing-filters
source_url: 'https://developer.apple.com/documentation/coreimage/stylizing-filters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/stylizing-filters.json'
content_hash: 'sha256:5d177bf90ff4b496'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# Stylizing Filters

<sub>API Collection</sub>

Create stylized versions of images by applying effects including pixelation and line overlays.

## Topics

### Filters

- [+ blendWithAlphaMaskFilter](<cifilter-swift.class/blendwithalphamask().md>) — Blends two images by using an alpha mask image.
- [+ blendWithBlueMaskFilter](<cifilter-swift.class/blendwithbluemask().md>) — Blends two images by using a blue mask image.
- [+ blendWithMaskFilter](<cifilter-swift.class/blendwithmask().md>) — Blends two images by using a mask image.
- [+ blendWithRedMaskFilter](<cifilter-swift.class/blendwithredmask().md>) — Blends two images by using a red mask image.
- [+ bloomFilter](<cifilter-swift.class/bloom().md>) — Adjusts an image’s colors by applying a blur effect.
- [+ cannyEdgeDetectorFilter](<cifilter-swift.class/cannyedgedetector().md>) — Applies the Canny edge-detection algorithm to an image.
- [+ comicEffectFilter](<cifilter-swift.class/comiceffect().md>) — Creates an image with a comic book effect.
- [+ coreMLModelFilter](<cifilter-swift.class/coremlmodel().md>) — Filters an image with a Core ML model.
- [+ crystallizeFilter](<cifilter-swift.class/crystallize().md>) — Creates an image made with a series of colorful polygons.
- [+ depthOfFieldFilter](<cifilter-swift.class/depthoffield().md>) — Simulates a depth of field effect.
- [+ edgesFilter](<cifilter-swift.class/edges().md>) — Hilghlights edges of objects found within an image.
- [+ edgeWorkFilter](<cifilter-swift.class/edgework().md>) — Produces a black-and-white image that looks similar to a woodblock print.
- [+ gaborGradientsFilter](<cifilter-swift.class/gaborgradients().md>) — Highlights textures in an image.
- [+ gloomFilter](<cifilter-swift.class/gloom().md>) — Adjusts an image’s color by applying a gloom filter.
- [+ heightFieldFromMaskFilter](<cifilter-swift.class/heightfieldfrommask().md>) — Creates a realistic shaded height-field image.
- [+ hexagonalPixellateFilter](<cifilter-swift.class/hexagonalpixellate().md>) — Creates an image made of a series of colorful hexagons.
- [+ highlightShadowAdjustFilter](<cifilter-swift.class/highlightshadowadjust().md>) — Adjusts the highlights of colors to reduce shadows.
- [+ lineOverlayFilter](<cifilter-swift.class/lineoverlay().md>) — Creates an image that resembles a sketch of the outlines of objects.
- [+ mixFilter](<cifilter-swift.class/mix().md>) — Blends two images together.
- [+ personSegmentationFilter](<cifilter-swift.class/personsegmentation().md>) — Creates a mask where red pixels indicate areas of the image that are likely to contain a person.
- [+ pixellateFilter](<cifilter-swift.class/pixellate().md>) — Enlarges the colors of the pixels to create a blurred effect.
- [+ pointillizeFilter](<cifilter-swift.class/pointillize().md>) — Applies a pointillize effect to an image.
- [+ saliencyMapFilter](<cifilter-swift.class/saliencymap().md>) — Creates a saliency map from an image.
- [+ shadedMaterialFilter](<cifilter-swift.class/shadedmaterial().md>) — Creates a shaded image from a height-field image.
- [+ sobelGradientsFilter](<cifilter-swift.class/sobelgradients().md>) — Calculates the Sobel gradients for an image.
- [+ spotColorFilter](<cifilter-swift.class/spotcolor().md>) — Replaces colors of an image with specifed colors.
- [+ spotLightFilter](<cifilter-swift.class/spotlight().md>) — Highlights a definined area of the image.
- [+ cannyEdgeDetectorFilter](<cifilter-swift.class/cannyedgedetector().md>) — Applies the Canny edge-detection algorithm to an image.

### Protocols

- [CIBlendWithMask](ciblendwithmask.md) — The properties you use to configure a blend with mask filter.
- [CIBloom](cibloom.md) — The properties you use to configure a bloom filter.
- [CICannyEdgeDetector](cicannyedgedetector.md)
- [CIComicEffect](cicomiceffect.md) — The properties you use to configure a comic effect filter.
- [CICoreMLModel](cicoremlmodel.md) — The properties you use to configure a Core ML model filter.
- [CICrystallize](cicrystallize.md) — The properties you use to configure a crystalize filter.
- [CIDepthOfField](cidepthoffield.md) — The properties you use to configure a depth-of-field filter.
- [CIEdgeWork](ciedgework.md) — The properties you use to configure an edge-work filter.
- [CIEdges](ciedges.md) — The properties you use to configure an edges filter.
- [CIGaborGradients](cigaborgradients.md) — The properties you use to configure a Gabor gradients filter.
- [CIGloom](cigloom.md) — The properties you use to configure a gloom filter.
- [CIHeightFieldFromMask](ciheightfieldfrommask.md) — The properties you use to configure a height-field-from-mask filter.
- [CIHexagonalPixellate](cihexagonalpixellate.md) — The properties you use to configure a hexagonal pixellate filter.
- [CIHighlightShadowAdjust](cihighlightshadowadjust.md) — The properties you use to configure a highlight-shadow adjust filter.
- [CILineOverlay](cilineoverlay.md) — The properties you use to configure a line overlay filter.
- [CIMix](cimix.md) — The properties you use to configure a mix filter.
- [CIPersonSegmentation](cipersonsegmentation.md)
- [CIPixellate](cipixellate.md) — The properties you use to configure a pixellate filter.
- [CIPointillize](cipointillize.md) — The properties you use to configure a pointillize filter.
- [CISaliencyMap](cisaliencymap.md) — The properties you use to configure a saliency map filter.
- [CIShadedMaterial](cishadedmaterial.md) — The properties you use to configure a shaded material filter.
- [CISobelGradients](cisobelgradients.md)
- [CISpotColor](cispotcolor.md) — The properties you use to configure a spot color filter.
- [CISpotLight](cispotlight.md) — The properties you use to configure a spotlight filter.

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
- [Reduction Filters](reduction-filters.md) — Create statistical information about an image.
- [Sharpening Filters](sharpening-filters.md) — Apply sharpening to images.
- [Tile Effect Filters](tile-effect-filters.md) — Produce tiled images from source images.
- [Transition Filters](transition-filters.md) — Transition between two images by using effects including page curl and swipe.
