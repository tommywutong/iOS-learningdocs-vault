---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/Accelerate.html
archived_at: '2026-07-18T02:50:33.397528Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Accelerate Changes for Objective-C

### Accelerate

#### BNNS/bnns.h (Added)

Added [BNNSActivation](https://developer.apple.com/documentation/accelerate/bnnsactivation)Added [BNNSActivationFunction](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction)Added [BNNSActivationFunctionAbs](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/bnnsactivationfunctionabs)Added [BNNSActivationFunctionIdentity](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/bnnsactivationfunctionidentity)Added [BNNSActivationFunctionLeakyRectifiedLinear](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/bnnsactivationfunctionleakyrectifiedlinear)Added [BNNSActivationFunctionRectifiedLinear](https://developer.apple.com/documentation/accelerate/bnnsactivationfunctionrectifiedlinear)Added [BNNSActivationFunctionScaledTanh](https://developer.apple.com/documentation/accelerate/bnnsactivationfunctionscaledtanh)Added [BNNSActivationFunctionSigmoid](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/bnnsactivationfunctionsigmoid)Added [BNNSActivationFunctionTanh](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/bnnsactivationfunctiontanh)Added [BNNSAlloc](https://developer.apple.com/documentation/accelerate/bnnsalloc)Added [BNNSConvolutionLayerParameters](https://developer.apple.com/documentation/accelerate/bnnsconvolutionlayerparameters)Added [BNNSDataType](https://developer.apple.com/documentation/accelerate/bnnsdatatype)Added [BNNSDataTypeFloat16](https://developer.apple.com/documentation/accelerate/bnnsdatatypefloat16)Added [BNNSDataTypeFloat32](https://developer.apple.com/documentation/accelerate/bnnsdatatypefloat32)Added [BNNSDataTypeFloatBit](https://developer.apple.com/documentation/accelerate/bnnsdatatype/bnnsdatatypefloatbit)Added [BNNSDataTypeIndexed8](https://developer.apple.com/documentation/accelerate/bnnsdatatypeindexed8)Added [BNNSDataTypeIndexedBit](https://developer.apple.com/documentation/accelerate/bnnsdatatype/bnnsdatatypeindexedbit)Added [BNNSDataTypeInt16](https://developer.apple.com/documentation/accelerate/bnnsdatatype/bnnsdatatypeint16)Added [BNNSDataTypeInt32](https://developer.apple.com/documentation/accelerate/bnnsdatatype/bnnsdatatypeint32)Added [BNNSDataTypeInt8](https://developer.apple.com/documentation/accelerate/bnnsdatatype/bnnsdatatypeint8)Added [BNNSDataTypeIntBit](https://developer.apple.com/documentation/accelerate/bnnsdatatype/bnnsdatatypeintbit)Added BNNSFilterAdded [BNNSFilterApply()](https://developer.apple.com/documentation/accelerate/1642376-bnnsfilterapply)Added [BNNSFilterApplyBatch()](https://developer.apple.com/documentation/accelerate/1642298-bnnsfilterapplybatch)Added [BNNSFilterCreateConvolutionLayer()](https://developer.apple.com/documentation/accelerate/1642537-bnnsfiltercreateconvolutionlayer)Added [BNNSFilterCreateFullyConnectedLayer()](https://developer.apple.com/documentation/accelerate/1642286-bnnsfiltercreatefullyconnectedla)Added [BNNSFilterCreatePoolingLayer()](https://developer.apple.com/documentation/accelerate/1642526-bnnsfiltercreatepoolinglayer)Added [BNNSFilterDestroy()](https://developer.apple.com/documentation/accelerate/1642291-bnnsfilterdestroy)Added [BNNSFilterParameters](https://developer.apple.com/documentation/accelerate/bnnsfilterparameters)Added BNNSFlagsAdded BNNSFlagsUseClientPtrAdded [BNNSFree](https://developer.apple.com/documentation/accelerate/bnnsfree)Added [BNNSFullyConnectedLayerParameters](https://developer.apple.com/documentation/accelerate/bnnsfullyconnectedlayerparameters)Added BNNSImageStackDescriptorAdded [BNNSLayerData](https://developer.apple.com/documentation/accelerate/bnnslayerdata)Added [BNNSPoolingFunction](https://developer.apple.com/documentation/accelerate/bnnspoolingfunction)Added [BNNSPoolingFunctionAverage](https://developer.apple.com/documentation/accelerate/bnnspoolingfunction/bnnspoolingfunctionaverage)Added [BNNSPoolingFunctionMax](https://developer.apple.com/documentation/accelerate/bnnspoolingfunction/bnnspoolingfunctionmax)Added [BNNSPoolingLayerParameters](https://developer.apple.com/documentation/accelerate/bnnspoolinglayerparameters)Added BNNSVectorDescriptor

#### Conversion.h

Added [vImageBufferFill_CbCr16U()](https://developer.apple.com/documentation/accelerate/1642323-vimagebufferfill_cbcr16u)Added [vImageBufferFill_CbCr8()](https://developer.apple.com/documentation/accelerate/1642313-vimagebufferfill_cbcr8)Added [vImageConvert_12UTo16U()](https://developer.apple.com/documentation/accelerate/1642424-vimageconvert_12uto16u)Added [vImageConvert_16Fto16Q12()](https://developer.apple.com/documentation/accelerate/1642491-vimageconvert_16fto16q12)Added [vImageConvert_16Q12to16F()](https://developer.apple.com/documentation/accelerate/1642512-vimageconvert_16q12to16f)Added [vImageConvert_16UTo12U()](https://developer.apple.com/documentation/accelerate/1642561-vimageconvert_16uto12u)Added [vImageConvert_ARGB16Q12ToARGB2101010()](https://developer.apple.com/documentation/accelerate/1642307-vimageconvert_argb16q12toargb210)Added [vImageConvert_ARGB16Q12ToXRGB2101010()](https://developer.apple.com/documentation/accelerate/1642338-vimageconvert_argb16q12toxrgb210)Added [vImageConvert_ARGB16UToARGB2101010()](https://developer.apple.com/documentation/accelerate/1642517-vimageconvert_argb16utoargb21010)Added [vImageConvert_ARGB16UtoARGB8888_dithered()](https://developer.apple.com/documentation/accelerate/1642400-vimageconvert_argb16utoargb8888_)Added [vImageConvert_ARGB16UToXRGB2101010()](https://developer.apple.com/documentation/accelerate/1642365-vimageconvert_argb16utoxrgb21010)Added [vImageConvert_ARGB2101010ToARGB16F()](https://developer.apple.com/documentation/accelerate/1642514-vimageconvert_argb2101010toargb1)Added [vImageConvert_ARGB2101010ToARGB16Q12()](https://developer.apple.com/documentation/accelerate/1642301-vimageconvert_argb2101010toargb1)Added [vImageConvert_ARGB2101010ToARGB16U()](https://developer.apple.com/documentation/accelerate/1642370-vimageconvert_argb2101010toargb1)Added [vImageConvert_ARGB2101010ToARGB8888()](https://developer.apple.com/documentation/accelerate/1642359-vimageconvert_argb2101010toargb8)Added [vImageConvert_ARGB2101010ToARGBFFFF()](https://developer.apple.com/documentation/accelerate/1642440-vimageconvert_argb2101010toargbf)Added [vImageConvert_ARGB8888toARGB1555_dithered()](https://developer.apple.com/documentation/accelerate/1642460-vimageconvert_argb8888toargb1555)Added [vImageConvert_ARGB8888ToARGB2101010()](https://developer.apple.com/documentation/accelerate/1642321-vimageconvert_argb8888toargb2101)Added [vImageConvert_ARGB8888toRGB565_dithered()](https://developer.apple.com/documentation/accelerate/1642516-vimageconvert_argb8888torgb565_d)Added [vImageConvert_ARGB8888ToXRGB2101010()](https://developer.apple.com/documentation/accelerate/1642505-vimageconvert_argb8888toxrgb2101)Added [vImageConvert_ARGBFFFFToARGB2101010()](https://developer.apple.com/documentation/accelerate/1642433-vimageconvert_argbfffftoargb2101)Added [vImageConvert_ARGBFFFFToXRGB2101010()](https://developer.apple.com/documentation/accelerate/1642412-vimageconvert_argbfffftoxrgb2101)Added #def vImageConvert_BGRA5551toBGRA8888Added #def vImageConvert_BGRA8888toBGRA5551Added #def vImageConvert_BGRA8888toBGRA5551_ditheredAdded [vImageConvert_BGRA8888toRGB565_dithered()](https://developer.apple.com/documentation/accelerate/1642341-vimageconvert_bgra8888torgb565_d)Added [vImageConvert_Planar16Q12toARGB16F()](https://developer.apple.com/documentation/accelerate/1642580-vimageconvert_planar16q12toargb1)Added [vImageConvert_Planar16Q12toRGB16F()](https://developer.apple.com/documentation/accelerate/1642476-vimageconvert_planar16q12torgb16)Added [vImageConvert_Planar16UtoPlanar8_dithered()](https://developer.apple.com/documentation/accelerate/1642293-vimageconvert_planar16utoplanar8)Added [vImageConvert_RGB16UtoRGB888_dithered()](https://developer.apple.com/documentation/accelerate/1642378-vimageconvert_rgb16utorgb888_dit)Added [vImageConvert_RGB888toRGB565_dithered()](https://developer.apple.com/documentation/accelerate/1642316-vimageconvert_rgb888torgb565_dit)Added [vImageConvert_RGBA5551toRGBA8888()](https://developer.apple.com/documentation/accelerate/1642297-vimageconvert_rgba5551torgba8888)Added [vImageConvert_RGBA8888toRGB565_dithered()](https://developer.apple.com/documentation/accelerate/1642347-vimageconvert_rgba8888torgb565_d)Added [vImageConvert_RGBA8888toRGBA5551()](https://developer.apple.com/documentation/accelerate/1642450-vimageconvert_rgba8888torgba5551)Added [vImageConvert_RGBA8888toRGBA5551_dithered()](https://developer.apple.com/documentation/accelerate/1642566-vimageconvert_rgba8888torgba5551)Added [vImageConvert_XRGB2101010ToARGB16F()](https://developer.apple.com/documentation/accelerate/1642403-vimageconvert_xrgb2101010toargb1)Added [vImageConvert_XRGB2101010ToARGB16Q12()](https://developer.apple.com/documentation/accelerate/1642361-vimageconvert_xrgb2101010toargb1)Added [vImageConvert_XRGB2101010ToARGB16U()](https://developer.apple.com/documentation/accelerate/1642353-vimageconvert_xrgb2101010toargb1)Added [vImageConvert_XRGB2101010ToARGB8888()](https://developer.apple.com/documentation/accelerate/1642591-vimageconvert_xrgb2101010toargb8)Added [vImageConvert_XRGB2101010ToARGBFFFF()](https://developer.apple.com/documentation/accelerate/1642428-vimageconvert_xrgb2101010toargbf)Added [vImagePermuteChannelsWithMaskedInsert_ARGB16U()](https://developer.apple.com/documentation/accelerate/1642490-vimagepermutechannelswithmaskedi)

#### Geometry.h

Added [vImageHorizontalShear_CbCr16U()](https://developer.apple.com/documentation/accelerate/1642483-vimagehorizontalshear_cbcr16u)Added [vImageHorizontalShear_CbCr8()](https://developer.apple.com/documentation/accelerate/1642529-vimagehorizontalshear_cbcr8)Added [vImageHorizontalShear_XRGB2101010W()](https://developer.apple.com/documentation/accelerate/1642303-vimagehorizontalshear_xrgb210101)Added [vImageScale_CbCr16U()](https://developer.apple.com/documentation/accelerate/1642532-vimagescale_cbcr16u)Added [vImageScale_CbCr8()](https://developer.apple.com/documentation/accelerate/1642327-vimagescale_cbcr8)Added [vImageScale_XRGB2101010W()](https://developer.apple.com/documentation/accelerate/1642426-vimagescale_xrgb2101010w)Added [vImageVerticalShear_CbCr16U()](https://developer.apple.com/documentation/accelerate/1642310-vimageverticalshear_cbcr16u)Added [vImageVerticalShear_CbCr8()](https://developer.apple.com/documentation/accelerate/1642507-vimageverticalshear_cbcr8)Added [vImageVerticalShear_XRGB2101010W()](https://developer.apple.com/documentation/accelerate/1642377-vimageverticalshear_xrgb2101010w)

#### Quadrature/Integration.h (Added)

Added quadrature_function_arrayAdded [quadrature_integrate()](https://developer.apple.com/documentation/accelerate/1642331-quadrature_integrate)Added quadrature_integrate_functionAdded quadrature_integrate_optionsAdded QUADRATURE_INTEGRATE_QAGAdded #def QUADRATURE_INTEGRATE_QAG_WORKSPACE_PER_INTERVALAdded QUADRATURE_INTEGRATE_QAGSAdded #def QUADRATURE_INTEGRATE_QAGS_WORKSPACE_PER_INTERVALAdded QUADRATURE_INTEGRATE_QNGAdded #def QUADRATURE_INTEGRATION_HAdded quadrature_integrator

#### Quadrature/Quadrature.h (Added)

Added QUADRATURE_ALLOC_ERRORAdded QUADRATURE_ERRORAdded QUADRATURE_INTEGRATE_BAD_BEHAVIOUR_ERRORAdded QUADRATURE_INTEGRATE_MAX_EVAL_ERRORAdded QUADRATURE_INTERNAL_ERRORAdded QUADRATURE_INVALID_ARG_ERRORAdded quadrature_statusAdded QUADRATURE_SUCCESS

#### Sparse/BLAS.h

Added [sparse_matrix_product_sparse_double()](https://developer.apple.com/documentation/accelerate/1642343-sparse_matrix_product_sparse_dou)Added [sparse_matrix_product_sparse_float()](https://developer.apple.com/documentation/accelerate/1642617-sparse_matrix_product_sparse_flo)

#### Transform.h

Added [vImageLookupTable_Planar16()](https://developer.apple.com/documentation/accelerate/1641964-vimagelookuptable_planar16)Added [vImageLookupTable_Planar8toPlanar128()](https://developer.apple.com/documentation/accelerate/1641965-vimagelookuptable_planar8toplana)Added [vImageLookupTable_Planar8toPlanar24()](https://developer.apple.com/documentation/accelerate/1641962-vimagelookuptable_planar8toplana)Added [vImageLookupTable_Planar8toPlanar48()](https://developer.apple.com/documentation/accelerate/1641957-vimagelookuptable_planar8toplana)Added [vImageLookupTable_Planar8toPlanar96()](https://developer.apple.com/documentation/accelerate/1641963-vimagelookuptable_planar8toplana)Added [vImageSymmetricPiecewiseGamma_Planar16Q12()](https://developer.apple.com/documentation/accelerate/1641959-vimagesymmetricpiecewisegamma_pl)Added [vImageSymmetricPiecewiseGamma_PlanarF()](https://developer.apple.com/documentation/accelerate/1641958-vimagesymmetricpiecewisegamma_pl)

#### vDSP.h

Added #def vDSP_ENUMModified [vDSP_dotpr2()](https://developer.apple.com/documentation/accelerate/1450752-vdsp_dotpr2)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr2 (     const float *__A0,     vDSP_Stride __A0Stride,     const float *__A1,     vDSP_Stride __A1Stride,     const float *__B,     vDSP_Stride __BStride,     float *__C0,     float *__C1,     vDSP_Length __Length ); ``` |
| To | ``` void vDSP_dotpr2 (     const float *__A0,     vDSP_Stride __IA0,     const float *__A1,     vDSP_Stride __IA1,     const float *__B,     vDSP_Stride __IB,     float *__C0,     float *__C1,     vDSP_Length __N ); ``` |

Modified [vDSP_dotpr2_s1_15()](https://developer.apple.com/documentation/accelerate/1449919-vdsp_dotpr2_s1_15)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr2_s1_15 (     const short *__A0,     vDSP_Stride __A0Stride,     const short *__A1,     vDSP_Stride __A1Stride,     const short *__B,     vDSP_Stride __BStride,     short *__C0,     short *__C1,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_dotpr2_s1_15 (     const short *__A0,     vDSP_Stride __IA0,     const short *__A1,     vDSP_Stride __IA1,     const short *__B,     vDSP_Stride __IB,     short *__C0,     short *__C1,     vDSP_Length __N ); ``` |

Modified [vDSP_dotpr2_s8_24()](https://developer.apple.com/documentation/accelerate/1449663-vdsp_dotpr2_s8_24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr2_s8_24 (     const int *__A0,     vDSP_Stride __A0Stride,     const int *__A1,     vDSP_Stride __A1Stride,     const int *__B,     vDSP_Stride __BStride,     int *__C0,     int *__C1,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_dotpr2_s8_24 (     const int *__A0,     vDSP_Stride __IA0,     const int *__A1,     vDSP_Stride __IA1,     const int *__B,     vDSP_Stride __IB,     int *__C0,     int *__C1,     vDSP_Length __N ); ``` |

Modified [vDSP_dotpr2D()](https://developer.apple.com/documentation/accelerate/1450152-vdsp_dotpr2d)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr2D (     const double *__A0,     vDSP_Stride __A0Stride,     const double *__A1,     vDSP_Stride __A1Stride,     const double *__B,     vDSP_Stride __BStride,     double *__C0,     double *__C1,     vDSP_Length __Length ); ``` |
| To | ``` void vDSP_dotpr2D (     const double *__A0,     vDSP_Stride __IA0,     const double *__A1,     vDSP_Stride __IA1,     const double *__B,     vDSP_Stride __IB,     double *__C0,     double *__C1,     vDSP_Length __N ); ``` |

Modified [vDSP_dotpr_s1_15()](https://developer.apple.com/documentation/accelerate/1449796-vdsp_dotpr_s1_15)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr_s1_15 (     const short *__A,     vDSP_Stride __AStride,     const short *__B,     vDSP_Stride __BStride,     short *__C,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_dotpr_s1_15 (     const short *__A,     vDSP_Stride __IA,     const short *__B,     vDSP_Stride __IB,     short *__C,     vDSP_Length __N ); ``` |

Modified [vDSP_dotpr_s8_24()](https://developer.apple.com/documentation/accelerate/1450480-vdsp_dotpr_s8_24)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_dotpr_s8_24 (     const int *__A,     vDSP_Stride __AStride,     const int *__B,     vDSP_Stride __BStride,     int *__C,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_dotpr_s8_24 (     const int *__A,     vDSP_Stride __IA,     const int *__B,     vDSP_Stride __IB,     int *__C,     vDSP_Length __N ); ``` |

Modified [vDSP_vdist()](https://developer.apple.com/documentation/accelerate/1450257-vdsp_vdist)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdist (     const float *__A,     vDSP_Stride __I,     const float *__B,     vDSP_Stride __J,     float *__C,     vDSP_Stride __K,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_vdist (     const float *__A,     vDSP_Stride __IA,     const float *__B,     vDSP_Stride __IB,     float *__C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vdistD()](https://developer.apple.com/documentation/accelerate/1449966-vdsp_vdistd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdistD (     const double *__A,     vDSP_Stride __I,     const double *__B,     vDSP_Stride __J,     double *__C,     vDSP_Stride __K,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_vdistD (     const double *__A,     vDSP_Stride __IA,     const double *__B,     vDSP_Stride __IB,     double *__C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfill()](https://developer.apple.com/documentation/kernel/1579967-vdsp_vfill)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfill (     const float *__A,     float *__C,     vDSP_Stride __IA,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_vfill (     const float *__A,     float *__C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmsaD()](https://developer.apple.com/documentation/accelerate/1450432-vdsp_vsmsad)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmsaD (     const double *__A,     vDSP_Stride __IA,     const double *__B,     const double *__C,     double *__ID,     vDSP_Stride __L,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_vsmsaD (     const double *__A,     vDSP_Stride __IA,     const double *__B,     const double *__C,     double *__D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmsb()](https://developer.apple.com/documentation/accelerate/1450822-vdsp_vsmsb)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmsb (     const float *__A,     vDSP_Stride __I,     const float *__B,     const float *__C,     vDSP_Stride __K,     float *__D,     vDSP_Stride __L,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_vsmsb (     const float *__A,     vDSP_Stride __IA,     const float *__B,     const float *__C,     vDSP_Stride __IC,     float *__D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmsbD()](https://developer.apple.com/documentation/accelerate/1450238-vdsp_vsmsbd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmsbD (     const double *__A,     vDSP_Stride __I,     const double *__B,     const double *__C,     vDSP_Stride __K,     double *__D,     vDSP_Stride __L,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_vsmsbD (     const double *__A,     vDSP_Stride __IA,     const double *__B,     const double *__C,     vDSP_Stride __IC,     double *__D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vtabiD()](https://developer.apple.com/documentation/accelerate/1449832-vdsp_vtabid)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vtabiD (     const double *__A,     vDSP_Stride __IA,     const double *__S1,     const double *__S2,     const double *__C,     vDSP_Length __M,     double *__ID,     vDSP_Stride __L,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_vtabiD (     const double *__A,     vDSP_Stride __IA,     const double *__S1,     const double *__S2,     const double *__C,     vDSP_Length __M,     double *__D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

#### vfp.h

Removed vintf()Modified [vceilf()](https://developer.apple.com/documentation/accelerate/1556252-vceilf)

|  | Declaration |
| --- | --- |
| From | ``` vFloat vceilf (     vFloat ); ``` |
| To | ``` vFloat vceilf (     vFloat __vfp_a ); ``` |

Modified [vfloorf()](https://developer.apple.com/documentation/accelerate/1556275-vfloorf)

|  | Declaration |
| --- | --- |
| From | ``` vFloat vfloorf (     vFloat ); ``` |
| To | ``` vFloat vfloorf (     vFloat __vfp_a ); ``` |

Modified [vnintf()](https://developer.apple.com/documentation/accelerate/1556253-vnintf)

|  | Declaration |
| --- | --- |
| From | ``` vFloat vnintf (     vFloat ); ``` |
| To | ``` vFloat vnintf (     vFloat __vfp_a ); ``` |

Modified vtruncf()

|  | Declaration |
| --- | --- |
| From | ``` vFloat vtruncf (     vFloat ); ``` |
| To | ``` vFloat vtruncf (     vFloat __vfp_a ); ``` |

#### vImage_Types.h

Added [kvImageDoNotClamp](https://developer.apple.com/documentation/accelerate/1578976-processing_flags/kvimagedonotclamp)Added Pixel_16U16UAdded Pixel_32UAdded Pixel_88

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
