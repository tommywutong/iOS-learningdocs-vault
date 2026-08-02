---
title: vImage Programming Guide
apple_id: TP30001001
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Accelerate
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vImage/Glossary/Glossary.html
archived_at: '2026-07-27T06:57:05.633644Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [vImage Programming Guide](Introduction%20to%20vImage%20Programming%20Guide.md)


[Next](Vector%20Programming%20Primer.md)[Previous](Best%20Practices%20for%20Using%20vImage.md)

# Glossary

- __Accelerate framework__

  An OS X framework that serves as a container for several other frameworks related to optimization and high performance.

- __affine warp__

  A transform that changes the distance between points by a linear transformation followed by a translation.

  An affine warp retains parallel lines, collinearity of points, and the ratio between collinear line segments, but does not preserve absolute length or angle measurements.

  Some common affine warps include scaling, shearing, rotation, and translation.

- __alpha channel__

  A channel dedicated to representing how opaque a given pixel is. Unlike the red, green, and blue channels, which specify the intensity of their respective colors, the alpha channel specifies the opacity of the entire pixel.

  For example, if a pixel was defined using `float` values ranging from 0.0 to 1.0, an alpha channel intensity of 1.0 would indicate 100% opacity, while an intensity of 0.0 would indicate 0% opacity, or transparent.

- __convolution__

  A common image processing technique that changes the intensities of a pixel to reflect the intensities of the surrounding pixels. Using convolution, you can get image effects like blur, emboss, and sharpen.

- __cache__

  A special type of memory that is substantially faster than typical main memory (RAM). When a program asks the CPU to read or write data in memory, it first checks to see if this data is stored in cache memory (since it will be a lot faster to retrieve or write). Cache sizes are usually quite small though, (under 2 MB) so in order to make use of it, the data must be small enough to fit in the cache.

- __coefficient__

  The number that is multiplied to each of the factors in a polynomial equation. For example, in the equation _x2 + 2x + 1_, the coefficients are _1_, _2_, and _1_.

- __dilation__

  An effect that takes each bright pixel in the source image and expands it into the shape of the kernel, flipped horizontally and vertically. The contribution of the source pixel to the kernel-shaped region depends on two things: the brightness of the source pixel (brighter pixels contribute more) and the values of the kernel pixels (pixels that are dark, relative to the center of the kernel, contribute more to their locations in the kernel-shaped region than pixels that are bright).

- __erosion__

  A morphological operation that is similar to dilation. It takes dark pixels in an image and spreads them around, causing them to “eat away” (or erode) objects in an image.

- __equalization__

  A histogram operation that makes the resultant image conform to a uniform histogram, ensuring an equal frequency of pixel intensities.

- __filter__

  An image process that when applied to an image causes its appearance to change. Many filters use kernel convolution to achieve their effect. Emboss, blur, smooth, and edge detect are all examples of common image filters that use convolution kernels.

- __gamma correction__

  an operation that changes color intensity values to correct for the nonlinear response of the eye or of a display.

- __histogram__

  A diagram that shows the frequency of occurrences within a data set. In the graphics domain, histograms can be used to plot the frequencies of certain pixel intensities.

- __horizontal reflect__

  A type of geometric operation that reflects an image about its y-axis.

- __horizontal shear__

  A filter that shifts pixels along the x-axis to create an effect that’s similar to physical shearing.

- __image format__

  An image encoding standard that specifies the number of color channels and number of bits per channel.

- __interleaved image format__

  A format that encodes each color (and alpha) channel, one after the other, for every pixel. In contrast to planar image formats which encode an entire image using one color at a time, interleaved image formats alternate through each channel, encoding data for all channels simultaneously within each pixel. For example, an interleaved image would encode an image in a RGBRGBRGB fashion, where as a planar image would encode the same image as RRRGGGBBB.

