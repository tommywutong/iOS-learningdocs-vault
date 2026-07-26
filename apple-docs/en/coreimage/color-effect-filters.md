---
title: Color Effect Filters
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/color-effect-filters
source_url: 'https://developer.apple.com/documentation/coreimage/color-effect-filters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/color-effect-filters.json'
content_hash: 'sha256:6923228c470df17f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# Color Effect Filters

<sub>API Collection</sub>

Apply color effects, including photo effects, dithering, and color maps.

## Topics

### Color Effect Filters

- [+ colorCrossPolynomialFilter](<cifilter-swift.class/colorcrosspolynomial().md>) — Adjusts an image’s color by applying polynomial cross-products.
- [+ colorCubeFilter](<cifilter-swift.class/colorcube().md>) — Adjusts an image’s pixels using a three-dimensional color table.
- [+ colorCubeWithColorSpaceFilter](<cifilter-swift.class/colorcubewithcolorspace().md>) — Adjusts an image’s pixels using a three-dimensional color table in specified color space.
- [+ colorCubesMixedWithMaskFilter](<cifilter-swift.class/colorcubesmixedwithmask().md>) — Alters an image’s pixels using a three-dimensional color tables and a mask image.
- [+ colorCurvesFilter](<cifilter-swift.class/colorcurves().md>) — Adjusts an image’s color curves.
- [+ colorInvertFilter](<cifilter-swift.class/colorinvert().md>) — Inverts an image’s colors.
- [+ colorMapFilter](<cifilter-swift.class/colormap().md>) — Performs a transformation of the input image colors to colors from a gradient image.
- [+ colorMonochromeFilter](<cifilter-swift.class/colormonochrome().md>) — Adjusts an image’s colors to shades of a single color.
- [+ colorPosterizeFilter](<cifilter-swift.class/colorposterize().md>) — Flattens an image’s colors.
- [+ convertLabToRGBFilter](<cifilter-swift.class/convertlabtorgb().md>) — Converts an image from CIELAB to RGB color space.
- [+ convertRGBtoLabFilter](<cifilter-swift.class/convertrgbtolab().md>) — Converts an image from RGB to CIELAB color space.
- [+ ditherFilter](<cifilter-swift.class/dither().md>) — Applies randomized noise to produce a processed look.
- [+ documentEnhancerFilter](<cifilter-swift.class/documentenhancer().md>) — Adjusts an image’s shadows and contrast.
- [+ falseColorFilter](<cifilter-swift.class/falsecolor().md>) — Replaces an image’s colors with specified colors.
- [+ LabDeltaE](<cifilter-swift.class/labdeltae().md>) — Compares an image’s color values.
- [+ maskToAlphaFilter](<cifilter-swift.class/masktoalpha().md>) — Converts an image to a white image with an alpha component.
- [+ maximumComponentFilter](<cifilter-swift.class/maximumcomponent().md>) — Creates a maximum RGB grayscale image.
- [+ minimumComponentFilter](<cifilter-swift.class/minimumcomponent().md>) — Creates a minimum RGB grayscale image.
- [+ paletteCentroidFilter](<cifilter-swift.class/palettecentroid().md>) — Calculates the location of an image’s colors.
- [+ palettizeFilter](<cifilter-swift.class/palettize().md>) — Replaces colors with colors from a palette image.
- [+ photoEffectChromeFilter](<cifilter-swift.class/photoeffectchrome().md>) — Exaggerates an image’s colors.
- [+ photoEffectFadeFilter](<cifilter-swift.class/photoeffectfade().md>) — Diminishes an image’s colors.
- [+ photoEffectInstantFilter](<cifilter-swift.class/photoeffectinstant().md>) — Desaturates an image’s colors.
- [+ photoEffectMonoFilter](<cifilter-swift.class/photoeffectmono().md>) — Adjust an image’s colors to black and white.
- [+ photoEffectNoirFilter](<cifilter-swift.class/photoeffectnoir().md>) — Adjusts an image’s colors to black and white and intensifies the contrast.
- [+ photoEffectProcessFilter](<cifilter-swift.class/photoeffectprocess().md>) — Lowers the contrast of the input image.
- [+ photoEffectTonalFilter](<cifilter-swift.class/photoeffecttonal().md>) — Adjusts an image’s colors to black and white.
- [+ photoEffectTransferFilter](<cifilter-swift.class/photoeffecttransfer().md>) — Brightens an image’s colors.
- [+ sepiaToneFilter](<cifilter-swift.class/sepiatone().md>) — Adjusts an image’s colors to shades of brown.
- [+ thermalFilter](<cifilter-swift.class/thermal().md>) — Alters the image to make it look like it was taken by a thermal camera.
- [+ vignetteFilter](<cifilter-swift.class/vignette().md>) — Gradually darkens an image’s edges.
- [+ vignetteEffectFilter](<cifilter-swift.class/vignetteeffect().md>) — Gradually darkens a specified area of an image.
- [+ xRayFilter](<cifilter-swift.class/xray().md>) — Alters an image to make it look like an X-ray image.

