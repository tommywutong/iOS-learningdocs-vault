---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/Accelerate.html
archived_at: '2026-07-18T02:54:07.573567Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# Accelerate Changes

## Accelerate

Alpha.hAdded [vImagePremultipliedAlphaBlendWithPermute_ARGB8888()](https://developer.apple.com/documentation/accelerate/1410688-vimagepremultipliedalphablendwit)Added [vImagePremultipliedAlphaBlendWithPermute_RGBA8888()](https://developer.apple.com/documentation/accelerate/1410721-vimagepremultipliedalphablendwit)Added [vImagePremultiplyData_ARGB16Q12()](https://developer.apple.com/documentation/accelerate/1410659-vimagepremultiplydata_argb16q12)Added [vImagePremultiplyData_RGBA16Q12()](https://developer.apple.com/documentation/accelerate/1410636-vimagepremultiplydata_rgba16q12)Added [vImageUnpremultiplyData_ARGB16Q12()](https://developer.apple.com/documentation/accelerate/1410730-vimageunpremultiplydata_argb16q1)Added [vImageUnpremultiplyData_RGBA16Q12()](https://developer.apple.com/documentation/accelerate/1410683-vimageunpremultiplydata_rgba16q1)Conversion.hAdded [kvImageConvert_DitherAtkinson](https://developer.apple.com/documentation/accelerate/kvimageconvert_ditheratkinson)Added [kvImageConvert_DitherFloydSteinberg](https://developer.apple.com/documentation/accelerate/kvimageconvert_ditherfloydsteinberg)Added [kvImageConvert_DitherNone](https://developer.apple.com/documentation/accelerate/1533233-dithering_methods/kvimageconvert_dithernone)Added [kvImageConvert_DitherOrdered](https://developer.apple.com/documentation/accelerate/1533233-dithering_methods/kvimageconvert_ditherordered)Added [kvImageConvert_DitherOrderedReproducible](https://developer.apple.com/documentation/accelerate/kvimageconvert_ditherorderedreproducible)Added [kvImageConvert_OrderedGaussianBlue](https://developer.apple.com/documentation/accelerate/kvimageconvert_orderedgaussianblue)Added [kvImageConvert_OrderedNoiseShapeMask](https://developer.apple.com/documentation/accelerate/1533233-dithering_methods/kvimageconvert_orderednoiseshapemask)Added [kvImageConvert_OrderedUniformBlue](https://developer.apple.com/documentation/accelerate/1533233-dithering_methods/kvimageconvert_ordereduniformblue)Added [vImageBufferFill_ARGB16S()](https://developer.apple.com/documentation/accelerate/1533219-vimagebufferfill_argb16s)Added [vImageBufferFill_ARGB16U()](https://developer.apple.com/documentation/accelerate/1533077-vimagebufferfill_argb16u)Added [vImageByteSwap_Planar16U()](https://developer.apple.com/documentation/accelerate/1533153-vimagebyteswap_planar16u)Added [vImageConvert_16Fto16U()](https://developer.apple.com/documentation/accelerate/1533203-vimageconvert_16fto16u)Added [vImageConvert_16Q12to16U()](https://developer.apple.com/documentation/accelerate/1533226-vimageconvert_16q12to16u)Added [vImageConvert_16Q12to8()](https://developer.apple.com/documentation/accelerate/1533295-vimageconvert_16q12to8)Added [vImageConvert_16Q12toF()](https://developer.apple.com/documentation/accelerate/1533114-vimageconvert_16q12tof)Added [vImageConvert_16Uto16F()](https://developer.apple.com/documentation/accelerate/1533082-vimageconvert_16uto16f)Added [vImageConvert_16Uto16Q12()](https://developer.apple.com/documentation/accelerate/1533100-vimageconvert_16uto16q12)Added [vImageConvert_8to16Q12()](https://developer.apple.com/documentation/accelerate/1533296-vimageconvert_8to16q12)Added [vImageConvert_ARGB16UToARGB8888()](https://developer.apple.com/documentation/accelerate/1533191-vimageconvert_argb16utoargb8888)Added [vImageConvert_ARGB16UtoPlanar16U()](https://developer.apple.com/documentation/accelerate/1533248-vimageconvert_argb16utoplanar16u)Added [vImageConvert_ARGB16UtoRGB16U()](https://developer.apple.com/documentation/accelerate/1533087-vimageconvert_argb16utorgb16u)Added [vImageConvert_ARGB8888ToARGB16U()](https://developer.apple.com/documentation/accelerate/1533031-vimageconvert_argb8888toargb16u)Added [vImageConvert_ARGB8888ToRGB16U()](https://developer.apple.com/documentation/accelerate/1533004-vimageconvert_argb8888torgb16u)Added [vImageConvert_ARGB8888toPlanar16Q12()](https://developer.apple.com/documentation/accelerate/1533126-vimageconvert_argb8888toplanar16)Added [vImageConvert_ARGB8888toPlanarF()](https://developer.apple.com/documentation/accelerate/1533036-vimageconvert_argb8888toplanarf)Added [vImageConvert_ARGBFFFFtoPlanar8()](https://developer.apple.com/documentation/accelerate/1533059-vimageconvert_argbfffftoplanar8)Added [vImageConvert_ARGBFFFFtoRGBFFF()](https://developer.apple.com/documentation/accelerate/1533142-vimageconvert_argbfffftorgbfff)Added [vImageConvert_BGRA16UtoRGB16U()](https://developer.apple.com/documentation/accelerate/1533183-vimageconvert_bgra16utorgb16u)Added #def vImageConvert_BGRA8888toPlanar8Added [vImageConvert_BGRA8888toRGB565()](https://developer.apple.com/documentation/accelerate/1533285-vimageconvert_bgra8888torgb565)Added #def vImageConvert_BGRAFFFFtoPlanarFAdded [vImageConvert_BGRAFFFFtoRGBFFF()](https://developer.apple.com/documentation/accelerate/1533214-vimageconvert_bgrafffftorgbfff)Added #def vImageConvert_BGRFFFtoBGRAFFFFAdded #def vImageConvert_BGRFFFtoRGBAFFFFAdded [vImageConvert_BGRX8888ToPlanar8()](https://developer.apple.com/documentation/accelerate/1533037-vimageconvert_bgrx8888toplanar8)Added [vImageConvert_BGRXFFFFToPlanarF()](https://developer.apple.com/documentation/accelerate/1533129-vimageconvert_bgrxfffftoplanarf)Added [vImageConvert_Fto16Q12()](https://developer.apple.com/documentation/accelerate/1533200-vimageconvert_fto16q12)Added [vImageConvert_Indexed1toPlanar8()](https://developer.apple.com/documentation/accelerate/1533038-vimageconvert_indexed1toplanar8)Added [vImageConvert_Indexed2toPlanar8()](https://developer.apple.com/documentation/accelerate/1533271-vimageconvert_indexed2toplanar8)Added [vImageConvert_Indexed4toPlanar8()](https://developer.apple.com/documentation/accelerate/1533028-vimageconvert_indexed4toplanar8)Added [vImageConvert_Planar16FtoPlanar8()](https://developer.apple.com/documentation/accelerate/1533139-vimageconvert_planar16ftoplanar8)Added [vImageConvert_Planar16Q12toARGB8888()](https://developer.apple.com/documentation/accelerate/1533180-vimageconvert_planar16q12toargb8)Added [vImageConvert_Planar16Q12toRGB888()](https://developer.apple.com/documentation/accelerate/1533184-vimageconvert_planar16q12torgb88)Added [vImageConvert_Planar16UtoARGB16U()](https://developer.apple.com/documentation/accelerate/1533093-vimageconvert_planar16utoargb16u)Added [vImageConvert_Planar16UtoRGB16U()](https://developer.apple.com/documentation/accelerate/1533025-vimageconvert_planar16utorgb16u)Added [vImageConvert_Planar1toPlanar8()](https://developer.apple.com/documentation/accelerate/1533136-vimageconvert_planar1toplanar8)Added [vImageConvert_Planar2toPlanar8()](https://developer.apple.com/documentation/accelerate/1533035-vimageconvert_planar2toplanar8)Added [vImageConvert_Planar4toPlanar8()](https://developer.apple.com/documentation/accelerate/1533091-vimageconvert_planar4toplanar8)Added [vImageConvert_Planar8toIndexed1()](https://developer.apple.com/documentation/accelerate/1533115-vimageconvert_planar8toindexed1)Added [vImageConvert_Planar8toIndexed2()](https://developer.apple.com/documentation/accelerate/1533017-vimageconvert_planar8toindexed2)Added [vImageConvert_Planar8toIndexed4()](https://developer.apple.com/documentation/accelerate/1533049-vimageconvert_planar8toindexed4)Added [vImageConvert_Planar8toPlanar1()](https://developer.apple.com/documentation/accelerate/1533024-vimageconvert_planar8toplanar1)Added [vImageConvert_Planar8toPlanar16F()](https://developer.apple.com/documentation/accelerate/1533064-vimageconvert_planar8toplanar16f)Added [vImageConvert_Planar8toPlanar2()](https://developer.apple.com/documentation/accelerate/1533166-vimageconvert_planar8toplanar2)Added [vImageConvert_Planar8toPlanar4()](https://developer.apple.com/documentation/accelerate/1533223-vimageconvert_planar8toplanar4)Added [vImageConvert_RGB16UToARGB8888()](https://developer.apple.com/documentation/accelerate/1533005-vimageconvert_rgb16utoargb8888)Added [vImageConvert_RGB16UtoARGB16U()](https://developer.apple.com/documentation/accelerate/1533272-vimageconvert_rgb16utoargb16u)Added [vImageConvert_RGB16UtoBGRA16U()](https://developer.apple.com/documentation/accelerate/1533033-vimageconvert_rgb16utobgra16u)Added [vImageConvert_RGB16UtoPlanar16U()](https://developer.apple.com/documentation/accelerate/1533021-vimageconvert_rgb16utoplanar16u)Added [vImageConvert_RGB16UtoRGBA16U()](https://developer.apple.com/documentation/accelerate/1533158-vimageconvert_rgb16utorgba16u)Added [vImageConvert_RGB565toBGRA8888()](https://developer.apple.com/documentation/accelerate/1533057-vimageconvert_rgb565tobgra8888)Added [vImageConvert_RGB565toRGBA8888()](https://developer.apple.com/documentation/accelerate/1533249-vimageconvert_rgb565torgba8888)Added [vImageConvert_RGB888toPlanar16Q12()](https://developer.apple.com/documentation/accelerate/1533023-vimageconvert_rgb888toplanar16q1)Added [vImageConvert_RGBA16UtoRGB16U()](https://developer.apple.com/documentation/accelerate/1533149-vimageconvert_rgba16utorgb16u)Added #def vImageConvert_RGBA8888toPlanar8Added [vImageConvert_RGBA8888toRGB565()](https://developer.apple.com/documentation/accelerate/1533162-vimageconvert_rgba8888torgb565)Added #def vImageConvert_RGBAFFFFtoPlanarFAdded [vImageConvert_RGBAFFFFtoRGBFFF()](https://developer.apple.com/documentation/accelerate/1533187-vimageconvert_rgbafffftorgbfff)Added [vImageConvert_RGBFFFtoARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533175-vimageconvert_rgbffftoargbffff)Added [vImageConvert_RGBFFFtoBGRAFFFF()](https://developer.apple.com/documentation/accelerate/1533277-vimageconvert_rgbffftobgraffff)Added [vImageConvert_RGBFFFtoRGBAFFFF()](https://developer.apple.com/documentation/accelerate/1533050-vimageconvert_rgbffftorgbaffff)Added #def vImageConvert_RGBX8888ToPlanar8Added #def vImageConvert_RGBXFFFFToPlanarFAdded [vImageConvert_XRGB8888ToPlanar8()](https://developer.apple.com/documentation/accelerate/1533026-vimageconvert_xrgb8888toplanar8)Added [vImageConvert_XRGBFFFFToPlanarF()](https://developer.apple.com/documentation/accelerate/1533067-vimageconvert_xrgbfffftoplanarf)Added [vImageFlatten_ARGB16Q12()](https://developer.apple.com/documentation/accelerate/1533177-vimageflatten_argb16q12)Added [vImageFlatten_ARGB16U()](https://developer.apple.com/documentation/accelerate/1533278-vimageflatten_argb16u)Added [vImageFlatten_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533236-vimageflatten_argb8888)Added [vImageFlatten_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533071-vimageflatten_argbffff)Added #def vImageFlatten_BGRAFFFFToBGRFFFAdded [vImageFlatten_RGBA16Q12()](https://developer.apple.com/documentation/accelerate/1533112-vimageflatten_rgba16q12)Added [vImageFlatten_RGBA16U()](https://developer.apple.com/documentation/accelerate/1533048-vimageflatten_rgba16u)Added [vImageFlatten_RGBA8888()](https://developer.apple.com/documentation/accelerate/1532998-vimageflatten_rgba8888)Added [vImageFlatten_RGBAFFFF()](https://developer.apple.com/documentation/accelerate/1533221-vimageflatten_rgbaffff)Added #def vImageFlatten_RGBAFFFFToBGRFFFAdded [vImageOverwriteChannelsWithPixel_ARGB16U()](https://developer.apple.com/documentation/accelerate/1533053-vimageoverwritechannelswithpixel)Added [vImagePermuteChannelsWithMaskedInsert_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533263-vimagepermutechannelswithmaskedi)Added [vImagePermuteChannelsWithMaskedInsert_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533014-vimagepermutechannelswithmaskedi)Added [vImagePermuteChannels_ARGB16U()](https://developer.apple.com/documentation/accelerate/1533081-vimagepermutechannels_argb16u)Modified [vImageConvert_BGRA8888toRGB888()](https://developer.apple.com/documentation/accelerate/1533090-vimageconvert_bgra8888torgb888)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.9 |

Modified [vImageConvert_RGBA8888toRGB888()](https://developer.apple.com/documentation/accelerate/1533062-vimageconvert_rgba8888torgb888)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.9 |

Modified [vImageFlatten_ARGB8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533019-vimageflatten_argb8888torgb888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_ARGB8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_8888, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_ARGB8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_8888, bool, vImage_Flags); |

Modified [vImageFlatten_ARGBFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533210-vimageflatten_argbfffftorgbfff)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_ARGBFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_FFFF, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_ARGBFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_FFFF, bool, vImage_Flags); |

Modified [vImageFlatten_BGRA8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533119-vimageflatten_bgra8888torgb888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_BGRA8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_8888, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_BGRA8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_8888, bool, vImage_Flags); |

Modified [vImageFlatten_BGRAFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533156-vimageflatten_bgrafffftorgbfff)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_BGRAFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_FFFF, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_BGRAFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_FFFF, bool, vImage_Flags); |

Modified [vImageFlatten_RGBA8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533147-vimageflatten_rgba8888torgb888)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_RGBA8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_8888, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_RGBA8888ToRGB888 ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_8888, bool, vImage_Flags); |

Modified [vImageFlatten_RGBAFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533280-vimageflatten_rgbafffftorgbfff)

|  | Declaration |
| --- | --- |
| From | vImage_Error vImageFlatten_RGBAFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, Pixel_FFFF, bool, vImage_Flags); |
| To | vImage_Error vImageFlatten_RGBAFFFFToRGBFFF ( const vImage_Buffer \*, const vImage_Buffer \*, const Pixel_FFFF, bool, vImage_Flags); |

