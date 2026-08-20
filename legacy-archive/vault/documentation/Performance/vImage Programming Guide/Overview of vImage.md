---
title: vImage Programming Guide
apple_id: TP30001001
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Accelerate
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vImage/OverviewofvImage/OverviewofvImage.html
archived_at: '2026-07-27T06:57:05.514153Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [vImage Programming Guide](Introduction%20to%20vImage%20Programming%20Guide.md)


[Next](Performing%20Convolution%20Operations.md)[Previous](Introduction%20to%20vImage%20Programming%20Guide.md)

# Overview of vImage

vImage is a two-dimensional image processing framework. Part of the Accelerate Framework, vImage provides optimized routines for features such as image filters, scalings, reflections and rotations. While its features share several commonalities with other imaging frameworks such as Core Image, what distinguishes vImage from the rest is that it uses vectorized code wherever possible. If your code runs on a processor whose architecture includes a vector processor, vImage takes advantage of them to run vectorized code. When running on an architecture that does not feature a vector processor, it will still run, but without vector optimization.

## When to use vImage

If real-time image processing is a need for your application, you should use vImage. Be sure to make use of temporary buffers when available to avoid blocking on calls to `malloc()`.

Aside from applying effects to images, vImage is also well-suited for applications that require consistent, standards-compliant arithmetic results.

Generally speaking, vImage is a timesaver, but there are certain costs associated with using the specialized vector processor and data caches to process your images. For example, it would not be practical to use vImage to process a single, average-sized photo. While vImage is perfectly capable of doing such processing, its benefit lies in processing images in real-time or repeating an operation successively. Core Image is a better choice if you are not dealing with large, high-resolution images.

Because vImage is a pure C framework, there are no classes to keep track of, only functions, image formats, and data types. All vImage functions begin with the word “vImage” followed by the name of the operation. Some functions also have an underscore (“_“) in their names. The characters that follow the underscore usually indicate the image format that the function operates upon.

## Image Formats Available in vImage

vImage supports several images formats. _Image formats_ are specifications for how pixel data is represented in memory. Image file formats are the specific file types (such as JPG, PNG, GIF, and TIFF) used to exchange image data between programs and store them on the hard disk. Frameworks like Image I/O assist you in loading the various image file formats from disk and using them in memory. In memory, images are stored as two-dimensional arrays of pixel intensities (of type `int` or `float`). There is one pixel in the array for each pixel in the image.

Image formats are either planar or interleaved. A planar image format stores image data so that the data for each channel (plane) is in a separate buffer. For example, a typical planar image would have separate buffers for the red, green, blue, and alpha channels. An interleaved image format stores image data so that the data from each pixel alternates: ARGBARGBARGB . . .

Data values for images can be integer or floating-point. In vImage, image formats that use integer values represent an intensity level as an 8-bit unsigned value. Values can range from 0 to 255, inclusive, with 255 indicating full intensity and 0 no intensity. Image formats that use floating-point values typically use values in the range of 0.0 (lowest intensity) to 1.0 (full intensity). However, vImage does not enforce this range restriction and does not clip calculated values that lie outside this range.

vImage uses the following image formats for its core operations:

- __Planar8__ The image is a single channel (one color or alpha value). Each pixel is an 8-bit unsigned integer value. The data type for this image format is `Pixel_8`.
- __PlanarF__ The image is a single channel (one color). Each pixel is a 32-bit floating-point value. The data type for this image format is `Pixel_F`.
- __ARGB8888__ The image has four interleaved channels, for alpha, red, green, and blue, in that order. Each pixel is 32 bits, an array of four 8-bit unsigned integers. The data type for this image format is `Pixel_8888`.
- __ARGBFFFF__ The image has four interleaved channels, for alpha, red, green, and blue, in that order. Each pixel is an array of four floating-point numbers. The data type for this image format is `Pixel_FFFF`.
- __RGBA8888__ The image has four interleaved channels, for red, green, blue, and alpha, in that order. Each pixel is 32 bits, an array of four 8-bit unsigned integers. The data type for this image format is `Pixel_8888`.
- __RGBAFFFF__ The image has four interleaved channels, for red, green, blue, and alpha, in that order. Each pixel is an array of four floating-point numbers. The pixel data type for this image format is `Pixel_FFFF`.

