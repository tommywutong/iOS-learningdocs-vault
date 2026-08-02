---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/Accelerate.html
archived_at: '2026-07-18T02:56:29.429931Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Accelerate Changes for Objective-C

### Accelerate

#### Alpha.h

Added [vImagePremultipliedAlphaBlendDarken_RGBA8888()](https://developer.apple.com/documentation/accelerate/1410644-vimagepremultipliedalphablenddar)Added [vImagePremultipliedAlphaBlendLighten_RGBA8888()](https://developer.apple.com/documentation/accelerate/1410672-vimagepremultipliedalphablendlig)Added [vImagePremultipliedAlphaBlendMultiply_RGBA8888()](https://developer.apple.com/documentation/accelerate/1410664-vimagepremultipliedalphablendmul)Added [vImagePremultipliedAlphaBlendScreen_RGBA8888()](https://developer.apple.com/documentation/accelerate/1410729-vimagepremultipliedalphablendscr)

#### Convolution.h

Modified [vImageBoxConvolve_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515945-vimageboxconvolve_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageBoxConvolve_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     uint32_t kernel_height,     uint32_t kernel_width,     Pixel_8888 backgroundColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageBoxConvolve_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     uint32_t kernel_height,     uint32_t kernel_width,     const Pixel_8888 backgroundColor,     vImage_Flags flags ); ``` |

Modified [vImageConvolve_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515923-vimageconvolve_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageConvolve_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const int16_t *kernel,     uint32_t kernel_height,     uint32_t kernel_width,     int32_t divisor,     Pixel_8888 backgroundColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageConvolve_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const int16_t *kernel,     uint32_t kernel_height,     uint32_t kernel_width,     int32_t divisor,     const Pixel_8888 backgroundColor,     vImage_Flags flags ); ``` |

Modified [vImageConvolve_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1515929-vimageconvolve_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageConvolve_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const float *kernel,     uint32_t kernel_height,     uint32_t kernel_width,     Pixel_FFFF backgroundColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageConvolve_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const float *kernel,     uint32_t kernel_height,     uint32_t kernel_width,     const Pixel_FFFF backgroundColor,     vImage_Flags flags ); ``` |

Modified [vImageConvolveMultiKernel_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515930-vimageconvolvemultikernel_argb88)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageConvolveMultiKernel_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const int16_t *kernels[4],     uint32_t kernel_height,     uint32_t kernel_width,     const int32_t divisors[4],     const int32_t biases[4],     Pixel_8888 backgroundColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageConvolveMultiKernel_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const int16_t *kernels[4],     uint32_t kernel_height,     uint32_t kernel_width,     const int32_t divisors[4],     const int32_t biases[4],     const Pixel_8888 backgroundColor,     vImage_Flags flags ); ``` |

Modified [vImageConvolveMultiKernel_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1515931-vimageconvolvemultikernel_argbff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageConvolveMultiKernel_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const float *kernels[4],     uint32_t kernel_height,     uint32_t kernel_width,     const float biases[4],     Pixel_FFFF backgroundColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageConvolveMultiKernel_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const float *kernels[4],     uint32_t kernel_height,     uint32_t kernel_width,     const float biases[4],     const Pixel_FFFF backgroundColor,     vImage_Flags flags ); ``` |

Modified [vImageConvolveWithBias_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515933-vimageconvolvewithbias_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageConvolveWithBias_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const int16_t *kernel,     uint32_t kernel_height,     uint32_t kernel_width,     int32_t divisor,     int32_t bias,     Pixel_8888 backgroundColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageConvolveWithBias_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const int16_t *kernel,     uint32_t kernel_height,     uint32_t kernel_width,     int32_t divisor,     int32_t bias,     const Pixel_8888 backgroundColor,     vImage_Flags flags ); ``` |

Modified [vImageConvolveWithBias_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1515924-vimageconvolvewithbias_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageConvolveWithBias_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const float *kernel,     uint32_t kernel_height,     uint32_t kernel_width,     float bias,     Pixel_FFFF backgroundColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageConvolveWithBias_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const float *kernel,     uint32_t kernel_height,     uint32_t kernel_width,     float bias,     const Pixel_FFFF backgroundColor,     vImage_Flags flags ); ``` |

Modified [vImageRichardsonLucyDeConvolve_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515928-vimagerichardsonlucydeconvolve_a)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageRichardsonLucyDeConvolve_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const int16_t *kernel,     const int16_t *kernel2,     uint32_t kernel_height,     uint32_t kernel_width,     uint32_t kernel_height2,     uint32_t kernel_width2,     int32_t divisor,     int32_t divisor2,     Pixel_8888 backgroundColor,     uint32_t iterationCount,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageRichardsonLucyDeConvolve_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const int16_t *kernel,     const int16_t *kernel2,     uint32_t kernel_height,     uint32_t kernel_width,     uint32_t kernel_height2,     uint32_t kernel_width2,     int32_t divisor,     int32_t divisor2,     const Pixel_8888 backgroundColor,     uint32_t iterationCount,     vImage_Flags flags ); ``` |

Modified [vImageRichardsonLucyDeConvolve_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1515927-vimagerichardsonlucydeconvolve_a)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageRichardsonLucyDeConvolve_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const float *kernel,     const float *kernel2,     uint32_t kernel_height,     uint32_t kernel_width,     uint32_t kernel_height2,     uint32_t kernel_width2,     Pixel_FFFF backgroundColor,     uint32_t iterationCount,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageRichardsonLucyDeConvolve_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     const float *kernel,     const float *kernel2,     uint32_t kernel_height,     uint32_t kernel_width,     uint32_t kernel_height2,     uint32_t kernel_width2,     const Pixel_FFFF backgroundColor,     uint32_t iterationCount,     vImage_Flags flags ); ``` |

Modified [vImageTentConvolve_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515935-vimagetentconvolve_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageTentConvolve_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     uint32_t kernel_height,     uint32_t kernel_width,     Pixel_8888 backgroundColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageTentConvolve_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     uint32_t kernel_height,     uint32_t kernel_width,     const Pixel_8888 backgroundColor,     vImage_Flags flags ); ``` |

#### Geometry.h

Modified [vImageAffineWarp_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509164-vimageaffinewarp_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarp_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform *transform,     Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarp_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform *transform,     const Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarp_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509156-vimageaffinewarp_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarp_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform *transform,     Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarp_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform *transform,     const Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarp_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509182-vimageaffinewarp_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarp_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform *transform,     Pixel_8888 backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarp_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform *transform,     const Pixel_8888 backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarp_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509245-vimageaffinewarp_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarp_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform *transform,     Pixel_FFFF backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarp_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform *transform,     const Pixel_FFFF backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarpCG_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509246-vimageaffinewarpcg_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarpCG_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_CGAffineTransform *transform,     Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarpCG_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_CGAffineTransform *transform,     const Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarpCG_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509186-vimageaffinewarpcg_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarpCG_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_CGAffineTransform *transform,     Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarpCG_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_CGAffineTransform *transform,     const Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarpCG_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509276-vimageaffinewarpcg_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarpCG_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_CGAffineTransform *transform,     Pixel_8888 backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarpCG_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_CGAffineTransform *transform,     const Pixel_8888 backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarpCG_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509263-vimageaffinewarpcg_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarpCG_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_CGAffineTransform *transform,     Pixel_FFFF backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarpCG_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_CGAffineTransform *transform,     const Pixel_FFFF backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarpD_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509282-vimageaffinewarpd_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarpD_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform_Double *transform,     Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarpD_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform_Double *transform,     const Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarpD_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509292-vimageaffinewarpd_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarpD_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform_Double *transform,     Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarpD_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform_Double *transform,     const Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarpD_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509211-vimageaffinewarpd_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarpD_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform_Double *transform,     Pixel_8888 backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarpD_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform_Double *transform,     const Pixel_8888 backColor,     vImage_Flags flags ); ``` |

Modified [vImageAffineWarpD_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509214-vimageaffinewarpd_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageAffineWarpD_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform_Double *transform,     Pixel_FFFF backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageAffineWarpD_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     const vImage_AffineTransform_Double *transform,     const Pixel_FFFF backColor,     vImage_Flags flags ); ``` |