Geometry.hAdded [vImageAffineWarpCG_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509246-vimageaffinewarpcg_argb16s)Added [vImageAffineWarpCG_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509186-vimageaffinewarpcg_argb16u)Added [vImageAffineWarpD_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509282-vimageaffinewarpd_argb16s)Added [vImageAffineWarpD_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509292-vimageaffinewarpd_argb16u)Added [vImageAffineWarp_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509164-vimageaffinewarp_argb16s)Added [vImageAffineWarp_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509156-vimageaffinewarp_argb16u)Added [vImageGetResamplingFilterExtent()](https://developer.apple.com/documentation/accelerate/1509196-vimagegetresamplingfilterextent)Added [vImageHorizontalReflect_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509172-vimagehorizontalreflect_argb16s)Added [vImageHorizontalReflect_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509180-vimagehorizontalreflect_argb16u)Added [vImageHorizontalReflect_Planar16U()](https://developer.apple.com/documentation/accelerate/1509287-vimagehorizontalreflect_planar16)Added [vImageHorizontalShearD_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509268-vimagehorizontalsheard_argb16s)Added [vImageHorizontalShearD_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509248-vimagehorizontalsheard_argb16u)Added [vImageHorizontalShear_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509194-vimagehorizontalshear_argb16s)Added [vImageHorizontalShear_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509274-vimagehorizontalshear_argb16u)Added [vImageRotate90_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509195-vimagerotate90_argb16s)Added [vImageRotate90_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509232-vimagerotate90_argb16u)Added [vImageRotate90_Planar16U()](https://developer.apple.com/documentation/accelerate/1509205-vimagerotate90_planar16u)Added [vImageRotate_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509206-vimagerotate_argb16s)Added [vImageRotate_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509235-vimagerotate_argb16u)Added [vImageScale_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509174-vimagescale_argb16s)Added [vImageScale_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509158-vimagescale_argb16u)Added [vImageVerticalReflect_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509267-vimageverticalreflect_argb16s)Added [vImageVerticalReflect_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509197-vimageverticalreflect_argb16u)Added [vImageVerticalReflect_Planar16U()](https://developer.apple.com/documentation/accelerate/1509265-vimageverticalreflect_planar16u)Added [vImageVerticalShearD_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509278-vimageverticalsheard_argb16s)Added [vImageVerticalShearD_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509225-vimageverticalsheard_argb16u)Added [vImageVerticalShear_ARGB16S()](https://developer.apple.com/documentation/accelerate/1509154-vimageverticalshear_argb16s)Added [vImageVerticalShear_ARGB16U()](https://developer.apple.com/documentation/accelerate/1509227-vimageverticalshear_argb16u)Transform.hAdded [kvImageFullInterpolation](https://developer.apple.com/documentation/accelerate/kvimagefullinterpolation)Added [kvImageHalfInterpolation](https://developer.apple.com/documentation/accelerate/vimage_interpolationmethod/kvimagehalfinterpolation)Added [kvImageMDTableHint_16Q12](https://developer.apple.com/documentation/accelerate/kvimagemdtablehint_16q12)Added [kvImageMDTableHint_Float](https://developer.apple.com/documentation/accelerate/vimagemdtableusagehint/kvimagemdtablehint_float)Added [kvImageNoInterpolation](https://developer.apple.com/documentation/accelerate/kvimagenointerpolation)Added [vImageLookupTable_8to64U()](https://developer.apple.com/documentation/accelerate/1545860-vimagelookuptable_8to64u)Added [vImageLookupTable_Planar8toPlanar16()](https://developer.apple.com/documentation/accelerate/1545120-vimagelookuptable_planar8toplana)Added [vImageMDTableUsageHint](https://developer.apple.com/documentation/accelerate/vimagemdtableusagehint)Added [vImageMatrixMultiply_Planar16S()](https://developer.apple.com/documentation/accelerate/1545211-vimagematrixmultiply_planar16s)Added [vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12()](https://developer.apple.com/documentation/accelerate/1546327-vimagemultidimensionalinterpolat)Added [vImageMultiDimensionalInterpolatedLookupTable_PlanarF()](https://developer.apple.com/documentation/accelerate/1546728-vimagemultidimensionalinterpolat)Added [vImageMultidimensionalTable_Create()](https://developer.apple.com/documentation/accelerate/1544435-vimagemultidimensionaltable_crea)Added [vImageMultidimensionalTable_Release()](https://developer.apple.com/documentation/accelerate/1546993-vimagemultidimensionaltable_rele)Added [vImageMultidimensionalTable_Retain()](https://developer.apple.com/documentation/accelerate/1545031-vimagemultidimensionaltable_reta)Added [vImagePiecewiseGamma_Planar16Q12()](https://developer.apple.com/documentation/accelerate/1545796-vimagepiecewisegamma_planar16q12)Added [vImagePiecewiseGamma_Planar16Q12toPlanar8()](https://developer.apple.com/documentation/accelerate/1544548-vimagepiecewisegamma_planar16q12)Added [vImagePiecewiseGamma_Planar8()](https://developer.apple.com/documentation/accelerate/1546371-vimagepiecewisegamma_planar8)Added [vImagePiecewiseGamma_Planar8toPlanar16Q12()](https://developer.apple.com/documentation/accelerate/1546537-vimagepiecewisegamma_planar8topl)Added [vImagePiecewiseGamma_Planar8toPlanarF()](https://developer.apple.com/documentation/accelerate/1544764-vimagepiecewisegamma_planar8topl)Added [vImagePiecewiseGamma_PlanarF()](https://developer.apple.com/documentation/accelerate/1544860-vimagepiecewisegamma_planarf)Added [vImagePiecewiseGamma_PlanarFtoPlanar8()](https://developer.apple.com/documentation/accelerate/1546645-vimagepiecewisegamma_planarftopl)Added [vImage_InterpolationMethod](https://developer.apple.com/documentation/accelerate/vimage_interpolationmethod)Added [vImage_MultidimensionalTable](https://developer.apple.com/documentation/accelerate/vimage_multidimensionaltable)cblas.hModified ATLU_DestroyThreadMemory()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

vBasicOps.hModified [vLL64Shift()](https://developer.apple.com/documentation/accelerate/1442930-vll64shift)

|  | Introduction | Declaration |
| --- | --- | --- |
| From | OS X 10.0 | vUInt32 vLL64Shift ( vUInt32 vA, vUInt8 vShiftFactor); |
| To | _none_ | vUInt32 vLL64Shift ( vUInt32 __vbasicops_vA, vUInt8 __vbasicops_vShiftFactor); |

Modified [vLR64Shift()](https://developer.apple.com/documentation/accelerate/1442973-vlr64shift)

|  | Introduction | Declaration |
| --- | --- | --- |
| From | OS X 10.0 | vUInt32 vLR64Shift ( vUInt32 vA, vUInt8 vShiftFactor); |
| To | _none_ | vUInt32 vLR64Shift ( vUInt32 __vbasicops_vA, vUInt8 __vbasicops_vShiftFactor); |

Modified [vS16HalfMultiply()](https://developer.apple.com/documentation/accelerate/1442969-vs16halfmultiply)

|  | Introduction | Declaration |
| --- | --- | --- |
| From | OS X 10.0 | vSInt16 vS16HalfMultiply ( vSInt16 vA, vSInt16 vB); |
| To | _none_ | vSInt16 vS16HalfMultiply ( vSInt16 __vbasicops_vA, vSInt16 __vbasicops_vB); |

Modified [vS64Add()](https://developer.apple.com/documentation/accelerate/1442951-vs64add)

|  | Introduction | Declaration |
| --- | --- | --- |
| From | OS X 10.0 | vSInt32 vS64Add ( vSInt32 vA, vSInt32 vB); |
| To | _none_ | vSInt32 vS64Add ( vSInt32 __vbasicops_vA, vSInt32 __vbasicops_vB); |

Modified [vS64Sub()](https://developer.apple.com/documentation/accelerate/1442916-vs64sub)

|  | Introduction | Declaration |
| --- | --- | --- |
| From | OS X 10.0 | vSInt32 vS64Sub ( vSInt32 vA, vSInt32 vB); |
| To | _none_ | vSInt32 vS64Sub ( vSInt32 __vbasicops_vA, vSInt32 __vbasicops_vB); |

Modified [vU16HalfMultiply()](https://developer.apple.com/documentation/accelerate/1442863-vu16halfmultiply)

|  | Introduction | Declaration |
| --- | --- | --- |
| From | OS X 10.0 | vUInt16 vU16HalfMultiply ( vUInt16 vA, vUInt16 vB); |
| To | _none_ | vUInt16 vU16HalfMultiply ( vUInt16 __vbasicops_vA, vUInt16 __vbasicops_vB); |

Modified [vU32FullMulEven()](https://developer.apple.com/documentation/accelerate/1442871-vu32fullmuleven)

|  | Introduction | Declaration |
| --- | --- | --- |
| From | OS X 10.0 | vUInt32 vU32FullMulEven ( vUInt32 vA, vUInt32 vB); |
| To | _none_ | vUInt32 vU32FullMulEven ( vUInt32 __vbasicops_vA, vUInt32 __vbasicops_vB); |

Modified [vU32FullMulOdd()](https://developer.apple.com/documentation/accelerate/1442965-vu32fullmulodd)

|  | Introduction | Declaration |
| --- | --- | --- |
| From | OS X 10.0 | vUInt32 vU32FullMulOdd ( vUInt32 vA, vUInt32 vB); |
| To | _none_ | vUInt32 vU32FullMulOdd ( vUInt32 __vbasicops_vA, vUInt32 __vbasicops_vB); |

Modified [vU64Add()](https://developer.apple.com/documentation/accelerate/1442922-vu64add)

|  | Introduction | Declaration |
| --- | --- | --- |
| From | OS X 10.0 | vUInt32 vU64Add ( vUInt32 vA, vUInt32 vB); |
| To | _none_ | vUInt32 vU64Add ( vUInt32 __vbasicops_vA, vUInt32 __vbasicops_vB); |

Modified [vU64Sub()](https://developer.apple.com/documentation/accelerate/1442904-vu64sub)

|  | Introduction | Declaration |
| --- | --- | --- |
| From | OS X 10.0 | vUInt32 vU64Sub ( vUInt32 vA, vUInt32 vB); |
| To | _none_ | vUInt32 vU64Sub ( vUInt32 __vbasicops_vA, vUInt32 __vbasicops_vB); |

vDSP.hAdded [vDSP_DCT_CreateSetup()](https://developer.apple.com/documentation/accelerate/1449930-vdsp_dct_createsetup)Added [vDSP_DCT_Execute()](https://developer.apple.com/documentation/accelerate/1450016-vdsp_dct_execute)Added vDSP_DCT_IIAdded vDSP_DCT_IIIAdded vDSP_DCT_TypeAdded [vDSP_DFT_DestroySetupD()](https://developer.apple.com/documentation/accelerate/1450367-vdsp_dft_destroysetupd)Added [vDSP_DFT_ExecuteD()](https://developer.apple.com/documentation/accelerate/1449812-vdsp_dft_executed)Added vDSP_DFT_SetupDAdded [vDSP_DFT_zop_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1450730-vdsp_dft_zop_createsetupd)Added [vDSP_DFT_zrop_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1449790-vdsp_dft_zrop_createsetupd)Added [vDSP_biquad()](https://developer.apple.com/documentation/accelerate/1450838-vdsp_biquad)Added [vDSP_biquadD()](https://developer.apple.com/documentation/accelerate/1450359-vdsp_biquadd)Added [vDSP_biquad_CreateSetup()](https://developer.apple.com/documentation/accelerate/1450374-vdsp_biquad_createsetup)Added [vDSP_biquad_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1450239-vdsp_biquad_createsetupd)Added [vDSP_biquad_DestroySetup()](https://developer.apple.com/documentation/accelerate/1450168-vdsp_biquad_destroysetup)Added [vDSP_biquad_DestroySetupD()](https://developer.apple.com/documentation/accelerate/1450640-vdsp_biquad_destroysetupd)Added [vDSP_biquad_Setup](https://developer.apple.com/documentation/kernel/vdsp_biquad_setup)Added [vDSP_biquad_SetupD](https://developer.apple.com/documentation/kernel/vdsp_biquad_setupd)Added [vDSP_biquadm()](https://developer.apple.com/documentation/accelerate/1450603-vdsp_biquadm)Added [vDSP_biquadm_CopyState()](https://developer.apple.com/documentation/kernel/1579980-vdsp_biquadm_copystate)Added [vDSP_biquadm_CreateSetup()](https://developer.apple.com/documentation/kernel/1579945-vdsp_biquadm_createsetup)Added [vDSP_biquadm_DestroySetup()](https://developer.apple.com/documentation/kernel/1579970-vdsp_biquadm_destroysetup)Added [vDSP_biquadm_ResetState()](https://developer.apple.com/documentation/accelerate/1449898-vdsp_biquadm_resetstate)Added [vDSP_biquadm_Setup](https://developer.apple.com/documentation/kernel/vdsp_biquadm_setup)Added [vDSP_int24](https://developer.apple.com/documentation/accelerate/vdsp_int24)Added [vDSP_uint24](https://developer.apple.com/documentation/accelerate/vdsp_uint24)Added [vDSP_vaddi()](https://developer.apple.com/documentation/accelerate/1450179-vdsp_vaddi)Added [vDSP_vflt24()](https://developer.apple.com/documentation/accelerate/1450529-vdsp_vflt24)Added [vDSP_vfltsm24()](https://developer.apple.com/documentation/accelerate/1450177-vdsp_vfltsm24)Added [vDSP_vfltsmu24()](https://developer.apple.com/documentation/accelerate/1449841-vdsp_vfltsmu24)Added [vDSP_vfltu24()](https://developer.apple.com/documentation/accelerate/1450084-vdsp_vfltu24)Added [vDSP_vsmfix24()](https://developer.apple.com/documentation/accelerate/1449670-vdsp_vsmfix24)Added [vDSP_vsmfixu24()](https://developer.apple.com/documentation/kernel/1532178-vdsp_vsmfixu24)Added [vDSP_vsmsma()](https://developer.apple.com/documentation/accelerate/1450324-vdsp_vsmsma)Added [vDSP_zvma()](https://developer.apple.com/documentation/accelerate/1449940-vdsp_zvma)Added [vDSP_zvmmaa()](https://developer.apple.com/documentation/accelerate/1450110-vdsp_zvmmaa)Modified conv()

|  | Declaration |
| --- | --- |
| From | void conv ( const float __vDSP_signal[], vDSP_Stride __vDSP_signalStride, const float __vDSP_filter[], vDSP_Stride __vDSP_strideFilter, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void conv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_F, vDSP_Stride __vDSP_IF, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified convD()

|  | Declaration |
| --- | --- |
| From | void convD ( const double __vDSP_signal[], vDSP_Stride __vDSP_signalStride, const double __vDSP_filter[], vDSP_Stride __vDSP_strideFilter, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void convD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_F, vDSP_Stride __vDSP_IF, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified create_fftsetup()

|  | Declaration |
| --- | --- |
| From | FFTSetup create_fftsetup ( vDSP_Length __vDSP_log2n, FFTRadix __vDSP_radix); |
| To | FFTSetup create_fftsetup ( vDSP_Length __vDSP_Log2n, FFTRadix __vDSP_Radix); |

Modified create_fftsetupD()

|  | Declaration |
| --- | --- |
| From | FFTSetupD create_fftsetupD ( vDSP_Length __vDSP_log2n, FFTRadix __vDSP_radix); |
| To | FFTSetupD create_fftsetupD ( vDSP_Length __vDSP_Log2n, FFTRadix __vDSP_Radix); |

Modified ctoz()

|  | Declaration |
| --- | --- |
| From | void ctoz ( const DSPComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, vDSP_Length __vDSP_size); |
| To | void ctoz ( const DSPComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, vDSP_Length __vDSP_N); |

Modified ctozD()

|  | Declaration |
| --- | --- |
| From | void ctozD ( const DSPDoubleComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, vDSP_Length __vDSP_size); |
| To | void ctozD ( const DSPDoubleComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, vDSP_Length __vDSP_N); |

Modified dotpr()

|  | Declaration |
| --- | --- |
| From | void dotpr ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void dotpr ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified dotprD()

|  | Declaration |
| --- | --- |
| From | void dotprD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void dotprD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified f3x3()

|  | Declaration |
| --- | --- |
| From | void f3x3 ( float \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, float \*__vDSP_filter, float \*__vDSP_result); |
| To | void f3x3 ( const float \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const float \*__vDSP_F, float \*__vDSP_C); |

Modified f3x3D()

|  | Declaration |
| --- | --- |
| From | void f3x3D ( double \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, double \*__vDSP_filter, double \*__vDSP_result); |
| To | void f3x3D ( const double \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const double \*__vDSP_F, double \*__vDSP_C); |

Modified f5x5()

|  | Declaration |
| --- | --- |
| From | void f5x5 ( float \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, float \*__vDSP_filter, float \*__vDSP_result); |
| To | void f5x5 ( const float \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const float \*__vDSP_F, float \*__vDSP_C); |

Modified f5x5D()

|  | Declaration |
| --- | --- |
| From | void f5x5D ( double \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, double \*__vDSP_filter, double \*__vDSP_result); |
| To | void f5x5D ( const double \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const double \*__vDSP_F, double \*__vDSP_C); |

Modified fft2d_zip()

|  | Declaration |
| --- | --- |
| From | void fft2d_zip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void fft2d_zip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zipD()

|  | Declaration |
| --- | --- |
| From | void fft2d_zipD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void fft2d_zipD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zipt()

|  | Declaration |
| --- | --- |
| From | void fft2d_zipt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void fft2d_zipt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC1, vDSP_Stride __vDSP_IC0, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_ziptD()

|  | Declaration |
| --- | --- |
| From | void fft2d_ziptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void fft2d_ziptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zop()

|  | Declaration |
| --- | --- |
| From | void fft2d_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void fft2d_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zopD()

|  | Declaration |
| --- | --- |
| From | void fft2d_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void fft2d_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zopt()

|  | Declaration |
| --- | --- |
| From | void fft2d_zopt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void fft2d_zopt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zoptD()

|  | Declaration |
| --- | --- |
| From | void fft2d_zoptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void fft2d_zoptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zrip()

|  | Declaration |
| --- | --- |
| From | void fft2d_zrip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void fft2d_zrip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zripD()

|  | Declaration |
| --- | --- |
| From | void fft2d_zripD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void fft2d_zripD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_flag); |

Modified fft2d_zript()

|  | Declaration |
| --- | --- |
| From | void fft2d_zript ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void fft2d_zript ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zriptD()

|  | Declaration |
| --- | --- |
| From | void fft2d_zriptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void fft2d_zriptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_flag); |

Modified fft2d_zrop()

|  | Declaration |
| --- | --- |
| From | void fft2d_zrop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void fft2d_zrop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zropD()

|  | Declaration |
| --- | --- |
| From | void fft2d_zropD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_Kr, vDSP_Stride __vDSP_Kc, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_Ir, vDSP_Stride __vDSP_Ic, vDSP_Length __vDSP_log2nc, vDSP_Length __vDSP_log2nr, FFTDirection __vDSP_flag); |
| To | void fft2d_zropD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zropt()

|  | Declaration |
| --- | --- |
| From | void fft2d_zropt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void fft2d_zropt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft2d_zroptD()

|  | Declaration |
| --- | --- |
| From | void fft2d_zroptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_Kr, vDSP_Stride __vDSP_Kc, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_Ir, vDSP_Stride __vDSP_Ic, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2nc, vDSP_Length __vDSP_log2nr, FFTDirection __vDSP_flag); |
| To | void fft2d_zroptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified fft3_zop()

|  | Declaration |
| --- | --- |
| From | void fft3_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void fft3_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft3_zopD()

|  | Declaration |
| --- | --- |
| From | void fft3_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_K, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void fft3_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft5_zop()

|  | Declaration |
| --- | --- |
| From | void fft5_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void fft5_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft5_zopD()

|  | Declaration |
| --- | --- |
| From | void fft5_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_K, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void fft5_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zip()

|  | Declaration |
| --- | --- |
| From | void fft_zip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zipD()

|  | Declaration |
| --- | --- |
| From | void fft_zipD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zipD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zipt()

|  | Declaration |
| --- | --- |
| From | void fft_zipt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zipt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_ziptD()

|  | Declaration |
| --- | --- |
| From | void fft_ziptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_ziptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zop()

|  | Declaration |
| --- | --- |
| From | void fft_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zopD()

|  | Declaration |
| --- | --- |
| From | void fft_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zopt()

|  | Declaration |
| --- | --- |
| From | void fft_zopt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zopt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zoptD()

|  | Declaration |
| --- | --- |
| From | void fft_zoptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zoptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zrip()

|  | Declaration |
| --- | --- |
| From | void fft_zrip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zrip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zripD()

|  | Declaration |
| --- | --- |
| From | void fft_zripD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void fft_zripD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zript()

|  | Declaration |
| --- | --- |
| From | void fft_zript ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zript ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zriptD()

|  | Declaration |
| --- | --- |
| From | void fft_zriptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void fft_zriptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zrop()

|  | Declaration |
| --- | --- |
| From | void fft_zrop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zrop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zropD()

|  | Declaration |
| --- | --- |
| From | void fft_zropD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void fft_zropD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zropt()

|  | Declaration |
| --- | --- |
| From | void fft_zropt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void fft_zropt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fft_zroptD()

|  | Declaration |
| --- | --- |
| From | void fft_zroptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void fft_zroptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified fftm_zip()

|  | Declaration |
| --- | --- |
| From | void fftm_zip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zipD()

|  | Declaration |
| --- | --- |
| From | void fftm_zipD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zipD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zipt()

|  | Declaration |
| --- | --- |
| From | void fftm_zipt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zipt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_ziptD()

|  | Declaration |
| --- | --- |
| From | void fftm_ziptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_ziptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zop()

|  | Declaration |
| --- | --- |
| From | void fftm_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zopD()

|  | Declaration |
| --- | --- |
| From | void fftm_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zopt()

|  | Declaration |
| --- | --- |
| From | void fftm_zopt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zopt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zoptD()

|  | Declaration |
| --- | --- |
| From | void fftm_zoptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zoptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zrip()

|  | Declaration |
| --- | --- |
| From | void fftm_zrip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zrip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zripD()

|  | Declaration |
| --- | --- |
| From | void fftm_zripD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zripD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zript()

|  | Declaration |
| --- | --- |
| From | void fftm_zript ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zript ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zriptD()

|  | Declaration |
| --- | --- |
| From | void fftm_zriptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zriptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zrop()

|  | Declaration |
| --- | --- |
| From | void fftm_zrop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zrop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zropD()

|  | Declaration |
| --- | --- |
| From | void fftm_zropD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zropD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zropt()

|  | Declaration |
| --- | --- |
| From | void fftm_zropt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zropt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified fftm_zroptD()

|  | Declaration |
| --- | --- |
| From | void fftm_zroptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void fftm_zroptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified imgfir()

|  | Declaration |
| --- | --- |
| From | void imgfir ( float \*__vDSP_signal, vDSP_Length __vDSP_numRow, vDSP_Length __vDSP_numCol, float \*__vDSP_filter, float \*__vDSP_result, vDSP_Length __vDSP_fnumRow, vDSP_Length __vDSP_fnumCol); |
| To | void imgfir ( const float \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const float \*__vDSP_F, float \*__vDSP_C, vDSP_Length __vDSP_P, vDSP_Length __vDSP_Q); |

Modified imgfirD()

|  | Declaration |
| --- | --- |
| From | void imgfirD ( double \*__vDSP_signal, vDSP_Length __vDSP_numRow, vDSP_Length __vDSP_numCol, double \*__vDSP_filter, double \*__vDSP_result, vDSP_Length __vDSP_fnumRow, vDSP_Length __vDSP_fnumCol); |
| To | void imgfirD ( const double \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const double \*__vDSP_F, double \*__vDSP_C, vDSP_Length __vDSP_P, vDSP_Length __vDSP_Q); |

Modified mmul()

|  | Declaration |
| --- | --- |
| From | void mmul ( float \*__vDSP_a, vDSP_Stride __vDSP_aStride, float \*__vDSP_b, vDSP_Stride __vDSP_bStride, float \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void mmul ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified mmulD()

|  | Declaration |
| --- | --- |
| From | void mmulD ( double \*__vDSP_a, vDSP_Stride __vDSP_aStride, double \*__vDSP_b, vDSP_Stride __vDSP_bStride, double \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void mmulD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified mtrans()

|  | Declaration |
| --- | --- |
| From | void mtrans ( float \*__vDSP_a, vDSP_Stride __vDSP_aStride, float \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |
| To | void mtrans ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |

Modified mtransD()

|  | Declaration |
| --- | --- |
| From | void mtransD ( double \*__vDSP_a, vDSP_Stride __vDSP_aStride, double \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |
| To | void mtransD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |

Modified [vDSP_blkman_window()](https://developer.apple.com/documentation/accelerate/1450190-vdsp_blkman_window)

|  | Declaration |
| --- | --- |
| From | void vDSP_blkman_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_blkman_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_blkman_windowD()](https://developer.apple.com/documentation/accelerate/1450471-vdsp_blkman_windowd)

|  | Declaration |
| --- | --- |
| From | void vDSP_blkman_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_blkman_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_conv()](https://developer.apple.com/documentation/kernel/1532184-vdsp_conv)

|  | Declaration |
| --- | --- |
| From | void vDSP_conv ( const float __vDSP_signal[], vDSP_Stride __vDSP_signalStride, const float __vDSP_filter[], vDSP_Stride __vDSP_strideFilter, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void vDSP_conv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_F, vDSP_Stride __vDSP_IF, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_convD()](https://developer.apple.com/documentation/accelerate/1450637-vdsp_convd)

|  | Declaration |
| --- | --- |
| From | void vDSP_convD ( const double __vDSP_signal[], vDSP_Stride __vDSP_signalStride, const double __vDSP_filter[], vDSP_Stride __vDSP_strideFilter, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void vDSP_convD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_F, vDSP_Stride __vDSP_IF, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_create_fftsetup()](https://developer.apple.com/documentation/kernel/1580009-vdsp_create_fftsetup)

|  | Declaration |
| --- | --- |
| From | FFTSetup vDSP_create_fftsetup ( vDSP_Length __vDSP_log2n, FFTRadix __vDSP_radix); |
| To | FFTSetup vDSP_create_fftsetup ( vDSP_Length __vDSP_Log2n, FFTRadix __vDSP_Radix); |

Modified [vDSP_create_fftsetupD()](https://developer.apple.com/documentation/accelerate/1449974-vdsp_create_fftsetupd)

|  | Declaration |
| --- | --- |
| From | FFTSetupD vDSP_create_fftsetupD ( vDSP_Length __vDSP_log2n, FFTRadix __vDSP_radix); |
| To | FFTSetupD vDSP_create_fftsetupD ( vDSP_Length __vDSP_Log2n, FFTRadix __vDSP_Radix); |

Modified [vDSP_ctoz()](https://developer.apple.com/documentation/kernel/1579975-vdsp_ctoz)

|  | Declaration |
| --- | --- |
| From | void vDSP_ctoz ( const DSPComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, vDSP_Length __vDSP_size); |
| To | void vDSP_ctoz ( const DSPComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, vDSP_Length __vDSP_N); |

Modified [vDSP_ctozD()](https://developer.apple.com/documentation/accelerate/1449970-vdsp_ctozd)

|  | Declaration |
| --- | --- |
| From | void vDSP_ctozD ( const DSPDoubleComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, vDSP_Length __vDSP_size); |
| To | void vDSP_ctozD ( const DSPDoubleComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, vDSP_Length __vDSP_N); |

Modified [vDSP_deq22()](https://developer.apple.com/documentation/kernel/1532225-vdsp_deq22)

|  | Declaration |
| --- | --- |
| From | void vDSP_deq22 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_deq22 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_deq22D()](https://developer.apple.com/documentation/accelerate/1450534-vdsp_deq22d)

|  | Declaration |
| --- | --- |
| From | void vDSP_deq22D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_deq22D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_desamp()](https://developer.apple.com/documentation/accelerate/1449946-vdsp_desamp)

|  | Declaration |
| --- | --- |
| From | void vDSP_desamp ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_desamp ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_F, float \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_desampD()](https://developer.apple.com/documentation/accelerate/1450133-vdsp_desampd)

|  | Declaration |
| --- | --- |
| From | void vDSP_desampD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_desampD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, const double \*__vDSP_F, double \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_distancesq()](https://developer.apple.com/documentation/accelerate/1450619-vdsp_distancesq)

|  | Declaration |
| --- | --- |
| From | void vDSP_distancesq ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_distancesq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_dotpr()](https://developer.apple.com/documentation/accelerate/1450313-vdsp_dotpr)

|  | Declaration |
| --- | --- |
| From | void vDSP_dotpr ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_dotpr ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_dotprD()](https://developer.apple.com/documentation/accelerate/1450330-vdsp_dotprd)

|  | Declaration |
| --- | --- |
| From | void vDSP_dotprD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_dotprD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_f3x3()](https://developer.apple.com/documentation/accelerate/1450690-vdsp_f3x3)

|  | Declaration |
| --- | --- |
| From | void vDSP_f3x3 ( float \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, float \*__vDSP_filter, float \*__vDSP_result); |
| To | void vDSP_f3x3 ( const float \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const float \*__vDSP_F, float \*__vDSP_C); |

Modified [vDSP_f3x3D()](https://developer.apple.com/documentation/accelerate/1450651-vdsp_f3x3d)

|  | Declaration |
| --- | --- |
| From | void vDSP_f3x3D ( double \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, double \*__vDSP_filter, double \*__vDSP_result); |
| To | void vDSP_f3x3D ( const double \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const double \*__vDSP_F, double \*__vDSP_C); |

Modified [vDSP_f5x5()](https://developer.apple.com/documentation/accelerate/1450036-vdsp_f5x5)

|  | Declaration |
| --- | --- |
| From | void vDSP_f5x5 ( float \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, float \*__vDSP_filter, float \*__vDSP_result); |
| To | void vDSP_f5x5 ( const float \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const float \*__vDSP_F, float \*__vDSP_C); |

Modified [vDSP_f5x5D()](https://developer.apple.com/documentation/accelerate/1449839-vdsp_f5x5d)

|  | Declaration |
| --- | --- |
| From | void vDSP_f5x5D ( double \*__vDSP_signal, vDSP_Length __vDSP_rows, vDSP_Length __vDSP_cols, double \*__vDSP_filter, double \*__vDSP_result); |
| To | void vDSP_f5x5D ( const double \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const double \*__vDSP_F, double \*__vDSP_C); |

Modified [vDSP_fft2d_zip()](https://developer.apple.com/documentation/accelerate/1450430-vdsp_fft2d_zip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_zip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zipD()](https://developer.apple.com/documentation/accelerate/1450508-vdsp_fft2d_zipd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zipD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_zipD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zipt()](https://developer.apple.com/documentation/accelerate/1450777-vdsp_fft2d_zipt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zipt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_zipt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC1, vDSP_Stride __vDSP_IC0, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_ziptD()](https://developer.apple.com/documentation/accelerate/1450202-vdsp_fft2d_ziptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_ziptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_ziptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zop()](https://developer.apple.com/documentation/accelerate/1450355-vdsp_fft2d_zop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zopD()](https://developer.apple.com/documentation/accelerate/1449944-vdsp_fft2d_zopd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zopt()](https://developer.apple.com/documentation/accelerate/1450816-vdsp_fft2d_zopt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zopt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zopt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zoptD()](https://developer.apple.com/documentation/accelerate/1449963-vdsp_fft2d_zoptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zoptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zoptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zrip()](https://developer.apple.com/documentation/accelerate/1450116-vdsp_fft2d_zrip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zrip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_zrip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zripD()](https://developer.apple.com/documentation/accelerate/1450384-vdsp_fft2d_zripd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zripD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zripD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_flag); |

Modified [vDSP_fft2d_zript()](https://developer.apple.com/documentation/accelerate/1450144-vdsp_fft2d_zript)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zript ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_direction); |
| To | void vDSP_fft2d_zript ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zriptD()](https://developer.apple.com/documentation/accelerate/1450079-vdsp_fft2d_zriptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zriptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_strideInRow, vDSP_Stride __vDSP_strideInCol, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zriptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_flag); |

Modified [vDSP_fft2d_zrop()](https://developer.apple.com/documentation/accelerate/1450361-vdsp_fft2d_zrop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zrop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zrop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zropD()](https://developer.apple.com/documentation/accelerate/1450732-vdsp_fft2d_zropd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zropD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_Kr, vDSP_Stride __vDSP_Kc, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_Ir, vDSP_Stride __vDSP_Ic, vDSP_Length __vDSP_log2nc, vDSP_Length __vDSP_log2nr, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zropD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zropt()](https://developer.apple.com/documentation/accelerate/1450460-vdsp_fft2d_zropt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zropt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStrideInRow, vDSP_Stride __vDSP_signalStrideInCol, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResultInRow, vDSP_Stride __vDSP_strideResultInCol, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2nInCol, vDSP_Length __vDSP_log2nInRow, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zropt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft2d_zroptD()](https://developer.apple.com/documentation/accelerate/1450433-vdsp_fft2d_zroptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft2d_zroptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_Kr, vDSP_Stride __vDSP_Kc, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_Ir, vDSP_Stride __vDSP_Ic, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2nc, vDSP_Length __vDSP_log2nr, FFTDirection __vDSP_flag); |
| To | void vDSP_fft2d_zroptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA0, vDSP_Stride __vDSP_IA1, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC0, vDSP_Stride __vDSP_IC1, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N0, vDSP_Length __vDSP_Log2N1, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft3_zop()](https://developer.apple.com/documentation/accelerate/1450494-vdsp_fft3_zop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft3_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft3_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft3_zopD()](https://developer.apple.com/documentation/accelerate/1450124-vdsp_fft3_zopd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft3_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_K, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft3_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft5_zop()](https://developer.apple.com/documentation/accelerate/1450044-vdsp_fft5_zop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft5_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft5_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft5_zopD()](https://developer.apple.com/documentation/accelerate/1450738-vdsp_fft5_zopd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft5_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_K, DSPDoubleSplitComplex \*__vDSP_ioData2, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft5_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zip()](https://developer.apple.com/documentation/accelerate/1450224-vdsp_fft_zip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zipD()](https://developer.apple.com/documentation/accelerate/1449916-vdsp_fft_zipd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zipD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zipD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zipt()](https://developer.apple.com/documentation/accelerate/1449879-vdsp_fft_zipt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zipt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zipt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_ziptD()](https://developer.apple.com/documentation/accelerate/1450852-vdsp_fft_ziptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_ziptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_ziptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zop()](https://developer.apple.com/documentation/accelerate/1450581-vdsp_fft_zop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zopD()](https://developer.apple.com/documentation/accelerate/1450694-vdsp_fft_zopd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zopt()](https://developer.apple.com/documentation/accelerate/1450812-vdsp_fft_zopt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zopt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zopt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zoptD()](https://developer.apple.com/documentation/accelerate/1450447-vdsp_fft_zoptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zoptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zoptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zrip()](https://developer.apple.com/documentation/kernel/1579997-vdsp_fft_zrip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zrip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zrip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zripD()](https://developer.apple.com/documentation/accelerate/1450371-vdsp_fft_zripd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zripD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft_zripD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zript()](https://developer.apple.com/documentation/accelerate/1450455-vdsp_fft_zript)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zript ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zript ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zriptD()](https://developer.apple.com/documentation/accelerate/1450486-vdsp_fft_zriptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zriptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_ioData, vDSP_Stride __vDSP_stride, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft_zriptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zrop()](https://developer.apple.com/documentation/accelerate/1449994-vdsp_fft_zrop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zrop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zrop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zropD()](https://developer.apple.com/documentation/accelerate/1449666-vdsp_fft_zropd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zropD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft_zropD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zropt()](https://developer.apple.com/documentation/accelerate/1450404-vdsp_fft_zropt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zropt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_direction); |
| To | void vDSP_fft_zropt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fft_zroptD()](https://developer.apple.com/documentation/accelerate/1450828-vdsp_fft_zroptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fft_zroptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, DSPDoubleSplitComplex \*__vDSP_bufferTemp, vDSP_Length __vDSP_log2n, FFTDirection __vDSP_flag); |
| To | void vDSP_fft_zroptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zip()](https://developer.apple.com/documentation/accelerate/1450798-vdsp_fftm_zip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zipD()](https://developer.apple.com/documentation/accelerate/1449959-vdsp_fftm_zipd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zipD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zipD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zipt()](https://developer.apple.com/documentation/accelerate/1449852-vdsp_fftm_zipt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zipt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zipt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_ziptD()](https://developer.apple.com/documentation/accelerate/1450092-vdsp_fftm_ziptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_ziptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_ziptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zop()](https://developer.apple.com/documentation/accelerate/1450053-vdsp_fftm_zop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zopD()](https://developer.apple.com/documentation/accelerate/1450439-vdsp_fftm_zopd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zopD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zopD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zopt()](https://developer.apple.com/documentation/accelerate/1449737-vdsp_fftm_zopt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zopt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zopt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zoptD()](https://developer.apple.com/documentation/accelerate/1450596-vdsp_fftm_zoptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zoptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zoptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zrip()](https://developer.apple.com/documentation/accelerate/1449883-vdsp_fftm_zrip)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zrip ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zrip ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zripD()](https://developer.apple.com/documentation/accelerate/1450075-vdsp_fftm_zripd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zripD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zripD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zript()](https://developer.apple.com/documentation/accelerate/1450050-vdsp_fftm_zript)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zript ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zript ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zriptD()](https://developer.apple.com/documentation/accelerate/1450514-vdsp_fftm_zriptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zriptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zriptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IM, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zrop()](https://developer.apple.com/documentation/accelerate/1450073-vdsp_fftm_zrop)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zrop ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zrop ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zropD()](https://developer.apple.com/documentation/accelerate/1449714-vdsp_fftm_zropd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zropD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zropD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zropt()](https://developer.apple.com/documentation/accelerate/1450659-vdsp_fftm_zropt)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zropt ( FFTSetup __vDSP_setup, DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zropt ( FFTSetup __vDSP_Setup, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_fftm_zroptD()](https://developer.apple.com/documentation/accelerate/1450320-vdsp_fftm_zroptd)

|  | Declaration |
| --- | --- |
| From | void vDSP_fftm_zroptD ( FFTSetupD __vDSP_setup, DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, vDSP_Stride __vDSP_fftStride, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_resultStride, vDSP_Stride __vDSP_rfftStride, DSPDoubleSplitComplex \*__vDSP_temp, vDSP_Length __vDSP_log2n, vDSP_Length __vDSP_numFFT, FFTDirection __vDSP_flag); |
| To | void vDSP_fftm_zroptD ( FFTSetupD __vDSP_Setup, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Stride __vDSP_IMA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Stride __vDSP_IMC, const DSPDoubleSplitComplex \*__vDSP_Buffer, vDSP_Length __vDSP_Log2N, vDSP_Length __vDSP_M, FFTDirection __vDSP_Direction); |

Modified [vDSP_hamm_window()](https://developer.apple.com/documentation/accelerate/1450040-vdsp_hamm_window)

|  | Declaration |
| --- | --- |
| From | void vDSP_hamm_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_hamm_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_hamm_windowD()](https://developer.apple.com/documentation/accelerate/1450721-vdsp_hamm_windowd)

|  | Declaration |
| --- | --- |
| From | void vDSP_hamm_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_hamm_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_hann_window()](https://developer.apple.com/documentation/accelerate/1450263-vdsp_hann_window)

|  | Declaration |
| --- | --- |
| From | void vDSP_hann_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_hann_window ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_hann_windowD()](https://developer.apple.com/documentation/accelerate/1450048-vdsp_hann_windowd)

|  | Declaration |
| --- | --- |
| From | void vDSP_hann_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_FLAG); |
| To | void vDSP_hann_windowD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Flag); |

Modified [vDSP_imgfir()](https://developer.apple.com/documentation/accelerate/1449856-vdsp_imgfir)

|  | Declaration |
| --- | --- |
| From | void vDSP_imgfir ( float \*__vDSP_signal, vDSP_Length __vDSP_numRow, vDSP_Length __vDSP_numCol, float \*__vDSP_filter, float \*__vDSP_result, vDSP_Length __vDSP_fnumRow, vDSP_Length __vDSP_fnumCol); |
| To | void vDSP_imgfir ( const float \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const float \*__vDSP_F, float \*__vDSP_C, vDSP_Length __vDSP_P, vDSP_Length __vDSP_Q); |

Modified [vDSP_imgfirD()](https://developer.apple.com/documentation/accelerate/1449818-vdsp_imgfird)

|  | Declaration |
| --- | --- |
| From | void vDSP_imgfirD ( double \*__vDSP_signal, vDSP_Length __vDSP_numRow, vDSP_Length __vDSP_numCol, double \*__vDSP_filter, double \*__vDSP_result, vDSP_Length __vDSP_fnumRow, vDSP_Length __vDSP_fnumCol); |
| To | void vDSP_imgfirD ( const double \*__vDSP_A, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_NC, const double \*__vDSP_F, double \*__vDSP_C, vDSP_Length __vDSP_P, vDSP_Length __vDSP_Q); |

Modified [vDSP_maxmgv()](https://developer.apple.com/documentation/kernel/1532187-vdsp_maxmgv)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxmgv ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_maxmgv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_maxmgvD()](https://developer.apple.com/documentation/accelerate/1450633-vdsp_maxmgvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxmgvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_maxmgvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_maxmgvi()](https://developer.apple.com/documentation/accelerate/1450576-vdsp_maxmgvi)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxmgvi ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_maxmgvi ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_maxmgviD()](https://developer.apple.com/documentation/accelerate/1450249-vdsp_maxmgvid)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxmgviD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_maxmgviD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_maxv()](https://developer.apple.com/documentation/kernel/1580003-vdsp_maxv)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_maxv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_maxvD()](https://developer.apple.com/documentation/accelerate/1449854-vdsp_maxvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_maxvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_maxvi()](https://developer.apple.com/documentation/accelerate/1450814-vdsp_maxvi)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxvi ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_maxvi ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_maxviD()](https://developer.apple.com/documentation/accelerate/1449682-vdsp_maxvid)

|  | Declaration |
| --- | --- |
| From | void vDSP_maxviD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_maxviD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_meamgv()](https://developer.apple.com/documentation/accelerate/1449731-vdsp_meamgv)

|  | Declaration |
| --- | --- |
| From | void vDSP_meamgv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_meamgv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_meamgvD()](https://developer.apple.com/documentation/accelerate/1450214-vdsp_meamgvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_meamgvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_meamgvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_meanv()](https://developer.apple.com/documentation/accelerate/1449980-vdsp_meanv)

|  | Declaration |
| --- | --- |
| From | void vDSP_meanv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_meanv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_meanvD()](https://developer.apple.com/documentation/accelerate/1449784-vdsp_meanvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_meanvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_meanvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_measqv()](https://developer.apple.com/documentation/accelerate/1450014-vdsp_measqv)

|  | Declaration |
| --- | --- |
| From | void vDSP_measqv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_measqv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_measqvD()](https://developer.apple.com/documentation/accelerate/1450463-vdsp_measqvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_measqvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_measqvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_minmgv()](https://developer.apple.com/documentation/accelerate/1449786-vdsp_minmgv)

|  | Declaration |
| --- | --- |
| From | void vDSP_minmgv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_minmgv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_minmgvD()](https://developer.apple.com/documentation/accelerate/1449830-vdsp_minmgvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_minmgvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_minmgvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_minmgvi()](https://developer.apple.com/documentation/accelerate/1449814-vdsp_minmgvi)

|  | Declaration |
| --- | --- |
| From | void vDSP_minmgvi ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_minmgvi ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_minmgviD()](https://developer.apple.com/documentation/accelerate/1450843-vdsp_minmgvid)

|  | Declaration |
| --- | --- |
| From | void vDSP_minmgviD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_minmgviD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_minv()](https://developer.apple.com/documentation/accelerate/1450267-vdsp_minv)

|  | Declaration |
| --- | --- |
| From | void vDSP_minv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_minv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_minvD()](https://developer.apple.com/documentation/accelerate/1450663-vdsp_minvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_minvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_minvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_minvi()](https://developer.apple.com/documentation/accelerate/1449875-vdsp_minvi)

|  | Declaration |
| --- | --- |
| From | void vDSP_minvi ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_minvi ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_minviD()](https://developer.apple.com/documentation/accelerate/1450441-vdsp_minvid)

|  | Declaration |
| --- | --- |
| From | void vDSP_minviD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length __vDSP_N); |
| To | void vDSP_minviD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length __vDSP_N); |

Modified [vDSP_mmov()](https://developer.apple.com/documentation/accelerate/1449950-vdsp_mmov)

|  | Declaration |
| --- | --- |
| From | void vDSP_mmov ( float \*__vDSP_A, float \*__vDSP_C, vDSP_Length __vDSP_NC, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_TCA, vDSP_Length __vDSP_TCC); |
| To | void vDSP_mmov ( const float \*__vDSP_A, float \*__vDSP_C, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_TA, vDSP_Length __vDSP_TC); |

Modified [vDSP_mmovD()](https://developer.apple.com/documentation/accelerate/1449956-vdsp_mmovd)

|  | Declaration |
| --- | --- |
| From | void vDSP_mmovD ( double \*__vDSP_A, double \*__vDSP_C, vDSP_Length __vDSP_NC, vDSP_Length __vDSP_NR, vDSP_Length __vDSP_TCA, vDSP_Length __vDSP_TCC); |
| To | void vDSP_mmovD ( const double \*__vDSP_A, double \*__vDSP_C, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_TA, vDSP_Length __vDSP_TC); |

Modified [vDSP_mmul()](https://developer.apple.com/documentation/accelerate/1449984-vdsp_mmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_mmul ( float \*__vDSP_a, vDSP_Stride __vDSP_aStride, float \*__vDSP_b, vDSP_Stride __vDSP_bStride, float \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_mmul ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_mmulD()](https://developer.apple.com/documentation/accelerate/1450386-vdsp_mmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_mmulD ( double \*__vDSP_a, vDSP_Stride __vDSP_aStride, double \*__vDSP_b, vDSP_Stride __vDSP_bStride, double \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_mmulD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_mtrans()](https://developer.apple.com/documentation/accelerate/1449988-vdsp_mtrans)

|  | Declaration |
| --- | --- |
| From | void vDSP_mtrans ( float \*__vDSP_a, vDSP_Stride __vDSP_aStride, float \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_mtrans ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |

Modified [vDSP_mtransD()](https://developer.apple.com/documentation/accelerate/1450422-vdsp_mtransd)

|  | Declaration |
| --- | --- |
| From | void vDSP_mtransD ( double \*__vDSP_a, vDSP_Stride __vDSP_aStride, double \*__vDSP_c, vDSP_Stride __vDSP_cStride, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_mtransD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N); |

Modified [vDSP_mvessq()](https://developer.apple.com/documentation/accelerate/1449849-vdsp_mvessq)

|  | Declaration |
| --- | --- |
| From | void vDSP_mvessq ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_mvessq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_mvessqD()](https://developer.apple.com/documentation/accelerate/1449753-vdsp_mvessqd)

|  | Declaration |
| --- | --- |
| From | void vDSP_mvessqD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_mvessqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_nzcros()](https://developer.apple.com/documentation/accelerate/1450629-vdsp_nzcros)

|  | Declaration |
| --- | --- |
| From | void vDSP_nzcros ( float \*__vDSP_A, vDSP_Stride __vDSP_I, vDSP_Length __vDSP_B, vDSP_Length \*__vDSP_C, vDSP_Length \*__vDSP_D, vDSP_Length __vDSP_N); |
| To | void vDSP_nzcros ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Length __vDSP_B, vDSP_Length \*__vDSP_C, vDSP_Length \*__vDSP_D, vDSP_Length __vDSP_N); |

Modified [vDSP_nzcrosD()](https://developer.apple.com/documentation/accelerate/1450715-vdsp_nzcrosd)

|  | Declaration |
| --- | --- |
| From | void vDSP_nzcrosD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, vDSP_Length __vDSP_B, vDSP_Length \*__vDSP_C, vDSP_Length \*__vDSP_D, vDSP_Length __vDSP_N); |
| To | void vDSP_nzcrosD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, vDSP_Length __vDSP_B, vDSP_Length \*__vDSP_C, vDSP_Length \*__vDSP_D, vDSP_Length __vDSP_N); |

Modified [vDSP_polar()](https://developer.apple.com/documentation/accelerate/1450489-vdsp_polar)

|  | Declaration |
| --- | --- |
| From | void vDSP_polar ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_polar ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_polarD()](https://developer.apple.com/documentation/accelerate/1450540-vdsp_polard)

|  | Declaration |
| --- | --- |
| From | void vDSP_polarD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_polarD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_rect()](https://developer.apple.com/documentation/accelerate/1450416-vdsp_rect)

|  | Declaration |
| --- | --- |
| From | void vDSP_rect ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_rect ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_rectD()](https://developer.apple.com/documentation/accelerate/1450754-vdsp_rectd)

|  | Declaration |
| --- | --- |
| From | void vDSP_rectD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_rectD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_rmsqv()](https://developer.apple.com/documentation/accelerate/1450655-vdsp_rmsqv)

|  | Declaration |
| --- | --- |
| From | void vDSP_rmsqv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_rmsqv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_rmsqvD()](https://developer.apple.com/documentation/accelerate/1449917-vdsp_rmsqvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_rmsqvD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_rmsqvD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svdiv()](https://developer.apple.com/documentation/accelerate/1450412-vdsp_svdiv)

|  | Declaration |
| --- | --- |
| From | void vDSP_svdiv ( float \*__vDSP_A, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_svdiv ( const float \*__vDSP_A, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_svdivD()](https://developer.apple.com/documentation/accelerate/1450028-vdsp_svdivd)

|  | Declaration |
| --- | --- |
| From | void vDSP_svdivD ( double \*__vDSP_A, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_svdivD ( const double \*__vDSP_A, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_sve()](https://developer.apple.com/documentation/kernel/1579937-vdsp_sve)

|  | Declaration |
| --- | --- |
| From | void vDSP_sve ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_sve ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_sveD()](https://developer.apple.com/documentation/accelerate/1450567-vdsp_sved)

|  | Declaration |
| --- | --- |
| From | void vDSP_sveD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_sveD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_sve_svesq()](https://developer.apple.com/documentation/kernel/1579989-vdsp_sve_svesq)

|  | Declaration |
| --- | --- |
| From | void vDSP_sve_svesq ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_Sum, float \*__vDSP_SumOfSquares, vDSP_Length __vDSP_N); |
| To | void vDSP_sve_svesq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_Sum, float \*__vDSP_SumOfSquares, vDSP_Length __vDSP_N); |

Modified [vDSP_sve_svesqD()](https://developer.apple.com/documentation/accelerate/1450682-vdsp_sve_svesqd)

|  | Declaration |
| --- | --- |
| From | void vDSP_sve_svesqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_Sum, double \*__vDSP_SumOfSquares, vDSP_Length __vDSP_N); |
| To | void vDSP_sve_svesqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_Sum, double \*__vDSP_SumOfSquares, vDSP_Length __vDSP_N); |

Modified [vDSP_svemg()](https://developer.apple.com/documentation/accelerate/1450055-vdsp_svemg)

|  | Declaration |
| --- | --- |
| From | void vDSP_svemg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svemg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svemgD()](https://developer.apple.com/documentation/accelerate/1450856-vdsp_svemgd)

|  | Declaration |
| --- | --- |
| From | void vDSP_svemgD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svemgD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svesq()](https://developer.apple.com/documentation/accelerate/1450392-vdsp_svesq)

|  | Declaration |
| --- | --- |
| From | void vDSP_svesq ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svesq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svesqD()](https://developer.apple.com/documentation/accelerate/1450012-vdsp_svesqd)

|  | Declaration |
| --- | --- |
| From | void vDSP_svesqD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svesqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svs()](https://developer.apple.com/documentation/kernel/1532174-vdsp_svs)

|  | Declaration |
| --- | --- |
| From | void vDSP_svs ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svs ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_svsD()](https://developer.apple.com/documentation/accelerate/1450862-vdsp_svsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_svsD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_svsD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_vaam()](https://developer.apple.com/documentation/accelerate/1450588-vdsp_vaam)

|  | Declaration |
| --- | --- |
| From | void vDSP_vaam ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vaam ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vaamD()](https://developer.apple.com/documentation/accelerate/1450148-vdsp_vaamd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vaamD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vaamD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vabs()](https://developer.apple.com/documentation/kernel/1532216-vdsp_vabs)

|  | Declaration |
| --- | --- |
| From | void vDSP_vabs ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vabs ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vabsD()](https://developer.apple.com/documentation/accelerate/1449982-vdsp_vabsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vabsD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vabsD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vabsi()](https://developer.apple.com/documentation/accelerate/1449929-vdsp_vabsi)

|  | Declaration |
| --- | --- |
| From | void vDSP_vabsi ( int \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vabsi ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vadd()](https://developer.apple.com/documentation/kernel/1532191-vdsp_vadd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vadd ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vadd ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vaddD()](https://developer.apple.com/documentation/accelerate/1449910-vdsp_vaddd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vaddD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vaddD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vam()](https://developer.apple.com/documentation/accelerate/1450561-vdsp_vam)

|  | Declaration |
| --- | --- |
| From | void vDSP_vam ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, const float __vDSP_input3[], vDSP_Stride __vDSP_stride3, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vam ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vamD()](https://developer.apple.com/documentation/accelerate/1450382-vdsp_vamd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vamD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, const double __vDSP_input3[], vDSP_Stride __vDSP_stride3, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vamD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_IDD, vDSP_Length __vDSP_N); |

Modified [vDSP_vasbm()](https://developer.apple.com/documentation/accelerate/1450277-vdsp_vasbm)

|  | Declaration |
| --- | --- |
| From | void vDSP_vasbm ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vasbm ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vasbmD()](https://developer.apple.com/documentation/accelerate/1449885-vdsp_vasbmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vasbmD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vasbmD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vasm()](https://developer.apple.com/documentation/accelerate/1449773-vdsp_vasm)

|  | Declaration |
| --- | --- |
| From | void vDSP_vasm ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vasm ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vasmD()](https://developer.apple.com/documentation/accelerate/1450146-vdsp_vasmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vasmD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vasmD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vavlin()](https://developer.apple.com/documentation/accelerate/1449668-vdsp_vavlin)

|  | Declaration |
| --- | --- |
| From | void vDSP_vavlin ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vavlin ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vavlinD()](https://developer.apple.com/documentation/accelerate/1450158-vdsp_vavlind)

|  | Declaration |
| --- | --- |
| From | void vDSP_vavlinD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vavlinD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vclip()](https://developer.apple.com/documentation/accelerate/1450071-vdsp_vclip)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclip ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vclip ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vclipD()](https://developer.apple.com/documentation/accelerate/1450285-vdsp_vclipd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclipD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vclipD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vclipc()](https://developer.apple.com/documentation/accelerate/1450775-vdsp_vclipc)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclipc ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N, vDSP_Length \*__vDSP_NLOW, vDSP_Length \*__vDSP_NHI); |
| To | void vDSP_vclipc ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N, vDSP_Length \*__vDSP_NLow, vDSP_Length \*__vDSP_NHigh); |

Modified [vDSP_vclipcD()](https://developer.apple.com/documentation/accelerate/1450162-vdsp_vclipcd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclipcD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N, vDSP_Length \*__vDSP_NLOW, vDSP_Length \*__vDSP_NHI); |
| To | void vDSP_vclipcD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N, vDSP_Length \*__vDSP_NLow, vDSP_Length \*__vDSP_NHigh); |

Modified [vDSP_vclr()](https://developer.apple.com/documentation/accelerate/1450402-vdsp_vclr)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclr ( float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vclr ( float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vclrD()](https://developer.apple.com/documentation/accelerate/1450639-vdsp_vclrd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vclrD ( double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vclrD ( double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vcmprs()](https://developer.apple.com/documentation/accelerate/1450286-vdsp_vcmprs)

|  | Declaration |
| --- | --- |
| From | void vDSP_vcmprs ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vcmprs ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vcmprsD()](https://developer.apple.com/documentation/accelerate/1449861-vdsp_vcmprsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vcmprsD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vcmprsD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vdbcon()](https://developer.apple.com/documentation/accelerate/1450241-vdsp_vdbcon)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdbcon ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, unsigned int __vDSP_F); |
| To | void vDSP_vdbcon ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, unsigned int __vDSP_F); |

Modified [vDSP_vdbconD()](https://developer.apple.com/documentation/accelerate/1449896-vdsp_vdbcond)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdbconD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, unsigned int __vDSP_F); |
| To | void vDSP_vdbconD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, unsigned int __vDSP_F); |

Modified [vDSP_vdist()](https://developer.apple.com/documentation/accelerate/1450257-vdsp_vdist)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdist ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdist ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |

Modified [vDSP_vdistD()](https://developer.apple.com/documentation/accelerate/1449966-vdsp_vdistd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdistD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdistD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, const double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |

Modified [vDSP_vdiv()](https://developer.apple.com/documentation/accelerate/1450243-vdsp_vdiv)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdiv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdiv ( const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vdivD()](https://developer.apple.com/documentation/accelerate/1450126-vdsp_vdivd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdivD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdivD ( const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vdivi()](https://developer.apple.com/documentation/accelerate/1450839-vdsp_vdivi)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdivi ( int \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_B, vDSP_Stride __vDSP_J, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdivi ( const int \*__vDSP_B, vDSP_Stride __vDSP_IB, const int \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vdpsp()](https://developer.apple.com/documentation/accelerate/1450729-vdsp_vdpsp)

|  | Declaration |
| --- | --- |
| From | void vDSP_vdpsp ( double \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vdpsp ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_venvlp()](https://developer.apple.com/documentation/accelerate/1449964-vdsp_venvlp)

|  | Declaration |
| --- | --- |
| From | void vDSP_venvlp ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_venvlp ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_venvlpD()](https://developer.apple.com/documentation/accelerate/1449687-vdsp_venvlpd)

|  | Declaration |
| --- | --- |
| From | void vDSP_venvlpD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_venvlpD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_veqvi()](https://developer.apple.com/documentation/accelerate/1450585-vdsp_veqvi)

|  | Declaration |
| --- | --- |
| From | void vDSP_veqvi ( int \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_B, vDSP_Stride __vDSP_J, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_veqvi ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, const int \*__vDSP_B, vDSP_Stride __vDSP_IB, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfill()](https://developer.apple.com/documentation/kernel/1579967-vdsp_vfill)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfill ( float \*__vDSP_A, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfill ( const float \*__vDSP_A, float \*__vDSP_C, vDSP_Stride __vDSP_IA, vDSP_Length __vDSP_N); |

Modified [vDSP_vfillD()](https://developer.apple.com/documentation/accelerate/1450171-vdsp_vfilld)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfillD ( double \*__vDSP_A, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfillD ( const double \*__vDSP_A, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfilli()](https://developer.apple.com/documentation/accelerate/1450473-vdsp_vfilli)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfilli ( int \*__vDSP_A, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfilli ( const int \*__vDSP_A, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix16()](https://developer.apple.com/documentation/accelerate/1449992-vdsp_vfix16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix16 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix16 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix16D()](https://developer.apple.com/documentation/accelerate/1450469-vdsp_vfix16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix16D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix16D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix32()](https://developer.apple.com/documentation/accelerate/1449976-vdsp_vfix32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix32 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix32 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix32D()](https://developer.apple.com/documentation/accelerate/1450167-vdsp_vfix32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix32D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix32D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix8()](https://developer.apple.com/documentation/accelerate/1450548-vdsp_vfix8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix8 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix8 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfix8D()](https://developer.apple.com/documentation/accelerate/1450864-vdsp_vfix8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfix8D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfix8D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr16()](https://developer.apple.com/documentation/accelerate/1449925-vdsp_vfixr16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr16 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr16 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr16D()](https://developer.apple.com/documentation/accelerate/1450475-vdsp_vfixr16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr16D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr16D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr32()](https://developer.apple.com/documentation/accelerate/1450794-vdsp_vfixr32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr32 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr32 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr32D()](https://developer.apple.com/documentation/accelerate/1450765-vdsp_vfixr32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr32D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr32D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr8()](https://developer.apple.com/documentation/accelerate/1450408-vdsp_vfixr8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr8 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr8 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixr8D()](https://developer.apple.com/documentation/accelerate/1449927-vdsp_vfixr8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixr8D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixr8D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru16()](https://developer.apple.com/documentation/accelerate/1450599-vdsp_vfixru16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru16 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru16 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru16D()](https://developer.apple.com/documentation/accelerate/1450082-vdsp_vfixru16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru16D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru16D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru32()](https://developer.apple.com/documentation/accelerate/1449735-vdsp_vfixru32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru32 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru32 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru32D()](https://developer.apple.com/documentation/accelerate/1450065-vdsp_vfixru32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru32D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru32D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru8()](https://developer.apple.com/documentation/accelerate/1449777-vdsp_vfixru8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru8 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru8 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixru8D()](https://developer.apple.com/documentation/accelerate/1449847-vdsp_vfixru8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixru8D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixru8D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu16()](https://developer.apple.com/documentation/accelerate/1449834-vdsp_vfixu16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu16 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu16 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu16D()](https://developer.apple.com/documentation/accelerate/1449908-vdsp_vfixu16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu16D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu16D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned short \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu32()](https://developer.apple.com/documentation/accelerate/1450173-vdsp_vfixu32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu32 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu32 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu32D()](https://developer.apple.com/documentation/accelerate/1450846-vdsp_vfixu32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu32D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu32D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu8()](https://developer.apple.com/documentation/accelerate/1450800-vdsp_vfixu8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu8 ( float \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu8 ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfixu8D()](https://developer.apple.com/documentation/accelerate/1450868-vdsp_vfixu8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfixu8D ( double \*__vDSP_A, vDSP_Stride __vDSP_I, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfixu8D ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, unsigned char \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt16()](https://developer.apple.com/documentation/accelerate/1450096-vdsp_vflt16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt16 ( short \*A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt16 ( const short \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt16D()](https://developer.apple.com/documentation/accelerate/1450208-vdsp_vflt16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt16D ( short \*A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt16D ( const short \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt32()](https://developer.apple.com/documentation/kernel/1532181-vdsp_vflt32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt32 ( int \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt32 ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt32D()](https://developer.apple.com/documentation/accelerate/1450342-vdsp_vflt32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt32D ( int \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt32D ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt8()](https://developer.apple.com/documentation/accelerate/1450742-vdsp_vflt8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt8 ( char \*A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt8 ( const char \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vflt8D()](https://developer.apple.com/documentation/accelerate/1449894-vdsp_vflt8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vflt8D ( char \*A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vflt8D ( const char \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu16()](https://developer.apple.com/documentation/accelerate/1450118-vdsp_vfltu16)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu16 ( unsigned short \*A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu16 ( const unsigned short \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu16D()](https://developer.apple.com/documentation/accelerate/1450769-vdsp_vfltu16d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu16D ( unsigned short \*A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu16D ( const unsigned short \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu32()](https://developer.apple.com/documentation/accelerate/1450255-vdsp_vfltu32)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu32 ( unsigned int \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu32 ( const unsigned int \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu32D()](https://developer.apple.com/documentation/accelerate/1449794-vdsp_vfltu32d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu32D ( unsigned int \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu32D ( const unsigned int \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu8()](https://developer.apple.com/documentation/accelerate/1450549-vdsp_vfltu8)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu8 ( unsigned char \*A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu8 ( const unsigned char \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfltu8D()](https://developer.apple.com/documentation/accelerate/1450104-vdsp_vfltu8d)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfltu8D ( unsigned char \*A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfltu8D ( const unsigned char \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfrac()](https://developer.apple.com/documentation/accelerate/1450336-vdsp_vfrac)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfrac ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfrac ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vfracD()](https://developer.apple.com/documentation/accelerate/1449948-vdsp_vfracd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vfracD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vfracD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgathr()](https://developer.apple.com/documentation/accelerate/1449749-vdsp_vgathr)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgathr ( float \*__vDSP_A, vDSP_Length \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgathr ( const float \*__vDSP_A, const vDSP_Length \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgathrD()](https://developer.apple.com/documentation/accelerate/1449921-vdsp_vgathrd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgathrD ( double \*__vDSP_A, vDSP_Length \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgathrD ( const double \*__vDSP_A, const vDSP_Length \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgathra()](https://developer.apple.com/documentation/accelerate/1450261-vdsp_vgathra)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgathra ( float \*\*A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgathra ( const float \*\*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgathraD()](https://developer.apple.com/documentation/accelerate/1449865-vdsp_vgathrad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgathraD ( double \*\*A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgathraD ( const double \*\*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgen()](https://developer.apple.com/documentation/accelerate/1449703-vdsp_vgen)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgen ( float \*__vDSP_A, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgen ( const float \*__vDSP_A, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgenD()](https://developer.apple.com/documentation/accelerate/1450583-vdsp_vgend)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgenD ( double \*__vDSP_A, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vgenD ( const double \*__vDSP_A, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vgenp()](https://developer.apple.com/documentation/accelerate/1449771-vdsp_vgenp)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgenp ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vgenp ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_vgenpD()](https://developer.apple.com/documentation/accelerate/1450645-vdsp_vgenpd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vgenpD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vgenpD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_viclip()](https://developer.apple.com/documentation/accelerate/1450512-vdsp_viclip)

|  | Declaration |
| --- | --- |
| From | void vDSP_viclip ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_viclip ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_viclipD()](https://developer.apple.com/documentation/accelerate/1450559-vdsp_viclipd)

|  | Declaration |
| --- | --- |
| From | void vDSP_viclipD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_viclipD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vindex()](https://developer.apple.com/documentation/accelerate/1449792-vdsp_vindex)

|  | Declaration |
| --- | --- |
| From | void vDSP_vindex ( float \*__vDSP_A, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vindex ( const float \*__vDSP_A, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vindexD()](https://developer.apple.com/documentation/accelerate/1449958-vdsp_vindexd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vindexD ( double \*__vDSP_A, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vindexD ( const double \*__vDSP_A, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vintb()](https://developer.apple.com/documentation/accelerate/1449705-vdsp_vintb)

|  | Declaration |
| --- | --- |
| From | void vDSP_vintb ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vintb ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vintbD()](https://developer.apple.com/documentation/accelerate/1449968-vdsp_vintbd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vintbD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vintbD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vlim()](https://developer.apple.com/documentation/accelerate/1450525-vdsp_vlim)

|  | Declaration |
| --- | --- |
| From | void vDSP_vlim ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vlim ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vlimD()](https://developer.apple.com/documentation/accelerate/1450709-vdsp_vlimd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vlimD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vlimD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vlint()](https://developer.apple.com/documentation/accelerate/1449775-vdsp_vlint)

|  | Declaration |
| --- | --- |
| From | void vDSP_vlint ( float \*__vDSP_A, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vlint ( const float \*__vDSP_A, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_vlintD()](https://developer.apple.com/documentation/accelerate/1449733-vdsp_vlintd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vlintD ( double \*__vDSP_A, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vlintD ( const double \*__vDSP_A, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_vma()](https://developer.apple.com/documentation/kernel/1532193-vdsp_vma)

|  | Declaration |
| --- | --- |
| From | void vDSP_vma ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vma ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmaD()](https://developer.apple.com/documentation/accelerate/1450825-vdsp_vmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmaD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vmaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmax()](https://developer.apple.com/documentation/kernel/1579953-vdsp_vmax)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmax ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmax ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmaxD()](https://developer.apple.com/documentation/accelerate/1449938-vdsp_vmaxd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmaxD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmaxD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmaxmg()](https://developer.apple.com/documentation/accelerate/1450295-vdsp_vmaxmg)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmaxmg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmaxmg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmaxmgD()](https://developer.apple.com/documentation/accelerate/1449767-vdsp_vmaxmgd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmaxmgD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmaxmgD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmin()](https://developer.apple.com/documentation/accelerate/1450216-vdsp_vmin)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmin ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vmin ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vminD()](https://developer.apple.com/documentation/accelerate/1450601-vdsp_vmind)

|  | Declaration |
| --- | --- |
| From | void vDSP_vminD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vminD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vminmg()](https://developer.apple.com/documentation/accelerate/1450293-vdsp_vminmg)

|  | Declaration |
| --- | --- |
| From | void vDSP_vminmg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vminmg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vminmgD()](https://developer.apple.com/documentation/accelerate/1449680-vdsp_vminmgd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vminmgD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vminmgD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmma()](https://developer.apple.com/documentation/accelerate/1450802-vdsp_vmma)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmma ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vmma ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vmmaD()](https://developer.apple.com/documentation/accelerate/1450527-vdsp_vmmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmmaD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vmmaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vmmsb()](https://developer.apple.com/documentation/accelerate/1450613-vdsp_vmmsb)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmmsb ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vmmsb ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vmmsbD()](https://developer.apple.com/documentation/accelerate/1450418-vdsp_vmmsbd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmmsbD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vmmsbD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vmsa()](https://developer.apple.com/documentation/accelerate/1450590-vdsp_vmsa)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmsa ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vmsa ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmsaD()](https://developer.apple.com/documentation/accelerate/1450698-vdsp_vmsad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmsaD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vmsaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmsb()](https://developer.apple.com/documentation/accelerate/1450451-vdsp_vmsb)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmsb ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vmsb ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmsbD()](https://developer.apple.com/documentation/accelerate/1450609-vdsp_vmsbd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmsbD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vmsbD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vmul()](https://developer.apple.com/documentation/accelerate/1450344-vdsp_vmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmul ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vmul ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vmulD()](https://developer.apple.com/documentation/accelerate/1450138-vdsp_vmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_vmulD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vmulD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vnabs()](https://developer.apple.com/documentation/accelerate/1450420-vdsp_vnabs)

|  | Declaration |
| --- | --- |
| From | void vDSP_vnabs ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vnabs ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vnabsD()](https://developer.apple.com/documentation/accelerate/1450259-vdsp_vnabsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vnabsD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vnabsD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vneg()](https://developer.apple.com/documentation/accelerate/1450204-vdsp_vneg)

|  | Declaration |
| --- | --- |
| From | void vDSP_vneg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vneg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vnegD()](https://developer.apple.com/documentation/accelerate/1450346-vdsp_vnegd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vnegD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vnegD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vpoly()](https://developer.apple.com/documentation/accelerate/1450623-vdsp_vpoly)

|  | Declaration |
| --- | --- |
| From | void vDSP_vpoly ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_vpoly ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_vpolyD()](https://developer.apple.com/documentation/accelerate/1450503-vdsp_vpolyd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vpolyD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_vpolyD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_vpythg()](https://developer.apple.com/documentation/accelerate/1450824-vdsp_vpythg)

|  | Declaration |
| --- | --- |
| From | void vDSP_vpythg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vpythg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vpythgD()](https://developer.apple.com/documentation/accelerate/1449766-vdsp_vpythgd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vpythgD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vpythgD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vqint()](https://developer.apple.com/documentation/accelerate/1449942-vdsp_vqint)

|  | Declaration |
| --- | --- |
| From | void vDSP_vqint ( float \*__vDSP_A, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vqint ( const float \*__vDSP_A, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_vqintD()](https://developer.apple.com/documentation/accelerate/1450491-vdsp_vqintd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vqintD ( double \*__vDSP_A, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_vqintD ( const double \*__vDSP_A, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |

Modified [vDSP_vramp()](https://developer.apple.com/documentation/accelerate/1450369-vdsp_vramp)

|  | Declaration |
| --- | --- |
| From | void vDSP_vramp ( float \*__vDSP_A, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vramp ( const float \*__vDSP_A, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vrampD()](https://developer.apple.com/documentation/accelerate/1449999-vdsp_vrampd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vrampD ( double \*__vDSP_A, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vrampD ( const double \*__vDSP_A, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vrsum()](https://developer.apple.com/documentation/accelerate/1450245-vdsp_vrsum)

|  | Declaration |
| --- | --- |
| From | void vDSP_vrsum ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_S, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vrsum ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_S, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vrsumD()](https://developer.apple.com/documentation/accelerate/1450713-vdsp_vrsumd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vrsumD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_S, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vrsumD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_S, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vrvrs()](https://developer.apple.com/documentation/accelerate/1450290-vdsp_vrvrs)

|  | Declaration |
| --- | --- |
| From | void vDSP_vrvrs ( float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vrvrs ( float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vrvrsD()](https://developer.apple.com/documentation/accelerate/1449825-vdsp_vrvrsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vrvrsD ( double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vrvrsD ( double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsadd()](https://developer.apple.com/documentation/kernel/1579993-vdsp_vsadd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsadd ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsadd ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsaddD()](https://developer.apple.com/documentation/accelerate/1450860-vdsp_vsaddd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsaddD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsaddD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsaddi()](https://developer.apple.com/documentation/accelerate/1450088-vdsp_vsaddi)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsaddi ( int \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_B, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsaddi ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, const int \*__vDSP_B, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbm()](https://developer.apple.com/documentation/accelerate/1449914-vdsp_vsbm)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbm ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbm ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbmD()](https://developer.apple.com/documentation/accelerate/1450334-vdsp_vsbmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbmD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbmD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbsbm()](https://developer.apple.com/documentation/accelerate/1449761-vdsp_vsbsbm)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbsbm ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, float \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbsbm ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, const float \*__vDSP_D, vDSP_Stride __vDSP_ID, float \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbsbmD()](https://developer.apple.com/documentation/accelerate/1449707-vdsp_vsbsbmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbsbmD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, double \*__vDSP_E, vDSP_Stride __vDSP_M, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbsbmD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, const double \*__vDSP_D, vDSP_Stride __vDSP_ID, double \*__vDSP_E, vDSP_Stride __vDSP_IE, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbsm()](https://developer.apple.com/documentation/accelerate/1450734-vdsp_vsbsm)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbsm ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbsm ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsbsmD()](https://developer.apple.com/documentation/accelerate/1450372-vdsp_vsbsmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsbsmD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsbsmD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsdiv()](https://developer.apple.com/documentation/accelerate/1450680-vdsp_vsdiv)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsdiv ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsdiv ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsdivD()](https://developer.apple.com/documentation/accelerate/1450212-vdsp_vsdivd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsdivD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsdivD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsdivi()](https://developer.apple.com/documentation/accelerate/1449689-vdsp_vsdivi)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsdivi ( int \*__vDSP_A, vDSP_Stride __vDSP_I, int \*__vDSP_B, int \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsdivi ( const int \*__vDSP_A, vDSP_Stride __vDSP_IA, const int \*__vDSP_B, int \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsimps()](https://developer.apple.com/documentation/accelerate/1450644-vdsp_vsimps)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsimps ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsimps ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsimpsD()](https://developer.apple.com/documentation/accelerate/1450112-vdsp_vsimpsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsimpsD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vsimpsD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsma()](https://developer.apple.com/documentation/accelerate/1450271-vdsp_vsma)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsma ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, const float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsma ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmaD()](https://developer.apple.com/documentation/accelerate/1449759-vdsp_vsmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, const double \*__vDSP_B, const double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmsa()](https://developer.apple.com/documentation/accelerate/1450380-vdsp_vsmsa)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmsa ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmsa ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmsaD()](https://developer.apple.com/documentation/accelerate/1450432-vdsp_vsmsad)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmsaD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmsaD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_ID, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmsb()](https://developer.apple.com/documentation/accelerate/1450822-vdsp_vsmsb)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmsb ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmsb ( const float \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_B, const float \*__vDSP_C, vDSP_Stride __vDSP_K, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmsbD()](https://developer.apple.com/documentation/accelerate/1450238-vdsp_vsmsbd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmsbD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vsmsbD ( const double \*__vDSP_A, vDSP_Stride __vDSP_I, const double \*__vDSP_B, const double \*__vDSP_C, vDSP_Stride __vDSP_K, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmul()](https://developer.apple.com/documentation/kernel/1532223-vdsp_vsmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmul ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float \*__vDSP_input2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsmul ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsmulD()](https://developer.apple.com/documentation/accelerate/1449676-vdsp_vsmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsmulD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double \*__vDSP_input2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsmulD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsort()](https://developer.apple.com/documentation/accelerate/1449747-vdsp_vsort)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsort ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_OFLAG); |
| To | void vDSP_vsort ( float \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Order); |

Modified [vDSP_vsortD()](https://developer.apple.com/documentation/accelerate/1450482-vdsp_vsortd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsortD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_OFLAG); |
| To | void vDSP_vsortD ( double \*__vDSP_C, vDSP_Length __vDSP_N, int __vDSP_Order); |

Modified [vDSP_vsorti()](https://developer.apple.com/documentation/accelerate/1450736-vdsp_vsorti)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsorti ( float \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length \*__vDSP_List_addr, vDSP_Length __vDSP_N, int __vDSP_OFLAG); |
| To | void vDSP_vsorti ( const float \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length \*__vDSP_Temporary, vDSP_Length __vDSP_N, int __vDSP_Order); |

Modified [vDSP_vsortiD()](https://developer.apple.com/documentation/accelerate/1450858-vdsp_vsortid)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsortiD ( double \*__vDSP_C, vDSP_Length \*__vDSP_IC, vDSP_Length \*__vDSP_List_addr, vDSP_Length __vDSP_N, int __vDSP_OFLAG); |
| To | void vDSP_vsortiD ( const double \*__vDSP_C, vDSP_Length \*__vDSP_I, vDSP_Length \*__vDSP_Temporary, vDSP_Length __vDSP_N, int __vDSP_Order); |

Modified [vDSP_vspdp()](https://developer.apple.com/documentation/accelerate/1450265-vdsp_vspdp)

|  | Declaration |
| --- | --- |
| From | void vDSP_vspdp ( float \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vspdp ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsq()](https://developer.apple.com/documentation/accelerate/1450611-vdsp_vsq)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsq ( const float __vDSP_input[], vDSP_Stride __vDSP_strideInput, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsqD()](https://developer.apple.com/documentation/accelerate/1450841-vdsp_vsqd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsqD ( const double __vDSP_input[], vDSP_Stride __vDSP_strideInput, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vssq()](https://developer.apple.com/documentation/accelerate/1450445-vdsp_vssq)

|  | Declaration |
| --- | --- |
| From | void vDSP_vssq ( const float __vDSP_input[], vDSP_Stride __vDSP_strideInput, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vssq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vssqD()](https://developer.apple.com/documentation/accelerate/1450363-vdsp_vssqd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vssqD ( const double __vDSP_input[], vDSP_Stride __vDSP_strideInput, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vssqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsub()](https://developer.apple.com/documentation/accelerate/1449900-vdsp_vsub)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsub ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsub ( const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vsubD()](https://developer.apple.com/documentation/accelerate/1449743-vdsp_vsubd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vsubD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_vsubD ( const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vswap()](https://developer.apple.com/documentation/accelerate/1450661-vdsp_vswap)

|  | Declaration |
| --- | --- |
| From | void vDSP_vswap ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, vDSP_Length __vDSP_N); |
| To | void vDSP_vswap ( float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_B, vDSP_Stride __vDSP_IB, vDSP_Length __vDSP_N); |

Modified [vDSP_vswapD()](https://developer.apple.com/documentation/accelerate/1450555-vdsp_vswapd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vswapD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, vDSP_Length __vDSP_N); |
| To | void vDSP_vswapD ( double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_B, vDSP_Stride __vDSP_IB, vDSP_Length __vDSP_N); |

Modified [vDSP_vswsum()](https://developer.apple.com/documentation/accelerate/1449822-vdsp_vswsum)

|  | Declaration |
| --- | --- |
| From | void vDSP_vswsum ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_vswsum ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_vswsumD()](https://developer.apple.com/documentation/accelerate/1449693-vdsp_vswsumd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vswsumD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_vswsumD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_vtabi()](https://developer.apple.com/documentation/accelerate/1450762-vdsp_vtabi)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtabi ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_S1, float \*__vDSP_S2, float \*__vDSP_C, vDSP_Length __vDSP_M, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vtabi ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_S1, const float \*__vDSP_S2, const float \*__vDSP_C, vDSP_Length __vDSP_M, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vtabiD()](https://developer.apple.com/documentation/accelerate/1449832-vdsp_vtabid)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtabiD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_S1, double \*__vDSP_S2, double \*__vDSP_C, vDSP_Length __vDSP_M, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vtabiD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_S1, const double \*__vDSP_S2, const double \*__vDSP_C, vDSP_Length __vDSP_M, double \*__vDSP_ID, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |

Modified [vDSP_vthr()](https://developer.apple.com/documentation/accelerate/1450030-vdsp_vthr)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthr ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vthr ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vthrD()](https://developer.apple.com/documentation/accelerate/1450834-vdsp_vthrd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthrD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vthrD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vthres()](https://developer.apple.com/documentation/accelerate/1450597-vdsp_vthres)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthres ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vthres ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vthresD()](https://developer.apple.com/documentation/accelerate/1450767-vdsp_vthresd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthresD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vthresD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vthrsc()](https://developer.apple.com/documentation/accelerate/1450631-vdsp_vthrsc)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthrsc ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vthrsc ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, const float \*__vDSP_C, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vthrscD()](https://developer.apple.com/documentation/accelerate/1450230-vdsp_vthrscd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vthrscD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_vthrscD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, const double \*__vDSP_C, double \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_vtmerg()](https://developer.apple.com/documentation/accelerate/1450140-vdsp_vtmerg)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtmerg ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vtmerg ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vtmergD()](https://developer.apple.com/documentation/accelerate/1450175-vdsp_vtmergd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtmergD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vtmergD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vtrapz()](https://developer.apple.com/documentation/accelerate/1450678-vdsp_vtrapz)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtrapz ( float \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vtrapz ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_vtrapzD()](https://developer.apple.com/documentation/accelerate/1450810-vdsp_vtrapzd)

|  | Declaration |
| --- | --- |
| From | void vDSP_vtrapzD ( double \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_vtrapzD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_wiener()](https://developer.apple.com/documentation/accelerate/1450711-vdsp_wiener)

|  | Declaration |
| --- | --- |
| From | void vDSP_wiener ( vDSP_Length __vDSP_L, float \*__vDSP_A, float \*__vDSP_C, float \*__vDSP_F, float \*__vDSP_P, int __vDSP_IFLG, int \*__vDSP_IERR); |
| To | void vDSP_wiener ( vDSP_Length __vDSP_L, const float \*__vDSP_A, const float \*__vDSP_C, float \*__vDSP_F, float \*__vDSP_P, int __vDSP_Flag, int \*__vDSP_Error); |

Modified [vDSP_wienerD()](https://developer.apple.com/documentation/accelerate/1450592-vdsp_wienerd)

|  | Declaration |
| --- | --- |
| From | void vDSP_wienerD ( vDSP_Length __vDSP_L, double \*__vDSP_A, double \*__vDSP_C, double \*__vDSP_F, double \*__vDSP_P, int __vDSP_IFLG, int \*__vDSP_IERR); |
| To | void vDSP_wienerD ( vDSP_Length __vDSP_L, const double \*__vDSP_A, const double \*__vDSP_C, double \*__vDSP_F, double \*__vDSP_P, int __vDSP_Flag, int \*__vDSP_Error); |

Modified [vDSP_zaspec()](https://developer.apple.com/documentation/accelerate/1449691-vdsp_zaspec)

|  | Declaration |
| --- | --- |
| From | void vDSP_zaspec ( DSPSplitComplex \*__vDSP_A, float \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_zaspec ( const DSPSplitComplex \*__vDSP_A, float \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zaspecD()](https://developer.apple.com/documentation/accelerate/1450746-vdsp_zaspecd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zaspecD ( DSPDoubleSplitComplex \*A, double \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_zaspecD ( const DSPDoubleSplitComplex \*__vDSP_A, double \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zcoher()](https://developer.apple.com/documentation/accelerate/1450253-vdsp_zcoher)

|  | Declaration |
| --- | --- |
| From | void vDSP_zcoher ( float \*__vDSP_A, float \*__vDSP_B, DSPSplitComplex \*__vDSP_C, float \*__vDSP_D, vDSP_Length __vDSP_N); |
| To | void vDSP_zcoher ( const float \*__vDSP_A, const float \*__vDSP_B, const DSPSplitComplex \*__vDSP_C, float \*__vDSP_D, vDSP_Length __vDSP_N); |

Modified [vDSP_zcoherD()](https://developer.apple.com/documentation/accelerate/1450001-vdsp_zcoherd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zcoherD ( double \*__vDSP_A, double \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, double \*__vDSP_D, vDSP_Length __vDSP_N); |
| To | void vDSP_zcoherD ( const double \*__vDSP_A, const double \*__vDSP_B, const DSPDoubleSplitComplex \*__vDSP_C, double \*__vDSP_D, vDSP_Length __vDSP_N); |

Modified [vDSP_zconv()](https://developer.apple.com/documentation/accelerate/1450771-vdsp_zconv)

|  | Declaration |
| --- | --- |
| From | void vDSP_zconv ( DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_filter, vDSP_Stride __vDSP_strideFilter, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void vDSP_zconv ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_F, vDSP_Stride __vDSP_IF, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zconvD()](https://developer.apple.com/documentation/accelerate/1450522-vdsp_zconvd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zconvD ( DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_filter, vDSP_Stride __vDSP_strideFilter, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void vDSP_zconvD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_F, vDSP_Stride __vDSP_IF, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zcspec()](https://developer.apple.com/documentation/accelerate/1450283-vdsp_zcspec)

|  | Declaration |
| --- | --- |
| From | void vDSP_zcspec ( DSPSplitComplex \*__vDSP_A, DSPSplitComplex \*__vDSP_B, DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_zcspec ( const DSPSplitComplex \*__vDSP_A, const DSPSplitComplex \*__vDSP_B, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zcspecD()](https://developer.apple.com/documentation/accelerate/1450164-vdsp_zcspecd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zcspecD ( DSPDoubleSplitComplex \*A, DSPDoubleSplitComplex \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_zcspecD ( const DSPDoubleSplitComplex \*__vDSP_A, const DSPDoubleSplitComplex \*__vDSP_B, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zdotpr()](https://developer.apple.com/documentation/accelerate/1450701-vdsp_zdotpr)

|  | Declaration |
| --- | --- |
| From | void vDSP_zdotpr ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zdotpr ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zdotprD()](https://developer.apple.com/documentation/accelerate/1450740-vdsp_zdotprd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zdotprD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zdotprD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zidotpr()](https://developer.apple.com/documentation/accelerate/1450063-vdsp_zidotpr)

|  | Declaration |
| --- | --- |
| From | void vDSP_zidotpr ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zidotpr ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zidotprD()](https://developer.apple.com/documentation/accelerate/1450309-vdsp_zidotprd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zidotprD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zidotprD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zmma()](https://developer.apple.com/documentation/accelerate/1450160-vdsp_zmma)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmma ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmma ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmmaD()](https://developer.apple.com/documentation/accelerate/1450365-vdsp_zmmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmmaD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPDoubleSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmmaD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmms()](https://developer.apple.com/documentation/accelerate/1450785-vdsp_zmms)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmms ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmms ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmmsD()](https://developer.apple.com/documentation/accelerate/1450311-vdsp_zmmsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmmsD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPDoubleSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmmsD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmmul()](https://developer.apple.com/documentation/accelerate/1449712-vdsp_zmmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmmul ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmmulD()](https://developer.apple.com/documentation/accelerate/1450796-vdsp_zmmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmmulD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmsm()](https://developer.apple.com/documentation/accelerate/1450400-vdsp_zmsm)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmsm ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmsm ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zmsmD()](https://developer.apple.com/documentation/accelerate/1450218-vdsp_zmsmd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zmsmD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPDoubleSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void vDSP_zmsmD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zrdesamp()](https://developer.apple.com/documentation/accelerate/1449891-vdsp_zrdesamp)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrdesamp ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_zrdesamp ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, const float \*__vDSP_F, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zrdesampD()](https://developer.apple.com/documentation/accelerate/1449934-vdsp_zrdesampd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrdesampD ( DSPDoubleSplitComplex \*A, vDSP_Stride __vDSP_I, double \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_M); |
| To | void vDSP_zrdesampD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, const double \*__vDSP_F, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified [vDSP_zrdotpr()](https://developer.apple.com/documentation/accelerate/1450544-vdsp_zrdotpr)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrdotpr ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zrdotpr ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zrdotprD()](https://developer.apple.com/documentation/accelerate/1450394-vdsp_zrdotprd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrdotprD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void vDSP_zrdotprD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvadd()](https://developer.apple.com/documentation/accelerate/1449990-vdsp_zrvadd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvadd ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvadd ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvaddD()](https://developer.apple.com/documentation/accelerate/1450465-vdsp_zrvaddd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvaddD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvaddD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvdiv()](https://developer.apple.com/documentation/accelerate/1450142-vdsp_zrvdiv)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvdiv ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zrvdiv ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvdivD()](https://developer.apple.com/documentation/accelerate/1450666-vdsp_zrvdivd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvdivD ( DSPDoubleSplitComplex \*A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zrvdivD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvmul()](https://developer.apple.com/documentation/accelerate/1450657-vdsp_zrvmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvmul ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvmulD()](https://developer.apple.com/documentation/accelerate/1449954-vdsp_zrvmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvmulD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvsub()](https://developer.apple.com/documentation/accelerate/1449845-vdsp_zrvsub)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvsub ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvsub ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zrvsubD()](https://developer.apple.com/documentation/accelerate/1450034-vdsp_zrvsubd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zrvsubD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zrvsubD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_ztoc()](https://developer.apple.com/documentation/kernel/1579934-vdsp_ztoc)

|  | Declaration |
| --- | --- |
| From | void vDSP_ztoc ( const DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, DSPComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, vDSP_Length __vDSP_size); |
| To | void vDSP_ztoc ( const DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, DSPComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_ztocD()](https://developer.apple.com/documentation/accelerate/1450165-vdsp_ztocd)

|  | Declaration |
| --- | --- |
| From | void vDSP_ztocD ( const DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, DSPDoubleComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, vDSP_Length __vDSP_size); |
| To | void vDSP_ztocD ( const DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, DSPDoubleComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_ztrans()](https://developer.apple.com/documentation/accelerate/1450787-vdsp_ztrans)

|  | Declaration |
| --- | --- |
| From | void vDSP_ztrans ( float \*__vDSP_A, DSPSplitComplex \*__vDSP_B, DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_ztrans ( const float \*__vDSP_A, const DSPSplitComplex \*__vDSP_B, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_ztransD()](https://developer.apple.com/documentation/accelerate/1450357-vdsp_ztransd)

|  | Declaration |
| --- | --- |
| From | void vDSP_ztransD ( double \*__vDSP_A, DSPDoubleSplitComplex \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |
| To | void vDSP_ztransD ( const double \*__vDSP_A, const DSPDoubleSplitComplex \*__vDSP_B, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified [vDSP_zvabs()](https://developer.apple.com/documentation/kernel/1579998-vdsp_zvabs)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvabs ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvabs ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvabsD()](https://developer.apple.com/documentation/accelerate/1450251-vdsp_zvabsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvabsD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvabsD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvadd()](https://developer.apple.com/documentation/accelerate/1450051-vdsp_zvadd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvadd ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvadd ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvaddD()](https://developer.apple.com/documentation/accelerate/1449906-vdsp_zvaddd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvaddD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvaddD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvcma()](https://developer.apple.com/documentation/accelerate/1450200-vdsp_zvcma)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvcma ( const DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPSplitComplex \*__vDSP_input3, vDSP_Stride __vDSP_stride3, const DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvcma ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_zvcmaD()](https://developer.apple.com/documentation/accelerate/1450572-vdsp_zvcmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvcmaD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_input3, vDSP_Stride __vDSP_stride3, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvcmaD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_zvcmul()](https://developer.apple.com/documentation/accelerate/1450717-vdsp_zvcmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvcmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvcmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvcmulD()](https://developer.apple.com/documentation/accelerate/1449764-vdsp_zvcmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvcmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvcmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_iC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvconj()](https://developer.apple.com/documentation/accelerate/1450617-vdsp_zvconj)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvconj ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvconj ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvconjD()](https://developer.apple.com/documentation/accelerate/1450479-vdsp_zvconjd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvconjD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvconjD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvdiv()](https://developer.apple.com/documentation/accelerate/1449769-vdsp_zvdiv)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvdiv ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvdiv ( const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvdivD()](https://developer.apple.com/documentation/accelerate/1450594-vdsp_zvdivd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvdivD ( DSPDoubleSplitComplex \*A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_J, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvdivD ( const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvfill()](https://developer.apple.com/documentation/accelerate/1450499-vdsp_zvfill)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvfill ( DSPSplitComplex \*__vDSP_A, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvfill ( const DSPSplitComplex \*__vDSP_A, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvfillD()](https://developer.apple.com/documentation/accelerate/1450495-vdsp_zvfilld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvfillD ( DSPDoubleSplitComplex \*__vDSP_A, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvfillD ( const DSPDoubleSplitComplex \*__vDSP_A, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmags()](https://developer.apple.com/documentation/accelerate/1450557-vdsp_zvmags)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmags ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmags ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmagsD()](https://developer.apple.com/documentation/accelerate/1450026-vdsp_zvmagsd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmagsD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmagsD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmgsa()](https://developer.apple.com/documentation/accelerate/1450647-vdsp_zvmgsa)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmgsa ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_B, vDSP_Stride __vDSP_J, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmgsa ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmgsaD()](https://developer.apple.com/documentation/accelerate/1450338-vdsp_zvmgsad)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmgsaD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_B, vDSP_Stride __vDSP_J, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmgsaD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmov()](https://developer.apple.com/documentation/kernel/1579979-vdsp_zvmov)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmov ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmov ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmovD()](https://developer.apple.com/documentation/accelerate/1450484-vdsp_zvmovd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmovD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvmovD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvmul()](https://developer.apple.com/documentation/kernel/1579954-vdsp_zvmul)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmul ( const DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size, int __vDSP_conjugate); |
| To | void vDSP_zvmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, int __vDSP_Conjugate); |

Modified [vDSP_zvmulD()](https://developer.apple.com/documentation/accelerate/1450390-vdsp_zvmuld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvmulD ( const DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size, int __vDSP_conjugate); |
| To | void vDSP_zvmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, int __vDSP_Conjugate); |

Modified [vDSP_zvneg()](https://developer.apple.com/documentation/accelerate/1450326-vdsp_zvneg)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvneg ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvneg ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvnegD()](https://developer.apple.com/documentation/accelerate/1450351-vdsp_zvnegd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvnegD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvnegD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvphas()](https://developer.apple.com/documentation/accelerate/1449904-vdsp_zvphas)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvphas ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, float \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvphas ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvphasD()](https://developer.apple.com/documentation/accelerate/1450132-vdsp_zvphasd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvphasD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, double \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvphasD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvsma()](https://developer.apple.com/documentation/accelerate/1449902-vdsp_zvsma)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvsma ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_B, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_zvsma ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_zvsmaD()](https://developer.apple.com/documentation/accelerate/1450570-vdsp_zvsmad)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvsmaD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_L, vDSP_Length __vDSP_N); |
| To | void vDSP_zvsmaD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified [vDSP_zvsub()](https://developer.apple.com/documentation/accelerate/1450818-vdsp_zvsub)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvsub ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvsub ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvsubD()](https://developer.apple.com/documentation/accelerate/1450642-vdsp_zvsubd)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvsubD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vDSP_zvsubD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvzsml()](https://developer.apple.com/documentation/accelerate/1450410-vdsp_zvzsml)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvzsml ( DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPSplitComplex \*__vDSP_B, DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvzsml ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified [vDSP_zvzsmlD()](https://developer.apple.com/documentation/accelerate/1449727-vdsp_zvzsmld)

|  | Declaration |
| --- | --- |
| From | void vDSP_zvzsmlD ( DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_I, DSPDoubleSplitComplex \*__vDSP_B, DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_K, vDSP_Length __vDSP_N); |
| To | void vDSP_zvzsmlD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vadd()

|  | Declaration |
| --- | --- |
| From | void vadd ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vadd ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vaddD()

|  | Declaration |
| --- | --- |
| From | void vaddD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vaddD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vam()

|  | Declaration |
| --- | --- |
| From | void vam ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, const float __vDSP_input3[], vDSP_Stride __vDSP_stride3, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vam ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_C, vDSP_Stride __vDSP_IC, float \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified vamD()

|  | Declaration |
| --- | --- |
| From | void vamD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, const double __vDSP_input3[], vDSP_Stride __vDSP_stride3, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vamD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_C, vDSP_Stride __vDSP_IC, double \*__vDSP_D, vDSP_Stride __vDSP_IDD, vDSP_Length __vDSP_N); |

Modified vmul()

|  | Declaration |
| --- | --- |
| From | void vmul ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vmul ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vmulD()

|  | Declaration |
| --- | --- |
| From | void vmulD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vmulD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vsmul()

|  | Declaration |
| --- | --- |
| From | void vsmul ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float \*__vDSP_input2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vsmul ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vsmulD()

|  | Declaration |
| --- | --- |
| From | void vsmulD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double \*__vDSP_input2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vsmulD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vsq()

|  | Declaration |
| --- | --- |
| From | void vsq ( const float __vDSP_input[], vDSP_Stride __vDSP_strideInput, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vsq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vsqD()

|  | Declaration |
| --- | --- |
| From | void vsqD ( const double __vDSP_input[], vDSP_Stride __vDSP_strideInput, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vsqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vssq()

|  | Declaration |
| --- | --- |
| From | void vssq ( const float __vDSP_input[], vDSP_Stride __vDSP_strideInput, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vssq ( const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vssqD()

|  | Declaration |
| --- | --- |
| From | void vssqD ( const double __vDSP_input[], vDSP_Stride __vDSP_strideInput, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vssqD ( const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vsub()

|  | Declaration |
| --- | --- |
| From | void vsub ( const float __vDSP_input1[], vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, float __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vsub ( const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const float \*__vDSP_A, vDSP_Stride __vDSP_IA, float \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified vsubD()

|  | Declaration |
| --- | --- |
| From | void vsubD ( const double __vDSP_input1[], vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, double __vDSP_result[], vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void vsubD ( const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const double \*__vDSP_A, vDSP_Stride __vDSP_IA, double \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified zconv()

|  | Declaration |
| --- | --- |
| From | void zconv ( DSPSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPSplitComplex \*__vDSP_filter, vDSP_Stride __vDSP_strideFilter, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void zconv ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_F, vDSP_Stride __vDSP_IF, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified zconvD()

|  | Declaration |
| --- | --- |
| From | void zconvD ( DSPDoubleSplitComplex \*__vDSP_signal, vDSP_Stride __vDSP_signalStride, DSPDoubleSplitComplex \*__vDSP_filter, vDSP_Stride __vDSP_strideFilter, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_lenResult, vDSP_Length __vDSP_lenFilter); |
| To | void zconvD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_F, vDSP_Stride __vDSP_IF, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified zdotpr()

|  | Declaration |
| --- | --- |
| From | void zdotpr ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void zdotpr ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified zdotprD()

|  | Declaration |
| --- | --- |
| From | void zdotprD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void zdotprD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified zidotpr()

|  | Declaration |
| --- | --- |
| From | void zidotpr ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void zidotpr ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified zidotprD()

|  | Declaration |
| --- | --- |
| From | void zidotprD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void zidotprD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified zmma()

|  | Declaration |
| --- | --- |
| From | void zmma ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void zmma ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified zmmaD()

|  | Declaration |
| --- | --- |
| From | void zmmaD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPDoubleSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void zmmaD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified zmms()

|  | Declaration |
| --- | --- |
| From | void zmms ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void zmms ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified zmmsD()

|  | Declaration |
| --- | --- |
| From | void zmmsD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPDoubleSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void zmmsD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified zmmul()

|  | Declaration |
| --- | --- |
| From | void zmmul ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void zmmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified zmmulD()

|  | Declaration |
| --- | --- |
| From | void zmmulD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void zmmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified zmsm()

|  | Declaration |
| --- | --- |
| From | void zmsm ( DSPSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void zmsm ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified zmsmD()

|  | Declaration |
| --- | --- |
| From | void zmsmD ( DSPDoubleSplitComplex \*__vDSP_a, vDSP_Stride __vDSP_i, DSPDoubleSplitComplex \*__vDSP_b, vDSP_Stride __vDSP_j, DSPDoubleSplitComplex \*__vDSP_c, vDSP_Stride __vDSP_k, DSPDoubleSplitComplex \*__vDSP_d, vDSP_Stride __vDSP_l, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |
| To | void zmsmD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_M, vDSP_Length __vDSP_N, vDSP_Length __vDSP_P); |

Modified zrdotpr()

|  | Declaration |
| --- | --- |
| From | void zrdotpr ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void zrdotpr ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified zrdotprD()

|  | Declaration |
| --- | --- |
| From | void zrdotprD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Length __vDSP_size); |
| To | void zrdotprD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Length __vDSP_N); |

Modified zrvadd()

|  | Declaration |
| --- | --- |
| From | void zrvadd ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zrvadd ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified zrvaddD()

|  | Declaration |
| --- | --- |
| From | void zrvaddD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zrvaddD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified zrvmul()

|  | Declaration |
| --- | --- |
| From | void zrvmul ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zrvmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified zrvmulD()

|  | Declaration |
| --- | --- |
| From | void zrvmulD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zrvmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified zrvsub()

|  | Declaration |
| --- | --- |
| From | void zrvsub ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const float __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zrvsub ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const float \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified zrvsubD()

|  | Declaration |
| --- | --- |
| From | void zrvsubD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const double __vDSP_input2[], vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zrvsubD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const double \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified ztoc()

|  | Declaration |
| --- | --- |
| From | void ztoc ( const DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, DSPComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, vDSP_Length __vDSP_size); |
| To | void ztoc ( const DSPSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, DSPComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified ztocD()

|  | Declaration |
| --- | --- |
| From | void ztocD ( const DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_strideZ, DSPDoubleComplex __vDSP_C[], vDSP_Stride __vDSP_strideC, vDSP_Length __vDSP_size); |
| To | void ztocD ( const DSPDoubleSplitComplex \*__vDSP_Z, vDSP_Stride __vDSP_IZ, DSPDoubleComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified zvadd()

|  | Declaration |
| --- | --- |
| From | void zvadd ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zvadd ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified zvaddD()

|  | Declaration |
| --- | --- |
| From | void zvaddD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zvaddD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified zvcma()

|  | Declaration |
| --- | --- |
| From | void zvcma ( const DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPSplitComplex \*__vDSP_input3, vDSP_Stride __vDSP_stride3, const DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zvcma ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified zvcmaD()

|  | Declaration |
| --- | --- |
| From | void zvcmaD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_input3, vDSP_Stride __vDSP_stride3, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zvcmaD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, const DSPDoubleSplitComplex \*__vDSP_D, vDSP_Stride __vDSP_ID, vDSP_Length __vDSP_N); |

Modified zvmul()

|  | Declaration |
| --- | --- |
| From | void zvmul ( const DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size, int __vDSP_conjugate); |
| To | void zvmul ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, int __vDSP_Conjugate); |

Modified zvmulD()

|  | Declaration |
| --- | --- |
| From | void zvmulD ( const DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, const DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, const DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size, int __vDSP_conjugate); |
| To | void zvmulD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N, int __vDSP_Conjugate); |

Modified zvsub()

|  | Declaration |
| --- | --- |
| From | void zvsub ( DSPSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zvsub ( const DSPSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

Modified zvsubD()

|  | Declaration |
| --- | --- |
| From | void zvsubD ( DSPDoubleSplitComplex \*__vDSP_input1, vDSP_Stride __vDSP_stride1, DSPDoubleSplitComplex \*__vDSP_input2, vDSP_Stride __vDSP_stride2, DSPDoubleSplitComplex \*__vDSP_result, vDSP_Stride __vDSP_strideResult, vDSP_Length __vDSP_size); |
| To | void zvsubD ( const DSPDoubleSplitComplex \*__vDSP_A, vDSP_Stride __vDSP_IA, const DSPDoubleSplitComplex \*__vDSP_B, vDSP_Stride __vDSP_IB, const DSPDoubleSplitComplex \*__vDSP_C, vDSP_Stride __vDSP_IC, vDSP_Length __vDSP_N); |

vForce.hAdded vvpows()Added vvpowsf()Modified [vvcopysign()](https://developer.apple.com/documentation/accelerate/1470348-vvcopysign)

|  | Declaration |
| --- | --- |
| From | void vvcopysign ( double \*, double \*, const double \*, const int \*); |
| To | void vvcopysign ( double \*, const double \*, const double \*, const int \*); |

Modified [vvfmod()](https://developer.apple.com/documentation/accelerate/1470379-vvfmod)

|  | Declaration |
| --- | --- |
| From | void vvfmod ( double \*, double \*, const double \*, const int \*); |
| To | void vvfmod ( double \*, const double \*, const double \*, const int \*); |

Modified [vvnextafter()](https://developer.apple.com/documentation/accelerate/1470487-vvnextafter)

|  | Declaration |
| --- | --- |
| From | void vvnextafter ( double \*, double \*, const double \*, const int \*); |
| To | void vvnextafter ( double \*, const double \*, const double \*, const int \*); |

Modified [vvremainder()](https://developer.apple.com/documentation/accelerate/1470456-vvremainder)

|  | Declaration |
| --- | --- |
| From | void vvremainder ( double \*, double \*, const double \*, const int \*); |
| To | void vvremainder ( double \*, const double \*, const double \*, const int \*); |

vImage_Types.hAdded Pixel_16SAdded Pixel_ARGB_16SAdded Pixel_ARGB_16UAdded #def VIMAGE_CHOICE_ENUMAdded #def VIMAGE_ENUM_AVAILABLE_STARTINGAdded #def VIMAGE_NON_NULLAdded #def VIMAGE_OPTIONS_ENUMAdded [kvImageColorSyncIsAbsent](https://developer.apple.com/documentation/accelerate/kvimagecolorsyncisabsent)Added [kvImageInternalError](https://developer.apple.com/documentation/accelerate/kvimageinternalerror)Added [kvImageInvalidImageFormat](https://developer.apple.com/documentation/accelerate/1578972-error_codes/kvimageinvalidimageformat)Added [kvImageInvalidRowBytes](https://developer.apple.com/documentation/accelerate/kvimageinvalidrowbytes)Added [kvImageNoAllocate](https://developer.apple.com/documentation/accelerate/1578976-processing_flags/kvimagenoallocate)Added [kvImageOutOfPlaceOperationRequired](https://developer.apple.com/documentation/accelerate/kvimageoutofplaceoperationrequired)Added [kvImagePrintDiagnosticsToConsole](https://developer.apple.com/documentation/accelerate/kvimageprintdiagnosticstoconsole)vImage_Utilities.hAdded [kvImageDecodeArray_16Q12Format](https://developer.apple.com/documentation/accelerate/kvimagedecodearray_16q12format)Added [vImageBuffer_GetSize()](https://developer.apple.com/documentation/accelerate/1399062-vimagebuffer_getsize)Added [vImageBuffer_Init()](https://developer.apple.com/documentation/accelerate/1399064-vimagebuffer_init)Added [vImageBuffer_InitWithCGImage()](https://developer.apple.com/documentation/accelerate/1399118-vimagebuffer_initwithcgimage)Added [vImageCGImageFormat_GetComponentCount()](https://developer.apple.com/documentation/accelerate/1399104-vimagecgimageformat_getcomponent)Added [vImageCGImageFormat_IsEqual()](https://developer.apple.com/documentation/accelerate/1399126-vimagecgimageformat_isequal)Added [vImageConvert_AnyToAny()](https://developer.apple.com/documentation/accelerate/1399134-vimageconvert_anytoany)Added [vImageConverterRef](https://developer.apple.com/documentation/accelerate/vimageconverterref)Added [vImageConverter_CreateWithCGImageFormat()](https://developer.apple.com/documentation/accelerate/1399114-vimageconverter_createwithcgimag)Added [vImageConverter_CreateWithColorSyncCodeFragment()](https://developer.apple.com/documentation/accelerate/1399082-vimageconverter_createwithcolors)Added [vImageConverter_MustOperateOutOfPlace()](https://developer.apple.com/documentation/accelerate/1399054-vimageconverter_mustoperateoutof)Added [vImageConverter_Release()](https://developer.apple.com/documentation/accelerate/1399068-vimageconverter_release)Added [vImageConverter_Retain()](https://developer.apple.com/documentation/accelerate/1399028-vimageconverter_retain)Added [vImageCreateCGImageFromBuffer()](https://developer.apple.com/documentation/accelerate/1399036-vimagecreatecgimagefrombuffer)Added [vImage_CGImageFormat](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat)Added #def vImage_Utilities_hvfp.hAdded vcospif()Added vexp2f()Added vfabsf()Added vlog2f()Added vsinpif()Added vtanpif()Added vtruncf()

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