You can also use vImage to process images in other formats by first converting them to one of vImage’s core image formats. For example, you could take an image defined with 16-bit pixels and convert it to a 32-bit pixel format supported by vImage using a conversion function like [vImageConvert_16SToF](https://developer.apple.com/documentation/accelerate/1533286-vimageconvert_16stof). These functions can help you convert images to and from non supported formats and supported ones:

- [vImageConvert_16SToF](https://developer.apple.com/documentation/accelerate/1533286-vimageconvert_16stof)

  Converts a planar (or interleaved—multiply `vImage_Buffer.width` by 4) `vImage_Buffer` of 16-bit signed integers to a buffer containing floating-point values.
- [vImageConvert_16UToF](https://developer.apple.com/documentation/accelerate/1533130-vimageconvert_16utof)

  Converts a planar (or interleaved—multiply `vImage_Buffer.width` by 4) `vImage_Buffer` of 16-bit unsigned integers to a buffer containing floating-point values.
- [vImageConvert_FTo16S](https://developer.apple.com/documentation/accelerate/1533281-vimageconvert_fto16s)

  Converts a planar (or interleaved—multiply `vImage_Buffer.width` by 4) `vImage_Buffer` of floating-point values to a buffer containing 16-bit signed integers.
- [vImageConvert_FTo16U](https://developer.apple.com/documentation/accelerate/1533273-vimageconvert_fto16u)

  Converts a planar (or interleaved—multiply `vImage_Buffer.width` by 4) `vImage_Buffer` of floating-point values to a buffer containing 16-bit unsigned integers.
- `vImageConvert_16UtoPlanar8`

  Converts a planar (or interleaved—multiply `vImage_Buffer.width` by 4) `vImage_Buffer` of 16-bit unsigned integers to a buffer containing 8-bit integer values.
- `vImageConvert_Planar8to16U`

  Converts a planar (or interleaved—multiply `vImage_Buffer.width` by 4) `vImage_Buffer` of 8-bit integer values to a buffer containing 16-bit unsigned integer values.
- [vImageConvert_ARGB1555toPlanar8](https://developer.apple.com/documentation/accelerate/1533269-vimageconvert_argb1555toplanar8)

  Converts 16 bits/pixel images (with a 1-bit alpha channel and 5-bit red, green, and blue channels) to Planar8 format.
- [vImageConvert_ARGB1555toARGB8888](https://developer.apple.com/documentation/accelerate/1533237-vimageconvert_argb1555toargb8888)

  Converts 16 bits/pixel images (with a 1-bit alpha channel and 5-bit red, green, and blue channels) to ARGB8888 format.
- [vImageConvert_Planar8toARGB1555](https://developer.apple.com/documentation/accelerate/1532999-vimageconvert_planar8toargb1555)

  Converts Planar8 images to 16 bits/pixel images with 1-bit alpha channels, and 5-bit red, green, and blue channels.
- [vImageConvert_ARGB8888toARGB1555](https://developer.apple.com/documentation/accelerate/1533047-vimageconvert_argb8888toargb1555)

  Converts ARGB8888 images to 16 bits/pixel images with 1-bit alpha channels, and 5-bit red, green, and blue channels.
- [vImageConvert_RGB565toPlanar8](https://developer.apple.com/documentation/accelerate/1533170-vimageconvert_rgb565toplanar8)

  Converts 16 bits/pixel images with 5-bit red channels, 6-bit green channels, and 5-bit blue channels to Planar8 format.
- [vImageConvert_RGB565toARGB8888](https://developer.apple.com/documentation/accelerate/1533159-vimageconvert_rgb565toargb8888)

  Converts 16 bits/pixel images with 5-bit red channels, 6-bit green channels, and 5-bit blue channels to ARGB8888 format.
- [vImageConvert_Planar8toRGB565](https://developer.apple.com/documentation/accelerate/1533146-vimageconvert_planar8torgb565)

  Converts Planar8 images to 16 bits/pixel images with 5-bit red channels, 6-bit green channels, and 5-bit blue channels.
- [vImageConvert_ARGB8888toRGB565](https://developer.apple.com/documentation/accelerate/1533044-vimageconvert_argb8888torgb565)

  Converts ARGB8888 images to 16 bits/pixel images with 5-bit red channels, 6-bit green channels, and 5-bit blue channels.
- [vImageConvert_Planar16FtoPlanarF](https://developer.apple.com/documentation/accelerate/1533030-vimageconvert_planar16ftoplanarf)

  Converts planar images containing 16-bit floating-point values to 32-bit floating-point values.

  __Note:__ The 16-bit floating-point format used is identical to OpenEXR. Limit your usage of this function as conversions between 16-bit floating-point values and 32-bit floating-point values are expensive.
- [vImageConvert_PlanarFtoPlanar16F](https://developer.apple.com/documentation/accelerate/1533151-vimageconvert_planarftoplanar16f)

  Converts planar images containing 32-bit floating-point values to 16-bit floating-point values.

  __Note:__ The 16-bit floating-point format used is identical to OpenEXR. Limit your usage of this function as conversions between 16-bit floating-point values and 32-bit floating-point values are expensive.

## Data Types and 64-Bit Processing

Starting with version 10.4, OS X supports 64-bit addressing for those applications compiled for 64-bit architectures. The vImage framework natively supports 64-bit architectures, which means that all vImage functions available in OS X v10.4 and later are available for both 32-bit and 64-bit applications. 32-bit applications will continue to operate as always. For 64-bit processors, vImage accepts images with buffers larger than 4 gigapixels wide or tall (or both) and passes data with 64-bit pointers.

vImage uses several opaque data types to simplify handling raw image data. Most of the data types are just typedefs for `int` or `float` arrays. If you are writing shared source code that targets both the 32-bit and 64-bit architectures, you should be careful about your use of types with vImage. Some types in vImage change size between the two architectures, most notably `vImage_Error`, `size_t`, `vImagePixelCount`, anything with type `long` or `unsigned long`, and of course, pointers. These types are 64 bits in 64-bit architectures, and 32 bits for the 32-bit architecture. You should make sure that your own types grow and shrink accordingly to avoid truncation. Special care should be taken with data that might be transferred between architectures such as data stored to disk or sent over the network. See _[vImage Data Types and Constants Reference](https://developer.apple.com/documentation/accelerate/vimage/data_types_and_constants)_ for more information.

For more information on 64-bit programming in OS X, see _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_.

[Next](Performing%20Convolution%20Operations.md)[Previous](Introduction%20to%20vImage%20Programming%20Guide.md)