Modified [vImageHorizontalShear_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509194-vimagehorizontalshear_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageHorizontalShear_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float xTranslate,     float shearSlope,     ResamplingFilter filter,     Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageHorizontalShear_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float xTranslate,     float shearSlope,     ResamplingFilter filter,     const Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |

Modified [vImageHorizontalShear_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509274-vimagehorizontalshear_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageHorizontalShear_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float xTranslate,     float shearSlope,     ResamplingFilter filter,     Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageHorizontalShear_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float xTranslate,     float shearSlope,     ResamplingFilter filter,     const Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |

Modified [vImageHorizontalShear_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509237-vimagehorizontalshear_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageHorizontalShear_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float xTranslate,     float shearSlope,     ResamplingFilter filter,     Pixel_8888 backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageHorizontalShear_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float xTranslate,     float shearSlope,     ResamplingFilter filter,     const Pixel_8888 backColor,     vImage_Flags flags ); ``` |

Modified [vImageHorizontalShear_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509273-vimagehorizontalshear_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageHorizontalShear_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float xTranslate,     float shearSlope,     ResamplingFilter filter,     Pixel_FFFF backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageHorizontalShear_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float xTranslate,     float shearSlope,     ResamplingFilter filter,     const Pixel_FFFF backColor,     vImage_Flags flags ); ``` |

Modified [vImageHorizontalShearD_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509268-vimagehorizontalsheard_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageHorizontalShearD_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double xTranslate,     double shearSlope,     ResamplingFilter filter,     Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageHorizontalShearD_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double xTranslate,     double shearSlope,     ResamplingFilter filter,     const Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |

Modified [vImageHorizontalShearD_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509248-vimagehorizontalsheard_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageHorizontalShearD_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double xTranslate,     double shearSlope,     ResamplingFilter filter,     Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageHorizontalShearD_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double xTranslate,     double shearSlope,     ResamplingFilter filter,     const Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |

Modified [vImageHorizontalShearD_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509178-vimagehorizontalsheard_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageHorizontalShearD_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double xTranslate,     double shearSlope,     ResamplingFilter filter,     Pixel_8888 backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageHorizontalShearD_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double xTranslate,     double shearSlope,     ResamplingFilter filter,     const Pixel_8888 backColor,     vImage_Flags flags ); ``` |

Modified [vImageHorizontalShearD_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509269-vimagehorizontalsheard_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageHorizontalShearD_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double xTranslate,     double shearSlope,     ResamplingFilter filter,     Pixel_FFFF backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageHorizontalShearD_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double xTranslate,     double shearSlope,     ResamplingFilter filter,     const Pixel_FFFF backColor,     vImage_Flags flags ); ``` |

Modified [vImageRotate_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509206-vimagerotate_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageRotate_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     float angleInRadians,     Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageRotate_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     float angleInRadians,     const Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |

Modified [vImageRotate_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509235-vimagerotate_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageRotate_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     float angleInRadians,     Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageRotate_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     float angleInRadians,     const Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |

Modified [vImageRotate_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509284-vimagerotate_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageRotate_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     float angleInRadians,     Pixel_8888 backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageRotate_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     float angleInRadians,     const Pixel_8888 backColor,     vImage_Flags flags ); ``` |

Modified [vImageRotate_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509192-vimagerotate_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageRotate_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     float angleInRadians,     Pixel_FFFF backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageRotate_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     void *tempBuffer,     float angleInRadians,     const Pixel_FFFF backColor,     vImage_Flags flags ); ``` |

Modified [vImageVerticalShear_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509154-vimageverticalshear_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageVerticalShear_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float yTranslate,     float shearSlope,     ResamplingFilter filter,     Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageVerticalShear_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float yTranslate,     float shearSlope,     ResamplingFilter filter,     const Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |

Modified [vImageVerticalShear_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509227-vimageverticalshear_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageVerticalShear_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float yTranslate,     float shearSlope,     ResamplingFilter filter,     Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageVerticalShear_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float yTranslate,     float shearSlope,     ResamplingFilter filter,     const Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |

Modified [vImageVerticalShear_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509256-vimageverticalshear_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageVerticalShear_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float yTranslate,     float shearSlope,     ResamplingFilter filter,     Pixel_8888 backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageVerticalShear_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float yTranslate,     float shearSlope,     ResamplingFilter filter,     const Pixel_8888 backColor,     vImage_Flags flags ); ``` |

Modified [vImageVerticalShear_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509261-vimageverticalshear_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageVerticalShear_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float yTranslate,     float shearSlope,     ResamplingFilter filter,     Pixel_FFFF backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageVerticalShear_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     float yTranslate,     float shearSlope,     ResamplingFilter filter,     const Pixel_FFFF backColor,     vImage_Flags flags ); ``` |

Modified [vImageVerticalShearD_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509278-vimageverticalsheard_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageVerticalShearD_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double yTranslate,     double shearSlope,     ResamplingFilter filter,     Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageVerticalShearD_ARGB16S (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double yTranslate,     double shearSlope,     ResamplingFilter filter,     const Pixel_ARGB_16S backColor,     vImage_Flags flags ); ``` |

Modified [vImageVerticalShearD_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509225-vimageverticalsheard_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageVerticalShearD_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double yTranslate,     double shearSlope,     ResamplingFilter filter,     Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageVerticalShearD_ARGB16U (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double yTranslate,     double shearSlope,     ResamplingFilter filter,     const Pixel_ARGB_16U backColor,     vImage_Flags flags ); ``` |

Modified [vImageVerticalShearD_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509222-vimageverticalsheard_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageVerticalShearD_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double yTranslate,     double shearSlope,     ResamplingFilter filter,     Pixel_8888 backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageVerticalShearD_ARGB8888 (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double yTranslate,     double shearSlope,     ResamplingFilter filter,     const Pixel_8888 backColor,     vImage_Flags flags ); ``` |

Modified [vImageVerticalShearD_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509254-vimageverticalsheard_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` vImage_Error vImageVerticalShearD_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double yTranslate,     double shearSlope,     ResamplingFilter filter,     Pixel_FFFF backColor,     vImage_Flags flags ); ``` |
| To | ``` vImage_Error vImageVerticalShearD_ARGBFFFF (     const vImage_Buffer *src,     const vImage_Buffer *dest,     vImagePixelCount srcOffsetToROI_X,     vImagePixelCount srcOffsetToROI_Y,     double yTranslate,     double shearSlope,     ResamplingFilter filter,     const Pixel_FFFF backColor,     vImage_Flags flags ); ``` |

#### LinearAlgebra/object.h

Modified OS_la_object

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSObject |

#### Sparse/BLAS.h (Added)

Added [sparse_commit()](https://developer.apple.com/documentation/accelerate/1545870-sparse_commit)Added [sparse_elementwise_norm_double()](https://developer.apple.com/documentation/accelerate/1546486-sparse_elementwise_norm_double)Added [sparse_elementwise_norm_float()](https://developer.apple.com/documentation/accelerate/1544954-sparse_elementwise_norm_float)Added [sparse_extract_block_double()](https://developer.apple.com/documentation/accelerate/1544385-sparse_extract_block_double)Added [sparse_extract_block_float()](https://developer.apple.com/documentation/accelerate/1545554-sparse_extract_block_float)Added [sparse_extract_sparse_column_double()](https://developer.apple.com/documentation/accelerate/1545309-sparse_extract_sparse_column_dou)Added [sparse_extract_sparse_column_float()](https://developer.apple.com/documentation/accelerate/1544689-sparse_extract_sparse_column_flo)Added [sparse_extract_sparse_row_double()](https://developer.apple.com/documentation/accelerate/1545736-sparse_extract_sparse_row_double)Added [sparse_extract_sparse_row_float()](https://developer.apple.com/documentation/accelerate/1546148-sparse_extract_sparse_row_float)Added [sparse_get_block_dimension_for_col()](https://developer.apple.com/documentation/accelerate/1546658-sparse_get_block_dimension_for_c)Added [sparse_get_block_dimension_for_row()](https://developer.apple.com/documentation/accelerate/1546661-sparse_get_block_dimension_for_r)Added [sparse_get_matrix_nonzero_count()](https://developer.apple.com/documentation/accelerate/1546682-sparse_get_matrix_nonzero_count)Added [sparse_get_matrix_nonzero_count_for_column()](https://developer.apple.com/documentation/accelerate/1545287-sparse_get_matrix_nonzero_count_)Added [sparse_get_matrix_nonzero_count_for_row()](https://developer.apple.com/documentation/accelerate/1546965-sparse_get_matrix_nonzero_count_)Added [sparse_get_matrix_number_of_columns()](https://developer.apple.com/documentation/accelerate/1544948-sparse_get_matrix_number_of_colu)Added [sparse_get_matrix_number_of_rows()](https://developer.apple.com/documentation/accelerate/1546683-sparse_get_matrix_number_of_rows)Added [sparse_get_matrix_property()](https://developer.apple.com/documentation/accelerate/1545269-sparse_get_matrix_property)Added [sparse_get_vector_nonzero_count_double()](https://developer.apple.com/documentation/accelerate/1545336-sparse_get_vector_nonzero_count_)Added [sparse_get_vector_nonzero_count_float()](https://developer.apple.com/documentation/accelerate/1546927-sparse_get_vector_nonzero_count_)Added [sparse_inner_product_dense_double()](https://developer.apple.com/documentation/accelerate/1544388-sparse_inner_product_dense_doubl)Added [sparse_inner_product_dense_float()](https://developer.apple.com/documentation/accelerate/1544780-sparse_inner_product_dense_float)Added [sparse_inner_product_sparse_double()](https://developer.apple.com/documentation/accelerate/1546608-sparse_inner_product_sparse_doub)Added [sparse_inner_product_sparse_float()](https://developer.apple.com/documentation/accelerate/1545123-sparse_inner_product_sparse_floa)Added [sparse_insert_block_double()](https://developer.apple.com/documentation/accelerate/1546050-sparse_insert_block_double)Added [sparse_insert_block_float()](https://developer.apple.com/documentation/accelerate/1544469-sparse_insert_block_float)Added [sparse_insert_col_double()](https://developer.apple.com/documentation/accelerate/1546659-sparse_insert_col_double)Added [sparse_insert_col_float()](https://developer.apple.com/documentation/accelerate/1545348-sparse_insert_col_float)Added [sparse_insert_entries_double()](https://developer.apple.com/documentation/accelerate/1546631-sparse_insert_entries_double)Added [sparse_insert_entries_float()](https://developer.apple.com/documentation/accelerate/1546585-sparse_insert_entries_float)Added [sparse_insert_entry_double()](https://developer.apple.com/documentation/accelerate/1546876-sparse_insert_entry_double)Added [sparse_insert_entry_float()](https://developer.apple.com/documentation/accelerate/1546606-sparse_insert_entry_float)Added [sparse_insert_row_double()](https://developer.apple.com/documentation/accelerate/1545913-sparse_insert_row_double)Added [sparse_insert_row_float()](https://developer.apple.com/documentation/accelerate/1545432-sparse_insert_row_float)Added [sparse_matrix_block_create_double()](https://developer.apple.com/documentation/accelerate/1546690-sparse_matrix_block_create_doubl)Added [sparse_matrix_block_create_float()](https://developer.apple.com/documentation/accelerate/1544775-sparse_matrix_block_create_float)Added [sparse_matrix_create_double()](https://developer.apple.com/documentation/accelerate/1544642-sparse_matrix_create_double)Added [sparse_matrix_create_float()](https://developer.apple.com/documentation/accelerate/1546996-sparse_matrix_create_float)Added [sparse_matrix_destroy()](https://developer.apple.com/documentation/accelerate/1546691-sparse_matrix_destroy)Added [sparse_matrix_product_dense_double()](https://developer.apple.com/documentation/accelerate/1546216-sparse_matrix_product_dense_doub)Added [sparse_matrix_product_dense_float()](https://developer.apple.com/documentation/accelerate/1545734-sparse_matrix_product_dense_floa)Added [sparse_matrix_trace_double()](https://developer.apple.com/documentation/accelerate/1544239-sparse_matrix_trace_double)Added [sparse_matrix_trace_float()](https://developer.apple.com/documentation/accelerate/1545041-sparse_matrix_trace_float)Added [sparse_matrix_triangular_solve_dense_double()](https://developer.apple.com/documentation/accelerate/1544750-sparse_matrix_triangular_solve_d)Added [sparse_matrix_triangular_solve_dense_float()](https://developer.apple.com/documentation/accelerate/1546684-sparse_matrix_triangular_solve_d)Added [sparse_matrix_variable_block_create_double()](https://developer.apple.com/documentation/accelerate/1546650-sparse_matrix_variable_block_cre)Added [sparse_matrix_variable_block_create_float()](https://developer.apple.com/documentation/accelerate/1546234-sparse_matrix_variable_block_cre)Added [sparse_matrix_vector_product_dense_double()](https://developer.apple.com/documentation/accelerate/1546125-sparse_matrix_vector_product_den)Added [sparse_matrix_vector_product_dense_float()](https://developer.apple.com/documentation/accelerate/1545507-sparse_matrix_vector_product_den)Added [sparse_operator_norm_double()](https://developer.apple.com/documentation/accelerate/1546432-sparse_operator_norm_double)Added [sparse_operator_norm_float()](https://developer.apple.com/documentation/accelerate/1546614-sparse_operator_norm_float)Added [sparse_outer_product_dense_double()](https://developer.apple.com/documentation/accelerate/1546587-sparse_outer_product_dense_doubl)Added [sparse_outer_product_dense_float()](https://developer.apple.com/documentation/accelerate/1546589-sparse_outer_product_dense_float)Added [sparse_pack_vector_double()](https://developer.apple.com/documentation/accelerate/1544402-sparse_pack_vector_double)Added [sparse_pack_vector_float()](https://developer.apple.com/documentation/accelerate/1546385-sparse_pack_vector_float)Added [sparse_permute_cols_double()](https://developer.apple.com/documentation/accelerate/1545537-sparse_permute_cols_double)Added [sparse_permute_cols_float()](https://developer.apple.com/documentation/accelerate/1545945-sparse_permute_cols_float)Added [sparse_permute_rows_double()](https://developer.apple.com/documentation/accelerate/1546664-sparse_permute_rows_double)Added [sparse_permute_rows_float()](https://developer.apple.com/documentation/accelerate/1544648-sparse_permute_rows_float)Added [sparse_set_matrix_property()](https://developer.apple.com/documentation/accelerate/1545140-sparse_set_matrix_property)Added [sparse_unpack_vector_double()](https://developer.apple.com/documentation/accelerate/1545438-sparse_unpack_vector_double)Added [sparse_unpack_vector_float()](https://developer.apple.com/documentation/accelerate/1545010-sparse_unpack_vector_float)Added [sparse_vector_add_with_scale_dense_double()](https://developer.apple.com/documentation/accelerate/1546181-sparse_vector_add_with_scale_den)Added [sparse_vector_add_with_scale_dense_float()](https://developer.apple.com/documentation/accelerate/1544316-sparse_vector_add_with_scale_den)Added [sparse_vector_norm_double()](https://developer.apple.com/documentation/accelerate/1546785-sparse_vector_norm_double)Added [sparse_vector_norm_float()](https://developer.apple.com/documentation/accelerate/1546410-sparse_vector_norm_float)Added [sparse_vector_triangular_solve_dense_double()](https://developer.apple.com/documentation/accelerate/1545435-sparse_vector_triangular_solve_d)Added [sparse_vector_triangular_solve_dense_float()](https://developer.apple.com/documentation/accelerate/1544828-sparse_vector_triangular_solve_d)

#### Sparse/Types.h (Added)

Added [SPARSE_CANNOT_SET_PROPERTY](https://developer.apple.com/documentation/accelerate/sparse_cannot_set_property)Added [sparse_dimension](https://developer.apple.com/documentation/accelerate/sparse_dimension)Added [SPARSE_ILLEGAL_PARAMETER](https://developer.apple.com/documentation/accelerate/sparse_status/sparse_illegal_parameter)Added [sparse_index](https://developer.apple.com/documentation/accelerate/sparse_index)Added [SPARSE_LOWER_SYMMETRIC](https://developer.apple.com/documentation/accelerate/sparse_lower_symmetric)Added [SPARSE_LOWER_TRIANGULAR](https://developer.apple.com/documentation/accelerate/sparse_matrix_property/sparse_lower_triangular)Added [sparse_matrix_double](https://developer.apple.com/documentation/accelerate/sparse_matrix_double)Added [sparse_matrix_float](https://developer.apple.com/documentation/accelerate/sparse_matrix_float)Added [sparse_matrix_property](https://developer.apple.com/documentation/accelerate/sparse_matrix_property)Added [sparse_norm](https://developer.apple.com/documentation/accelerate/sparse_norm)Added [SPARSE_NORM_INF](https://developer.apple.com/documentation/accelerate/sparse_norm/sparse_norm_inf)Added [SPARSE_NORM_ONE](https://developer.apple.com/documentation/accelerate/sparse_norm/sparse_norm_one)Added [SPARSE_NORM_R1](https://developer.apple.com/documentation/accelerate/sparse_norm_r1)Added [SPARSE_NORM_TWO](https://developer.apple.com/documentation/accelerate/sparse_norm/sparse_norm_two)Added [sparse_status](https://developer.apple.com/documentation/accelerate/sparse_status)Added [sparse_stride](https://developer.apple.com/documentation/accelerate/sparse_stride)Added [SPARSE_SUCCESS](https://developer.apple.com/documentation/accelerate/sparse_status/sparse_success)Added [SPARSE_SYSTEM_ERROR](https://developer.apple.com/documentation/accelerate/sparse_status/sparse_system_error)Added [SPARSE_UPPER_SYMMETRIC](https://developer.apple.com/documentation/accelerate/sparse_matrix_property/sparse_upper_symmetric)Added [SPARSE_UPPER_TRIANGULAR](https://developer.apple.com/documentation/accelerate/sparse_matrix_property/sparse_upper_triangular)

#### Transform.h

Added [vImageMatrixMultiply_ARGB8888ToPlanar8()](https://developer.apple.com/documentation/accelerate/1546979-vimagematrixmultiply_argb8888top)Added [vImageMatrixMultiply_ARGBFFFFToPlanarF()](https://developer.apple.com/documentation/accelerate/1546678-vimagematrixmultiply_argbfffftop)Added [vImageSymmetricPiecewisePolynomial_PlanarF()](https://developer.apple.com/documentation/accelerate/1544253-vimagesymmetricpiecewisepolynomi)Modified [vImageMultidimensionalTable_Create()](https://developer.apple.com/documentation/accelerate/1544435-vimagemultidimensionaltable_crea)

|  | Declaration |
| --- | --- |
| From | ``` vImage_MultidimensionalTable vImageMultidimensionalTable_Create (     const uint16_t *tableData,     uint32_t numSrcChannels,     uint32_t numDestChannels,     uint8_t table_entries_per_dimension[],     vImageMDTableUsageHint hint,     vImage_Flags flags,     vImage_Error *err ); ``` |
| To | ``` vImage_MultidimensionalTable vImageMultidimensionalTable_Create (     const uint16_t *tableData,     uint32_t numSrcChannels,     uint32_t numDestChannels,     const uint8_t table_entries_per_dimension[],     vImageMDTableUsageHint hint,     vImage_Flags flags,     vImage_Error *err ); ``` |

#### vDSP.h

Added [vDSP_biquadm_SetActiveFilters()](https://developer.apple.com/documentation/kernel/1579973-vdsp_biquadm_setactivefilters)Added [vDSP_biquadm_SetCoefficientsDouble()](https://developer.apple.com/documentation/accelerate/1450453-vdsp_biquadm_setcoefficientsdoub)Added [vDSP_biquadm_SetCoefficientsSingle()](https://developer.apple.com/documentation/accelerate/1450128-vdsp_biquadm_setcoefficientssing)Added [vDSP_biquadm_SetTargetsDouble()](https://developer.apple.com/documentation/kernel/1580010-vdsp_biquadm_settargetsdouble)Added [vDSP_biquadm_SetTargetsSingle()](https://developer.apple.com/documentation/accelerate/1450077-vdsp_biquadm_settargetssingle)Modified [vDSP_biquad()](https://developer.apple.com/documentation/accelerate/1450838-vdsp_biquad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquad (     const struct vDSP_biquad_SetupStruct *__vDSP_Setup,     float *__vDSP_Delay,     const float *__vDSP_X,     vDSP_Stride __vDSP_IX,     float *__vDSP_Y,     vDSP_Stride __vDSP_IY,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_biquad (     const struct vDSP_biquad_SetupStruct * _Nonnull __Setup,     float * _Nonnull __Delay,     const float * _Nonnull __X,     vDSP_Stride __IX,     float * _Nonnull __Y,     vDSP_Stride __IY,     vDSP_Length __N ); ``` |

Modified [vDSP_biquad_CreateSetup()](https://developer.apple.com/documentation/accelerate/1450374-vdsp_biquad_createsetup)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_biquad_Setup vDSP_biquad_CreateSetup (     const double *__vDSP_Coefficients,     vDSP_Length __vDSP_M ); ``` |
| To | ``` vDSP_biquad_Setup _Nullable vDSP_biquad_CreateSetup (     const double * _Nonnull __Coefficients,     vDSP_Length __M ); ``` |

Modified [vDSP_biquad_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1450239-vdsp_biquad_createsetupd)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_biquad_SetupD vDSP_biquad_CreateSetupD (     const double *__vDSP_Coefficients,     vDSP_Length __vDSP_M ); ``` |
| To | ``` vDSP_biquad_SetupD _Nullable vDSP_biquad_CreateSetupD (     const double * _Nonnull __Coefficients,     vDSP_Length __M ); ``` |

Modified [vDSP_biquad_DestroySetup()](https://developer.apple.com/documentation/accelerate/1450168-vdsp_biquad_destroysetup)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquad_DestroySetup (     vDSP_biquad_Setup __vDSP_setup ); ``` |
| To | ``` void vDSP_biquad_DestroySetup (     vDSP_biquad_Setup _Nullable __setup ); ``` |

Modified [vDSP_biquad_DestroySetupD()](https://developer.apple.com/documentation/accelerate/1450640-vdsp_biquad_destroysetupd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquad_DestroySetupD (     vDSP_biquad_SetupD __vDSP_setup ); ``` |
| To | ``` void vDSP_biquad_DestroySetupD (     vDSP_biquad_SetupD _Nullable __setup ); ``` |

Modified [vDSP_biquadD()](https://developer.apple.com/documentation/accelerate/1450359-vdsp_biquadd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadD (     const struct vDSP_biquad_SetupStructD *__vDSP_Setup,     double *__vDSP_Delay,     const double *__vDSP_X,     vDSP_Stride __vDSP_IX,     double *__vDSP_Y,     vDSP_Stride __vDSP_IY,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_biquadD (     const struct vDSP_biquad_SetupStructD * _Nonnull __Setup,     double * _Nonnull __Delay,     const double * _Nonnull __X,     vDSP_Stride __IX,     double * _Nonnull __Y,     vDSP_Stride __IY,     vDSP_Length __N ); ``` |

Modified [vDSP_biquadm()](https://developer.apple.com/documentation/accelerate/1450603-vdsp_biquadm)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm (     vDSP_biquadm_Setup __vDSP_Setup,     const float **__vDSP_X,     vDSP_Stride __vDSP_IX,     float **__vDSP_Y,     vDSP_Stride __vDSP_IY,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_biquadm (     vDSP_biquadm_Setup _Nonnull __Setup,     const float * _Nonnull * _Nonnull __X,     vDSP_Stride __IX,     float * _Nonnull * _Nonnull __Y,     vDSP_Stride __IY,     vDSP_Length __N ); ``` |

Modified [vDSP_biquadm_CopyState()](https://developer.apple.com/documentation/kernel/1579980-vdsp_biquadm_copystate)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_CopyState (     vDSP_biquadm_Setup __vDSP_dest,     const struct vDSP_biquadm_SetupStruct *__vDSP_src ); ``` |
| To | ``` void vDSP_biquadm_CopyState (     vDSP_biquadm_Setup _Nonnull __dest,     const struct vDSP_biquadm_SetupStruct * _Nonnull __src ); ``` |

Modified [vDSP_biquadm_CopyStateD()](https://developer.apple.com/documentation/kernel/1580000-vdsp_biquadm_copystated)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_CopyStateD (     vDSP_biquadm_SetupD __vDSP_dest,     const struct vDSP_biquadm_SetupStructD *__vDSP_src ); ``` |
| To | ``` void vDSP_biquadm_CopyStateD (     vDSP_biquadm_SetupD _Nonnull __dest,     const struct vDSP_biquadm_SetupStructD * _Nonnull __src ); ``` |

Modified [vDSP_biquadm_CreateSetup()](https://developer.apple.com/documentation/kernel/1579945-vdsp_biquadm_createsetup)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_biquadm_Setup vDSP_biquadm_CreateSetup (     const double *__vDSP_coeffs,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N ); ``` |
| To | ``` vDSP_biquadm_Setup _Nullable vDSP_biquadm_CreateSetup (     const double * _Nonnull __coeffs,     vDSP_Length __M,     vDSP_Length __N ); ``` |

Modified [vDSP_biquadm_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1449719-vdsp_biquadm_createsetupd)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_biquadm_SetupD vDSP_biquadm_CreateSetupD (     const double *__vDSP_coeffs,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N ); ``` |
| To | ``` vDSP_biquadm_SetupD _Nullable vDSP_biquadm_CreateSetupD (     const double * _Nonnull __coeffs,     vDSP_Length __M,     vDSP_Length __N ); ``` |

Modified [vDSP_biquadm_DestroySetup()](https://developer.apple.com/documentation/kernel/1579970-vdsp_biquadm_destroysetup)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_DestroySetup (     vDSP_biquadm_Setup __vDSP_setup ); ``` |
| To | ``` void vDSP_biquadm_DestroySetup (     vDSP_biquadm_Setup _Nonnull __setup ); ``` |

Modified [vDSP_biquadm_DestroySetupD()](https://developer.apple.com/documentation/accelerate/1450779-vdsp_biquadm_destroysetupd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_DestroySetupD (     vDSP_biquadm_SetupD __vDSP_setup ); ``` |
| To | ``` void vDSP_biquadm_DestroySetupD (     vDSP_biquadm_SetupD _Nonnull __setup ); ``` |

Modified [vDSP_biquadm_ResetState()](https://developer.apple.com/documentation/accelerate/1449898-vdsp_biquadm_resetstate)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_ResetState (     vDSP_biquadm_Setup __vDSP_setup ); ``` |
| To | ``` void vDSP_biquadm_ResetState (     vDSP_biquadm_Setup _Nonnull __setup ); ``` |

Modified [vDSP_biquadm_ResetStateD()](https://developer.apple.com/documentation/kernel/1579935-vdsp_biquadm_resetstated)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_ResetStateD (     vDSP_biquadm_SetupD __vDSP_setup ); ``` |
| To | ``` void vDSP_biquadm_ResetStateD (     vDSP_biquadm_SetupD _Nonnull __setup ); ``` |

Modified [vDSP_biquadmD()](https://developer.apple.com/documentation/accelerate/1450102-vdsp_biquadmd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadmD (     vDSP_biquadm_SetupD __vDSP_Setup,     const double **__vDSP_X,     vDSP_Stride __vDSP_IX,     double **__vDSP_Y,     vDSP_Stride __vDSP_IY,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_biquadmD (     vDSP_biquadm_SetupD _Nonnull __Setup,     const double * _Nonnull * _Nonnull __X,     vDSP_Stride __IX,     double * _Nonnull * _Nonnull __Y,     vDSP_Stride __IY,     vDSP_Length __N ); ``` |

Modified [vDSP_blkman_window()](https://developer.apple.com/documentation/accelerate/1450190-vdsp_blkman_window)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_blkman_window (     float *__vDSP_C,     vDSP_Length __vDSP_N,     int __vDSP_Flag ); ``` |
| To | ``` void vDSP_blkman_window (     float * _Nonnull __C,     vDSP_Length __N,     int __Flag ); ``` |

Modified [vDSP_blkman_windowD()](https://developer.apple.com/documentation/accelerate/1450471-vdsp_blkman_windowd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_blkman_windowD (     double *__vDSP_C,     vDSP_Length __vDSP_N,     int __vDSP_Flag ); ``` |
| To | ``` void vDSP_blkman_windowD (     double * _Nonnull __C,     vDSP_Length __N,     int __Flag ); ``` |

Modified [vDSP_conv()](https://developer.apple.com/documentation/kernel/1532184-vdsp_conv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_conv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_F,     vDSP_Stride __vDSP_IF,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_conv (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __F,     vDSP_Stride __IF,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_convD()](https://developer.apple.com/documentation/accelerate/1450637-vdsp_convd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_convD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_F,     vDSP_Stride __vDSP_IF,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_convD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __F,     vDSP_Stride __IF,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_create_fftsetup()](https://developer.apple.com/documentation/kernel/1580009-vdsp_create_fftsetup)

|  | Declaration |
| --- | --- |
| From | ``` FFTSetup vDSP_create_fftsetup (     vDSP_Length __vDSP_Log2n,     FFTRadix __vDSP_Radix ); ``` |
| To | ``` FFTSetup _Nullable vDSP_create_fftsetup (     vDSP_Length __Log2n,     FFTRadix __Radix ); ``` |

Modified [vDSP_create_fftsetupD()](https://developer.apple.com/documentation/accelerate/1449974-vdsp_create_fftsetupd)

|  | Declaration |
| --- | --- |
| From | ``` FFTSetupD vDSP_create_fftsetupD (     vDSP_Length __vDSP_Log2n,     FFTRadix __vDSP_Radix ); ``` |
| To | ``` FFTSetupD _Nullable vDSP_create_fftsetupD (     vDSP_Length __Log2n,     FFTRadix __Radix ); ``` |

Modified [vDSP_ctoz()](https://developer.apple.com/documentation/kernel/1579975-vdsp_ctoz)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_ctoz (     const DSPComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_Z,     vDSP_Stride __vDSP_IZ,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_ctoz (     const DSPComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __Z,     vDSP_Stride __IZ,     vDSP_Length __N ); ``` |

Modified [vDSP_ctozD()](https://developer.apple.com/documentation/accelerate/1449970-vdsp_ctozd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_ctozD (     const DSPDoubleComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_Z,     vDSP_Stride __vDSP_IZ,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_ctozD (     const DSPDoubleComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __Z,     vDSP_Stride __IZ,     vDSP_Length __N ); ``` |

Modified [vDSP_DCT_CreateSetup()](https://developer.apple.com/documentation/accelerate/1449930-vdsp_dct_createsetup)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_DFT_Setup vDSP_DCT_CreateSetup (     vDSP_DFT_Setup __vDSP_Previous,     vDSP_Length __vDSP_Length,     vDSP_DCT_Type __vDSP_Type ); ``` |
| To | ``` vDSP_DFT_Setup _Nullable vDSP_DCT_CreateSetup (     vDSP_DFT_Setup _Nullable __Previous,     vDSP_Length __Length,     vDSP_DCT_Type __Type ); ``` |

Modified [vDSP_DCT_Execute()](https://developer.apple.com/documentation/accelerate/1450016-vdsp_dct_execute)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_DCT_Execute (     const struct vDSP_DFT_SetupStruct *__vDSP_Setup,     const float *__vDSP_Input,     float *__vDSP_Output ); ``` |
| To | ``` void vDSP_DCT_Execute (     const struct vDSP_DFT_SetupStruct * _Nonnull __Setup,     const float * _Nonnull __Input,     float * _Nonnull __Output ); ``` |

Modified [vDSP_deq22()](https://developer.apple.com/documentation/kernel/1532225-vdsp_deq22)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_deq22 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_deq22 (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_deq22D()](https://developer.apple.com/documentation/accelerate/1450534-vdsp_deq22d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_deq22D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_deq22D (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_desamp()](https://developer.apple.com/documentation/accelerate/1449946-vdsp_desamp)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_desamp (     const float *__vDSP_A,     vDSP_Stride __vDSP_I,     const float *__vDSP_F,     float *__vDSP_C,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_desamp (     const float * _Nonnull __A,     vDSP_Stride __DF,     const float * _Nonnull __F,     float * _Nonnull __C,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_desampD()](https://developer.apple.com/documentation/accelerate/1450133-vdsp_desampd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_desampD (     const double *__vDSP_A,     vDSP_Stride __vDSP_I,     const double *__vDSP_F,     double *__vDSP_C,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_desampD (     const double * _Nonnull __A,     vDSP_Stride __DF,     const double * _Nonnull __F,     double * _Nonnull __C,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_destroy_fftsetup()](https://developer.apple.com/documentation/accelerate/1450396-vdsp_destroy_fftsetup)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_destroy_fftsetup (     FFTSetup __vDSP_setup ); ``` |
| To | ``` void vDSP_destroy_fftsetup (     FFTSetup _Nullable __setup ); ``` |

Modified [vDSP_destroy_fftsetupD()](https://developer.apple.com/documentation/accelerate/1449686-vdsp_destroy_fftsetupd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_destroy_fftsetupD (     FFTSetupD __vDSP_setup ); ``` |
| To | ``` void vDSP_destroy_fftsetupD (     FFTSetupD _Nullable __setup ); ``` |

Modified vDSP_DFT_CreateSetup()

|  | Declaration |
| --- | --- |
| From | ``` vDSP_DFT_Setup vDSP_DFT_CreateSetup (     vDSP_DFT_Setup __vDSP_Previous,     vDSP_Length __vDSP_Length ); ``` |
| To | ``` vDSP_DFT_Setup _Nullable vDSP_DFT_CreateSetup (     vDSP_DFT_Setup _Nullable __Previous,     vDSP_Length __Length ); ``` |

Modified [vDSP_DFT_DestroySetup()](https://developer.apple.com/documentation/accelerate/1450791-vdsp_dft_destroysetup)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_DFT_DestroySetup (     vDSP_DFT_Setup __vDSP_Setup ); ``` |
| To | ``` void vDSP_DFT_DestroySetup (     vDSP_DFT_Setup _Nullable __Setup ); ``` |

Modified [vDSP_DFT_DestroySetupD()](https://developer.apple.com/documentation/accelerate/1450367-vdsp_dft_destroysetupd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_DFT_DestroySetupD (     vDSP_DFT_SetupD __vDSP_Setup ); ``` |
| To | ``` void vDSP_DFT_DestroySetupD (     vDSP_DFT_SetupD _Nullable __Setup ); ``` |

Modified [vDSP_DFT_Execute()](https://developer.apple.com/documentation/accelerate/1450538-vdsp_dft_execute)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_DFT_Execute (     const struct vDSP_DFT_SetupStruct *__vDSP_Setup,     const float *__vDSP_Ir,     const float *__vDSP_Ii,     float *__vDSP_Or,     float *__vDSP_Oi ); ``` |
| To | ``` void vDSP_DFT_Execute (     const struct vDSP_DFT_SetupStruct * _Nonnull __Setup,     const float * _Nonnull __Ir,     const float * _Nonnull __Ii,     float * _Nonnull __Or,     float * _Nonnull __Oi ); ``` |

Modified [vDSP_DFT_ExecuteD()](https://developer.apple.com/documentation/accelerate/1449812-vdsp_dft_executed)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_DFT_ExecuteD (     const struct vDSP_DFT_SetupStructD *__vDSP_Setup,     const double *__vDSP_Ir,     const double *__vDSP_Ii,     double *__vDSP_Or,     double *__vDSP_Oi ); ``` |
| To | ``` void vDSP_DFT_ExecuteD (     const struct vDSP_DFT_SetupStructD * _Nonnull __Setup,     const double * _Nonnull __Ir,     const double * _Nonnull __Ii,     double * _Nonnull __Or,     double * _Nonnull __Oi ); ``` |

Modified vDSP_DFT_zop()

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_DFT_zop (     const struct vDSP_DFT_SetupStruct *__vDSP_Setup,     const float *__vDSP_Ir,     const float *__vDSP_Ii,     vDSP_Stride __vDSP_Is,     float *__vDSP_Or,     float *__vDSP_Oi,     vDSP_Stride __vDSP_Os,     vDSP_DFT_Direction __vDSP_Direction ); ``` |
| To | ``` void vDSP_DFT_zop (     const struct vDSP_DFT_SetupStruct * _Nonnull __Setup,     const float * _Nonnull __Ir,     const float * _Nonnull __Ii,     vDSP_Stride __Is,     float * _Nonnull __Or,     float * _Nonnull __Oi,     vDSP_Stride __Os,     vDSP_DFT_Direction __Direction ); ``` |

Modified [vDSP_DFT_zop_CreateSetup()](https://developer.apple.com/documentation/accelerate/1450061-vdsp_dft_zop_createsetup)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_DFT_Setup vDSP_DFT_zop_CreateSetup (     vDSP_DFT_Setup __vDSP_Previous,     vDSP_Length __vDSP_Length,     vDSP_DFT_Direction __vDSP_Direction ); ``` |
| To | ``` vDSP_DFT_Setup _Nullable vDSP_DFT_zop_CreateSetup (     vDSP_DFT_Setup _Nullable __Previous,     vDSP_Length __Length,     vDSP_DFT_Direction __Direction ); ``` |

Modified [vDSP_DFT_zop_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1450730-vdsp_dft_zop_createsetupd)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_DFT_SetupD vDSP_DFT_zop_CreateSetupD (     vDSP_DFT_SetupD __vDSP_Previous,     vDSP_Length __vDSP_Length,     vDSP_DFT_Direction __vDSP_Direction ); ``` |
| To | ``` vDSP_DFT_SetupD _Nullable vDSP_DFT_zop_CreateSetupD (     vDSP_DFT_SetupD _Nullable __Previous,     vDSP_Length __Length,     vDSP_DFT_Direction __Direction ); ``` |

Modified [vDSP_DFT_zrop_CreateSetup()](https://developer.apple.com/documentation/accelerate/1449739-vdsp_dft_zrop_createsetup)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_DFT_Setup vDSP_DFT_zrop_CreateSetup (     vDSP_DFT_Setup __vDSP_Previous,     vDSP_Length __vDSP_Length,     vDSP_DFT_Direction __vDSP_Direction ); ``` |
| To | ``` vDSP_DFT_Setup _Nullable vDSP_DFT_zrop_CreateSetup (     vDSP_DFT_Setup _Nullable __Previous,     vDSP_Length __Length,     vDSP_DFT_Direction __Direction ); ``` |

Modified [vDSP_DFT_zrop_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1449790-vdsp_dft_zrop_createsetupd)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_DFT_SetupD vDSP_DFT_zrop_CreateSetupD (     vDSP_DFT_SetupD __vDSP_Previous,     vDSP_Length __vDSP_Length,     vDSP_DFT_Direction __vDSP_Direction ); ``` |
| To | ``` vDSP_DFT_SetupD _Nullable vDSP_DFT_zrop_CreateSetupD (     vDSP_DFT_SetupD _Nullable __Previous,     vDSP_Length __Length,     vDSP_DFT_Direction __Direction ); ``` |

Modified [vDSP_distancesq()](https://developer.apple.com/documentation/accelerate/1450619-vdsp_distancesq)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_distancesq (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_distancesq (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_distancesqD()](https://developer.apple.com/documentation/accelerate/1449892-vdsp_distancesqd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_distancesqD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_distancesqD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_dotpr()](https://developer.apple.com/documentation/accelerate/1450313-vdsp_dotpr)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_dotpr (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_dotpr2()](https://developer.apple.com/documentation/accelerate/1450752-vdsp_dotpr2)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr2 (     const float *__vDSP_A0,     vDSP_Stride __vDSP_A0Stride,     const float *__vDSP_A1,     vDSP_Stride __vDSP_A1Stride,     const float *__vDSP_B,     vDSP_Stride __vDSP_BStride,     float *__vDSP_C0,     float *__vDSP_C1,     vDSP_Length __vDSP_Length ); ``` |
| To | ``` void vDSP_dotpr2 (     const float * _Nonnull __A0,     vDSP_Stride __A0Stride,     const float * _Nonnull __A1,     vDSP_Stride __A1Stride,     const float * _Nonnull __B,     vDSP_Stride __BStride,     float * _Nonnull __C0,     float * _Nonnull __C1,     vDSP_Length __Length ); ``` |

Modified [vDSP_dotpr2_s1_15()](https://developer.apple.com/documentation/accelerate/1449919-vdsp_dotpr2_s1_15)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr2_s1_15 (     const short *__vDSP_A0,     vDSP_Stride __vDSP_A0Stride,     const short *__vDSP_A1,     vDSP_Stride __vDSP_A1Stride,     const short *__vDSP_B,     vDSP_Stride __vDSP_BStride,     short *__vDSP_C0,     short *__vDSP_C1,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_dotpr2_s1_15 (     const short * _Nonnull __A0,     vDSP_Stride __A0Stride,     const short * _Nonnull __A1,     vDSP_Stride __A1Stride,     const short * _Nonnull __B,     vDSP_Stride __BStride,     short * _Nonnull __C0,     short * _Nonnull __C1,     vDSP_Length __N ); ``` |

Modified [vDSP_dotpr2_s8_24()](https://developer.apple.com/documentation/accelerate/1449663-vdsp_dotpr2_s8_24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr2_s8_24 (     const int *__vDSP_A0,     vDSP_Stride __vDSP_A0Stride,     const int *__vDSP_A1,     vDSP_Stride __vDSP_A1Stride,     const int *__vDSP_B,     vDSP_Stride __vDSP_BStride,     int *__vDSP_C0,     int *__vDSP_C1,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_dotpr2_s8_24 (     const int * _Nonnull __A0,     vDSP_Stride __A0Stride,     const int * _Nonnull __A1,     vDSP_Stride __A1Stride,     const int * _Nonnull __B,     vDSP_Stride __BStride,     int * _Nonnull __C0,     int * _Nonnull __C1,     vDSP_Length __N ); ``` |

Modified [vDSP_dotpr2D()](https://developer.apple.com/documentation/accelerate/1450152-vdsp_dotpr2d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr2D (     const double *__vDSP_A0,     vDSP_Stride __vDSP_A0Stride,     const double *__vDSP_A1,     vDSP_Stride __vDSP_A1Stride,     const double *__vDSP_B,     vDSP_Stride __vDSP_BStride,     double *__vDSP_C0,     double *__vDSP_C1,     vDSP_Length __vDSP_Length ); ``` |
| To | ``` void vDSP_dotpr2D (     const double * _Nonnull __A0,     vDSP_Stride __A0Stride,     const double * _Nonnull __A1,     vDSP_Stride __A1Stride,     const double * _Nonnull __B,     vDSP_Stride __BStride,     double * _Nonnull __C0,     double * _Nonnull __C1,     vDSP_Length __Length ); ``` |

Modified [vDSP_dotpr_s1_15()](https://developer.apple.com/documentation/accelerate/1449796-vdsp_dotpr_s1_15)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr_s1_15 (     const short *__vDSP_A,     vDSP_Stride __vDSP_AStride,     const short *__vDSP_B,     vDSP_Stride __vDSP_BStride,     short *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_dotpr_s1_15 (     const short * _Nonnull __A,     vDSP_Stride __AStride,     const short * _Nonnull __B,     vDSP_Stride __BStride,     short * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_dotpr_s8_24()](https://developer.apple.com/documentation/accelerate/1450480-vdsp_dotpr_s8_24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr_s8_24 (     const int *__vDSP_A,     vDSP_Stride __vDSP_AStride,     const int *__vDSP_B,     vDSP_Stride __vDSP_BStride,     int *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_dotpr_s8_24 (     const int * _Nonnull __A,     vDSP_Stride __AStride,     const int * _Nonnull __B,     vDSP_Stride __BStride,     int * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_dotprD()](https://developer.apple.com/documentation/accelerate/1450330-vdsp_dotprd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotprD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_dotprD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_f3x3()](https://developer.apple.com/documentation/accelerate/1450690-vdsp_f3x3)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_f3x3 (     const float *__vDSP_A,     vDSP_Length __vDSP_NR,     vDSP_Length __vDSP_NC,     const float *__vDSP_F,     float *__vDSP_C ); ``` |
| To | ``` void vDSP_f3x3 (     const float * _Nonnull __A,     vDSP_Length __NR,     vDSP_Length __NC,     const float * _Nonnull __F,     float * _Nonnull __C ); ``` |

Modified [vDSP_f3x3D()](https://developer.apple.com/documentation/accelerate/1450651-vdsp_f3x3d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_f3x3D (     const double *__vDSP_A,     vDSP_Length __vDSP_NR,     vDSP_Length __vDSP_NC,     const double *__vDSP_F,     double *__vDSP_C ); ``` |
| To | ``` void vDSP_f3x3D (     const double * _Nonnull __A,     vDSP_Length __NR,     vDSP_Length __NC,     const double * _Nonnull __F,     double * _Nonnull __C ); ``` |

Modified [vDSP_f5x5()](https://developer.apple.com/documentation/accelerate/1450036-vdsp_f5x5)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_f5x5 (     const float *__vDSP_A,     vDSP_Length __vDSP_NR,     vDSP_Length __vDSP_NC,     const float *__vDSP_F,     float *__vDSP_C ); ``` |
| To | ``` void vDSP_f5x5 (     const float * _Nonnull __A,     vDSP_Length __NR,     vDSP_Length __NC,     const float * _Nonnull __F,     float * _Nonnull __C ); ``` |

Modified [vDSP_f5x5D()](https://developer.apple.com/documentation/accelerate/1449839-vdsp_f5x5d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_f5x5D (     const double *__vDSP_A,     vDSP_Length __vDSP_NR,     vDSP_Length __vDSP_NC,     const double *__vDSP_F,     double *__vDSP_C ); ``` |
| To | ``` void vDSP_f5x5D (     const double * _Nonnull __A,     vDSP_Length __NR,     vDSP_Length __NC,     const double * _Nonnull __F,     double * _Nonnull __C ); ``` |

Modified [vDSP_FFT16_copv()](https://developer.apple.com/documentation/accelerate/1450220-vdsp_fft16_copv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_FFT16_copv (     float *__vDSP_Output,     const float *__vDSP_Input,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_FFT16_copv (     float * _Nonnull __Output,     const float * _Nonnull __Input,     FFTDirection __Direction ); ``` |

Modified [vDSP_FFT16_zopv()](https://developer.apple.com/documentation/accelerate/1450002-vdsp_fft16_zopv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_FFT16_zopv (     float *__vDSP_Or,     float *__vDSP_Oi,     const float *__vDSP_Ir,     const float *__vDSP_Ii,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_FFT16_zopv (     float * _Nonnull __Or,     float * _Nonnull __Oi,     const float * _Nonnull __Ir,     const float * _Nonnull __Ii,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zip()](https://developer.apple.com/documentation/accelerate/1450430-vdsp_fft2d_zip)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zip (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zip (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zipD()](https://developer.apple.com/documentation/accelerate/1450508-vdsp_fft2d_zipd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zipD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zipD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zipt()](https://developer.apple.com/documentation/accelerate/1450777-vdsp_fft2d_zipt)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zipt (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC1,     vDSP_Stride __vDSP_IC0,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zipt (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC1,     vDSP_Stride __IC0,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_ziptD()](https://developer.apple.com/documentation/accelerate/1450202-vdsp_fft2d_ziptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_ziptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_ziptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zop()](https://developer.apple.com/documentation/accelerate/1450355-vdsp_fft2d_zop)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zop (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA0,     vDSP_Stride __vDSP_IA1,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zop (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA0,     vDSP_Stride __IA1,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zopD()](https://developer.apple.com/documentation/accelerate/1449944-vdsp_fft2d_zopd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zopD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA0,     vDSP_Stride __vDSP_IA1,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zopD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA0,     vDSP_Stride __IA1,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zopt()](https://developer.apple.com/documentation/accelerate/1450816-vdsp_fft2d_zopt)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zopt (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA0,     vDSP_Stride __vDSP_IA1,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zopt (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA0,     vDSP_Stride __IA1,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zoptD()](https://developer.apple.com/documentation/accelerate/1449963-vdsp_fft2d_zoptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zoptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA0,     vDSP_Stride __vDSP_IA1,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zoptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA0,     vDSP_Stride __IA1,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zrip()](https://developer.apple.com/documentation/accelerate/1450116-vdsp_fft2d_zrip)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zrip (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zrip (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zripD()](https://developer.apple.com/documentation/accelerate/1450384-vdsp_fft2d_zripd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zripD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_flag ); ``` |
| To | ``` void vDSP_fft2d_zripD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __flag ); ``` |

Modified [vDSP_fft2d_zript()](https://developer.apple.com/documentation/accelerate/1450144-vdsp_fft2d_zript)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zript (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zript (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zriptD()](https://developer.apple.com/documentation/accelerate/1450079-vdsp_fft2d_zriptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zriptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_flag ); ``` |
| To | ``` void vDSP_fft2d_zriptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __flag ); ``` |

Modified [vDSP_fft2d_zrop()](https://developer.apple.com/documentation/accelerate/1450361-vdsp_fft2d_zrop)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zrop (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA0,     vDSP_Stride __vDSP_IA1,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zrop (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA0,     vDSP_Stride __IA1,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zropD()](https://developer.apple.com/documentation/accelerate/1450732-vdsp_fft2d_zropd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zropD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA0,     vDSP_Stride __vDSP_IA1,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zropD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA0,     vDSP_Stride __IA1,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zropt()](https://developer.apple.com/documentation/accelerate/1450460-vdsp_fft2d_zropt)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zropt (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA0,     vDSP_Stride __vDSP_IA1,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zropt (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA0,     vDSP_Stride __IA1,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft2d_zroptD()](https://developer.apple.com/documentation/accelerate/1450433-vdsp_fft2d_zroptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft2d_zroptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA0,     vDSP_Stride __vDSP_IA1,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC0,     vDSP_Stride __vDSP_IC1,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N0,     vDSP_Length __vDSP_Log2N1,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft2d_zroptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA0,     vDSP_Stride __IA1,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC0,     vDSP_Stride __IC1,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N0,     vDSP_Length __Log2N1,     FFTDirection __Direction ); ``` |

Modified [vDSP_FFT32_copv()](https://developer.apple.com/documentation/accelerate/1450426-vdsp_fft32_copv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_FFT32_copv (     float *__vDSP_Output,     const float *__vDSP_Input,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_FFT32_copv (     float * _Nonnull __Output,     const float * _Nonnull __Input,     FFTDirection __Direction ); ``` |

Modified [vDSP_FFT32_zopv()](https://developer.apple.com/documentation/accelerate/1449684-vdsp_fft32_zopv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_FFT32_zopv (     float *__vDSP_Or,     float *__vDSP_Oi,     const float *__vDSP_Ir,     const float *__vDSP_Ii,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_FFT32_zopv (     float * _Nonnull __Or,     float * _Nonnull __Oi,     const float * _Nonnull __Ir,     const float * _Nonnull __Ii,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft3_zop()](https://developer.apple.com/documentation/accelerate/1450494-vdsp_fft3_zop)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` void vDSP_fft3_zop (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` | -- |
| To | ``` void vDSP_fft3_zop (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` | iOS 9.0 |

Modified [vDSP_fft3_zopD()](https://developer.apple.com/documentation/accelerate/1450124-vdsp_fft3_zopd)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` void vDSP_fft3_zopD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` | -- |
| To | ``` void vDSP_fft3_zopD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` | iOS 9.0 |

Modified [vDSP_fft5_zop()](https://developer.apple.com/documentation/accelerate/1450044-vdsp_fft5_zop)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` void vDSP_fft5_zop (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` | -- |
| To | ``` void vDSP_fft5_zop (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` | iOS 9.0 |

Modified [vDSP_fft5_zopD()](https://developer.apple.com/documentation/accelerate/1450738-vdsp_fft5_zopd)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` void vDSP_fft5_zopD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` | -- |
| To | ``` void vDSP_fft5_zopD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` | iOS 9.0 |

Modified [vDSP_fft_zip()](https://developer.apple.com/documentation/accelerate/1450224-vdsp_fft_zip)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zip (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zip (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zipD()](https://developer.apple.com/documentation/accelerate/1449916-vdsp_fft_zipd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zipD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zipD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zipt()](https://developer.apple.com/documentation/accelerate/1449879-vdsp_fft_zipt)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zipt (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zipt (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_ziptD()](https://developer.apple.com/documentation/accelerate/1450852-vdsp_fft_ziptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_ziptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_ziptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zop()](https://developer.apple.com/documentation/accelerate/1450581-vdsp_fft_zop)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zop (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zop (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zopD()](https://developer.apple.com/documentation/accelerate/1450694-vdsp_fft_zopd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zopD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zopD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zopt()](https://developer.apple.com/documentation/accelerate/1450812-vdsp_fft_zopt)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zopt (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zopt (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zoptD()](https://developer.apple.com/documentation/accelerate/1450447-vdsp_fft_zoptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zoptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zoptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zrip()](https://developer.apple.com/documentation/kernel/1579997-vdsp_fft_zrip)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zrip (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zrip (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zripD()](https://developer.apple.com/documentation/accelerate/1450371-vdsp_fft_zripd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zripD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zripD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zript()](https://developer.apple.com/documentation/accelerate/1450455-vdsp_fft_zript)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zript (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zript (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zriptD()](https://developer.apple.com/documentation/accelerate/1450486-vdsp_fft_zriptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zriptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zriptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zrop()](https://developer.apple.com/documentation/accelerate/1449994-vdsp_fft_zrop)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zrop (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zrop (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zropD()](https://developer.apple.com/documentation/accelerate/1449666-vdsp_fft_zropd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zropD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zropD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zropt()](https://developer.apple.com/documentation/accelerate/1450404-vdsp_fft_zropt)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zropt (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zropt (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fft_zroptD()](https://developer.apple.com/documentation/accelerate/1450828-vdsp_fft_zroptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zroptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zroptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zip()](https://developer.apple.com/documentation/accelerate/1450798-vdsp_fftm_zip)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zip (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IM,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zip (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IM,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zipD()](https://developer.apple.com/documentation/accelerate/1449959-vdsp_fftm_zipd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zipD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IM,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zipD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IM,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zipt()](https://developer.apple.com/documentation/accelerate/1449852-vdsp_fftm_zipt)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zipt (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IM,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zipt (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IM,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_ziptD()](https://developer.apple.com/documentation/accelerate/1450092-vdsp_fftm_ziptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_ziptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IM,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_ziptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IM,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zop()](https://developer.apple.com/documentation/accelerate/1450053-vdsp_fftm_zop)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zop (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     vDSP_Stride __vDSP_IMA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IMC,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zop (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     vDSP_Stride __IMA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IMC,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zopD()](https://developer.apple.com/documentation/accelerate/1450439-vdsp_fftm_zopd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zopD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     vDSP_Stride __vDSP_IMA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IMC,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zopD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     vDSP_Stride __IMA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IMC,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zopt()](https://developer.apple.com/documentation/accelerate/1449737-vdsp_fftm_zopt)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zopt (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     vDSP_Stride __vDSP_IMA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IMC,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zopt (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     vDSP_Stride __IMA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IMC,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zoptD()](https://developer.apple.com/documentation/accelerate/1450596-vdsp_fftm_zoptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zoptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     vDSP_Stride __vDSP_IMA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IMC,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zoptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     vDSP_Stride __IMA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IMC,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zrip()](https://developer.apple.com/documentation/accelerate/1449883-vdsp_fftm_zrip)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zrip (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IM,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zrip (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IM,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zripD()](https://developer.apple.com/documentation/accelerate/1450075-vdsp_fftm_zripd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zripD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IM,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zripD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IM,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zript()](https://developer.apple.com/documentation/accelerate/1450050-vdsp_fftm_zript)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zript (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IM,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zript (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IM,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zriptD()](https://developer.apple.com/documentation/accelerate/1450514-vdsp_fftm_zriptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zriptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IM,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zriptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IM,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zrop()](https://developer.apple.com/documentation/accelerate/1450073-vdsp_fftm_zrop)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zrop (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     vDSP_Stride __vDSP_IMA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IMC,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zrop (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     vDSP_Stride __IMA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IMC,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zropD()](https://developer.apple.com/documentation/accelerate/1449714-vdsp_fftm_zropd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zropD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     vDSP_Stride __vDSP_IMA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IMC,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zropD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     vDSP_Stride __IMA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IMC,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zropt()](https://developer.apple.com/documentation/accelerate/1450659-vdsp_fftm_zropt)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zropt (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     vDSP_Stride __vDSP_IMA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IMC,     const DSPSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zropt (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     vDSP_Stride __IMA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IMC,     const DSPSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_fftm_zroptD()](https://developer.apple.com/documentation/accelerate/1450320-vdsp_fftm_zroptd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fftm_zroptD (     FFTSetupD __vDSP_Setup,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     vDSP_Stride __vDSP_IMA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Stride __vDSP_IMC,     const DSPDoubleSplitComplex *__vDSP_Buffer,     vDSP_Length __vDSP_Log2N,     vDSP_Length __vDSP_M,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fftm_zroptD (     FFTSetupD _Nonnull __Setup,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     vDSP_Stride __IMA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Stride __IMC,     const DSPDoubleSplitComplex * _Nonnull __Buffer,     vDSP_Length __Log2N,     vDSP_Length __M,     FFTDirection __Direction ); ``` |

Modified [vDSP_hamm_window()](https://developer.apple.com/documentation/accelerate/1450040-vdsp_hamm_window)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_hamm_window (     float *__vDSP_C,     vDSP_Length __vDSP_N,     int __vDSP_Flag ); ``` |
| To | ``` void vDSP_hamm_window (     float * _Nonnull __C,     vDSP_Length __N,     int __Flag ); ``` |

Modified [vDSP_hamm_windowD()](https://developer.apple.com/documentation/accelerate/1450721-vdsp_hamm_windowd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_hamm_windowD (     double *__vDSP_C,     vDSP_Length __vDSP_N,     int __vDSP_Flag ); ``` |
| To | ``` void vDSP_hamm_windowD (     double * _Nonnull __C,     vDSP_Length __N,     int __Flag ); ``` |

Modified [vDSP_hann_window()](https://developer.apple.com/documentation/accelerate/1450263-vdsp_hann_window)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_hann_window (     float *__vDSP_C,     vDSP_Length __vDSP_N,     int __vDSP_Flag ); ``` |
| To | ``` void vDSP_hann_window (     float * _Nonnull __C,     vDSP_Length __N,     int __Flag ); ``` |

Modified [vDSP_hann_windowD()](https://developer.apple.com/documentation/accelerate/1450048-vdsp_hann_windowd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_hann_windowD (     double *__vDSP_C,     vDSP_Length __vDSP_N,     int __vDSP_Flag ); ``` |
| To | ``` void vDSP_hann_windowD (     double * _Nonnull __C,     vDSP_Length __N,     int __Flag ); ``` |

Modified [vDSP_imgfir()](https://developer.apple.com/documentation/accelerate/1449856-vdsp_imgfir)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_imgfir (     const float *__vDSP_A,     vDSP_Length __vDSP_NR,     vDSP_Length __vDSP_NC,     const float *__vDSP_F,     float *__vDSP_C,     vDSP_Length __vDSP_P,     vDSP_Length __vDSP_Q ); ``` |
| To | ``` void vDSP_imgfir (     const float * _Nonnull __A,     vDSP_Length __NR,     vDSP_Length __NC,     const float * _Nonnull __F,     float * _Nonnull __C,     vDSP_Length __P,     vDSP_Length __Q ); ``` |

Modified [vDSP_imgfirD()](https://developer.apple.com/documentation/accelerate/1449818-vdsp_imgfird)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_imgfirD (     const double *__vDSP_A,     vDSP_Length __vDSP_NR,     vDSP_Length __vDSP_NC,     const double *__vDSP_F,     double *__vDSP_C,     vDSP_Length __vDSP_P,     vDSP_Length __vDSP_Q ); ``` |
| To | ``` void vDSP_imgfirD (     const double * _Nonnull __A,     vDSP_Length __NR,     vDSP_Length __NC,     const double * _Nonnull __F,     double * _Nonnull __C,     vDSP_Length __P,     vDSP_Length __Q ); ``` |

Modified [vDSP_maxmgv()](https://developer.apple.com/documentation/kernel/1532187-vdsp_maxmgv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_maxmgv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_maxmgv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_maxmgvD()](https://developer.apple.com/documentation/accelerate/1450633-vdsp_maxmgvd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_maxmgvD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_maxmgvD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_maxmgvi()](https://developer.apple.com/documentation/accelerate/1450576-vdsp_maxmgvi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_maxmgvi (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length *__vDSP_I,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_maxmgvi (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length * _Nonnull __I,     vDSP_Length __N ); ``` |

Modified [vDSP_maxmgviD()](https://developer.apple.com/documentation/accelerate/1450249-vdsp_maxmgvid)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_maxmgviD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length *__vDSP_I,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_maxmgviD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length * _Nonnull __I,     vDSP_Length __N ); ``` |

Modified [vDSP_maxv()](https://developer.apple.com/documentation/kernel/1580003-vdsp_maxv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_maxv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_maxv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_maxvD()](https://developer.apple.com/documentation/accelerate/1449854-vdsp_maxvd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_maxvD (     const double *__vDSP_A,     vDSP_Stride __vDSP_I,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_maxvD (     const double * _Nonnull __A,     vDSP_Stride __I,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_maxvi()](https://developer.apple.com/documentation/accelerate/1450814-vdsp_maxvi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_maxvi (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length *__vDSP_I,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_maxvi (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length * _Nonnull __I,     vDSP_Length __N ); ``` |

Modified [vDSP_maxviD()](https://developer.apple.com/documentation/accelerate/1449682-vdsp_maxvid)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_maxviD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length *__vDSP_I,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_maxviD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length * _Nonnull __I,     vDSP_Length __N ); ``` |

Modified [vDSP_meamgv()](https://developer.apple.com/documentation/accelerate/1449731-vdsp_meamgv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_meamgv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_meamgv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_meamgvD()](https://developer.apple.com/documentation/accelerate/1450214-vdsp_meamgvd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_meamgvD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_meamgvD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_meanv()](https://developer.apple.com/documentation/accelerate/1449980-vdsp_meanv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_meanv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_meanv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_meanvD()](https://developer.apple.com/documentation/accelerate/1449784-vdsp_meanvd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_meanvD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_meanvD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_measqv()](https://developer.apple.com/documentation/accelerate/1450014-vdsp_measqv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_measqv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_measqv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_measqvD()](https://developer.apple.com/documentation/accelerate/1450463-vdsp_measqvd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_measqvD (     const double *__vDSP_A,     vDSP_Stride __vDSP_I,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_measqvD (     const double * _Nonnull __A,     vDSP_Stride __I,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_minmgv()](https://developer.apple.com/documentation/accelerate/1449786-vdsp_minmgv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_minmgv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_minmgv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_minmgvD()](https://developer.apple.com/documentation/accelerate/1449830-vdsp_minmgvd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_minmgvD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_minmgvD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_minmgvi()](https://developer.apple.com/documentation/accelerate/1449814-vdsp_minmgvi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_minmgvi (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length *__vDSP_I,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_minmgvi (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length * _Nonnull __I,     vDSP_Length __N ); ``` |

Modified [vDSP_minmgviD()](https://developer.apple.com/documentation/accelerate/1450843-vdsp_minmgvid)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_minmgviD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length *__vDSP_I,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_minmgviD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length * _Nonnull __I,     vDSP_Length __N ); ``` |

Modified [vDSP_minv()](https://developer.apple.com/documentation/accelerate/1450267-vdsp_minv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_minv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_minv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_minvD()](https://developer.apple.com/documentation/accelerate/1450663-vdsp_minvd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_minvD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_minvD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_minvi()](https://developer.apple.com/documentation/accelerate/1449875-vdsp_minvi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_minvi (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length *__vDSP_I,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_minvi (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length * _Nonnull __I,     vDSP_Length __N ); ``` |

Modified [vDSP_minviD()](https://developer.apple.com/documentation/accelerate/1450441-vdsp_minvid)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_minviD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length *__vDSP_I,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_minviD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length * _Nonnull __I,     vDSP_Length __N ); ``` |

Modified [vDSP_mmov()](https://developer.apple.com/documentation/accelerate/1449950-vdsp_mmov)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_mmov (     const float *__vDSP_A,     float *__vDSP_C,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_TA,     vDSP_Length __vDSP_TC ); ``` |
| To | ``` void vDSP_mmov (     const float * _Nonnull __A,     float * _Nonnull __C,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __TA,     vDSP_Length __TC ); ``` |

Modified [vDSP_mmovD()](https://developer.apple.com/documentation/accelerate/1449956-vdsp_mmovd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_mmovD (     const double *__vDSP_A,     double *__vDSP_C,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_TA,     vDSP_Length __vDSP_TC ); ``` |
| To | ``` void vDSP_mmovD (     const double * _Nonnull __A,     double * _Nonnull __C,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __TA,     vDSP_Length __TC ); ``` |

Modified [vDSP_mmul()](https://developer.apple.com/documentation/accelerate/1449984-vdsp_mmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_mmul (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_mmul (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_mmulD()](https://developer.apple.com/documentation/accelerate/1450386-vdsp_mmuld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_mmulD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_mmulD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_mtrans()](https://developer.apple.com/documentation/accelerate/1449988-vdsp_mtrans)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_mtrans (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_mtrans (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __M,     vDSP_Length __N ); ``` |

Modified [vDSP_mtransD()](https://developer.apple.com/documentation/accelerate/1450422-vdsp_mtransd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_mtransD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_mtransD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __M,     vDSP_Length __N ); ``` |

Modified [vDSP_mvessq()](https://developer.apple.com/documentation/accelerate/1449849-vdsp_mvessq)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_mvessq (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_mvessq (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_mvessqD()](https://developer.apple.com/documentation/accelerate/1449753-vdsp_mvessqd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_mvessqD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_mvessqD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_normalize()](https://developer.apple.com/documentation/accelerate/1450106-vdsp_normalize)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_normalize (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     float *__vDSP_Mean,     float *__vDSP_StandardDeviation,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_normalize (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nullable __C,     vDSP_Stride __IC,     float * _Nonnull __Mean,     float * _Nonnull __StandardDeviation,     vDSP_Length __N ); ``` |

Modified [vDSP_normalizeD()](https://developer.apple.com/documentation/accelerate/1450154-vdsp_normalized)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_normalizeD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     double *__vDSP_Mean,     double *__vDSP_StandardDeviation,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_normalizeD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nullable __C,     vDSP_Stride __IC,     double * _Nonnull __Mean,     double * _Nonnull __StandardDeviation,     vDSP_Length __N ); ``` |

Modified [vDSP_nzcros()](https://developer.apple.com/documentation/accelerate/1450629-vdsp_nzcros)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_nzcros (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     vDSP_Length __vDSP_B,     vDSP_Length *__vDSP_C,     vDSP_Length *__vDSP_D,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_nzcros (     const float * _Nonnull __A,     vDSP_Stride __IA,     vDSP_Length __B,     vDSP_Length * _Nonnull __C,     vDSP_Length * _Nonnull __D,     vDSP_Length __N ); ``` |

Modified [vDSP_nzcrosD()](https://developer.apple.com/documentation/accelerate/1450715-vdsp_nzcrosd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_nzcrosD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     vDSP_Length __vDSP_B,     vDSP_Length *__vDSP_C,     vDSP_Length *__vDSP_D,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_nzcrosD (     const double * _Nonnull __A,     vDSP_Stride __IA,     vDSP_Length __B,     vDSP_Length * _Nonnull __C,     vDSP_Length * _Nonnull __D,     vDSP_Length __N ); ``` |

Modified [vDSP_polar()](https://developer.apple.com/documentation/accelerate/1450489-vdsp_polar)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_polar (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_polar (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_polarD()](https://developer.apple.com/documentation/accelerate/1450540-vdsp_polard)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_polarD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_polarD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_rect()](https://developer.apple.com/documentation/accelerate/1450416-vdsp_rect)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_rect (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_rect (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_rectD()](https://developer.apple.com/documentation/accelerate/1450754-vdsp_rectd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_rectD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_rectD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_rmsqv()](https://developer.apple.com/documentation/accelerate/1450655-vdsp_rmsqv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_rmsqv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_rmsqv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_rmsqvD()](https://developer.apple.com/documentation/accelerate/1449917-vdsp_rmsqvd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_rmsqvD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_rmsqvD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_svdiv()](https://developer.apple.com/documentation/accelerate/1450412-vdsp_svdiv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svdiv (     const float *__vDSP_A,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svdiv (     const float * _Nonnull __A,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_svdivD()](https://developer.apple.com/documentation/accelerate/1450028-vdsp_svdivd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svdivD (     const double *__vDSP_A,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svdivD (     const double * _Nonnull __A,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_sve()](https://developer.apple.com/documentation/kernel/1579937-vdsp_sve)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_sve (     const float *__vDSP_A,     vDSP_Stride __vDSP_I,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_sve (     const float * _Nonnull __A,     vDSP_Stride __I,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_sve_svesq()](https://developer.apple.com/documentation/kernel/1579989-vdsp_sve_svesq)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_sve_svesq (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_Sum,     float *__vDSP_SumOfSquares,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_sve_svesq (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __Sum,     float * _Nonnull __SumOfSquares,     vDSP_Length __N ); ``` |

Modified [vDSP_sve_svesqD()](https://developer.apple.com/documentation/accelerate/1450682-vdsp_sve_svesqd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_sve_svesqD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_Sum,     double *__vDSP_SumOfSquares,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_sve_svesqD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __Sum,     double * _Nonnull __SumOfSquares,     vDSP_Length __N ); ``` |

Modified [vDSP_sveD()](https://developer.apple.com/documentation/accelerate/1450567-vdsp_sved)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_sveD (     const double *__vDSP_A,     vDSP_Stride __vDSP_I,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_sveD (     const double * _Nonnull __A,     vDSP_Stride __I,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_svemg()](https://developer.apple.com/documentation/accelerate/1450055-vdsp_svemg)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svemg (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svemg (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_svemgD()](https://developer.apple.com/documentation/accelerate/1450856-vdsp_svemgd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svemgD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svemgD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_svesq()](https://developer.apple.com/documentation/accelerate/1450392-vdsp_svesq)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svesq (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svesq (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_svesqD()](https://developer.apple.com/documentation/accelerate/1450012-vdsp_svesqd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svesqD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svesqD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_svs()](https://developer.apple.com/documentation/kernel/1532174-vdsp_svs)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svs (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svs (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_svsD()](https://developer.apple.com/documentation/accelerate/1450862-vdsp_svsd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svsD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svsD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_vaam()](https://developer.apple.com/documentation/accelerate/1450588-vdsp_vaam)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vaam (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     const float *__vDSP_D,     vDSP_Stride __vDSP_ID,     float *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vaam (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     const float * _Nonnull __D,     vDSP_Stride __ID,     float * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vaamD()](https://developer.apple.com/documentation/accelerate/1450148-vdsp_vaamd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vaamD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     const double *__vDSP_D,     vDSP_Stride __vDSP_ID,     double *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vaamD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     const double * _Nonnull __D,     vDSP_Stride __ID,     double * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vabs()](https://developer.apple.com/documentation/kernel/1532216-vdsp_vabs)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vabs (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vabs (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vabsD()](https://developer.apple.com/documentation/accelerate/1449982-vdsp_vabsd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vabsD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vabsD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vabsi()](https://developer.apple.com/documentation/accelerate/1449929-vdsp_vabsi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vabsi (     const int *__vDSP_A,     vDSP_Stride __vDSP_IA,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vabsi (     const int * _Nonnull __A,     vDSP_Stride __IA,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vadd()](https://developer.apple.com/documentation/kernel/1532191-vdsp_vadd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vadd (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vadd (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vaddD()](https://developer.apple.com/documentation/accelerate/1449910-vdsp_vaddd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vaddD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vaddD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vaddi()](https://developer.apple.com/documentation/accelerate/1450179-vdsp_vaddi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vaddi (     const int *__vDSP_A,     vDSP_Stride __vDSP_IA,     const int *__vDSP_B,     vDSP_Stride __vDSP_IB,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vaddi (     const int * _Nonnull __A,     vDSP_Stride __IA,     const int * _Nonnull __B,     vDSP_Stride __IB,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vaddsub()](https://developer.apple.com/documentation/accelerate/1449781-vdsp_vaddsub)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vaddsub (     const float *__vDSP_I0,     vDSP_Stride __vDSP_I0S,     const float *__vDSP_I1,     vDSP_Stride __vDSP_I1S,     float *__vDSP_O0,     vDSP_Stride __vDSP_O0S,     float *__vDSP_O1,     vDSP_Stride __vDSP_O1S,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vaddsub (     const float * _Nonnull __I0,     vDSP_Stride __I0S,     const float * _Nonnull __I1,     vDSP_Stride __I1S,     float * _Nonnull __O0,     vDSP_Stride __O0S,     float * _Nonnull __O1,     vDSP_Stride __O1S,     vDSP_Length __N ); ``` |

Modified [vDSP_vaddsubD()](https://developer.apple.com/documentation/accelerate/1450568-vdsp_vaddsubd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vaddsubD (     const double *__vDSP_I0,     vDSP_Stride __vDSP_I0S,     const double *__vDSP_I1,     vDSP_Stride __vDSP_I1S,     double *__vDSP_O0,     vDSP_Stride __vDSP_O0S,     double *__vDSP_O1,     vDSP_Stride __vDSP_O1S,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vaddsubD (     const double * _Nonnull __I0,     vDSP_Stride __I0S,     const double * _Nonnull __I1,     vDSP_Stride __I1S,     double * _Nonnull __O0,     vDSP_Stride __O0S,     double * _Nonnull __O1,     vDSP_Stride __O1S,     vDSP_Length __N ); ``` |

Modified [vDSP_vam()](https://developer.apple.com/documentation/accelerate/1450561-vdsp_vam)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vam (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vam (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vamD()](https://developer.apple.com/documentation/accelerate/1450382-vdsp_vamd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vamD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     double *__vDSP_D,     vDSP_Stride __vDSP_IDD,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vamD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     double * _Nonnull __D,     vDSP_Stride __IDD,     vDSP_Length __N ); ``` |

Modified [vDSP_vasbm()](https://developer.apple.com/documentation/accelerate/1450277-vdsp_vasbm)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vasbm (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     const float *__vDSP_D,     vDSP_Stride __vDSP_ID,     float *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vasbm (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     const float * _Nonnull __D,     vDSP_Stride __ID,     float * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vasbmD()](https://developer.apple.com/documentation/accelerate/1449885-vdsp_vasbmd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vasbmD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     const double *__vDSP_D,     vDSP_Stride __vDSP_ID,     double *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vasbmD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     const double * _Nonnull __D,     vDSP_Stride __ID,     double * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vasm()](https://developer.apple.com/documentation/accelerate/1449773-vdsp_vasm)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vasm (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vasm (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vasmD()](https://developer.apple.com/documentation/accelerate/1450146-vdsp_vasmd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vasmD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vasmD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vavlin()](https://developer.apple.com/documentation/accelerate/1449668-vdsp_vavlin)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vavlin (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vavlin (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vavlinD()](https://developer.apple.com/documentation/accelerate/1450158-vdsp_vavlind)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vavlinD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vavlinD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vclip()](https://developer.apple.com/documentation/accelerate/1450071-vdsp_vclip)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vclip (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vclip (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vclipc()](https://developer.apple.com/documentation/accelerate/1450775-vdsp_vclipc)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vclipc (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N,     vDSP_Length *__vDSP_NLow,     vDSP_Length *__vDSP_NHigh ); ``` |
| To | ``` void vDSP_vclipc (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N,     vDSP_Length * _Nonnull __NLow,     vDSP_Length * _Nonnull __NHigh ); ``` |

Modified [vDSP_vclipcD()](https://developer.apple.com/documentation/accelerate/1450162-vdsp_vclipcd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vclipcD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     const double *__vDSP_C,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N,     vDSP_Length *__vDSP_NLow,     vDSP_Length *__vDSP_NHigh ); ``` |
| To | ``` void vDSP_vclipcD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     const double * _Nonnull __C,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N,     vDSP_Length * _Nonnull __NLow,     vDSP_Length * _Nonnull __NHigh ); ``` |

Modified [vDSP_vclipD()](https://developer.apple.com/documentation/accelerate/1450285-vdsp_vclipd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vclipD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     const double *__vDSP_C,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vclipD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     const double * _Nonnull __C,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vclr()](https://developer.apple.com/documentation/accelerate/1450402-vdsp_vclr)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vclr (     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vclr (     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vclrD()](https://developer.apple.com/documentation/accelerate/1450639-vdsp_vclrd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vclrD (     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vclrD (     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vcmprs()](https://developer.apple.com/documentation/accelerate/1450286-vdsp_vcmprs)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vcmprs (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vcmprs (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vcmprsD()](https://developer.apple.com/documentation/accelerate/1449861-vdsp_vcmprsd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vcmprsD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vcmprsD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vdbcon()](https://developer.apple.com/documentation/accelerate/1450241-vdsp_vdbcon)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdbcon (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     unsigned int __vDSP_F ); ``` |
| To | ``` void vDSP_vdbcon (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     unsigned int __F ); ``` |

Modified [vDSP_vdbconD()](https://developer.apple.com/documentation/accelerate/1449896-vdsp_vdbcond)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdbconD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     unsigned int __vDSP_F ); ``` |
| To | ``` void vDSP_vdbconD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     unsigned int __F ); ``` |

Modified [vDSP_vdist()](https://developer.apple.com/documentation/accelerate/1450257-vdsp_vdist)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdist (     const float *__vDSP_A,     vDSP_Stride __vDSP_I,     const float *__vDSP_B,     vDSP_Stride __vDSP_J,     float *__vDSP_C,     vDSP_Stride __vDSP_K,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vdist (     const float * _Nonnull __A,     vDSP_Stride __I,     const float * _Nonnull __B,     vDSP_Stride __J,     float * _Nonnull __C,     vDSP_Stride __K,     vDSP_Length __N ); ``` |

Modified [vDSP_vdistD()](https://developer.apple.com/documentation/accelerate/1449966-vdsp_vdistd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdistD (     const double *__vDSP_A,     vDSP_Stride __vDSP_I,     const double *__vDSP_B,     vDSP_Stride __vDSP_J,     double *__vDSP_C,     vDSP_Stride __vDSP_K,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vdistD (     const double * _Nonnull __A,     vDSP_Stride __I,     const double * _Nonnull __B,     vDSP_Stride __J,     double * _Nonnull __C,     vDSP_Stride __K,     vDSP_Length __N ); ``` |

Modified [vDSP_vdiv()](https://developer.apple.com/documentation/accelerate/1450243-vdsp_vdiv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdiv (     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vdiv (     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vdivD()](https://developer.apple.com/documentation/accelerate/1450126-vdsp_vdivd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdivD (     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vdivD (     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vdivi()](https://developer.apple.com/documentation/accelerate/1450839-vdsp_vdivi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdivi (     const int *__vDSP_B,     vDSP_Stride __vDSP_IB,     const int *__vDSP_A,     vDSP_Stride __vDSP_IA,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vdivi (     const int * _Nonnull __B,     vDSP_Stride __IB,     const int * _Nonnull __A,     vDSP_Stride __IA,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vdpsp()](https://developer.apple.com/documentation/accelerate/1450729-vdsp_vdpsp)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdpsp (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vdpsp (     const double * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_venvlp()](https://developer.apple.com/documentation/accelerate/1449964-vdsp_venvlp)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_venvlp (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_venvlp (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_venvlpD()](https://developer.apple.com/documentation/accelerate/1449687-vdsp_venvlpd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_venvlpD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_venvlpD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_veqvi()](https://developer.apple.com/documentation/accelerate/1450585-vdsp_veqvi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_veqvi (     const int *__vDSP_A,     vDSP_Stride __vDSP_IA,     const int *__vDSP_B,     vDSP_Stride __vDSP_IB,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_veqvi (     const int * _Nonnull __A,     vDSP_Stride __IA,     const int * _Nonnull __B,     vDSP_Stride __IB,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfill()](https://developer.apple.com/documentation/kernel/1579967-vdsp_vfill)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfill (     const float *__vDSP_A,     float *__vDSP_C,     vDSP_Stride __vDSP_IA,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfill (     const float * _Nonnull __A,     float * _Nonnull __C,     vDSP_Stride __IA,     vDSP_Length __N ); ``` |

Modified [vDSP_vfillD()](https://developer.apple.com/documentation/accelerate/1450171-vdsp_vfilld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfillD (     const double *__vDSP_A,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfillD (     const double * _Nonnull __A,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfilli()](https://developer.apple.com/documentation/accelerate/1450473-vdsp_vfilli)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfilli (     const int *__vDSP_A,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfilli (     const int * _Nonnull __A,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfix16()](https://developer.apple.com/documentation/accelerate/1449992-vdsp_vfix16)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfix16 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     short *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfix16 (     const float * _Nonnull __A,     vDSP_Stride __IA,     short * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfix16D()](https://developer.apple.com/documentation/accelerate/1450469-vdsp_vfix16d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfix16D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     short *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfix16D (     const double * _Nonnull __A,     vDSP_Stride __IA,     short * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfix32()](https://developer.apple.com/documentation/accelerate/1449976-vdsp_vfix32)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfix32 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfix32 (     const float * _Nonnull __A,     vDSP_Stride __IA,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfix32D()](https://developer.apple.com/documentation/accelerate/1450167-vdsp_vfix32d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfix32D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfix32D (     const double * _Nonnull __A,     vDSP_Stride __IA,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfix8()](https://developer.apple.com/documentation/accelerate/1450548-vdsp_vfix8)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfix8 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     char *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfix8 (     const float * _Nonnull __A,     vDSP_Stride __IA,     char * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfix8D()](https://developer.apple.com/documentation/accelerate/1450864-vdsp_vfix8d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfix8D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     char *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfix8D (     const double * _Nonnull __A,     vDSP_Stride __IA,     char * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixr16()](https://developer.apple.com/documentation/accelerate/1449925-vdsp_vfixr16)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixr16 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     short *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixr16 (     const float * _Nonnull __A,     vDSP_Stride __IA,     short * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixr16D()](https://developer.apple.com/documentation/accelerate/1450475-vdsp_vfixr16d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixr16D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     short *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixr16D (     const double * _Nonnull __A,     vDSP_Stride __IA,     short * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixr32()](https://developer.apple.com/documentation/accelerate/1450794-vdsp_vfixr32)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixr32 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixr32 (     const float * _Nonnull __A,     vDSP_Stride __IA,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixr32D()](https://developer.apple.com/documentation/accelerate/1450765-vdsp_vfixr32d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixr32D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixr32D (     const double * _Nonnull __A,     vDSP_Stride __IA,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixr8()](https://developer.apple.com/documentation/accelerate/1450408-vdsp_vfixr8)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixr8 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     char *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixr8 (     const float * _Nonnull __A,     vDSP_Stride __IA,     char * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixr8D()](https://developer.apple.com/documentation/accelerate/1449927-vdsp_vfixr8d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixr8D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     char *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixr8D (     const double * _Nonnull __A,     vDSP_Stride __IA,     char * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixru16()](https://developer.apple.com/documentation/accelerate/1450599-vdsp_vfixru16)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixru16 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned short *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixru16 (     const float * _Nonnull __A,     vDSP_Stride __IA,     unsigned short * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixru16D()](https://developer.apple.com/documentation/accelerate/1450082-vdsp_vfixru16d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixru16D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned short *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixru16D (     const double * _Nonnull __A,     vDSP_Stride __IA,     unsigned short * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixru32()](https://developer.apple.com/documentation/accelerate/1449735-vdsp_vfixru32)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixru32 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixru32 (     const float * _Nonnull __A,     vDSP_Stride __IA,     unsigned int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixru32D()](https://developer.apple.com/documentation/accelerate/1450065-vdsp_vfixru32d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixru32D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixru32D (     const double * _Nonnull __A,     vDSP_Stride __IA,     unsigned int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixru8()](https://developer.apple.com/documentation/accelerate/1449777-vdsp_vfixru8)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixru8 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned char *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixru8 (     const float * _Nonnull __A,     vDSP_Stride __IA,     unsigned char * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixru8D()](https://developer.apple.com/documentation/accelerate/1449847-vdsp_vfixru8d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixru8D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned char *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixru8D (     const double * _Nonnull __A,     vDSP_Stride __IA,     unsigned char * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixu16()](https://developer.apple.com/documentation/accelerate/1449834-vdsp_vfixu16)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixu16 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned short *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixu16 (     const float * _Nonnull __A,     vDSP_Stride __IA,     unsigned short * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixu16D()](https://developer.apple.com/documentation/accelerate/1449908-vdsp_vfixu16d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixu16D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned short *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixu16D (     const double * _Nonnull __A,     vDSP_Stride __IA,     unsigned short * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixu32()](https://developer.apple.com/documentation/accelerate/1450173-vdsp_vfixu32)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixu32 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixu32 (     const float * _Nonnull __A,     vDSP_Stride __IA,     unsigned int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixu32D()](https://developer.apple.com/documentation/accelerate/1450846-vdsp_vfixu32d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixu32D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixu32D (     const double * _Nonnull __A,     vDSP_Stride __IA,     unsigned int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixu8()](https://developer.apple.com/documentation/accelerate/1450800-vdsp_vfixu8)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixu8 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned char *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixu8 (     const float * _Nonnull __A,     vDSP_Stride __IA,     unsigned char * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfixu8D()](https://developer.apple.com/documentation/accelerate/1450868-vdsp_vfixu8d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfixu8D (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     unsigned char *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfixu8D (     const double * _Nonnull __A,     vDSP_Stride __IA,     unsigned char * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vflt16()](https://developer.apple.com/documentation/accelerate/1450096-vdsp_vflt16)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vflt16 (     const short *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vflt16 (     const short * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vflt16D()](https://developer.apple.com/documentation/accelerate/1450208-vdsp_vflt16d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vflt16D (     const short *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vflt16D (     const short * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vflt24()](https://developer.apple.com/documentation/accelerate/1450529-vdsp_vflt24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vflt24 (     const vDSP_int24 *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vflt24 (     const vDSP_int24 * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vflt32()](https://developer.apple.com/documentation/kernel/1532181-vdsp_vflt32)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vflt32 (     const int *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vflt32 (     const int * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vflt32D()](https://developer.apple.com/documentation/accelerate/1450342-vdsp_vflt32d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vflt32D (     const int *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vflt32D (     const int * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vflt8()](https://developer.apple.com/documentation/accelerate/1450742-vdsp_vflt8)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vflt8 (     const char *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vflt8 (     const char * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vflt8D()](https://developer.apple.com/documentation/accelerate/1449894-vdsp_vflt8d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vflt8D (     const char *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vflt8D (     const char * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfltsm24()](https://developer.apple.com/documentation/accelerate/1450177-vdsp_vfltsm24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfltsm24 (     const vDSP_int24 *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfltsm24 (     const vDSP_int24 * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfltsmu24()](https://developer.apple.com/documentation/accelerate/1449841-vdsp_vfltsmu24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfltsmu24 (     const vDSP_uint24 *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfltsmu24 (     const vDSP_uint24 * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfltu16()](https://developer.apple.com/documentation/accelerate/1450118-vdsp_vfltu16)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfltu16 (     const unsigned short *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfltu16 (     const unsigned short * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfltu16D()](https://developer.apple.com/documentation/accelerate/1450769-vdsp_vfltu16d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfltu16D (     const unsigned short *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfltu16D (     const unsigned short * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfltu24()](https://developer.apple.com/documentation/accelerate/1450084-vdsp_vfltu24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfltu24 (     const vDSP_uint24 *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfltu24 (     const vDSP_uint24 * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfltu32()](https://developer.apple.com/documentation/accelerate/1450255-vdsp_vfltu32)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfltu32 (     const unsigned int *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfltu32 (     const unsigned int * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfltu32D()](https://developer.apple.com/documentation/accelerate/1449794-vdsp_vfltu32d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfltu32D (     const unsigned int *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfltu32D (     const unsigned int * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfltu8()](https://developer.apple.com/documentation/accelerate/1450549-vdsp_vfltu8)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfltu8 (     const unsigned char *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfltu8 (     const unsigned char * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfltu8D()](https://developer.apple.com/documentation/accelerate/1450104-vdsp_vfltu8d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfltu8D (     const unsigned char *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfltu8D (     const unsigned char * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfrac()](https://developer.apple.com/documentation/accelerate/1450336-vdsp_vfrac)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfrac (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfrac (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfracD()](https://developer.apple.com/documentation/accelerate/1449948-vdsp_vfracd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfracD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfracD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vgathr()](https://developer.apple.com/documentation/accelerate/1449749-vdsp_vgathr)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vgathr (     const float *__vDSP_A,     const vDSP_Length *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vgathr (     const float * _Nonnull __A,     const vDSP_Length * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vgathra()](https://developer.apple.com/documentation/accelerate/1450261-vdsp_vgathra)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vgathra (     const float **__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vgathra (     const float * _Nonnull * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vgathraD()](https://developer.apple.com/documentation/accelerate/1449865-vdsp_vgathrad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vgathraD (     const double **__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vgathraD (     const double * _Nonnull * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vgathrD()](https://developer.apple.com/documentation/accelerate/1449921-vdsp_vgathrd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vgathrD (     const double *__vDSP_A,     const vDSP_Length *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vgathrD (     const double * _Nonnull __A,     const vDSP_Length * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vgen()](https://developer.apple.com/documentation/accelerate/1449703-vdsp_vgen)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vgen (     const float *__vDSP_A,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vgen (     const float * _Nonnull __A,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vgenD()](https://developer.apple.com/documentation/accelerate/1450583-vdsp_vgend)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vgenD (     const double *__vDSP_A,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vgenD (     const double * _Nonnull __A,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vgenp()](https://developer.apple.com/documentation/accelerate/1449771-vdsp_vgenp)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vgenp (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_M ); ``` |
| To | ``` void vDSP_vgenp (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __M ); ``` |

Modified [vDSP_vgenpD()](https://developer.apple.com/documentation/accelerate/1450645-vdsp_vgenpd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vgenpD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_M ); ``` |
| To | ``` void vDSP_vgenpD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __M ); ``` |

Modified [vDSP_viclip()](https://developer.apple.com/documentation/accelerate/1450512-vdsp_viclip)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_viclip (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_viclip (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_viclipD()](https://developer.apple.com/documentation/accelerate/1450559-vdsp_viclipd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_viclipD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     const double *__vDSP_C,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_viclipD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     const double * _Nonnull __C,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vindex()](https://developer.apple.com/documentation/accelerate/1449792-vdsp_vindex)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vindex (     const float *__vDSP_A,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vindex (     const float * _Nonnull __A,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vindexD()](https://developer.apple.com/documentation/accelerate/1449958-vdsp_vindexd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vindexD (     const double *__vDSP_A,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vindexD (     const double * _Nonnull __A,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vintb()](https://developer.apple.com/documentation/accelerate/1449705-vdsp_vintb)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vintb (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vintb (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vintbD()](https://developer.apple.com/documentation/accelerate/1449968-vdsp_vintbd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vintbD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vintbD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vlim()](https://developer.apple.com/documentation/accelerate/1450525-vdsp_vlim)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vlim (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vlim (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vlimD()](https://developer.apple.com/documentation/accelerate/1450709-vdsp_vlimd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vlimD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     const double *__vDSP_C,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vlimD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     const double * _Nonnull __C,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vlint()](https://developer.apple.com/documentation/accelerate/1449775-vdsp_vlint)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vlint (     const float *__vDSP_A,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_M ); ``` |
| To | ``` void vDSP_vlint (     const float * _Nonnull __A,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __M ); ``` |

Modified [vDSP_vlintD()](https://developer.apple.com/documentation/accelerate/1449733-vdsp_vlintd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vlintD (     const double *__vDSP_A,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_M ); ``` |
| To | ``` void vDSP_vlintD (     const double * _Nonnull __A,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __M ); ``` |

Modified [vDSP_vma()](https://developer.apple.com/documentation/kernel/1532193-vdsp_vma)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vma (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vma (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vmaD()](https://developer.apple.com/documentation/accelerate/1450825-vdsp_vmad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmaD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmaD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vmax()](https://developer.apple.com/documentation/kernel/1579953-vdsp_vmax)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmax (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmax (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vmaxD()](https://developer.apple.com/documentation/accelerate/1449938-vdsp_vmaxd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmaxD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmaxD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vmaxmg()](https://developer.apple.com/documentation/accelerate/1450295-vdsp_vmaxmg)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmaxmg (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmaxmg (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vmaxmgD()](https://developer.apple.com/documentation/accelerate/1449767-vdsp_vmaxmgd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmaxmgD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmaxmgD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vmin()](https://developer.apple.com/documentation/accelerate/1450216-vdsp_vmin)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmin (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmin (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vminD()](https://developer.apple.com/documentation/accelerate/1450601-vdsp_vmind)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vminD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vminD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vminmg()](https://developer.apple.com/documentation/accelerate/1450293-vdsp_vminmg)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vminmg (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vminmg (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vminmgD()](https://developer.apple.com/documentation/accelerate/1449680-vdsp_vminmgd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vminmgD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vminmgD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vmma()](https://developer.apple.com/documentation/accelerate/1450802-vdsp_vmma)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmma (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     const float *__vDSP_D,     vDSP_Stride __vDSP_ID,     float *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmma (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     const float * _Nonnull __D,     vDSP_Stride __ID,     float * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vmmaD()](https://developer.apple.com/documentation/accelerate/1450527-vdsp_vmmad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmmaD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     const double *__vDSP_D,     vDSP_Stride __vDSP_ID,     double *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmmaD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     const double * _Nonnull __D,     vDSP_Stride __ID,     double * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vmmsb()](https://developer.apple.com/documentation/accelerate/1450613-vdsp_vmmsb)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmmsb (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     const float *__vDSP_D,     vDSP_Stride __vDSP_ID,     float *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmmsb (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     const float * _Nonnull __D,     vDSP_Stride __ID,     float * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vmmsbD()](https://developer.apple.com/documentation/accelerate/1450418-vdsp_vmmsbd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmmsbD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     const double *__vDSP_D,     vDSP_Stride __vDSP_ID,     double *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmmsbD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     const double * _Nonnull __D,     vDSP_Stride __ID,     double * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vmsa()](https://developer.apple.com/documentation/accelerate/1450590-vdsp_vmsa)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmsa (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmsa (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vmsaD()](https://developer.apple.com/documentation/accelerate/1450698-vdsp_vmsad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmsaD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmsaD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vmsb()](https://developer.apple.com/documentation/accelerate/1450451-vdsp_vmsb)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmsb (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmsb (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vmsbD()](https://developer.apple.com/documentation/accelerate/1450609-vdsp_vmsbd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmsbD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmsbD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vmul()](https://developer.apple.com/documentation/accelerate/1450344-vdsp_vmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmul (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmul (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vmulD()](https://developer.apple.com/documentation/accelerate/1450138-vdsp_vmuld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmulD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmulD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vnabs()](https://developer.apple.com/documentation/accelerate/1450420-vdsp_vnabs)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vnabs (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vnabs (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vnabsD()](https://developer.apple.com/documentation/accelerate/1450259-vdsp_vnabsd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vnabsD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vnabsD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vneg()](https://developer.apple.com/documentation/accelerate/1450204-vdsp_vneg)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vneg (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vneg (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vnegD()](https://developer.apple.com/documentation/accelerate/1450346-vdsp_vnegd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vnegD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vnegD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vpoly()](https://developer.apple.com/documentation/accelerate/1450623-vdsp_vpoly)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vpoly (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_vpoly (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_vpolyD()](https://developer.apple.com/documentation/accelerate/1450503-vdsp_vpolyd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vpolyD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_vpolyD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_vpythg()](https://developer.apple.com/documentation/accelerate/1450824-vdsp_vpythg)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vpythg (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     const float *__vDSP_D,     vDSP_Stride __vDSP_ID,     float *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vpythg (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     const float * _Nonnull __D,     vDSP_Stride __ID,     float * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vpythgD()](https://developer.apple.com/documentation/accelerate/1449766-vdsp_vpythgd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vpythgD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     const double *__vDSP_D,     vDSP_Stride __vDSP_ID,     double *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vpythgD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     const double * _Nonnull __D,     vDSP_Stride __ID,     double * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vqint()](https://developer.apple.com/documentation/accelerate/1449942-vdsp_vqint)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vqint (     const float *__vDSP_A,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_M ); ``` |
| To | ``` void vDSP_vqint (     const float * _Nonnull __A,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __M ); ``` |

Modified [vDSP_vqintD()](https://developer.apple.com/documentation/accelerate/1450491-vdsp_vqintd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vqintD (     const double *__vDSP_A,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_M ); ``` |
| To | ``` void vDSP_vqintD (     const double * _Nonnull __A,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __M ); ``` |

Modified [vDSP_vramp()](https://developer.apple.com/documentation/accelerate/1450369-vdsp_vramp)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vramp (     const float *__vDSP_A,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vramp (     const float * _Nonnull __A,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampD()](https://developer.apple.com/documentation/accelerate/1449999-vdsp_vrampd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampD (     const double *__vDSP_A,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampD (     const double * _Nonnull __A,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmul()](https://developer.apple.com/documentation/accelerate/1450226-vdsp_vrampmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmul (     const float *__vDSP_I,     vDSP_Stride __vDSP_IS,     float *__vDSP_Start,     const float *__vDSP_Step,     float *__vDSP_O,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmul (     const float * _Nonnull __I,     vDSP_Stride __IS,     float * _Nonnull __Start,     const float * _Nonnull __Step,     float * _Nonnull __O,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmul2()](https://developer.apple.com/documentation/accelerate/1449695-vdsp_vrampmul2)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmul2 (     const float *__vDSP_I0,     const float *__vDSP_I1,     vDSP_Stride __vDSP_IS,     float *__vDSP_Start,     const float *__vDSP_Step,     float *__vDSP_O0,     float *__vDSP_O1,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmul2 (     const float * _Nonnull __I0,     const float * _Nonnull __I1,     vDSP_Stride __IS,     float * _Nonnull __Start,     const float * _Nonnull __Step,     float * _Nonnull __O0,     float * _Nonnull __O1,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmul2_s1_15()](https://developer.apple.com/documentation/accelerate/1449788-vdsp_vrampmul2_s1_15)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmul2_s1_15 (     const short *__vDSP_I0,     const short *__vDSP_I1,     vDSP_Stride __vDSP_IS,     short *__vDSP_Start,     const short *__vDSP_Step,     short *__vDSP_O0,     short *__vDSP_O1,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmul2_s1_15 (     const short * _Nonnull __I0,     const short * _Nonnull __I1,     vDSP_Stride __IS,     short * _Nonnull __Start,     const short * _Nonnull __Step,     short * _Nonnull __O0,     short * _Nonnull __O1,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmul2_s8_24()](https://developer.apple.com/documentation/accelerate/1449936-vdsp_vrampmul2_s8_24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmul2_s8_24 (     const int *__vDSP_I0,     const int *__vDSP_I1,     vDSP_Stride __vDSP_IS,     int *__vDSP_Start,     const int *__vDSP_Step,     int *__vDSP_O0,     int *__vDSP_O1,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmul2_s8_24 (     const int * _Nonnull __I0,     const int * _Nonnull __I1,     vDSP_Stride __IS,     int * _Nonnull __Start,     const int * _Nonnull __Step,     int * _Nonnull __O0,     int * _Nonnull __O1,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmul2D()](https://developer.apple.com/documentation/accelerate/1449829-vdsp_vrampmul2d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmul2D (     const double *__vDSP_I0,     const double *__vDSP_I1,     vDSP_Stride __vDSP_IS,     double *__vDSP_Start,     const double *__vDSP_Step,     double *__vDSP_O0,     double *__vDSP_O1,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmul2D (     const double * _Nonnull __I0,     const double * _Nonnull __I1,     vDSP_Stride __IS,     double * _Nonnull __Start,     const double * _Nonnull __Step,     double * _Nonnull __O0,     double * _Nonnull __O1,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmul_s1_15()](https://developer.apple.com/documentation/accelerate/1449877-vdsp_vrampmul_s1_15)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmul_s1_15 (     const short *__vDSP_I,     vDSP_Stride __vDSP_IS,     short *__vDSP_Start,     const short *__vDSP_Step,     short *__vDSP_O,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmul_s1_15 (     const short * _Nonnull __I,     vDSP_Stride __IS,     short * _Nonnull __Start,     const short * _Nonnull __Step,     short * _Nonnull __O,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmul_s8_24()](https://developer.apple.com/documentation/accelerate/1450008-vdsp_vrampmul_s8_24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmul_s8_24 (     const int *__vDSP_I,     vDSP_Stride __vDSP_IS,     int *__vDSP_Start,     const int *__vDSP_Step,     int *__vDSP_O,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmul_s8_24 (     const int * _Nonnull __I,     vDSP_Stride __IS,     int * _Nonnull __Start,     const int * _Nonnull __Step,     int * _Nonnull __O,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmuladd()](https://developer.apple.com/documentation/accelerate/1450042-vdsp_vrampmuladd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmuladd (     const float *__vDSP_I,     vDSP_Stride __vDSP_IS,     float *__vDSP_Start,     const float *__vDSP_Step,     float *__vDSP_O,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmuladd (     const float * _Nonnull __I,     vDSP_Stride __IS,     float * _Nonnull __Start,     const float * _Nonnull __Step,     float * _Nonnull __O,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmuladd2()](https://developer.apple.com/documentation/accelerate/1450406-vdsp_vrampmuladd2)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmuladd2 (     const float *__vDSP_I0,     const float *__vDSP_I1,     vDSP_Stride __vDSP_IS,     float *__vDSP_Start,     const float *__vDSP_Step,     float *__vDSP_O0,     float *__vDSP_O1,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmuladd2 (     const float * _Nonnull __I0,     const float * _Nonnull __I1,     vDSP_Stride __IS,     float * _Nonnull __Start,     const float * _Nonnull __Step,     float * _Nonnull __O0,     float * _Nonnull __O1,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmuladd2_s1_15()](https://developer.apple.com/documentation/accelerate/1450845-vdsp_vrampmuladd2_s1_15)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmuladd2_s1_15 (     const short *__vDSP_I0,     const short *__vDSP_I1,     vDSP_Stride __vDSP_IS,     short *__vDSP_Start,     const short *__vDSP_Step,     short *__vDSP_O0,     short *__vDSP_O1,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmuladd2_s1_15 (     const short * _Nonnull __I0,     const short * _Nonnull __I1,     vDSP_Stride __IS,     short * _Nonnull __Start,     const short * _Nonnull __Step,     short * _Nonnull __O0,     short * _Nonnull __O1,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmuladd2_s8_24()](https://developer.apple.com/documentation/accelerate/1450046-vdsp_vrampmuladd2_s8_24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmuladd2_s8_24 (     const int *__vDSP_I0,     const int *__vDSP_I1,     vDSP_Stride __vDSP_IS,     int *__vDSP_Start,     const int *__vDSP_Step,     int *__vDSP_O0,     int *__vDSP_O1,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmuladd2_s8_24 (     const int * _Nonnull __I0,     const int * _Nonnull __I1,     vDSP_Stride __IS,     int * _Nonnull __Start,     const int * _Nonnull __Step,     int * _Nonnull __O0,     int * _Nonnull __O1,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmuladd2D()](https://developer.apple.com/documentation/accelerate/1450349-vdsp_vrampmuladd2d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmuladd2D (     const double *__vDSP_I0,     const double *__vDSP_I1,     vDSP_Stride __vDSP_IS,     double *__vDSP_Start,     const double *__vDSP_Step,     double *__vDSP_O0,     double *__vDSP_O1,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmuladd2D (     const double * _Nonnull __I0,     const double * _Nonnull __I1,     vDSP_Stride __IS,     double * _Nonnull __Start,     const double * _Nonnull __Step,     double * _Nonnull __O0,     double * _Nonnull __O1,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmuladd_s1_15()](https://developer.apple.com/documentation/accelerate/1450758-vdsp_vrampmuladd_s1_15)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmuladd_s1_15 (     const short *__vDSP_I,     vDSP_Stride __vDSP_IS,     short *__vDSP_Start,     const short *__vDSP_Step,     short *__vDSP_O,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmuladd_s1_15 (     const short * _Nonnull __I,     vDSP_Stride __IS,     short * _Nonnull __Start,     const short * _Nonnull __Step,     short * _Nonnull __O,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmuladd_s8_24()](https://developer.apple.com/documentation/accelerate/1450347-vdsp_vrampmuladd_s8_24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmuladd_s8_24 (     const int *__vDSP_I,     vDSP_Stride __vDSP_IS,     int *__vDSP_Start,     const int *__vDSP_Step,     int *__vDSP_O,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmuladd_s8_24 (     const int * _Nonnull __I,     vDSP_Stride __IS,     int * _Nonnull __Start,     const int * _Nonnull __Step,     int * _Nonnull __O,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmuladdD()](https://developer.apple.com/documentation/accelerate/1449717-vdsp_vrampmuladdd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmuladdD (     const double *__vDSP_I,     vDSP_Stride __vDSP_IS,     double *__vDSP_Start,     const double *__vDSP_Step,     double *__vDSP_O,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmuladdD (     const double * _Nonnull __I,     vDSP_Stride __IS,     double * _Nonnull __Start,     const double * _Nonnull __Step,     double * _Nonnull __O,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrampmulD()](https://developer.apple.com/documentation/accelerate/1450707-vdsp_vrampmuld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrampmulD (     const double *__vDSP_I,     vDSP_Stride __vDSP_IS,     double *__vDSP_Start,     const double *__vDSP_Step,     double *__vDSP_O,     vDSP_Stride __vDSP_OS,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrampmulD (     const double * _Nonnull __I,     vDSP_Stride __IS,     double * _Nonnull __Start,     const double * _Nonnull __Step,     double * _Nonnull __O,     vDSP_Stride __OS,     vDSP_Length __N ); ``` |

Modified [vDSP_vrsum()](https://developer.apple.com/documentation/accelerate/1450245-vdsp_vrsum)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrsum (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_S,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrsum (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __S,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vrsumD()](https://developer.apple.com/documentation/accelerate/1450713-vdsp_vrsumd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrsumD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_S,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrsumD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __S,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vrvrs()](https://developer.apple.com/documentation/accelerate/1450290-vdsp_vrvrs)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrvrs (     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrvrs (     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vrvrsD()](https://developer.apple.com/documentation/accelerate/1449825-vdsp_vrvrsd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vrvrsD (     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vrvrsD (     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsadd()](https://developer.apple.com/documentation/kernel/1579993-vdsp_vsadd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsadd (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsadd (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsaddD()](https://developer.apple.com/documentation/accelerate/1450860-vdsp_vsaddd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsaddD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsaddD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsaddi()](https://developer.apple.com/documentation/accelerate/1450088-vdsp_vsaddi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsaddi (     const int *__vDSP_A,     vDSP_Stride __vDSP_IA,     const int *__vDSP_B,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsaddi (     const int * _Nonnull __A,     vDSP_Stride __IA,     const int * _Nonnull __B,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsbm()](https://developer.apple.com/documentation/accelerate/1449914-vdsp_vsbm)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsbm (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsbm (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vsbmD()](https://developer.apple.com/documentation/accelerate/1450334-vdsp_vsbmd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsbmD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsbmD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vsbsbm()](https://developer.apple.com/documentation/accelerate/1449761-vdsp_vsbsbm)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsbsbm (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     const float *__vDSP_D,     vDSP_Stride __vDSP_ID,     float *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsbsbm (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     const float * _Nonnull __D,     vDSP_Stride __ID,     float * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vsbsbmD()](https://developer.apple.com/documentation/accelerate/1449707-vdsp_vsbsbmd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsbsbmD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     const double *__vDSP_D,     vDSP_Stride __vDSP_ID,     double *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsbsbmD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     vDSP_Stride __IC,     const double * _Nonnull __D,     vDSP_Stride __ID,     double * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vsbsm()](https://developer.apple.com/documentation/accelerate/1450734-vdsp_vsbsm)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsbsm (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsbsm (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vsbsmD()](https://developer.apple.com/documentation/accelerate/1450372-vdsp_vsbsmd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsbsmD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_C,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsbsmD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __C,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vsdiv()](https://developer.apple.com/documentation/accelerate/1450680-vdsp_vsdiv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsdiv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsdiv (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsdivD()](https://developer.apple.com/documentation/accelerate/1450212-vdsp_vsdivd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsdivD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsdivD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsdivi()](https://developer.apple.com/documentation/accelerate/1449689-vdsp_vsdivi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsdivi (     const int *__vDSP_A,     vDSP_Stride __vDSP_IA,     const int *__vDSP_B,     int *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsdivi (     const int * _Nonnull __A,     vDSP_Stride __IA,     const int * _Nonnull __B,     int * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsimps()](https://developer.apple.com/documentation/accelerate/1450644-vdsp_vsimps)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsimps (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsimps (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsimpsD()](https://developer.apple.com/documentation/accelerate/1450112-vdsp_vsimpsd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsimpsD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsimpsD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsma()](https://developer.apple.com/documentation/accelerate/1450271-vdsp_vsma)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsma (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsma (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     const float * _Nonnull __C,     vDSP_Stride __IC,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmaD()](https://developer.apple.com/documentation/accelerate/1449759-vdsp_vsmad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmaD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmaD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     const double * _Nonnull __C,     vDSP_Stride __IC,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmfix24()](https://developer.apple.com/documentation/accelerate/1449670-vdsp_vsmfix24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmfix24 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_int24 *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmfix24 (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_int24 * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmfixu24()](https://developer.apple.com/documentation/kernel/1532178-vdsp_vsmfixu24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmfixu24 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_uint24 *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmfixu24 (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_uint24 * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmsa()](https://developer.apple.com/documentation/accelerate/1450380-vdsp_vsmsa)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmsa (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmsa (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmsaD()](https://developer.apple.com/documentation/accelerate/1450432-vdsp_vsmsad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmsaD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     const double *__vDSP_C,     double *__vDSP_ID,     vDSP_Stride __vDSP_L,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmsaD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     const double * _Nonnull __C,     double * _Nonnull __ID,     vDSP_Stride __L,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmsb()](https://developer.apple.com/documentation/accelerate/1450822-vdsp_vsmsb)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmsb (     const float *__vDSP_A,     vDSP_Stride __vDSP_I,     const float *__vDSP_B,     const float *__vDSP_C,     vDSP_Stride __vDSP_K,     float *__vDSP_D,     vDSP_Stride __vDSP_L,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmsb (     const float * _Nonnull __A,     vDSP_Stride __I,     const float * _Nonnull __B,     const float * _Nonnull __C,     vDSP_Stride __K,     float * _Nonnull __D,     vDSP_Stride __L,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmsbD()](https://developer.apple.com/documentation/accelerate/1450238-vdsp_vsmsbd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmsbD (     const double *__vDSP_A,     vDSP_Stride __vDSP_I,     const double *__vDSP_B,     const double *__vDSP_C,     vDSP_Stride __vDSP_K,     double *__vDSP_D,     vDSP_Stride __vDSP_L,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmsbD (     const double * _Nonnull __A,     vDSP_Stride __I,     const double * _Nonnull __B,     const double * _Nonnull __C,     vDSP_Stride __K,     double * _Nonnull __D,     vDSP_Stride __L,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmsma()](https://developer.apple.com/documentation/accelerate/1450324-vdsp_vsmsma)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmsma (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     const float *__vDSP_D,     float *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmsma (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     const float * _Nonnull __C,     vDSP_Stride __IC,     const float * _Nonnull __D,     float * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmsmaD()](https://developer.apple.com/documentation/accelerate/1449850-vdsp_vsmsmad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmsmaD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     const double *__vDSP_C,     vDSP_Stride __vDSP_IC,     const double *__vDSP_D,     double *__vDSP_E,     vDSP_Stride __vDSP_IE,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmsmaD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     const double * _Nonnull __C,     vDSP_Stride __IC,     const double * _Nonnull __D,     double * _Nonnull __E,     vDSP_Stride __IE,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmul()](https://developer.apple.com/documentation/kernel/1532223-vdsp_vsmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmul (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmul (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmulD()](https://developer.apple.com/documentation/accelerate/1449676-vdsp_vsmuld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmulD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmulD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsort()](https://developer.apple.com/documentation/accelerate/1449747-vdsp_vsort)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsort (     float *__vDSP_C,     vDSP_Length __vDSP_N,     int __vDSP_Order ); ``` |
| To | ``` void vDSP_vsort (     float * _Nonnull __C,     vDSP_Length __N,     int __Order ); ``` |

Modified [vDSP_vsortD()](https://developer.apple.com/documentation/accelerate/1450482-vdsp_vsortd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsortD (     double *__vDSP_C,     vDSP_Length __vDSP_N,     int __vDSP_Order ); ``` |
| To | ``` void vDSP_vsortD (     double * _Nonnull __C,     vDSP_Length __N,     int __Order ); ``` |

Modified [vDSP_vsorti()](https://developer.apple.com/documentation/accelerate/1450736-vdsp_vsorti)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsorti (     const float *__vDSP_C,     vDSP_Length *__vDSP_I,     vDSP_Length *__vDSP_Temporary,     vDSP_Length __vDSP_N,     int __vDSP_Order ); ``` |
| To | ``` void vDSP_vsorti (     const float * _Nonnull __C,     vDSP_Length * _Nonnull __I,     vDSP_Length * _Nullable __Temporary,     vDSP_Length __N,     int __Order ); ``` |

Modified [vDSP_vsortiD()](https://developer.apple.com/documentation/accelerate/1450858-vdsp_vsortid)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsortiD (     const double *__vDSP_C,     vDSP_Length *__vDSP_I,     vDSP_Length *__vDSP_Temporary,     vDSP_Length __vDSP_N,     int __vDSP_Order ); ``` |
| To | ``` void vDSP_vsortiD (     const double * _Nonnull __C,     vDSP_Length * _Nonnull __I,     vDSP_Length * _Nullable __Temporary,     vDSP_Length __N,     int __Order ); ``` |

Modified [vDSP_vspdp()](https://developer.apple.com/documentation/accelerate/1450265-vdsp_vspdp)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vspdp (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vspdp (     const float * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsq()](https://developer.apple.com/documentation/accelerate/1450611-vdsp_vsq)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsq (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsq (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsqD()](https://developer.apple.com/documentation/accelerate/1450841-vdsp_vsqd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsqD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsqD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vssq()](https://developer.apple.com/documentation/accelerate/1450445-vdsp_vssq)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vssq (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vssq (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vssqD()](https://developer.apple.com/documentation/accelerate/1450363-vdsp_vssqd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vssqD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vssqD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsub()](https://developer.apple.com/documentation/accelerate/1449900-vdsp_vsub)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsub (     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsub (     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsubD()](https://developer.apple.com/documentation/accelerate/1449743-vdsp_vsubd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsubD (     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsubD (     const double * _Nonnull __B,     vDSP_Stride __IB,     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vswap()](https://developer.apple.com/documentation/accelerate/1450661-vdsp_vswap)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vswap (     float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_B,     vDSP_Stride __vDSP_IB,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vswap (     float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __B,     vDSP_Stride __IB,     vDSP_Length __N ); ``` |

Modified [vDSP_vswapD()](https://developer.apple.com/documentation/accelerate/1450555-vdsp_vswapd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vswapD (     double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_B,     vDSP_Stride __vDSP_IB,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vswapD (     double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __B,     vDSP_Stride __IB,     vDSP_Length __N ); ``` |

Modified [vDSP_vswmax()](https://developer.apple.com/documentation/kernel/1579990-vdsp_vswmax)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vswmax (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_WindowLength ); ``` |
| To | ``` void vDSP_vswmax (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __WindowLength ); ``` |

Modified [vDSP_vswmaxD()](https://developer.apple.com/documentation/accelerate/1450322-vdsp_vswmaxd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vswmaxD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_WindowLength ); ``` |
| To | ``` void vDSP_vswmaxD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __WindowLength ); ``` |

Modified [vDSP_vswsum()](https://developer.apple.com/documentation/accelerate/1449822-vdsp_vswsum)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vswsum (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_vswsum (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_vswsumD()](https://developer.apple.com/documentation/accelerate/1449693-vdsp_vswsumd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vswsumD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_vswsumD (     const double * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_vtabi()](https://developer.apple.com/documentation/accelerate/1450762-vdsp_vtabi)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vtabi (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_S1,     const float *__vDSP_S2,     const float *__vDSP_C,     vDSP_Length __vDSP_M,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vtabi (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __S1,     const float * _Nonnull __S2,     const float * _Nonnull __C,     vDSP_Length __M,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vtabiD()](https://developer.apple.com/documentation/accelerate/1449832-vdsp_vtabid)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vtabiD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_S1,     const double *__vDSP_S2,     const double *__vDSP_C,     vDSP_Length __vDSP_M,     double *__vDSP_ID,     vDSP_Stride __vDSP_L,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vtabiD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __S1,     const double * _Nonnull __S2,     const double * _Nonnull __C,     vDSP_Length __M,     double * _Nonnull __ID,     vDSP_Stride __L,     vDSP_Length __N ); ``` |

Modified [vDSP_vthr()](https://developer.apple.com/documentation/accelerate/1450030-vdsp_vthr)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vthr (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vthr (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vthrD()](https://developer.apple.com/documentation/accelerate/1450834-vdsp_vthrd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vthrD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vthrD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vthres()](https://developer.apple.com/documentation/accelerate/1450597-vdsp_vthres)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vthres (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vthres (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vthresD()](https://developer.apple.com/documentation/accelerate/1450767-vdsp_vthresd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vthresD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vthresD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vthrsc()](https://developer.apple.com/documentation/accelerate/1450631-vdsp_vthrsc)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vthrsc (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vthrsc (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vthrscD()](https://developer.apple.com/documentation/accelerate/1450230-vdsp_vthrscd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vthrscD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     const double *__vDSP_C,     double *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vthrscD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     const double * _Nonnull __C,     double * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vtmerg()](https://developer.apple.com/documentation/accelerate/1450140-vdsp_vtmerg)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vtmerg (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vtmerg (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vtmergD()](https://developer.apple.com/documentation/accelerate/1450175-vdsp_vtmergd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vtmergD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vtmergD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vtrapz()](https://developer.apple.com/documentation/accelerate/1450678-vdsp_vtrapz)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vtrapz (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vtrapz (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vtrapzD()](https://developer.apple.com/documentation/accelerate/1450810-vdsp_vtrapzd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vtrapzD (     const double *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vtrapzD (     const double * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_wiener()](https://developer.apple.com/documentation/accelerate/1450711-vdsp_wiener)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_wiener (     vDSP_Length __vDSP_L,     const float *__vDSP_A,     const float *__vDSP_C,     float *__vDSP_F,     float *__vDSP_P,     int __vDSP_Flag,     int *__vDSP_Error ); ``` |
| To | ``` void vDSP_wiener (     vDSP_Length __L,     const float * _Nonnull __A,     const float * _Nonnull __C,     float * _Nonnull __F,     float * _Nonnull __P,     int __Flag,     int * _Nonnull __Error ); ``` |

Modified [vDSP_wienerD()](https://developer.apple.com/documentation/accelerate/1450592-vdsp_wienerd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_wienerD (     vDSP_Length __vDSP_L,     const double *__vDSP_A,     const double *__vDSP_C,     double *__vDSP_F,     double *__vDSP_P,     int __vDSP_Flag,     int *__vDSP_Error ); ``` |
| To | ``` void vDSP_wienerD (     vDSP_Length __L,     const double * _Nonnull __A,     const double * _Nonnull __C,     double * _Nonnull __F,     double * _Nonnull __P,     int __Flag,     int * _Nonnull __Error ); ``` |

Modified [vDSP_zaspec()](https://developer.apple.com/documentation/accelerate/1449691-vdsp_zaspec)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zaspec (     const DSPSplitComplex *__vDSP_A,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zaspec (     const DSPSplitComplex * _Nonnull __A,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zaspecD()](https://developer.apple.com/documentation/accelerate/1450746-vdsp_zaspecd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zaspecD (     const DSPDoubleSplitComplex *__vDSP_A,     double *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zaspecD (     const DSPDoubleSplitComplex * _Nonnull __A,     double * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zcoher()](https://developer.apple.com/documentation/accelerate/1450253-vdsp_zcoher)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zcoher (     const float *__vDSP_A,     const float *__vDSP_B,     const DSPSplitComplex *__vDSP_C,     float *__vDSP_D,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zcoher (     const float * _Nonnull __A,     const float * _Nonnull __B,     const DSPSplitComplex * _Nonnull __C,     float * _Nonnull __D,     vDSP_Length __N ); ``` |

Modified [vDSP_zcoherD()](https://developer.apple.com/documentation/accelerate/1450001-vdsp_zcoherd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zcoherD (     const double *__vDSP_A,     const double *__vDSP_B,     const DSPDoubleSplitComplex *__vDSP_C,     double *__vDSP_D,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zcoherD (     const double * _Nonnull __A,     const double * _Nonnull __B,     const DSPDoubleSplitComplex * _Nonnull __C,     double * _Nonnull __D,     vDSP_Length __N ); ``` |

Modified [vDSP_zconv()](https://developer.apple.com/documentation/accelerate/1450771-vdsp_zconv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zconv (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_F,     vDSP_Stride __vDSP_IF,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zconv (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __F,     vDSP_Stride __IF,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zconvD()](https://developer.apple.com/documentation/accelerate/1450522-vdsp_zconvd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zconvD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_F,     vDSP_Stride __vDSP_IF,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zconvD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __F,     vDSP_Stride __IF,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zcspec()](https://developer.apple.com/documentation/accelerate/1450283-vdsp_zcspec)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zcspec (     const DSPSplitComplex *__vDSP_A,     const DSPSplitComplex *__vDSP_B,     const DSPSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zcspec (     const DSPSplitComplex * _Nonnull __A,     const DSPSplitComplex * _Nonnull __B,     const DSPSplitComplex * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zcspecD()](https://developer.apple.com/documentation/accelerate/1450164-vdsp_zcspecd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zcspecD (     const DSPDoubleSplitComplex *__vDSP_A,     const DSPDoubleSplitComplex *__vDSP_B,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zcspecD (     const DSPDoubleSplitComplex * _Nonnull __A,     const DSPDoubleSplitComplex * _Nonnull __B,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zdotpr()](https://developer.apple.com/documentation/accelerate/1450701-vdsp_zdotpr)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zdotpr (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zdotpr (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zdotprD()](https://developer.apple.com/documentation/accelerate/1450740-vdsp_zdotprd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zdotprD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zdotprD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zidotpr()](https://developer.apple.com/documentation/accelerate/1450063-vdsp_zidotpr)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zidotpr (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zidotpr (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zidotprD()](https://developer.apple.com/documentation/accelerate/1450309-vdsp_zidotprd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zidotprD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zidotprD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zmma()](https://developer.apple.com/documentation/accelerate/1450160-vdsp_zmma)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zmma (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zmma (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zmmaD()](https://developer.apple.com/documentation/accelerate/1450365-vdsp_zmmad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zmmaD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zmmaD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zmms()](https://developer.apple.com/documentation/accelerate/1450785-vdsp_zmms)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zmms (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zmms (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zmmsD()](https://developer.apple.com/documentation/accelerate/1450311-vdsp_zmmsd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zmmsD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zmmsD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zmmul()](https://developer.apple.com/documentation/accelerate/1449712-vdsp_zmmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zmmul (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zmmul (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zmmulD()](https://developer.apple.com/documentation/accelerate/1450796-vdsp_zmmuld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zmmulD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zmmulD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zmsm()](https://developer.apple.com/documentation/accelerate/1450400-vdsp_zmsm)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zmsm (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zmsm (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zmsmD()](https://developer.apple.com/documentation/accelerate/1450218-vdsp_zmsmd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zmsmD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zmsmD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zrdesamp()](https://developer.apple.com/documentation/accelerate/1449891-vdsp_zrdesamp)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrdesamp (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_I,     const float *__vDSP_F,     const DSPSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zrdesamp (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __DF,     const float * _Nonnull __F,     const DSPSplitComplex * _Nonnull __C,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zrdesampD()](https://developer.apple.com/documentation/accelerate/1449934-vdsp_zrdesampd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrdesampD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_I,     const double *__vDSP_F,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zrdesampD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __DF,     const double * _Nonnull __F,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_zrdotpr()](https://developer.apple.com/documentation/accelerate/1450544-vdsp_zrdotpr)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrdotpr (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zrdotpr (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zrdotprD()](https://developer.apple.com/documentation/accelerate/1450394-vdsp_zrdotprd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrdotprD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zrdotprD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zrvadd()](https://developer.apple.com/documentation/accelerate/1449990-vdsp_zrvadd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrvadd (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zrvadd (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zrvaddD()](https://developer.apple.com/documentation/accelerate/1450465-vdsp_zrvaddd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrvaddD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zrvaddD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zrvdiv()](https://developer.apple.com/documentation/accelerate/1450142-vdsp_zrvdiv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrvdiv (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zrvdiv (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zrvdivD()](https://developer.apple.com/documentation/accelerate/1450666-vdsp_zrvdivd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrvdivD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zrvdivD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zrvmul()](https://developer.apple.com/documentation/accelerate/1450657-vdsp_zrvmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrvmul (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zrvmul (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zrvmulD()](https://developer.apple.com/documentation/accelerate/1449954-vdsp_zrvmuld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrvmulD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zrvmulD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zrvsub()](https://developer.apple.com/documentation/accelerate/1449845-vdsp_zrvsub)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrvsub (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zrvsub (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zrvsubD()](https://developer.apple.com/documentation/accelerate/1450034-vdsp_zrvsubd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zrvsubD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zrvsubD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_ztoc()](https://developer.apple.com/documentation/kernel/1579934-vdsp_ztoc)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_ztoc (     const DSPSplitComplex *__vDSP_Z,     vDSP_Stride __vDSP_IZ,     DSPComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_ztoc (     const DSPSplitComplex * _Nonnull __Z,     vDSP_Stride __IZ,     DSPComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_ztocD()](https://developer.apple.com/documentation/accelerate/1450165-vdsp_ztocd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_ztocD (     const DSPDoubleSplitComplex *__vDSP_Z,     vDSP_Stride __vDSP_IZ,     DSPDoubleComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_ztocD (     const DSPDoubleSplitComplex * _Nonnull __Z,     vDSP_Stride __IZ,     DSPDoubleComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_ztrans()](https://developer.apple.com/documentation/accelerate/1450787-vdsp_ztrans)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_ztrans (     const float *__vDSP_A,     const DSPSplitComplex *__vDSP_B,     const DSPSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_ztrans (     const float * _Nonnull __A,     const DSPSplitComplex * _Nonnull __B,     const DSPSplitComplex * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_ztransD()](https://developer.apple.com/documentation/accelerate/1450357-vdsp_ztransd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_ztransD (     const double *__vDSP_A,     const DSPDoubleSplitComplex *__vDSP_B,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_ztransD (     const double * _Nonnull __A,     const DSPDoubleSplitComplex * _Nonnull __B,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_zvabs()](https://developer.apple.com/documentation/kernel/1579998-vdsp_zvabs)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvabs (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvabs (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvabsD()](https://developer.apple.com/documentation/accelerate/1450251-vdsp_zvabsd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvabsD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvabsD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvadd()](https://developer.apple.com/documentation/accelerate/1450051-vdsp_zvadd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvadd (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvadd (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvaddD()](https://developer.apple.com/documentation/accelerate/1449906-vdsp_zvaddd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvaddD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvaddD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvcma()](https://developer.apple.com/documentation/accelerate/1450200-vdsp_zvcma)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvcma (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvcma (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_zvcmaD()](https://developer.apple.com/documentation/accelerate/1450572-vdsp_zvcmad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvcmaD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvcmaD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_zvcmul()](https://developer.apple.com/documentation/accelerate/1450717-vdsp_zvcmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvcmul (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvcmul (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvcmulD()](https://developer.apple.com/documentation/accelerate/1449764-vdsp_zvcmuld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvcmulD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_iC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvcmulD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __iC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvconj()](https://developer.apple.com/documentation/accelerate/1450617-vdsp_zvconj)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvconj (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvconj (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvconjD()](https://developer.apple.com/documentation/accelerate/1450479-vdsp_zvconjd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvconjD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvconjD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvdiv()](https://developer.apple.com/documentation/accelerate/1449769-vdsp_zvdiv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvdiv (     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvdiv (     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvdivD()](https://developer.apple.com/documentation/accelerate/1450594-vdsp_zvdivd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvdivD (     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvdivD (     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvfill()](https://developer.apple.com/documentation/accelerate/1450499-vdsp_zvfill)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvfill (     const DSPSplitComplex *__vDSP_A,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvfill (     const DSPSplitComplex * _Nonnull __A,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvfillD()](https://developer.apple.com/documentation/accelerate/1450495-vdsp_zvfilld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvfillD (     const DSPDoubleSplitComplex *__vDSP_A,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvfillD (     const DSPDoubleSplitComplex * _Nonnull __A,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvma()](https://developer.apple.com/documentation/accelerate/1449940-vdsp_zvma)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvma (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvma (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmaD()](https://developer.apple.com/documentation/accelerate/1449721-vdsp_zvmad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmaD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvmaD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmags()](https://developer.apple.com/documentation/accelerate/1450557-vdsp_zvmags)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmags (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvmags (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmagsD()](https://developer.apple.com/documentation/accelerate/1450026-vdsp_zvmagsd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmagsD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvmagsD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmgsa()](https://developer.apple.com/documentation/accelerate/1450647-vdsp_zvmgsa)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmgsa (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvmgsa (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmgsaD()](https://developer.apple.com/documentation/accelerate/1450338-vdsp_zvmgsad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmgsaD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const double *__vDSP_B,     vDSP_Stride __vDSP_IB,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvmgsaD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const double * _Nonnull __B,     vDSP_Stride __IB,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmmaa()](https://developer.apple.com/documentation/accelerate/1450110-vdsp_zvmmaa)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmmaa (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     const DSPSplitComplex *__vDSP_E,     vDSP_Stride __vDSP_IE,     const DSPSplitComplex *__vDSP_F,     vDSP_Stride __vDSP_IF,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvmmaa (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     const DSPSplitComplex * _Nonnull __E,     vDSP_Stride __IE,     const DSPSplitComplex * _Nonnull __F,     vDSP_Stride __IF,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmmaaD()](https://developer.apple.com/documentation/accelerate/1449810-vdsp_zvmmaad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmmaaD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     const DSPDoubleSplitComplex *__vDSP_E,     vDSP_Stride __vDSP_IE,     const DSPDoubleSplitComplex *__vDSP_F,     vDSP_Stride __vDSP_IF,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvmmaaD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     const DSPDoubleSplitComplex * _Nonnull __E,     vDSP_Stride __IE,     const DSPDoubleSplitComplex * _Nonnull __F,     vDSP_Stride __IF,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmov()](https://developer.apple.com/documentation/kernel/1579979-vdsp_zvmov)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmov (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvmov (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmovD()](https://developer.apple.com/documentation/accelerate/1450484-vdsp_zvmovd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmovD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvmovD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmul()](https://developer.apple.com/documentation/kernel/1579954-vdsp_zvmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmul (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     int __vDSP_Conjugate ); ``` |
| To | ``` void vDSP_zvmul (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     int __Conjugate ); ``` |

Modified [vDSP_zvmulD()](https://developer.apple.com/documentation/accelerate/1450390-vdsp_zvmuld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmulD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     int __vDSP_Conjugate ); ``` |
| To | ``` void vDSP_zvmulD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     int __Conjugate ); ``` |

Modified [vDSP_zvneg()](https://developer.apple.com/documentation/accelerate/1450326-vdsp_zvneg)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvneg (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvneg (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvnegD()](https://developer.apple.com/documentation/accelerate/1450351-vdsp_zvnegd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvnegD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvnegD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvphas()](https://developer.apple.com/documentation/accelerate/1449904-vdsp_zvphas)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvphas (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvphas (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvphasD()](https://developer.apple.com/documentation/accelerate/1450132-vdsp_zvphasd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvphasD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     double *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvphasD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     double * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvsma()](https://developer.apple.com/documentation/accelerate/1449902-vdsp_zvsma)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvsma (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvsma (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_zvsmaD()](https://developer.apple.com/documentation/accelerate/1450570-vdsp_zvsmad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvsmaD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPDoubleSplitComplex *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvsmaD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPDoubleSplitComplex * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_zvsub()](https://developer.apple.com/documentation/accelerate/1450818-vdsp_zvsub)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvsub (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvsub (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvsubD()](https://developer.apple.com/documentation/accelerate/1450642-vdsp_zvsubd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvsubD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvsubD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvzsml()](https://developer.apple.com/documentation/accelerate/1450410-vdsp_zvzsml)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvzsml (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvzsml (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvzsmlD()](https://developer.apple.com/documentation/accelerate/1449727-vdsp_zvzsmld)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvzsmlD (     const DSPDoubleSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPDoubleSplitComplex *__vDSP_B,     const DSPDoubleSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvzsmlD (     const DSPDoubleSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPDoubleSplitComplex * _Nonnull __B,     const DSPDoubleSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

#### vDSP_translate.h

Removed #def vDSP_convRemoved #def vDSP_convDRemoved #def vDSP_create_fftsetupRemoved #def vDSP_create_fftsetupDRemoved #def vDSP_ctozRemoved #def vDSP_ctozDRemoved #def vDSP_destroy_fftsetupRemoved #def vDSP_destroy_fftsetupDRemoved #def vDSP_dotprRemoved #def vDSP_dotprDRemoved #def vDSP_f3x3Removed #def vDSP_f3x3DRemoved #def vDSP_f5x5Removed #def vDSP_f5x5DRemoved #def vDSP_fft2d_zipRemoved #def vDSP_fft2d_zipDRemoved #def vDSP_fft2d_ziptRemoved #def vDSP_fft2d_ziptDRemoved #def vDSP_fft2d_zopRemoved #def vDSP_fft2d_zopDRemoved #def vDSP_fft2d_zoptRemoved #def vDSP_fft2d_zoptDRemoved #def vDSP_fft2d_zripRemoved #def vDSP_fft2d_zripDRemoved #def vDSP_fft2d_zriptRemoved #def vDSP_fft2d_zriptDRemoved #def vDSP_fft2d_zropRemoved #def vDSP_fft2d_zropDRemoved #def vDSP_fft2d_zroptRemoved #def vDSP_fft2d_zroptDRemoved #def vDSP_fft3_zopRemoved #def vDSP_fft3_zopDRemoved #def vDSP_fft5_zopRemoved #def vDSP_fft5_zopDRemoved #def vDSP_fft_cipRemoved #def vDSP_fft_ciptRemoved #def vDSP_fft_copRemoved #def vDSP_fft_coptRemoved #def vDSP_fft_zipRemoved #def vDSP_fft_zipDRemoved #def vDSP_fft_ziptRemoved #def vDSP_fft_ziptDRemoved #def vDSP_fft_zopRemoved #def vDSP_fft_zopDRemoved #def vDSP_fft_zoptRemoved #def vDSP_fft_zoptDRemoved #def vDSP_fft_zripRemoved #def vDSP_fft_zripDRemoved #def vDSP_fft_zriptRemoved #def vDSP_fft_zriptDRemoved #def vDSP_fft_zropRemoved #def vDSP_fft_zropDRemoved #def vDSP_fft_zroptRemoved #def vDSP_fft_zroptDRemoved #def vDSP_fftm_zipRemoved #def vDSP_fftm_zipDRemoved #def vDSP_fftm_ziptRemoved #def vDSP_fftm_ziptDRemoved #def vDSP_fftm_zopRemoved #def vDSP_fftm_zopDRemoved #def vDSP_fftm_zoptRemoved #def vDSP_fftm_zoptDRemoved #def vDSP_fftm_zripRemoved #def vDSP_fftm_zripDRemoved #def vDSP_fftm_zriptRemoved #def vDSP_fftm_zriptDRemoved #def vDSP_fftm_zropRemoved #def vDSP_fftm_zropDRemoved #def vDSP_fftm_zroptRemoved #def vDSP_fftm_zroptDRemoved #def vDSP_imgfirRemoved #def vDSP_imgfirDRemoved #def vDSP_mmulRemoved #def vDSP_mmulDRemoved #def vDSP_mtransRemoved #def vDSP_mtransDRemoved #def vDSP_vaddRemoved #def vDSP_vaddDRemoved #def vDSP_vamRemoved #def vDSP_vamDRemoved #def vDSP_vmulRemoved #def vDSP_vmulDRemoved #def vDSP_vsmulRemoved #def vDSP_vsmulDRemoved #def vDSP_vsqRemoved #def vDSP_vsqDRemoved #def vDSP_vssqRemoved #def vDSP_vssqDRemoved #def vDSP_vsubRemoved #def vDSP_vsubDRemoved #def vDSP_zconvRemoved #def vDSP_zconvDRemoved #def vDSP_zdotprRemoved #def vDSP_zdotprDRemoved #def vDSP_zidotprRemoved #def vDSP_zidotprDRemoved #def vDSP_zmmaRemoved #def vDSP_zmmaDRemoved #def vDSP_zmmsRemoved #def vDSP_zmmsDRemoved #def vDSP_zmmulRemoved #def vDSP_zmmulDRemoved #def vDSP_zmsmRemoved #def vDSP_zmsmDRemoved #def vDSP_zrdotprRemoved #def vDSP_zrdotprDRemoved #def vDSP_zrvaddRemoved #def vDSP_zrvaddDRemoved #def vDSP_zrvmulRemoved #def vDSP_zrvmulDRemoved #def vDSP_zrvsubRemoved #def vDSP_zrvsubDRemoved #def vDSP_ztocRemoved #def vDSP_ztocDRemoved #def vDSP_zvaddRemoved #def vDSP_zvaddDRemoved #def vDSP_zvcmaRemoved #def vDSP_zvcmaDRemoved #def vDSP_zvmulRemoved #def vDSP_zvmulDRemoved #def vDSP_zvsubRemoved #def vDSP_zvsubDAdded #def vDSP_DeprecateTranslations

#### vecLibTypes.h

Removed #def ARM_NEON_GCC_COMPATIBILITYRemoved [vBool32](https://developer.apple.com/documentation/kernel/vbool32)Removed [vDouble](https://developer.apple.com/documentation/kernel/vdouble)Removed [vFloat](https://developer.apple.com/documentation/kernel/vfloat)Removed [vSInt16](https://developer.apple.com/documentation/kernel/vsint16)Removed [vSInt32](https://developer.apple.com/documentation/kernel/vsint32)Removed [vSInt8](https://developer.apple.com/documentation/kernel/vsint8)Removed [vUInt16](https://developer.apple.com/documentation/kernel/vuint16)Removed [vUInt32](https://developer.apple.com/documentation/kernel/vuint32)Removed [vUInt8](https://developer.apple.com/documentation/kernel/vuint8)

#### vImage_CVUtilities.h

Added [vImageCreateMonochromeColorSpaceWithWhitePointAndTransferFunction()](https://developer.apple.com/documentation/accelerate/1498186-vimagecreatemonochromecolorspace)Added [vImageWhitePoint](https://developer.apple.com/documentation/accelerate/vimagewhitepoint)

#### vImage_Types.h

Added #def CF_BRIDGED_TYPEAdded [kvImageHDRContent](https://developer.apple.com/documentation/accelerate/kvimagehdrcontent)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
