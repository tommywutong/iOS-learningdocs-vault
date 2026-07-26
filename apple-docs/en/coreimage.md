---
title: Core Image
framework: Core Image
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage
source_url: 'https://developer.apple.com/documentation/coreimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage.json'
content_hash: 'sha256:85ae44972c25dcf4'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Core Image

<sub>Framework</sub>

Use built-in or custom filters to process still and video images.

## Overview

Core Image is an image processing and analysis technology that provides high-performance processing for still and video images. Use the many built-in image filters to process images and build complex effects by chaining filters. For a list of all the built-in filters see the [Filter Catalog](coreimage.md#Filter-Catalog).

You can also create new effects with custom filters and image processors; see [Custom Filters](coreimage.md#Custom-Filters).

## Topics

### Essentials

- [Processing an Image Using Built-in Filters](coreimage/processing-an-image-using-built-in-filters.md) — Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [CIContext](coreimage/cicontext.md) — The Core Image context class provides an evaluation context for Core Image processing with Metal, OpenGL, or OpenCL.
- [CIImage](coreimage/ciimage.md) — A representation of an image to be processed or produced by Core Image filters.

### Filters

- [CIFilter](coreimage/cifilter-swift.class.md) — An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [CIRAWFilter](coreimage/cirawfilter.md) — A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [CIColor](coreimage/cicolor.md) — The Core Image class that defines a color object.
- [CIVector](coreimage/civector.md) — The Core Image class that defines a vector object.

### Filter Catalog

- [Blur Filters](coreimage/blur-filters.md) — Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](coreimage/color-adjustment-filters.md) — Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](coreimage/color-effect-filters.md) — Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](coreimage/composite-operations.md) — Composite images by using a range of blend modes and compositing operators.
- [Convolution Filters](coreimage/convolution-filters.md) — Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](coreimage/distortion-filters.md) — Apply distortion to images.
- [Generator Filters](coreimage/generator-filters.md) — Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](coreimage/geometry-adjustment-filters.md) — Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](coreimage/gradient-filters.md) — Generate linear and radial gradients.
- [Halftone Effect Filters](coreimage/halftone-effect-filters.md) — Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](coreimage/reduction-filters.md) — Create statistical information about an image.
- [Sharpening Filters](coreimage/sharpening-filters.md) — Apply sharpening to images.
- [Stylizing Filters](coreimage/stylizing-filters.md) — Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](coreimage/tile-effect-filters.md) — Produce tiled images from source images.
- [Transition Filters](coreimage/transition-filters.md) — Transition between two images by using effects including page curl and swipe.

### Filter Recipes

- [Applying a Chroma Key Effect](coreimage/applying-a-chroma-key-effect.md) — Replace a color in one image with the background from another.
- [Selectively Focusing on an Image](coreimage/selectively-focusing-on-an-image.md) — Focus on a part of an image by applying Gaussian blur and gradient masks.
- [Customizing Image Transitions](coreimage/customizing-image-transitions.md) — Transition between images in creative ways using Core Image filters.
- [Simulating Scratchy Analog Film](coreimage/simulating-scratchy-analog-film.md) — Degrade the quality of an image to make it look like dated, analog film.

### Custom Filters

- [Writing Custom Kernels](coreimage/writing-custom-kernels.md) — Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [CIKernel](coreimage/cikernel.md) — A GPU-based image-processing routine used to create custom Core Image filters.
- [CIColorKernel](coreimage/cicolorkernel.md) — A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [CIWarpKernel](coreimage/ciwarpkernel.md) — A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [CIBlendKernel](coreimage/ciblendkernel.md) — A GPU-based image-processing routine that is optimized for blending two images.
- [CISampler](coreimage/cisampler.md) — An object that retrieves pixel samples for processing by a filter kernel.
- [CIFilterShape](coreimage/cifiltershape.md) — A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [CIFormat](coreimage/ciformat.md) — Pixel data formats for image input, output, and processing.

### Custom Image Processors

