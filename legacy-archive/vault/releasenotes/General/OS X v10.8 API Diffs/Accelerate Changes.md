---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/Accelerate.html
archived_at: '2026-07-18T02:53:55.553264Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# Accelerate Changes

## Accelerate

Alpha.hAdded #def vImageClipToAlpha_BGRA8888Added #def vImageClipToAlpha_BGRAFFFFAdded [vImageClipToAlpha_RGBA8888()](https://developer.apple.com/documentation/accelerate/1410676-vimagecliptoalpha_rgba8888)Added [vImageClipToAlpha_RGBAFFFF()](https://developer.apple.com/documentation/accelerate/1410680-vimagecliptoalpha_rgbaffff)Added [vImagePremultiplyData_ARGB16U()](https://developer.apple.com/documentation/accelerate/1410642-vimagepremultiplydata_argb16u)Added #def vImagePremultiplyData_BGRA16UAdded [vImagePremultiplyData_RGBA16U()](https://developer.apple.com/documentation/accelerate/1410647-vimagepremultiplydata_rgba16u)Added [vImageUnpremultiplyData_ARGB16U()](https://developer.apple.com/documentation/accelerate/1410638-vimageunpremultiplydata_argb16u)Added #def vImageUnpremultiplyData_BGRA16UAdded [vImageUnpremultiplyData_RGBA16U()](https://developer.apple.com/documentation/accelerate/1410690-vimageunpremultiplydata_rgba16u)Conversion.hAdded [#def vImageConvert_BGR888toBGRA8888](https://developer.apple.com/documentation/accelerate/vimageconvert_bgr888tobgra8888)Added [#def vImageConvert_BGR888toRGBA8888](https://developer.apple.com/documentation/accelerate/vimageconvert_bgr888torgba8888)Added [#def vImageConvert_BGRA8888toBGR888](https://developer.apple.com/documentation/accelerate/vimageconvert_bgra8888tobgr888)Added [vImageConvert_BGRA8888toRGB888()](https://developer.apple.com/documentation/accelerate/1533090-vimageconvert_bgra8888torgb888)Added [vImageConvert_RGB888toBGRA8888()](https://developer.apple.com/documentation/accelerate/1533212-vimageconvert_rgb888tobgra8888)Added [vImageConvert_RGB888toRGBA8888()](https://developer.apple.com/documentation/accelerate/1533228-vimageconvert_rgb888torgba8888)Added [#def vImageConvert_RGBA8888toBGR888](https://developer.apple.com/documentation/accelerate/vimageconvert_rgba8888tobgr888)Added [vImageConvert_RGBA8888toRGB888()](https://developer.apple.com/documentation/accelerate/1533062-vimageconvert_rgba8888torgb888)Added [#def vImageFlatten_BGRA8888ToBGR888](https://developer.apple.com/documentation/accelerate/vimageflatten_bgra8888tobgr888)Added [vImageFlatten_BGRA8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533119-vimageflatten_bgra8888torgb888)Added [vImageFlatten_BGRAFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533156-vimageflatten_bgrafffftorgbfff)Added [#def vImageFlatten_RGBA8888ToBGR888](https://developer.apple.com/documentation/accelerate/vimageflatten_rgba8888tobgr888)Added [vImageFlatten_RGBA8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533147-vimageflatten_rgba8888torgb888)Added [vImageFlatten_RGBAFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533280-vimageflatten_rgbafffftorgbfff)Modified [vImageConvert_ARGB8888toRGB888()](https://developer.apple.com/documentation/accelerate/1533276-vimageconvert_argb8888torgb888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageConvert_ARGB8888toRGB888 ( const vImage_Buffer \*argbSrc, const vImage_Buffer \*rgbDest, vImage_Flags flags); |
| To | vImage_Error vImageConvert_ARGB8888toRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, vImage_Flags); |

Modified [vImageConvert_RGB888toARGB8888()](https://developer.apple.com/documentation/accelerate/1533137-vimageconvert_rgb888toargb8888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageConvert_RGB888toARGB8888 ( const vImage_Buffer \*rgbSrc, const vImage_Buffer \*aSrc, Pixel_8 alpha, const vImage_Buffer \*argbDest, bool premultiply, vImage_Flags flags); |
| To | vImage_Error vImageConvert_RGB888toARGB8888 ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_8, const vImage_Buffer \*, bool, vImage_Flags); |