- __kernel__

  A grid of numbers used in both convolution and morphological operations (such as dilation and erosion). It is typically represented as a square grid (or matrix) whose height and width are both odd, such as a 3 x 3 grid. Each cell in the grid contains a number. An image process that uses a kernel typically takes these numbers within the kernel and applies them to the image by undergoing a series of arithmetic operations between the kernel values and the image pixel intensity values.

- __Lanczos resampling__

  A commonly used math routine for resampling values in a data set. vImage uses this as a default technique for determining new pixels that did not previously exist in the input image.

- __lookup table__

  A data structure used to quickly make computations or retrievals of certain values. In image processing it is used to store precalculated values of an equation instead of calculating the value each time it is requested. For example, if the equation is _y = 2x_, and you know that there are at most _n_ distinct values, then you can create an array of size n (one for each input), that stores the precalculated value of the equation for the corresponding input (e.g. `[0] = 0, [1] = 2, [2] = 4, ... [n] = 2n`).

- __matrix__

  A collection of numbers arranged in a grid. It can be thought of as the mathematical equivalent of a two-dimensional array. Much like two-dimensional arrays, matrices are composed of rows and columns with their elements referred to as _cells_.

- __non-premultiplied__

  A technique for processing the alpha channel of a pixel. Instead of performing the alpha blend for each pixel, the alpha value is premultiplied to each of the other color channel values for that pixel. The pixel can then be interpreted as is from then on since all of the color channel values have been appropriately changed to reflect the alpha component.

- __object__

  A group of bright, high-intensity pixels in an image, as opposed to the darker pixels, which are considered part of the background.

- __order__

  The maximum number of factors in an equation. For example, the equation _x_2 _+ x + 1_ has an order of 3 because there are three distinct factors in the equation (_x_2, _x_, and _x_0).

- __planar image format__

  A format that encodes a color channel. Planar images tend to be faster to operate on than nonplanar images because operations do not need to be repeated for each color channel. A grayscale image is an example of a planar image since it encodes only one (black and white) channel.

- __polynomial function__

  An equation commonly used for transforming pixel intensities in an image that is a summation of n factors and coefficients in the form of _ax_n _+ bx_n_—1 + ... cx_0.

- __premultiplied__

  A pixel that already has its intensity levels appropriately multiplied by the alpha value.

- __Quartz__

  The 2D graphics technology used throughout OS X and in most Cocoa applications.

- __region of interest (ROI)__

  The portion of an image data buffer that is being operated upon by a function. It is not uncommon to allocate a large pixel buffer to hold several images and then process only the smaller regions of interest when need be.

- __resampling__

  An operation that changes the dimensions of an image.

- __resampling filter__

  A function used to determine new pixel values for an image that has its dimensions changed somehow.

- __rotation__

  An operation to rotate an image by a certain number of degrees.

- __scale__

  To shrink or enlarge an image by a certain percent.

- __scalar programming__

  A programming paradigm in which values are operated upon individually. Scalar programming is more common than [vector code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrrgawvgvzr).

- __SIMD__

  Single Instruction, Multiple Data. A computing technique used to achieve data level parallelism. Commonly employed in vector processors, this technique allows for multiple data elements to be processed in a single CPU instruction.

- __SSE__

  Streaming SIMD Extensions. Intel’s SIMD instruction set.

- __vector__

  A grouped series of numbers. Commonly represented either as a row of numbers [1, 2, 3, 4] or a column of numbers. It is analogous to an array.

- __vector processor__

  A processor that can perform arithmetic on several pairs of numbers simultaneously. Also called an _array processor_.

- __vector code__

  Code makes use of available on-board vector processors. vImage uses vector code.

- __vertical reflect__

  A type of geometric operation that reflects an image about its x-axis.

- __vertical shear__

  A filter that shifts pixels along the y-axis to create an effect that’s similar to physical shearing.

[Next](Vector%20Programming%20Primer.md)[Previous](Best%20Practices%20for%20Using%20vImage.md)