- [CIImageProcessorKernel](coreimage/ciimageprocessorkernel.md) — The abstract class you extend to create custom image processors that can integrate with Core Image workflows.
- [CIImageProcessorInput](coreimage/ciimageprocessorinput.md) — A container of image data and information for use in a custom image processor.
- [CIImageProcessorOutput](coreimage/ciimageprocessoroutput.md) — A container for writing image data and information produced by a custom image processor.

### Custom Render Destination

- [Generating an animation with a Core Image Render Destination](coreimage/generating-an-animation-with-a-core-image-render-destination.md) — Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [CIRenderDestination](coreimage/cirenderdestination.md) — A specification for configuring all attributes of a render task’s destination and issuing asynchronous render tasks.
- [CIRenderInfo](coreimage/cirenderinfo.md) — An encapsulation of a render task’s timing, passes, and pixels processed.
- [CIRenderTask](coreimage/cirendertask.md) — A single render task.
- [CIRenderDestinationAlphaMode](coreimage/cirenderdestinationalphamode.md) — Different ways of representing alpha.

### Feedback-Based Processing

- [CIImageAccumulator](coreimage/ciimageaccumulator.md) — An object that manages feedback-based image processing for tasks such as painting or fluid simulation.

### Barcode Descriptions

- [CIBarcodeDescriptor](coreimage/cibarcodedescriptor.md) — An abstract base class that represents a machine-readable code’s attributes.
- [CIQRCodeDescriptor](coreimage/ciqrcodedescriptor.md) — A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
- [CIAztecCodeDescriptor](coreimage/ciazteccodedescriptor.md) — A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [CIPDF417CodeDescriptor](coreimage/cipdf417codedescriptor.md) — A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
- [CIDataMatrixCodeDescriptor](coreimage/cidatamatrixcodedescriptor.md) — A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.

### Image Feature Detection

- [CIDetector](coreimage/cidetector.md) — An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [CIFeature](coreimage/cifeature.md) — The abstract superclass for objects representing notable features detected in an image.
- [CIFaceFeature](coreimage/cifacefeature.md) — Information about a face detected in a still or video image.
- [CIRectangleFeature](coreimage/cirectanglefeature.md) — Information about a rectangular region detected in a still or video image.
- [CITextFeature](coreimage/citextfeature.md) — Information about a text that was detected in a still or video image.
- [CIQRCodeFeature](coreimage/ciqrcodefeature.md) — Information about a Quick Response code detected in a still or video image.

### Image Units

- [CIPlugIn](coreimage/ciplugin.md) — The mechanism for loading image units in macOS.
- [CIFilterGenerator](coreimage/cifiltergenerator.md) — An object that creates and configures chains of individual image filters.
- [CIPlugInRegistration](coreimage/cipluginregistration.md) — The interface for loading Core Image image units.
- [CIFilterConstructor](coreimage/cifilterconstructor.md) — A general interface for objects that produce filters.

### Protocols

- [CIAreaBoundsRed](coreimage/ciareaboundsred.md)
- [CIMaximumScaleTransform](coreimage/cimaximumscaletransform.md)
- [CIToneMapHeadroom](coreimage/citonemapheadroom.md)
- [CIAreaAverageMaximumRed](coreimage/ciareaaveragemaximumred.md) — The protocol for the Area Average and Maximum Red filter.
- [CIBlurredRoundedRectangleGenerator](coreimage/ciblurredroundedrectanglegenerator.md) — The protocol for the Blurred Rounded Rectangle Generator filter.
- [CIDistanceGradientFromRedMask](coreimage/cidistancegradientfromredmask.md) — The protocol for the Distance Gradient From Red Mask filter.
- [CIRoundedQRCodeGenerator](coreimage/ciroundedqrcodegenerator.md) — The protocol for the Rounded QR Code Generator filter.
- [CISignedDistanceGradientFromRedMask](coreimage/cisigneddistancegradientfromredmask.md) — The protocol for the Signed Distance Gradient From Red Mask filter.

### Reference

- [Core Image Constants](coreimage/core-image-constants.md)

## See Also

### Related Documentation

- [Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346-Reference)
- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