Modified [vImageFlatten_ARGBFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533210-vimageflatten_argbfffftorgbfff)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_ARGBFFFFToRGBFFF ( const vImage_Buffer \*argbFFFFSrc, const vImage_Buffer \*rgbFFFdest, Pixel_FFFF backgroundColor, bool isImagePremultiplied, vImage_Flags flags); |
| To | vImage_Error vImageFlatten_ARGBFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_FFFF, bool, vImage_Flags); |

Modified [vImageFlatten_ARGB8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533019-vimageflatten_argb8888torgb888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_ARGB8888ToRGB888 ( const vImage_Buffer \*argb8888Src, const vImage_Buffer \*rgb888dest, Pixel_8888 backgroundColor, bool isImagePremultiplied, vImage_Flags flags); |
| To | vImage_Error vImageFlatten_ARGB8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_8888, bool, vImage_Flags); |

vBLAS.hModified [SAXPY()](https://developer.apple.com/documentation/accelerate/1546716-vs512halfmultiply)

|  | Declaration |
| --- | --- |
| From | void SAXPY ( const int \*N, const float \*alpha, const float \*X, const int \*incX, float \*Y, const int \*incY); |
| To | void SAXPY ( const int \*, const float \*, const float \*, const int \*, float \*, const int \*); |

Modified [SDOT()](https://developer.apple.com/documentation/accelerate/1545106-vs1024halfmultiply)

|  | Declaration |
| --- | --- |
| From | float SDOT ( const int \*N, const float \*X, const int \*incX, const float \*Y, const int \*incY); |
| To | float SDOT ( const int \*, const float \*, const int \*, const float \*, const int \*); |

Modified [SGEMM()](https://developer.apple.com/documentation/accelerate/1545260-vu128fullmultiply)

|  | Declaration |
| --- | --- |
| From | void SGEMM ( const char \*transA, const char \*transB, const int \*M, const int \*N, const int \*K, const float \*alpha, const float \*A, const int \*lda, const float \*B, const int \*ldb, const float \*beta, float \*C, const int \*ldc); |
| To | void SGEMM ( const char \*, const char \*, const int \*, const int \*, const int \*, const float \*, const float \*, const int \*, const float \*, const int \*, const float \*, float \*, const int \*); |

Modified [SASUM()](https://developer.apple.com/documentation/accelerate/1544423-vu512halfmultiply)

|  | Declaration |
| --- | --- |
| From | float SASUM ( const int \*N, const float \*X, const int \*incX); |
| To | float SASUM ( const int \*, const float \*, const int \*); |

Modified [SCOPY()](https://developer.apple.com/documentation/accelerate/1546648-vu1024halfmultiply)

|  | Declaration |
| --- | --- |
| From | void SCOPY ( const int \*N, const float \*X, const int \*incX, float \*Y, const int \*incY); |
| To | void SCOPY ( const int \*, const float \*, const int \*, float \*, const int \*); |

Modified [SNRM2()](https://developer.apple.com/documentation/accelerate/1544634-vu256fullmultiply)

|  | Declaration |
| --- | --- |
| From | float SNRM2 ( const int \*N, const float \*X, const int \*incX); |
| To | float SNRM2 ( const int \*, const float \*, const int \*); |

Modified [SGEMV()](https://developer.apple.com/documentation/accelerate/1544607-vs128fullmultiply)

|  | Declaration |
| --- | --- |
| From | void SGEMV ( const char \*transA, const int \*M, const int \*N, const float \*alpha, const float \*A, const int \*lda, const float \*X, const int \*incX, const float \*beta, float \*Y, const int \*incY); |
| To | void SGEMV ( const char \*, const int \*, const int \*, const float \*, const float \*, const int \*, const float \*, const int \*, const float \*, float \*, const int \*); |

Modified [SROT()](https://developer.apple.com/documentation/accelerate/1544484-vs256fullmultiply)

|  | Declaration |
| --- | --- |
| From | void SROT ( const int \*N, float \*X, const int \*incX, float \*Y, const int \*incY, const float \*c, const float \*s); |
| To | void SROT ( const int \*, float \*, const int \*, float \*, const int \*, const float \*, const float \*); |

Modified [SSWAP()](https://developer.apple.com/documentation/accelerate/1546864-vs512fullmultiply)

|  | Declaration |
| --- | --- |
| From | void SSWAP ( const int \*N, float \*X, const int \*incX, float \*Y, const int \*incY); |
| To | void SSWAP ( const int \*, const float \*, const int \*, float \*, const int \*); |

Modified [SSCAL()](https://developer.apple.com/documentation/accelerate/1546696-vu512fullmultiply)

|  | Declaration |
| --- | --- |
| From | void SSCAL ( const int \*N, const float \*alpha, float \*X, const int \*incX); |
| To | void SSCAL ( const int \*, const float \*, float \*, const int \*); |

Modified [ISAMAX()](https://developer.apple.com/documentation/accelerate/1545319-vs256halfmultiply)

|  | Declaration |
| --- | --- |
| From | int ISAMAX ( const int \*N, const float \*X, const int \*incX); |
| To | int ISAMAX ( const int \*, const float \*, const int \*); |

vDSP.hAdded [vDSP_distancesq()](https://developer.apple.com/documentation/accelerate/1450619-vdsp_distancesq)Added [vDSP_normalize()](https://developer.apple.com/documentation/accelerate/1450106-vdsp_normalize)Added [vDSP_normalizeD()](https://developer.apple.com/documentation/accelerate/1450154-vdsp_normalized)Added [vDSP_sve_svesq()](https://developer.apple.com/documentation/kernel/1579989-vdsp_sve_svesq)Added [vDSP_sve_svesqD()](https://developer.apple.com/documentation/accelerate/1450682-vdsp_sve_svesqd)Modified [vDSP_vmax()](https://developer.apple.com/documentation/kernel/1579953-vdsp_vmax)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmax ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmax ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |

Modified [vDSP_vmin()](https://developer.apple.com/documentation/accelerate/1450216-vdsp_vmin)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmin ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmin ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |

vImage_Types.hAdded Pixel_16Uvfp.hModified [vfabf()](https://developer.apple.com/documentation/accelerate/1556258-vfabf)

|  | Declaration |
| --- | --- |
| From | vFloat vfabf ( vFloat v); |
| To | vFloat vfabf ( vFloat); |

Modified [vcoshf()](https://developer.apple.com/documentation/accelerate/1556256-vcoshf)

|  | Declaration |
| --- | --- |
| From | vFloat vcoshf ( vFloat X); |
| To | vFloat vcoshf ( vFloat); |

Modified [vlog10f()](https://developer.apple.com/documentation/accelerate/1556285-vlog10f)

|  | Declaration |
| --- | --- |
| From | vFloat vlog10f ( vFloat X); |
| To | vFloat vlog10f ( vFloat); |

Modified [vsqrtf()](https://developer.apple.com/documentation/accelerate/1556282-vsqrtf)

|  | Declaration |
| --- | --- |
| From | vFloat vsqrtf ( vFloat X); |
| To | vFloat vsqrtf ( vFloat); |

Modified [vatanhf()](https://developer.apple.com/documentation/accelerate/1556251-vatanhf)

|  | Declaration |
| --- | --- |
| From | vFloat vatanhf ( vFloat X); |
| To | vFloat vatanhf ( vFloat); |

Modified [vipowf()](https://developer.apple.com/documentation/accelerate/1556262-vipowf)

|  | Declaration |
| --- | --- |
| From | vFloat vipowf ( vFloat X, vSInt32 Y); |
| To | vFloat vipowf ( vFloat, vSInt32); |

Modified [vacoshf()](https://developer.apple.com/documentation/accelerate/1556279-vacoshf)

|  | Declaration |
| --- | --- |
| From | vFloat vacoshf ( vFloat X); |
| To | vFloat vacoshf ( vFloat); |

Modified [vlogbf()](https://developer.apple.com/documentation/accelerate/1556274-vlogbf)

|  | Declaration |
| --- | --- |
| From | vFloat vlogbf ( vFloat X); |
| To | vFloat vlogbf ( vFloat); |

Modified [vdivf()](https://developer.apple.com/documentation/accelerate/1556290-vdivf)

|  | Declaration |
| --- | --- |
| From | vFloat vdivf ( vFloat A, vFloat B); |
| To | vFloat vdivf ( vFloat, vFloat); |

Modified [vasinf()](https://developer.apple.com/documentation/accelerate/1556255-vasinf)

|  | Declaration |
| --- | --- |
| From | vFloat vasinf ( vFloat arg); |
| To | vFloat vasinf ( vFloat); |

Modified vintf()

|  | Declaration |
| --- | --- |
| From | vFloat vintf ( vFloat A); |
| To | vFloat vintf ( vFloat); |

Modified [vsignbitf()](https://developer.apple.com/documentation/accelerate/1556294-vsignbitf)

|  | Declaration |
| --- | --- |
| From | vUInt32 vsignbitf ( vFloat arg); |
| To | vUInt32 vsignbitf ( vFloat); |

Modified [vtanhf()](https://developer.apple.com/documentation/accelerate/1556267-vtanhf)

|  | Declaration |
| --- | --- |
| From | vFloat vtanhf ( vFloat X); |
| To | vFloat vtanhf ( vFloat); |

Modified [vpowf()](https://developer.apple.com/documentation/accelerate/1556269-vpowf)

|  | Declaration |
| --- | --- |
| From | vFloat vpowf ( vFloat X, vFloat Y); |
| To | vFloat vpowf ( vFloat, vFloat); |

Modified [vscalbf()](https://developer.apple.com/documentation/accelerate/1556284-vscalbf)

|  | Declaration |
| --- | --- |
| From | vFloat vscalbf ( vFloat X, vSInt32 n); |
| To | vFloat vscalbf ( vFloat, vSInt32); |

Modified [vsincosf()](https://developer.apple.com/documentation/accelerate/1556288-vsincosf)

|  | Declaration |
| --- | --- |
| From | vFloat vsincosf ( vFloat arg, vFloat \*sine_result); |
| To | vFloat vsincosf ( vFloat, vFloat \*); |

Modified [vexpm1f()](https://developer.apple.com/documentation/accelerate/1556259-vexpm1f)

|  | Declaration |
| --- | --- |
| From | vFloat vexpm1f ( vFloat X); |
| To | vFloat vexpm1f ( vFloat); |

Modified [vfloorf()](https://developer.apple.com/documentation/accelerate/1556275-vfloorf)

|  | Declaration |
| --- | --- |
| From | vFloat vfloorf ( vFloat A); |
| To | vFloat vfloorf ( vFloat); |

Modified [vlog1pf()](https://developer.apple.com/documentation/accelerate/1556277-vlog1pf)

|  | Declaration |
| --- | --- |
| From | vFloat vlog1pf ( vFloat X); |
| To | vFloat vlog1pf ( vFloat); |

Modified [vtablelookup()](https://developer.apple.com/documentation/accelerate/1556270-vtablelookup)

|  | Declaration |
| --- | --- |
| From | vUInt32 vtablelookup ( vSInt32 Index_Vect, uint32_t \*Table); |
| To | vUInt32 vtablelookup ( vSInt32, uint32_t \*); |

Modified [vasinhf()](https://developer.apple.com/documentation/accelerate/1556281-vasinhf)

|  | Declaration |
| --- | --- |
| From | vFloat vasinhf ( vFloat X); |
| To | vFloat vasinhf ( vFloat); |

Modified [vatanf()](https://developer.apple.com/documentation/accelerate/1556289-vatanf)

|  | Declaration |
| --- | --- |
| From | vFloat vatanf ( vFloat arg); |
| To | vFloat vatanf ( vFloat); |

Modified [vtanf()](https://developer.apple.com/documentation/accelerate/1556287-vtanf)

|  | Declaration |
| --- | --- |
| From | vFloat vtanf ( vFloat arg); |
| To | vFloat vtanf ( vFloat); |

Modified [vnextafterf()](https://developer.apple.com/documentation/accelerate/1556280-vnextafterf)

|  | Declaration |
| --- | --- |
| From | vFloat vnextafterf ( vFloat x, vFloat y); |
| To | vFloat vnextafterf ( vFloat, vFloat); |

Modified [vexpf()](https://developer.apple.com/documentation/accelerate/1556271-vexpf)

|  | Declaration |
| --- | --- |
| From | vFloat vexpf ( vFloat X); |
| To | vFloat vexpf ( vFloat); |

Modified [vclassifyf()](https://developer.apple.com/documentation/accelerate/1556265-vclassifyf)

|  | Declaration |
| --- | --- |
| From | vUInt32 vclassifyf ( vFloat arg); |
| To | vUInt32 vclassifyf ( vFloat); |

Modified [vacosf()](https://developer.apple.com/documentation/accelerate/1556283-vacosf)

|  | Declaration |
| --- | --- |
| From | vFloat vacosf ( vFloat arg); |
| To | vFloat vacosf ( vFloat); |

Modified [vnintf()](https://developer.apple.com/documentation/accelerate/1556253-vnintf)

|  | Declaration |
| --- | --- |
| From | vFloat vnintf ( vFloat A); |
| To | vFloat vnintf ( vFloat); |

Modified [vlogf()](https://developer.apple.com/documentation/accelerate/1556263-vlogf)

|  | Declaration |
| --- | --- |
| From | vFloat vlogf ( vFloat X); |
| To | vFloat vlogf ( vFloat); |

Modified [vfmodf()](https://developer.apple.com/documentation/accelerate/1556261-vfmodf)

|  | Declaration |
| --- | --- |
| From | vFloat vfmodf ( vFloat X, vFloat Y); |
| To | vFloat vfmodf ( vFloat, vFloat); |

Modified [vsinf()](https://developer.apple.com/documentation/accelerate/1556250-vsinf)

|  | Declaration |
| --- | --- |
| From | vFloat vsinf ( vFloat arg); |
| To | vFloat vsinf ( vFloat); |

Modified [vceilf()](https://developer.apple.com/documentation/accelerate/1556252-vceilf)

|  | Declaration |
| --- | --- |
| From | vFloat vceilf ( vFloat A); |
| To | vFloat vceilf ( vFloat); |

Modified [vatan2f()](https://developer.apple.com/documentation/accelerate/1556295-vatan2f)

|  | Declaration |
| --- | --- |
| From | vFloat vatan2f ( vFloat arg1, vFloat arg2); |
| To | vFloat vatan2f ( vFloat, vFloat); |

Modified [vsinhf()](https://developer.apple.com/documentation/accelerate/1556254-vsinhf)

|  | Declaration |
| --- | --- |
| From | vFloat vsinhf ( vFloat X); |
| To | vFloat vsinhf ( vFloat); |

Modified [vrecf()](https://developer.apple.com/documentation/accelerate/1556257-vrecf)

|  | Declaration |
| --- | --- |
| From | vFloat vrecf ( vFloat A); |
| To | vFloat vrecf ( vFloat); |

Modified [vrsqrtf()](https://developer.apple.com/documentation/accelerate/1556268-vrsqrtf)

|  | Declaration |
| --- | --- |
| From | vFloat vrsqrtf ( vFloat X); |
| To | vFloat vrsqrtf ( vFloat); |

Modified [vcosf()](https://developer.apple.com/documentation/accelerate/1556273-vcosf)

|  | Declaration |
| --- | --- |
| From | vFloat vcosf ( vFloat arg); |
| To | vFloat vcosf ( vFloat); |

Modified [vremainderf()](https://developer.apple.com/documentation/accelerate/1556293-vremainderf)

|  | Declaration |
| --- | --- |
| From | vFloat vremainderf ( vFloat X, vFloat Y); |
| To | vFloat vremainderf ( vFloat, vFloat); |

Modified [vcopysignf()](https://developer.apple.com/documentation/accelerate/1556276-vcopysignf)

|  | Declaration |
| --- | --- |
| From | vFloat vcopysignf ( vFloat arg2, vFloat arg1); |
| To | vFloat vcopysignf ( vFloat, vFloat); |

Modified [vremquof()](https://developer.apple.com/documentation/accelerate/1556264-vremquof)

|  | Declaration |
| --- | --- |
| From | vFloat vremquof ( vFloat X, vFloat Y, vUInt32 \*QUO); |
| To | vFloat vremquof ( vFloat, vFloat, vUInt32 \*); |

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