### Protocols

- [CIColorCrossPolynomial](cicolorcrosspolynomial.md) — The properties you use to configure a color cross-polynomial filter.
- [CIColorCube](cicolorcube.md) — The properties you use to configure a color cube filter.
- [CIColorCubeWithColorSpace](cicolorcubewithcolorspace.md) — The properties you use to configure a color cube with color space filter.
- [CIColorCubesMixedWithMask](cicolorcubesmixedwithmask.md) — The properties you use to configure a color cube mixed with mask filter.
- [CIColorCurves](cicolorcurves.md) — The properties you use to configure a color curves filter.
- [CIColorInvert](cicolorinvert.md) — The properties you use to configure a color invert filter.
- [CIColorMap](cicolormap.md) — The properties you use to configure a color map filter.
- [CIColorMonochrome](cicolormonochrome.md) — The properties you use to configure a color monochrome filter.
- [CIConvertLab](ciconvertlab.md)
- [CIDither](cidither.md) — The properties you use to configure a dither filter.
- [CIColorPosterize](cicolorposterize.md) — The properties you use to configure a color posterize filter.
- [CIDocumentEnhancer](cidocumentenhancer.md) — The properties you use to configure a document enhancer filter.
- [CIFalseColor](cifalsecolor.md) — The properties you use to configure a false color filter.
- [CILabDeltaE](cilabdeltae.md) — The properties you use to configure a Lab Delta E filter.
- [CIMaskToAlpha](cimasktoalpha.md) — The properties you use to configure a mask-to-alpha filter.
- [CIMaximumComponent](cimaximumcomponent.md) — The properties you use to configure a maximum component filter.
- [CIMinimumComponent](ciminimumcomponent.md) — The properties you use to configure a minimum component filter.
- [CIPaletteCentroid](cipalettecentroid.md) — The properties you use to configure a palette centroid filter.
- [CIPalettize](cipalettize.md) — The properties you use to configure a palettize filter.
- [CIPhotoEffect](ciphotoeffect.md) — The properties you use to configure a photo-effect filter.
- [CISepiaTone](cisepiatone.md) — The properties you use to configure a sepia-tone filter.
- [CIThermal](cithermal.md) — The properties you use to configure a thermal filter.
- [CIVignette](civignette.md) — The properties you use to configure a vignette filter.
- [CIVignetteEffect](civignetteeffect.md) — The properties you use to configure a vignette-effect filter.
- [CIXRay](cixray.md) — The properties you use to configure an X-ray filter.

## See Also

### Filter Catalog

- [Blur Filters](blur-filters.md) — Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color-adjustment-filters.md) — Apply color transformations, including exposure, hue, and tint adjustments.
- [Composite Operations](composite-operations.md) — Composite images by using a range of blend modes and compositing operators.
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
