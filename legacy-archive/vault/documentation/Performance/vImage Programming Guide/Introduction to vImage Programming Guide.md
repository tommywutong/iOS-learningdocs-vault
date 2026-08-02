---
title: vImage Programming Guide
apple_id: TP30001001
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Accelerate
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vImage/Introduction/Introduction.html
archived_at: '2026-07-27T06:57:05.501319Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20vImage.md)

# Introduction to vImage Programming Guide

vImage, introduced in OS X v10.3, is a high-performance image processing framework. It includes high-level functions for image manipulation—convolutions, geometric transformations, histogram operations, morphological transformations, and alpha compositing—as well as utility functions for format conversions and other operations. You can call vImage functions from applications on the OS X, iOS, tvOS, and watchOS platforms.

vImage optimizes image processing by using the CPU’s vector processor. If a vector processor is not available, vImage uses the next best available option. This framework allows you to reap the benefits of vector processors without the need to write vectorized code.

To understand the information in this document, you should be familiar with Macintosh application development, the C programming language, and the basics of image representation and manipulation.

The vImage framework isn't the only image processing API that OS X provides. Starting in OS X v10.5, you also have the option of using Core Image. vImage is the ideal choice if you need to process large quantities of high-resolution images.

## Who Should Read This Document?

This document is for developers who need to write Macintosh programs that process large images quickly. Because technologies such as Quartz 2D and Core Image provide most common image manipulation routines, vImage is not intended for general-purpose image processing. It is particularly suited for:

- Incorporating high-performance graphics into their applications
- Efficiently processing large images
- Real-time video processing software
- Scientific applications that require high-accuracy numerical calculations
- Getting consistent numerical results across platforms despite video card arithmetic inconsistencies

## Organization of This Document

This document is organized into the following chapters:

- [Overview of vImage](Overview%20of%20vImage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrqgiwvgvzr) introduces vImage and discusses how it optimizes image processing. It introduces the Accelerate framework, and explains how vector processing is used to achieve better performance. This also offers general usage guidelines for vImage and describes the workflow for incorporating vImage into an application.
- [Performing Convolution Operations](Performing%20Convolution%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrqguwvgvzr) explains the theory behind kernel convolution, a technique frequently employed in image processing to apply a filter to an image. It describes how convolutions can be performed with vImage and provides several sample kernels.
- [Performing Geometric Operations](Performing%20Geometric%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrqgywvgvzr) explains what a geometric operation is and which ones are supported in vImage.
- [Performing Morphological Operations](Performing%20Morphological%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrrgiwvgvzs) describes what morphological operations are and the types available in vImage.
- [Performing Histogram Operations](Performing%20Histogram%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrqg4wvgvzr) discusses histograms and how they can be useful for calibrating or analyzing images.
- [Performing Alpha Compositing Operations](Performing%20Alpha%20Compositing%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrqhawvgvzr) explains the theory behind alpha compositing and the alpha channel and shows how they can be used in vImage to create layered visual effects.
- [Performing Image Transformation Operations](Performing%20Image%20Transformation%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrqhewvgvzr) introduces the use of callback functions to alter each pixel in an image.

## See Also

You might find these other Apple developer documents of value as you determine your image processing needs:

- _[Image I/O Programming Guide](../../Graphics%20Imaging/Image%20I-O%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrs)_

  Image I/O facilitates the process of reading and writing images of various formats to and from the disk. vImage does not do this for you. It may be worth familiarizing yourself with Image I/O so that you can more effectively supply vImage with data.
- _[Core Image Programming Guide](../../Graphics%20Imaging/Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_

  If you want to add image processing capability to an application to support color adjustment, halftone effects, stylizing filters, compositing, and transition effects, you might want to consider Core Image. The Core Image framework is a high-level Objective-C programming interface that has more than 800 built-in filters and supports writing your own custom filters.
- _[OpenGL Programming Guide for Mac](../../Graphics%20Imaging/OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_

  If you have a need for hardware-accelerated 3D graphics, OS X provides an implementation of the OpenGL graphics standard.

[Next](Overview%20of%20vImage.md)
