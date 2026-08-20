---
title: Image Unit Tutorial
apple_id: TP40004531
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/Overview/Overview.html
archived_at: '2026-07-15T07:36:04.147952Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Image Unit Tutorial](Introduction.md)


[Next](Writing%20Kernels.md)[Previous](Introduction.md)

# An Image Unit and Its Parts

This tutorial provides detailed information on how to write the various parts of an image unit so that they work together as an image unit. It’s important that you have an idea not only of what the parts are, but how they fit together. This chapter provides such an overview. It describes the parts of an image unit, discusses what each one does, and provides guidelines for writing some of the components in an image unit.

Before you start this chapter, you should be familiar with the concepts described in _[Core Image Programming Guide](../Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_, have already used some of the built-in image processing filters provided by Core Image, and understand the classes defined by the Core Image API (see _[Core Image Reference Collection](https://developer.apple.com/documentation/coreimage)_).

An image processing filter, when packaged as an executable image unit, has three major parts:

- A `kernel` routine file. This file contains one or more `kernel` routines and any needed subroutines. The `kernel` routine must be written using the Core Image Kernel Language (CIKL). A C-like language, CIKL is a subset of the OpenGL Shading Language (glslang). CIKL restricts some of the glslang keywords that you can use, but introduces a number of keywords and data types that are not provided by glslang. (See _[Core Image Kernel Language Reference](../Core%20Image%20Kernel%20Language%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojx)_.)
- Objective-C filter files. Each filter has an interface and implementation file that performs all the set up work required prior to applying a `kernel` routine.
- Plug-in loading files. Each image unit has an interface and implementation file that implements the plug-in loading protocol.

Image processing tasks are divided into low-level (kernel) and high-level (Objective-C) tasks. When you first start writing image units, you might find it challenging to divide the tasks appropriately. If you strive to keep `kernel` routines lean, you will likely succeed in dividing the tasks appropriately.

A `kernel` routine operates on individual pixels and uses the GPU (assuming one is available). For best performance, a `kernel` routine should be as focused as possible on pixel processing. Any set up work or calculations that can be done outside the `kernel` routine should be done outside the `kernel` routine, in the Objective-C filter files. As you’ll see, because Core Image expects certain tasks to be performed outside the `kernel` routine, the Xcode image unit plug-in template provides methods set up for just this purpose. In [Writing the Objective-C Portion](Writing%20the%20Objective-C%20Portion.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqnbnknltc) you see the specifics, but for now, a general understanding is all you’ll need.

These are the tasks typically performed in the Objective-C filter files:

- Retrieve the files needed for the filter. Image I/O is a high-level task that is typically done during the initialization phase of the image unit filter. Files can include the image (or images) to be processed and any other image data needed by the `kernel` routine (such as a texture or an environment map).
- Set up one or more [CISampler](https://developer.apple.com/documentation/coreimage/cisampler) objects. A `sampler` (lowercase “s”) is a data source for a kernel routine. (It is defined in _[Core Image Kernel Language Reference](../Core%20Image%20Kernel%20Language%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojx)_.) A `CISampler` object is a Core Image class that encapsulates a `sampler`, references a file to fetch samples from, defines a coordinate transform (if any) to use on the samples, and defines modes to use for interpolation and wrapping. The data source referenced by a `CISampler` object can be a texture, an environment map, an image to process, a lookup table—whatever is needed by the `kernel` routine.
- Set up one or more [CIKernel](https://developer.apple.com/documentation/coreimage/cikernel) objects. A `kernel` (lowercase “k”) refers to a kernel routine. (It is defined in _[Core Image Kernel Language Reference](../Core%20Image%20Kernel%20Language%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojx)_.) A `CIKernel` object is a Core Image class that encapsulates a kernel file, references each of the `kernel` routines in the file and defines a region-of-interest method for each of the `kernel` routines that requires such a method.
- Set a region-of-interest method and any input parameters required for that method. A region of interest (ROI) defines the area in the source image from which a sampler takes pixel information to provide to the kernel for processing. Simple filters—those for which there is a 1:1 mapping between a source and destination pixel—don’t need a method to calculate the region of interest because Core Image assumes a 1:1 mapping if you don’t supply an ROI method. See [Region-of-Interest Methods](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqnrnknlte) for more details.
- Set up input parameters for the `kernel` routine. The Objective-C portion of an image unit is where you perform all calculations possible so that the values you pass to the `kernel` routine are ready to use. For example, you could calculate the radius of an effect in the Objective-C portion rather than pass a diameter to the kernel and perform the radius calculation in the kernel. This way, the calculation is performed only once, and not for every pixel that’s processed.
- Apply the `kernel` routine. You can invoke a `kernel` routine more than once (as you might for effects that require iteration, such as a blur effect). You can use more than one `kernel` routine to process an image. You can also combine your `kernel` routine with an effect produced by one of the built-in Core Image filters.

A `kernel` routine is like a worker on an assembly line—it specializes in a focused task. Each time the routine is invoked, it produces a `vec4` data type from the materials (input parameters) given to it. The routine must perform as little work as possible to be efficient. Assembly line work goes fastest when workers use preassembled subcomponents. It’s also true of `kernel` routines. Anything that can be calculated ahead of time and passed to the routine should be. As you become more experienced at writing `kernel` routines, you’ll devise clever ways to pare down the code in the routine. The examples in [Writing Kernels](Writing%20Kernels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqmznknltc) should give you some ideas. Core Image also helps in this regard by restricting what sorts of operations can be done in a `kernel` routine.

Keep the following in mind as you design and write `kernel` routines:

- Flow control statements (`if`, `for`, `while`, `do while`) are supported only when the loop condition can be inferred at the time the code compiles.
- The input parameters to a `kernel` routine can be any of these data types: `sampler`, `__table sampler`, `__color`, `float`, `vec2`, `vec3`, or `vec4`. However, when you apply a `kernel` routine in the Objective-C portion of an image unit, you must supply objects. See [Table 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqnrnknltk).
- A `kernel` routine does not take images as input parameters. Instead, it takes a `sampler` object that’s associated with an image. It is the job of the `sampler` object to fetch image data and provide it to the `kernel` routine. All `sampler` objects are set up as `CISampler` objects in the Objective-C portion of an image unit. See [Division of Labor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqnrnknltg).
- You are restricted to using what’s described in _[Core Image Kernel Language Reference](../Core%20Image%20Kernel%20Language%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojx)_. The Core Image Kernel Language (CIKL) is a subset of OpenGL Shading Language (glslang), so not everything that’s defined by glslang is allowed by CIKL. However, you’ll find that most of the keywords in gslang are available to you. In addition, CIKL provides a number of data types, keywords, and functions that are not available in glslang.
- You can’t use arrays.
- A `kernel` routine computes an output pixel by using an inverse mapping back to the corresponding pixels of the input images. Although you can express most pixel computations this way—some more naturally than others—there are some image processing operations for which this is difficult, if not impossible. For example, computing a histogram is difficult to describe as an inverse mapping to the source image. You also cannot perform seed fills or any image analysis operations that require complex conditional statements.
- A routine is faster if you unroll loops.

Table 1-1 lists the valid input parameters for a `kernel` routine and the associated objects that must be passed to the kernel routine from the Objective-C portion of an image unit. Core Image extracts the appropriate base data type from the higher-level Objective-C object that you supply. If you don’t use an object, the filter may unexpectedly quit. For example, if, in the Objective-C portion of the image unit, you pass a floating-point value directly instead of packaging it as an `NSNumber` object, your filter will not work. In fact, when you use the Image Unit Validator tool on such an image unit, the image unit fails with a cryptic message. (See [Validating an Image Unit](Preparing%20an%20Image%20Unit%20for%20Distribution.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqnjnknltg).)

__Table 1-1__  `Kernel` routine input parameters and their associated objects

| Kernel routine input parameter | Object |
| `sampler` | `CISampler` |
| `__table sampler` | `CISampler` |
| `__color` | `CIColor` |
| `float` | `NSNumber` |
| `vec2`, `vec3`, or `vec4` | `CIVector` |

The region of interest (ROI) is the area of the sampler source data that your kernel uses for its per-pixel processing. A `kernel` routine always returns a `vec4` data type—that is, one pixel. However, the routine can operate on any number of pixels to produce that `vec4` data type. If the mapping between the source and the destination is not one-to-one, then you must define a region-of-interest method in the Objective-C filter file.

You do not need an ROI method when a `kernel` routine:

- Processes a pixel from the working-space coordinate (_r_,_s_) of the sampler to produce a pixel at the working-space coordinate (_r_,_s_) in the destination image.

You must supply an ROI method when a `kernel` routine:

- Uses many source pixels in the calculation of one destination pixel. For example, a distortion filter might use a pixel (_r_,_s_) and its neighbors from the source image to produce a single pixel (_r_,_s_) in the destination image.
- Uses values provided by a `sampler` that are unrelated to the working-space coordinates in the source image and the destination. For example, a texture, a color ramp, or a table that approximates a function provides values that are unrelated to the notion of working coordinates.

You supply an ROI method for each `kernel` routine in an image unit that needs you. (An image unit can contain one or more `kernel` routines.) Each ROI method that you supply must use a method signature of the following form:

```objc
- (CGRect) regionOf:(int)samplerIndex
            destRect:(CGRect)r
            userInfo:obj;
```

You can replace `regionOf` with an appropriate name. For example, an ROI method for a blur filter could be named `blurROI:destRect:userInfo:`.

Core Image invokes your ROI method when appropriate, passing to it the `sampler` index (which you’ll learn more about later), the rectangle for the region being rendered, and any data that is needed by your routine. The method must define the ROI for each `sampler` data source used by the `kernel` routine. If a `sampler` data source used by the `kernel` routine doesn’t require an ROI method, then you can pass back the `destRect` rectangle for that `sampler`. You simply check the `samplerIndex` value passed to the method. If an ROI calculation is need for the `sampler`, perform the calculation and pass back the appropriate rectangle. If an ROI calculation is not needed for that particular `sampler`, then pass back the `destRect` passed to the method.

For example, if your `kernel` routine accesses pixels within a radius `r` around the current target, you need to offset the destination rectangle in the ROI method by the radius `r`. You’ll see how all this works in more detail later.

Now that you have a general idea of what the major parts of an image unit are and what each does, you are ready to move on to writing `kernel` routines. [Writing Kernels](Writing%20Kernels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmzrfvbuqmznknltc) starts with a few simple `kernel` routines and progresses to more complex ones. Not only will you se how to write `kernel` routines, but you’ll see how you can test simple `kernel` routines without the need to provide Objective-C code.

[Next](Writing%20Kernels.md)[Previous](Introduction.md)

