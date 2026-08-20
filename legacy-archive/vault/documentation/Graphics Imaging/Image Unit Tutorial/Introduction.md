---
title: Image Unit Tutorial
apple_id: TP40004531
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/Introduction/Introduction.html
archived_at: '2026-07-15T07:36:04.136653Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](An%20Image%20Unit%20and%20Its%20Parts.md)

# Introduction

An image unit is a Core Image filter that is packaged as an [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) object. Any image processing filter that uses Core Image should be packaged as an image unit. Doing so makes it easy to distribute your filter. An image unit is not only a Core Image filter packaged as a bundle, it is a distribution mechanism for an image processing filter. This means that when you create an image unit, you also get the benefit of consistent packaging and an Apple-provided logo that you can license to use.

This tutorial provides the steps you need to write an image processing filter for OS X. More specifically, it shows you how to create image units that contain an executable filter. An executable filter has one portion that uses the central processing unit (CPU) to execute and another portion that uses the graphics processing unit (GPU). This document does not discuss nonexecutable filters, because they consist only of code that runs on the GPU and therefore have limitations.

The document is organized into these chapter:

- [An Image Unit and Its Parts](An%20Image%20Unit%20and%20Its%20Parts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqnrnknltc) describes the major parts of an image processing unit, what each does, and how they work together.
- [Writing Kernels](Writing%20Kernels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqmznknltc) provides examples, from simple to complex, of `kernel` routines.
- [Writing the Objective-C Portion](Writing%20the%20Objective-C%20Portion.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqnbnknltc) describes the image unit template provided by Xcode, discusses each of the files provided in the template, and shows how to package some of the `kernel` routines from the previous chapter as image units.
- [Preparing an Image Unit for Distribution](Preparing%20an%20Image%20Unit%20for%20Distribution.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqnjnknltc) discusses installing, validating, and testing image units and tells where to get more information on licensing the image unit logo.

Before reading this document you should:

- Read _[Core Image Programming Guide](../Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_.
- Be familiar with the Core Image API. See _[Core Image Reference Collection](https://developer.apple.com/documentation/coreimage)_.
- Write code that uses one of the built-in Core Image filters. See Using Core Image Filters in _[Core Image Programming Guide](../Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_.
- Take a look at _[Core Image Kernel Language Reference](../Core%20Image%20Kernel%20Language%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojx)_, which describes the procedural programming language used to write the kernel portion of an image unit.

If you are not a Cocoa programmer, don’t panic! The `kernel` routine portion of an image processing filter uses a procedural language. If you know C, you’ll catch on fast. The higher-level portion of an image processing filter uses the Core Image API, which is an Objective-C API, but is not part of the Cocoa framework. Because Xcode provides a template for writing an image unit, you’ll see that it’s relatively straightforward to use Objective-C to write an image unit.

If you are not an OpenGL programmer, don’t worry. The Core Image API was designed to hide all the messy details of dealing with the GPU from you. Although the `kernel` routine portion of an image processing filter uses a subset of the OpenGL Shading Language (glslang), you’ll see by looking at the examples that you don’t need prior knowledge to write `kernel` routines. You do, however, need to have an understanding of the mathematics behind the processing that you want to implement.

The resources in this section are valuable to any developer who is writing an image unit. You’ll find them most helpful as you work your way through this document and later on, when you are writing your own image units.

- ImageUnitAnalyzer is a tool that you use to ensure that any image unit you write is valid. After you install the developer tools, you can find the analyzer in `/Developer/usr/bin`.
- CIFilterBrowser is a widget that lets you inspect all installed image units as well as Core Image built-in filters. You can view the input parameters and attributes of a filter and see a preview of an output image produced by the filter.
- Core Image Fun House is an application that lets you explore all installed image units and Core Image built-in filters. You can choose any image to process and then apply one or more filters to the image by stacking the filters together. You can also turn off or on any filter in the stack to more closely examine filter effects. After you install the developer tools, you can find Core Image Fun House in `/Developer/Applications/Graphics Tools/`.
- _[CIAnnotation](../../../samplecode/CIAnnotation/CIAnnotation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrygi)_ is a sample application that contains two image unit projects and uses them for compositing images and painting over them.
- Quartz Composer is an application that you can use to explore motion graphics. Core Image developers can use this application to test image units and to try out `kernel` routines. After you install the developer tools, you can find Quartz Composer in /`Developer/Applications/`.
- _[Quartz Composer User Guide](../Quartz%20Composer%20User%20Guide/Introduction%20to%20Quartz%20Composer%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobr)_ describes how to use the Quartz Composer development tool.
- The `Quartz-dev` mailing list is a technical discussion forum for developers using Quartz technologies on OS X, including Core Image. To sign up, see [http://lists.apple.com/mailman/listinfo/quartz-dev](http://lists.apple.com/mailman/listinfo/quartz-dev).
[Next](An%20Image%20Unit%20and%20Its%20Parts.md)

