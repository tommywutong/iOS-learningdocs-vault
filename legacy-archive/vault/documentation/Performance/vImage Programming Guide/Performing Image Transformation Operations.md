---
title: vImage Programming Guide
apple_id: TP30001001
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Accelerate
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vImage/ImageTransformationOperations/ImageTransformationOperations.html
archived_at: '2026-07-27T06:57:05.607870Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [vImage Programming Guide](Introduction%20to%20vImage%20Programming%20Guide.md)


[Next](Best%20Practices%20for%20Using%20vImage.md)[Previous](Performing%20Alpha%20Compositing%20Operations.md)

# Performing Image Transformation Operations

Image transformation operations alter the values of pixels in an image as defined by custom functions provided as a callback. Unlike convolution operations, transformation functions do not depend on the values of neighboring pixels.

Developers who are interested in efficiently performing gamma corrections or custom pixel manipulation functions on large or real-time image will find these functions useful. With vImage, you can use image transformation operations on the following sorts of functions:

- Gamma correction functions
- Functions that use lookup tables to determine destination pixel value
- Matrix multiplication functions
- Piecewise functions that allow you provide custom polynomial functions

This chapters describes the principles of image transformation and shows you how to use the functions provided by vImage. By reading this chapter you will learn how to:

- Correct images using pre-defined gamma functions
- Transform an image using a lookup table
- Apply polynomials and matrix multiplication to an image

## Transformation Operations

Image transformation functions fall into four categories:

- Gamma correction functions correct the brightness profile of an image by multiplying each pixel by the value of the function. Gamma correction prepares an image for display or printing on a particular device.
- Lookup table functions are like the piecewise polynomial functions, but instead of applying a polynomial they use a lookup table that you supply.
- Matrix multiplication functions have a variety of uses, such as to convert between color spaces (RGB and YUV, for example), change a color image to a grayscale one, and perform “colortwisting.”
- Piecewise functions are similar to the gamma correction functions, but instead of applying a predefined gamma function they apply one or more polynomials that you supply. The number of polynomials must be an integer power of 2, and they must all be of the same order.

Transformation functions use a `vImage_Buffer` structure to receive and supply image data. This buffer contains a pointer to image data, the height and width (in pixels) of the image data, and the number of row bytes.

Some transformation functions work in place. That is, the source and destination images can occupy the same memory if they are strictly aligned pixel for pixel. For these, you can provide a pointer to the same `vImage_Buffer` structure for one of the source images and the destination image.

## Gamma Correction

Gamma corrections have to do with changing the intensities of the pixels in an image such that it corrects for the eye’s uneven response to certain colors in an image display. The overall goal of gamma correction is to ensure an accurate depiction of an image given its display’s limited signal range, (such as the number of bits in each pixel).

When vImage performs a gamma correction on an image, it takes each pixel of the source image and passes its intensity through a pre-defined gamma function, and saves this resultant (gamma-corrected) pixel intensity in the destination image.

## Using Lookup Tables

You can use a lookup table to apply custom image transformations to an image. By providing an array of 256 integers (for integer pixel types) or 4096 values representing the intensity of floating-point pixel types, you define the destination pixel intensity for each potential source pixel intensity. When vImage transforms an image according to a lookup table, it takes each pixel intensity in the image, indexes into the corresponding array element for that intensity, and saves the intensity stored at that position in the array as the destination pixel intensity.

[Listing 7-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrqhewvgvzs) shows how to use a lookup table to apply a custom image transformation.

__Listing 7-1__  Transforming an image using a lookup table

```
int MyLookup(void *inData, unsigned int inRowBytes, void *outData, unsigned int outRowBytes, unsigned int height, unsigned int width, void *table, unsigned int table_height, unsigned int table_width, int divisor, vImage_Flags flags )
{
    vImage_Buffer    in = { inData, height, width, inRowBytes }; // 1
    vImage_Buffer    out = { outData, height, width, outRowBytes }; // 2

    if( table_height != 1 || table_width != 256 ) // 3
        return kvImageInvalidKernelSize;

    return vImageTableLookUp_Planar8(&in, &out, table, flags); // 4

}
```

1. Declares a `vImage_Buffer` data structure for the source image information. Image data is received as an array of bytes (`inData`). The other members store the height, width, and bytes-per-row of the image. This data allows vImage to know how large the image data array is, and how to properly handle it.
2. Declares `vImage_Buffer` data structure for the destination image information as done previously with the source image.
3. Checks to make sure that size of the lookup table is suitable for the `Planar8` pixel type.
4. Performs the actual vImage function call and passes up potential errors.

## Using Matrix Multiplication

Using matrix multiplication is similar to using a lookup table to determine the destination pixel intensity, except that vImage multiplies each pixel intensity by a specific matrix that you provide. vImage multiplies each pixel intensity by the same matrix to perform this type of transformation. The format of the matrix is a 1D array of 4x4 `int16_t` data types for integer pixel types, and a 1D array of 4x4 `float` data types for float pixel types.

vImage provides the following functions for performing pixel-matrix multiplication:

- [vImageMatrixMultiply_Planar8](https://developer.apple.com/documentation/accelerate/1544331-vimagematrixmultiply_planar8)
- [vImageMatrixMultiply_PlanarF](https://developer.apple.com/documentation/accelerate/1545687-vimagematrixmultiply_planarf)
- [vImageMatrixMultiply_ARGB8888](https://developer.apple.com/documentation/accelerate/1546176-vimagematrixmultiply_argb8888)
- [vImageMatrixMultiply_ARGBFFFF](https://developer.apple.com/documentation/accelerate/1545863-vimagematrixmultiply_argbffff)

## Using Polynomials

You can provide a polynomial function for vImage to apply to each pixel intensity of a given image. You define the polynomial by deciding upon its __order__, and then providing an array of __coefficients__ (with order - 1 coefficients). You also need to decide the boundary values for separating adjacent ranges of pixel values. This determines how vImage should truncate and/or clip the pixel intensities. You can use polynomials to serve as approximations for other functions that are to expensive to calculate. Imagine a polynomial curve fitting in a data plotting application, except that you are fitting a polynomial to a continuous function rather than a series of discrete data. You can usually create a polynomial with some number of terms that closely matches the function that you want (e.g. sine, power, etc.) over a limited range.

Additionally, vImage supports using piecewise polynomials to transform an image. In order to fit a particular curve over the entire range of possible input pixel values, it is sometimes necessary to use multiple polynomials that fit contiguous subregions of the expected input gamut. For example, if you expect all pixels to be in the range [0, 1.0], you might have one polynomial good for inputs in the range [0, 0.5], and one for [0.5, 1.0]. You may have any number of polynomials, so long as that number is an exact power of two. in order to enforce this requirement, vImage receives this value as the `log2segments` parameter — the polynomial count. For example, if you say that your function is the head-to-tail concatenation of eight polynomials, the number you should pass in the `log2segments` parameter should be 3 (because log2(8) = 3).

vImage provides the following functions for using piecewise polynomials to transform images:

- `vImagePieceWisePolynomial_PlanarF`
- `vImagePieceWisePolynomial_Planar8ToPlanarF`
- `vImagePieceWisePolynomial_PlanarFToPlanar8`
- [vImagePiecewiseRational_PlanarF](https://developer.apple.com/documentation/accelerate/1545831-vimagepiecewiserational_planarf)

[Next](Best%20Practices%20for%20Using%20vImage.md)[Previous](Performing%20Alpha%20Compositing%20Operations.md)
