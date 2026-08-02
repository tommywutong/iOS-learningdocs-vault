---
title: iOS 5.0 API Diffs
apple_id: TP40011042
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS50APIDiff/index.html
archived_at: '2026-07-18T02:55:46.751092Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# iOS 4.3 to iOS 5.0 API Differences

## Added frameworks:

- Accounts
- CoreBluetooth
- CoreImage
- GLKit
- GSS
- NewsstandKit
- Twitter

## Accelerate

Alpha.hAdded #def VIMAGE_ALPHA_HAdded [vImageAlphaBlend_ARGB8888()](https://developer.apple.com/documentation/accelerate/1410655-vimagealphablend_argb8888)Added [vImageAlphaBlend_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1410632-vimagealphablend_argbffff)Added [vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGB8888()](https://developer.apple.com/documentation/accelerate/1410736-vimagealphablend_nonpremultiplie)Added [vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1410713-vimagealphablend_nonpremultiplie)Added [vImageAlphaBlend_NonpremultipliedToPremultiplied_Planar8()](https://developer.apple.com/documentation/accelerate/1410653-vimagealphablend_nonpremultiplie)Added [vImageAlphaBlend_NonpremultipliedToPremultiplied_PlanarF()](https://developer.apple.com/documentation/accelerate/1410662-vimagealphablend_nonpremultiplie)Added [vImageAlphaBlend_Planar8()](https://developer.apple.com/documentation/accelerate/1410685-vimagealphablend_planar8)Added [vImageAlphaBlend_PlanarF()](https://developer.apple.com/documentation/accelerate/1410723-vimagealphablend_planarf)Added [vImageClipToAlpha_ARGB8888()](https://developer.apple.com/documentation/accelerate/1410630-vimagecliptoalpha_argb8888)Added [vImageClipToAlpha_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1410717-vimagecliptoalpha_argbffff)Added [vImageClipToAlpha_Planar8()](https://developer.apple.com/documentation/accelerate/1410698-vimagecliptoalpha_planar8)Added [vImageClipToAlpha_PlanarF()](https://developer.apple.com/documentation/accelerate/1410640-vimagecliptoalpha_planarf)Added [vImagePremultipliedAlphaBlend_ARGB8888()](https://developer.apple.com/documentation/accelerate/1410657-vimagepremultipliedalphablend_ar)Added [vImagePremultipliedAlphaBlend_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1410705-vimagepremultipliedalphablend_ar)Added [vImagePremultipliedAlphaBlend_BGRA8888()](https://developer.apple.com/documentation/accelerate/1410682-vimagepremultipliedalphablend_bg)Added [vImagePremultipliedAlphaBlend_BGRAFFFF()](https://developer.apple.com/documentation/accelerate/1410634-vimagepremultipliedalphablend_bg)Added [vImagePremultipliedAlphaBlend_Planar8()](https://developer.apple.com/documentation/accelerate/1410645-vimagepremultipliedalphablend_pl)Added [vImagePremultipliedAlphaBlend_PlanarF()](https://developer.apple.com/documentation/accelerate/1410686-vimagepremultipliedalphablend_pl)Added [#def vImagePremultipliedAlphaBlend_RGBA8888](https://developer.apple.com/documentation/accelerate/vimagepremultipliedalphablend_rgba8888)Added [#def vImagePremultipliedAlphaBlend_RGBAFFFF](https://developer.apple.com/documentation/accelerate/vimagepremultipliedalphablend_rgbaffff)Added [vImagePremultipliedConstAlphaBlend_ARGB8888()](https://developer.apple.com/documentation/accelerate/1410696-vimagepremultipliedconstalphable)Added [vImagePremultipliedConstAlphaBlend_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1410731-vimagepremultipliedconstalphable)Added [vImagePremultipliedConstAlphaBlend_Planar8()](https://developer.apple.com/documentation/accelerate/1410709-vimagepremultipliedconstalphable)Added [vImagePremultipliedConstAlphaBlend_PlanarF()](https://developer.apple.com/documentation/accelerate/1410719-vimagepremultipliedconstalphable)Added [vImagePremultiplyData_ARGB8888()](https://developer.apple.com/documentation/accelerate/1410692-vimagepremultiplydata_argb8888)Added [vImagePremultiplyData_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1410678-vimagepremultiplydata_argbffff)Added [#def vImagePremultiplyData_BGRA8888](https://developer.apple.com/documentation/accelerate/vimagepremultiplydata_bgra8888)Added [#def vImagePremultiplyData_BGRAFFFF](https://developer.apple.com/documentation/accelerate/vimagepremultiplydata_bgraffff)Added [vImagePremultiplyData_Planar8()](https://developer.apple.com/documentation/accelerate/1410727-vimagepremultiplydata_planar8)Added [vImagePremultiplyData_PlanarF()](https://developer.apple.com/documentation/accelerate/1410684-vimagepremultiplydata_planarf)Added [vImagePremultiplyData_RGBA8888()](https://developer.apple.com/documentation/accelerate/1410671-vimagepremultiplydata_rgba8888)Added [vImagePremultiplyData_RGBAFFFF()](https://developer.apple.com/documentation/accelerate/1410699-vimagepremultiplydata_rgbaffff)Added [vImageUnpremultiplyData_ARGB8888()](https://developer.apple.com/documentation/accelerate/1410651-vimageunpremultiplydata_argb8888)Added [vImageUnpremultiplyData_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1410667-vimageunpremultiplydata_argbffff)Added [#def vImageUnpremultiplyData_BGRA8888](https://developer.apple.com/documentation/accelerate/vimageunpremultiplydata_bgra8888)Added [#def vImageUnpremultiplyData_BGRAFFFF](https://developer.apple.com/documentation/accelerate/vimageunpremultiplydata_bgraffff)Added [vImageUnpremultiplyData_Planar8()](https://developer.apple.com/documentation/accelerate/1410732-vimageunpremultiplydata_planar8)Added [vImageUnpremultiplyData_PlanarF()](https://developer.apple.com/documentation/accelerate/1410649-vimageunpremultiplydata_planarf)Added [vImageUnpremultiplyData_RGBA8888()](https://developer.apple.com/documentation/accelerate/1410701-vimageunpremultiplydata_rgba8888)Added [vImageUnpremultiplyData_RGBAFFFF()](https://developer.apple.com/documentation/accelerate/1410734-vimageunpremultiplydata_rgbaffff)BasicImageTypes.hAdded #def VIMAGE_BASIC_IMAGE_TYPES_HAdded [kvImage_PNG_FILTER_VALUE_AVG](https://developer.apple.com/documentation/accelerate/1515413-png_filter_types/kvimage_png_filter_value_avg)Added [kvImage_PNG_FILTER_VALUE_NONE](https://developer.apple.com/documentation/accelerate/1515413-png_filter_types/kvimage_png_filter_value_none)Added [kvImage_PNG_FILTER_VALUE_PAETH](https://developer.apple.com/documentation/accelerate/1515413-png_filter_types/kvimage_png_filter_value_paeth)Added [kvImage_PNG_FILTER_VALUE_SUB](https://developer.apple.com/documentation/accelerate/kvimage_png_filter_value_sub)Added [kvImage_PNG_FILTER_VALUE_UP](https://developer.apple.com/documentation/accelerate/1515413-png_filter_types/kvimage_png_filter_value_up)Added [vImagePNGDecompressionFilter()](https://developer.apple.com/documentation/accelerate/1515414-vimagepngdecompressionfilter)Conversion.hAdded #def VIMAGE_CONVERSION_HAdded [vImageBufferFill_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533131-vimagebufferfill_argb8888)Added [vImageBufferFill_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533238-vimagebufferfill_argbffff)Added [vImageClip_PlanarF()](https://developer.apple.com/documentation/accelerate/1533117-vimageclip_planarf)Added [vImageConvert_16SToF()](https://developer.apple.com/documentation/accelerate/1533286-vimageconvert_16stof)Added [vImageConvert_16UToF()](https://developer.apple.com/documentation/accelerate/1533130-vimageconvert_16utof)Added [vImageConvert_16UToPlanar8()](https://developer.apple.com/documentation/accelerate/1533224-vimageconvert_16utoplanar8)Added [vImageConvert_ARGB1555toARGB8888()](https://developer.apple.com/documentation/accelerate/1533237-vimageconvert_argb1555toargb8888)Added [vImageConvert_ARGB1555toPlanar8()](https://developer.apple.com/documentation/accelerate/1533269-vimageconvert_argb1555toplanar8)Added [vImageConvert_ARGB8888toARGB1555()](https://developer.apple.com/documentation/accelerate/1533047-vimageconvert_argb8888toargb1555)Added [vImageConvert_ARGB8888toPlanar8()](https://developer.apple.com/documentation/accelerate/1533144-vimageconvert_argb8888toplanar8)Added [vImageConvert_ARGB8888toRGB565()](https://developer.apple.com/documentation/accelerate/1533044-vimageconvert_argb8888torgb565)Added [vImageConvert_ARGB8888toRGB888()](https://developer.apple.com/documentation/accelerate/1533276-vimageconvert_argb8888torgb888)Added [vImageConvert_ARGBFFFFtoPlanarF()](https://developer.apple.com/documentation/accelerate/1533243-vimageconvert_argbfffftoplanarf)Added [vImageConvert_ChunkyToPlanar8()](https://developer.apple.com/documentation/accelerate/1533240-vimageconvert_chunkytoplanar8)Added [vImageConvert_ChunkyToPlanarF()](https://developer.apple.com/documentation/accelerate/1533260-vimageconvert_chunkytoplanarf)Added [vImageConvert_FTo16S()](https://developer.apple.com/documentation/accelerate/1533281-vimageconvert_fto16s)Added [vImageConvert_FTo16U()](https://developer.apple.com/documentation/accelerate/1533273-vimageconvert_fto16u)Added [vImageConvert_Planar16FtoPlanarF()](https://developer.apple.com/documentation/accelerate/1533030-vimageconvert_planar16ftoplanarf)Added [vImageConvert_Planar8To16U()](https://developer.apple.com/documentation/accelerate/1533230-vimageconvert_planar8to16u)Added [vImageConvert_Planar8ToARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533069-vimageconvert_planar8toargbffff)Added [vImageConvert_Planar8ToBGRX8888()](https://developer.apple.com/documentation/accelerate/1533215-vimageconvert_planar8tobgrx8888)Added [vImageConvert_Planar8ToBGRXFFFF()](https://developer.apple.com/documentation/accelerate/1533138-vimageconvert_planar8tobgrxffff)Added [#def vImageConvert_Planar8ToRGBX8888](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8torgbx8888)Added [#def vImageConvert_Planar8ToRGBXFFFF](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8torgbxffff)Added [vImageConvert_Planar8ToXRGB8888()](https://developer.apple.com/documentation/accelerate/1533265-vimageconvert_planar8toxrgb8888)Added [vImageConvert_Planar8ToXRGBFFFF()](https://developer.apple.com/documentation/accelerate/1533232-vimageconvert_planar8toxrgbffff)Added [vImageConvert_Planar8toARGB1555()](https://developer.apple.com/documentation/accelerate/1532999-vimageconvert_planar8toargb1555)Added [vImageConvert_Planar8toARGB8888()](https://developer.apple.com/documentation/accelerate/1533134-vimageconvert_planar8toargb8888)Added [vImageConvert_Planar8toPlanarF()](https://developer.apple.com/documentation/accelerate/1533188-vimageconvert_planar8toplanarf)Added [vImageConvert_Planar8toRGB565()](https://developer.apple.com/documentation/accelerate/1533146-vimageconvert_planar8torgb565)Added [vImageConvert_Planar8toRGB888()](https://developer.apple.com/documentation/accelerate/1533110-vimageconvert_planar8torgb888)Added [vImageConvert_PlanarFToARGB8888()](https://developer.apple.com/documentation/accelerate/1533216-vimageconvert_planarftoargb8888)Added [vImageConvert_PlanarFToBGRX8888()](https://developer.apple.com/documentation/accelerate/1533213-vimageconvert_planarftobgrx8888)Added [vImageConvert_PlanarFToBGRXFFFF()](https://developer.apple.com/documentation/accelerate/1533052-vimageconvert_planarftobgrxffff)Added [#def vImageConvert_PlanarFToRGBX8888](https://developer.apple.com/documentation/accelerate/vimageconvert_planarftorgbx8888)Added [#def vImageConvert_PlanarFToRGBXFFFF](https://developer.apple.com/documentation/accelerate/vimageconvert_planarftorgbxffff)Added [vImageConvert_PlanarFToXRGB8888()](https://developer.apple.com/documentation/accelerate/1533297-vimageconvert_planarftoxrgb8888)Added [vImageConvert_PlanarFToXRGBFFFF()](https://developer.apple.com/documentation/accelerate/1533208-vimageconvert_planarftoxrgbffff)Added [vImageConvert_PlanarFtoARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533204-vimageconvert_planarftoargbffff)Added [vImageConvert_PlanarFtoPlanar16F()](https://developer.apple.com/documentation/accelerate/1533151-vimageconvert_planarftoplanar16f)Added [vImageConvert_PlanarFtoPlanar8()](https://developer.apple.com/documentation/accelerate/1533107-vimageconvert_planarftoplanar8)Added [vImageConvert_PlanarFtoRGBFFF()](https://developer.apple.com/documentation/accelerate/1533051-vimageconvert_planarftorgbfff)Added [vImageConvert_PlanarToChunky8()](https://developer.apple.com/documentation/accelerate/1533042-vimageconvert_planartochunky8)Added [vImageConvert_PlanarToChunkyF()](https://developer.apple.com/documentation/accelerate/1533074-vimageconvert_planartochunkyf)Added [vImageConvert_RGB565toARGB8888()](https://developer.apple.com/documentation/accelerate/1533159-vimageconvert_rgb565toargb8888)Added [vImageConvert_RGB565toPlanar8()](https://developer.apple.com/documentation/accelerate/1533170-vimageconvert_rgb565toplanar8)Added [vImageConvert_RGB888toARGB8888()](https://developer.apple.com/documentation/accelerate/1533137-vimageconvert_rgb888toargb8888)Added [vImageConvert_RGB888toPlanar8()](https://developer.apple.com/documentation/accelerate/1533040-vimageconvert_rgb888toplanar8)Added [vImageConvert_RGBFFFtoPlanarF()](https://developer.apple.com/documentation/accelerate/1533181-vimageconvert_rgbffftoplanarf)Added [vImageFlatten_ARGB8888ToRGB888()](https://developer.apple.com/documentation/accelerate/1533019-vimageflatten_argb8888torgb888)Added [vImageFlatten_ARGBFFFFToRGBFFF()](https://developer.apple.com/documentation/accelerate/1533210-vimageflatten_argbfffftorgbfff)Added [vImageOverwriteChannelsWithPixel_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533206-vimageoverwritechannelswithpixel)Added [vImageOverwriteChannelsWithPixel_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533111-vimageoverwritechannelswithpixel)Added [vImageOverwriteChannelsWithScalar_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533141-vimageoverwritechannelswithscala)Added [vImageOverwriteChannelsWithScalar_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533055-vimageoverwritechannelswithscala)Added [vImageOverwriteChannelsWithScalar_Planar8()](https://developer.apple.com/documentation/accelerate/1533034-vimageoverwritechannelswithscala)Added [vImageOverwriteChannelsWithScalar_PlanarF()](https://developer.apple.com/documentation/accelerate/1533174-vimageoverwritechannelswithscala)Added [vImageOverwriteChannels_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533120-vimageoverwritechannels_argb8888)Added [vImageOverwriteChannels_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533088-vimageoverwritechannels_argbffff)Added [vImagePermuteChannels_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533241-vimagepermutechannels_argb8888)Added [vImagePermuteChannels_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533266-vimagepermutechannels_argbffff)Added [vImageSelectChannels_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533096-vimageselectchannels_argb8888)Added [vImageSelectChannels_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1533155-vimageselectchannels_argbffff)Added [vImageTableLookUp_ARGB8888()](https://developer.apple.com/documentation/accelerate/1533201-vimagetablelookup_argb8888)Added [vImageTableLookUp_Planar8()](https://developer.apple.com/documentation/accelerate/1533167-vimagetablelookup_planar8)Convolution.hAdded #def VIMAGE_CONVOLUTION_HAdded [vImageBoxConvolve_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515945-vimageboxconvolve_argb8888)Added [vImageBoxConvolve_Planar8()](https://developer.apple.com/documentation/accelerate/1515941-vimageboxconvolve_planar8)Added [vImageConvolveMultiKernel_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515930-vimageconvolvemultikernel_argb88)Added [vImageConvolveMultiKernel_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1515931-vimageconvolvemultikernel_argbff)Added [vImageConvolveWithBias_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515933-vimageconvolvewithbias_argb8888)Added [vImageConvolveWithBias_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1515924-vimageconvolvewithbias_argbffff)Added [vImageConvolveWithBias_Planar8()](https://developer.apple.com/documentation/accelerate/1515922-vimageconvolvewithbias_planar8)Added [vImageConvolveWithBias_PlanarF()](https://developer.apple.com/documentation/accelerate/1515937-vimageconvolvewithbias_planarf)Added [vImageConvolve_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515923-vimageconvolve_argb8888)Added [vImageConvolve_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1515929-vimageconvolve_argbffff)Added [vImageConvolve_Planar8()](https://developer.apple.com/documentation/accelerate/1515925-vimageconvolve_planar8)Added [vImageConvolve_PlanarF()](https://developer.apple.com/documentation/accelerate/1515936-vimageconvolve_planarf)Added [vImageRichardsonLucyDeConvolve_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515928-vimagerichardsonlucydeconvolve_a)Added [vImageRichardsonLucyDeConvolve_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1515927-vimagerichardsonlucydeconvolve_a)Added [vImageRichardsonLucyDeConvolve_Planar8()](https://developer.apple.com/documentation/accelerate/1515943-vimagerichardsonlucydeconvolve_p)Added [vImageRichardsonLucyDeConvolve_PlanarF()](https://developer.apple.com/documentation/accelerate/1515932-vimagerichardsonlucydeconvolve_p)Added [vImageTentConvolve_ARGB8888()](https://developer.apple.com/documentation/accelerate/1515935-vimagetentconvolve_argb8888)Added [vImageTentConvolve_Planar8()](https://developer.apple.com/documentation/accelerate/1515934-vimagetentconvolve_planar8)Geometry.hAdded #def VIMAGE_GEOMETRY_HAdded [kRotate0DegreesClockwise](https://developer.apple.com/documentation/accelerate/1509228-rotation_constants/krotate0degreesclockwise)Added [kRotate0DegreesCounterClockwise](https://developer.apple.com/documentation/accelerate/1509228-rotation_constants/krotate0degreescounterclockwise)Added [kRotate180DegreesClockwise](https://developer.apple.com/documentation/accelerate/krotate180degreesclockwise)Added [kRotate180DegreesCounterClockwise](https://developer.apple.com/documentation/accelerate/krotate180degreescounterclockwise)Added [kRotate270DegreesClockwise](https://developer.apple.com/documentation/accelerate/1509228-rotation_constants/krotate270degreesclockwise)Added [kRotate270DegreesCounterClockwise](https://developer.apple.com/documentation/accelerate/krotate270degreescounterclockwise)Added [kRotate90DegreesClockwise](https://developer.apple.com/documentation/accelerate/krotate90degreesclockwise)Added [kRotate90DegreesCounterClockwise](https://developer.apple.com/documentation/accelerate/krotate90degreescounterclockwise)Added [vImageAffineWarpCG_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509276-vimageaffinewarpcg_argb8888) (no architecture available)Added [vImageAffineWarpCG_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509263-vimageaffinewarpcg_argbffff) (no architecture available)Added [vImageAffineWarpCG_Planar8()](https://developer.apple.com/documentation/accelerate/1509190-vimageaffinewarpcg_planar8) (no architecture available)Added [vImageAffineWarpCG_PlanarF()](https://developer.apple.com/documentation/accelerate/1509193-vimageaffinewarpcg_planarf) (no architecture available)Added [vImageAffineWarpD_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509211-vimageaffinewarpd_argb8888)Added [vImageAffineWarpD_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509214-vimageaffinewarpd_argbffff)Added [vImageAffineWarpD_Planar8()](https://developer.apple.com/documentation/accelerate/1509152-vimageaffinewarpd_planar8)Added [vImageAffineWarpD_PlanarF()](https://developer.apple.com/documentation/accelerate/1509209-vimageaffinewarpd_planarf)Added [vImageAffineWarp_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509182-vimageaffinewarp_argb8888)Added [vImageAffineWarp_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509245-vimageaffinewarp_argbffff)Added [vImageAffineWarp_Planar8()](https://developer.apple.com/documentation/accelerate/1509257-vimageaffinewarp_planar8)Added [vImageAffineWarp_PlanarF()](https://developer.apple.com/documentation/accelerate/1509226-vimageaffinewarp_planarf)Added [vImageDestroyResamplingFilter()](https://developer.apple.com/documentation/accelerate/1509201-vimagedestroyresamplingfilter)Added [vImageGetResamplingFilterSize()](https://developer.apple.com/documentation/accelerate/1509252-vimagegetresamplingfiltersize)Added [vImageHorizontalReflect_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509199-vimagehorizontalreflect_argb8888)Added [vImageHorizontalReflect_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509184-vimagehorizontalreflect_argbffff)Added [vImageHorizontalReflect_Planar8()](https://developer.apple.com/documentation/accelerate/1509259-vimagehorizontalreflect_planar8)Added [vImageHorizontalReflect_PlanarF()](https://developer.apple.com/documentation/accelerate/1509250-vimagehorizontalreflect_planarf)Added [vImageHorizontalShearD_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509178-vimagehorizontalsheard_argb8888)Added [vImageHorizontalShearD_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509269-vimagehorizontalsheard_argbffff)Added [vImageHorizontalShearD_Planar8()](https://developer.apple.com/documentation/accelerate/1509221-vimagehorizontalsheard_planar8)Added [vImageHorizontalShearD_PlanarF()](https://developer.apple.com/documentation/accelerate/1509234-vimagehorizontalsheard_planarf)Added [vImageHorizontalShear_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509237-vimagehorizontalshear_argb8888)Added [vImageHorizontalShear_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509273-vimagehorizontalshear_argbffff)Added [vImageHorizontalShear_Planar8()](https://developer.apple.com/documentation/accelerate/1509213-vimagehorizontalshear_planar8)Added [vImageHorizontalShear_PlanarF()](https://developer.apple.com/documentation/accelerate/1509148-vimagehorizontalshear_planarf)Added [vImageNewResamplingFilter()](https://developer.apple.com/documentation/accelerate/1509216-vimagenewresamplingfilter)Added [vImageNewResamplingFilterForFunctionUsingBuffer()](https://developer.apple.com/documentation/accelerate/1509217-vimagenewresamplingfilterforfunc)Added [vImageRotate90_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509188-vimagerotate90_argb8888)Added [vImageRotate90_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509262-vimagerotate90_argbffff)Added [vImageRotate90_Planar8()](https://developer.apple.com/documentation/accelerate/1509176-vimagerotate90_planar8)Added [vImageRotate90_PlanarF()](https://developer.apple.com/documentation/accelerate/1509242-vimagerotate90_planarf)Added [vImageRotate_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509284-vimagerotate_argb8888)Added [vImageRotate_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509192-vimagerotate_argbffff)Added [vImageRotate_Planar8()](https://developer.apple.com/documentation/accelerate/1509288-vimagerotate_planar8)Added [vImageRotate_PlanarF()](https://developer.apple.com/documentation/accelerate/1509203-vimagerotate_planarf)Added [vImageScale_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509266-vimagescale_argb8888)Added [vImageScale_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509208-vimagescale_argbffff)Added [vImageScale_Planar8()](https://developer.apple.com/documentation/accelerate/1509285-vimagescale_planar8)Added [vImageScale_PlanarF()](https://developer.apple.com/documentation/accelerate/1509219-vimagescale_planarf)Added [vImageVerticalReflect_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509157-vimageverticalreflect_argb8888)Added [vImageVerticalReflect_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509170-vimageverticalreflect_argbffff)Added [vImageVerticalReflect_Planar8()](https://developer.apple.com/documentation/accelerate/1509160-vimageverticalreflect_planar8)Added [vImageVerticalReflect_PlanarF()](https://developer.apple.com/documentation/accelerate/1509168-vimageverticalreflect_planarf)Added [vImageVerticalShearD_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509222-vimageverticalsheard_argb8888)Added [vImageVerticalShearD_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509254-vimageverticalsheard_argbffff)Added [vImageVerticalShearD_Planar8()](https://developer.apple.com/documentation/accelerate/1509240-vimageverticalsheard_planar8)Added [vImageVerticalShearD_PlanarF()](https://developer.apple.com/documentation/accelerate/1509277-vimageverticalsheard_planarf)Added [vImageVerticalShear_ARGB8888()](https://developer.apple.com/documentation/accelerate/1509256-vimageverticalshear_argb8888)Added [vImageVerticalShear_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1509261-vimageverticalshear_argbffff)Added [vImageVerticalShear_Planar8()](https://developer.apple.com/documentation/accelerate/1509165-vimageverticalshear_planar8)Added [vImageVerticalShear_PlanarF()](https://developer.apple.com/documentation/accelerate/1509289-vimageverticalshear_planarf)Histogram.hAdded #def VIMAGE_HISTOGRAM_HAdded [vImageContrastStretch_ARGB8888()](https://developer.apple.com/documentation/accelerate/1546811-vimagecontraststretch_argb8888)Added [vImageContrastStretch_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1545737-vimagecontraststretch_argbffff)Added [vImageContrastStretch_Planar8()](https://developer.apple.com/documentation/accelerate/1546840-vimagecontraststretch_planar8)Added [vImageContrastStretch_PlanarF()](https://developer.apple.com/documentation/accelerate/1545756-vimagecontraststretch_planarf)Added [vImageEndsInContrastStretch_ARGB8888()](https://developer.apple.com/documentation/accelerate/1545003-vimageendsincontraststretch_argb)Added [vImageEndsInContrastStretch_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1546618-vimageendsincontraststretch_argb)Added [vImageEndsInContrastStretch_Planar8()](https://developer.apple.com/documentation/accelerate/1544335-vimageendsincontraststretch_plan)Added [vImageEndsInContrastStretch_PlanarF()](https://developer.apple.com/documentation/accelerate/1546610-vimageendsincontraststretch_plan)Added [vImageEqualization_ARGB8888()](https://developer.apple.com/documentation/accelerate/1546860-vimageequalization_argb8888)Added [vImageEqualization_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1545373-vimageequalization_argbffff)Added [vImageEqualization_Planar8()](https://developer.apple.com/documentation/accelerate/1545340-vimageequalization_planar8)Added [vImageEqualization_PlanarF()](https://developer.apple.com/documentation/accelerate/1546654-vimageequalization_planarf)Added [vImageHistogramCalculation_ARGB8888()](https://developer.apple.com/documentation/accelerate/1545743-vimagehistogramcalculation_argb8)Added [vImageHistogramCalculation_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1545752-vimagehistogramcalculation_argbf)Added [vImageHistogramCalculation_Planar8()](https://developer.apple.com/documentation/accelerate/1544353-vimagehistogramcalculation_plana)Added [vImageHistogramCalculation_PlanarF()](https://developer.apple.com/documentation/accelerate/1545392-vimagehistogramcalculation_plana)Added [vImageHistogramSpecification_ARGB8888()](https://developer.apple.com/documentation/accelerate/1546963-vimagehistogramspecification_arg)Added [vImageHistogramSpecification_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1546602-vimagehistogramspecification_arg)Added [vImageHistogramSpecification_Planar8()](https://developer.apple.com/documentation/accelerate/1545851-vimagehistogramspecification_pla)Added [vImageHistogramSpecification_PlanarF()](https://developer.apple.com/documentation/accelerate/1545709-vimagehistogramspecification_pla)Morphology.hAdded #def VIMAGE_MORPHOLOGY_HAdded [vImageDilate_ARGB8888()](https://developer.apple.com/documentation/accelerate/1545760-vimagedilate_argb8888)Added [vImageDilate_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1545570-vimagedilate_argbffff)Added [vImageDilate_Planar8()](https://developer.apple.com/documentation/accelerate/1545869-vimagedilate_planar8)Added [vImageDilate_PlanarF()](https://developer.apple.com/documentation/accelerate/1547004-vimagedilate_planarf)Added [vImageErode_ARGB8888()](https://developer.apple.com/documentation/accelerate/1546816-vimageerode_argb8888)Added [vImageErode_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1546484-vimageerode_argbffff)Added [vImageErode_Planar8()](https://developer.apple.com/documentation/accelerate/1545856-vimageerode_planar8)Added [vImageErode_PlanarF()](https://developer.apple.com/documentation/accelerate/1546818-vimageerode_planarf)Added [vImageMax_ARGB8888()](https://developer.apple.com/documentation/accelerate/1546943-vimagemax_argb8888)Added [vImageMax_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1545640-vimagemax_argbffff)Added [vImageMax_Planar8()](https://developer.apple.com/documentation/accelerate/1544630-vimagemax_planar8)Added [vImageMax_PlanarF()](https://developer.apple.com/documentation/accelerate/1546665-vimagemax_planarf)Added [vImageMin_ARGB8888()](https://developer.apple.com/documentation/accelerate/1546276-vimagemin_argb8888)Added [vImageMin_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1545797-vimagemin_argbffff)Added [vImageMin_Planar8()](https://developer.apple.com/documentation/accelerate/1544288-vimagemin_planar8)Added [vImageMin_PlanarF()](https://developer.apple.com/documentation/accelerate/1545440-vimagemin_planarf)Transform.hAdded #def VIMAGE_TRANSFORM_HAdded [kvImageGamma_11_over_5_half_precision](https://developer.apple.com/documentation/accelerate/kvimagegamma_11_over_5_half_precision)Added [kvImageGamma_11_over_9_half_precision](https://developer.apple.com/documentation/accelerate/kvimagegamma_11_over_9_half_precision)Added [kvImageGamma_5_over_11_half_precision](https://developer.apple.com/documentation/accelerate/kvimagegamma_5_over_11_half_precision)Added [kvImageGamma_5_over_9_half_precision](https://developer.apple.com/documentation/accelerate/kvimagegamma_5_over_9_half_precision)Added [kvImageGamma_9_over_11_half_precision](https://developer.apple.com/documentation/accelerate/1584480-gamma_function_types/kvimagegamma_9_over_11_half_precision)Added [kvImageGamma_9_over_5_half_precision](https://developer.apple.com/documentation/accelerate/kvimagegamma_9_over_5_half_precision)Added [kvImageGamma_BT709_forward_half_precision](https://developer.apple.com/documentation/accelerate/kvimagegamma_bt709_forward_half_precision)Added [kvImageGamma_BT709_reverse_half_precision](https://developer.apple.com/documentation/accelerate/1584480-gamma_function_types/kvimagegamma_bt709_reverse_half_precision)Added [kvImageGamma_UseGammaValue](https://developer.apple.com/documentation/accelerate/kvimagegamma_usegammavalue)Added [kvImageGamma_UseGammaValue_half_precision](https://developer.apple.com/documentation/accelerate/1584480-gamma_function_types/kvimagegamma_usegammavalue_half_precision)Added [kvImageGamma_sRGB_forward_half_precision](https://developer.apple.com/documentation/accelerate/1584480-gamma_function_types/kvimagegamma_srgb_forward_half_precision)Added [kvImageGamma_sRGB_reverse_half_precision](https://developer.apple.com/documentation/accelerate/kvimagegamma_srgb_reverse_half_precision)Added [vImageCreateGammaFunction()](https://developer.apple.com/documentation/accelerate/1545896-vimagecreategammafunction)Added [vImageDestroyGammaFunction()](https://developer.apple.com/documentation/accelerate/1546971-vimagedestroygammafunction)Added [vImageGamma_Planar8toPlanarF()](https://developer.apple.com/documentation/accelerate/1546987-vimagegamma_planar8toplanarf)Added [vImageGamma_PlanarF()](https://developer.apple.com/documentation/accelerate/1546983-vimagegamma_planarf)Added [vImageGamma_PlanarFtoPlanar8()](https://developer.apple.com/documentation/accelerate/1545497-vimagegamma_planarftoplanar8)Added [vImageInterpolatedLookupTable_PlanarF()](https://developer.apple.com/documentation/accelerate/1545093-vimageinterpolatedlookuptable_pl)Added [vImageLookupTable_Planar8toPlanarF()](https://developer.apple.com/documentation/accelerate/1546994-vimagelookuptable_planar8toplana)Added [vImageLookupTable_PlanarFtoPlanar8()](https://developer.apple.com/documentation/accelerate/1544412-vimagelookuptable_planarftoplana)Added [vImageMatrixMultiply_ARGB8888()](https://developer.apple.com/documentation/accelerate/1546176-vimagematrixmultiply_argb8888)Added [vImageMatrixMultiply_ARGBFFFF()](https://developer.apple.com/documentation/accelerate/1545863-vimagematrixmultiply_argbffff)Added [vImageMatrixMultiply_Planar8()](https://developer.apple.com/documentation/accelerate/1544331-vimagematrixmultiply_planar8)Added [vImageMatrixMultiply_PlanarF()](https://developer.apple.com/documentation/accelerate/1545687-vimagematrixmultiply_planarf)Added [vImagePiecewisePolynomial_Planar8toPlanarF()](https://developer.apple.com/documentation/accelerate/1546252-vimagepiecewisepolynomial_planar)Added [vImagePiecewisePolynomial_PlanarF()](https://developer.apple.com/documentation/accelerate/1546813-vimagepiecewisepolynomial_planar)Added [vImagePiecewisePolynomial_PlanarFtoPlanar8()](https://developer.apple.com/documentation/accelerate/1546201-vimagepiecewisepolynomial_planar)Added [vImagePiecewiseRational_PlanarF()](https://developer.apple.com/documentation/accelerate/1545831-vimagepiecewiserational_planarf)vDSP.hAdded [vDSP_distancesq()](https://developer.apple.com/documentation/accelerate/1450619-vdsp_distancesq)vForce.hAdded [vvacos()](https://developer.apple.com/documentation/accelerate/1470383-vvacos)Added [vvacosf()](https://developer.apple.com/documentation/accelerate/1470367-vvacosf)Added [vvacosh()](https://developer.apple.com/documentation/accelerate/1470369-vvacosh)Added [vvacoshf()](https://developer.apple.com/documentation/accelerate/1470430-vvacoshf)Added [vvasin()](https://developer.apple.com/documentation/accelerate/1470489-vvasin)Added [vvasinf()](https://developer.apple.com/documentation/accelerate/1470354-vvasinf)Added [vvasinh()](https://developer.apple.com/documentation/accelerate/1470454-vvasinh)Added [vvasinhf()](https://developer.apple.com/documentation/accelerate/1470466-vvasinhf)Added [vvatan()](https://developer.apple.com/documentation/accelerate/1470450-vvatan)Added [vvatan2()](https://developer.apple.com/documentation/accelerate/1470446-vvatan2)Added [vvatan2f()](https://developer.apple.com/documentation/accelerate/1470387-vvatan2f)Added [vvatanf()](https://developer.apple.com/documentation/accelerate/1470464-vvatanf)Added [vvatanh()](https://developer.apple.com/documentation/accelerate/1470506-vvatanh)Added [vvatanhf()](https://developer.apple.com/documentation/accelerate/1470418-vvatanhf)Added [vvceil()](https://developer.apple.com/documentation/accelerate/1470448-vvceil)Added [vvceilf()](https://developer.apple.com/documentation/accelerate/1470395-vvceilf)Added [vvcopysign()](https://developer.apple.com/documentation/accelerate/1470348-vvcopysign)Added [vvcopysignf()](https://developer.apple.com/documentation/accelerate/1470475-vvcopysignf)Added [vvcos()](https://developer.apple.com/documentation/accelerate/1470471-vvcos)Added [vvcosf()](https://developer.apple.com/documentation/accelerate/1470444-vvcosf)Added [vvcosh()](https://developer.apple.com/documentation/accelerate/1470473-vvcosh)Added [vvcoshf()](https://developer.apple.com/documentation/accelerate/1470428-vvcoshf)Added [vvcosisin()](https://developer.apple.com/documentation/accelerate/1470504-vvcosisin)Added [vvcosisinf()](https://developer.apple.com/documentation/accelerate/1470362-vvcosisinf)Added [vvcospi()](https://developer.apple.com/documentation/accelerate/1470391-vvcospi)Added [vvcospif()](https://developer.apple.com/documentation/accelerate/1470479-vvcospif)Added [vvdiv()](https://developer.apple.com/documentation/accelerate/1470406-vvdiv)Added [vvdivf()](https://developer.apple.com/documentation/accelerate/1470436-vvdivf)Added [vvexp()](https://developer.apple.com/documentation/accelerate/1470381-vvexp)Added [vvexp2()](https://developer.apple.com/documentation/accelerate/1470358-vvexp2)Added [vvexp2f()](https://developer.apple.com/documentation/accelerate/1470512-vvexp2f)Added [vvexpf()](https://developer.apple.com/documentation/kernel/1532176-vvexpf)Added [vvexpm1()](https://developer.apple.com/documentation/accelerate/1470389-vvexpm1)Added [vvexpm1f()](https://developer.apple.com/documentation/accelerate/1470350-vvexpm1f)Added [vvfabs()](https://developer.apple.com/documentation/accelerate/1470370-vvfabs)Added [vvfabsf()](https://developer.apple.com/documentation/accelerate/1470393-vvfabsf)Added [vvfloor()](https://developer.apple.com/documentation/accelerate/1470485-vvfloor)Added [vvfloorf()](https://developer.apple.com/documentation/accelerate/1470452-vvfloorf)Added [vvfmod()](https://developer.apple.com/documentation/accelerate/1470379-vvfmod)Added [vvfmodf()](https://developer.apple.com/documentation/accelerate/1470502-vvfmodf)Added [vvint()](https://developer.apple.com/documentation/accelerate/1470514-vvint)Added [vvintf()](https://developer.apple.com/documentation/accelerate/1470385-vvintf)Added [vvlog()](https://developer.apple.com/documentation/accelerate/1470458-vvlog)Added [vvlog10()](https://developer.apple.com/documentation/accelerate/1470424-vvlog10)Added [vvlog10f()](https://developer.apple.com/documentation/accelerate/1470410-vvlog10f)Added [vvlog1p()](https://developer.apple.com/documentation/accelerate/1470377-vvlog1p)Added [vvlog1pf()](https://developer.apple.com/documentation/accelerate/1470422-vvlog1pf)Added [vvlog2()](https://developer.apple.com/documentation/accelerate/1470420-vvlog2)Added [vvlog2f()](https://developer.apple.com/documentation/accelerate/1470416-vvlog2f)Added [vvlogb()](https://developer.apple.com/documentation/accelerate/1470432-vvlogb)Added [vvlogbf()](https://developer.apple.com/documentation/accelerate/1470442-vvlogbf)Added [vvlogf()](https://developer.apple.com/documentation/accelerate/1470373-vvlogf)Added [vvnextafter()](https://developer.apple.com/documentation/accelerate/1470487-vvnextafter)Added [vvnextafterf()](https://developer.apple.com/documentation/accelerate/1470375-vvnextafterf)Added [vvnint()](https://developer.apple.com/documentation/accelerate/1470402-vvnint)Added [vvnintf()](https://developer.apple.com/documentation/accelerate/1470438-vvnintf)Added [vvpow()](https://developer.apple.com/documentation/accelerate/1470399-vvpow)Added [vvpowf()](https://developer.apple.com/documentation/accelerate/1470360-vvpowf)Added [vvrec()](https://developer.apple.com/documentation/accelerate/1470412-vvrec)Added [vvrecf()](https://developer.apple.com/documentation/accelerate/1470510-vvrecf)Added [vvremainder()](https://developer.apple.com/documentation/accelerate/1470456-vvremainder)Added [vvremainderf()](https://developer.apple.com/documentation/accelerate/1470483-vvremainderf)Added [vvrsqrt()](https://developer.apple.com/documentation/accelerate/1470498-vvrsqrt)Added [vvrsqrtf()](https://developer.apple.com/documentation/accelerate/1470434-vvrsqrtf)Added [vvsin()](https://developer.apple.com/documentation/accelerate/1470352-vvsin)Added [vvsincos()](https://developer.apple.com/documentation/accelerate/1470346-vvsincos)Added [vvsincosf()](https://developer.apple.com/documentation/accelerate/1470460-vvsincosf)Added [vvsinf()](https://developer.apple.com/documentation/accelerate/1470364-vvsinf)Added [vvsinh()](https://developer.apple.com/documentation/accelerate/1470426-vvsinh)Added [vvsinhf()](https://developer.apple.com/documentation/accelerate/1470401-vvsinhf)Added [vvsinpi()](https://developer.apple.com/documentation/accelerate/1470440-vvsinpi)Added [vvsinpif()](https://developer.apple.com/documentation/accelerate/1470414-vvsinpif)Added [vvsqrt()](https://developer.apple.com/documentation/accelerate/1470462-vvsqrt)Added [vvsqrtf()](https://developer.apple.com/documentation/accelerate/1470491-vvsqrtf)Added [vvtan()](https://developer.apple.com/documentation/accelerate/1470481-vvtan)Added [vvtanf()](https://developer.apple.com/documentation/accelerate/1470356-vvtanf)Added [vvtanh()](https://developer.apple.com/documentation/accelerate/1470408-vvtanh)Added [vvtanhf()](https://developer.apple.com/documentation/accelerate/1470496-vvtanhf)Added [vvtanpi()](https://developer.apple.com/documentation/accelerate/1470404-vvtanpi)Added [vvtanpif()](https://developer.apple.com/documentation/accelerate/1470469-vvtanpif)vImage.hAdded #def VIMAGE_HvImage_Types.hAdded [GammaFunction](https://developer.apple.com/documentation/accelerate/gammafunction)Added [Pixel_8](https://developer.apple.com/documentation/accelerate/pixel_8)Added [Pixel_8888](https://developer.apple.com/documentation/accelerate/pixel_8888)Added [Pixel_F](https://developer.apple.com/documentation/accelerate/pixel_f)Added [Pixel_FFFF](https://developer.apple.com/documentation/accelerate/pixel_ffff)Added [ResamplingFilter](https://developer.apple.com/documentation/accelerate/resamplingfilter)Added [#def VIMAGE_AFFINETRANSFORM_DOUBLE_IS_AVAILABLE](https://developer.apple.com/documentation/accelerate/vimage_affinetransform_double_is_available)Added #def VIMAGE_TYPES_HAdded [kvImageBackgroundColorFill](https://developer.apple.com/documentation/accelerate/kvimagebackgroundcolorfill)Added [kvImageBufferSizeMismatch](https://developer.apple.com/documentation/accelerate/1578972-error_codes/kvimagebuffersizemismatch)Added [kvImageCopyInPlace](https://developer.apple.com/documentation/accelerate/kvimagecopyinplace)Added [kvImageDoNotTile](https://developer.apple.com/documentation/accelerate/1578976-processing_flags/kvimagedonottile)Added [kvImageEdgeExtend](https://developer.apple.com/documentation/accelerate/1578976-processing_flags/kvimageedgeextend)Added [kvImageGetTempBufferSize](https://developer.apple.com/documentation/accelerate/1578976-processing_flags/kvimagegettempbuffersize)Added [kvImageHighQualityResampling](https://developer.apple.com/documentation/accelerate/1578976-processing_flags/kvimagehighqualityresampling)Added [kvImageInvalidEdgeStyle](https://developer.apple.com/documentation/accelerate/1578972-error_codes/kvimageinvalidedgestyle)Added [kvImageInvalidKernelSize](https://developer.apple.com/documentation/accelerate/1578972-error_codes/kvimageinvalidkernelsize)Added [kvImageInvalidOffset_X](https://developer.apple.com/documentation/accelerate/1578972-error_codes/kvimageinvalidoffset_x)Added [kvImageInvalidOffset_Y](https://developer.apple.com/documentation/accelerate/1578972-error_codes/kvimageinvalidoffset_y)Added [kvImageInvalidParameter](https://developer.apple.com/documentation/accelerate/1578972-error_codes/kvimageinvalidparameter)Added [kvImageLeaveAlphaUnchanged](https://developer.apple.com/documentation/accelerate/1578976-processing_flags/kvimageleavealphaunchanged)Added [kvImageMemoryAllocationError](https://developer.apple.com/documentation/accelerate/kvimagememoryallocationerror)Added [kvImageNoError](https://developer.apple.com/documentation/accelerate/kvimagenoerror)Added [kvImageNoFlags](https://developer.apple.com/documentation/accelerate/1578976-processing_flags/kvimagenoflags)Added [kvImageNullPointerArgument](https://developer.apple.com/documentation/accelerate/kvimagenullpointerargument)Added [kvImageRoiLargerThanInputBuffer](https://developer.apple.com/documentation/accelerate/1578972-error_codes/kvimageroilargerthaninputbuffer)Added [kvImageTruncateKernel](https://developer.apple.com/documentation/accelerate/1578976-processing_flags/kvimagetruncatekernel)Added [kvImageUnknownFlagsBit](https://developer.apple.com/documentation/accelerate/1578972-error_codes/kvimageunknownflagsbit)Added [vImagePixelCount](https://developer.apple.com/documentation/accelerate/vimagepixelcount)Added [vImage_AffineTransform](https://developer.apple.com/documentation/accelerate/vimage_affinetransform)Added [vImage_AffineTransform_Double](https://developer.apple.com/documentation/accelerate/vimage_affinetransform_double)Added [vImage_Buffer](https://developer.apple.com/documentation/accelerate/vimage_buffer)Added [vImage_CGAffineTransform](https://developer.apple.com/documentation/accelerate/vimage_cgaffinetransform) (no architecture available)Added [vImage_Error](https://developer.apple.com/documentation/accelerate/vimage_error)Added [vImage_Flags](https://developer.apple.com/documentation/accelerate/vimage_flags)

## Accounts

ACAccount.hAdded [ACAccount](https://developer.apple.com/documentation/accounts/acaccount)Added [ACAccount.accountDescription](https://developer.apple.com/documentation/accounts/acaccount/1543836-accountdescription)Added [ACAccount.accountType](https://developer.apple.com/documentation/accounts/acaccount/1543805-accounttype)Added [ACAccount.credential](https://developer.apple.com/documentation/accounts/acaccount/1543779-credential)Added [ACAccount.identifier](https://developer.apple.com/documentation/accounts/acaccount/1543840-identifier)Added [-[ACAccount initWithAccountType:]](https://developer.apple.com/documentation/accounts/acaccount/1543781-initwithaccounttype)Added [ACAccount.username](https://developer.apple.com/documentation/accounts/acaccount/1543839-username)ACAccountCredential.hAdded [ACAccountCredential](https://developer.apple.com/documentation/accounts/acaccountcredential)Added [-[ACAccountCredential initWithOAuthToken:tokenSecret:]](https://developer.apple.com/documentation/accounts/acaccountcredential/1507896-initwithoauthtoken)ACAccountStore.hAdded [ACAccountStore](https://developer.apple.com/documentation/accounts/acaccountstore)Added [-[ACAccountStore accountTypeWithAccountTypeIdentifier:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493967-accounttype)Added [-[ACAccountStore accountWithIdentifier:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493947-account)Added [ACAccountStore.accounts](https://developer.apple.com/documentation/accounts/acaccountstore/1493961-accounts)Added [-[ACAccountStore accountsWithAccountType:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493942-accountswithaccounttype)Added [-[ACAccountStore requestAccessToAccountsWithType:withCompletionHandler:]](https://developer.apple.com/documentation/accounts/acaccountstore/1624250-requestaccesstoaccountswithtype)Added [-[ACAccountStore saveAccount:withCompletionHandler:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493957-saveaccount)Added [ACAccountStoreDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1493946-acaccountstoredidchange)Added [ACAccountStoreRequestAccessCompletionHandler](https://developer.apple.com/documentation/accounts/acaccountstorerequestaccesscompletionhandler)Added [ACAccountStoreSaveCompletionHandler](https://developer.apple.com/documentation/accounts/acaccountstoresavecompletionhandler)ACAccountType.hAdded [ACAccountType](https://developer.apple.com/documentation/accounts/acaccounttype)Added [ACAccountType.accessGranted](https://developer.apple.com/documentation/accounts/acaccounttype/1543838-accessgranted)Added [ACAccountType.accountTypeDescription](https://developer.apple.com/documentation/accounts/acaccounttype/1543834-accounttypedescription)Added [ACAccountType.identifier](https://developer.apple.com/documentation/accounts/acaccounttype/1543833-identifier)Added [ACAccountTypeIdentifierTwitter](https://developer.apple.com/documentation/accounts/acaccounttypeidentifiertwitter)ACError.hAdded [ACErrorAccountAlreadyExists](https://developer.apple.com/documentation/accounts/acerrorcode/acerroraccountalreadyexists)Added [ACErrorAccountAuthenticationFailed](https://developer.apple.com/documentation/accounts/acerrorcode/acerroraccountauthenticationfailed)Added [ACErrorAccountMissingRequiredProperty](https://developer.apple.com/documentation/accounts/acerrorcode/acerroraccountmissingrequiredproperty)Added [ACErrorAccountNotFound](https://developer.apple.com/documentation/accounts/acerrorcode/acerroraccountnotfound)Added [ACErrorAccountTypeInvalid](https://developer.apple.com/documentation/accounts/acerroraccounttypeinvalid)Added [ACErrorCode](https://developer.apple.com/documentation/accounts/acerrorcode)Added [ACErrorDomain](https://developer.apple.com/documentation/accounts/acerrordomain)Added [ACErrorPermissionDenied](https://developer.apple.com/documentation/accounts/acerrorpermissiondenied)Added [ACErrorUnknown](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorunknown)AccountsDefines.hAdded #def ACCOUNTS_CLASS_AVAILABLEAdded #def ACCOUNTS_EXTERN

## AddressBook

ABPerson.hAdded [ABPersonCreatePeopleInSourceWithVCardRepresentation()](https://developer.apple.com/documentation/addressbook/1619772-abpersoncreatepeopleinsourcewith)Added [ABPersonCreateVCardRepresentationWithPeople()](https://developer.apple.com/documentation/addressbook/1619779-abpersoncreatevcardrepresentatio)Added [kABPersonInstantMessageServiceFacebook](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageservicefacebook)Added [kABPersonInstantMessageServiceGaduGadu](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageservicegadugadu)Added [kABPersonInstantMessageServiceGoogleTalk](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageservicegoogletalk)Added [kABPersonInstantMessageServiceQQ](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageserviceqq)Added [kABPersonInstantMessageServiceSkype](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageserviceskype)Added [kABPersonPhoneOtherFAXLabel](https://developer.apple.com/documentation/addressbook/kabpersonphoneotherfaxlabel)Added [kABPersonSocialProfileProperty](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileproperty)Added [kABPersonSocialProfileServiceFacebook](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicefacebook)Added [kABPersonSocialProfileServiceFlickr](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileserviceflickr)Added [kABPersonSocialProfileServiceGameCenter](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicegamecenter)Added [kABPersonSocialProfileServiceKey](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicekey)Added [kABPersonSocialProfileServiceLinkedIn](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicelinkedin)Added [kABPersonSocialProfileServiceMyspace](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicemyspace)Added [kABPersonSocialProfileServiceTwitter](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicetwitter)Added [kABPersonSocialProfileURLKey](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileurlkey)Added [kABPersonSocialProfileUserIdentifierKey](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileuseridentifierkey)Added [kABPersonSocialProfileUsernameKey](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileusernamekey)ABRecord.hAdded [kABSourceType](https://developer.apple.com/documentation/addressbook/kabsourcetype)

## AddressBookUI

ABPersonViewController.hAdded [ABPersonViewController.allowsActions](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622201-allowsactions)

## AssetsLibrary

ALAsset.hAdded [-[ALAsset aspectRatioThumbnail]](https://developer.apple.com/documentation/assetslibrary/alasset/1615872-aspectratiothumbnail)Added [ALAsset.editable](https://developer.apple.com/documentation/assetslibrary/alasset/1615867-iseditable)Added [ALAsset.originalAsset](https://developer.apple.com/documentation/assetslibrary/alasset/1615857-originalasset)Added [-[ALAsset setImageData:metadata:completionBlock:]](https://developer.apple.com/documentation/assetslibrary/alasset/1615874-setimagedata)Added [-[ALAsset setVideoAtPath:completionBlock:]](https://developer.apple.com/documentation/assetslibrary/alasset/1615880-setvideoatpath)Added [-[ALAsset writeModifiedImageDataToSavedPhotosAlbum:metadata:completionBlock:]](https://developer.apple.com/documentation/assetslibrary/alasset/1615863-writemodifiedimagedatatosavedpho)Added [-[ALAsset writeModifiedVideoAtPathToSavedPhotosAlbum:completionBlock:]](https://developer.apple.com/documentation/assetslibrary/alasset/1615878-writemodifiedvideoatpath)ALAssetRepresentation.hAdded [-[ALAssetRepresentation filename]](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617857-filename)ALAssetsGroup.hAdded [-[ALAssetsGroup addAsset:]](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621964-addasset)Added [ALAssetsGroup.editable](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621969-editable)Added [ALAssetsGroupPropertyURL](https://developer.apple.com/documentation/assetslibrary/alassetsgrouppropertyurl)ALAssetsLibrary.hAdded [-[ALAssetsLibrary addAssetsGroupAlbumWithName:resultBlock:failureBlock:]](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617872-addassetsgroupalbumwithname)Added [-[ALAssetsLibrary groupForURL:resultBlock:failureBlock:]](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617907-groupforurl)Added [ALAssetsGroupPhotoStream](https://developer.apple.com/documentation/assetslibrary/1617883-types_of_asset/alassetsgroupphotostream)Added [ALAssetsLibraryGroupResultBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibrarygroupresultblock)

## AudioToolbox

AudioConverter.hAdded [AudioConverterConvertComplexBuffer()](https://developer.apple.com/documentation/audiotoolbox/1502473-audioconverterconvertcomplexbuff)AudioFile.hAdded [kAudioFilePropertyAlbumArtwork](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyalbumartwork)AudioQueue.hAdded [kAudioQueueErr_RecordUnderrun](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_recordunderrun)Added [kAudioQueueProperty_ConverterError](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_convertererror)AudioServices.hAdded [kAudioSessionInputRoute_BluetoothHFP](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_bluetoothhfp)Added [kAudioSessionInputRoute_BuiltInMic](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_builtinmic)Added [kAudioSessionInputRoute_HeadsetMic](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_headsetmic)Added [kAudioSessionInputRoute_LineIn](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_linein)Added [kAudioSessionInputRoute_USBAudio](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninputroute_usbaudio)Added [kAudioSessionMode_Default](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionmode_default)Added [kAudioSessionMode_GameChat](https://developer.apple.com/documentation/audiotoolbox/1618405-audio_session_modes/kaudiosessionmode_gamechat)Added [kAudioSessionMode_Measurement](https://developer.apple.com/documentation/audiotoolbox/1618405-audio_session_modes/kaudiosessionmode_measurement)Added [kAudioSessionMode_VideoRecording](https://developer.apple.com/documentation/audiotoolbox/1618405-audio_session_modes/kaudiosessionmode_videorecording)Added [kAudioSessionMode_VoiceChat](https://developer.apple.com/documentation/audiotoolbox/1618405-audio_session_modes/kaudiosessionmode_voicechat)Added [kAudioSessionOutputRoute_AirPlay](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_airplay)Added [kAudioSessionOutputRoute_BluetoothA2DP](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_bluetootha2dp)Added [kAudioSessionOutputRoute_BluetoothHFP](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_bluetoothhfp)Added [kAudioSessionOutputRoute_BuiltInReceiver](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_builtinreceiver)Added [kAudioSessionOutputRoute_BuiltInSpeaker](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_builtinspeaker)Added [kAudioSessionOutputRoute_HDMI](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_hdmi)Added [kAudioSessionOutputRoute_Headphones](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_headphones)Added [kAudioSessionOutputRoute_LineOut](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_lineout)Added [kAudioSessionOutputRoute_USBAudio](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionoutputroute_usbaudio)Added [kAudioSessionProperty_AudioRouteDescription](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_audioroutedescription)Added [kAudioSessionProperty_InputGainAvailable](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_inputgainavailable)Added [kAudioSessionProperty_InputGainScalar](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_inputgainscalar)Added [kAudioSessionProperty_InputSource](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_inputsource)Added [kAudioSessionProperty_InputSources](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_inputsources)Added [kAudioSessionProperty_Mode](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_mode)Added [kAudioSessionProperty_OutputDestination](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_outputdestination)Added [kAudioSessionProperty_OutputDestinations](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_outputdestinations)Added [kAudioSession_AudioRouteChangeKey_CurrentRouteDescription](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutechangekey_currentroutedescription)Added [kAudioSession_AudioRouteChangeKey_PreviousRouteDescription](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutechangekey_previousroutedescription)Added [kAudioSession_AudioRouteKey_Inputs](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutekey_inputs)Added [kAudioSession_AudioRouteKey_Outputs](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutekey_outputs)Added [kAudioSession_AudioRouteKey_Type](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutekey_type)Added [kAudioSession_InputSourceKey_Description](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_inputsourcekey_description)Added [kAudioSession_InputSourceKey_ID](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_inputsourcekey_id)Added [kAudioSession_OutputDestinationKey_Description](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_outputdestinationkey_description)Added [kAudioSession_OutputDestinationKey_ID](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_outputdestinationkey_id)Added [kAudioSession_RouteChangeKey_Reason](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_routechangekey_reason)CAFFile.hAdded #def ATTRIBUTE_PACKEDAdded ATTRIBUTE_PACKED (no architecture available)Added [CAFAudioDescription](https://developer.apple.com/documentation/audiotoolbox/cafaudiodescription)Added CAFAudioFormatListItemAdded [CAFChunkHeader](https://developer.apple.com/documentation/audiotoolbox/cafchunkheader)Added [CAFDataChunk](https://developer.apple.com/documentation/audiotoolbox/cafdatachunk)Added [CAFFileHeader](https://developer.apple.com/documentation/audiotoolbox/caffileheader)Added [CAFInfoStrings](https://developer.apple.com/documentation/audiotoolbox/cafinfostrings)Added [CAFInstrumentChunk](https://developer.apple.com/documentation/audiotoolbox/cafinstrumentchunk)Added [CAFMarker](https://developer.apple.com/documentation/audiotoolbox/cafmarker)Added [CAFMarkerChunk](https://developer.apple.com/documentation/audiotoolbox/cafmarkerchunk)Added [CAFOverviewChunk](https://developer.apple.com/documentation/audiotoolbox/cafoverviewchunk)Added [CAFOverviewSample](https://developer.apple.com/documentation/audiotoolbox/cafoverviewsample)Added [CAFPacketTableHeader](https://developer.apple.com/documentation/audiotoolbox/cafpackettableheader)Added [CAFPeakChunk](https://developer.apple.com/documentation/audiotoolbox/cafpeakchunk)Added [CAFPositionPeak](https://developer.apple.com/documentation/audiotoolbox/cafpositionpeak)Added [CAFRegion](https://developer.apple.com/documentation/audiotoolbox/cafregion)Added [CAFRegionChunk](https://developer.apple.com/documentation/audiotoolbox/cafregionchunk)Added [CAFStringID](https://developer.apple.com/documentation/audiotoolbox/cafstringid)Added [CAFStrings](https://developer.apple.com/documentation/audiotoolbox/cafstrings)Added [CAFUMIDChunk](https://developer.apple.com/documentation/audiotoolbox/cafumidchunk)Added [CAF_SMPTE_Time](https://developer.apple.com/documentation/audiotoolbox/caf_smpte_time)Added [CAF_UUID_ChunkHeader](https://developer.apple.com/documentation/audiotoolbox/caf_uuid_chunkheader)Added #def NextCAFRegionAdded [kCAFLinearPCMFormatFlagIsFloat](https://developer.apple.com/documentation/audiotoolbox/cafformatflags/kcaflinearpcmformatflagisfloat)Added [kCAFLinearPCMFormatFlagIsLittleEndian](https://developer.apple.com/documentation/audiotoolbox/cafformatflags/kcaflinearpcmformatflagislittleendian)Added #def kCAFMarkerChunkHdrSizeAdded [kCAFMarkerType_EditDestinationBegin](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_editdestinationbegin)Added [kCAFMarkerType_EditDestinationEnd](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_editdestinationend)Added [kCAFMarkerType_EditSourceBegin](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_editsourcebegin)Added [kCAFMarkerType_EditSourceEnd](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_editsourceend)Added [kCAFMarkerType_Generic](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_generic)Added [kCAFMarkerType_Index](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_index)Added [kCAFMarkerType_KeySignature](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_keysignature)Added [kCAFMarkerType_ProgramEnd](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_programend)Added [kCAFMarkerType_ProgramStart](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_programstart)Added [kCAFMarkerType_RegionEnd](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_regionend)Added [kCAFMarkerType_RegionStart](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_regionstart)Added [kCAFMarkerType_RegionSyncPoint](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_regionsyncpoint)Added [kCAFMarkerType_ReleaseLoopEnd](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_releaseloopend)Added [kCAFMarkerType_ReleaseLoopStart](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_releaseloopstart)Added [kCAFMarkerType_SavedPlayPosition](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_savedplayposition)Added [kCAFMarkerType_SelectionEnd](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_selectionend)Added [kCAFMarkerType_SelectionStart](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_selectionstart)Added [kCAFMarkerType_SustainLoopEnd](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_sustainloopend)Added [kCAFMarkerType_SustainLoopStart](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_sustainloopstart)Added [kCAFMarkerType_Tempo](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_tempo)Added [kCAFMarkerType_TimeSignature](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_timesignature)Added [kCAFMarkerType_TrackEnd](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_trackend)Added [kCAFMarkerType_TrackStart](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_trackstart)Added #def kCAFRegionChunkHdrSizeAdded [kCAFRegionFlag_LoopEnable](https://developer.apple.com/documentation/audiotoolbox/cafregionflags/kcafregionflag_loopenable)Added [kCAFRegionFlag_PlayBackward](https://developer.apple.com/documentation/audiotoolbox/cafregionflags/1501777-playbackward)Added [kCAFRegionFlag_PlayForward](https://developer.apple.com/documentation/audiotoolbox/cafregionflags/kcafregionflag_playforward)Added [kCAF_AudioDataChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_audiodatachunkid)Added [kCAF_ChannelLayoutChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_channellayoutchunkid)Added [kCAF_EditCommentsChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_editcommentschunkid)Added [kCAF_FileType](https://developer.apple.com/documentation/audiotoolbox/kcaf_filetype)Added [kCAF_FileVersion_Initial](https://developer.apple.com/documentation/audiotoolbox/kcaf_fileversion_initial)Added [kCAF_FillerChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_fillerchunkid)Added [kCAF_FormatListID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_formatlistid)Added [kCAF_InfoStringsChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_infostringschunkid)Added [kCAF_InstrumentChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_instrumentchunkid)Added [kCAF_MIDIChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_midichunkid)Added [kCAF_MagicCookieID](https://developer.apple.com/documentation/audiotoolbox/kcaf_magiccookieid)Added [kCAF_MarkerChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_markerchunkid)Added [kCAF_OverviewChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_overviewchunkid)Added [kCAF_PacketTableChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_packettablechunkid)Added [kCAF_PeakChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_peakchunkid)Added [kCAF_RegionChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_regionchunkid)Added [kCAF_SMPTE_TimeType2398](https://developer.apple.com/documentation/audiotoolbox/kcaf_smpte_timetype2398)Added [kCAF_SMPTE_TimeType24](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype24)Added [kCAF_SMPTE_TimeType25](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype25)Added [kCAF_SMPTE_TimeType2997](https://developer.apple.com/documentation/audiotoolbox/kcaf_smpte_timetype2997)Added [kCAF_SMPTE_TimeType2997Drop](https://developer.apple.com/documentation/audiotoolbox/kcaf_smpte_timetype2997drop)Added [kCAF_SMPTE_TimeType30](https://developer.apple.com/documentation/audiotoolbox/kcaf_smpte_timetype30)Added [kCAF_SMPTE_TimeType30Drop](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype30drop)Added [kCAF_SMPTE_TimeType50](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype50)Added [kCAF_SMPTE_TimeType5994](https://developer.apple.com/documentation/audiotoolbox/kcaf_smpte_timetype5994)Added [kCAF_SMPTE_TimeType5994Drop](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype5994drop)Added [kCAF_SMPTE_TimeType60](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype60)Added [kCAF_SMPTE_TimeType60Drop](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype60drop)Added [kCAF_SMPTE_TimeTypeNone](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetypenone)Added [kCAF_StreamDescriptionChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_streamdescriptionchunkid)Added [kCAF_StringsChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_stringschunkid)Added [kCAF_UMIDChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_umidchunkid)Added [kCAF_UUIDChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_uuidchunkid)MusicPlayer.hAdded [AUPresetEvent](https://developer.apple.com/documentation/audiotoolbox/aupresetevent)Added [CABarBeatTime](https://developer.apple.com/documentation/audiotoolbox/cabarbeattime)Added [DisposeMusicEventIterator()](https://developer.apple.com/documentation/audiotoolbox/1503301-disposemusiceventiterator)Added [DisposeMusicPlayer()](https://developer.apple.com/documentation/audiotoolbox/1502985-disposemusicplayer)Added [DisposeMusicSequence()](https://developer.apple.com/documentation/audiotoolbox/1501909-disposemusicsequence)Added [ExtendedControlEvent](https://developer.apple.com/documentation/audiotoolbox/extendedcontrolevent) (no architecture available)Added [ExtendedNoteOnEvent](https://developer.apple.com/documentation/audiotoolbox/extendednoteonevent)Added [ExtendedTempoEvent](https://developer.apple.com/documentation/audiotoolbox/extendedtempoevent)Added [MIDIChannelMessage](https://developer.apple.com/documentation/audiotoolbox/midichannelmessage)Added [MIDIMetaEvent](https://developer.apple.com/documentation/audiotoolbox/midimetaevent)Added [MIDINoteMessage](https://developer.apple.com/documentation/audiotoolbox/midinotemessage)Added [MIDIRawData](https://developer.apple.com/documentation/audiotoolbox/midirawdata)Added [MusicEventIterator](https://developer.apple.com/documentation/audiotoolbox/musiceventiterator)Added [MusicEventIteratorDeleteEvent()](https://developer.apple.com/documentation/audiotoolbox/1502605-musiceventiteratordeleteevent)Added [MusicEventIteratorGetEventInfo()](https://developer.apple.com/documentation/audiotoolbox/1501702-musiceventiteratorgeteventinfo)Added [MusicEventIteratorHasCurrentEvent()](https://developer.apple.com/documentation/audiotoolbox/1503065-musiceventiteratorhascurrenteven)Added [MusicEventIteratorHasNextEvent()](https://developer.apple.com/documentation/audiotoolbox/1503205-musiceventiteratorhasnextevent)Added [MusicEventIteratorHasPreviousEvent()](https://developer.apple.com/documentation/audiotoolbox/1502205-musiceventiteratorhaspreviouseve)Added [MusicEventIteratorNextEvent()](https://developer.apple.com/documentation/audiotoolbox/1503143-musiceventiteratornextevent)Added [MusicEventIteratorPreviousEvent()](https://developer.apple.com/documentation/audiotoolbox/1501710-musiceventiteratorpreviousevent)Added [MusicEventIteratorSeek()](https://developer.apple.com/documentation/audiotoolbox/1502108-musiceventiteratorseek)Added [MusicEventIteratorSetEventInfo()](https://developer.apple.com/documentation/audiotoolbox/1503101-musiceventiteratorseteventinfo)Added [MusicEventIteratorSetEventTime()](https://developer.apple.com/documentation/audiotoolbox/1503403-musiceventiteratorseteventtime)Added [MusicEventType](https://developer.apple.com/documentation/audiotoolbox/musiceventtype)Added [MusicEventUserData](https://developer.apple.com/documentation/audiotoolbox/musiceventuserdata)Added [MusicPlayer](https://developer.apple.com/documentation/audiotoolbox/musicplayer)Added [MusicPlayerGetBeatsForHostTime()](https://developer.apple.com/documentation/audiotoolbox/1502501-musicplayergetbeatsforhosttime)Added [MusicPlayerGetHostTimeForBeats()](https://developer.apple.com/documentation/audiotoolbox/1502486-musicplayergethosttimeforbeats)Added [MusicPlayerGetPlayRateScalar()](https://developer.apple.com/documentation/audiotoolbox/1501767-musicplayergetplayratescalar)Added [MusicPlayerGetSequence()](https://developer.apple.com/documentation/audiotoolbox/1502355-musicplayergetsequence)Added [MusicPlayerGetTime()](https://developer.apple.com/documentation/audiotoolbox/1502259-musicplayergettime)Added [MusicPlayerIsPlaying()](https://developer.apple.com/documentation/audiotoolbox/1502241-musicplayerisplaying)Added [MusicPlayerPreroll()](https://developer.apple.com/documentation/audiotoolbox/1503131-musicplayerpreroll)Added [MusicPlayerSetPlayRateScalar()](https://developer.apple.com/documentation/audiotoolbox/1502928-musicplayersetplayratescalar)Added [MusicPlayerSetSequence()](https://developer.apple.com/documentation/audiotoolbox/1502518-musicplayersetsequence)Added [MusicPlayerSetTime()](https://developer.apple.com/documentation/audiotoolbox/1501770-musicplayersettime)Added [MusicPlayerStart()](https://developer.apple.com/documentation/audiotoolbox/1503255-musicplayerstart)Added [MusicPlayerStop()](https://developer.apple.com/documentation/audiotoolbox/1502668-musicplayerstop)Added [MusicSequence](https://developer.apple.com/documentation/audiotoolbox/musicsequence)Added [MusicSequenceBarBeatTimeToBeats()](https://developer.apple.com/documentation/audiotoolbox/1503191-musicsequencebarbeattimetobeats)Added [MusicSequenceBeatsToBarBeatTime()](https://developer.apple.com/documentation/audiotoolbox/1503366-musicsequencebeatstobarbeattime)Added [MusicSequenceDisposeTrack()](https://developer.apple.com/documentation/audiotoolbox/1502673-musicsequencedisposetrack)Added [MusicSequenceFileCreate()](https://developer.apple.com/documentation/audiotoolbox/1502760-musicsequencefilecreate)Added [MusicSequenceFileCreateData()](https://developer.apple.com/documentation/audiotoolbox/1503006-musicsequencefilecreatedata)Added [MusicSequenceFileFlags](https://developer.apple.com/documentation/audiotoolbox/musicsequencefileflags)Added [MusicSequenceFileLoad()](https://developer.apple.com/documentation/audiotoolbox/1502222-musicsequencefileload)Added [MusicSequenceFileLoadData()](https://developer.apple.com/documentation/audiotoolbox/1502465-musicsequencefileloaddata)Added [MusicSequenceFileTypeID](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid)Added [MusicSequenceGetAUGraph()](https://developer.apple.com/documentation/audiotoolbox/1502317-musicsequencegetaugraph)Added [MusicSequenceGetBeatsForSeconds()](https://developer.apple.com/documentation/audiotoolbox/1503378-musicsequencegetbeatsforseconds)Added [MusicSequenceGetIndTrack()](https://developer.apple.com/documentation/audiotoolbox/1501623-musicsequencegetindtrack)Added [MusicSequenceGetInfoDictionary()](https://developer.apple.com/documentation/audiotoolbox/1502298-musicsequencegetinfodictionary)Added [MusicSequenceGetSMPTEResolution()](https://developer.apple.com/documentation/audiotoolbox/1502035-musicsequencegetsmpteresolution)Added [MusicSequenceGetSecondsForBeats()](https://developer.apple.com/documentation/audiotoolbox/1502781-musicsequencegetsecondsforbeats)Added [MusicSequenceGetSequenceType()](https://developer.apple.com/documentation/audiotoolbox/1501659-musicsequencegetsequencetype)Added [MusicSequenceGetTempoTrack()](https://developer.apple.com/documentation/audiotoolbox/1502277-musicsequencegettempotrack)Added [MusicSequenceGetTrackCount()](https://developer.apple.com/documentation/audiotoolbox/1503390-musicsequencegettrackcount)Added [MusicSequenceGetTrackIndex()](https://developer.apple.com/documentation/audiotoolbox/1503150-musicsequencegettrackindex)Added [MusicSequenceLoadFlags](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags)Added [MusicSequenceNewTrack()](https://developer.apple.com/documentation/audiotoolbox/1503090-musicsequencenewtrack)Added [MusicSequenceReverse()](https://developer.apple.com/documentation/audiotoolbox/1502802-musicsequencereverse)Added [MusicSequenceSetAUGraph()](https://developer.apple.com/documentation/audiotoolbox/1503097-musicsequencesetaugraph)Added [MusicSequenceSetMIDIEndpoint()](https://developer.apple.com/documentation/audiotoolbox/1501917-musicsequencesetmidiendpoint)Added [MusicSequenceSetSMPTEResolution()](https://developer.apple.com/documentation/audiotoolbox/1502422-musicsequencesetsmpteresolution)Added [MusicSequenceSetSequenceType()](https://developer.apple.com/documentation/audiotoolbox/1501664-musicsequencesetsequencetype)Added [MusicSequenceSetUserCallback()](https://developer.apple.com/documentation/audiotoolbox/1503188-musicsequencesetusercallback)Added [MusicSequenceType](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype)Added [MusicSequenceUserCallback](https://developer.apple.com/documentation/audiotoolbox/musicsequenceusercallback)Added [MusicTimeStamp](https://developer.apple.com/documentation/audiotoolbox/musictimestamp)Added [MusicTrack](https://developer.apple.com/documentation/audiotoolbox/musictrack)Added [MusicTrackClear()](https://developer.apple.com/documentation/audiotoolbox/1503074-musictrackclear)Added [MusicTrackCopyInsert()](https://developer.apple.com/documentation/audiotoolbox/1501985-musictrackcopyinsert)Added [MusicTrackCut()](https://developer.apple.com/documentation/audiotoolbox/1502402-musictrackcut)Added [MusicTrackGetDestMIDIEndpoint()](https://developer.apple.com/documentation/audiotoolbox/1502965-musictrackgetdestmidiendpoint)Added [MusicTrackGetDestNode()](https://developer.apple.com/documentation/audiotoolbox/1501907-musictrackgetdestnode)Added [MusicTrackGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1503210-musictrackgetproperty)Added [MusicTrackGetSequence()](https://developer.apple.com/documentation/audiotoolbox/1502453-musictrackgetsequence)Added [MusicTrackLoopInfo](https://developer.apple.com/documentation/audiotoolbox/musictrackloopinfo)Added [MusicTrackMerge()](https://developer.apple.com/documentation/audiotoolbox/1502959-musictrackmerge)Added [MusicTrackMoveEvents()](https://developer.apple.com/documentation/audiotoolbox/1503297-musictrackmoveevents)Added [MusicTrackNewAUPresetEvent()](https://developer.apple.com/documentation/audiotoolbox/1502115-musictracknewaupresetevent)Added [MusicTrackNewExtendedNoteEvent()](https://developer.apple.com/documentation/audiotoolbox/1501902-musictracknewextendednoteevent)Added [MusicTrackNewExtendedTempoEvent()](https://developer.apple.com/documentation/audiotoolbox/1502846-musictracknewextendedtempoevent)Added [MusicTrackNewMIDIChannelEvent()](https://developer.apple.com/documentation/audiotoolbox/1502640-musictracknewmidichannelevent)Added [MusicTrackNewMIDINoteEvent()](https://developer.apple.com/documentation/audiotoolbox/1502187-musictracknewmidinoteevent)Added [MusicTrackNewMIDIRawDataEvent()](https://developer.apple.com/documentation/audiotoolbox/1501632-musictracknewmidirawdataevent)Added [MusicTrackNewMetaEvent()](https://developer.apple.com/documentation/audiotoolbox/1503236-musictracknewmetaevent)Added [MusicTrackNewParameterEvent()](https://developer.apple.com/documentation/audiotoolbox/1502270-musictracknewparameterevent)Added [MusicTrackNewUserEvent()](https://developer.apple.com/documentation/audiotoolbox/1503370-musictracknewuserevent)Added [MusicTrackSetDestMIDIEndpoint()](https://developer.apple.com/documentation/audiotoolbox/1503337-musictracksetdestmidiendpoint)Added [MusicTrackSetDestNode()](https://developer.apple.com/documentation/audiotoolbox/1502931-musictracksetdestnode)Added [MusicTrackSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1501688-musictracksetproperty)Added [NewMusicEventIterator()](https://developer.apple.com/documentation/audiotoolbox/1502076-newmusiceventiterator)Added [NewMusicPlayer()](https://developer.apple.com/documentation/audiotoolbox/1503211-newmusicplayer)Added [NewMusicSequence()](https://developer.apple.com/documentation/audiotoolbox/1502634-newmusicsequence)Added [ParameterEvent](https://developer.apple.com/documentation/audiotoolbox/parameterevent)Added [kAudioToolboxErr_CannotDoInCurrentContext](https://developer.apple.com/documentation/audiotoolbox/kaudiotoolboxerr_cannotdoincurrentcontext)Added [kAudioToolboxErr_EndOfTrack](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_endoftrack)Added [kAudioToolboxErr_IllegalTrackDestination](https://developer.apple.com/documentation/audiotoolbox/kaudiotoolboxerr_illegaltrackdestination)Added [kAudioToolboxErr_InvalidEventType](https://developer.apple.com/documentation/audiotoolbox/kaudiotoolboxerr_invalideventtype)Added [kAudioToolboxErr_InvalidPlayerState](https://developer.apple.com/documentation/audiotoolbox/kaudiotoolboxerr_invalidplayerstate)Added [kAudioToolboxErr_InvalidSequenceType](https://developer.apple.com/documentation/audiotoolbox/kaudiotoolboxerr_invalidsequencetype)Added [kAudioToolboxErr_NoSequence](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_nosequence)Added [kAudioToolboxErr_StartOfTrack](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_startoftrack)Added [kAudioToolboxErr_TrackIndexError](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_trackindexerror)Added [kAudioToolboxErr_TrackNotFound](https://developer.apple.com/documentation/audiotoolbox/kaudiotoolboxerr_tracknotfound)Added [kMusicEventType_AUPreset](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_aupreset)Added [kMusicEventType_ExtendedControl](https://developer.apple.com/documentation/audiotoolbox/1515446-anonymous/kmusiceventtype_extendedcontrol) (no architecture available)Added [kMusicEventType_ExtendedNote](https://developer.apple.com/documentation/audiotoolbox/1515479-anonymous/kmusiceventtype_extendednote)Added [kMusicEventType_ExtendedTempo](https://developer.apple.com/documentation/audiotoolbox/1515479-anonymous/kmusiceventtype_extendedtempo)Added [kMusicEventType_MIDIChannelMessage](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_midichannelmessage)Added [kMusicEventType_MIDINoteMessage](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_midinotemessage)Added [kMusicEventType_MIDIRawData](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_midirawdata)Added [kMusicEventType_Meta](https://developer.apple.com/documentation/audiotoolbox/1515479-anonymous/kmusiceventtype_meta)Added [kMusicEventType_NULL](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_null)Added [kMusicEventType_Parameter](https://developer.apple.com/documentation/audiotoolbox/1515479-anonymous/kmusiceventtype_parameter)Added [kMusicEventType_User](https://developer.apple.com/documentation/audiotoolbox/1515479-anonymous/kmusiceventtype_user)Added [kMusicSequenceFileFlags_EraseFile](https://developer.apple.com/documentation/audiotoolbox/musicsequencefileflags/kmusicsequencefileflags_erasefile)Added [kMusicSequenceFile_MIDIType](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid/kmusicsequencefile_miditype)Added [kMusicSequenceFile_iMelodyType](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid/kmusicsequencefile_imelodytype)Added [kMusicSequenceLoadSMF_ChannelsToTracks](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags/1501650-smf_channelstotracks)Added [kMusicSequenceType_Beats](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/beats)Added [kMusicSequenceType_Samples](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/kmusicsequencetype_samples)Added [kMusicSequenceType_Seconds](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/seconds)Added [#def kMusicTimeStamp_EndOfTrack](https://developer.apple.com/documentation/audiotoolbox/kmusictimestamp_endoftrack)Added [kSequenceTrackProperty_AutomatedParameters](https://developer.apple.com/documentation/audiotoolbox/ksequencetrackproperty_automatedparameters)Added [kSequenceTrackProperty_LoopInfo](https://developer.apple.com/documentation/audiotoolbox/ksequencetrackproperty_loopinfo)Added [kSequenceTrackProperty_MuteStatus](https://developer.apple.com/documentation/audiotoolbox/1515456-music_track_properties/ksequencetrackproperty_mutestatus)Added [kSequenceTrackProperty_OffsetTime](https://developer.apple.com/documentation/audiotoolbox/ksequencetrackproperty_offsettime)Added [kSequenceTrackProperty_SoloStatus](https://developer.apple.com/documentation/audiotoolbox/1515456-music_track_properties/ksequencetrackproperty_solostatus)Added [kSequenceTrackProperty_TimeResolution](https://developer.apple.com/documentation/audiotoolbox/1515456-music_track_properties/ksequencetrackproperty_timeresolution)Added [kSequenceTrackProperty_TrackLength](https://developer.apple.com/documentation/audiotoolbox/ksequencetrackproperty_tracklength)

## AudioUnit

AUComponent.hAdded [AudioUnitProcessMultipleProc](https://developer.apple.com/documentation/audiotoolbox/audiounitprocessmultipleproc)Added [AudioUnitRemovePropertyListenerWithUserDataProc](https://developer.apple.com/documentation/audiotoolbox/audiounitremovepropertylistenerwithuserdataproc)Added [kAudioUnitProcessMultipleSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitprocessmultipleselect)Added [kAudioUnitSubType_AUiPodTimeOther](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_auipodtimeother)Added [kAudioUnitSubType_NBandEQ](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_nbandeq)Added [kAudioUnitSubType_Reverb2](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_reverb2)Modified [kAudioUnitSubType_Distortion](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_distortion)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_Varispeed](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_varispeed)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_DynamicsProcessor](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_dynamicsprocessor)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_HighPassFilter](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_highpassfilter)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_Sampler](https://developer.apple.com/documentation/audiotoolbox/1619498-anonymous/kaudiounitsubtype_sampler)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_HighShelfFilter](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_highshelffilter)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_BandPassFilter](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_bandpassfilter)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_AudioFilePlayer](https://developer.apple.com/documentation/audiotoolbox/1619493-generator_audio_unit_subtypes/kaudiounitsubtype_audiofileplayer)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_LowShelfFilter](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_lowshelffilter)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_ScheduledSoundPlayer](https://developer.apple.com/documentation/audiotoolbox/1584155-anonymous/kaudiounitsubtype_scheduledsoundplayer)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_LowPassFilter](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_lowpassfilter)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_ParametricEQ](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_parametriceq)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitSubType_PeakLimiter](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_peaklimiter)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

AudioComponent.hAdded [AudioComponentRegister()](https://developer.apple.com/documentation/audiotoolbox/1410487-audiocomponentregister)Added [kAudioComponentFlag_Unsearchable](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_unsearchable)AudioUnitParameters.hAdded [kAUNBandEQFilterType_2ndOrderButterworthHighPass](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_2ndorderbutterworthhighpass)Added [kAUNBandEQFilterType_2ndOrderButterworthLowPass](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_2ndorderbutterworthlowpass)Added [kAUNBandEQFilterType_BandPass](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/kaunbandeqfiltertype_bandpass)Added [kAUNBandEQFilterType_BandStop](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_bandstop)Added [kAUNBandEQFilterType_HighShelf](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_highshelf)Added [kAUNBandEQFilterType_LowShelf](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_lowshelf)Added [kAUNBandEQFilterType_Parametric](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/kaunbandeqfiltertype_parametric)Added [kAUNBandEQFilterType_ResonantHighPass](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/kaunbandeqfiltertype_resonanthighpass)Added [kAUNBandEQFilterType_ResonantHighShelf](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_resonanthighshelf)Added [kAUNBandEQFilterType_ResonantLowPass](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/kaunbandeqfiltertype_resonantlowpass)Added [kAUNBandEQFilterType_ResonantLowShelf](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/kaunbandeqfiltertype_resonantlowshelf)Added [kAUNBandEQParam_Bandwidth](https://developer.apple.com/documentation/audiotoolbox/1389745-anonymous/kaunbandeqparam_bandwidth)Added [kAUNBandEQParam_BypassBand](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_bypassband)Added [kAUNBandEQParam_FilterType](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_filtertype)Added [kAUNBandEQParam_Frequency](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_frequency)Added [kAUNBandEQParam_Gain](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_gain)Added [kNumAUNBandEQFilterTypes](https://developer.apple.com/documentation/audiotoolbox/knumaunbandeqfiltertypes)Added [kReverb2Param_DecayTimeAt0Hz](https://developer.apple.com/documentation/audiotoolbox/1615024-reverb_unit_parameters/kreverb2param_decaytimeat0hz)Added [kReverb2Param_DecayTimeAtNyquist](https://developer.apple.com/documentation/audiotoolbox/1615024-reverb_unit_parameters/kreverb2param_decaytimeatnyquist)Added [kReverb2Param_DryWetMix](https://developer.apple.com/documentation/audiotoolbox/1615024-reverb_unit_parameters/kreverb2param_drywetmix)Added [kReverb2Param_Gain](https://developer.apple.com/documentation/audiotoolbox/kreverb2param_gain)Added [kReverb2Param_MaxDelayTime](https://developer.apple.com/documentation/audiotoolbox/kreverb2param_maxdelaytime)Added [kReverb2Param_MinDelayTime](https://developer.apple.com/documentation/audiotoolbox/1615024-reverb_unit_parameters/kreverb2param_mindelaytime)Added [kReverb2Param_RandomizeReflections](https://developer.apple.com/documentation/audiotoolbox/1615024-reverb_unit_parameters/kreverb2param_randomizereflections)Modified [kDynamicsProcessorParam_AttackTime](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_attacktime)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kLowPassParam_Resonance](https://developer.apple.com/documentation/audiotoolbox/1389999-lowpass_unit_parameters/klowpassparam_resonance)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDynamicsProcessorParam_OutputAmplitude](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_outputamplitude)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_Pan](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_pan)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_AllNotesOff](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_allnotesoff)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kParametricEQParam_CenterFreq](https://developer.apple.com/documentation/audiotoolbox/1389950-parametric_eq_unit_parameters/kparametriceqparam_centerfreq)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_DataEntry](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_dataentry)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_AllSoundOff](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_allsoundoff)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_Foot_LSB](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_foot_lsb)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_Rounding](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_rounding)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDynamicsProcessorParam_ExpansionThreshold](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_expansionthreshold)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kBandpassParam_Bandwidth](https://developer.apple.com/documentation/audiotoolbox/1390144-bandpass_unit_parameters/kbandpassparam_bandwidth)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_RingModFreq1](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_ringmodfreq1)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kLimiterParam_PreGain](https://developer.apple.com/documentation/audiotoolbox/klimiterparam_pregain)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [k3DMixerParam_ReverbBlend](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_reverbblend)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbParam_FilterBandwidth](https://developer.apple.com/documentation/audiotoolbox/1390119-additional_reverb_parameters/kreverbparam_filterbandwidth)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_PolynomialMix](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_polynomialmix)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDynamicsProcessorParam_ExpansionRatio](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_expansionratio)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDynamicsProcessorParam_ReleaseTime](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_releasetime)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kLimiterParam_DecayTime](https://developer.apple.com/documentation/audiotoolbox/1389597-peak_limiter_unit_parameters/klimiterparam_decaytime)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_ModWheel_LSB](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_modwheel_lsb)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kHipassParam_Resonance](https://developer.apple.com/documentation/audiotoolbox/1389948-highpass_unit_parameters/khipassparam_resonance)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_Expression](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_expression)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_DecimationMix](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_decimationmix)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_RingModMix](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_ringmodmix)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_Foot](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_foot)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kBandpassParam_CenterFrequency](https://developer.apple.com/documentation/audiotoolbox/1390144-bandpass_unit_parameters/kbandpassparam_centerfrequency)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [k3DMixerParam_GlobalReverbGain](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_globalreverbgain)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_ResetAllControllers](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_resetallcontrollers)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kHighShelfParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1389967-high_shelf_filter_unit_parameter/khighshelfparam_gain)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_Delay](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_delay)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbParam_FilterFrequency](https://developer.apple.com/documentation/audiotoolbox/1390119-additional_reverb_parameters/kreverbparam_filterfrequency)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_Pan_LSB](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_pan_lsb)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kVarispeedParam_PlaybackCents](https://developer.apple.com/documentation/audiotoolbox/1390014-varispeed_unit_parameters/kvarispeedparam_playbackcents)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_CubicTerm](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_cubicterm)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDynamicsProcessorParam_MasterGain](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_mastergain)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_PitchBend](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_pitchbend)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kHipassParam_CutoffFrequency](https://developer.apple.com/documentation/audiotoolbox/khipassparam_cutofffrequency)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAULowShelfParam_CutoffFrequency](https://developer.apple.com/documentation/audiotoolbox/1389995-low_shelf_filter_unit_parameters/kaulowshelfparam_cutofffrequency)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kLimiterParam_AttackTime](https://developer.apple.com/documentation/audiotoolbox/1389597-peak_limiter_unit_parameters/klimiterparam_attacktime)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDynamicsProcessorParam_HeadRoom](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_headroom)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_DataEntry_LSB](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_dataentry_lsb)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_DelayMix](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_delaymix)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kParametricEQParam_Q](https://developer.apple.com/documentation/audiotoolbox/1389950-parametric_eq_unit_parameters/kparametriceqparam_q)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_RingModBalance](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_ringmodbalance)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_Volume](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_volume)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_KeyPressure](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_keypressure)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_ModWheel](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_modwheel)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [k3DMixerParam_OcclusionAttenuation](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_occlusionattenuation)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_KeyPressure_LastKey](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_keypressure_lastkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_LinearTerm](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_linearterm)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_Sustain](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_sustain)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_ChannelPressure](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_channelpressure)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDynamicsProcessorParam_CompressionAmount](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_compressionamount)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_RingModFreq2](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_ringmodfreq2)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_Decay](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_decay)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDynamicsProcessorParam_InputAmplitude](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_inputamplitude)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDynamicsProcessorParam_Threshold](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_threshold)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAULowShelfParam_Gain](https://developer.apple.com/documentation/audiotoolbox/kaulowshelfparam_gain)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_Expression_LSB](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_expression_lsb)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kLowPassParam_CutoffFrequency](https://developer.apple.com/documentation/audiotoolbox/1389999-lowpass_unit_parameters/klowpassparam_cutofffrequency)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kParametricEQParam_Gain](https://developer.apple.com/documentation/audiotoolbox/kparametriceqparam_gain)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_KeyPressure_FirstKey](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_keypressure_firstkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAUGroupParameterID_Volume_LSB](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_volume_lsb)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kVarispeedParam_PlaybackRate](https://developer.apple.com/documentation/audiotoolbox/kvarispeedparam_playbackrate)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_SoftClipGain](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_softclipgain)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_SquaredTerm](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_squaredterm)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbParam_FilterGain](https://developer.apple.com/documentation/audiotoolbox/kreverbparam_filtergain)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_Decimation](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_decimation)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [k3DMixerParam_ObstructionAttenuation](https://developer.apple.com/documentation/audiotoolbox/k3dmixerparam_obstructionattenuation)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kHighShelfParam_CutOffFrequency](https://developer.apple.com/documentation/audiotoolbox/khighshelfparam_cutofffrequency)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kDistortionParam_FinalMix](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_finalmix)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

AudioUnitProperties.hRemoved VoiceIOFarEndVersionInfoRemoved kAUVoiceIOProperty_FarEndVersionInfoRemoved kVoiceIOFarEndAUVersion_RequiresBackwardCompatibilityRemoved kVoiceIOFarEndAUVersion_ThirdPartyAdded [AUSamplerBankPresetData](https://developer.apple.com/documentation/audiotoolbox/ausamplerbankpresetdata)Added [kAUNBandEQProperty_MaxNumberOfBands](https://developer.apple.com/documentation/audiotoolbox/1534022-anonymous/kaunbandeqproperty_maxnumberofbands)Added [kAUNBandEQProperty_NumberOfBands](https://developer.apple.com/documentation/audiotoolbox/1534022-anonymous/kaunbandeqproperty_numberofbands)Added [kAUSamplerProperty_LoadAudioFiles](https://developer.apple.com/documentation/audiotoolbox/kausamplerproperty_loadaudiofiles)Added [kAUSamplerProperty_LoadPresetFromBank](https://developer.apple.com/documentation/audiotoolbox/kausamplerproperty_loadpresetfrombank)Added [kAUSampler_DefaultBankLSB](https://developer.apple.com/documentation/audiotoolbox/kausampler_defaultbanklsb)Added [kAUSampler_DefaultMelodicBankMSB](https://developer.apple.com/documentation/audiotoolbox/1534086-anonymous/kausampler_defaultmelodicbankmsb)Added [kAUSampler_DefaultPercussionBankMSB](https://developer.apple.com/documentation/audiotoolbox/1534086-anonymous/kausampler_defaultpercussionbankmsb)Added [kAudioUnitScope_Layer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitscope_layer)Added [kAudioUnitScope_LayerItem](https://developer.apple.com/documentation/audiotoolbox/kaudiounitscope_layeritem)Modified [HostCallback_GetMusicalTimeLocation](https://developer.apple.com/documentation/audiotoolbox/hostcallback_getmusicaltimelocation)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitScope_Group](https://developer.apple.com/documentation/audiotoolbox/kaudiounitscope_group)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_CPULoad](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_cpuload)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_LargeHall](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_largehall)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [ScheduledAudioFileRegion](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [HostCallbackInfo](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [ScheduledAudioSlice](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_LargeChamber](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_largechamber)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kNumberOfResponseFrequencies](https://developer.apple.com/documentation/audiotoolbox/1534092-frequency_response_constants/knumberofresponsefrequencies)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_LargeHall2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_largehall2)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kScheduledAudioSliceFlag_BeganToRender](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1438311-scheduledaudiosliceflag_begantor)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_ScheduledFileIDs](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_scheduledfileids)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_ScheduleStartTimeStamp](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_schedulestarttimestamp)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_UsesInternalReverb](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_usesinternalreverb)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_MediumRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_mediumroom)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitScope_Part](https://developer.apple.com/documentation/audiotoolbox/1534214-audio_unit_scopes/kaudiounitscope_part)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_Cathedral](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_cathedral)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [HostCallback_GetTransportState](https://developer.apple.com/documentation/audiotoolbox/hostcallback_gettransportstate)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [ScheduledAudioFileRegionCompletionProc](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregioncompletionproc)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_ParameterValueStrings](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parametervaluestrings)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kScheduledAudioSliceFlag_Complete](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_complete)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [AudioUnitFrequencyResponseBin](https://developer.apple.com/documentation/audiotoolbox/audiounitfrequencyresponsebin)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_LargeRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_largeroom)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_ScheduledFileRegion](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_scheduledfileregion)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_Plate](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_plate)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_MediumChamber](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_mediumchamber)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_ScheduledFileNumberBuffers](https://developer.apple.com/documentation/audiotoolbox/1534079-anonymous/kaudiounitproperty_scheduledfilenumberbuffers)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_LargeRoom2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_largeroom2)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kScheduledAudioSliceFlag_BeganToRenderLate](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1438581-scheduledaudiosliceflag_begantor)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_ScheduledFilePrime](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_scheduledfileprime)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_ReverbRoomType](https://developer.apple.com/documentation/audiotoolbox/1534150-anonymous/kaudiounitproperty_reverbroomtype)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_MediumHall2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall2)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_ScheduleAudioSlice](https://developer.apple.com/documentation/audiotoolbox/1534024-anonymous/kaudiounitproperty_scheduleaudioslice)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_MediumHall](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_CurrentPlayTime](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_currentplaytime)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [HostCallback_GetBeatAndTempo](https://developer.apple.com/documentation/audiotoolbox/hostcallback_getbeatandtempo)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitScope_Note](https://developer.apple.com/documentation/audiotoolbox/1534214-audio_unit_scopes/kaudiounitscope_note)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_SmallRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_smallroom)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [ScheduledAudioSliceCompletionProc](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslicecompletionproc)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_ScheduledFileBufferSizeFrames](https://developer.apple.com/documentation/audiotoolbox/1534079-anonymous/kaudiounitproperty_scheduledfilebuffersizeframes)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kAudioUnitProperty_HostCallbacks](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_hostcallbacks)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kReverbRoomType_MediumHall3](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall3)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

MusicDevice.hAdded [MusicDeviceComponent](https://developer.apple.com/documentation/audiotoolbox/musicdevicecomponent)Added [MusicDeviceGroupID](https://developer.apple.com/documentation/audiotoolbox/musicdevicegroupid)Added [MusicDeviceInstrumentID](https://developer.apple.com/documentation/audiotoolbox/musicdeviceinstrumentid)Added [MusicDeviceMIDIEvent()](https://developer.apple.com/documentation/audiotoolbox/1439861-musicdevicemidievent)Added [MusicDeviceMIDIEventProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicemidieventproc)Added [MusicDeviceNoteParams](https://developer.apple.com/documentation/audiotoolbox/musicdevicenoteparams)Added [MusicDeviceStartNote()](https://developer.apple.com/documentation/audiotoolbox/1440960-musicdevicestartnote)Added [MusicDeviceStartNoteProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicestartnoteproc)Added [MusicDeviceStdNoteParams](https://developer.apple.com/documentation/audiotoolbox/musicdevicestdnoteparams)Added [MusicDeviceStopNote()](https://developer.apple.com/documentation/audiotoolbox/1440390-musicdevicestopnote)Added [MusicDeviceStopNoteProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicestopnoteproc)Added [MusicDeviceSysEx()](https://developer.apple.com/documentation/audiotoolbox/1438996-musicdevicesysex)Added [MusicDeviceSysExProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicesysexproc)Added [NoteInstanceID](https://developer.apple.com/documentation/audiotoolbox/noteinstanceid)Added [NoteParamsControlValue](https://developer.apple.com/documentation/audiotoolbox/noteparamscontrolvalue)Added [kMusicDeviceMIDIEventSelect](https://developer.apple.com/documentation/audiotoolbox/kmusicdevicemidieventselect)Added [kMusicDevicePrepareInstrumentSelect](https://developer.apple.com/documentation/audiotoolbox/kmusicdeviceprepareinstrumentselect)Added [kMusicDeviceRange](https://developer.apple.com/documentation/audiotoolbox/1473469-anonymous/kmusicdevicerange)Added [kMusicDeviceReleaseInstrumentSelect](https://developer.apple.com/documentation/audiotoolbox/kmusicdevicereleaseinstrumentselect)Added [kMusicDeviceStartNoteSelect](https://developer.apple.com/documentation/audiotoolbox/1473469-anonymous/kmusicdevicestartnoteselect)Added [kMusicDeviceStopNoteSelect](https://developer.apple.com/documentation/audiotoolbox/kmusicdevicestopnoteselect)Added [kMusicDeviceSysExSelect](https://developer.apple.com/documentation/audiotoolbox/kmusicdevicesysexselect)Added [kMusicNoteEvent_Unused](https://developer.apple.com/documentation/audiotoolbox/1473494-anonymous/kmusicnoteevent_unused)Added [kMusicNoteEvent_UseGroupInstrument](https://developer.apple.com/documentation/audiotoolbox/kmusicnoteevent_usegroupinstrument)

## AVFoundation

AVAsset.hAdded [+[AVAsset assetWithURL:]](https://developer.apple.com/documentation/avfoundation/avasset/1389943-init)Added [AVAsset.availableMediaCharacteristicsWithMediaSelectionOptions](https://developer.apple.com/documentation/avfoundation/avasset/1389433-availablemediacharacteristicswit)Added [AVAsset.compatibleWithSavedPhotosAlbum](https://developer.apple.com/documentation/avfoundation/avasset/1616742-compatiblewithsavedphotosalbum)Added [AVAsset.creationDate](https://developer.apple.com/documentation/avfoundation/avasset/1386342-creationdate)Added [-[AVAsset mediaSelectionGroupForMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avasset/1387496-mediaselectiongroupformediachara)Added [AVAsset.referenceRestrictions](https://developer.apple.com/documentation/avfoundation/avasset/1390489-referencerestrictions)Added [+[AVURLAsset audiovisualMIMETypes]](https://developer.apple.com/documentation/avfoundation/avurlasset/1390006-audiovisualmimetypes)Added [+[AVURLAsset audiovisualTypes]](https://developer.apple.com/documentation/avfoundation/avurlasset/1386800-audiovisualtypes)Added [+[AVURLAsset isPlayableExtendedMIMEType:]](https://developer.apple.com/documentation/avfoundation/avurlasset/1387142-isplayableextendedmimetype)Added AVAsset(AVAssetMediaSelection)Added AVAsset(AVAssetReferenceRestrictions)Added [AVAssetReferenceRestrictionForbidAll](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/1387554-forbidall)Added [AVAssetReferenceRestrictionForbidCrossSiteReference](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/1390228-forbidcrosssitereference)Added [AVAssetReferenceRestrictionForbidLocalReferenceToLocal](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidlocalreferencetolocal)Added [AVAssetReferenceRestrictionForbidLocalReferenceToRemote](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidlocalreferencetoremote)Added [AVAssetReferenceRestrictionForbidNone](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidnone)Added [AVAssetReferenceRestrictionForbidRemoteReferenceToLocal](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/1387464-forbidremotereferencetolocal)Added [AVURLAssetReferenceRestrictionsKey](https://developer.apple.com/documentation/avfoundation/avurlassetreferencerestrictionskey)Modified [AVAsset.naturalSize](https://developer.apple.com/documentation/avfoundation/avasset/1508715-naturalsize)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

AVAssetExportSession.hAdded [AVAssetExportSession.asset](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385690-asset)Added [AVAssetExportSession.estimatedOutputFileLength](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1389181-estimatedoutputfilelength)Added [AVAssetExportPreset1920x1080](https://developer.apple.com/documentation/avfoundation/avassetexportpreset1920x1080)AVAssetImageGenerator.hAdded [AVAssetImageGenerator.requestedTimeToleranceAfter](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1387751-requestedtimetoleranceafter)Added [AVAssetImageGenerator.requestedTimeToleranceBefore](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1390571-requestedtimetolerancebefore)AVAssetReaderOutput.hAdded [AVAssetReaderOutput.alwaysCopiesSampleData](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1389189-alwayscopiessampledata)AVAssetTrack.hAdded [AVAssetTrack.playable](https://developer.apple.com/documentation/avfoundation/avassettrack/1388276-isplayable)AVAudioPlayer.hAdded [AVAudioPlayer.enableRate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387084-enablerate)Added [AVAudioPlayer.rate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386118-rate)AVAudioSession.hAdded [AVAudioSession.mode](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616508-mode)Added [-[AVAudioSession setMode:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616614-setmode)Added [AVAudioSessionModeDefault](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616579-default)Added [AVAudioSessionModeGameChat](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616511-gamechat)Added [AVAudioSessionModeMeasurement](https://developer.apple.com/documentation/avfoundation/avaudiosessionmodemeasurement)Added [AVAudioSessionModeVideoRecording](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616535-videorecording)Added [AVAudioSessionModeVoiceChat](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616455-voicechat)AVBase.hAdded #def AVAILABLE_MAC_OS_X_VERSION_TBD_AND_LATERAdded #def AVF_EXPORTAVCaptureDevice.hAdded [AVCaptureDevice.flashActive](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624598-flashactive)Added [AVCaptureDevice.flashAvailable](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624627-flashavailable)Added [AVCaptureDevice.subjectAreaChangeMonitoringEnabled](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624644-issubjectareachangemonitoringena)Added [AVCaptureDevice.torchAvailable](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624626-torchavailable)Added [AVCaptureDevice.torchLevel](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624605-torchlevel)Added AVCaptureDevice(AVCaptureDeviceSubjectAreaChangeMonitoring)Added [AVCaptureDeviceSubjectAreaDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1624619-avcapturedevicesubjectareadidcha)AVCaptureOutput.hAdded [-[AVCaptureOutput connectionWithMediaType:]](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/1389574-connectionwithmediatype)Added [AVCaptureStillImageOutput.capturingStillImage](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1387269-iscapturingstillimage)Added [AVCaptureVideoDataOutput.availableVideoCVPixelFormatTypes](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1387050-availablevideocvpixelformattypes)Added [AVCaptureVideoDataOutput.availableVideoCodecTypes](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389227-availablevideocodectypes)Modified [AVCaptureVideoDataOutput.minFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1616296-minframeduration)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

AVCaptureSession.hAdded [AVCaptureConnection.supportsVideoMaxFrameDuration](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1389158-isvideomaxframedurationsupported)Added [AVCaptureConnection.supportsVideoMinFrameDuration](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1386978-isvideominframedurationsupported)Added [AVCaptureConnection.videoMaxFrameDuration](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1390246-videomaxframeduration)Added [AVCaptureConnection.videoMaxScaleAndCropFactor](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1620478-videomaxscaleandcropfactor)Added [AVCaptureConnection.videoMinFrameDuration](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1388931-videominframeduration)Added [AVCaptureConnection.videoScaleAndCropFactor](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1620479-videoscaleandcropfactor)Added [AVCaptureSessionPreset1920x1080](https://developer.apple.com/documentation/avfoundation/avcapturesessionpreset1920x1080)Added [AVCaptureSessionPreset352x288](https://developer.apple.com/documentation/avfoundation/avcapturesessionpreset352x288)Added [AVCaptureSessionPresetiFrame1280x720](https://developer.apple.com/documentation/avfoundation/avcapturesessionpresetiframe1280x720)Added [AVCaptureSessionPresetiFrame960x540](https://developer.apple.com/documentation/avfoundation/avcapturesessionpresetiframe960x540)AVComposition.hAdded [AVComposition.naturalSize](https://developer.apple.com/documentation/avfoundation/avcomposition/1387247-naturalsize)Modified [AVMutableComposition.naturalSize](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1390424-naturalsize)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

AVCompositionTrack.hAdded [-[AVMutableCompositionTrack insertTimeRanges:ofTracks:atTime:error:]](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1388629-inserttimeranges)AVError.hAdded [AVErrorDecoderTemporarilyUnavailable](https://developer.apple.com/documentation/avfoundation/averror/code/decodertemporarilyunavailable)Added [AVErrorEncoderTemporarilyUnavailable](https://developer.apple.com/documentation/avfoundation/averror/averrorencodertemporarilyunavailable)Added [AVErrorInvalidVideoComposition](https://developer.apple.com/documentation/avfoundation/averror/averrorinvalidvideocomposition)Added [AVErrorOperationNotSupportedForAsset](https://developer.apple.com/documentation/avfoundation/averror/averroroperationnotsupportedforasset)Added [AVErrorReferenceForbiddenByReferencePolicy](https://developer.apple.com/documentation/avfoundation/averror/code/referenceforbiddenbyreferencepolicy)AVMediaFormat.hAdded [AVMediaCharacteristicContainsOnlyForcedSubtitles](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1390487-containsonlyforcedsubtitles)Added [AVMediaCharacteristicDescribesMusicAndSoundForAccessibility](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1387889-describesmusicandsoundforaccessi)Added [AVMediaCharacteristicDescribesVideoForAccessibility](https://developer.apple.com/documentation/avfoundation/avmediacharacteristicdescribesvideoforaccessibility)Added [AVMediaCharacteristicIsAuxiliaryContent](https://developer.apple.com/documentation/avfoundation/avmediacharacteristicisauxiliarycontent)Added [AVMediaCharacteristicIsMainProgramContent](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1387506-ismainprogramcontent)Added [AVMediaCharacteristicTranscribesSpokenDialogForAccessibility](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1386206-transcribesspokendialogforaccess)AVMediaSelectionGroup.hAdded [AVMediaSelectionGroup](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup)Added [AVMediaSelectionGroup.allowsEmptySelection](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388483-allowsemptyselection)Added [-[AVMediaSelectionGroup mediaSelectionOptionWithPropertyList:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1389968-mediaselectionoptionwithproperty)Added [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withLocale:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387494-mediaselectionoptionsfromarray)Added [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withMediaCharacteristics:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388258-mediaselectionoptions)Added [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withoutMediaCharacteristics:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387631-mediaselectionoptionsfromarray)Added [AVMediaSelectionGroup.options](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388351-options)Added [+[AVMediaSelectionGroup playableMediaSelectionOptionsFromArray:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387351-playablemediaselectionoptions)Added [AVMediaSelectionOption](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption)Added [-[AVMediaSelectionOption associatedMediaSelectionOptionInMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388232-associatedmediaselectionoptionin)Added [AVMediaSelectionOption.availableMetadataFormats](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1389504-availablemetadataformats)Added [AVMediaSelectionOption.commonMetadata](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1387859-commonmetadata)Added [-[AVMediaSelectionOption hasMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388531-hasmediacharacteristic)Added [AVMediaSelectionOption.locale](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388436-locale)Added [AVMediaSelectionOption.mediaSubTypes](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1385587-mediasubtypes)Added [AVMediaSelectionOption.mediaType](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386322-mediatype)Added [-[AVMediaSelectionOption metadataForFormat:]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386666-metadataforformat)Added [AVMediaSelectionOption.playable](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1390917-isplayable)Added [-[AVMediaSelectionOption propertyList]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386310-propertylist)Added AVMediaSelectionGroup(AVMediaSelectionOptionFiltering)AVMetadataFormat.hAdded [AVMetadataQuickTimeUserDataKeyTaggedCharacteristic](https://developer.apple.com/documentation/avfoundation/avmetadatakey/1386104-quicktimeuserdatakeytaggedcharac)AVPlayer.hAdded [AVPlayer.airPlayVideoActive](https://developer.apple.com/documentation/avfoundation/avplayer/1624259-airplayvideoactive)Added [AVPlayer.allowsAirPlayVideo](https://developer.apple.com/documentation/avfoundation/avplayer/1624258-allowsairplayvideo)Added [-[AVPlayer seekToTime:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayer/1387018-seektotime)Added [-[AVPlayer seekToTime:toleranceBefore:toleranceAfter:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayer/1388493-seek)Added [AVPlayer.usesAirPlayVideoWhileAirPlayScreenIsActive](https://developer.apple.com/documentation/avfoundation/avplayer/1624256-usesairplayvideowhileairplayscre)Added AVPlayer(AVPlayerAirPlaySupport)Added AVPlayer(AVPlayerItemControl)Added AVPlayer(AVPlayerMediaControl)Added AVPlayer(AVPlayerTimeControl)AVPlayerItem.hAdded [AVPlayerItem.canPlayFastForward](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389096-canplayfastforward)Added [AVPlayerItem.canPlayFastReverse](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390493-canplayfastreverse)Added [-[AVPlayerItem cancelPendingSeeks]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388316-cancelpendingseeks)Added [-[AVPlayerItem seekToTime:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387418-seektotime)Added [-[AVPlayerItem seekToTime:toleranceBefore:toleranceAfter:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387753-seek)Added [-[AVPlayerItem selectMediaOption:inMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389610-selectmediaoption)Added [-[AVPlayerItem selectedMediaOptionInMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386314-selectedmediaoptioninmediaselect)Added AVPlayerItem(AVPlayerItemInspection)Added AVPlayerItem(AVPlayerItemMediaSelection)Added AVPlayerItem(AVPlayerItemPlayability)Added AVPlayerItem(AVPlayerItemPresentation)Added AVPlayerItem(AVPlayerItemTimeControl)Added [AVPlayerItemTimeJumpedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1390911-avplayeritemtimejumped)AVVideoComposition.hAdded [-[AVVideoComposition isValidForAsset:timeRange:validationDelegate:]](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389917-isvalid)Added [AVVideoCompositionValidationHandling](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling)Added [-[AVVideoCompositionValidationHandling videoComposition:shouldContinueValidatingAfterFindingEmptyTimeRange:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1388620-videocomposition)Added [-[AVVideoCompositionValidationHandling videoComposition:shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1390721-videocomposition)Added [-[AVVideoCompositionValidationHandling videoComposition:shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:layerInstruction:asset:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1388452-videocomposition)Added [-[AVVideoCompositionValidationHandling videoComposition:shouldContinueValidatingAfterFindingInvalidValueForKey:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1389404-videocomposition)Added AVVideoComposition(AVVideoCompositionValidation)AVVideoSettings.hAdded [AVVideoProfileLevelH264Baseline41](https://developer.apple.com/documentation/avfoundation/avvideoprofilelevelh264baseline41)Added [AVVideoProfileLevelH264Main32](https://developer.apple.com/documentation/avfoundation/avvideoprofilelevelh264main32)Added [AVVideoProfileLevelH264Main41](https://developer.apple.com/documentation/avfoundation/avvideoprofilelevelh264main41)Added [AVVideoQualityKey](https://developer.apple.com/documentation/avfoundation/avvideoqualitykey)Added [AVVideoScalingModeFit](https://developer.apple.com/documentation/avfoundation/avvideoscalingmodefit)Added [AVVideoScalingModeKey](https://developer.apple.com/documentation/avfoundation/avvideoscalingmodekey)Added [AVVideoScalingModeResize](https://developer.apple.com/documentation/avfoundation/avvideoscalingmoderesize)Added [AVVideoScalingModeResizeAspect](https://developer.apple.com/documentation/avfoundation/avvideoscalingmoderesizeaspect)Added [AVVideoScalingModeResizeAspectFill](https://developer.apple.com/documentation/avfoundation/avvideoscalingmoderesizeaspectfill)

## CFNetwork

CFHTTPMessage.hAdded [kCFHTTPAuthenticationSchemeXMobileMeAuthToken](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemexmobilemeauthtoken)CFSocketStream.hAdded [kCFStreamNetworkServiceTypeBackground](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypebackground)Added [kCFStreamNetworkServiceTypeVideo](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevideo)Added [kCFStreamNetworkServiceTypeVoice](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevoice)Added [kCFStreamPropertySSLContext](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertysslcontext)

## CoreAudio

CoreAudioTypes.hAdded [kAudioFormatMPEG4AAC_ELD_SBR](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4aac_eld_sbr)

## CoreBluetooth

CBCentralManager.hAdded [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)Added [-[CBCentralManager cancelPeripheralConnection:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518952-cancelperipheralconnection)Added [-[CBCentralManager connectPeripheral:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518766-connect)Added [CBCentralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518944-delegate)Added [-[CBCentralManager initWithDelegate:queue:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518695-initwithdelegate)Added -[CBCentralManager retrieveConnectedPeripherals]Added -[CBCentralManager retrievePeripherals:]Added [-[CBCentralManager scanForPeripheralsWithServices:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518986-scanforperipheralswithservices)Added CBCentralManager.stateAdded [-[CBCentralManager stopScan]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518984-stopscan)Added [CBCentralManagerDelegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate)Added [-[CBCentralManagerDelegate centralManager:didConnectPeripheral:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518969-centralmanager)Added [-[CBCentralManagerDelegate centralManager:didDisconnectPeripheral:error:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518791-centralmanager)Added [-[CBCentralManagerDelegate centralManager:didDiscoverPeripheral:advertisementData:RSSI:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518937-centralmanager)Added [-[CBCentralManagerDelegate centralManager:didFailToConnectPeripheral:error:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518988-centralmanager)Added -[CBCentralManagerDelegate centralManager:didRetrieveConnectedPeripherals:]Added -[CBCentralManagerDelegate centralManager:didRetrievePeripherals:]Added [-[CBCentralManagerDelegate centralManagerDidUpdateState:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518888-centralmanagerdidupdatestate)Added [CBAdvertisementDataLocalNameKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatalocalnamekey)Added [CBAdvertisementDataManufacturerDataKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatamanufacturerdatakey)Added [CBAdvertisementDataServiceDataKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataservicedatakey)Added [CBAdvertisementDataServiceUUIDsKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataserviceuuidskey)Added [CBAdvertisementDataTxPowerLevelKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatatxpowerlevelkey)Added [CBCentralManagerScanOptionAllowDuplicatesKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerscanoptionallowduplicateskey)Added [CBCentralManagerState](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate)Added [CBCentralManagerStatePoweredOff](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstatepoweredoff)Added [CBCentralManagerStatePoweredOn](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/poweredon)Added [CBCentralManagerStateResetting](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstateresetting)Added [CBCentralManagerStateUnauthorized](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstateunauthorized)Added [CBCentralManagerStateUnknown](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/unknown)Added [CBCentralManagerStateUnsupported](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/unsupported)Added [CBConnectPeripheralOptionNotifyOnDisconnectionKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyondisconnectionkey)CBCharacteristic.hAdded [CBCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic)Added CBCharacteristic.UUIDAdded [CBCharacteristic.descriptors](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518957-descriptors)Added [CBCharacteristic.isBroadcasted](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518920-isbroadcasted)Added [CBCharacteristic.isNotifying](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1519057-isnotifying)Added [CBCharacteristic.properties](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1519010-properties)Added [CBCharacteristic.service](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518728-service)Added [CBCharacteristic.value](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518878-value)Added [CBCharacteristicProperties](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties)Added [CBCharacteristicPropertyAuthenticatedSignedWrites](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertyauthenticatedsignedwrites)Added [CBCharacteristicPropertyBroadcast](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1518871-broadcast)Added [CBCharacteristicPropertyExtendedProperties](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1518699-extendedproperties)Added [CBCharacteristicPropertyIndicate](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1519085-indicate)Added [CBCharacteristicPropertyNotify](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1518976-notify)Added [CBCharacteristicPropertyRead](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertyread)Added [CBCharacteristicPropertyWrite](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1519089-write)Added [CBCharacteristicPropertyWriteWithoutResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertywritewithoutresponse)CBDefines.hAdded #def CB_EXTERNAdded #def CB_EXTERN_CLASSCBDescriptor.hAdded [CBDescriptor](https://developer.apple.com/documentation/corebluetooth/cbdescriptor)Added CBDescriptor.UUIDAdded [CBDescriptor.characteristic](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1519035-characteristic)Added [CBDescriptor.value](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1518778-value)CBError.hAdded [CBATTError](https://developer.apple.com/documentation/corebluetooth/cbatterror)Added [CBATTErrorAttributeNotFound](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorattributenotfound)Added [CBATTErrorAttributeNotLong](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/attributenotlong)Added [CBATTErrorDomain](https://developer.apple.com/documentation/corebluetooth/cbatterrordomain)Added [CBATTErrorInsufficientAuthentication](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/insufficientauthentication)Added [CBATTErrorInsufficientAuthorization](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/insufficientauthorization)Added [CBATTErrorInsufficientEncryption](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/insufficientencryption)Added [CBATTErrorInsufficientEncryptionKeySize](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/insufficientencryptionkeysize)Added [CBATTErrorInsufficientResources](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinsufficientresources)Added [CBATTErrorInvalidAttributeValueLength](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/invalidattributevaluelength)Added [CBATTErrorInvalidHandle](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinvalidhandle)Added [CBATTErrorInvalidOffset](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinvalidoffset)Added [CBATTErrorInvalidPdu](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/invalidpdu)Added [CBATTErrorPrepareQueueFull](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorpreparequeuefull)Added [CBATTErrorReadNotPermitted](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/readnotpermitted)Added [CBATTErrorRequestNotSupported](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/requestnotsupported)Added [CBATTErrorUnlikelyError](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/unlikelyerror)Added [CBATTErrorUnsupportedGroupType](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorunsupportedgrouptype)Added [CBATTErrorWriteNotPermitted](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorwritenotpermitted)Added [CBError](https://developer.apple.com/documentation/corebluetooth/cberror)Added [CBErrorDomain](https://developer.apple.com/documentation/corebluetooth/cberrordomain)Added [CBErrorUnknown](https://developer.apple.com/documentation/corebluetooth/cberror/code/unknown)CBPeripheral.hAdded [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral)Added [CBPeripheral.RSSI](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518869-rssi)Added CBPeripheral.UUIDAdded [CBPeripheral.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518730-delegate)Added [-[CBPeripheral discoverCharacteristics:forService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518797-discovercharacteristics)Added [-[CBPeripheral discoverDescriptorsForCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519070-discoverdescriptors)Added [-[CBPeripheral discoverIncludedServices:forService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519014-discoverincludedservices)Added [-[CBPeripheral discoverServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518706-discoverservices)Added CBPeripheral.isConnectedAdded [CBPeripheral.name](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519029-name)Added [-[CBPeripheral readRSSI]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519111-readrssi)Added [-[CBPeripheral readValueForCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518759-readvalue)Added [-[CBPeripheral readValueForDescriptor:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518789-readvaluefordescriptor)Added [CBPeripheral.services](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518978-services)Added [-[CBPeripheral setNotifyValue:forCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518949-setnotifyvalue)Added [-[CBPeripheral writeValue:forCharacteristic:type:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518747-writevalue)Added [-[CBPeripheral writeValue:forDescriptor:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519107-writevalue)Added [CBPeripheralDelegate](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate)Added [-[CBPeripheralDelegate peripheral:didDiscoverCharacteristicsForService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518821-peripheral)Added [-[CBPeripheralDelegate peripheral:didDiscoverDescriptorsForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518785-peripheral)Added [-[CBPeripheralDelegate peripheral:didDiscoverIncludedServicesForService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519124-peripheral)Added [-[CBPeripheralDelegate peripheral:didDiscoverServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518744-peripheral)Added [-[CBPeripheralDelegate peripheral:didUpdateNotificationStateForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518768-peripheral)Added [-[CBPeripheralDelegate peripheral:didUpdateValueForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518708-peripheral)Added [-[CBPeripheralDelegate peripheral:didUpdateValueForDescriptor:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518929-peripheral)Added [-[CBPeripheralDelegate peripheral:didWriteValueForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518823-peripheral)Added [-[CBPeripheralDelegate peripheral:didWriteValueForDescriptor:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519062-peripheral)Added [-[CBPeripheralDelegate peripheralDidUpdateRSSI:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519083-peripheraldidupdaterssi)Added [CBCharacteristicWriteType](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype)Added [CBCharacteristicWriteWithResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype/cbcharacteristicwritewithresponse)Added [CBCharacteristicWriteWithoutResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype/withoutresponse)CBService.hAdded [CBService](https://developer.apple.com/documentation/corebluetooth/cbservice)Added CBService.UUIDAdded [CBService.characteristics](https://developer.apple.com/documentation/corebluetooth/cbservice/1434319-characteristics)Added [CBService.includedServices](https://developer.apple.com/documentation/corebluetooth/cbservice/1434324-includedservices)Added [CBService.peripheral](https://developer.apple.com/documentation/corebluetooth/cbservice/1434334-peripheral)CBUUID.hAdded [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid)Added [+[CBUUID UUIDWithCFUUID:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518861-uuidwithcfuuid)Added [+[CBUUID UUIDWithData:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518799-uuidwithdata)Added [+[CBUUID UUIDWithString:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1519025-uuidwithstring)Added [CBUUID.data](https://developer.apple.com/documentation/corebluetooth/cbuuid/1519007-data)Added CBUUIDAppearanceStringAdded [CBUUIDCharacteristicAggregateFormatString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicaggregateformatstring)Added [CBUUIDCharacteristicExtendedPropertiesString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicextendedpropertiesstring)Added [CBUUIDCharacteristicFormatString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicformatstring)Added [CBUUIDCharacteristicUserDescriptionString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicuserdescriptionstring)Added [CBUUIDClientCharacteristicConfigurationString](https://developer.apple.com/documentation/corebluetooth/cbuuidclientcharacteristicconfigurationstring)Added CBUUIDDeviceNameStringAdded CBUUIDGenericAccessProfileStringAdded CBUUIDGenericAttributeProfileStringAdded CBUUIDPeripheralPreferredConnectionParametersStringAdded CBUUIDPeripheralPrivacyFlagStringAdded CBUUIDReconnectionAddressStringAdded [CBUUIDServerCharacteristicConfigurationString](https://developer.apple.com/documentation/corebluetooth/cbuuidservercharacteristicconfigurationstring)Added CBUUIDServiceChangedString

## CoreData

CoreDataDefines.hAdded [#def NSCoreDataVersionNumber_iPhoneOS_4_1](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_4_1)Added [#def NSCoreDataVersionNumber_iPhoneOS_4_2](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_4_2)Added [#def NSCoreDataVersionNumber_iPhoneOS_4_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_4_3)CoreDataErrors.hAdded [NSPersistentStoreSaveConflictsError](https://developer.apple.com/documentation/coredata/nspersistentstoresaveconflictserror)Added [NSPersistentStoreSaveConflictsErrorKey](https://developer.apple.com/documentation/coredata/nspersistentstoresaveconflictserrorkey)Added [NSPersistentStoreUnsupportedRequestTypeError](https://developer.apple.com/documentation/coredata/nspersistentstoreunsupportedrequesttypeerror)NSAttributeDescription.hAdded [-[NSAttributeDescription allowsExternalBinaryDataStorage]](https://developer.apple.com/documentation/coredata/nsattributedescription/1498295-allowsexternalbinarydatastorage)Added [-[NSAttributeDescription setAllowsExternalBinaryDataStorage:]](https://developer.apple.com/documentation/coredata/nsattributedescription/1498295-allowsexternalbinarydatastorage)NSEntityDescription.hAdded [-[NSEntityDescription compoundIndexes]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425115-compoundindexes)Added [-[NSEntityDescription setCompoundIndexes:]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425115-compoundindexes)NSFetchRequest.hAdded [-[NSFetchRequest entityName]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506233-entityname)Added [+[NSFetchRequest fetchRequestWithEntityName:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1563437-fetchrequestwithentityname)Added [-[NSFetchRequest havingPredicate]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506429-havingpredicate)Added [-[NSFetchRequest init]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506679-init)Added [-[NSFetchRequest initWithEntityName:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506802-init)Added [-[NSFetchRequest propertiesToGroupBy]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506191-propertiestogroupby)Added [-[NSFetchRequest setHavingPredicate:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506429-havingpredicate)Added [-[NSFetchRequest setPropertiesToGroupBy:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506191-propertiestogroupby)Added [-[NSFetchRequest setShouldRefreshRefetchedObjects:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506440-shouldrefreshrefetchedobjects)Added [-[NSFetchRequest shouldRefreshRefetchedObjects]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506440-shouldrefreshrefetchedobjects)Added [NSCountResultType](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype/nscountresulttype)Modified [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest)

|  | Superclass | Protocols |
| --- | --- | --- |
| From | NSObject | NSCoding, NSCopying |
| To | NSPersistentStoreRequest | NSCoding |

NSIncrementalStore.hAdded [NSIncrementalStore](https://developer.apple.com/documentation/coredata/nsincrementalstore)Added [-[NSIncrementalStore executeRequest:withContext:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506653-execute)Added [+[NSIncrementalStore identifierForNewStoreAtURL:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506781-identifierfornewstore)Added [-[NSIncrementalStore loadMetadata:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506708-loadmetadata)Added [-[NSIncrementalStore managedObjectContextDidRegisterObjectsWithIDs:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506199-managedobjectcontextdidregistero)Added [-[NSIncrementalStore managedObjectContextDidUnregisterObjectsWithIDs:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506878-managedobjectcontextdidunregiste)Added [-[NSIncrementalStore newObjectIDForEntity:referenceObject:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506666-newobjectidforentity)Added [-[NSIncrementalStore newValueForRelationship:forObjectWithID:withContext:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506438-newvalueforrelationship)Added [-[NSIncrementalStore newValuesForObjectWithID:withContext:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506729-newvaluesforobjectwithid)Added [-[NSIncrementalStore obtainPermanentIDsForObjects:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506348-obtainpermanentids)Added [-[NSIncrementalStore referenceObjectForObjectID:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506828-referenceobjectforobjectid)NSIncrementalStoreNode.hAdded [NSIncrementalStoreNode](https://developer.apple.com/documentation/coredata/nsincrementalstorenode)Added [-[NSIncrementalStoreNode initWithObjectID:withValues:version:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506321-init)Added [-[NSIncrementalStoreNode objectID]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506827-objectid)Added [-[NSIncrementalStoreNode updateWithValues:version:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506721-updatewithvalues)Added [-[NSIncrementalStoreNode valueForPropertyDescription:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506442-value)Added [-[NSIncrementalStoreNode version]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506769-version)NSManagedObject.hAdded [-[NSManagedObject changedValuesForCurrentEvent]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506472-changedvaluesforcurrentevent)Added [-[NSManagedObject hasChanges]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506654-haschanges)NSManagedObjectContext.hAdded [-[NSManagedObjectContext concurrencyType]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506792-concurrencytype)Added [-[NSManagedObjectContext initWithConcurrencyType:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506709-init)Added [-[NSManagedObjectContext parentContext]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506529-parent)Added [-[NSManagedObjectContext performBlock:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506578-performblock)Added [-[NSManagedObjectContext performBlockAndWait:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506364-performblockandwait)Added -[NSManagedObjectContext setParentContext:]Added [-[NSManagedObjectContext userInfo]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506740-userinfo)Added [NSConfinementConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype)Added [NSMainQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsmainqueueconcurrencytype)Added [NSManagedObjectContextConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype)Added [NSPrivateQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsprivatequeueconcurrencytype)NSMergePolicy.hAdded [NSMergeConflict](https://developer.apple.com/documentation/coredata/nsmergeconflict)Added [NSMergeConflict.cachedSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506685-cachedsnapshot)Added [-[NSMergeConflict initWithSource:newVersion:oldVersion:cachedSnapshot:persistedSnapshot:]](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506216-init)Added [NSMergeConflict.newVersionNumber](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506190-newversionnumber)Added [NSMergeConflict.objectSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506454-objectsnapshot)Added [NSMergeConflict.oldVersionNumber](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506271-oldversionnumber)Added [NSMergeConflict.persistedSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506412-persistedsnapshot)Added [NSMergeConflict.sourceObject](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506809-sourceobject)Added [NSMergePolicy](https://developer.apple.com/documentation/coredata/nsmergepolicy)Added [-[NSMergePolicy initWithMergeType:]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506763-init)Added [NSMergePolicy.mergeType](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506675-mergetype)Added [-[NSMergePolicy resolveConflicts:error:]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506253-resolveconflicts)Added [NSErrorMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/nserrormergepolicytype)Added [NSMergeByPropertyObjectTrumpMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype)Added [NSMergeByPropertyStoreTrumpMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/mergebypropertystoretrumpmergepolicytype)Added [NSMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype)Added [NSOverwriteMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/nsoverwritemergepolicytype)Added [NSRollbackMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/nsrollbackmergepolicytype)NSMigrationManager.hAdded [-[NSMigrationManager setUsesStoreSpecificMigrationManager:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417606-usesstorespecificmigrationmanage)Added [-[NSMigrationManager usesStoreSpecificMigrationManager]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417606-usesstorespecificmigrationmanage)NSPersistentStoreCoordinator.hAdded [-[NSPersistentStoreCoordinator executeRequest:withContext:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468872-execute)Added [NSPersistentStoreDidImportUbiquitousContentChangesNotification](https://developer.apple.com/documentation/coredata/nspersistentstoredidimportubiquitouscontentchangesnotification)Added [NSPersistentStoreFileProtectionKey](https://developer.apple.com/documentation/coredata/nspersistentstorefileprotectionkey)Added [NSPersistentStoreUbiquitousContentNameKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontentnamekey)Added [NSPersistentStoreUbiquitousContentURLKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontenturlkey)NSPersistentStoreRequest.hAdded [NSPersistentStoreRequest](https://developer.apple.com/documentation/coredata/nspersistentstorerequest)Added [-[NSPersistentStoreRequest affectedStores]](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/1506844-affectedstores)Added [-[NSPersistentStoreRequest requestType]](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/1506892-requesttype)Added [-[NSPersistentStoreRequest setAffectedStores:]](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/1506844-affectedstores)Added [NSFetchRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/fetchrequesttype)Added [NSPersistentStoreRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype)Added [NSSaveRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/saverequesttype)NSPropertyDescription.hAdded [-[NSPropertyDescription isIndexedBySpotlight]](https://developer.apple.com/documentation/coredata/nspropertydescription/1506784-indexedbyspotlight)Added [-[NSPropertyDescription isStoredInExternalRecord]](https://developer.apple.com/documentation/coredata/nspropertydescription/1506260-isstoredinexternalrecord)Added [-[NSPropertyDescription setIndexedBySpotlight:]](https://developer.apple.com/documentation/coredata/nspropertydescription/1506784-isindexedbyspotlight)Added [-[NSPropertyDescription setStoredInExternalRecord:]](https://developer.apple.com/documentation/coredata/nspropertydescription/1506260-isstoredinexternalrecord)NSRelationshipDescription.hAdded [-[NSRelationshipDescription isOrdered]](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/1506382-isordered)Added [-[NSRelationshipDescription setOrdered:]](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/1506382-isordered)NSSaveChangesRequest.hAdded [NSSaveChangesRequest](https://developer.apple.com/documentation/coredata/nssavechangesrequest)Added [-[NSSaveChangesRequest deletedObjects]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500420-deletedobjects)Added [-[NSSaveChangesRequest initWithInsertedObjects:updatedObjects:deletedObjects:lockedObjects:]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500418-init)Added [-[NSSaveChangesRequest insertedObjects]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500416-insertedobjects)Added [-[NSSaveChangesRequest lockedObjects]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500426-lockedobjects)Added [-[NSSaveChangesRequest updatedObjects]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500424-updatedobjects)

## CoreFoundation

CFBase.hAdded #def CF_AUTOMATED_REFCOUNT_UNAVAILABLEAdded #def CF_AVAILABLE_IOSAdded #def CF_DEPRECATED_IOSAdded #def CF_RETURNS_NOT_RETAINEDCFCalendar.hAdded [kCFCalendarUnitWeekOfMonth](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533518-weekofmonth)Added [kCFCalendarUnitWeekOfYear](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/kcfcalendarunitweekofyear)Added [kCFCalendarUnitYearForWeekOfYear](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/kcfcalendarunityearforweekofyear)CFError.hAdded [kCFErrorFilePathKey](https://developer.apple.com/documentation/corefoundation/kcferrorfilepathkey)Added [kCFErrorURLKey](https://developer.apple.com/documentation/corefoundation/kcferrorurlkey)CFFileSecurity.hAdded [CFFileSecurityCopyAccessControlList()](https://developer.apple.com/documentation/corefoundation/1426508-cffilesecuritycopyaccesscontroll)Added [CFFileSecurityCopyGroupUUID()](https://developer.apple.com/documentation/corefoundation/1426512-cffilesecuritycopygroupuuid)Added [CFFileSecurityCopyOwnerUUID()](https://developer.apple.com/documentation/corefoundation/1426519-cffilesecuritycopyowneruuid)Added [CFFileSecurityCreate()](https://developer.apple.com/documentation/corefoundation/1426509-cffilesecuritycreate)Added [CFFileSecurityCreateCopy()](https://developer.apple.com/documentation/corefoundation/1426498-cffilesecuritycreatecopy)Added [CFFileSecurityGetGroup()](https://developer.apple.com/documentation/corefoundation/1426526-cffilesecuritygetgroup)Added [CFFileSecurityGetMode()](https://developer.apple.com/documentation/corefoundation/1426517-cffilesecuritygetmode)Added [CFFileSecurityGetOwner()](https://developer.apple.com/documentation/corefoundation/1426516-cffilesecuritygetowner)Added [CFFileSecurityGetTypeID()](https://developer.apple.com/documentation/corefoundation/1426530-cffilesecuritygettypeid)Added [CFFileSecurityRef](https://developer.apple.com/documentation/corefoundation/cffilesecurityref)Added [CFFileSecuritySetAccessControlList()](https://developer.apple.com/documentation/corefoundation/1426506-cffilesecuritysetaccesscontrolli)Added [CFFileSecuritySetGroup()](https://developer.apple.com/documentation/corefoundation/1426524-cffilesecuritysetgroup)Added [CFFileSecuritySetGroupUUID()](https://developer.apple.com/documentation/corefoundation/1426492-cffilesecuritysetgroupuuid)Added [CFFileSecuritySetMode()](https://developer.apple.com/documentation/corefoundation/1426496-cffilesecuritysetmode)Added [CFFileSecuritySetOwner()](https://developer.apple.com/documentation/corefoundation/1426528-cffilesecuritysetowner)Added [CFFileSecuritySetOwnerUUID()](https://developer.apple.com/documentation/corefoundation/1426494-cffilesecuritysetowneruuid)Added #def kCFFileSecurityRemoveACLCFRunLoop.hAdded [CFRunLoopObserverCreateWithHandler()](https://developer.apple.com/documentation/corefoundation/1542816-cfrunloopobservercreatewithhandl)Added [CFRunLoopTimerCreateWithHandler()](https://developer.apple.com/documentation/corefoundation/1542555-cfrunlooptimercreatewithhandler)CFURL.hRemoved [CFURLCreateBookmarkDataFromAliasRecord()](https://developer.apple.com/documentation/corefoundation/1542129-cfurlcreatebookmarkdatafromalias) (no architecture available)Added [kCFURLFileResourceIdentifierKey](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourceidentifierkey)Added [kCFURLFileResourceTypeBlockSpecial](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypeblockspecial)Added [kCFURLFileResourceTypeCharacterSpecial](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypecharacterspecial)Added [kCFURLFileResourceTypeDirectory](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypedirectory)Added [kCFURLFileResourceTypeKey](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypekey)Added [kCFURLFileResourceTypeNamedPipe](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypenamedpipe)Added [kCFURLFileResourceTypeRegular](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetyperegular)Added [kCFURLFileResourceTypeSocket](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypesocket)Added [kCFURLFileResourceTypeSymbolicLink](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypesymboliclink)Added [kCFURLFileResourceTypeUnknown](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypeunknown)Added [kCFURLFileSecurityKey](https://developer.apple.com/documentation/corefoundation/kcfurlfilesecuritykey)Added [kCFURLIsExecutableKey](https://developer.apple.com/documentation/corefoundation/kcfurlisexecutablekey)Added [kCFURLIsMountTriggerKey](https://developer.apple.com/documentation/corefoundation/kcfurlismounttriggerkey)Added [kCFURLIsReadableKey](https://developer.apple.com/documentation/corefoundation/kcfurlisreadablekey)Added [kCFURLIsUbiquitousItemKey](https://developer.apple.com/documentation/corefoundation/kcfurlisubiquitousitemkey)Added [kCFURLIsWritableKey](https://developer.apple.com/documentation/corefoundation/kcfurliswritablekey)Added [kCFURLKeysOfUnsetValuesKey](https://developer.apple.com/documentation/corefoundation/kcfurlkeysofunsetvalueskey)Added [kCFURLPreferredIOBlockSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurlpreferredioblocksizekey)Added [kCFURLTotalFileAllocatedSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurltotalfileallocatedsizekey)Added [kCFURLTotalFileSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurltotalfilesizekey)Added [kCFURLUbiquitousItemHasUnresolvedConflictsKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemhasunresolvedconflictskey)Added [kCFURLUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisdownloadedkey)Added [kCFURLUbiquitousItemIsDownloadingKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisdownloadingkey)Added [kCFURLUbiquitousItemIsUploadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisuploadedkey)Added [kCFURLUbiquitousItemIsUploadingKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisuploadingkey)Added [kCFURLUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentdownloadedkey)Added [kCFURLUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentuploadedkey)Added [kCFURLVolumeCreationDateKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumecreationdatekey)Added [kCFURLVolumeIdentifierKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeidentifierkey)Added [kCFURLVolumeIsAutomountedKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisautomountedkey)Added [kCFURLVolumeIsBrowsableKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisbrowsablekey)Added [kCFURLVolumeIsEjectableKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisejectablekey)Added [kCFURLVolumeIsInternalKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisinternalkey)Added [kCFURLVolumeIsLocalKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeislocalkey)Added [kCFURLVolumeIsReadOnlyKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisreadonlykey)Added [kCFURLVolumeIsRemovableKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisremovablekey)Added [kCFURLVolumeLocalizedNameKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumelocalizednamekey)Added [kCFURLVolumeMaximumFileSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumemaximumfilesizekey)Added [kCFURLVolumeNameKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumenamekey)Added [kCFURLVolumeSupportsAdvisoryFileLockingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsadvisoryfilelockingkey)Added [kCFURLVolumeSupportsExtendedSecurityKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsextendedsecuritykey)Added [kCFURLVolumeSupportsRenamingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsrenamingkey)Added [kCFURLVolumeSupportsRootDirectoryDatesKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsrootdirectorydateskey)Added [kCFURLVolumeSupportsVolumeSizesKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsvolumesizeskey)Added [kCFURLVolumeURLForRemountingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeurlforremountingkey)Added [kCFURLVolumeUUIDStringKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeuuidstringkey)Modified [kCFURLFileSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurlfilesizekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeResourceCountKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeresourcecountkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeURLKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeurlkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLHasHiddenExtensionKey](https://developer.apple.com/documentation/corefoundation/kcfurlhashiddenextensionkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLBookmarkCreationMinimalBookmarkMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/1541966-minimalbookmarkmask)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLLocalizedTypeDescriptionKey](https://developer.apple.com/documentation/corefoundation/kcfurllocalizedtypedescriptionkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeLocalizedFormatDescriptionKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumelocalizedformatdescriptionkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLIsSystemImmutableKey](https://developer.apple.com/documentation/corefoundation/kcfurlissystemimmutablekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeSupportsHardLinksKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportshardlinkskey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLBookmarkCreationPreferFileIDResolutionMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/kcfurlbookmarkcreationpreferfileidresolutionmask)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLSetResourcePropertiesForKeys()](https://developer.apple.com/documentation/corefoundation/1542947-cfurlsetresourcepropertiesforkey)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT Boolean CFURLSetResourcePropertiesForKeys ( CFURLRef url, CFDictionaryRef keyedPropertyValues, CFErrorRef \*error); |
| To | arm | Boolean CFURLSetResourcePropertiesForKeys ( CFURLRef url, CFDictionaryRef keyedPropertyValues, CFErrorRef \*error); |

Modified [kCFURLVolumeIsJournalingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisjournalingkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLEffectiveIconKey](https://developer.apple.com/documentation/corefoundation/kcfurleffectiveiconkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLCreationDateKey](https://developer.apple.com/documentation/corefoundation/kcfurlcreationdatekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLBookmarkCreationOptions](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeTotalCapacityKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumetotalcapacitykey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLSetResourcePropertyForKey()](https://developer.apple.com/documentation/corefoundation/1541607-cfurlsetresourcepropertyforkey)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT Boolean CFURLSetResourcePropertyForKey ( CFURLRef url, CFStringRef key, CFTypeRef propertValue, CFErrorRef \*error); |
| To | arm | Boolean CFURLSetResourcePropertyForKey ( CFURLRef url, CFStringRef key, CFTypeRef propertyValue, CFErrorRef \*error); |

Modified [CFURLResourceIsReachable()](https://developer.apple.com/documentation/corefoundation/1543666-cfurlresourceisreachable)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT Boolean CFURLResourceIsReachable ( CFURLRef url, CFErrorRef \*error); |
| To | arm | Boolean CFURLResourceIsReachable ( CFURLRef url, CFErrorRef \*error); |

Modified [kCFURLIsVolumeKey](https://developer.apple.com/documentation/corefoundation/kcfurlisvolumekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLCreateByResolvingBookmarkData()](https://developer.apple.com/documentation/corefoundation/1543252-cfurlcreatebyresolvingbookmarkda)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeSupportsPersistentIDsKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportspersistentidskey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeSupportsSymbolicLinksKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportssymboliclinkskey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLCopyResourcePropertyForKey()](https://developer.apple.com/documentation/corefoundation/1542764-cfurlcopyresourcepropertyforkey)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT Boolean CFURLCopyResourcePropertyForKey ( CFURLRef url, CFStringRef key, void \*propertyValueTypeRefPtr, CFErrorRef \*error); |
| To | arm | Boolean CFURLCopyResourcePropertyForKey ( CFURLRef url, CFStringRef key, void \*propertyValueTypeRefPtr, CFErrorRef \*error); |

Modified [CFURLClearResourcePropertyCache()](https://developer.apple.com/documentation/corefoundation/1541959-cfurlclearresourcepropertycache)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT void CFURLClearResourcePropertyCache ( CFURLRef url); |
| To | arm | void CFURLClearResourcePropertyCache ( CFURLRef url); |

Modified [kCFURLCustomIconKey](https://developer.apple.com/documentation/corefoundation/kcfurlcustomiconkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLAttributeModificationDateKey](https://developer.apple.com/documentation/corefoundation/kcfurlattributemodificationdatekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeSupportsCaseSensitiveNamesKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportscasesensitivenameskey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLCreateResourcePropertyForKeyFromBookmarkData()](https://developer.apple.com/documentation/corefoundation/1543031-cfurlcreateresourcepropertyforke)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeSupportsZeroRunsKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportszerorunskey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLIsRegularFileKey](https://developer.apple.com/documentation/corefoundation/kcfurlisregularfilekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLIsAliasFileKey](https://developer.apple.com/documentation/corefoundation/kcfurlisaliasfilekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLCreateBookmarkDataFromFile()](https://developer.apple.com/documentation/corefoundation/1543258-cfurlcreatebookmarkdatafromfile)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLCreateBookmarkData()](https://developer.apple.com/documentation/corefoundation/1542923-cfurlcreatebookmarkdata)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLCopyResourcePropertiesForKeys()](https://developer.apple.com/documentation/corefoundation/1542370-cfurlcopyresourcepropertiesforke)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT CFDictionaryRef CFURLCopyResourcePropertiesForKeys ( CFURLRef url, CFArrayRef keys, CFErrorRef \*error); |
| To | arm | CFDictionaryRef CFURLCopyResourcePropertiesForKeys ( CFURLRef url, CFArrayRef keys, CFErrorRef \*error); |

Modified [kCFURLFileAllocatedSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurlfileallocatedsizekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeSupportsCasePreservedNamesKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportscasepreservednameskey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLIsPackageKey](https://developer.apple.com/documentation/corefoundation/kcfurlispackagekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLLocalizedLabelKey](https://developer.apple.com/documentation/corefoundation/kcfurllocalizedlabelkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLBookmarkCreationSuitableForBookmarkFile](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/1542275-suitableforbookmarkfile)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFBookmarkResolutionWithoutUIMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions/kcfbookmarkresolutionwithoutuimask)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLNameKey](https://developer.apple.com/documentation/corefoundation/kcfurlnamekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLBookmarkResolutionOptions](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLClearResourcePropertyCacheForKey()](https://developer.apple.com/documentation/corefoundation/1542054-cfurlclearresourcepropertycachef)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT void CFURLClearResourcePropertyCacheForKey ( CFURLRef url, CFStringRef key); |
| To | arm | void CFURLClearResourcePropertyCacheForKey ( CFURLRef url, CFStringRef key); |

Modified [kCFURLParentDirectoryURLKey](https://developer.apple.com/documentation/corefoundation/kcfurlparentdirectoryurlkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLIsDirectoryKey](https://developer.apple.com/documentation/corefoundation/kcfurlisdirectorykey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLLabelNumberKey](https://developer.apple.com/documentation/corefoundation/kcfurllabelnumberkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLIsUserImmutableKey](https://developer.apple.com/documentation/corefoundation/kcfurlisuserimmutablekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLLabelColorKey](https://developer.apple.com/documentation/corefoundation/kcfurllabelcolorkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeSupportsJournalingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsjournalingkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLCreateFileReferenceURL()](https://developer.apple.com/documentation/corefoundation/1543282-cfurlcreatefilereferenceurl)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT CFURLRef CFURLCreateFileReferenceURL ( CFAllocatorRef allocator, CFURLRef url, CFErrorRef \*error); |
| To | arm | CFURLRef CFURLCreateFileReferenceURL ( CFAllocatorRef allocator, CFURLRef url, CFErrorRef \*error); |

Modified [kCFURLTypeIdentifierKey](https://developer.apple.com/documentation/corefoundation/kcfurltypeidentifierkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLBookmarkFileCreationOptions](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkfilecreationoptions)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLIsHiddenKey](https://developer.apple.com/documentation/corefoundation/kcfurlishiddenkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLContentModificationDateKey](https://developer.apple.com/documentation/corefoundation/kcfurlcontentmodificationdatekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLIsSymbolicLinkKey](https://developer.apple.com/documentation/corefoundation/kcfurlissymboliclinkkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLLocalizedNameKey](https://developer.apple.com/documentation/corefoundation/kcfurllocalizednamekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeAvailableCapacityKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeavailablecapacitykey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFBookmarkResolutionWithoutMountingMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions/1541888-cfbookmarkresolutionwithoutmount)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLSetTemporaryResourcePropertyForKey()](https://developer.apple.com/documentation/corefoundation/1542384-cfurlsettemporaryresourcepropert)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT void CFURLSetTemporaryResourcePropertyForKey ( CFURLRef url, CFStringRef key, CFTypeRef propertyValue); |
| To | arm | void CFURLSetTemporaryResourcePropertyForKey ( CFURLRef url, CFStringRef key, CFTypeRef propertyValue); |

Modified [kCFURLContentAccessDateKey](https://developer.apple.com/documentation/corefoundation/kcfurlcontentaccessdatekey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLCreateFilePathURL()](https://developer.apple.com/documentation/corefoundation/1542076-cfurlcreatefilepathurl)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT CFURLRef CFURLCreateFilePathURL ( CFAllocatorRef allocator, CFURLRef url, CFErrorRef \*error); |
| To | arm | CFURLRef CFURLCreateFilePathURL ( CFAllocatorRef allocator, CFURLRef url, CFErrorRef \*error); |

Modified [CFURLCreateResourcePropertiesForKeysFromBookmarkData()](https://developer.apple.com/documentation/corefoundation/1543621-cfurlcreateresourcepropertiesfor)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLWriteBookmarkDataToFile()](https://developer.apple.com/documentation/corefoundation/1541737-cfurlwritebookmarkdatatofile)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLLinkCountKey](https://developer.apple.com/documentation/corefoundation/kcfurllinkcountkey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLVolumeSupportsSparseFilesKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportssparsefileskey)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

CFURLEnumerator.hAdded [kCFURLEnumeratorDefaultBehavior](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/kcfurlenumeratordefaultbehavior)Added [kCFURLEnumeratorDirectoryPostOrderSuccess](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult/kcfurlenumeratordirectorypostordersuccess)Added [kCFURLEnumeratorIncludeDirectoriesPostOrder](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/1542791-includedirectoriespostorder)Added [kCFURLEnumeratorIncludeDirectoriesPreOrder](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/1541726-includedirectoriespreorder)Modified [CFURLEnumeratorSkipDescendents()](https://developer.apple.com/documentation/corefoundation/1541451-cfurlenumeratorskipdescendents)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT void CFURLEnumeratorSkipDescendents ( CFURLEnumeratorRef enumerator); |
| To | arm | void CFURLEnumeratorSkipDescendents ( CFURLEnumeratorRef enumerator); |

Modified [kCFURLEnumeratorEnd](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult/end)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLEnumeratorGetDescendentLevel()](https://developer.apple.com/documentation/corefoundation/1542086-cfurlenumeratorgetdescendentleve)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT CFIndex CFURLEnumeratorGetDescendentLevel ( CFURLEnumeratorRef enumerator); |
| To | arm | CFIndex CFURLEnumeratorGetDescendentLevel ( CFURLEnumeratorRef enumerator); |

Modified [CFURLEnumeratorResult](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLEnumeratorGetTypeID()](https://developer.apple.com/documentation/corefoundation/1542687-cfurlenumeratorgettypeid)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT CFTypeID CFURLEnumeratorGetTypeID ( void); |
| To | arm | CFTypeID CFURLEnumeratorGetTypeID ( void); |

Modified [kCFURLEnumeratorSkipInvisibles](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/kcfurlenumeratorskipinvisibles)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLEnumeratorSuccess](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult/success)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLEnumeratorGetSourceDidChange()](https://developer.apple.com/documentation/corefoundation/1575035-cfurlenumeratorgetsourcedidchang)

|  | Deprecation | Architectures | Declaration |
| --- | --- | --- | --- |
| From | _none_ | Unknown | CF_EXPORT Boolean CFURLEnumeratorGetSourceDidChange ( CFURLEnumeratorRef enumerator); |
| To | iOS 5.0 | arm | Boolean CFURLEnumeratorGetSourceDidChange ( CFURLEnumeratorRef enumerator); |

Modified [CFURLEnumeratorCreateForMountedVolumes()](https://developer.apple.com/documentation/corefoundation/1542110-cfurlenumeratorcreateformountedv)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT CFURLEnumeratorRef CFURLEnumeratorCreateForMountedVolumes ( CFAllocatorRef alloc, CFURLEnumeratorOptions option, CFArrayRef propertyKeys); |
| To | arm | CFURLEnumeratorRef CFURLEnumeratorCreateForMountedVolumes ( CFAllocatorRef alloc, CFURLEnumeratorOptions option, CFArrayRef propertyKeys); |

Modified [CFURLEnumeratorOptions](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLEnumeratorSkipPackageContents](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/kcfurlenumeratorskippackagecontents)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLEnumeratorError](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult/error)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLEnumeratorGenerateFileReferenceURLs](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/kcfurlenumeratorgeneratefilereferenceurls)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLEnumeratorCreateForDirectoryURL()](https://developer.apple.com/documentation/corefoundation/1543646-cfurlenumeratorcreatefordirector)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT CFURLEnumeratorRef CFURLEnumeratorCreateForDirectoryURL ( CFAllocatorRef alloc, CFURLRef directoryURL, CFURLEnumeratorOptions option, CFArrayRef propertyKeys); |
| To | arm | CFURLEnumeratorRef CFURLEnumeratorCreateForDirectoryURL ( CFAllocatorRef alloc, CFURLRef directoryURL, CFURLEnumeratorOptions option, CFArrayRef propertyKeys); |

Modified [CFURLEnumeratorRef](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorref)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [kCFURLEnumeratorDescendRecursively](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/1542771-descendrecursively)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

Modified [CFURLEnumeratorGetNextURL()](https://developer.apple.com/documentation/corefoundation/1542747-cfurlenumeratorgetnexturl)

|  | Architectures | Declaration |
| --- | --- | --- |
| From | Unknown | CF_EXPORT CFURLEnumeratorResult CFURLEnumeratorGetNextURL ( CFURLEnumeratorRef enumerator, CFURLRef \*url, CFErrorRef \*error); |
| To | arm | CFURLEnumeratorResult CFURLEnumeratorGetNextURL ( CFURLEnumeratorRef enumerator, CFURLRef \*url, CFErrorRef \*error); |

CFUtilities.hAdded [CFCopyHomeDirectoryURL()](https://developer.apple.com/documentation/corefoundation/1620446-cfcopyhomedirectoryurl)

## CoreGraphics

CGPath.hAdded [CGPathAddRelativeArc()](https://developer.apple.com/documentation/coregraphics/1411136-cgpathaddrelativearc)Added [CGPathCreateCopyByDashingPath()](https://developer.apple.com/documentation/coregraphics/cgpath/1411134-init)Added [CGPathCreateCopyByStrokingPath()](https://developer.apple.com/documentation/coregraphics/cgpath/1411128-init)Added [CGPathCreateCopyByTransformingPath()](https://developer.apple.com/documentation/coregraphics/cgpath/1411161-copy)Added [CGPathCreateMutableCopyByTransformingPath()](https://developer.apple.com/documentation/coregraphics/1411150-cgpathcreatemutablecopybytransfo)Added [CGPathCreateWithEllipseInRect()](https://developer.apple.com/documentation/coregraphics/1411177-cgpathcreatewithellipseinrect)Added [CGPathCreateWithRect()](https://developer.apple.com/documentation/coregraphics/cgpath/1411155-init)Modified [CGLineCap](https://developer.apple.com/documentation/coregraphics/cglinecap)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineCapSquare](https://developer.apple.com/documentation/coregraphics/cglinecap/square)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineJoinBevel](https://developer.apple.com/documentation/coregraphics/cglinejoin/bevel)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineJoinRound](https://developer.apple.com/documentation/coregraphics/cglinejoin/kcglinejoinround)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [CGLineJoin](https://developer.apple.com/documentation/coregraphics/cglinejoin)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineJoinMiter](https://developer.apple.com/documentation/coregraphics/cglinejoin/kcglinejoinmiter)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineCapRound](https://developer.apple.com/documentation/coregraphics/cglinecap/kcglinecapround)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineCapButt](https://developer.apple.com/documentation/coregraphics/cglinecap/kcglinecapbutt)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

## CoreImage

CIColor.hAdded [CIColor](https://developer.apple.com/documentation/coreimage/cicolor)Added [-[CIColor alpha]](https://developer.apple.com/documentation/coreimage/cicolor/1437981-alpha)Added [-[CIColor blue]](https://developer.apple.com/documentation/coreimage/cicolor/1438033-blue)Added [-[CIColor colorSpace]](https://developer.apple.com/documentation/coreimage/cicolor/1437917-colorspace)Added [+[CIColor colorWithCGColor:]](https://developer.apple.com/documentation/coreimage/cicolor/1502106-colorwithcgcolor)Added [+[CIColor colorWithRed:green:blue:]](https://developer.apple.com/documentation/coreimage/cicolor/1437941-colorwithred)Added [+[CIColor colorWithRed:green:blue:alpha:]](https://developer.apple.com/documentation/coreimage/cicolor/1502111-colorwithred)Added [+[CIColor colorWithString:]](https://developer.apple.com/documentation/coreimage/cicolor/1438059-init)Added [-[CIColor components]](https://developer.apple.com/documentation/coreimage/cicolor/1437862-components)Added [-[CIColor green]](https://developer.apple.com/documentation/coreimage/cicolor/1437607-green)Added [-[CIColor initWithCGColor:]](https://developer.apple.com/documentation/coreimage/cicolor/1437821-init)Added [-[CIColor numberOfComponents]](https://developer.apple.com/documentation/coreimage/cicolor/1438151-numberofcomponents)Added [-[CIColor red]](https://developer.apple.com/documentation/coreimage/cicolor/1437969-red)Added [-[CIColor stringRepresentation]](https://developer.apple.com/documentation/coreimage/cicolor/1437910-stringrepresentation)CIContext.hAdded [CIContext](https://developer.apple.com/documentation/coreimage/cicontext)Added [+[CIContext contextWithEAGLContext:]](https://developer.apple.com/documentation/coreimage/cicontext/1620419-contextwitheaglcontext)Added [+[CIContext contextWithEAGLContext:options:]](https://developer.apple.com/documentation/coreimage/cicontext/1620362-contextwitheaglcontext)Added [+[CIContext contextWithOptions:]](https://developer.apple.com/documentation/coreimage/cicontext/1438261-init)Added [-[CIContext createCGImage:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1437784-createcgimage)Added [-[CIContext createCGImage:fromRect:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicontext/1437978-createcgimage)Added [-[CIContext drawImage:atPoint:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1473521-drawimage)Added [-[CIContext drawImage:inRect:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1437786-drawimage)Added [-[CIContext inputImageMaximumSize]](https://developer.apple.com/documentation/coreimage/cicontext/1620425-inputimagemaximumsize)Added [-[CIContext outputImageMaximumSize]](https://developer.apple.com/documentation/coreimage/cicontext/1620335-outputimagemaximumsize)Added [-[CIContext render:toBitmap:rowBytes:bounds:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicontext/1437897-render)Added [-[CIContext render:toCVPixelBuffer:]](https://developer.apple.com/documentation/coreimage/cicontext/1437853-render)Added [-[CIContext render:toCVPixelBuffer:bounds:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicontext/1437835-render)CIDetector.hAdded [CIDetector](https://developer.apple.com/documentation/coreimage/cidetector)Added [+[CIDetector detectorOfType:context:options:]](https://developer.apple.com/documentation/coreimage/cidetector/1437884-init)Added [-[CIDetector featuresInImage:]](https://developer.apple.com/documentation/coreimage/cidetector/1438049-featuresinimage)Added [-[CIDetector featuresInImage:options:]](https://developer.apple.com/documentation/coreimage/cidetector/1438189-features)Added [CIDetectorAccuracy](https://developer.apple.com/documentation/coreimage/cidetectoraccuracy)Added [CIDetectorAccuracyHigh](https://developer.apple.com/documentation/coreimage/cidetectoraccuracyhigh)Added [CIDetectorAccuracyLow](https://developer.apple.com/documentation/coreimage/cidetectoraccuracylow)Added [CIDetectorImageOrientation](https://developer.apple.com/documentation/coreimage/cidetectorimageorientation)Added [CIDetectorTypeFace](https://developer.apple.com/documentation/coreimage/cidetectortypeface)CIFeature.hAdded [CIFaceFeature](https://developer.apple.com/documentation/coreimage/cifacefeature)Added [CIFaceFeature.hasLeftEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437900-haslefteyeposition)Added [CIFaceFeature.hasMouthPosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437976-hasmouthposition)Added [CIFaceFeature.hasRightEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438076-hasrighteyeposition)Added [CIFaceFeature.leftEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437923-lefteyeposition)Added [CIFaceFeature.mouthPosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438020-mouthposition)Added [CIFaceFeature.rightEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438213-righteyeposition)Added [CIFeature](https://developer.apple.com/documentation/coreimage/cifeature)Added [CIFeature.bounds](https://developer.apple.com/documentation/coreimage/cifeature/1437782-bounds)Added [CIFeature.type](https://developer.apple.com/documentation/coreimage/cifeature/1438092-type)Added [CIFeatureTypeFace](https://developer.apple.com/documentation/coreimage/cifeaturetypeface)CIFilter.hAdded [CIFilter](https://developer.apple.com/documentation/coreimage/cifilter)Added [-[CIFilter attributes]](https://developer.apple.com/documentation/coreimage/cifilter/1437661-attributes)Added [+[CIFilter filterNamesInCategories:]](https://developer.apple.com/documentation/coreimage/cifilter/1437595-filternamesincategories)Added [+[CIFilter filterNamesInCategory:]](https://developer.apple.com/documentation/coreimage/cifilter/1438145-filternames)Added [+[CIFilter filterWithName:]](https://developer.apple.com/documentation/coreimage/cifilter/1438255-filterwithname)Added [+[CIFilter filterWithName:keysAndValues:]](https://developer.apple.com/documentation/coreimage/cifilter/1562057-filterwithname)Added [-[CIFilter inputKeys]](https://developer.apple.com/documentation/coreimage/cifilter/1438013-inputkeys)Added [-[CIFilter name]](https://developer.apple.com/documentation/coreimage/cifilter/1437997-name)Added [CIFilter.outputImage](https://developer.apple.com/documentation/coreimage/cifilter/1438169-outputimage)Added [-[CIFilter outputKeys]](https://developer.apple.com/documentation/coreimage/cifilter/1438122-outputkeys)Added [-[CIFilter setDefaults]](https://developer.apple.com/documentation/coreimage/cifilter/1437902-setdefaults)Added CIFilter(CIFilterRegistry)Added [kCIAttributeClass](https://developer.apple.com/documentation/coreimage/kciattributeclass)Added [kCIAttributeDefault](https://developer.apple.com/documentation/coreimage/kciattributedefault)Added [kCIAttributeDisplayName](https://developer.apple.com/documentation/coreimage/kciattributedisplayname)Added [kCIAttributeFilterCategories](https://developer.apple.com/documentation/coreimage/kciattributefiltercategories)Added [kCIAttributeFilterDisplayName](https://developer.apple.com/documentation/coreimage/kciattributefilterdisplayname)Added [kCIAttributeFilterName](https://developer.apple.com/documentation/coreimage/kciattributefiltername)Added [kCIAttributeIdentity](https://developer.apple.com/documentation/coreimage/kciattributeidentity)Added [kCIAttributeMax](https://developer.apple.com/documentation/coreimage/kciattributemax)Added [kCIAttributeMin](https://developer.apple.com/documentation/coreimage/kciattributemin)Added [kCIAttributeName](https://developer.apple.com/documentation/coreimage/kciattributename)Added [kCIAttributeSliderMax](https://developer.apple.com/documentation/coreimage/kciattributeslidermax)Added [kCIAttributeSliderMin](https://developer.apple.com/documentation/coreimage/kciattributeslidermin)Added [kCIAttributeType](https://developer.apple.com/documentation/coreimage/kciattributetype)Added [kCIAttributeTypeAngle](https://developer.apple.com/documentation/coreimage/kciattributetypeangle)Added [kCIAttributeTypeBoolean](https://developer.apple.com/documentation/coreimage/kciattributetypeboolean)Added [kCIAttributeTypeColor](https://developer.apple.com/documentation/coreimage/kciattributetypecolor)Added [kCIAttributeTypeCount](https://developer.apple.com/documentation/coreimage/kciattributetypecount)Added [kCIAttributeTypeDistance](https://developer.apple.com/documentation/coreimage/kciattributetypedistance)Added [kCIAttributeTypeImage](https://developer.apple.com/documentation/coreimage/kciattributetypeimage)Added [kCIAttributeTypeInteger](https://developer.apple.com/documentation/coreimage/kciattributetypeinteger)Added [kCIAttributeTypeOffset](https://developer.apple.com/documentation/coreimage/kciattributetypeoffset)Added [kCIAttributeTypePosition](https://developer.apple.com/documentation/coreimage/kciattributetypeposition)Added [kCIAttributeTypePosition3](https://developer.apple.com/documentation/coreimage/kciattributetypeposition3)Added [kCIAttributeTypeRectangle](https://developer.apple.com/documentation/coreimage/kciattributetyperectangle)Added [kCIAttributeTypeScalar](https://developer.apple.com/documentation/coreimage/kciattributetypescalar)Added [kCIAttributeTypeTime](https://developer.apple.com/documentation/coreimage/kciattributetypetime)Added [kCIAttributeTypeTransform](https://developer.apple.com/documentation/coreimage/kciattributetypetransform)Added kCICategoryApplePrivateAdded [kCICategoryBlur](https://developer.apple.com/documentation/coreimage/kcicategoryblur)Added [kCICategoryBuiltIn](https://developer.apple.com/documentation/coreimage/kcicategorybuiltin)Added [kCICategoryColorAdjustment](https://developer.apple.com/documentation/coreimage/kcicategorycoloradjustment)Added [kCICategoryColorEffect](https://developer.apple.com/documentation/coreimage/kcicategorycoloreffect)Added [kCICategoryCompositeOperation](https://developer.apple.com/documentation/coreimage/kcicategorycompositeoperation)Added [kCICategoryDistortionEffect](https://developer.apple.com/documentation/coreimage/kcicategorydistortioneffect)Added [kCICategoryGenerator](https://developer.apple.com/documentation/coreimage/kcicategorygenerator)Added [kCICategoryGeometryAdjustment](https://developer.apple.com/documentation/coreimage/kcicategorygeometryadjustment)Added [kCICategoryGradient](https://developer.apple.com/documentation/coreimage/kcicategorygradient)Added [kCICategoryHalftoneEffect](https://developer.apple.com/documentation/coreimage/kcicategoryhalftoneeffect)Added [kCICategoryHighDynamicRange](https://developer.apple.com/documentation/coreimage/kcicategoryhighdynamicrange)Added [kCICategoryInterlaced](https://developer.apple.com/documentation/coreimage/kcicategoryinterlaced)Added [kCICategoryNonSquarePixels](https://developer.apple.com/documentation/coreimage/kcicategorynonsquarepixels)Added [kCICategoryReduction](https://developer.apple.com/documentation/coreimage/kcicategoryreduction)Added [kCICategorySharpen](https://developer.apple.com/documentation/coreimage/kcicategorysharpen)Added [kCICategoryStillImage](https://developer.apple.com/documentation/coreimage/kcicategorystillimage)Added [kCICategoryStylize](https://developer.apple.com/documentation/coreimage/kcicategorystylize)Added [kCICategoryTileEffect](https://developer.apple.com/documentation/coreimage/kcicategorytileeffect)Added [kCICategoryTransition](https://developer.apple.com/documentation/coreimage/kcicategorytransition)Added [kCICategoryVideo](https://developer.apple.com/documentation/coreimage/kcicategoryvideo)Added [kCIInputBackgroundImageKey](https://developer.apple.com/documentation/coreimage/kciinputbackgroundimagekey)Added [kCIInputImageKey](https://developer.apple.com/documentation/coreimage/kciinputimagekey)Added [kCIOutputImageKey](https://developer.apple.com/documentation/coreimage/kcioutputimagekey)CIImage.hAdded [CIImage](https://developer.apple.com/documentation/coreimage/ciimage)Added [-[CIImage autoAdjustmentFilters]](https://developer.apple.com/documentation/coreimage/ciimage/1645889-autoadjustmentfilters)Added [-[CIImage autoAdjustmentFiltersWithOptions:]](https://developer.apple.com/documentation/coreimage/ciimage/1437792-autoadjustmentfilters)Added [+[CIImage emptyImage]](https://developer.apple.com/documentation/coreimage/ciimage/1438023-emptyimage)Added [-[CIImage extent]](https://developer.apple.com/documentation/coreimage/ciimage/1437996-extent)Added [-[CIImage imageByApplyingTransform:]](https://developer.apple.com/documentation/coreimage/ciimage/1438203-imagebyapplyingtransform)Added [-[CIImage imageByCroppingToRect:]](https://developer.apple.com/documentation/coreimage/ciimage/1437833-imagebycroppingtorect)Added [+[CIImage imageWithBitmapData:bytesPerRow:size:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1547023-imagewithbitmapdata)Added [+[CIImage imageWithCGImage:]](https://developer.apple.com/documentation/coreimage/ciimage/1547025-imagewithcgimage)Added [+[CIImage imageWithCGImage:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547021-imagewithcgimage)Added [+[CIImage imageWithCVPixelBuffer:]](https://developer.apple.com/documentation/coreimage/ciimage/1547005-imagewithcvpixelbuffer)Added [+[CIImage imageWithCVPixelBuffer:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547003-imagewithcvpixelbuffer)Added [+[CIImage imageWithColor:]](https://developer.apple.com/documentation/coreimage/ciimage/1547012-imagewithcolor)Added [+[CIImage imageWithContentsOfURL:]](https://developer.apple.com/documentation/coreimage/ciimage/1547027-imagewithcontentsofurl)Added [+[CIImage imageWithContentsOfURL:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1546997-imagewithcontentsofurl)Added [+[CIImage imageWithData:]](https://developer.apple.com/documentation/coreimage/ciimage/1547029-imagewithdata)Added [+[CIImage imageWithData:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547016-imagewithdata)Added [-[CIImage initWithBitmapData:bytesPerRow:size:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1437857-init)Added [-[CIImage initWithCGImage:]](https://developer.apple.com/documentation/coreimage/ciimage/1437986-initwithcgimage)Added [-[CIImage initWithCGImage:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437764-initwithcgimage)Added [-[CIImage initWithCVPixelBuffer:]](https://developer.apple.com/documentation/coreimage/ciimage/1438072-initwithcvpixelbuffer)Added [-[CIImage initWithCVPixelBuffer:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1438209-initwithcvpixelbuffer)Added [-[CIImage initWithColor:]](https://developer.apple.com/documentation/coreimage/ciimage/1437947-initwithcolor)Added [-[CIImage initWithContentsOfURL:]](https://developer.apple.com/documentation/coreimage/ciimage/1437908-initwithcontentsofurl)Added [-[CIImage initWithContentsOfURL:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437867-initwithcontentsofurl)Added [-[CIImage initWithData:]](https://developer.apple.com/documentation/coreimage/ciimage/1437925-initwithdata)Added [-[CIImage initWithData:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1438032-init)Added [-[CIImage properties]](https://developer.apple.com/documentation/coreimage/ciimage/1437733-properties)Added CIImage(AutoAdjustment)CIVector.hAdded [CIVector](https://developer.apple.com/documentation/coreimage/civector)Added [-[CIVector CGAffineTransformValue]](https://developer.apple.com/documentation/coreimage/civector/1438249-cgaffinetransformvalue)Added [-[CIVector CGPointValue]](https://developer.apple.com/documentation/coreimage/civector/1437672-cgpointvalue)Added [-[CIVector CGRectValue]](https://developer.apple.com/documentation/coreimage/civector/1438108-cgrectvalue)Added [-[CIVector W]](https://developer.apple.com/documentation/coreimage/civector/1438058-w)Added [-[CIVector X]](https://developer.apple.com/documentation/coreimage/civector/1437738-x)Added [-[CIVector Y]](https://developer.apple.com/documentation/coreimage/civector/1437843-y)Added [-[CIVector Z]](https://developer.apple.com/documentation/coreimage/civector/1437627-z)Added [-[CIVector count]](https://developer.apple.com/documentation/coreimage/civector/1438197-count)Added [-[CIVector initWithCGAffineTransform:]](https://developer.apple.com/documentation/coreimage/civector/1438102-initwithcgaffinetransform)Added [-[CIVector initWithCGPoint:]](https://developer.apple.com/documentation/coreimage/civector/1438133-initwithcgpoint)Added [-[CIVector initWithCGRect:]](https://developer.apple.com/documentation/coreimage/civector/1437644-init)Added [-[CIVector initWithString:]](https://developer.apple.com/documentation/coreimage/civector/1437938-initwithstring)Added [-[CIVector initWithValues:count:]](https://developer.apple.com/documentation/coreimage/civector/1437849-init)Added [-[CIVector initWithX:]](https://developer.apple.com/documentation/coreimage/civector/1437657-init)Added [-[CIVector initWithX:Y:]](https://developer.apple.com/documentation/coreimage/civector/1437865-init)Added [-[CIVector initWithX:Y:Z:]](https://developer.apple.com/documentation/coreimage/civector/1438056-initwithx)Added [-[CIVector initWithX:Y:Z:W:]](https://developer.apple.com/documentation/coreimage/civector/1438088-init)Added [-[CIVector stringRepresentation]](https://developer.apple.com/documentation/coreimage/civector/1437752-stringrepresentation)Added [-[CIVector valueAtIndex:]](https://developer.apple.com/documentation/coreimage/civector/1438207-valueatindex)Added [+[CIVector vectorWithCGAffineTransform:]](https://developer.apple.com/documentation/coreimage/civector/1564090-vectorwithcgaffinetransform)Added [+[CIVector vectorWithCGPoint:]](https://developer.apple.com/documentation/coreimage/civector/1564086-vectorwithcgpoint)Added [+[CIVector vectorWithCGRect:]](https://developer.apple.com/documentation/coreimage/civector/1564085-vectorwithcgrect)Added [+[CIVector vectorWithString:]](https://developer.apple.com/documentation/coreimage/civector/1564093-vectorwithstring)Added [+[CIVector vectorWithValues:count:]](https://developer.apple.com/documentation/coreimage/civector/1564088-vectorwithvalues)Added [+[CIVector vectorWithX:]](https://developer.apple.com/documentation/coreimage/civector/1564092-vectorwithx)Added [+[CIVector vectorWithX:Y:]](https://developer.apple.com/documentation/coreimage/civector/1564091-vectorwithx)Added [+[CIVector vectorWithX:Y:Z:]](https://developer.apple.com/documentation/coreimage/civector/1564089-vectorwithx)Added [+[CIVector vectorWithX:Y:Z:W:]](https://developer.apple.com/documentation/coreimage/civector/1564087-vectorwithx)CoreImageDefines.hAdded #def CI_EXTERN_C_BEGINAdded #def CI_EXTERN_C_ENDAdded #def COREIMAGEDEFINES_HAdded #def CORE_IMAGE_CLASS_EXPORTAdded #def CORE_IMAGE_EXPORT

## CoreLocation

CLAvailability.hAdded #def CL_EXTERNCLError.hAdded [kCLErrorGeocodeCanceled](https://developer.apple.com/documentation/corelocation/clerror/kclerrorgeocodecanceled)Added [kCLErrorGeocodeFoundNoResult](https://developer.apple.com/documentation/corelocation/clerror/code/geocodefoundnoresult)Added [kCLErrorGeocodeFoundPartialResult](https://developer.apple.com/documentation/corelocation/clerror/kclerrorgeocodefoundpartialresult)Added [kCLErrorRegionMonitoringResponseDelayed](https://developer.apple.com/documentation/corelocation/clerror/code/regionmonitoringresponsedelayed)Added [kCLErrorUserInfoAlternateRegionKey](https://developer.apple.com/documentation/corelocation/kclerroruserinfoalternateregionkey)CLGeocoder.hAdded [CLGeocoder](https://developer.apple.com/documentation/corelocation/clgeocoder)Added [-[CLGeocoder cancelGeocode]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423562-cancelgeocode)Added [-[CLGeocoder geocodeAddressDictionary:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423693-geocodeaddressdictionary)Added [-[CLGeocoder geocodeAddressString:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423509-geocodeaddressstring)Added [-[CLGeocoder geocodeAddressString:inRegion:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423591-geocodeaddressstring)Added [CLGeocoder.geocoding](https://developer.apple.com/documentation/corelocation/clgeocoder/1423765-geocoding)Added [-[CLGeocoder reverseGeocodeLocation:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423621-reversegeocodelocation)Added [CLGeocodeCompletionHandler](https://developer.apple.com/documentation/corelocation/clgeocodecompletionhandler)CLLocationManager.hAdded [-[CLLocationManager startMonitoringForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423656-startmonitoringforregion)CLLocationManagerDelegate.hAdded [-[CLLocationManagerDelegate locationManager:didStartMonitoringForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423842-locationmanager)CLPlacemark.hAdded [CLPlacemark](https://developer.apple.com/documentation/corelocation/clplacemark)Added [CLPlacemark.ISOcountryCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423796-isocountrycode)Added [CLPlacemark.addressDictionary](https://developer.apple.com/documentation/corelocation/clplacemark/1423605-addressdictionary)Added [CLPlacemark.administrativeArea](https://developer.apple.com/documentation/corelocation/clplacemark/1423628-administrativearea)Added [CLPlacemark.areasOfInterest](https://developer.apple.com/documentation/corelocation/clplacemark/1423673-areasofinterest)Added [CLPlacemark.country](https://developer.apple.com/documentation/corelocation/clplacemark/1423800-country)Added [-[CLPlacemark initWithPlacemark:]](https://developer.apple.com/documentation/corelocation/clplacemark/1423818-init)Added [CLPlacemark.inlandWater](https://developer.apple.com/documentation/corelocation/clplacemark/1423738-inlandwater)Added [CLPlacemark.locality](https://developer.apple.com/documentation/corelocation/clplacemark/1423507-locality)Added [CLPlacemark.location](https://developer.apple.com/documentation/corelocation/clplacemark/1423603-location)Added [CLPlacemark.name](https://developer.apple.com/documentation/corelocation/clplacemark/1423634-name)Added [CLPlacemark.ocean](https://developer.apple.com/documentation/corelocation/clplacemark/1423619-ocean)Added [CLPlacemark.postalCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423851-postalcode)Added [CLPlacemark.region](https://developer.apple.com/documentation/corelocation/clplacemark/1423808-region)Added [CLPlacemark.subAdministrativeArea](https://developer.apple.com/documentation/corelocation/clplacemark/1423776-subadministrativearea)Added [CLPlacemark.subLocality](https://developer.apple.com/documentation/corelocation/clplacemark/1423794-sublocality)Added [CLPlacemark.subThoroughfare](https://developer.apple.com/documentation/corelocation/clplacemark/1423782-subthoroughfare)Added [CLPlacemark.thoroughfare](https://developer.apple.com/documentation/corelocation/clplacemark/1423814-thoroughfare)

## CoreMedia

CMFormatDescription.hAdded [kCMTextDisplayFlag_obeySubtitleFormatting](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_obeysubtitleformatting)CMSampleBuffer.hAdded [kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotificationparameter_maxupcomingoutputpts)

## CoreMIDI

No changes

## CoreMotion

CMAttitude.hAdded [CMAttitudeReferenceFrame](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)Added [CMAttitudeReferenceFrameXArbitraryCorrectedZVertical](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/1615969-xarbitrarycorrectedzvertical)Added [CMAttitudeReferenceFrameXArbitraryZVertical](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/cmattitudereferenceframexarbitraryzvertical)Added [CMAttitudeReferenceFrameXMagneticNorthZVertical](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/cmattitudereferenceframexmagneticnorthzvertical)Added [CMAttitudeReferenceFrameXTrueNorthZVertical](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/cmattitudereferenceframextruenorthzvertical)CMDeviceMotion.hAdded [CMDeviceMotion.magneticField](https://developer.apple.com/documentation/coremotion/cmdevicemotion/1616140-magneticfield)Added [CMCalibratedMagneticField](https://developer.apple.com/documentation/coremotion/cmcalibratedmagneticfield)Added [CMMagneticFieldCalibrationAccuracy](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy)Added [CMMagneticFieldCalibrationAccuracyHigh](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/high)Added [CMMagneticFieldCalibrationAccuracyLow](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/cmmagneticfieldcalibrationaccuracylow)Added [CMMagneticFieldCalibrationAccuracyMedium](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/medium)Added [CMMagneticFieldCalibrationAccuracyUncalibrated](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/cmmagneticfieldcalibrationaccuracyuncalibrated)CMError.hAdded [CMErrorDeviceRequiresMovement](https://developer.apple.com/documentation/coremotion/cmerrordevicerequiresmovement)Added [CMErrorTrueNorthNotAvailable](https://developer.apple.com/documentation/coremotion/cmerrortruenorthnotavailable)CMMagnetometer.hAdded [CMMagnetometerData](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata)Added [CMMagnetometerData.magneticField](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata/1616084-magneticfield)Added [CMMagneticField](https://developer.apple.com/documentation/coremotion/cmmagneticfield)CMMotionManager.hAdded [CMMotionManager.attitudeReferenceFrame](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616112-attitudereferenceframe)Added [+[CMMotionManager availableAttitudeReferenceFrames]](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615955-availableattitudereferenceframes)Added [CMMotionManager.magnetometerActive](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615977-magnetometeractive)Added [CMMotionManager.magnetometerAvailable](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616143-magnetometeravailable)Added [CMMotionManager.magnetometerData](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616032-magnetometerdata)Added [CMMotionManager.magnetometerUpdateInterval](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616089-magnetometerupdateinterval)Added [CMMotionManager.showsDeviceMovementDisplay](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616122-showsdevicemovementdisplay)Added [-[CMMotionManager startDeviceMotionUpdatesUsingReferenceFrame:]](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616107-startdevicemotionupdates)Added [-[CMMotionManager startDeviceMotionUpdatesUsingReferenceFrame:toQueue:withHandler:]](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616176-startdevicemotionupdates)Added [-[CMMotionManager startMagnetometerUpdates]](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615961-startmagnetometerupdates)Added [-[CMMotionManager startMagnetometerUpdatesToQueue:withHandler:]](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615968-startmagnetometerupdatestoqueue)Added [-[CMMotionManager stopMagnetometerUpdates]](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616174-stopmagnetometerupdates)Added [CMMagnetometerHandler](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler)

## CoreTelephony

No changes

## CoreText

SFNTLayoutTypes.hAdded ALMXGlyphEntryAdded ALMXHeaderAdded JustDirectionTableAdded JustPCActionAdded JustPCActionSubrecordAdded JustPCActionTypeAdded JustPCConditionalAddActionAdded JustPCDecompositionActionAdded JustPCDuctilityActionAdded JustPCGlyphRepeatAddActionAdded JustPCUnconditionalAddActionAdded JustPostcompTableAdded JustTableAdded JustWidthDeltaEntryAdded JustWidthDeltaGroupAdded JustificationFlagsAdded KernArrayOffsetAdded KernFormatSpecificHeaderAdded KernIndexArrayHeaderAdded KernKerningPairAdded KernKerningValueAdded KernOffsetTableAdded KernOffsetTablePtrAdded KernOrderedListEntryAdded KernOrderedListEntryPtrAdded KernOrderedListHeaderAdded KernSimpleArrayHeaderAdded KernStateEntryAdded KernStateHeaderAdded KernSubtableHeaderAdded KernSubtableHeaderPtrAdded KernSubtableInfoAdded KernTableFormatAdded KernTableHeaderAdded KernTableHeaderHandleAdded KernTableHeaderPtrAdded KernVersion0HeaderAdded KernVersion0SubtableHeaderAdded KerxArrayOffsetAdded KerxControlPointActionAdded KerxControlPointEntryAdded KerxControlPointHeaderAdded KerxCoordinateActionAdded KerxFormatSpecificHeaderAdded KerxIndexArrayHeaderAdded KerxKerningPairAdded KerxOffsetTableAdded KerxOffsetTablePtrAdded KerxOrderedListEntryAdded KerxOrderedListEntryPtrAdded KerxOrderedListHeaderAdded KerxSimpleArrayHeaderAdded KerxStateEntryAdded KerxStateHeaderAdded KerxSubtableCoverageAdded KerxSubtableHeaderAdded KerxSubtableHeaderPtrAdded KerxTableHeaderAdded KerxTableHeaderHandleAdded KerxTableHeaderPtrAdded LcarCaretClassEntryAdded LcarCaretTableAdded LcarCaretTablePtrAdded MortChainAdded MortContextualSubtableAdded MortFeatureEntryAdded MortInsertionSubtableAdded MortLigatureActionEntryAdded MortLigatureSubtableAdded MortRearrangementSubtableAdded MortSpecificSubtableAdded MortSubtableAdded MortSubtableMaskFlagsAdded MortSwashSubtableAdded MortTableAdded MorxChainAdded MorxContextualSubtableAdded MorxInsertionSubtableAdded MorxLigatureSubtableAdded MorxRearrangementSubtableAdded MorxSpecificSubtableAdded MorxSubtableAdded MorxTableAdded PropCharPropertiesAdded PropLookupSegmentAdded PropLookupSingleAdded PropTableAdded ROTAGlyphEntryAdded ROTAHeaderAdded SFNTLookupArrayHeaderAdded SFNTLookupBinarySearchHeaderAdded SFNTLookupFormatSpecificHeaderAdded SFNTLookupKindAdded SFNTLookupOffsetAdded SFNTLookupSegmentAdded SFNTLookupSegmentHeaderAdded SFNTLookupSingleAdded SFNTLookupSingleHeaderAdded SFNTLookupTableAdded SFNTLookupTableFormatAdded SFNTLookupTableHandleAdded SFNTLookupTablePtrAdded SFNTLookupTrimmedArrayHeaderAdded SFNTLookupValueAdded STClassAdded STClassTableAdded STEntryIndexAdded STEntryOneAdded STEntryTwoAdded STEntryZeroAdded STHeaderAdded STXClassAdded STXClassTableAdded STXEntryIndexAdded STXEntryOneAdded STXEntryTwoAdded STXEntryZeroAdded STXHeaderAdded STXStateIndexAdded kAbbrevSquaredLigaturesOffSelectorAdded kAbbrevSquaredLigaturesOnSelectorAdded kAllCapsSelectorAdded kAllLowerCaseSelectorAdded kAllTypeFeaturesOffSelectorAdded kAllTypeFeaturesOnSelectorAdded kAllTypographicFeaturesTypeAdded kAnnotationTypeAdded kAsteriskToMultiplyOffSelectorAdded kAsteriskToMultiplyOnSelectorAdded kBoxAnnotationSelectorAdded kCJKItalicRomanOffSelectorAdded kCJKItalicRomanOnSelectorAdded kCJKItalicRomanSelectorAdded kCJKRomanSpacingTypeAdded kCJKSymbolAltFiveSelectorAdded kCJKSymbolAltFourSelectorAdded kCJKSymbolAltOneSelectorAdded kCJKSymbolAltThreeSelectorAdded kCJKSymbolAltTwoSelectorAdded kCJKSymbolAlternativesTypeAdded kCJKVerticalRomanCenteredSelectorAdded kCJKVerticalRomanHBaselineSelectorAdded kCJKVerticalRomanPlacementTypeAdded kCanonicalCompositionOffSelectorAdded kCanonicalCompositionOnSelectorAdded kCharacterAlternativesTypeAdded kCharacterShapeTypeAdded kCircleAnnotationSelectorAdded kCommonLigaturesOffSelectorAdded kCommonLigaturesOnSelectorAdded kCompatibilityCompositionOffSelectorAdded kCompatibilityCompositionOnSelectorAdded kCursiveConnectionTypeAdded kCursiveSelectorAdded kDecomposeDiacriticsSelectorAdded kDecorativeBordersSelectorAdded kDefaultCJKRomanSelectorAdded kDesignComplexityTypeAdded kDesignLevel1SelectorAdded kDesignLevel2SelectorAdded kDesignLevel3SelectorAdded kDesignLevel4SelectorAdded kDesignLevel5SelectorAdded kDiacriticsTypeAdded kDiagonalFractionsSelectorAdded kDiamondAnnotationSelectorAdded kDingbatsSelectorAdded kDiphthongLigaturesOffSelectorAdded kDiphthongLigaturesOnSelectorAdded kDisplayTextSelectorAdded kEngravedTextSelectorAdded kExpertCharactersSelectorAdded kExponentsOffSelectorAdded kExponentsOnSelectorAdded kFleuronsSelectorAdded kFormInterrobangOffSelectorAdded kFormInterrobangOnSelectorAdded kFractionsTypeAdded kFullWidthCJKRomanSelectorAdded kFullWidthIdeographsSelectorAdded kFullWidthKanaSelectorAdded kHalfWidthCJKRomanSelectorAdded kHalfWidthIdeographsSelectorAdded kHalfWidthTextSelectorAdded kHanjaToHangulAltOneSelectorAdded kHanjaToHangulAltThreeSelectorAdded kHanjaToHangulAltTwoSelectorAdded kHanjaToHangulSelectorAdded kHideDiacriticsSelectorAdded kHiraganaToKatakanaSelectorAdded kHyphenToEnDashOffSelectorAdded kHyphenToEnDashOnSelectorAdded kHyphenToMinusOffSelectorAdded kHyphenToMinusOnSelectorAdded kHyphensToEmDashOffSelectorAdded kHyphensToEmDashOnSelectorAdded kIdeographicAltFiveSelectorAdded kIdeographicAltFourSelectorAdded kIdeographicAltOneSelectorAdded kIdeographicAltThreeSelectorAdded kIdeographicAltTwoSelectorAdded kIdeographicAlternativesTypeAdded kIdeographicSpacingTypeAdded kIlluminatedCapsSelectorAdded kInequalityLigaturesOffSelectorAdded kInequalityLigaturesOnSelectorAdded kInferiorsSelectorAdded kInitialCapsAndSmallCapsSelectorAdded kInitialCapsSelectorAdded kInternationalSymbolsSelectorAdded kInvertedBoxAnnotationSelectorAdded kInvertedCircleAnnotationSelectorAdded kInvertedRoundedBoxAnnotationSelectorAdded kItalicCJKRomanTypeAdded kJIS1978CharactersSelectorAdded kJIS1983CharactersSelectorAdded kJIS1990CharactersSelectorAdded kJUSTCurrentVersionAdded kJUSTKashidaPriorityAdded kJUSTLetterPriorityAdded kJUSTNullPriorityAdded kJUSTOverrideLimitsAdded kJUSTOverridePriorityAdded kJUSTOverrideUnlimitedAdded kJUSTPriorityCountAdded kJUSTPriorityMaskAdded kJUSTSpacePriorityAdded kJUSTStandardFormatAdded kJUSTTagAdded kJUSTUnlimitedAdded kJUSTnoGlyphcodeAdded kJUSTpcConditionalAddActionAdded kJUSTpcDecompositionActionAdded kJUSTpcDuctilityActionAdded kJUSTpcGlyphRepeatAddActionAdded kJUSTpcGlyphStretchActionAdded kJUSTpcUnconditionalAddActionAdded kKERNCrossStreamAdded kKERNCrossStreamResetNoteAdded kKERNCurrentVersionAdded kKERNFormatMaskAdded kKERNIndexArrayAdded kKERNLineEndKerningAdded kKERNLineStartAdded kKERNNoCrossKerningAdded kKERNNoStakeNoteAdded kKERNNotAppliedAdded kKERNNotesRequestedAdded kKERNOrderedListAdded kKERNResetCrossStreamAdded kKERNSimpleArrayAdded kKERNStateTableAdded kKERNTagAdded kKERNUnusedBitsAdded kKERNVariationAdded kKERNVerticalAdded kKERXActionOffsetMaskAdded kKERXControlPointAdded kKERXCrossStreamAdded kKERXCrossStreamResetNoteAdded kKERXCurrentVersionAdded kKERXFormatMaskAdded kKERXIndexArrayAdded kKERXLineEndKerningAdded kKERXLineStartAdded kKERXNoCrossKerningAdded kKERXNoStakeNoteAdded kKERXNotAppliedAdded kKERXNotesRequestedAdded kKERXOrderedListAdded kKERXResetCrossStreamAdded kKERXSimpleArrayAdded kKERXStateTableAdded kKERXTagAdded kKERXUnusedBitsAdded kKERXUsesCoordinatesAdded kKERXVariationAdded kKERXVerticalAdded kKanaSpacingTypeAdded kKanaToRomanizationSelectorAdded kKatakanaToHiraganaSelectorAdded kLCARCtlPointFormatAdded kLCARCurrentVersionAdded kLCARLinearFormatAdded kLCARTagAdded kLastFeatureTypeAdded kLetterCaseTypeAdded kLigaturesTypeAdded kLineFinalSwashesOffSelectorAdded kLineFinalSwashesOnSelectorAdded kLineInitialSwashesOffSelectorAdded kLineInitialSwashesOnSelectorAdded kLinguisticRearrangementOffSelectorAdded kLinguisticRearrangementOnSelectorAdded kLinguisticRearrangementTypeAdded kLogosOffSelectorAdded kLogosOnSelectorAdded kLowerCaseNumbersSelectorAdded kMORTContextualTypeAdded kMORTCoverDescendingAdded kMORTCoverIgnoreVerticalAdded kMORTCoverTypeMaskAdded kMORTCoverVerticalAdded kMORTCurrInsertBeforeAdded kMORTCurrInsertCountMaskAdded kMORTCurrInsertCountShiftAdded kMORTCurrInsertKashidaLikeAdded kMORTCurrJustTableCountMaskAdded kMORTCurrJustTableCountShiftAdded kMORTCurrentVersionAdded kMORTDoInsertionsBeforeAdded kMORTInsertionTypeAdded kMORTInsertionsCountMaskAdded kMORTIsSplitVowelPieceAdded kMORTLigFormOffsetMaskAdded kMORTLigFormOffsetShiftAdded kMORTLigLastActionAdded kMORTLigStoreLigatureAdded kMORTLigatureTypeAdded kMORTMarkInsertBeforeAdded kMORTMarkInsertCountMaskAdded kMORTMarkInsertCountShiftAdded kMORTMarkInsertKashidaLikeAdded kMORTMarkJustTableCountMaskAdded kMORTMarkJustTableCountShiftAdded kMORTRearrangementTypeAdded kMORTSwashTypeAdded kMORTTagAdded kMORTraCDxAdded kMORTraCDxAAdded kMORTraCDxABAdded kMORTraCDxBAAdded kMORTraDCxAdded kMORTraDCxAAdded kMORTraDCxABAdded kMORTraDCxBAAdded kMORTraDxAdded kMORTraDxAAdded kMORTraDxABAdded kMORTraDxBAAdded kMORTraNoActionAdded kMORTraxAAdded kMORTraxABAdded kMORTraxBAAdded kMORXCoverDescendingAdded kMORXCoverIgnoreVerticalAdded kMORXCoverTypeMaskAdded kMORXCoverVerticalAdded kMORXCurrentVersionAdded kMORXTagAdded kMathSymbolsSelectorAdded kMathematicalExtrasTypeAdded kMonospacedNumbersSelectorAdded kMonospacedTextSelectorAdded kNoAlternatesSelectorAdded kNoAnnotationSelectorAdded kNoCJKItalicRomanSelectorAdded kNoCJKSymbolAlternativesSelectorAdded kNoFractionsSelectorAdded kNoIdeographicAlternativesSelectorAdded kNoOrnamentsSelectorAdded kNoRubyKanaSelectorAdded kNoStyleOptionsSelectorAdded kNoTransliterationSelectorAdded kNonFinalSwashesOffSelectorAdded kNonFinalSwashesOnSelectorAdded kNormalPositionSelectorAdded kNumberCaseTypeAdded kNumberSpacingTypeAdded kOrdinalsSelectorAdded kOrnamentSetsTypeAdded kOverlappingCharactersTypeAdded kPROPALDirectionClassAdded kPROPANDirectionClassAdded kPROPBNDirectionClassAdded kPROPCSDirectionClassAdded kPROPCanHangLTMaskAdded kPROPCanHangRBMaskAdded kPROPCurrentVersionAdded kPROPDirectionMaskAdded kPROPENDirectionClassAdded kPROPESDirectionClassAdded kPROPETDirectionClassAdded kPROPIsFloaterMaskAdded kPROPLDirectionClassAdded kPROPLREDirectionClassAdded kPROPLRODirectionClassAdded kPROPNSMDirectionClassAdded kPROPNumDirectionClassesAdded kPROPONDirectionClassAdded kPROPPDFDirectionClassAdded kPROPPSDirectionClassAdded kPROPPairOffsetMaskAdded kPROPPairOffsetShiftAdded kPROPPairOffsetSignAdded kPROPRDirectionClassAdded kPROPRLEDirectionClassAdded kPROPRLODirectionClassAdded kPROPRightConnectMaskAdded kPROPSDirectionClassAdded kPROPSENDirectionClassAdded kPROPTagAdded kPROPUseRLPairMaskAdded kPROPWSDirectionClassAdded kPROPZeroReservedAdded kParenthesisAnnotationSelectorAdded kPartiallyConnectedSelectorAdded kPeriodAnnotationSelectorAdded kPeriodsToEllipsisOffSelectorAdded kPeriodsToEllipsisOnSelectorAdded kPiCharactersSelectorAdded kPreventOverlapOffSelectorAdded kPreventOverlapOnSelectorAdded kProportionalCJKRomanSelectorAdded kProportionalIdeographsSelectorAdded kProportionalKanaSelectorAdded kProportionalNumbersSelectorAdded kProportionalTextSelectorAdded kQuarterWidthNumbersSelectorAdded kRareLigaturesOffSelectorAdded kRareLigaturesOnSelectorAdded kRebusPicturesOffSelectorAdded kRebusPicturesOnSelectorAdded kRequiredLigaturesOffSelectorAdded kRequiredLigaturesOnSelectorAdded kRomanNumeralAnnotationSelectorAdded kRomanizationToHiraganaSelectorAdded kRomanizationToKatakanaSelectorAdded kRoundedBoxAnnotationSelectorAdded kRubyKanaOffSelectorAdded kRubyKanaOnSelectorAdded kRubyKanaSelectorAdded kRubyKanaTypeAdded kSFNTLookupSegmentArrayAdded kSFNTLookupSegmentSingleAdded kSFNTLookupSimpleArrayAdded kSFNTLookupSingleTableAdded kSFNTLookupTrimmedArrayAdded kSTClassDeletedGlyphAdded kSTClassEndOfLineAdded kSTClassEndOfTextAdded kSTClassOutOfBoundsAdded kSTLigActionMaskAdded kSTMarkEndAdded kSTNoAdvanceAdded kSTRearrVerbMaskAdded kSTSetMarkAdded kSTXHasLigActionAdded kShowDiacriticsSelectorAdded kSimplifiedCharactersSelectorAdded kSlashToDivideOffSelectorAdded kSlashToDivideOnSelectorAdded kSlashedZeroOffSelectorAdded kSlashedZeroOnSelectorAdded kSmallCapsSelectorAdded kSmartQuotesOffSelectorAdded kSmartQuotesOnSelectorAdded kSmartSwashTypeAdded kSquaredLigaturesOffSelectorAdded kSquaredLigaturesOnSelectorAdded kStyleOptionsTypeAdded kSubstituteVerticalFormsOffSelectorAdded kSubstituteVerticalFormsOnSelectorAdded kSuperiorsSelectorAdded kSymbolLigaturesOffSelectorAdded kSymbolLigaturesOnSelectorAdded kTallCapsSelectorAdded kTextSpacingTypeAdded kThirdWidthNumbersSelectorAdded kTitlingCapsSelectorAdded kTraditionalAltFiveSelectorAdded kTraditionalAltFourSelectorAdded kTraditionalAltOneSelectorAdded kTraditionalAltThreeSelectorAdded kTraditionalAltTwoSelectorAdded kTraditionalCharactersSelectorAdded kTranscodingCompositionOffSelectorAdded kTranscodingCompositionOnSelectorAdded kTransliterationTypeAdded kTypographicExtrasTypeAdded kUnconnectedSelectorAdded kUnicodeDecompositionTypeAdded kUpperAndLowerCaseSelectorAdded kUpperCaseNumbersSelectorAdded kVerticalFractionsSelectorAdded kVerticalPositionTypeAdded kVerticalSubstitutionTypeAdded kWordFinalSwashesOffSelectorAdded kWordFinalSwashesOnSelectorAdded kWordInitialSwashesOffSelectorAdded kWordInitialSwashesOnSelectorSFNTTypes.hAdded FontLanguageCodeAdded FontNameCodeAdded FontPlatformCodeAdded FontScriptCodeAdded cmapFontTableTagAdded featureFontTableTagAdded kFontAlbanianLanguageAdded kFontAmharicLanguageAdded kFontAmharicScriptAdded kFontArabicLanguageAdded kFontArabicScriptAdded kFontArmenianLanguageAdded kFontArmenianScriptAdded kFontAssameseLanguageAdded kFontAymaraLanguageAdded kFontAzerbaijanArLanguageAdded kFontAzerbaijaniLanguageAdded kFontBasqueLanguageAdded kFontBengaliLanguageAdded kFontBengaliScriptAdded kFontBulgarianLanguageAdded kFontBurmeseLanguageAdded kFontBurmeseScriptAdded kFontByelorussianLanguageAdded kFontCatalanLanguageAdded kFontChewaLanguageAdded kFontChineseScriptAdded kFontCopyrightNameAdded kFontCroatianLanguageAdded kFontCustom16BitScriptAdded kFontCustom816BitScriptAdded kFontCustom8BitScriptAdded kFontCustomPlatformAdded kFontCyrillicScriptAdded kFontCzechLanguageAdded kFontDanishLanguageAdded kFontDescriptionNameAdded kFontDesignerNameAdded kFontDesignerURLNameAdded kFontDevanagariScriptAdded kFontDutchLanguageAdded kFontDzongkhaLanguageAdded kFontEastEuropeanRomanScriptAdded kFontEnglishLanguageAdded kFontEsperantoLanguageAdded kFontEstonianLanguageAdded kFontEthiopicScriptAdded kFontExtendedArabicScriptAdded kFontFaeroeseLanguageAdded kFontFamilyNameAdded kFontFarsiLanguageAdded kFontFinnishLanguageAdded kFontFlemishLanguageAdded kFontFrenchLanguageAdded kFontFullNameAdded kFontGallaLanguageAdded kFontGeezScriptAdded kFontGeorgianLanguageAdded kFontGeorgianScriptAdded kFontGermanLanguageAdded kFontGreekLanguageAdded kFontGreekScriptAdded kFontGuaraniLanguageAdded kFontGujaratiLanguageAdded kFontGujaratiScriptAdded kFontGurmukhiScriptAdded kFontHebrewLanguageAdded kFontHebrewScriptAdded kFontHindiLanguageAdded kFontHungarianLanguageAdded kFontISO10646_1993SemanticsAdded kFontIcelandicLanguageAdded kFontIndonesianLanguageAdded kFontIrishLanguageAdded kFontItalianLanguageAdded kFontJapaneseLanguageAdded kFontJapaneseScriptAdded kFontJavaneseRomLanguageAdded kFontKannadaLanguageAdded kFontKannadaScriptAdded kFontKashmiriLanguageAdded kFontKazakhLanguageAdded kFontKhmerLanguageAdded kFontKhmerScriptAdded kFontKirghizLanguageAdded kFontKoreanLanguageAdded kFontKoreanScriptAdded kFontKurdishLanguageAdded kFontLaoLanguageAdded kFontLaotianScriptAdded kFontLappishLanguageAdded kFontLastReservedNameAdded kFontLatinLanguageAdded kFontLatvianLanguageAdded kFontLettishLanguageAdded kFontLicenseDescriptionNameAdded kFontLicenseInfoURLNameAdded kFontLithuanianLanguageAdded kFontMacCompatibleFullNameAdded kFontMacedonianLanguageAdded kFontMacintoshPlatformAdded kFontMalagasyLanguageAdded kFontMalayArabicLanguageAdded kFontMalayRomanLanguageAdded kFontMalayalamLanguageAdded kFontMalayalamScriptAdded kFontMalteseLanguageAdded kFontManufacturerNameAdded kFontMarathiLanguageAdded kFontMicrosoftPlatformAdded kFontMicrosoftStandardScriptAdded kFontMicrosoftSymbolScriptAdded kFontMicrosoftUCS4ScriptAdded kFontMoldavianLanguageAdded kFontMongolianCyrLanguageAdded kFontMongolianLanguageAdded kFontMongolianScriptAdded kFontNepaliLanguageAdded kFontNoLanguageCodeAdded kFontNoNameCodeAdded kFontNoPlatformCodeAdded kFontNoScriptCodeAdded kFontNorwegianLanguageAdded kFontOriyaLanguageAdded kFontOriyaScriptAdded kFontOromoLanguageAdded kFontPashtoLanguageAdded kFontPersianLanguageAdded kFontPolishLanguageAdded kFontPortugueseLanguageAdded kFontPostScriptCIDNameAdded kFontPostscriptNameAdded kFontPreferredFamilyNameAdded kFontPreferredSubfamilyNameAdded kFontPunjabiLanguageAdded kFontQuechuaLanguageAdded kFontRSymbolScriptAdded kFontReservedPlatformAdded kFontRomanScriptAdded kFontRomanianLanguageAdded kFontRuandaLanguageAdded kFontRundiLanguageAdded kFontRussianAdded kFontRussianLanguageAdded kFontSaamiskLanguageAdded kFontSampleTextNameAdded kFontSanskritLanguageAdded kFontSerbianLanguageAdded kFontSimpChineseLanguageAdded kFontSimpleChineseScriptAdded kFontSindhiLanguageAdded kFontSindhiScriptAdded kFontSinhaleseLanguageAdded kFontSinhaleseScriptAdded kFontSlavicScriptAdded kFontSlovakLanguageAdded kFontSlovenianLanguageAdded kFontSomaliLanguageAdded kFontSpanishLanguageAdded kFontStyleNameAdded kFontSundaneseRomLanguageAdded kFontSwahiliLanguageAdded kFontSwedishLanguageAdded kFontTagalogLanguageAdded kFontTajikiLanguageAdded kFontTamilLanguageAdded kFontTamilScriptAdded kFontTatarLanguageAdded kFontTeluguLanguageAdded kFontTeluguScriptAdded kFontThaiLanguageAdded kFontThaiScriptAdded kFontTibetanLanguageAdded kFontTibetanScriptAdded kFontTigrinyaLanguageAdded kFontTradChineseLanguageAdded kFontTrademarkNameAdded kFontTraditionalChineseScriptAdded kFontTurkishLanguageAdded kFontTurkmenLanguageAdded kFontUighurLanguageAdded kFontUkrainianLanguageAdded kFontUnicodeDefaultSemanticsAdded kFontUnicodePlatformAdded kFontUnicodeV1_1SemanticsAdded kFontUnicodeV2_0BMPOnlySemanticsAdded kFontUnicodeV2_0FullCoverageSemanticsAdded kFontUnicodeV4_0VariationSequenceSemanticsAdded kFontUninterpretedScriptAdded kFontUniqueNameAdded kFontUrduLanguageAdded kFontUzbekLanguageAdded kFontVendorURLNameAdded kFontVersionNameAdded kFontVietnameseLanguageAdded kFontVietnameseScriptAdded kFontWelshLanguageAdded kFontYiddishLanguageAdded nameFontTableTagAdded sfntCMapEncodingAdded sfntCMapExtendedSubHeaderAdded sfntCMapHeaderAdded sfntCMapSubHeaderAdded sfntDirectoryAdded sfntDirectoryEntryAdded sfntFeatureHeaderAdded sfntFeatureNameAdded sfntFontFeatureSettingAdded sfntFontRunFeatureAdded sfntInstanceAdded sfntNameHeaderAdded sfntNameRecordAdded sfntVariationAxisAdded sfntVariationHeaderAdded sizeof_sfntCMapEncodingAdded sizeof_sfntCMapExtendedSubHeaderAdded sizeof_sfntCMapHeaderAdded sizeof_sfntCMapSubHeaderAdded sizeof_sfntDirectoryAdded sizeof_sfntInstanceAdded sizeof_sfntNameHeaderAdded sizeof_sfntNameRecordAdded sizeof_sfntVariationAxisAdded sizeof_sfntVariationHeaderAdded variationFontTableTag

## CoreVideo

CVBase.hAdded #def COREVIDEO_SUPPORTS_OPENGLESCVOpenGLESTexture.hAdded [CVOpenGLESTextureGetCleanTexCoords()](https://developer.apple.com/documentation/corevideo/1621287-cvopenglestexturegetcleantexcoor)Added [CVOpenGLESTextureGetName()](https://developer.apple.com/documentation/corevideo/1621290-cvopenglestexturegetname)Added [CVOpenGLESTextureGetTarget()](https://developer.apple.com/documentation/corevideo/1621289-cvopenglestexturegettarget)Added [CVOpenGLESTextureGetTypeID()](https://developer.apple.com/documentation/corevideo/1621291-cvopenglestexturegettypeid)Added [CVOpenGLESTextureIsFlipped()](https://developer.apple.com/documentation/corevideo/1621288-cvopenglestextureisflipped)Added [CVOpenGLESTextureRef](https://developer.apple.com/documentation/corevideo/cvopenglestextureref)CVOpenGLESTextureCache.hAdded [CVOpenGLESTextureCacheCreate()](https://developer.apple.com/documentation/corevideo/1619858-cvopenglestexturecachecreate)Added [CVOpenGLESTextureCacheCreateTextureFromImage()](https://developer.apple.com/documentation/corevideo/1619860-cvopenglestexturecachecreatetext)Added [CVOpenGLESTextureCacheFlush()](https://developer.apple.com/documentation/corevideo/1619857-cvopenglestexturecacheflush)Added [CVOpenGLESTextureCacheGetTypeID()](https://developer.apple.com/documentation/corevideo/1619861-cvopenglestexturecachegettypeid)Added [CVOpenGLESTextureCacheRef](https://developer.apple.com/documentation/corevideo/cvopenglestexturecacheref)Added [kCVOpenGLESTextureCacheMaximumTextureAgeKey](https://developer.apple.com/documentation/corevideo/kcvopenglestexturecachemaximumtextureagekey)CVPixelFormatDescription.hAdded [kCVPixelFormatOpenGLESCompatibility](https://developer.apple.com/documentation/corevideo/kcvpixelformatopenglescompatibility)

## EventKit

EKAlarm.hModified [EKAlarm](https://developer.apple.com/documentation/eventkit/ekalarm)

|  | Superclass |
| --- | --- |
| From | NSObject |
| To | EKObject |

EKCalendar.hAdded [EKCalendar.calendarIdentifier](https://developer.apple.com/documentation/eventkit/ekcalendar/1507380-calendaridentifier)Added [+[EKCalendar calendarWithEventStore:]](https://developer.apple.com/documentation/eventkit/ekcalendar/1620447-calendarwitheventstore)Added [EKCalendar.immutable](https://developer.apple.com/documentation/eventkit/ekcalendar/1507084-immutable)Added [EKCalendar.source](https://developer.apple.com/documentation/eventkit/ekcalendar/1507288-source)Added [EKCalendar.subscribed](https://developer.apple.com/documentation/eventkit/ekcalendar/1507471-subscribed)Modified [EKCalendar.title](https://developer.apple.com/documentation/eventkit/ekcalendar/1507487-title)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSString \*title |
| To | @property(nonatomic, copy) NSString \*title |

Modified [EKCalendar.CGColor](https://developer.apple.com/documentation/eventkit/ekcalendar/1615894-cgcolor)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) CGColorRef CGColor |
| To | @property(nonatomic) CGColorRef CGColor |

Modified [EKCalendar](https://developer.apple.com/documentation/eventkit/ekcalendar)

|  | Superclass |
| --- | --- |
| From | NSObject |
| To | EKObject |

EKCalendarItem.hAdded [EKCalendarItem](https://developer.apple.com/documentation/eventkit/ekcalendaritem)Added [EKCalendarItem.URL](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507265-url)Added [EKCalendarItem.UUID](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1623897-uuid)Added [-[EKCalendarItem addAlarm:]](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507397-addalarm)Added [-[EKCalendarItem addRecurrenceRule:]](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507256-addrecurrencerule)Added [EKCalendarItem.alarms](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507211-alarms)Added [EKCalendarItem.attendees](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507140-attendees)Added [EKCalendarItem.calendar](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507169-calendar)Added [EKCalendarItem.creationDate](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507213-creationdate)Added [EKCalendarItem.hasAlarms](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507271-hasalarms)Added [EKCalendarItem.hasAttendees](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507073-hasattendees)Added [EKCalendarItem.hasNotes](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507389-hasnotes)Added [EKCalendarItem.hasRecurrenceRules](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507459-hasrecurrencerules)Added [EKCalendarItem.lastModifiedDate](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507374-lastmodifieddate)Added [EKCalendarItem.location](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507269-location)Added [EKCalendarItem.notes](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507507-notes)Added [EKCalendarItem.recurrenceRules](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507135-recurrencerules)Added [-[EKCalendarItem removeAlarm:]](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507133-removealarm)Added [-[EKCalendarItem removeRecurrenceRule:]](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507495-removerecurrencerule)Added [EKCalendarItem.timeZone](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507104-timezone)Added [EKCalendarItem.title](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507305-title)EKError.hAdded [EKErrorCalendarHasNoSource](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorcalendarhasnosource)Added [EKErrorCalendarIsImmutable](https://developer.apple.com/documentation/eventkit/ekerror/code/calendarisimmutable)Added [EKErrorCalendarSourceCannotBeModified](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorcalendarsourcecannotbemodified)Added [EKErrorSourceDoesNotAllowCalendarAddDelete](https://developer.apple.com/documentation/eventkit/ekerror/code/sourcedoesnotallowcalendaradddelete)EKEvent.hRemoved -[EKEvent addAlarm:]Removed EKEvent.alarmsRemoved EKEvent.attendeesRemoved EKEvent.calendarRemoved EKEvent.lastModifiedDateRemoved EKEvent.locationRemoved EKEvent.notesRemoved -[EKEvent removeAlarm:]Removed EKEvent.titleAdded [EKEvent.birthdayPersonID](https://developer.apple.com/documentation/eventkit/ekevent/1615845-birthdaypersonid)Modified [EKEvent](https://developer.apple.com/documentation/eventkit/ekevent)

|  | Superclass |
| --- | --- |
| From | NSObject |
| To | EKCalendarItem |

Modified [EKEvent.recurrenceRule](https://developer.apple.com/documentation/eventkit/ekevent/1804716-recurrencerule)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

EKEventStore.hAdded [-[EKEventStore calendarWithIdentifier:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507484-calendarwithidentifier)Added [-[EKEventStore commit:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507424-commit)Added [-[EKEventStore refreshSourcesIfNecessary]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507421-refreshsourcesifnecessary)Added [-[EKEventStore removeCalendar:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507523-removecalendar)Added [-[EKEventStore removeEvent:span:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507469-removeevent)Added [-[EKEventStore reset]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507345-reset)Added [-[EKEventStore saveCalendar:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507080-savecalendar)Added [-[EKEventStore saveEvent:span:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507295-save)Added [-[EKEventStore sourceWithIdentifier:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507521-source)Added [-[EKEventStore sources]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507315-sources)EKObject.hAdded [EKObject](https://developer.apple.com/documentation/eventkit/ekobject)Added [-[EKObject hasChanges]](https://developer.apple.com/documentation/eventkit/ekobject/1507333-haschanges)Added [-[EKObject isNew]](https://developer.apple.com/documentation/eventkit/ekobject/1812546-isnew)Added [-[EKObject refresh]](https://developer.apple.com/documentation/eventkit/ekobject/1507327-refresh)Added [-[EKObject reset]](https://developer.apple.com/documentation/eventkit/ekobject/1507405-reset)Added [-[EKObject rollback]](https://developer.apple.com/documentation/eventkit/ekobject/1507462-rollback)EKParticipant.hModified [EKParticipant](https://developer.apple.com/documentation/eventkit/ekparticipant)

|  | Superclass |
| --- | --- |
| From | NSObject |
| To | EKObject |

EKRecurrenceDayOfWeek.hAdded [-[EKRecurrenceDayOfWeek initWithDayOfTheWeek:weekNumber:]](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448581-init)Modified [+[EKRecurrenceDayOfWeek dayOfWeek:]](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448589-dayofweek)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKRecurrenceDayOfWeek.h |

Modified [EKRecurrenceDayOfWeek.weekNumber](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448577-weeknumber)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKRecurrenceDayOfWeek.h |

Modified [EKRecurrenceDayOfWeek.dayOfTheWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448579-dayoftheweek)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKRecurrenceDayOfWeek.h |

Modified [+[EKRecurrenceDayOfWeek dayOfWeek:weekNumber:]](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448591-init)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKRecurrenceDayOfWeek.h |

Modified [EKRecurrenceDayOfWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKRecurrenceDayOfWeek.h |

EKRecurrenceEnd.hModified [EKRecurrenceEnd.endDate](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415648-enddate)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKRecurrenceEnd.h |

Modified [+[EKRecurrenceEnd recurrenceEndWithOccurrenceCount:]](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415640-init)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKRecurrenceEnd.h |

Modified [EKRecurrenceEnd.occurrenceCount](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415642-occurrencecount)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKRecurrenceEnd.h |

Modified [+[EKRecurrenceEnd recurrenceEndWithEndDate:]](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415644-init)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKRecurrenceEnd.h |

Modified [EKRecurrenceEnd](https://developer.apple.com/documentation/eventkit/ekrecurrenceend)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKRecurrenceEnd.h |

EKRecurrenceRule.hModified [-[EKRecurrenceRule initRecurrenceWithFrequency:interval:end:]](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507273-initrecurrencewithfrequency)

|  | Declaration |
| --- | --- |
| From | - (id)initRecurrenceWithFrequency:(EKRecurrenceFrequency)type interval:(NSUInteger)interval end:(EKRecurrenceEnd \*)end |
| To | - (id)initRecurrenceWithFrequency:(EKRecurrenceFrequency)type interval:(NSInteger)interval end:(EKRecurrenceEnd \*)end |

Modified [EKRecurrenceRule](https://developer.apple.com/documentation/eventkit/ekrecurrencerule)

|  | Superclass | Protocols |
| --- | --- | --- |
| From | NSObject | _none_ |
| To | EKObject | NSCopying |

EKSource.hAdded [EKSource](https://developer.apple.com/documentation/eventkit/eksource)Added [EKSource.calendars](https://developer.apple.com/documentation/eventkit/eksource/1624237-calendars)Added [EKSource.sourceIdentifier](https://developer.apple.com/documentation/eventkit/eksource/1507275-sourceidentifier)Added [EKSource.sourceType](https://developer.apple.com/documentation/eventkit/eksource/1507300-sourcetype)Added [EKSource.title](https://developer.apple.com/documentation/eventkit/eksource/1507385-title)EKTypes.hAdded [EKSourceType](https://developer.apple.com/documentation/eventkit/eksourcetype)Added [EKSourceTypeBirthdays](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypebirthdays)Added [EKSourceTypeCalDAV](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypecaldav)Added [EKSourceTypeExchange](https://developer.apple.com/documentation/eventkit/eksourcetype/exchange)Added [EKSourceTypeLocal](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypelocal)Added [EKSourceTypeMobileMe](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypemobileme)Added [EKSourceTypeSubscribed](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypesubscribed)Modified [EKParticipantRoleNonParticipant](https://developer.apple.com/documentation/eventkit/ekparticipantrole/ekparticipantrolenonparticipant)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKRecurrenceFrequencyYearly](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/yearly)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKParticipantRole](https://developer.apple.com/documentation/eventkit/ekparticipantrole)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKCalendarTypeLocal](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypelocal)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKRecurrenceFrequencyWeekly](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/weekly)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKParticipantRoleOptional](https://developer.apple.com/documentation/eventkit/ekparticipantrole/optional)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKCalendarEventAvailabilityNone](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/ekcalendareventavailabilitynone)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKSaturday](https://developer.apple.com/documentation/eventkit/ekweekday/eksaturday)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKCalendarEventAvailabilityTentative](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/ekcalendareventavailabilitytentative)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKParticipantStatusTentative](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/tentative)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKParticipantRoleRequired](https://developer.apple.com/documentation/eventkit/ekparticipantrole/ekparticipantrolerequired)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKMonday](https://developer.apple.com/documentation/eventkit/ekweekday/ekmonday)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKParticipantRoleUnknown](https://developer.apple.com/documentation/eventkit/ekparticipantrole/ekparticipantroleunknown)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKTuesday](https://developer.apple.com/documentation/eventkit/ekweekday/1451993-ektuesday)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKCalendarTypeSubscription](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypesubscription)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKWednesday](https://developer.apple.com/documentation/eventkit/ekweekday/1451817-ekwednesday)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKCalendarEventAvailabilityBusy](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/1451880-busy)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKParticipantStatus](https://developer.apple.com/documentation/eventkit/ekparticipantstatus)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKParticipantType](https://developer.apple.com/documentation/eventkit/ekparticipanttype)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKRecurrenceFrequencyMonthly](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/monthly)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKParticipantTypeRoom](https://developer.apple.com/documentation/eventkit/ekparticipanttype/room)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKParticipantStatusInProcess](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/inprocess)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKParticipantStatusUnknown](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/unknown)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKCalendarType](https://developer.apple.com/documentation/eventkit/ekcalendartype)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKParticipantStatusPending](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/pending)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKParticipantTypePerson](https://developer.apple.com/documentation/eventkit/ekparticipanttype/person)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKSunday](https://developer.apple.com/documentation/eventkit/ekweekday/eksunday)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKFriday](https://developer.apple.com/documentation/eventkit/ekweekday/1451835-ekfriday)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKCalendarTypeBirthday](https://developer.apple.com/documentation/eventkit/ekcalendartype/birthday)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKCalendarEventAvailabilityMask](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKThursday](https://developer.apple.com/documentation/eventkit/ekweekday/1451894-ekthursday)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKParticipantStatusDeclined](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/declined)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKCalendarTypeExchange](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypeexchange)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKCalendarEventAvailabilityUnavailable](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/ekcalendareventavailabilityunavailable)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKCalendarTypeCalDAV](https://developer.apple.com/documentation/eventkit/ekcalendartype/caldav)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKParticipantRoleChair](https://developer.apple.com/documentation/eventkit/ekparticipantrole/ekparticipantrolechair)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKParticipantTypeResource](https://developer.apple.com/documentation/eventkit/ekparticipanttype/resource)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKCalendarEventAvailabilityFree](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/ekcalendareventavailabilityfree)

|  | Header |
| --- | --- |
| From | EKCalendar.h |
| To | EKTypes.h |

Modified [EKRecurrenceFrequency](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKRecurrenceFrequencyDaily](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/daily)

|  | Header |
| --- | --- |
| From | EKRecurrenceRule.h |
| To | EKTypes.h |

Modified [EKParticipantStatusDelegated](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/delegated)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKParticipantTypeGroup](https://developer.apple.com/documentation/eventkit/ekparticipanttype/ekparticipanttypegroup)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKParticipantStatusAccepted](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/accepted)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKParticipantTypeUnknown](https://developer.apple.com/documentation/eventkit/ekparticipanttype/unknown)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

Modified [EKParticipantStatusCompleted](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/ekparticipantstatuscompleted)

|  | Header |
| --- | --- |
| From | EKParticipant.h |
| To | EKTypes.h |

EventKitDefines.hAdded #def EVENTKIT_CLASS_AVAILABLEAdded #def EVENTKIT_EXTERN

## EventKitUI

EKCalendarChooser.hAdded [EKCalendarChooser](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser)Added [EKCalendarChooser.delegate](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613949-delegate)Added [-[EKCalendarChooser initWithSelectionStyle:displayStyle:eventStore:]](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613974-initwithselectionstyle)Added [EKCalendarChooser.selectedCalendars](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613926-selectedcalendars)Added [EKCalendarChooser.selectionStyle](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613923-selectionstyle)Added [EKCalendarChooser.showsCancelButton](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613935-showscancelbutton)Added [EKCalendarChooser.showsDoneButton](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613958-showsdonebutton)Added [EKCalendarChooserDelegate](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate)Added [-[EKCalendarChooserDelegate calendarChooserDidCancel:]](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate/1613941-calendarchooserdidcancel)Added [-[EKCalendarChooserDelegate calendarChooserDidFinish:]](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate/1613979-calendarchooserdidfinish)Added [-[EKCalendarChooserDelegate calendarChooserSelectionDidChange:]](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate/1613924-calendarchooserselectiondidchang)Added [EKCalendarChooserDisplayAllCalendars](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdisplaystyle/allcalendars)Added [EKCalendarChooserDisplayStyle](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdisplaystyle)Added [EKCalendarChooserDisplayWritableCalendarsOnly](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdisplaystyle/ekcalendarchooserdisplaywritablecalendarsonly)Added [EKCalendarChooserSelectionStyle](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserselectionstyle)Added [EKCalendarChooserSelectionStyleMultiple](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserselectionstyle/ekcalendarchooserselectionstylemultiple)Added [EKCalendarChooserSelectionStyleSingle](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserselectionstyle/single)EventKitUIDefines.hAdded #def EVENTKITUI_CLASS_AVAILABLEAdded #def EVENTKITUI_EXTERN

## ExternalAccessory

No changes

## Foundation

FoundationErrors.hAdded [NSFileWriteFileExistsError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsfilewritefileexistserror)NSArray.hModified [-[NSArray getObjects:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/getObjects:range:)

|  | Declaration |
| --- | --- |
| From | - (void)getObjects:(id \*)objects range:(NSRange)range |
| To | - (void)getObjects:(id[])objects range:(NSRange)range |

Modified [-[NSArray getObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/getObjects:)

|  | Declaration |
| --- | --- |
| From | - (void)getObjects:(id \*)objects |
| To | - (void)getObjects:(id[])objects |

Modified [+[NSArray arrayWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithObjects:(const id \*)objects count:(NSUInteger)cnt |
| To | + (id)arrayWithObjects:(const id[])objects count:(NSUInteger)cnt |

Modified [-[NSArray initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id \*)objects count:(NSUInteger)cnt |
| To | - (id)initWithObjects:(const id[])objects count:(NSUInteger)cnt |

NSCache.hModified [-[NSCache setDelegate:]](https://developer.apple.com/documentation/foundation/nscache/1413061-delegate)

|  | Declaration |
| --- | --- |
| From | - (void)setDelegate:(id)d |
| To | - (void)setDelegate:(id < NSCacheDelegate >)d |

Modified [NSCacheDelegate](https://developer.apple.com/documentation/foundation/nscachedelegate)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSObject |

Modified [-[NSCache delegate]](https://developer.apple.com/documentation/foundation/nscache/1413061-delegate)

|  | Declaration |
| --- | --- |
| From | - (id)delegate |
| To | - (id < NSCacheDelegate >)delegate |

NSCalendar.hAdded [-[NSDateComponents setWeekOfMonth:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1413168-weekofmonth)Added [-[NSDateComponents setWeekOfYear:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416908-weekofyear)Added [-[NSDateComponents setYearForWeekOfYear:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1413809-yearforweekofyear)Added [-[NSDateComponents weekOfMonth]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1413168-weekofmonth)Added [-[NSDateComponents weekOfYear]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416908-weekofyear)Added [-[NSDateComponents yearForWeekOfYear]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1413809-yearforweekofyear)Added [NSWeekOfMonthCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsweekofmonthcalendarunit)Added [NSWeekOfYearCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsweekofyearcalendarunit)Added [NSYearForWeekOfYearCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1408285-nsyearforweekofyearcalendarunit)NSCoder.hAdded -[NSCoder NS_AUTOMATED_REFCOUNT_UNAVAILABLE] (no architecture available)NSComparisonPredicate.hAdded [NSComparisonPredicateOptions](https://developer.apple.com/documentation/foundation/nscomparisonpredicateoptions)Added [NSNormalizedPredicateOption](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options/1409785-normalized)Modified [-[NSComparisonPredicate options]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1414069-options)

|  | Declaration |
| --- | --- |
| From | - (NSUInteger)options |
| To | - (NSComparisonPredicateOptions)options |

Modified [+[NSComparisonPredicate predicateWithLeftExpression:rightExpression:modifier:type:options:]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1568140-predicatewithleftexpression)

|  | Declaration |
| --- | --- |
| From | + (NSPredicate \*)predicateWithLeftExpression:(NSExpression \*)lhs rightExpression:(NSExpression \*)rhs modifier:(NSComparisonPredicateModifier)modifier type:(NSPredicateOperatorType)type options:(NSUInteger)options |
| To | + (NSPredicate \*)predicateWithLeftExpression:(NSExpression \*)lhs rightExpression:(NSExpression \*)rhs modifier:(NSComparisonPredicateModifier)modifier type:(NSPredicateOperatorType)type options:(NSComparisonPredicateOptions)options |

Modified [-[NSComparisonPredicate initWithLeftExpression:rightExpression:modifier:type:options:]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1413523-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithLeftExpression:(NSExpression \*)lhs rightExpression:(NSExpression \*)rhs modifier:(NSComparisonPredicateModifier)modifier type:(NSPredicateOperatorType)type options:(NSUInteger)options |
| To | - (id)initWithLeftExpression:(NSExpression \*)lhs rightExpression:(NSExpression \*)rhs modifier:(NSComparisonPredicateModifier)modifier type:(NSPredicateOperatorType)type options:(NSComparisonPredicateOptions)options |

NSData.hAdded [NSDataReadingMappedAlways](https://developer.apple.com/documentation/foundation/nsdata/readingoptions/1418417-alwaysmapped)Added [NSDataReadingMappedIfSafe](https://developer.apple.com/documentation/foundation/nsdata/readingoptions/1413157-mappedifsafe)Added [NSDataWritingFileProtectionCompleteUnlessOpen](https://developer.apple.com/documentation/foundation/nsdatawritingoptions/nsdatawritingfileprotectioncompleteunlessopen)Added [NSDataWritingFileProtectionCompleteUntilFirstUserAuthentication](https://developer.apple.com/documentation/foundation/nsdata/writingoptions/1617028-completefileprotectionuntilfirst)Modified [-[NSData initWithContentsOfMappedFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/initWithContentsOfMappedFile:)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [+[NSData dataWithContentsOfMappedFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/dataWithContentsOfMappedFile:)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

NSDictionary.hModified [+[NSDictionary dictionaryWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObjects:(id \*)objects forKeys:(id \*)keys count:(NSUInteger)cnt |
| To | + (id)dictionaryWithObjects:(const id[])objects forKeys:(const id[])keys count:(NSUInteger)cnt |

Modified [-[NSDictionary getObjects:andKeys:]](https://developer.apple.com/documentation/foundation/nsdictionary/1409428-getobjects)

|  | Declaration |
| --- | --- |
| From | - (void)getObjects:(id \*)objects andKeys:(id \*)keys |
| To | - (void)getObjects:(id[])objects andKeys:(id[])keys |

Modified [-[NSDictionary initWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(id \*)objects forKeys:(id \*)keys count:(NSUInteger)cnt |
| To | - (id)initWithObjects:(const id[])objects forKeys:(const id[])keys count:(NSUInteger)cnt |

NSEnumerator.hModified [-[NSFastEnumeration countByEnumeratingWithState:objects:count:]](https://developer.apple.com/documentation/foundation/nsfastenumeration/1412867-countbyenumerating)

|  | Declaration |
| --- | --- |
| From | - (NSUInteger)countByEnumeratingWithState:(NSFastEnumerationState \*)state objects:(id \*)stackbuf count:(NSUInteger)len |
| To | - (NSUInteger)countByEnumeratingWithState:(NSFastEnumerationState \*)state objects:(id[])buffer count:(NSUInteger)len |

NSExpression.hAdded [+[NSExpression expressionWithFormat:]](https://developer.apple.com/documentation/foundation/nsexpression/1587937-expressionwithformat)Added [+[NSExpression expressionWithFormat:argumentArray:]](https://developer.apple.com/documentation/foundation/nsexpression/1413484-expressionwithformat)Added [+[NSExpression expressionWithFormat:arguments:]](https://developer.apple.com/documentation/foundation/nsexpression/1410346-expressionwithformat)NSFileCoordinator.hAdded [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator)Added [+[NSFileCoordinator addFilePresenter:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1417120-addfilepresenter)Added [-[NSFileCoordinator cancel]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1418457-cancel)Added [-[NSFileCoordinator coordinateReadingItemAtURL:options:error:byAccessor:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1407416-coordinate)Added [-[NSFileCoordinator coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1413385-coordinatereadingitematurl)Added [-[NSFileCoordinator coordinateWritingItemAtURL:options:error:byAccessor:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1413344-coordinate)Added [-[NSFileCoordinator coordinateWritingItemAtURL:options:writingItemAtURL:options:error:byAccessor:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1408970-coordinate)Added [+[NSFileCoordinator filePresenters]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1407685-filepresenters)Added [-[NSFileCoordinator initWithFilePresenter:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1416795-init)Added [-[NSFileCoordinator itemAtURL:didMoveToURL:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1410328-item)Added [-[NSFileCoordinator prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1412420-prepareforreadingitemsaturls)Added [+[NSFileCoordinator removeFilePresenter:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1414924-removefilepresenter)Added [NSFileCoordinatorReadingOptions](https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions)Added [NSFileCoordinatorReadingResolvesSymbolicLink](https://developer.apple.com/documentation/foundation/nsfilecoordinatorreadingoptions/nsfilecoordinatorreadingresolvessymboliclink)Added [NSFileCoordinatorReadingWithoutChanges](https://developer.apple.com/documentation/foundation/nsfilecoordinatorreadingoptions/nsfilecoordinatorreadingwithoutchanges)Added [NSFileCoordinatorWritingForDeleting](https://developer.apple.com/documentation/foundation/nsfilecoordinatorwritingoptions/nsfilecoordinatorwritingfordeleting)Added [NSFileCoordinatorWritingForMerging](https://developer.apple.com/documentation/foundation/nsfilecoordinatorwritingoptions/nsfilecoordinatorwritingformerging)Added [NSFileCoordinatorWritingForMoving](https://developer.apple.com/documentation/foundation/nsfilecoordinatorwritingoptions/nsfilecoordinatorwritingformoving)Added [NSFileCoordinatorWritingForReplacing](https://developer.apple.com/documentation/foundation/nsfilecoordinatorwritingoptions/nsfilecoordinatorwritingforreplacing)Added [NSFileCoordinatorWritingOptions](https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions)NSFileHandle.hAdded [NSFileHandle.readabilityHandler](https://developer.apple.com/documentation/foundation/filehandle/1412413-readabilityhandler)Added [NSFileHandle.writeabilityHandler](https://developer.apple.com/documentation/foundation/nsfilehandle/1415367-writeabilityhandler)Modified [NSFileHandleNotificationMonitorModes](https://developer.apple.com/documentation/foundation/nsfilehandlenotificationmonitormodes)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

NSFileManager.hRemoved -[NSObject fileManager:shouldCopyItemAtPath:toPath:]Removed -[NSObject fileManager:shouldCopyItemAtURL:toURL:]Removed -[NSObject fileManager:shouldLinkItemAtPath:toPath:]Removed -[NSObject fileManager:shouldLinkItemAtURL:toURL:]Removed -[NSObject fileManager:shouldMoveItemAtPath:toPath:]Removed -[NSObject fileManager:shouldMoveItemAtURL:toURL:]Removed -[NSObject fileManager:shouldProceedAfterError:copyingItemAtPath:toPath:]Removed -[NSObject fileManager:shouldProceedAfterError:copyingItemAtURL:toURL:]Removed -[NSObject fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:]Removed -[NSObject fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:]Removed -[NSObject fileManager:shouldProceedAfterError:movingItemAtPath:toPath:]Removed -[NSObject fileManager:shouldProceedAfterError:movingItemAtURL:toURL:]Removed -[NSObject fileManager:shouldProceedAfterError:removingItemAtPath:]Removed -[NSObject fileManager:shouldProceedAfterError:removingItemAtURL:]Removed -[NSObject fileManager:shouldRemoveItemAtPath:]Removed -[NSObject fileManager:shouldRemoveItemAtURL:]Removed NSObject(NSFileManagerFileOperationAdditions)Added [-[NSFileManager URLForPublishingUbiquitousItemAtURL:expirationDate:error:]](https://developer.apple.com/documentation/foundation/filemanager/1411577-url)Added [-[NSFileManager URLForUbiquityContainerIdentifier:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie)Added [-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1415371-createdirectoryaturl)Added [-[NSFileManager createSymbolicLinkAtURL:withDestinationURL:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1414652-createsymboliclinkaturl)Added [-[NSFileManager evictUbiquitousItemAtURL:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1409696-evictubiquitousitematurl)Added [-[NSFileManager isUbiquitousItemAtURL:]](https://developer.apple.com/documentation/foundation/filemanager/1410218-isubiquitousitem)Added [-[NSFileManager setUbiquitous:itemAtURL:destinationURL:error:]](https://developer.apple.com/documentation/foundation/filemanager/1413989-setubiquitous)Added [-[NSFileManager startDownloadingUbiquitousItemAtURL:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1410377-startdownloadingubiquitousitemat)Added [NSFileManagerDelegate](https://developer.apple.com/documentation/foundation/filemanagerdelegate)Added [-[NSFileManagerDelegate fileManager:shouldCopyItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1414922-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldCopyItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1417936-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldLinkItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1414699-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldLinkItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1417589-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldMoveItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1407734-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldMoveItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1411878-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:copyingItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1410189-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:copyingItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1410788-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1415627-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1408003-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:movingItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1412865-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:movingItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1411289-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:removingItemAtPath:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1409791-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:removingItemAtURL:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1408660-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldRemoveItemAtPath:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1412994-filemanager)Added [-[NSFileManagerDelegate fileManager:shouldRemoveItemAtURL:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1411918-filemanager)Added [NSFileProtectionCompleteUnlessOpen](https://developer.apple.com/documentation/foundation/nsfileprotectioncompleteunlessopen)Added [NSFileProtectionCompleteUntilFirstUserAuthentication](https://developer.apple.com/documentation/foundation/fileprotectiontype/1616633-completeuntilfirstuserauthentica)NSFilePresenter.hAdded [NSFilePresenter](https://developer.apple.com/documentation/foundation/nsfilepresenter)Added [-[NSFilePresenter accommodatePresentedItemDeletionWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1414732-accommodatepresenteditemdeletion)Added [-[NSFilePresenter accommodatePresentedSubitemDeletionAtURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415657-accommodatepresentedsubitemdelet)Added [-[NSFilePresenter presentedItemDidChange]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1416103-presenteditemdidchange)Added [-[NSFilePresenter presentedItemDidGainVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415018-presenteditemdidgainversion)Added [-[NSFilePresenter presentedItemDidLoseVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1417258-presenteditemdidlose)Added [-[NSFilePresenter presentedItemDidMoveToURL:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1417861-presenteditemdidmove)Added [-[NSFilePresenter presentedItemDidResolveConflictVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1418445-presenteditemdidresolveconflictv)Added [NSFilePresenter.presentedItemOperationQueue](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415250-presenteditemoperationqueue)Added [NSFilePresenter.presentedItemURL](https://developer.apple.com/documentation/foundation/nsfilepresenter/1414861-presenteditemurl)Added [-[NSFilePresenter presentedSubitemAtURL:didGainVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415472-presentedsubitematurl)Added [-[NSFilePresenter presentedSubitemAtURL:didLoseVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1413957-presentedsubitem)Added [-[NSFilePresenter presentedSubitemAtURL:didMoveToURL:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1409465-presentedsubitematurl)Added [-[NSFilePresenter presentedSubitemAtURL:didResolveConflictVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1416913-presentedsubitematurl)Added [-[NSFilePresenter presentedSubitemDidAppearAtURL:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1408642-presentedsubitemdidappear)Added [-[NSFilePresenter presentedSubitemDidChangeAtURL:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1411135-presentedsubitemdidchangeaturl)Added [-[NSFilePresenter relinquishPresentedItemToReader:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1410743-relinquishpresenteditemtoreader)Added [-[NSFilePresenter relinquishPresentedItemToWriter:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1413688-relinquishpresenteditemtowriter)Added [-[NSFilePresenter savePresentedItemChangesWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1414407-savepresenteditemchangeswithcomp)NSFileVersion.hAdded [NSFileVersion](https://developer.apple.com/documentation/foundation/nsfileversion)Added [NSFileVersion.URL](https://developer.apple.com/documentation/foundation/nsfileversion/1418131-url)Added [NSFileVersion.conflict](https://developer.apple.com/documentation/foundation/nsfileversion/1409277-conflict)Added [+[NSFileVersion currentVersionOfItemAtURL:]](https://developer.apple.com/documentation/foundation/nsfileversion/1412963-currentversionofitematurl)Added [NSFileVersion.localizedName](https://developer.apple.com/documentation/foundation/nsfileversion/1413855-localizedname)Added [NSFileVersion.localizedNameOfSavingComputer](https://developer.apple.com/documentation/foundation/nsfileversion/1408866-localizednameofsavingcomputer)Added [NSFileVersion.modificationDate](https://developer.apple.com/documentation/foundation/nsfileversion/1411506-modificationdate)Added [+[NSFileVersion otherVersionsOfItemAtURL:]](https://developer.apple.com/documentation/foundation/nsfileversion/1418163-otherversionsofitematurl)Added [NSFileVersion.persistentIdentifier](https://developer.apple.com/documentation/foundation/nsfileversion/1407948-persistentidentifier)Added [-[NSFileVersion removeAndReturnError:]](https://developer.apple.com/documentation/foundation/nsfileversion/1407486-remove)Added [+[NSFileVersion removeOtherVersionsOfItemAtURL:error:]](https://developer.apple.com/documentation/foundation/nsfileversion/1411537-removeotherversionsofitematurl)Added [-[NSFileVersion replaceItemAtURL:options:error:]](https://developer.apple.com/documentation/foundation/nsfileversion/1412297-replaceitem)Added [NSFileVersion.resolved](https://developer.apple.com/documentation/foundation/nsfileversion/1414906-resolved)Added [+[NSFileVersion unresolvedConflictVersionsOfItemAtURL:]](https://developer.apple.com/documentation/foundation/nsfileversion/1417854-unresolvedconflictversionsofitem)Added [+[NSFileVersion versionOfItemAtURL:forPersistentIdentifier:]](https://developer.apple.com/documentation/foundation/nsfileversion/1415443-version)Added [NSFileVersionAddingByMoving](https://developer.apple.com/documentation/foundation/nsfileversionaddingoptions/nsfileversionaddingbymoving)Added [NSFileVersionAddingOptions](https://developer.apple.com/documentation/foundation/nsfileversion/addingoptions)Added [NSFileVersionReplacingByMoving](https://developer.apple.com/documentation/foundation/nsfileversionreplacingoptions/nsfileversionreplacingbymoving)Added [NSFileVersionReplacingOptions](https://developer.apple.com/documentation/foundation/nsfileversionreplacingoptions)NSFileWrapper.hModified [-[NSFileWrapper symbolicLinkDestination]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1418302-symboliclinkdestination)

|  | Architectures |
| --- | --- |
| From | arm |
| To | Unknown |

Modified [-[NSFileWrapper addFileWithPath:]](https://developer.apple.com/documentation/foundation/filewrapper/1417211-addfile)

|  | Architectures |
| --- | --- |
| From | arm |
| To | Unknown |

Modified [-[NSFileWrapper addSymbolicLinkWithDestination:preferredFilename:]](https://developer.apple.com/documentation/foundation/filewrapper/1414604-addsymboliclink)

|  | Architectures |
| --- | --- |
| From | arm |
| To | Unknown |

Modified [-[NSFileWrapper writeToFile:atomically:updateFilenames:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415079-writetofile)

|  | Architectures |
| --- | --- |
| From | arm |
| To | Unknown |

Modified NSFileWrapper(NSDeprecated)

|  | Architectures |
| --- | --- |
| From | arm |
| To | Unknown |

Modified [-[NSFileWrapper needsToBeUpdatedFromPath:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1407738-needstobeupdatedfrompath)

|  | Architectures |
| --- | --- |
| From | arm |
| To | Unknown |

Modified [-[NSFileWrapper initWithPath:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1408388-initwithpath)

|  | Architectures |
| --- | --- |
| From | arm |
| To | Unknown |

Modified [-[NSFileWrapper initSymbolicLinkWithDestination:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1411268-initsymboliclinkwithdestination)

|  | Architectures |
| --- | --- |
| From | arm |
| To | Unknown |

Modified [-[NSFileWrapper updateFromPath:]](https://developer.apple.com/documentation/foundation/filewrapper/1416300-update)

|  | Architectures |
| --- | --- |
| From | arm |
| To | Unknown |

NSHTTPCookieStorage.hRemoved [-[NSHTTPCookieStorage initWithStorageLocation:]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1807248-initwithstoragelocation)Added [-[NSHTTPCookieStorage sortedCookiesUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1413730-sortedcookiesusingdescriptors)NSIndexSet.hAdded [-[NSIndexSet enumerateRangesInRange:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nsindexset/1416352-enumeraterangesinrange)Added [-[NSIndexSet enumerateRangesUsingBlock:]](https://developer.apple.com/documentation/foundation/nsindexset/1409668-enumeraterangesusingblock)Added [-[NSIndexSet enumerateRangesWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsindexset/1412673-enumeraterangeswithoptions)NSJSONSerialization.hAdded [NSJSONSerialization](https://developer.apple.com/documentation/foundation/nsjsonserialization)Added [+[NSJSONSerialization JSONObjectWithData:options:error:]](https://developer.apple.com/documentation/foundation/nsjsonserialization/1415493-jsonobjectwithdata)Added [+[NSJSONSerialization JSONObjectWithStream:options:error:]](https://developer.apple.com/documentation/foundation/nsjsonserialization/1418059-jsonobjectwithstream)Added [+[NSJSONSerialization dataWithJSONObject:options:error:]](https://developer.apple.com/documentation/foundation/nsjsonserialization/1413636-datawithjsonobject)Added [+[NSJSONSerialization isValidJSONObject:]](https://developer.apple.com/documentation/foundation/nsjsonserialization/1418461-isvalidjsonobject)Added [+[NSJSONSerialization writeJSONObject:toStream:options:error:]](https://developer.apple.com/documentation/foundation/nsjsonserialization/1417433-writejsonobject)Added [NSJSONReadingAllowFragments](https://developer.apple.com/documentation/foundation/jsonserialization/readingoptions/1416042-allowfragments)Added [NSJSONReadingMutableContainers](https://developer.apple.com/documentation/foundation/nsjsonreadingoptions/nsjsonreadingmutablecontainers)Added [NSJSONReadingMutableLeaves](https://developer.apple.com/documentation/foundation/jsonserialization/readingoptions/1414448-mutableleaves)Added [NSJSONReadingOptions](https://developer.apple.com/documentation/foundation/nsjsonreadingoptions)Added [NSJSONWritingOptions](https://developer.apple.com/documentation/foundation/nsjsonwritingoptions)Added [NSJSONWritingPrettyPrinted](https://developer.apple.com/documentation/foundation/nsjsonwritingoptions/nsjsonwritingprettyprinted)NSKeyValueCoding.hAdded [-[NSObject mutableOrderedSetValueForKey:]](https://developer.apple.com/documentation/objectivec/nsobject/1415479-mutableorderedsetvalue)Added [-[NSObject mutableOrderedSetValueForKeyPath:]](https://developer.apple.com/documentation/objectivec/nsobject/1407188-mutableorderedsetvalue)Added [-[NSOrderedSet setValue:forKey:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413118-setvalue)Added [-[NSOrderedSet valueForKey:]](https://developer.apple.com/documentation/foundation/nsorderedset/1409378-value)Added NSOrderedSet(NSKeyValueCoding)Modified [-[NSObject validateValue:forKey:error:]](https://developer.apple.com/documentation/objectivec/nsobject/1416754-validatevalue)

|  | Declaration |
| --- | --- |
| From | - (BOOL)validateValue:(id \*)ioValue forKey:(NSString \*)inKey error:(NSError \*\*)outError |
| To | - (BOOL)validateValue:(inout id \*)ioValue forKey:(NSString \*)inKey error:(out NSError \*\*)outError |

Modified [-[NSObject validateValue:forKeyPath:error:]](https://developer.apple.com/documentation/objectivec/nsobject/1416245-validatevalue)

|  | Declaration |
| --- | --- |
| From | - (BOOL)validateValue:(id \*)ioValue forKeyPath:(NSString \*)inKeyPath error:(NSError \*\*)outError |
| To | - (BOOL)validateValue:(inout id \*)ioValue forKeyPath:(NSString \*)inKeyPath error:(out NSError \*\*)outError |

NSKeyValueObserving.hAdded [-[NSArray removeObserver:forKeyPath:context:]](https://developer.apple.com/documentation/foundation/nsarray/1418441-removeobserver)Added [-[NSArray removeObserver:fromObjectsAtIndexes:forKeyPath:context:]](https://developer.apple.com/documentation/foundation/nsarray/1408305-removeobserver)Added [-[NSObject removeObserver:forKeyPath:context:]](https://developer.apple.com/documentation/objectivec/nsobject/1410691-removeobserver)Added [-[NSOrderedSet addObserver:forKeyPath:options:context:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408740-addobserver)Added [-[NSOrderedSet removeObserver:forKeyPath:]](https://developer.apple.com/documentation/foundation/nsorderedset/1412955-removeobserver)Added [-[NSOrderedSet removeObserver:forKeyPath:context:]](https://developer.apple.com/documentation/foundation/nsorderedset/1410496-removeobserver)Added [-[NSSet removeObserver:forKeyPath:context:]](https://developer.apple.com/documentation/foundation/nsset/1415413-removeobserver)Added NSOrderedSet(NSKeyValueObserverRegistration)NSLinguisticTagger.hAdded [NSLinguisticTagger](https://developer.apple.com/documentation/foundation/nslinguistictagger)Added [+[NSLinguisticTagger availableTagSchemesForLanguage:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1408694-availabletagschemesforlanguage)Added [-[NSLinguisticTagger enumerateTagsInRange:scheme:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1410036-enumeratetags)Added [-[NSLinguisticTagger initWithTagSchemes:options:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1414576-initwithtagschemes)Added [-[NSLinguisticTagger orthographyAtIndex:effectiveRange:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1415566-orthography)Added [-[NSLinguisticTagger possibleTagsAtIndex:scheme:tokenRange:sentenceRange:scores:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1408537-possibletags)Added [-[NSLinguisticTagger sentenceRangeForRange:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1415532-sentencerange)Added [-[NSLinguisticTagger setOrthography:range:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1409101-setorthography)Added [-[NSLinguisticTagger setString:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1407750-string)Added [-[NSLinguisticTagger string]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1407750-string)Added [-[NSLinguisticTagger stringEditedInRange:changeInLength:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1417623-stringedited)Added [-[NSLinguisticTagger tagAtIndex:scheme:tokenRange:sentenceRange:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1411834-tag)Added [-[NSLinguisticTagger tagSchemes]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1409018-tagschemes)Added [-[NSLinguisticTagger tagsInRange:scheme:options:tokenRanges:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1417826-tags)Added [-[NSString enumerateLinguisticTagsInRange:scheme:options:orthography:usingBlock:]](https://developer.apple.com/documentation/foundation/nsstring/1412161-enumeratelinguistictags)Added [-[NSString linguisticTagsInRange:scheme:options:orthography:tokenRanges:]](https://developer.apple.com/documentation/foundation/nsstring/1416530-linguistictagsinrange)Added [NSLinguisticTagAdjective](https://developer.apple.com/documentation/foundation/nslinguistictag/1416444-adjective)Added [NSLinguisticTagAdverb](https://developer.apple.com/documentation/foundation/nslinguistictagadverb)Added [NSLinguisticTagClassifier](https://developer.apple.com/documentation/foundation/nslinguistictag/1417959-classifier)Added [NSLinguisticTagCloseParenthesis](https://developer.apple.com/documentation/foundation/nslinguistictag/1418472-closeparenthesis)Added [NSLinguisticTagCloseQuote](https://developer.apple.com/documentation/foundation/nslinguistictagclosequote)Added [NSLinguisticTagConjunction](https://developer.apple.com/documentation/foundation/nslinguistictagconjunction)Added [NSLinguisticTagDash](https://developer.apple.com/documentation/foundation/nslinguistictag/1410097-dash)Added [NSLinguisticTagDeterminer](https://developer.apple.com/documentation/foundation/nslinguistictagdeterminer)Added [NSLinguisticTagIdiom](https://developer.apple.com/documentation/foundation/nslinguistictagidiom)Added [NSLinguisticTagInterjection](https://developer.apple.com/documentation/foundation/nslinguistictag/1415803-interjection)Added [NSLinguisticTagNoun](https://developer.apple.com/documentation/foundation/nslinguistictagnoun)Added [NSLinguisticTagNumber](https://developer.apple.com/documentation/foundation/nslinguistictagnumber)Added [NSLinguisticTagOpenParenthesis](https://developer.apple.com/documentation/foundation/nslinguistictag/1410101-openparenthesis)Added [NSLinguisticTagOpenQuote](https://developer.apple.com/documentation/foundation/nslinguistictag/1415620-openquote)Added [NSLinguisticTagOrganizationName](https://developer.apple.com/documentation/foundation/nslinguistictagorganizationname)Added [NSLinguisticTagOther](https://developer.apple.com/documentation/foundation/nslinguistictag/1412556-other)Added [NSLinguisticTagOtherPunctuation](https://developer.apple.com/documentation/foundation/nslinguistictagotherpunctuation)Added [NSLinguisticTagOtherWhitespace](https://developer.apple.com/documentation/foundation/nslinguistictag/1416562-otherwhitespace)Added [NSLinguisticTagOtherWord](https://developer.apple.com/documentation/foundation/nslinguistictag/1407498-otherword)Added [NSLinguisticTagParagraphBreak](https://developer.apple.com/documentation/foundation/nslinguistictagparagraphbreak)Added [NSLinguisticTagParticle](https://developer.apple.com/documentation/foundation/nslinguistictagparticle)Added [NSLinguisticTagPersonalName](https://developer.apple.com/documentation/foundation/nslinguistictag/1417476-personalname)Added [NSLinguisticTagPlaceName](https://developer.apple.com/documentation/foundation/nslinguistictagplacename)Added [NSLinguisticTagPreposition](https://developer.apple.com/documentation/foundation/nslinguistictagpreposition)Added [NSLinguisticTagPronoun](https://developer.apple.com/documentation/foundation/nslinguistictag/1408771-pronoun)Added [NSLinguisticTagPunctuation](https://developer.apple.com/documentation/foundation/nslinguistictag/1416694-punctuation)Added [NSLinguisticTagSchemeLanguage](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/1408597-language)Added [NSLinguisticTagSchemeLemma](https://developer.apple.com/documentation/foundation/nslinguistictagschemelemma)Added [NSLinguisticTagSchemeLexicalClass](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/1415311-lexicalclass)Added [NSLinguisticTagSchemeNameType](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/1415135-nametype)Added [NSLinguisticTagSchemeNameTypeOrLexicalClass](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/1409103-nametypeorlexicalclass)Added [NSLinguisticTagSchemeScript](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/1414794-script)Added [NSLinguisticTagSchemeTokenType](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/1411898-tokentype)Added [NSLinguisticTagSentenceTerminator](https://developer.apple.com/documentation/foundation/nslinguistictag/1412725-sentenceterminator)Added [NSLinguisticTagVerb](https://developer.apple.com/documentation/foundation/nslinguistictag/1409771-verb)Added [NSLinguisticTagWhitespace](https://developer.apple.com/documentation/foundation/nslinguistictag/1407724-whitespace)Added [NSLinguisticTagWord](https://developer.apple.com/documentation/foundation/nslinguistictag/1418153-word)Added [NSLinguisticTagWordJoiner](https://developer.apple.com/documentation/foundation/nslinguistictag/1411539-wordjoiner)Added [NSLinguisticTaggerJoinNames](https://developer.apple.com/documentation/foundation/nslinguistictaggeroptions/nslinguistictaggerjoinnames)Added [NSLinguisticTaggerOmitOther](https://developer.apple.com/documentation/foundation/nslinguistictagger/options/1411386-omitother)Added [NSLinguisticTaggerOmitPunctuation](https://developer.apple.com/documentation/foundation/nslinguistictaggeroptions/nslinguistictaggeromitpunctuation)Added [NSLinguisticTaggerOmitWhitespace](https://developer.apple.com/documentation/foundation/nslinguistictaggeroptions/nslinguistictaggeromitwhitespace)Added [NSLinguisticTaggerOmitWords](https://developer.apple.com/documentation/foundation/nslinguistictaggeroptions/nslinguistictaggeromitwords)Added [NSLinguisticTaggerOptions](https://developer.apple.com/documentation/foundation/nslinguistictaggeroptions)Added NSString(NSLinguisticAnalysis)NSMetadata.hAdded [NSMetadataItem](https://developer.apple.com/documentation/foundation/nsmetadataitem)Added [-[NSMetadataItem attributes]](https://developer.apple.com/documentation/foundation/nsmetadataitem/1418347-attributes)Added [-[NSMetadataItem valueForAttribute:]](https://developer.apple.com/documentation/foundation/nsmetadataitem/1411721-valueforattribute)Added [-[NSMetadataItem valuesForAttributes:]](https://developer.apple.com/documentation/foundation/nsmetadataitem/1409934-valuesforattributes)Added [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery)Added [-[NSMetadataQuery delegate]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1413181-delegate)Added [-[NSMetadataQuery disableUpdates]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416337-disableupdates)Added [-[NSMetadataQuery enableUpdates]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416943-enableupdates)Added [-[NSMetadataQuery groupedResults]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416579-groupedresults)Added [-[NSMetadataQuery groupingAttributes]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1409191-groupingattributes)Added [-[NSMetadataQuery indexOfResult:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1410014-indexofresult)Added -[NSMetadataQuery init]Added [-[NSMetadataQuery isGathering]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407539-isgathering)Added [-[NSMetadataQuery isStarted]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416780-isstarted)Added [-[NSMetadataQuery isStopped]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411941-stopped)Added [-[NSMetadataQuery notificationBatchingInterval]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411884-notificationbatchinginterval)Added [-[NSMetadataQuery predicate]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411478-predicate)Added [-[NSMetadataQuery resultAtIndex:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1410162-result)Added [-[NSMetadataQuery resultCount]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1418315-resultcount)Added [-[NSMetadataQuery results]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1408872-results)Added [-[NSMetadataQuery searchScopes]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1412155-searchscopes)Added [-[NSMetadataQuery setDelegate:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1413181-delegate)Added [-[NSMetadataQuery setGroupingAttributes:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1409191-groupingattributes)Added [-[NSMetadataQuery setNotificationBatchingInterval:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411884-notificationbatchinginterval)Added [-[NSMetadataQuery setPredicate:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411478-predicate)Added [-[NSMetadataQuery setSearchScopes:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1412155-searchscopes)Added [-[NSMetadataQuery setSortDescriptors:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411847-sortdescriptors)Added [-[NSMetadataQuery setValueListAttributes:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407767-valuelistattributes)Added [-[NSMetadataQuery sortDescriptors]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411847-sortdescriptors)Added [-[NSMetadataQuery startQuery]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407304-startquery)Added [-[NSMetadataQuery stopQuery]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1408021-stopquery)Added [-[NSMetadataQuery valueListAttributes]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407767-valuelistattributes)Added [-[NSMetadataQuery valueLists]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1418401-valuelists)Added [-[NSMetadataQuery valueOfAttribute:forResultAtIndex:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1417133-value)Added [NSMetadataQueryAttributeValueTuple](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple)Added [-[NSMetadataQueryAttributeValueTuple attribute]](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple/1415060-attribute)Added [-[NSMetadataQueryAttributeValueTuple count]](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple/1414426-count)Added [-[NSMetadataQueryAttributeValueTuple value]](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple/1417894-value)Added [NSMetadataQueryDelegate](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate)Added [-[NSMetadataQueryDelegate metadataQuery:replacementObjectForResultObject:]](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/1407317-metadataquery)Added [-[NSMetadataQueryDelegate metadataQuery:replacementValueForAttribute:value:]](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/1414215-metadataquery)Added [NSMetadataQueryResultGroup](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup)Added [-[NSMetadataQueryResultGroup attribute]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1411276-attribute)Added [-[NSMetadataQueryResultGroup resultAtIndex:]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1410397-result)Added [-[NSMetadataQueryResultGroup resultCount]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1414790-resultcount)Added [-[NSMetadataQueryResultGroup results]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1410191-results)Added [-[NSMetadataQueryResultGroup subgroups]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1409929-subgroups)Added [-[NSMetadataQueryResultGroup value]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1417674-value)Added [NSMetadataItemDisplayNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdisplaynamekey)Added [NSMetadataItemFSContentChangeDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfscontentchangedatekey)Added [NSMetadataItemFSCreationDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfscreationdatekey)Added [NSMetadataItemFSNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfsnamekey)Added [NSMetadataItemFSSizeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfssizekey)Added [NSMetadataItemIsUbiquitousKey](https://developer.apple.com/documentation/foundation/nsmetadataitemisubiquitouskey)Added [NSMetadataItemPathKey](https://developer.apple.com/documentation/foundation/nsmetadataitempathkey)Added [NSMetadataItemURLKey](https://developer.apple.com/documentation/foundation/nsmetadataitemurlkey)Added [NSMetadataQueryDidFinishGatheringNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1414740-nsmetadataquerydidfinishgatherin)Added [NSMetadataQueryDidStartGatheringNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1416717-nsmetadataquerydidstartgathering)Added [NSMetadataQueryDidUpdateNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1413406-nsmetadataquerydidupdate)Added [NSMetadataQueryGatheringProgressNotification](https://developer.apple.com/documentation/foundation/nsmetadataquerygatheringprogressnotification)Added [NSMetadataQueryResultContentRelevanceAttribute](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultcontentrelevanceattribute)Added [NSMetadataQueryUbiquitousDataScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryubiquitousdatascope)Added [NSMetadataQueryUbiquitousDocumentsScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryubiquitousdocumentsscope)Added [NSMetadataUbiquitousItemHasUnresolvedConflictsKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemhasunresolvedconflictskey)Added [NSMetadataUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadedkey)Added [NSMetadataUbiquitousItemIsDownloadingKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadingkey)Added [NSMetadataUbiquitousItemIsUploadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisuploadedkey)Added [NSMetadataUbiquitousItemIsUploadingKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisuploadingkey)Added [NSMetadataUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitempercentdownloadedkey)Added [NSMetadataUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitempercentuploadedkey)NSNotification.hModified [-[NSNotificationCenter addObserverForName:object:queue:usingBlock:]](https://developer.apple.com/documentation/foundation/nsnotificationcenter/1411723-addobserverforname)

|  | Declaration |
| --- | --- |
| From | - (id)addObserverForName:(NSString \*)name object:(id)obj queue:(NSOperationQueue \*)queue usingBlock:(void (^)(NSNotification \*))block |
| To | - (id)addObserverForName:(NSString \*)name object:(id)obj queue:(NSOperationQueue \*)queue usingBlock:(void (^)(NSNotification \*note))block |

NSObjCRuntime.hAdded #def NS_AUTOMATED_REFCOUNT_UNAVAILABLEAdded #def NS_AUTOMATED_REFCOUNT_WEAK_UNAVAILABLEAdded #def NS_AVAILABLE_IOSAdded #def NS_DEPRECATED_IOSAdded #def NS_NONATOMIC_IOSONLYAdded #def NS_RETURNS_NOT_RETAINEDAdded #def NS_UNAVAILABLENSObject.hAdded -[NSObject NS_AUTOMATED_REFCOUNT_UNAVAILABLE] (no architecture available)Added -[NSObject NS_UNAVAILABLE] (no architecture available)Added [-[NSObject debugDescription]](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418703-debugdescription)Added [CFBridgingRelease()](https://developer.apple.com/documentation/foundation/1587932-cfbridgingrelease)Added [CFBridgingRetain()](https://developer.apple.com/documentation/foundation/1416649-cfbridgingretain)NSOrderedSet.hAdded [NSMutableOrderedSet](https://developer.apple.com/documentation/foundation/nsmutableorderedset)Added [-[NSMutableOrderedSet addObject:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1408009-add)Added [-[NSMutableOrderedSet addObjects:count:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1413840-addobjects)Added [-[NSMutableOrderedSet addObjectsFromArray:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1417200-addobjects)Added [-[NSMutableOrderedSet exchangeObjectAtIndex:withObjectAtIndex:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1416821-exchangeobjectatindex)Added [-[NSMutableOrderedSet initWithCapacity:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411583-init)Added [-[NSMutableOrderedSet insertObject:atIndex:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1416634-insertobject)Added [-[NSMutableOrderedSet insertObjects:atIndexes:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410287-insert)Added [-[NSMutableOrderedSet intersectOrderedSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1408541-intersect)Added [-[NSMutableOrderedSet intersectSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1415257-intersectset)Added [-[NSMutableOrderedSet minusOrderedSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1407987-minusorderedset)Added [-[NSMutableOrderedSet minusSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411229-minusset)Added [-[NSMutableOrderedSet moveObjectsAtIndexes:toIndex:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1417677-moveobjectsatindexes)Added [+[NSMutableOrderedSet orderedSetWithCapacity:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1543283-orderedsetwithcapacity)Added [-[NSMutableOrderedSet removeAllObjects]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1414262-removeallobjects)Added [-[NSMutableOrderedSet removeObject:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1416776-remove)Added [-[NSMutableOrderedSet removeObjectAtIndex:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1415040-removeobject)Added [-[NSMutableOrderedSet removeObjectsAtIndexes:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1418161-removeobjectsatindexes)Added [-[NSMutableOrderedSet removeObjectsInArray:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411635-removeobjectsinarray)Added [-[NSMutableOrderedSet removeObjectsInRange:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1417539-removeobjects)Added [-[NSMutableOrderedSet replaceObjectAtIndex:withObject:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1412115-replaceobjectatindex)Added [-[NSMutableOrderedSet replaceObjectsAtIndexes:withObjects:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1416127-replaceobjectsatindexes)Added [-[NSMutableOrderedSet replaceObjectsInRange:withObjects:count:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1415340-replaceobjects)Added [-[NSMutableOrderedSet setObject:atIndex:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411158-setobject)Added [-[NSMutableOrderedSet sortRange:options:usingComparator:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1407529-sortrange)Added [-[NSMutableOrderedSet sortUsingComparator:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1414566-sortusingcomparator)Added [-[NSMutableOrderedSet sortWithOptions:usingComparator:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411561-sort)Added [-[NSMutableOrderedSet unionOrderedSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410973-unionorderedset)Added [-[NSMutableOrderedSet unionSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1413853-unionset)Added [NSOrderedSet](https://developer.apple.com/documentation/foundation/nsorderedset)Added [-[NSOrderedSet array]](https://developer.apple.com/documentation/foundation/nsorderedset/1411531-array)Added [-[NSOrderedSet containsObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408681-containsobject)Added [-[NSOrderedSet count]](https://developer.apple.com/documentation/foundation/nsorderedset/1410106-count)Added [-[NSOrderedSet description]](https://developer.apple.com/documentation/foundation/nsorderedset/1415872-description)Added [-[NSOrderedSet descriptionWithLocale:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417325-descriptionwithlocale)Added [-[NSOrderedSet descriptionWithLocale:indent:]](https://developer.apple.com/documentation/foundation/nsorderedset/1416761-descriptionwithlocale)Added [-[NSOrderedSet enumerateObjectsAtIndexes:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nsorderedset/1412332-enumerateobjectsatindexes)Added [-[NSOrderedSet enumerateObjectsUsingBlock:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413531-enumerateobjectsusingblock)Added [-[NSOrderedSet enumerateObjectsWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsorderedset/1409354-enumerateobjectswithoptions)Added [-[NSOrderedSet firstObject]](https://developer.apple.com/documentation/foundation/nsorderedset/1409765-firstobject)Added [-[NSOrderedSet getObjects:range:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411401-getobjects)Added [-[NSOrderedSet indexOfObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411856-indexofobject)Added [-[NSOrderedSet indexOfObject:inSortedRange:options:usingComparator:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417701-index)Added [-[NSOrderedSet indexOfObjectAtIndexes:options:passingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417531-index)Added [-[NSOrderedSet indexOfObjectPassingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413003-index)Added [-[NSOrderedSet indexOfObjectWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408700-indexofobjectwithoptions)Added [-[NSOrderedSet indexesOfObjectsAtIndexes:options:passingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413586-indexesofobjectsatindexes)Added [-[NSOrderedSet indexesOfObjectsPassingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411331-indexes)Added [-[NSOrderedSet indexesOfObjectsWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1415944-indexes)Added [-[NSOrderedSet initWithArray:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408623-init)Added [-[NSOrderedSet initWithArray:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1418006-initwitharray)Added [-[NSOrderedSet initWithArray:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1409272-initwitharray)Added [-[NSOrderedSet initWithObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413883-initwithobject)Added [-[NSOrderedSet initWithObjects:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543287-initwithobjects)Added [-[NSOrderedSet initWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411910-initwithobjects)Added [-[NSOrderedSet initWithOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1412402-init)Added [-[NSOrderedSet initWithOrderedSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411658-initwithorderedset)Added [-[NSOrderedSet initWithOrderedSet:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417751-init)Added [-[NSOrderedSet initWithSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1416344-initwithset)Added [-[NSOrderedSet initWithSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411246-init)Added [-[NSOrderedSet intersectsOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414364-intersectsorderedset)Added [-[NSOrderedSet intersectsSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408625-intersectsset)Added [-[NSOrderedSet isEqualToOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408049-isequal)Added [-[NSOrderedSet isSubsetOfOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411496-issubset)Added [-[NSOrderedSet isSubsetOfSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1418464-issubsetofset)Added [-[NSOrderedSet lastObject]](https://developer.apple.com/documentation/foundation/nsorderedset/1409143-lastobject)Added [-[NSOrderedSet objectAtIndex:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414734-objectatindex)Added [-[NSOrderedSet objectEnumerator]](https://developer.apple.com/documentation/foundation/nsorderedset/1409430-objectenumerator)Added [-[NSOrderedSet objectsAtIndexes:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414943-objects)Added [+[NSOrderedSet orderedSet]](https://developer.apple.com/documentation/foundation/nsorderedset/1543313-orderedset)Added [+[NSOrderedSet orderedSetWithArray:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543310-orderedsetwitharray)Added [+[NSOrderedSet orderedSetWithArray:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543321-orderedsetwitharray)Added [+[NSOrderedSet orderedSetWithObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543339-orderedsetwithobject)Added [+[NSOrderedSet orderedSetWithObjects:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543312-orderedsetwithobjects)Added [+[NSOrderedSet orderedSetWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543334-init)Added [+[NSOrderedSet orderedSetWithOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543280-orderedsetwithorderedset)Added [+[NSOrderedSet orderedSetWithOrderedSet:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543292-orderedsetwithorderedset)Added [+[NSOrderedSet orderedSetWithSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543298-orderedsetwithset)Added [+[NSOrderedSet orderedSetWithSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543331-orderedsetwithset)Added [-[NSOrderedSet reverseObjectEnumerator]](https://developer.apple.com/documentation/foundation/nsorderedset/1407607-reverseobjectenumerator)Added [-[NSOrderedSet reversedOrderedSet]](https://developer.apple.com/documentation/foundation/nsorderedset/1411022-reversedorderedset)Added [-[NSOrderedSet set]](https://developer.apple.com/documentation/foundation/nsorderedset/1413944-set)Added [-[NSOrderedSet sortedArrayUsingComparator:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413383-sortedarray)Added [-[NSOrderedSet sortedArrayWithOptions:usingComparator:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414806-sortedarray)Added NSMutableOrderedSet(NSExtendedMutableOrderedSet)Added NSMutableOrderedSet(NSMutableOrderedSetCreation)Added NSOrderedSet(NSExtendedOrderedSet)Added NSOrderedSet(NSOrderedSetCreation)NSPort.hRemoved [+[NSPort allocWithZone:]](https://developer.apple.com/documentation/foundation/nsport/1807189-allocwithzone)NSProcessInfo.hRemoved [-[NSProcessInfo disableSuddenTermination]](https://developer.apple.com/documentation/foundation/processinfo/1412841-disablesuddentermination) (no architecture available)Removed [-[NSProcessInfo enableSuddenTermination]](https://developer.apple.com/documentation/foundation/processinfo/1409836-enablesuddentermination) (no architecture available)NSPropertyList.hModified [+[NSPropertyListSerialization dataFromPropertyList:format:errorDescription:]](https://developer.apple.com/documentation/foundation/nspropertylistserialization/1416061-datafrompropertylist)

|  | Declaration |
| --- | --- |
| From | + (NSData \*)dataFromPropertyList:(id)plist format:(NSPropertyListFormat)format errorDescription:(NSString \*\*)errorString |
| To | + (NSData \*)dataFromPropertyList:(id)plist format:(NSPropertyListFormat)format errorDescription:(out NSString \*\*)errorString |

Modified [+[NSPropertyListSerialization propertyListWithData:options:format:error:]](https://developer.apple.com/documentation/foundation/propertylistserialization/1409678-propertylist)

|  | Declaration |
| --- | --- |
| From | + (id)propertyListWithData:(NSData \*)data options:(NSPropertyListReadOptions)opt format:(NSPropertyListFormat \*)format error:(NSError \*\*)error |
| To | + (id)propertyListWithData:(NSData \*)data options:(NSPropertyListReadOptions)opt format:(NSPropertyListFormat \*)format error:(out NSError \*\*)error |

Modified [+[NSPropertyListSerialization propertyListWithStream:options:format:error:]](https://developer.apple.com/documentation/foundation/propertylistserialization/1415468-propertylist)

|  | Declaration |
| --- | --- |
| From | + (id)propertyListWithStream:(NSInputStream \*)stream options:(NSPropertyListReadOptions)opt format:(NSPropertyListFormat \*)format error:(NSError \*\*)error |
| To | + (id)propertyListWithStream:(NSInputStream \*)stream options:(NSPropertyListReadOptions)opt format:(NSPropertyListFormat \*)format error:(out NSError \*\*)error |

Modified [+[NSPropertyListSerialization writePropertyList:toStream:format:options:error:]](https://developer.apple.com/documentation/foundation/propertylistserialization/1407862-writepropertylist)

|  | Declaration |
| --- | --- |
| From | + (NSInteger)writePropertyList:(id)plist toStream:(NSOutputStream \*)stream format:(NSPropertyListFormat)format options:(NSPropertyListWriteOptions)opt error:(NSError \*\*)error |
| To | + (NSInteger)writePropertyList:(id)plist toStream:(NSOutputStream \*)stream format:(NSPropertyListFormat)format options:(NSPropertyListWriteOptions)opt error:(out NSError \*\*)error |

Modified [+[NSPropertyListSerialization dataWithPropertyList:format:options:error:]](https://developer.apple.com/documentation/foundation/nspropertylistserialization/1418309-datawithpropertylist)

|  | Declaration |
| --- | --- |
| From | + (NSData \*)dataWithPropertyList:(id)plist format:(NSPropertyListFormat)format options:(NSPropertyListWriteOptions)opt error:(NSError \*\*)error |
| To | + (NSData \*)dataWithPropertyList:(id)plist format:(NSPropertyListFormat)format options:(NSPropertyListWriteOptions)opt error:(out NSError \*\*)error |

Modified [+[NSPropertyListSerialization propertyListFromData:mutabilityOption:format:errorDescription:]](https://developer.apple.com/documentation/foundation/propertylistserialization/1411993-propertylistfromdata)

|  | Declaration |
| --- | --- |
| From | + (id)propertyListFromData:(NSData \*)data mutabilityOption:(NSPropertyListMutabilityOptions)opt format:(NSPropertyListFormat \*)format errorDescription:(NSString \*\*)errorString |
| To | + (id)propertyListFromData:(NSData \*)data mutabilityOption:(NSPropertyListMutabilityOptions)opt format:(NSPropertyListFormat \*)format errorDescription:(out NSString \*\*)errorString |

NSProxy.hAdded -[NSProxy NS_UNAVAILABLE] (no architecture available)Added [-[NSProxy debugDescription]](https://developer.apple.com/documentation/foundation/nsproxy/1416366-debugdescription)NSSet.hModified [-[NSSet initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(id \*)objects count:(NSUInteger)cnt |
| To | - (id)initWithObjects:(const id \*)objects count:(NSUInteger)cnt |

Modified [+[NSSet setWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithObjects:(id \*)objects count:(NSUInteger)cnt |
| To | + (id)setWithObjects:(const id \*)objects count:(NSUInteger)cnt |

NSStream.hAdded [NSStreamNetworkServiceTypeBackground](https://developer.apple.com/documentation/foundation/nsstreamnetworkservicetypebackground)Added [NSStreamNetworkServiceTypeVideo](https://developer.apple.com/documentation/foundation/nsstreamnetworkservicetypevideo)Added [NSStreamNetworkServiceTypeVoice](https://developer.apple.com/documentation/foundation/streamnetworkservicetypevalue/1416419-voice)NSString.hAdded [#def NSMaximumStringLength](https://developer.apple.com/documentation/foundation/nsmaximumstringlength)Modified [NSProprietaryStringEncoding](https://developer.apple.com/documentation/foundation/1497268-anonymous/nsproprietarystringencoding)

|  | Architectures |
| --- | --- |
| From | Unknown |
| To | arm |

NSTextCheckingResult.hAdded [-[NSTextCheckingResult resultByAdjustingRangesWithOffset:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1417597-resultbyadjustingrangeswithoffse)NSURL.hAdded [NSFileSecurity](https://developer.apple.com/documentation/foundation/nsfilesecurity)Added [-[NSURL URLByAppendingPathComponent:isDirectory:]](https://developer.apple.com/documentation/foundation/nsurl/1413953-urlbyappendingpathcomponent)Added [NSURLFileResourceIdentifierKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1414512-fileresourceidentifierkey)Added [NSURLFileResourceTypeBlockSpecial](https://developer.apple.com/documentation/foundation/urlfileresourcetype/1417396-blockspecial)Added [NSURLFileResourceTypeCharacterSpecial](https://developer.apple.com/documentation/foundation/nsurlfileresourcetypecharacterspecial)Added [NSURLFileResourceTypeDirectory](https://developer.apple.com/documentation/foundation/nsurlfileresourcetypedirectory)Added [NSURLFileResourceTypeKey](https://developer.apple.com/documentation/foundation/nsurlfileresourcetypekey)Added [NSURLFileResourceTypeNamedPipe](https://developer.apple.com/documentation/foundation/urlfileresourcetype/1414127-namedpipe)Added [NSURLFileResourceTypeRegular](https://developer.apple.com/documentation/foundation/nsurlfileresourcetyperegular)Added [NSURLFileResourceTypeSocket](https://developer.apple.com/documentation/foundation/nsurlfileresourcetypesocket)Added [NSURLFileResourceTypeSymbolicLink](https://developer.apple.com/documentation/foundation/urlfileresourcetype/1415809-symboliclink)Added [NSURLFileResourceTypeUnknown](https://developer.apple.com/documentation/foundation/urlfileresourcetype/1410708-unknown)Added [NSURLFileSecurityKey](https://developer.apple.com/documentation/foundation/nsurlfilesecuritykey)Added [NSURLIsExecutableKey](https://developer.apple.com/documentation/foundation/nsurlisexecutablekey)Added [NSURLIsMountTriggerKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1416377-ismounttriggerkey)Added [NSURLIsReadableKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1409521-isreadablekey)Added [NSURLIsUbiquitousItemKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1416894-isubiquitousitemkey)Added [NSURLIsWritableKey](https://developer.apple.com/documentation/foundation/nsurliswritablekey)Added [NSURLKeysOfUnsetValuesKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1416230-keysofunsetvalueskey)Added [NSURLPreferredIOBlockSizeKey](https://developer.apple.com/documentation/foundation/nsurlpreferredioblocksizekey)Added [NSURLTotalFileAllocatedSizeKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1415519-totalfileallocatedsizekey)Added [NSURLTotalFileSizeKey](https://developer.apple.com/documentation/foundation/nsurltotalfilesizekey)Added [NSURLUbiquitousItemHasUnresolvedConflictsKey](https://developer.apple.com/documentation/foundation/nsurlubiquitousitemhasunresolvedconflictskey)Added [NSURLUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1572053-ubiquitousitemisdownloadedkey)Added [NSURLUbiquitousItemIsDownloadingKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1414260-ubiquitousitemisdownloadingkey)Added [NSURLUbiquitousItemIsUploadedKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1416038-ubiquitousitemisuploadedkey)Added [NSURLUbiquitousItemIsUploadingKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1414273-ubiquitousitemisuploadingkey)Added [NSURLUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/foundation/nsurlubiquitousitempercentdownloadedkey)Added [NSURLUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1572055-ubiquitousitempercentuploadedkey)Added [NSURLVolumeCreationDateKey](https://developer.apple.com/documentation/foundation/nsurlvolumecreationdatekey)Added [NSURLVolumeIdentifierKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1414336-volumeidentifierkey)Added [NSURLVolumeIsAutomountedKey](https://developer.apple.com/documentation/foundation/nsurlvolumeisautomountedkey)Added [NSURLVolumeIsBrowsableKey](https://developer.apple.com/documentation/foundation/nsurlvolumeisbrowsablekey)Added [NSURLVolumeIsEjectableKey](https://developer.apple.com/documentation/foundation/nsurlvolumeisejectablekey)Added [NSURLVolumeIsInternalKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1409870-volumeisinternalkey)Added [NSURLVolumeIsLocalKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1409809-volumeislocalkey)Added [NSURLVolumeIsReadOnlyKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1415182-volumeisreadonlykey)Added [NSURLVolumeIsRemovableKey](https://developer.apple.com/documentation/foundation/nsurlvolumeisremovablekey)Added [NSURLVolumeLocalizedNameKey](https://developer.apple.com/documentation/foundation/nsurlvolumelocalizednamekey)Added [NSURLVolumeMaximumFileSizeKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1417709-volumemaximumfilesizekey)Added [NSURLVolumeNameKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1416252-volumenamekey)Added [NSURLVolumeSupportsAdvisoryFileLockingKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1412637-volumesupportsadvisoryfilelockin)Added [NSURLVolumeSupportsExtendedSecurityKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1417405-volumesupportsextendedsecurityke)Added [NSURLVolumeSupportsRenamingKey](https://developer.apple.com/documentation/foundation/nsurlvolumesupportsrenamingkey)Added [NSURLVolumeSupportsRootDirectoryDatesKey](https://developer.apple.com/documentation/foundation/nsurlvolumesupportsrootdirectorydateskey)Added [NSURLVolumeSupportsVolumeSizesKey](https://developer.apple.com/documentation/foundation/nsurlvolumesupportsvolumesizeskey)Added [NSURLVolumeURLForRemountingKey](https://developer.apple.com/documentation/foundation/nsurlvolumeurlforremountingkey)Added [NSURLVolumeUUIDStringKey](https://developer.apple.com/documentation/foundation/nsurlvolumeuuidstringkey)Modified [-[NSURL getResourceValue:forKey:error:]](https://developer.apple.com/documentation/foundation/nsurl/1408874-getresourcevalue)

|  | Declaration |
| --- | --- |
| From | - (BOOL)getResourceValue:(id \*)value forKey:(NSString \*)key error:(NSError \*\*)error |
| To | - (BOOL)getResourceValue:(out id \*)value forKey:(NSString \*)key error:(out NSError \*\*)error |

NSURLAuthenticationChallenge.hAdded [-[NSURLAuthenticationChallengeSender performDefaultHandlingForAuthenticationChallenge:]](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/1414590-performdefaulthandling)Added [-[NSURLAuthenticationChallengeSender rejectProtectionSpaceAndContinueWithChallenge:]](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallengesender/1417331-rejectprotectionspaceandcontinue)Modified [NSURLAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCoding |

NSURLConnection.hRemoved -[NSObject connection:canAuthenticateAgainstProtectionSpace:]Removed -[NSObject connection:didCancelAuthenticationChallenge:]Removed -[NSObject connection:didFailWithError:]Removed -[NSObject connection:didReceiveAuthenticationChallenge:]Removed -[NSObject connection:didReceiveData:]Removed -[NSObject connection:didReceiveResponse:]Removed -[NSObject connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:]Removed -[NSObject connection:needNewBodyStream:]Removed -[NSObject connection:willCacheResponse:]Removed -[NSObject connection:willSendRequest:redirectResponse:]Removed -[NSObject connectionDidFinishLoading:]Removed -[NSObject connectionShouldUseCredentialStorage:]Removed NSObject(NSURLConnectionDelegate)Added [-[NSURLConnection currentRequest]](https://developer.apple.com/documentation/foundation/nsurlconnection/1409060-currentrequest)Added [-[NSURLConnection originalRequest]](https://developer.apple.com/documentation/foundation/nsurlconnection/1411340-originalrequest)Added [+[NSURLConnection sendAsynchronousRequest:queue:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1418125-sendasynchronousrequest)Added [-[NSURLConnection setDelegateQueue:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1411849-setdelegatequeue)Added [NSURLConnectionDataDelegate](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate)Added [-[NSURLConnectionDataDelegate connection:didReceiveData:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1414090-connection)Added [-[NSURLConnectionDataDelegate connection:didReceiveResponse:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1407728-connection)Added [-[NSURLConnectionDataDelegate connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1418264-connection)Added [-[NSURLConnectionDataDelegate connection:needNewBodyStream:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1412892-connection)Added [-[NSURLConnectionDataDelegate connection:willCacheResponse:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1414834-connection)Added [-[NSURLConnectionDataDelegate connection:willSendRequest:redirectResponse:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1415830-connection)Added [-[NSURLConnectionDataDelegate connectionDidFinishLoading:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1416409-connectiondidfinishloading)Added [NSURLConnectionDelegate](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate)Added [-[NSURLConnectionDelegate connection:canAuthenticateAgainstProtectionSpace:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1415706-connection)Added [-[NSURLConnectionDelegate connection:didCancelAuthenticationChallenge:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1407177-connection)Added [-[NSURLConnectionDelegate connection:didFailWithError:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1418443-connection)Added [-[NSURLConnectionDelegate connection:didReceiveAuthenticationChallenge:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1417135-connection)Added [-[NSURLConnectionDelegate connection:willSendRequestForAuthenticationChallenge:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1414078-connection)Added [-[NSURLConnectionDelegate connectionShouldUseCredentialStorage:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1414890-connectionshouldusecredentialsto)Added [NSURLConnectionDownloadDelegate](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate)Added [-[NSURLConnectionDownloadDelegate connection:didWriteData:totalBytesWritten:expectedTotalBytes:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/1418304-connection)Added [-[NSURLConnectionDownloadDelegate connectionDidFinishDownloading:destinationURL:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/1412126-connectiondidfinishdownloading)Added [-[NSURLConnectionDownloadDelegate connectionDidResumeDownloading:totalBytesWritten:expectedTotalBytes:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/1418157-connectiondidresumedownloading)Added NSURLConnection(NSURLConnectionQueuedLoading)NSURLCredential.hModified [NSURLCredential](https://developer.apple.com/documentation/foundation/urlcredential)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCoding, NSCopying |

NSURLProtectionSpace.hModified [NSURLProtectionSpace](https://developer.apple.com/documentation/foundation/nsurlprotectionspace)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCoding, NSCopying |

NSURLRequest.hAdded [NSURLNetworkServiceTypeBackground](https://developer.apple.com/documentation/foundation/nsurlrequestnetworkservicetype/nsurlnetworkservicetypebackground)Added [NSURLNetworkServiceTypeVideo](https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype/video)Added [NSURLNetworkServiceTypeVoice](https://developer.apple.com/documentation/foundation/nsurlrequestnetworkservicetype/nsurlnetworkservicetypevoice)NSURLResponse.hAdded [-[NSHTTPURLResponse initWithURL:statusCode:HTTPVersion:headerFields:]](https://developer.apple.com/documentation/foundation/nshttpurlresponse/1415870-initwithurl)NSUbiquitousKeyValueStore.hAdded [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore)Added [-[NSUbiquitousKeyValueStore arrayForKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1412191-arrayforkey)Added [-[NSUbiquitousKeyValueStore boolForKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1417350-bool)Added [-[NSUbiquitousKeyValueStore dataForKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1417800-data)Added [+[NSUbiquitousKeyValueStore defaultStore]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1413949-defaultstore)Added [-[NSUbiquitousKeyValueStore dictionaryForKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1416241-dictionary)Added [-[NSUbiquitousKeyValueStore dictionaryRepresentation]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1411129-dictionaryrepresentation)Added [-[NSUbiquitousKeyValueStore doubleForKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1409319-double)Added [-[NSUbiquitousKeyValueStore longLongForKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1413240-longlong)Added [-[NSUbiquitousKeyValueStore objectForKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1407436-objectforkey)Added [-[NSUbiquitousKeyValueStore removeObjectForKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1410916-removeobjectforkey)Added [-[NSUbiquitousKeyValueStore setArray:forKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1417721-set)Added [-[NSUbiquitousKeyValueStore setBool:forKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1415054-set)Added [-[NSUbiquitousKeyValueStore setData:forKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1416218-setdata)Added [-[NSUbiquitousKeyValueStore setDictionary:forKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1417155-setdictionary)Added [-[NSUbiquitousKeyValueStore setDouble:forKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1412608-setdouble)Added [-[NSUbiquitousKeyValueStore setLongLong:forKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1407812-setlonglong)Added [-[NSUbiquitousKeyValueStore setObject:forKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1416434-set)Added [-[NSUbiquitousKeyValueStore setString:forKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1414610-setstring)Added [-[NSUbiquitousKeyValueStore stringForKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1418249-stringforkey)Added [-[NSUbiquitousKeyValueStore synchronize]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1415989-synchronize)Added [NSUbiquitousKeyValueStoreChangeReasonKey](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestorechangereasonkey)Added [NSUbiquitousKeyValueStoreChangedKeysKey](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestorechangedkeyskey)Added [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1412267-didchangeexternallynotification)Added [NSUbiquitousKeyValueStoreInitialSyncChange](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestoreinitialsyncchange)Added [NSUbiquitousKeyValueStoreQuotaViolationChange](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestorequotaviolationchange)Added [NSUbiquitousKeyValueStoreServerChange](https://developer.apple.com/documentation/foundation/1433687-change_reason_values/nsubiquitouskeyvaluestoreserverchange)NSUndoManager.hAdded [-[NSUndoManager redoActionIsDiscardable]](https://developer.apple.com/documentation/foundation/nsundomanager/1413488-redoactionisdiscardable)Added [-[NSUndoManager setActionIsDiscardable:]](https://developer.apple.com/documentation/foundation/undomanager/1412159-setactionisdiscardable)Added [-[NSUndoManager undoActionIsDiscardable]](https://developer.apple.com/documentation/foundation/undomanager/1415261-undoactionisdiscardable)Added [NSUndoManagerDidCloseUndoGroupNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1408817-nsundomanagerdidcloseundogroup)Added [NSUndoManagerGroupIsDiscardableKey](https://developer.apple.com/documentation/foundation/nsundomanagergroupisdiscardablekey)NSXMLParser.hAdded [-[NSXMLParser initWithStream:]](https://developer.apple.com/documentation/foundation/nsxmlparser/1415904-initwithstream)NSZone.hAdded #def CF_CONSUMED

## GameKit

GKAchievement.hAdded [GKAchievement.showsCompletionBanner](https://developer.apple.com/documentation/gamekit/gkachievement/1521058-showscompletionbanner)GKDefines.hAdded #def GK_EXTERN_WEAKGKError.hAdded [GKErrorUnexpectedConnection](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorunexpectedconnection)GKLeaderboard.hAdded [+[GKLeaderboard setDefaultLeaderboard:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503123-setdefaultleaderboard)GKMatch.hAdded [-[GKMatchDelegate match:shouldReinvitePlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502058-match)GKMatchmakerViewController.hAdded [-[GKMatchmakerViewController addPlayersToMatch:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492425-addplayers)Added [GKMatchmakerViewController.defaultInvitationMessage](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492409-defaultinvitationmessage)Added [-[GKMatchmakerViewController setHostedPlayer:connected:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492418-sethostedplayer)Added [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didReceiveAcceptFromHostedPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492436-matchmakerviewcontroller)Modified [-[GKMatchmakerViewController setHostedPlayerReady:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1620326-sethostedplayerready)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

GKNotificationBanner.hAdded [GKNotificationBanner](https://developer.apple.com/documentation/gamekit/gknotificationbanner)Added [+[GKNotificationBanner showBannerWithTitle:message:completionHandler:]](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515370-showbannerwithtitle)GKPlayer.hAdded [-[GKPlayer loadPhotoForSize:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkplayer/1521176-loadphoto)Added [GKPhotoSize](https://developer.apple.com/documentation/gamekit/gkphotosize)Added [GKPhotoSizeNormal](https://developer.apple.com/documentation/gamekit/gkphotosize/gkphotosizenormal)Added [GKPhotoSizeSmall](https://developer.apple.com/documentation/gamekit/gkphotosize/gkphotosizesmall)GKScore.hAdded [GKScore.context](https://developer.apple.com/documentation/gamekit/gkscore/1399250-context)Added [GKScore.shouldSetDefaultLeaderboard](https://developer.apple.com/documentation/gamekit/gkscore/1399238-shouldsetdefaultleaderboard)GKTurnBasedMatch.hAdded [GKTurnBasedEventHandler](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler)Added [GKTurnBasedEventHandler.delegate](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/1521013-delegate)Added [+[GKTurnBasedEventHandler sharedTurnBasedEventHandler]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/1521211-sharedturnbasedeventhandler)Added [GKTurnBasedEventHandlerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate)Added [-[GKTurnBasedEventHandlerDelegate handleInviteFromGameCenter:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1520926-handleinvite)Added [-[GKTurnBasedEventHandlerDelegate handleMatchEnded:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1521053-handlematchended)Added [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1556899-handleturneventformatch)Added [GKTurnBasedMatch](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch)Added [GKTurnBasedMatch.creationDate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521168-creationdate)Added [GKTurnBasedMatch.currentParticipant](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520643-currentparticipant)Added [-[GKTurnBasedMatch endMatchInTurnWithMatchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520907-endmatchinturn)Added [-[GKTurnBasedMatch endTurnWithNextParticipant:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1556897-endturn)Added [+[GKTurnBasedMatch findMatchForRequest:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521008-find)Added [-[GKTurnBasedMatch loadMatchDataWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521005-loadmatchdata)Added [+[GKTurnBasedMatch loadMatchesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521207-loadmatcheswithcompletionhandler)Added [GKTurnBasedMatch.matchData](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520991-matchdata)Added [GKTurnBasedMatch.matchID](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520625-matchid)Added [GKTurnBasedMatch.message](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520721-message)Added [-[GKTurnBasedMatch participantQuitInTurnWithOutcome:nextParticipant:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1556898-participantquitinturnwithoutcome)Added [-[GKTurnBasedMatch participantQuitOutOfTurnWithOutcome:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521106-participantquitoutofturnwithoutc)Added [GKTurnBasedMatch.participants](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520875-participants)Added [-[GKTurnBasedMatch removeWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520651-remove)Added [GKTurnBasedMatch.status](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520548-status)Added [GKTurnBasedParticipant](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant)Added [GKTurnBasedParticipant.lastTurnDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520941-lastturndate)Added [GKTurnBasedParticipant.matchOutcome](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521110-matchoutcome)Added [GKTurnBasedParticipant.playerID](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520474-playerid)Added [GKTurnBasedParticipant.status](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520514-status)Added [GKTurnBasedMatchOutcome](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome)Added [GKTurnBasedMatchOutcomeCustomRange](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/customrange)Added [GKTurnBasedMatchOutcomeFirst](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/gkturnbasedmatchoutcomefirst)Added [GKTurnBasedMatchOutcomeFourth](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/fourth)Added [GKTurnBasedMatchOutcomeLost](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/lost)Added [GKTurnBasedMatchOutcomeNone](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/gkturnbasedmatchoutcomenone)Added [GKTurnBasedMatchOutcomeQuit](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/gkturnbasedmatchoutcomequit)Added [GKTurnBasedMatchOutcomeSecond](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/second)Added [GKTurnBasedMatchOutcomeThird](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/gkturnbasedmatchoutcomethird)Added [GKTurnBasedMatchOutcomeTied](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/gkturnbasedmatchoutcometied)Added [GKTurnBasedMatchOutcomeTimeExpired](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/gkturnbasedmatchoutcometimeexpired)Added [GKTurnBasedMatchOutcomeWon](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/gkturnbasedmatchoutcomewon)Added [GKTurnBasedMatchStatus](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus)Added [GKTurnBasedMatchStatusEnded](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus/ended)Added [GKTurnBasedMatchStatusMatching](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus/gkturnbasedmatchstatusmatching)Added [GKTurnBasedMatchStatusOpen](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus/gkturnbasedmatchstatusopen)Added [GKTurnBasedMatchStatusUnknown](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus/unknown)Added [GKTurnBasedParticipantStatus](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus)Added [GKTurnBasedParticipantStatusActive](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/active)Added [GKTurnBasedParticipantStatusDeclined](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/gkturnbasedparticipantstatusdeclined)Added [GKTurnBasedParticipantStatusDone](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/gkturnbasedparticipantstatusdone)Added [GKTurnBasedParticipantStatusInvited](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/gkturnbasedparticipantstatusinvited)Added [GKTurnBasedParticipantStatusMatching](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/gkturnbasedparticipantstatusmatching)Added [GKTurnBasedParticipantStatusUnknown](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/gkturnbasedparticipantstatusunknown)GKTurnBasedMatchmakerViewController.hAdded [GKTurnBasedMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller)Added [-[GKTurnBasedMatchmakerViewController initWithMatchRequest:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1521069-init)Added [GKTurnBasedMatchmakerViewController.showExistingMatches](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1521099-showexistingmatches)Added [GKTurnBasedMatchmakerViewController.turnBasedMatchmakerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1520697-turnbasedmatchmakerdelegate)Added [GKTurnBasedMatchmakerViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate)Added [-[GKTurnBasedMatchmakerViewControllerDelegate turnBasedMatchmakerViewController:didFailWithError:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1521028-turnbasedmatchmakerviewcontrolle)Added [-[GKTurnBasedMatchmakerViewControllerDelegate turnBasedMatchmakerViewController:didFindMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1520653-turnbasedmatchmakerviewcontrolle)Added [-[GKTurnBasedMatchmakerViewControllerDelegate turnBasedMatchmakerViewController:playerQuitForMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1520967-turnbasedmatchmakerviewcontrolle)Added [-[GKTurnBasedMatchmakerViewControllerDelegate turnBasedMatchmakerViewControllerWasCancelled:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1521000-turnbasedmatchmakerviewcontrolle)GKVoiceChat.hAdded [GKVoiceChat.playerIDs](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385721-playerids)

## GLKit

GLKBaseEffect.hAdded [GLKBaseEffect](https://developer.apple.com/documentation/glkit/glkbaseeffect)Added [GLKBaseEffect.colorMaterialEnabled](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488710-colormaterialenabled)Added [GLKBaseEffect.constantColor](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488903-constantcolor)Added [GLKBaseEffect.fog](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488697-fog)Added [GLKBaseEffect.label](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488835-label)Added [GLKBaseEffect.light0](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488785-light0)Added [GLKBaseEffect.light1](https://developer.apple.com/documentation/glkit/glkbaseeffect/1489095-light1)Added [GLKBaseEffect.light2](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488671-light2)Added [GLKBaseEffect.lightModelAmbientColor](https://developer.apple.com/documentation/glkit/glkbaseeffect/1489061-lightmodelambientcolor)Added [GLKBaseEffect.lightModelTwoSided](https://developer.apple.com/documentation/glkit/glkbaseeffect/1489036-lightmodeltwosided)Added [GLKBaseEffect.lightingType](https://developer.apple.com/documentation/glkit/glkbaseeffect/1489037-lightingtype)Added [GLKBaseEffect.material](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488753-material)Added [-[GLKBaseEffect prepareToDraw]](https://developer.apple.com/documentation/glkit/glkbaseeffect/1489101-preparetodraw)Added [GLKBaseEffect.texture2d0](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488664-texture2d0)Added [GLKBaseEffect.texture2d1](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488699-texture2d1)Added [GLKBaseEffect.textureOrder](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488830-textureorder)Added [GLKBaseEffect.transform](https://developer.apple.com/documentation/glkit/glkbaseeffect/1489030-transform)Added [GLKBaseEffect.useConstantColor](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488783-useconstantcolor)GLKEffectProperty.hAdded [GLKEffectProperty](https://developer.apple.com/documentation/glkit/glkeffectproperty)Added GLKEffectPropertyPrvPtrGLKEffectPropertyFog.hAdded [GLKEffectPropertyFog](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog)Added [GLKEffectPropertyFog.color](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/1429938-color)Added [GLKEffectPropertyFog.density](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/1429947-density)Added [GLKEffectPropertyFog.enabled](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/1429941-enabled)Added [GLKEffectPropertyFog.end](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/1429949-end)Added [GLKEffectPropertyFog.mode](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/1429943-mode)Added [GLKEffectPropertyFog.start](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/1429936-start)Added [GLKFogModeExp](https://developer.apple.com/documentation/glkit/glkfogmode/exp)Added [GLKFogModeExp2](https://developer.apple.com/documentation/glkit/glkfogmode/glkfogmodeexp2)Added [GLKFogModeLinear](https://developer.apple.com/documentation/glkit/glkfogmode/glkfogmodelinear)GLKEffectPropertyLight.hAdded [GLKEffectPropertyLight](https://developer.apple.com/documentation/glkit/glkeffectpropertylight)Added [GLKEffectPropertyLight.ambientColor](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473564-ambientcolor)Added [GLKEffectPropertyLight.constantAttenuation](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473574-constantattenuation)Added [GLKEffectPropertyLight.diffuseColor](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473560-diffusecolor)Added [GLKEffectPropertyLight.enabled](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473558-enabled)Added [GLKEffectPropertyLight.linearAttenuation](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473549-linearattenuation)Added [GLKEffectPropertyLight.position](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473576-position)Added [GLKEffectPropertyLight.quadraticAttenuation](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473578-quadraticattenuation)Added [GLKEffectPropertyLight.specularColor](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473562-specularcolor)Added [GLKEffectPropertyLight.spotCutoff](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473572-spotcutoff)Added [GLKEffectPropertyLight.spotDirection](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473547-spotdirection)Added [GLKEffectPropertyLight.spotExponent](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473551-spotexponent)Added [GLKEffectPropertyLight.transform](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473568-transform)Added [GLKLightingType](https://developer.apple.com/documentation/glkit/glklightingtype)Added [GLKLightingTypePerPixel](https://developer.apple.com/documentation/glkit/glklightingtype/perpixel)Added [GLKLightingTypePerVertex](https://developer.apple.com/documentation/glkit/glklightingtype/pervertex)GLKEffectPropertyMaterial.hAdded [GLKEffectPropertyMaterial](https://developer.apple.com/documentation/glkit/glkeffectpropertymaterial)Added [GLKEffectPropertyMaterial.ambientColor](https://developer.apple.com/documentation/glkit/glkeffectpropertymaterial/1409844-ambientcolor)Added [GLKEffectPropertyMaterial.diffuseColor](https://developer.apple.com/documentation/glkit/glkeffectpropertymaterial/1409843-diffusecolor)Added [GLKEffectPropertyMaterial.emissiveColor](https://developer.apple.com/documentation/glkit/glkeffectpropertymaterial/1409839-emissivecolor)Added [GLKEffectPropertyMaterial.shininess](https://developer.apple.com/documentation/glkit/glkeffectpropertymaterial/1409837-shininess)Added [GLKEffectPropertyMaterial.specularColor](https://developer.apple.com/documentation/glkit/glkeffectpropertymaterial/1409841-specularcolor)GLKEffectPropertyTexture.hAdded [GLKEffectPropertyTexture](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture)Added [GLKEffectPropertyTexture.enabled](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture/1488708-enabled)Added [GLKEffectPropertyTexture.envMode](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture/1488986-envmode)Added [GLKEffectPropertyTexture.name](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture/1488884-name)Added [GLKEffectPropertyTexture.target](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture/1488852-target)Added [GLKTextureEnvMode](https://developer.apple.com/documentation/glkit/glktextureenvmode)Added [GLKTextureEnvModeDecal](https://developer.apple.com/documentation/glkit/glktextureenvmode/decal)Added [GLKTextureEnvModeModulate](https://developer.apple.com/documentation/glkit/glktextureenvmode/glktextureenvmodemodulate)Added [GLKTextureEnvModeReplace](https://developer.apple.com/documentation/glkit/glktextureenvmode/replace)Added [GLKTextureTarget](https://developer.apple.com/documentation/glkit/glktexturetarget)Added [GLKTextureTarget2D](https://developer.apple.com/documentation/glkit/glktexturetarget/target2d)Added [GLKTextureTargetCt](https://developer.apple.com/documentation/glkit/glktexturetarget/glktexturetargetct)Added [GLKTextureTargetCubeMap](https://developer.apple.com/documentation/glkit/glktexturetarget/targetcubemap)GLKEffectPropertyTransform.hAdded [GLKEffectPropertyTransform](https://developer.apple.com/documentation/glkit/glkeffectpropertytransform)Added [GLKEffectPropertyTransform.modelviewMatrix](https://developer.apple.com/documentation/glkit/glkeffectpropertytransform/1489097-modelviewmatrix)Added [GLKEffectPropertyTransform.normalMatrix](https://developer.apple.com/documentation/glkit/glkeffectpropertytransform/1488648-normalmatrix)Added [GLKEffectPropertyTransform.projectionMatrix](https://developer.apple.com/documentation/glkit/glkeffectpropertytransform/1489114-projectionmatrix)GLKEffects.hAdded [GLKVertexAttrib](https://developer.apple.com/documentation/glkit/glkvertexattrib)Added [GLKVertexAttribColor](https://developer.apple.com/documentation/glkit/glkvertexattrib/glkvertexattribcolor)Added [GLKVertexAttribNormal](https://developer.apple.com/documentation/glkit/glkvertexattrib/glkvertexattribnormal)Added [GLKVertexAttribPosition](https://developer.apple.com/documentation/glkit/glkvertexattrib/position)Added [GLKVertexAttribTexCoord0](https://developer.apple.com/documentation/glkit/glkvertexattrib/texcoord0)Added [GLKVertexAttribTexCoord1](https://developer.apple.com/documentation/glkit/glkvertexattrib/texcoord1)GLKMathTypes.hAdded [GLKMatrix2](https://developer.apple.com/documentation/glkit/glkmatrix2)Added [GLKMatrix3](https://developer.apple.com/documentation/glkit/1462419-glkmatrix3)Added [GLKMatrix4](https://developer.apple.com/documentation/glkit/1462441-glkmatrix4)Added [GLKQuaternion](https://developer.apple.com/documentation/glkit/1462435-glkquaternion)Added [GLKVector2](https://developer.apple.com/documentation/glkit/1462421-glkvector2)Added [GLKVector3](https://developer.apple.com/documentation/glkit/1462425-glkvector3)Added [GLKVector4](https://developer.apple.com/documentation/glkit/glkvector4)GLKMathUtils.hAdded [GLKMathDegreesToRadians()](https://developer.apple.com/documentation/glkit/1488960-glkmathdegreestoradians)Added [GLKMathProject()](https://developer.apple.com/documentation/glkit/1488726-glkmathproject)Added [GLKMathRadiansToDegrees()](https://developer.apple.com/documentation/glkit/1488628-glkmathradianstodegrees)Added [GLKMathUnproject()](https://developer.apple.com/documentation/glkit/1488720-glkmathunproject)Added [NSStringFromGLKMatrix2()](https://developer.apple.com/documentation/glkit/1489099-nsstringfromglkmatrix2)Added [NSStringFromGLKMatrix3()](https://developer.apple.com/documentation/glkit/1489048-nsstringfromglkmatrix3)Added [NSStringFromGLKMatrix4()](https://developer.apple.com/documentation/glkit/1488877-nsstringfromglkmatrix4)Added [NSStringFromGLKQuaternion()](https://developer.apple.com/documentation/glkit/1488908-nsstringfromglkquaternion)Added [NSStringFromGLKVector2()](https://developer.apple.com/documentation/glkit/1488857-nsstringfromglkvector2)Added [NSStringFromGLKVector3()](https://developer.apple.com/documentation/glkit/1489089-nsstringfromglkvector3)Added [NSStringFromGLKVector4()](https://developer.apple.com/documentation/glkit/1489056-nsstringfromglkvector4)GLKMatrix3.hAdded [GLKMatrix3Add()](https://developer.apple.com/documentation/glkit/1489128-glkmatrix3add)Added [GLKMatrix3GetColumn()](https://developer.apple.com/documentation/glkit/1488850-glkmatrix3getcolumn)Added [GLKMatrix3GetMatrix2()](https://developer.apple.com/documentation/glkit/1489118-glkmatrix3getmatrix2)Added [GLKMatrix3GetRow()](https://developer.apple.com/documentation/glkit/1489066-glkmatrix3getrow)Added [GLKMatrix3Identity](https://developer.apple.com/documentation/glkit/glkmatrix3identity)Added [GLKMatrix3Invert()](https://developer.apple.com/documentation/glkit/1488816-glkmatrix3invert)Added [GLKMatrix3InvertAndTranspose()](https://developer.apple.com/documentation/glkit/1488692-glkmatrix3invertandtranspose)Added [GLKMatrix3Make()](https://developer.apple.com/documentation/glkit/1489086-glkmatrix3make)Added [GLKMatrix3MakeAndTranspose()](https://developer.apple.com/documentation/glkit/1489084-glkmatrix3makeandtranspose)Added [GLKMatrix3MakeRotation()](https://developer.apple.com/documentation/glkit/1489109-glkmatrix3makerotation)Added [GLKMatrix3MakeScale()](https://developer.apple.com/documentation/glkit/1489127-glkmatrix3makescale)Added [GLKMatrix3MakeWithArray()](https://developer.apple.com/documentation/glkit/1488889-glkmatrix3makewitharray)Added [GLKMatrix3MakeWithArrayAndTranspose()](https://developer.apple.com/documentation/glkit/1488737-glkmatrix3makewitharrayandtransp)Added [GLKMatrix3MakeWithColumns()](https://developer.apple.com/documentation/glkit/1488962-glkmatrix3makewithcolumns)Added [GLKMatrix3MakeWithQuaternion()](https://developer.apple.com/documentation/glkit/1489121-glkmatrix3makewithquaternion)Added [GLKMatrix3MakeWithRows()](https://developer.apple.com/documentation/glkit/1488995-glkmatrix3makewithrows)Added [GLKMatrix3MakeXRotation()](https://developer.apple.com/documentation/glkit/1489022-glkmatrix3makexrotation)Added [GLKMatrix3MakeYRotation()](https://developer.apple.com/documentation/glkit/1488998-glkmatrix3makeyrotation)Added [GLKMatrix3MakeZRotation()](https://developer.apple.com/documentation/glkit/1488741-glkmatrix3makezrotation)Added [GLKMatrix3Multiply()](https://developer.apple.com/documentation/glkit/1488643-glkmatrix3multiply)Added [GLKMatrix3MultiplyVector3()](https://developer.apple.com/documentation/glkit/1489125-glkmatrix3multiplyvector3)Added [GLKMatrix3MultiplyVector3Array()](https://developer.apple.com/documentation/glkit/1488871-glkmatrix3multiplyvector3array)Added [GLKMatrix3Rotate()](https://developer.apple.com/documentation/glkit/1488775-glkmatrix3rotate)Added [GLKMatrix3RotateWithVector3()](https://developer.apple.com/documentation/glkit/1488657-glkmatrix3rotatewithvector3)Added [GLKMatrix3RotateWithVector4()](https://developer.apple.com/documentation/glkit/1489094-glkmatrix3rotatewithvector4)Added [GLKMatrix3RotateX()](https://developer.apple.com/documentation/glkit/1489047-glkmatrix3rotatex)Added [GLKMatrix3RotateY()](https://developer.apple.com/documentation/glkit/1488806-glkmatrix3rotatey)Added [GLKMatrix3RotateZ()](https://developer.apple.com/documentation/glkit/1488881-glkmatrix3rotatez)Added [GLKMatrix3Scale()](https://developer.apple.com/documentation/glkit/1488970-glkmatrix3scale)Added [GLKMatrix3ScaleWithVector3()](https://developer.apple.com/documentation/glkit/1489011-glkmatrix3scalewithvector3)Added [GLKMatrix3ScaleWithVector4()](https://developer.apple.com/documentation/glkit/1488619-glkmatrix3scalewithvector4)Added [GLKMatrix3SetColumn()](https://developer.apple.com/documentation/glkit/1488640-glkmatrix3setcolumn)Added [GLKMatrix3SetRow()](https://developer.apple.com/documentation/glkit/1488780-glkmatrix3setrow)Added [GLKMatrix3Subtract()](https://developer.apple.com/documentation/glkit/1489031-glkmatrix3subtract)Added [GLKMatrix3Transpose()](https://developer.apple.com/documentation/glkit/1489053-glkmatrix3transpose)GLKMatrix4.hAdded [GLKMatrix4Add()](https://developer.apple.com/documentation/glkit/1488772-glkmatrix4add)Added [GLKMatrix4GetColumn()](https://developer.apple.com/documentation/glkit/1489062-glkmatrix4getcolumn)Added [GLKMatrix4GetMatrix2()](https://developer.apple.com/documentation/glkit/1488660-glkmatrix4getmatrix2)Added [GLKMatrix4GetMatrix3()](https://developer.apple.com/documentation/glkit/1488632-glkmatrix4getmatrix3)Added [GLKMatrix4GetRow()](https://developer.apple.com/documentation/glkit/1489075-glkmatrix4getrow)Added [GLKMatrix4Identity](https://developer.apple.com/documentation/glkit/glkmatrix4identity)Added [GLKMatrix4Invert()](https://developer.apple.com/documentation/glkit/1488859-glkmatrix4invert)Added [GLKMatrix4InvertAndTranspose()](https://developer.apple.com/documentation/glkit/1489040-glkmatrix4invertandtranspose)Added [GLKMatrix4Make()](https://developer.apple.com/documentation/glkit/1488803-glkmatrix4make)Added [GLKMatrix4MakeAndTranspose()](https://developer.apple.com/documentation/glkit/1488799-glkmatrix4makeandtranspose)Added [GLKMatrix4MakeFrustum()](https://developer.apple.com/documentation/glkit/1488610-glkmatrix4makefrustum)Added [GLKMatrix4MakeLookAt()](https://developer.apple.com/documentation/glkit/1488691-glkmatrix4makelookat)Added [GLKMatrix4MakeOrtho()](https://developer.apple.com/documentation/glkit/1488872-glkmatrix4makeortho)Added [GLKMatrix4MakePerspective()](https://developer.apple.com/documentation/glkit/1488637-glkmatrix4makeperspective)Added [GLKMatrix4MakeRotation()](https://developer.apple.com/documentation/glkit/1488749-glkmatrix4makerotation)Added [GLKMatrix4MakeScale()](https://developer.apple.com/documentation/glkit/1489055-glkmatrix4makescale)Added [GLKMatrix4MakeTranslation()](https://developer.apple.com/documentation/glkit/1488653-glkmatrix4maketranslation)Added [GLKMatrix4MakeWithArray()](https://developer.apple.com/documentation/glkit/1488687-glkmatrix4makewitharray)Added [GLKMatrix4MakeWithArrayAndTranspose()](https://developer.apple.com/documentation/glkit/1489079-glkmatrix4makewitharrayandtransp)Added [GLKMatrix4MakeWithColumns()](https://developer.apple.com/documentation/glkit/1489026-glkmatrix4makewithcolumns)Added [GLKMatrix4MakeWithQuaternion()](https://developer.apple.com/documentation/glkit/1489088-glkmatrix4makewithquaternion)Added [GLKMatrix4MakeWithRows()](https://developer.apple.com/documentation/glkit/1489033-glkmatrix4makewithrows)Added [GLKMatrix4MakeXRotation()](https://developer.apple.com/documentation/glkit/1488694-glkmatrix4makexrotation)Added [GLKMatrix4MakeYRotation()](https://developer.apple.com/documentation/glkit/1489054-glkmatrix4makeyrotation)Added [GLKMatrix4MakeZRotation()](https://developer.apple.com/documentation/glkit/1488683-glkmatrix4makezrotation)Added [GLKMatrix4Multiply()](https://developer.apple.com/documentation/glkit/1489045-glkmatrix4multiply)Added [GLKMatrix4MultiplyAndProjectVector3()](https://developer.apple.com/documentation/glkit/1488761-glkmatrix4multiplyandprojectvect)Added [GLKMatrix4MultiplyAndProjectVector3Array()](https://developer.apple.com/documentation/glkit/1489093-glkmatrix4multiplyandprojectvect)Added [GLKMatrix4MultiplyVector3()](https://developer.apple.com/documentation/glkit/1489017-glkmatrix4multiplyvector3)Added [GLKMatrix4MultiplyVector3Array()](https://developer.apple.com/documentation/glkit/1488937-glkmatrix4multiplyvector3array)Added [GLKMatrix4MultiplyVector3ArrayWithTranslation()](https://developer.apple.com/documentation/glkit/1489028-glkmatrix4multiplyvector3arraywi)Added [GLKMatrix4MultiplyVector3WithTranslation()](https://developer.apple.com/documentation/glkit/1489102-glkmatrix4multiplyvector3withtra)Added [GLKMatrix4MultiplyVector4()](https://developer.apple.com/documentation/glkit/1489016-glkmatrix4multiplyvector4)Added [GLKMatrix4MultiplyVector4Array()](https://developer.apple.com/documentation/glkit/1489090-glkmatrix4multiplyvector4array)Added [GLKMatrix4Rotate()](https://developer.apple.com/documentation/glkit/1489039-glkmatrix4rotate)Added [GLKMatrix4RotateWithVector3()](https://developer.apple.com/documentation/glkit/1488645-glkmatrix4rotatewithvector3)Added [GLKMatrix4RotateWithVector4()](https://developer.apple.com/documentation/glkit/1488821-glkmatrix4rotatewithvector4)Added [GLKMatrix4RotateX()](https://developer.apple.com/documentation/glkit/1489070-glkmatrix4rotatex)Added [GLKMatrix4RotateY()](https://developer.apple.com/documentation/glkit/1488626-glkmatrix4rotatey)Added [GLKMatrix4RotateZ()](https://developer.apple.com/documentation/glkit/1488641-glkmatrix4rotatez)Added [GLKMatrix4Scale()](https://developer.apple.com/documentation/glkit/1489091-glkmatrix4scale)Added [GLKMatrix4ScaleWithVector3()](https://developer.apple.com/documentation/glkit/1489116-glkmatrix4scalewithvector3)Added [GLKMatrix4ScaleWithVector4()](https://developer.apple.com/documentation/glkit/1489008-glkmatrix4scalewithvector4)Added [GLKMatrix4SetColumn()](https://developer.apple.com/documentation/glkit/1488730-glkmatrix4setcolumn)Added [GLKMatrix4SetRow()](https://developer.apple.com/documentation/glkit/1488625-glkmatrix4setrow)Added [GLKMatrix4Subtract()](https://developer.apple.com/documentation/glkit/1489029-glkmatrix4subtract)Added [GLKMatrix4Translate()](https://developer.apple.com/documentation/glkit/1488875-glkmatrix4translate)Added [GLKMatrix4TranslateWithVector3()](https://developer.apple.com/documentation/glkit/1488863-glkmatrix4translatewithvector3)Added [GLKMatrix4TranslateWithVector4()](https://developer.apple.com/documentation/glkit/1489130-glkmatrix4translatewithvector4)Added [GLKMatrix4Transpose()](https://developer.apple.com/documentation/glkit/1489100-glkmatrix4transpose)GLKMatrixStack.hAdded [GLKMatrixStackCreate()](https://developer.apple.com/documentation/glkit/1483169-glkmatrixstackcreate)Added [GLKMatrixStackGetMatrix2()](https://developer.apple.com/documentation/glkit/1483181-glkmatrixstackgetmatrix2)Added [GLKMatrixStackGetMatrix3()](https://developer.apple.com/documentation/glkit/1483158-glkmatrixstackgetmatrix3)Added [GLKMatrixStackGetMatrix3Inverse()](https://developer.apple.com/documentation/glkit/1483159-glkmatrixstackgetmatrix3inverse)Added [GLKMatrixStackGetMatrix3InverseTranspose()](https://developer.apple.com/documentation/glkit/1483160-glkmatrixstackgetmatrix3inverset)Added [GLKMatrixStackGetMatrix4()](https://developer.apple.com/documentation/glkit/1483163-glkmatrixstackgetmatrix4)Added [GLKMatrixStackGetMatrix4Inverse()](https://developer.apple.com/documentation/glkit/1483168-glkmatrixstackgetmatrix4inverse)Added [GLKMatrixStackGetMatrix4InverseTranspose()](https://developer.apple.com/documentation/glkit/1483184-glkmatrixstackgetmatrix4inverset)Added [GLKMatrixStackGetTypeID()](https://developer.apple.com/documentation/glkit/1483166-glkmatrixstackgettypeid)Added [GLKMatrixStackLoadMatrix4()](https://developer.apple.com/documentation/glkit/1483161-glkmatrixstackloadmatrix4)Added [GLKMatrixStackMultiplyMatrix4()](https://developer.apple.com/documentation/glkit/1483162-glkmatrixstackmultiplymatrix4)Added [GLKMatrixStackMultiplyMatrixStack()](https://developer.apple.com/documentation/glkit/1483197-glkmatrixstackmultiplymatrixstac)Added [GLKMatrixStackPop()](https://developer.apple.com/documentation/glkit/1483174-glkmatrixstackpop)Added [GLKMatrixStackPush()](https://developer.apple.com/documentation/glkit/1483190-glkmatrixstackpush)Added [GLKMatrixStackRef](https://developer.apple.com/documentation/glkit/glkmatrixstackref)Added [GLKMatrixStackRotate()](https://developer.apple.com/documentation/glkit/1483179-glkmatrixstackrotate)Added [GLKMatrixStackRotateWithVector3()](https://developer.apple.com/documentation/glkit/1483192-glkmatrixstackrotatewithvector3)Added [GLKMatrixStackRotateWithVector4()](https://developer.apple.com/documentation/glkit/1483188-glkmatrixstackrotatewithvector4)Added [GLKMatrixStackRotateX()](https://developer.apple.com/documentation/glkit/1483195-glkmatrixstackrotatex)Added [GLKMatrixStackRotateY()](https://developer.apple.com/documentation/glkit/1483157-glkmatrixstackrotatey)Added [GLKMatrixStackRotateZ()](https://developer.apple.com/documentation/glkit/1483171-glkmatrixstackrotatez)Added [GLKMatrixStackScale()](https://developer.apple.com/documentation/glkit/1483164-glkmatrixstackscale)Added [GLKMatrixStackScaleWithVector3()](https://developer.apple.com/documentation/glkit/1483176-glkmatrixstackscalewithvector3)Added [GLKMatrixStackScaleWithVector4()](https://developer.apple.com/documentation/glkit/1483183-glkmatrixstackscalewithvector4)Added [GLKMatrixStackSize()](https://developer.apple.com/documentation/glkit/1483156-glkmatrixstacksize)Added [GLKMatrixStackTranslate()](https://developer.apple.com/documentation/glkit/1483177-glkmatrixstacktranslate)Added [GLKMatrixStackTranslateWithVector3()](https://developer.apple.com/documentation/glkit/1483186-glkmatrixstacktranslatewithvecto)Added [GLKMatrixStackTranslateWithVector4()](https://developer.apple.com/documentation/glkit/1483172-glkmatrixstacktranslatewithvecto)GLKNamedEffect.hAdded [GLKNamedEffect](https://developer.apple.com/documentation/glkit/glknamedeffect)Added [-[GLKNamedEffect prepareToDraw]](https://developer.apple.com/documentation/glkit/glknamedeffect/1459375-preparetodraw)GLKQuaternion.hAdded [GLKQuaternionAdd()](https://developer.apple.com/documentation/glkit/1476861-glkquaternionadd)Added [GLKQuaternionAngle()](https://developer.apple.com/documentation/glkit/1476867-glkquaternionangle)Added [GLKQuaternionAxis()](https://developer.apple.com/documentation/glkit/1476895-glkquaternionaxis)Added [GLKQuaternionConjugate()](https://developer.apple.com/documentation/glkit/1476885-glkquaternionconjugate)Added [GLKQuaternionIdentity](https://developer.apple.com/documentation/glkit/glkquaternionidentity)Added [GLKQuaternionInvert()](https://developer.apple.com/documentation/glkit/1476873-glkquaternioninvert)Added [GLKQuaternionLength()](https://developer.apple.com/documentation/glkit/1476877-glkquaternionlength)Added [GLKQuaternionMake()](https://developer.apple.com/documentation/glkit/1476903-glkquaternionmake)Added [GLKQuaternionMakeWithAngleAndAxis()](https://developer.apple.com/documentation/glkit/1476891-glkquaternionmakewithangleandaxi)Added [GLKQuaternionMakeWithAngleAndVector3Axis()](https://developer.apple.com/documentation/glkit/1476897-glkquaternionmakewithangleandvec)Added [GLKQuaternionMakeWithArray()](https://developer.apple.com/documentation/glkit/1476889-glkquaternionmakewitharray)Added [GLKQuaternionMakeWithMatrix3()](https://developer.apple.com/documentation/glkit/1476865-glkquaternionmakewithmatrix3)Added [GLKQuaternionMakeWithMatrix4()](https://developer.apple.com/documentation/glkit/1476881-glkquaternionmakewithmatrix4)Added [GLKQuaternionMakeWithVector3()](https://developer.apple.com/documentation/glkit/1476883-glkquaternionmakewithvector3)Added [GLKQuaternionMultiply()](https://developer.apple.com/documentation/glkit/1476863-glkquaternionmultiply)Added [GLKQuaternionNormalize()](https://developer.apple.com/documentation/glkit/1476893-glkquaternionnormalize)Added [GLKQuaternionRotateVector3()](https://developer.apple.com/documentation/glkit/1476869-glkquaternionrotatevector3)Added [GLKQuaternionRotateVector3Array()](https://developer.apple.com/documentation/glkit/1476901-glkquaternionrotatevector3array)Added [GLKQuaternionRotateVector4()](https://developer.apple.com/documentation/glkit/1476887-glkquaternionrotatevector4)Added [GLKQuaternionRotateVector4Array()](https://developer.apple.com/documentation/glkit/1476879-glkquaternionrotatevector4array)Added [GLKQuaternionSlerp()](https://developer.apple.com/documentation/glkit/1476875-glkquaternionslerp)Added [GLKQuaternionSubtract()](https://developer.apple.com/documentation/glkit/1476871-glkquaternionsubtract)GLKReflectionMapEffect.hAdded [GLKReflectionMapEffect](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect)Added [GLKReflectionMapEffect.matrix](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect/1415314-matrix)Added [-[GLKReflectionMapEffect prepareToDraw]](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect/1415310-preparetodraw)Added [GLKReflectionMapEffect.textureCubeMap](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect/1415312-texturecubemap)GLKSkyboxEffect.hAdded [GLKSkyboxEffect](https://developer.apple.com/documentation/glkit/glkskyboxeffect)Added [GLKSkyboxEffect.center](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1488839-center)Added [-[GLKSkyboxEffect draw]](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1488843-draw)Added [GLKSkyboxEffect.label](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1489038-label)Added [-[GLKSkyboxEffect prepareToDraw]](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1488887-preparetodraw)Added [GLKSkyboxEffect.textureCubeMap](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1488873-texturecubemap)Added [GLKSkyboxEffect.transform](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1489015-transform)Added [GLKSkyboxEffect.xSize](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1488891-xsize)Added [GLKSkyboxEffect.ySize](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1489024-ysize)Added [GLKSkyboxEffect.zSize](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1488976-zsize)GLKTextureLoader.hAdded [GLKTextureInfo](https://developer.apple.com/documentation/glkit/glktextureinfo)Added [GLKTextureInfo.alphaState](https://developer.apple.com/documentation/glkit/glktextureinfo/1489050-alphastate)Added [GLKTextureInfo.containsMipmaps](https://developer.apple.com/documentation/glkit/glktextureinfo/1488618-containsmipmaps)Added [GLKTextureInfo.height](https://developer.apple.com/documentation/glkit/glktextureinfo/1488622-height)Added [GLKTextureInfo.name](https://developer.apple.com/documentation/glkit/glktextureinfo/1488763-name)Added [GLKTextureInfo.target](https://developer.apple.com/documentation/glkit/glktextureinfo/1489087-target)Added [GLKTextureInfo.textureOrigin](https://developer.apple.com/documentation/glkit/glktextureinfo/1488624-textureorigin)Added [GLKTextureInfo.width](https://developer.apple.com/documentation/glkit/glktextureinfo/1489126-width)Added [GLKTextureLoader](https://developer.apple.com/documentation/glkit/glktextureloader)Added [+[GLKTextureLoader cubeMapWithContentsOfFile:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488848-cubemap)Added [-[GLKTextureLoader cubeMapWithContentsOfFile:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488617-cubemapwithcontentsoffile)Added [+[GLKTextureLoader cubeMapWithContentsOfFiles:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488810-cubemapwithcontentsoffiles)Added [-[GLKTextureLoader cubeMapWithContentsOfFiles:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488854-cubemapwithcontentsoffiles)Added [+[GLKTextureLoader cubeMapWithContentsOfURL:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488743-cubemap)Added [-[GLKTextureLoader cubeMapWithContentsOfURL:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488926-cubemap)Added [-[GLKTextureLoader initWithSharegroup:]](https://developer.apple.com/documentation/glkit/glktextureloader/1620707-initwithsharegroup)Added [+[GLKTextureLoader textureWithCGImage:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488673-texture)Added [-[GLKTextureLoader textureWithCGImage:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488861-texturewithcgimage)Added [+[GLKTextureLoader textureWithContentsOfData:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1489081-texturewithcontentsofdata)Added [-[GLKTextureLoader textureWithContentsOfData:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488905-texturewithcontentsofdata)Added [+[GLKTextureLoader textureWithContentsOfFile:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488932-texturewithcontentsoffile)Added [-[GLKTextureLoader textureWithContentsOfFile:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1489064-texture)Added [+[GLKTextureLoader textureWithContentsOfURL:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1489025-texturewithcontentsofurl)Added [-[GLKTextureLoader textureWithContentsOfURL:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488621-texturewithcontentsofurl)Added [GLKTextureInfoAlphaState](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate)Added [GLKTextureInfoAlphaStateNonPremultiplied](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate/glktextureinfoalphastatenonpremultiplied)Added [GLKTextureInfoAlphaStateNone](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate/none)Added [GLKTextureInfoAlphaStatePremultiplied](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate/glktextureinfoalphastatepremultiplied)Added [GLKTextureInfoOrigin](https://developer.apple.com/documentation/glkit/glktextureinfoorigin)Added [GLKTextureInfoOriginBottomLeft](https://developer.apple.com/documentation/glkit/glktextureinfoorigin/bottomleft)Added [GLKTextureInfoOriginTopLeft](https://developer.apple.com/documentation/glkit/glktextureinfoorigin/glktextureinfoorigintopleft)Added [GLKTextureInfoOriginUnknown](https://developer.apple.com/documentation/glkit/glktextureinfoorigin/glktextureinfooriginunknown)Added [GLKTextureLoaderApplyPremultiplication](https://developer.apple.com/documentation/glkit/glktextureloaderapplypremultiplication)Added [GLKTextureLoaderCallback](https://developer.apple.com/documentation/glkit/glktextureloadercallback)Added [GLKTextureLoaderError](https://developer.apple.com/documentation/glkit/glktextureloadererror)Added [GLKTextureLoaderErrorAlphaPremultiplicationFailure](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/alphapremultiplicationfailure)Added [GLKTextureLoaderErrorCompressedTextureUpload](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/compressedtextureupload)Added [GLKTextureLoaderErrorCubeMapInvalidNumFiles](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/cubemapinvalidnumfiles)Added [GLKTextureLoaderErrorDataPreprocessingFailure](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrordatapreprocessingfailure)Added [GLKTextureLoaderErrorDomain](https://developer.apple.com/documentation/glkit/glktextureloadererrordomain)Added [GLKTextureLoaderErrorFileOrURLNotFound](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorfileorurlnotfound)Added [GLKTextureLoaderErrorInvalidCGImage](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorinvalidcgimage)Added [GLKTextureLoaderErrorInvalidEAGLContext](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/invalideaglcontext)Added [GLKTextureLoaderErrorInvalidNSData](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/invalidnsdata)Added [GLKTextureLoaderErrorKey](https://developer.apple.com/documentation/glkit/glktextureloadererrorkey)Added [GLKTextureLoaderErrorMipmapUnsupported](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrormipmapunsupported)Added [GLKTextureLoaderErrorPVRAtlasUnsupported](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/pvratlasunsupported)Added [GLKTextureLoaderErrorReorientationFailure](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorreorientationfailure)Added [GLKTextureLoaderErrorUncompressedTextureUpload](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/uncompressedtextureupload)Added [GLKTextureLoaderErrorUnknownFileType](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorunknownfiletype)Added [GLKTextureLoaderErrorUnknownPathType](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/unknownpathtype)Added [GLKTextureLoaderErrorUnsupportedBitDepth](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorunsupportedbitdepth)Added [GLKTextureLoaderErrorUnsupportedCubeMapDimensions](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorunsupportedcubemapdimensions)Added [GLKTextureLoaderErrorUnsupportedOrientation](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/unsupportedorientation)Added [GLKTextureLoaderErrorUnsupportedPVRFormat](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorunsupportedpvrformat)Added [GLKTextureLoaderGLErrorKey](https://developer.apple.com/documentation/glkit/glktextureloaderglerrorkey)Added [GLKTextureLoaderGenerateMipmaps](https://developer.apple.com/documentation/glkit/glktextureloadergeneratemipmaps)Added [GLKTextureLoaderGrayscaleAsAlpha](https://developer.apple.com/documentation/glkit/glktextureloadergrayscaleasalpha)Added [GLKTextureLoaderOriginBottomLeft](https://developer.apple.com/documentation/glkit/glktextureloaderoriginbottomleft)GLKVector2.hAdded [GLKVector2Add()](https://developer.apple.com/documentation/glkit/1391986-glkvector2add)Added [GLKVector2AddScalar()](https://developer.apple.com/documentation/glkit/1391984-glkvector2addscalar)Added [GLKVector2AllEqualToScalar()](https://developer.apple.com/documentation/glkit/1391969-glkvector2allequaltoscalar)Added [GLKVector2AllEqualToVector2()](https://developer.apple.com/documentation/glkit/1392010-glkvector2allequaltovector2)Added [GLKVector2AllGreaterThanOrEqualToScalar()](https://developer.apple.com/documentation/glkit/1391970-glkvector2allgreaterthanorequalt)Added [GLKVector2AllGreaterThanOrEqualToVector2()](https://developer.apple.com/documentation/glkit/1391997-glkvector2allgreaterthanorequalt)Added [GLKVector2AllGreaterThanScalar()](https://developer.apple.com/documentation/glkit/1392006-glkvector2allgreaterthanscalar)Added [GLKVector2AllGreaterThanVector2()](https://developer.apple.com/documentation/glkit/1391972-glkvector2allgreaterthanvector2)Added [GLKVector2Distance()](https://developer.apple.com/documentation/glkit/1391975-glkvector2distance)Added [GLKVector2Divide()](https://developer.apple.com/documentation/glkit/1392004-glkvector2divide)Added [GLKVector2DivideScalar()](https://developer.apple.com/documentation/glkit/1392001-glkvector2dividescalar)Added [GLKVector2DotProduct()](https://developer.apple.com/documentation/glkit/1391988-glkvector2dotproduct)Added [GLKVector2Length()](https://developer.apple.com/documentation/glkit/1391967-glkvector2length)Added [GLKVector2Lerp()](https://developer.apple.com/documentation/glkit/1391973-glkvector2lerp)Added [GLKVector2Make()](https://developer.apple.com/documentation/glkit/1391992-glkvector2make)Added [GLKVector2MakeWithArray()](https://developer.apple.com/documentation/glkit/1391980-glkvector2makewitharray)Added [GLKVector2Maximum()](https://developer.apple.com/documentation/glkit/1392008-glkvector2maximum)Added [GLKVector2Minimum()](https://developer.apple.com/documentation/glkit/1392003-glkvector2minimum)Added [GLKVector2Multiply()](https://developer.apple.com/documentation/glkit/1391993-glkvector2multiply)Added [GLKVector2MultiplyScalar()](https://developer.apple.com/documentation/glkit/1391990-glkvector2multiplyscalar)Added [GLKVector2Negate()](https://developer.apple.com/documentation/glkit/1391999-glkvector2negate)Added [GLKVector2Normalize()](https://developer.apple.com/documentation/glkit/1391976-glkvector2normalize)Added [GLKVector2Project()](https://developer.apple.com/documentation/glkit/1391982-glkvector2project)Added [GLKVector2Subtract()](https://developer.apple.com/documentation/glkit/1391978-glkvector2subtract)Added [GLKVector2SubtractScalar()](https://developer.apple.com/documentation/glkit/1391995-glkvector2subtractscalar)GLKVector3.hAdded [GLKVector3Add()](https://developer.apple.com/documentation/glkit/1393786-glkvector3add)Added [GLKVector3AddScalar()](https://developer.apple.com/documentation/glkit/1393772-glkvector3addscalar)Added [GLKVector3AllEqualToScalar()](https://developer.apple.com/documentation/glkit/1393746-glkvector3allequaltoscalar)Added [GLKVector3AllEqualToVector3()](https://developer.apple.com/documentation/glkit/1393754-glkvector3allequaltovector3)Added [GLKVector3AllGreaterThanOrEqualToScalar()](https://developer.apple.com/documentation/glkit/1393782-glkvector3allgreaterthanorequalt)Added [GLKVector3AllGreaterThanOrEqualToVector3()](https://developer.apple.com/documentation/glkit/1393787-glkvector3allgreaterthanorequalt)Added [GLKVector3AllGreaterThanScalar()](https://developer.apple.com/documentation/glkit/1393768-glkvector3allgreaterthanscalar)Added [GLKVector3AllGreaterThanVector3()](https://developer.apple.com/documentation/glkit/1393762-glkvector3allgreaterthanvector3)Added [GLKVector3CrossProduct()](https://developer.apple.com/documentation/glkit/1393740-glkvector3crossproduct)Added [GLKVector3Distance()](https://developer.apple.com/documentation/glkit/1393770-glkvector3distance)Added [GLKVector3Divide()](https://developer.apple.com/documentation/glkit/1393789-glkvector3divide)Added [GLKVector3DivideScalar()](https://developer.apple.com/documentation/glkit/1393744-glkvector3dividescalar)Added [GLKVector3DotProduct()](https://developer.apple.com/documentation/glkit/1393778-glkvector3dotproduct)Added [GLKVector3Length()](https://developer.apple.com/documentation/glkit/1393750-glkvector3length)Added [GLKVector3Lerp()](https://developer.apple.com/documentation/glkit/1393780-glkvector3lerp)Added [GLKVector3Make()](https://developer.apple.com/documentation/glkit/1393752-glkvector3make)Added [GLKVector3MakeWithArray()](https://developer.apple.com/documentation/glkit/1393760-glkvector3makewitharray)Added [GLKVector3Maximum()](https://developer.apple.com/documentation/glkit/1393748-glkvector3maximum)Added [GLKVector3Minimum()](https://developer.apple.com/documentation/glkit/1393764-glkvector3minimum)Added [GLKVector3Multiply()](https://developer.apple.com/documentation/glkit/1393776-glkvector3multiply)Added [GLKVector3MultiplyScalar()](https://developer.apple.com/documentation/glkit/1393784-glkvector3multiplyscalar)Added [GLKVector3Negate()](https://developer.apple.com/documentation/glkit/1393766-glkvector3negate)Added [GLKVector3Normalize()](https://developer.apple.com/documentation/glkit/1393756-glkvector3normalize)Added [GLKVector3Project()](https://developer.apple.com/documentation/glkit/1393742-glkvector3project)Added [GLKVector3Subtract()](https://developer.apple.com/documentation/glkit/1393774-glkvector3subtract)Added [GLKVector3SubtractScalar()](https://developer.apple.com/documentation/glkit/1393758-glkvector3subtractscalar)GLKVector4.hAdded [GLKVector4Add()](https://developer.apple.com/documentation/glkit/1403359-glkvector4add)Added [GLKVector4AddScalar()](https://developer.apple.com/documentation/glkit/1403347-glkvector4addscalar)Added [GLKVector4AllEqualToScalar()](https://developer.apple.com/documentation/glkit/1403374-glkvector4allequaltoscalar)Added [GLKVector4AllEqualToVector4()](https://developer.apple.com/documentation/glkit/1403350-glkvector4allequaltovector4)Added [GLKVector4AllGreaterThanOrEqualToScalar()](https://developer.apple.com/documentation/glkit/1403378-glkvector4allgreaterthanorequalt)Added [GLKVector4AllGreaterThanOrEqualToVector4()](https://developer.apple.com/documentation/glkit/1403365-glkvector4allgreaterthanorequalt)Added [GLKVector4AllGreaterThanScalar()](https://developer.apple.com/documentation/glkit/1403366-glkvector4allgreaterthanscalar)Added [GLKVector4AllGreaterThanVector4()](https://developer.apple.com/documentation/glkit/1403363-glkvector4allgreaterthanvector4)Added [GLKVector4CrossProduct()](https://developer.apple.com/documentation/glkit/1403335-glkvector4crossproduct)Added [GLKVector4Distance()](https://developer.apple.com/documentation/glkit/1403356-glkvector4distance)Added [GLKVector4Divide()](https://developer.apple.com/documentation/glkit/1403341-glkvector4divide)Added [GLKVector4DivideScalar()](https://developer.apple.com/documentation/glkit/1403370-glkvector4dividescalar)Added [GLKVector4DotProduct()](https://developer.apple.com/documentation/glkit/1403354-glkvector4dotproduct)Added [GLKVector4Length()](https://developer.apple.com/documentation/glkit/1403343-glkvector4length)Added [GLKVector4Lerp()](https://developer.apple.com/documentation/glkit/1403348-glkvector4lerp)Added [GLKVector4Make()](https://developer.apple.com/documentation/glkit/1403372-glkvector4make)Added [GLKVector4MakeWithArray()](https://developer.apple.com/documentation/glkit/1403358-glkvector4makewitharray)Added [GLKVector4MakeWithVector3()](https://developer.apple.com/documentation/glkit/1403332-glkvector4makewithvector3)Added [GLKVector4Maximum()](https://developer.apple.com/documentation/glkit/1403361-glkvector4maximum)Added [GLKVector4Minimum()](https://developer.apple.com/documentation/glkit/1403337-glkvector4minimum)Added [GLKVector4Multiply()](https://developer.apple.com/documentation/glkit/1403368-glkvector4multiply)Added [GLKVector4MultiplyScalar()](https://developer.apple.com/documentation/glkit/1403339-glkvector4multiplyscalar)Added [GLKVector4Negate()](https://developer.apple.com/documentation/glkit/1403331-glkvector4negate)Added [GLKVector4Normalize()](https://developer.apple.com/documentation/glkit/1403352-glkvector4normalize)Added [GLKVector4Project()](https://developer.apple.com/documentation/glkit/1403345-glkvector4project)Added [GLKVector4Subtract()](https://developer.apple.com/documentation/glkit/1403333-glkvector4subtract)Added [GLKVector4SubtractScalar()](https://developer.apple.com/documentation/glkit/1403376-glkvector4subtractscalar)GLKView.hAdded [GLKView](https://developer.apple.com/documentation/glkit/glkview)Added [-[GLKView bindDrawable]](https://developer.apple.com/documentation/glkit/glkview/1615593-binddrawable)Added [GLKView.context](https://developer.apple.com/documentation/glkit/glkview/1615597-context)Added [GLKView.delegate](https://developer.apple.com/documentation/glkit/glkview/1615557-delegate)Added [-[GLKView deleteDrawable]](https://developer.apple.com/documentation/glkit/glkview/1615569-deletedrawable)Added [-[GLKView display]](https://developer.apple.com/documentation/glkit/glkview/1615571-display)Added [GLKView.drawableColorFormat](https://developer.apple.com/documentation/glkit/glkview/1615587-drawablecolorformat)Added [GLKView.drawableDepthFormat](https://developer.apple.com/documentation/glkit/glkview/1615583-drawabledepthformat)Added [GLKView.drawableHeight](https://developer.apple.com/documentation/glkit/glkview/1615559-drawableheight)Added [GLKView.drawableMultisample](https://developer.apple.com/documentation/glkit/glkview/1615601-drawablemultisample)Added [GLKView.drawableStencilFormat](https://developer.apple.com/documentation/glkit/glkview/1615605-drawablestencilformat)Added [GLKView.drawableWidth](https://developer.apple.com/documentation/glkit/glkview/1615591-drawablewidth)Added [GLKView.enableSetNeedsDisplay](https://developer.apple.com/documentation/glkit/glkview/1615561-enablesetneedsdisplay)Added [-[GLKView initWithFrame:context:]](https://developer.apple.com/documentation/glkit/glkview/1615609-initwithframe)Added [-[GLKView snapshot]](https://developer.apple.com/documentation/glkit/glkview/1615562-snapshot)Added [GLKViewDelegate](https://developer.apple.com/documentation/glkit/glkviewdelegate)Added [-[GLKViewDelegate glkView:drawInRect:]](https://developer.apple.com/documentation/glkit/glkviewdelegate/1615595-glkview)Added [GLKViewDrawableColorFormat](https://developer.apple.com/documentation/glkit/glkviewdrawablecolorformat)Added [GLKViewDrawableColorFormatRGB565](https://developer.apple.com/documentation/glkit/glkviewdrawablecolorformat/rgb565)Added [GLKViewDrawableColorFormatRGBA8888](https://developer.apple.com/documentation/glkit/glkviewdrawablecolorformat/glkviewdrawablecolorformatrgba8888)Added [GLKViewDrawableDepthFormat](https://developer.apple.com/documentation/glkit/glkviewdrawabledepthformat)Added [GLKViewDrawableDepthFormat16](https://developer.apple.com/documentation/glkit/glkviewdrawabledepthformat/glkviewdrawabledepthformat16)Added [GLKViewDrawableDepthFormat24](https://developer.apple.com/documentation/glkit/glkviewdrawabledepthformat/glkviewdrawabledepthformat24)Added [GLKViewDrawableDepthFormatNone](https://developer.apple.com/documentation/glkit/glkviewdrawabledepthformat/formatnone)Added [GLKViewDrawableMultisample](https://developer.apple.com/documentation/glkit/glkviewdrawablemultisample)Added [GLKViewDrawableMultisample4X](https://developer.apple.com/documentation/glkit/glkviewdrawablemultisample/multisample4x)Added [GLKViewDrawableMultisampleNone](https://developer.apple.com/documentation/glkit/glkviewdrawablemultisample/multisamplenone)Added [GLKViewDrawableStencilFormat](https://developer.apple.com/documentation/glkit/glkviewdrawablestencilformat)Added [GLKViewDrawableStencilFormat8](https://developer.apple.com/documentation/glkit/glkviewdrawablestencilformat/glkviewdrawablestencilformat8)Added [GLKViewDrawableStencilFormatNone](https://developer.apple.com/documentation/glkit/glkviewdrawablestencilformat/glkviewdrawablestencilformatnone)GLKViewController.hAdded [GLKViewController](https://developer.apple.com/documentation/glkit/glkviewcontroller)Added [GLKViewController.delegate](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620711-delegate)Added [GLKViewController.framesDisplayed](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620790-framesdisplayed)Added [GLKViewController.framesPerSecond](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620723-framespersecond)Added [GLKViewController.pauseOnWillResignActive](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620699-pauseonwillresignactive)Added [GLKViewController.paused](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620712-ispaused)Added [GLKViewController.preferredFramesPerSecond](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620702-preferredframespersecond)Added [GLKViewController.resumeOnDidBecomeActive](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620734-resumeondidbecomeactive)Added [GLKViewController.timeSinceFirstResume](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620709-timesincefirstresume)Added [GLKViewController.timeSinceLastDraw](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620725-timesincelastdraw)Added [GLKViewController.timeSinceLastResume](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620706-timesincelastresume)Added [GLKViewController.timeSinceLastUpdate](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620726-timesincelastupdate)Added [GLKViewControllerDelegate](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate)Added [-[GLKViewControllerDelegate glkViewController:willPause:]](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate/1620776-glkviewcontroller)Added [-[GLKViewControllerDelegate glkViewControllerUpdate:]](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate/1620710-glkviewcontrollerupdate)

## GSS

gssapi.hAdded #def GSSAPI_CPP_ENDAdded #def GSSAPI_CPP_STARTAdded #def GSSAPI_DEPRECATEDAdded #def GSSAPI_LIB_CALLAdded #def GSSAPI_LIB_FUNCTIONAdded #def GSSAPI_LIB_VARIABLEAdded #def GSS_CALLING_ERRORAdded [#def GSS_C_ACCEPT](https://developer.apple.com/documentation/gss/gss_c_accept)Added [#def GSS_C_AF_APPLETALK](https://developer.apple.com/documentation/gss/gss_c_af_appletalk)Added [#def GSS_C_AF_BSC](https://developer.apple.com/documentation/gss/gss_c_af_bsc)Added [#def GSS_C_AF_CCITT](https://developer.apple.com/documentation/gss/gss_c_af_ccitt)Added [#def GSS_C_AF_CHAOS](https://developer.apple.com/documentation/gss/gss_c_af_chaos)Added [#def GSS_C_AF_DATAKIT](https://developer.apple.com/documentation/gss/gss_c_af_datakit)Added [#def GSS_C_AF_DECnet](https://developer.apple.com/documentation/gss/gss_c_af_decnet)Added [#def GSS_C_AF_DLI](https://developer.apple.com/documentation/gss/gss_c_af_dli)Added [#def GSS_C_AF_DSS](https://developer.apple.com/documentation/gss/gss_c_af_dss)Added [#def GSS_C_AF_ECMA](https://developer.apple.com/documentation/gss/gss_c_af_ecma)Added [#def GSS_C_AF_HYLINK](https://developer.apple.com/documentation/gss/gss_c_af_hylink)Added [#def GSS_C_AF_IMPLINK](https://developer.apple.com/documentation/gss/gss_c_af_implink)Added [#def GSS_C_AF_INET](https://developer.apple.com/documentation/gss/gss_c_af_inet)Added [#def GSS_C_AF_INET6](https://developer.apple.com/documentation/gss/gss_c_af_inet6)Added [#def GSS_C_AF_LAT](https://developer.apple.com/documentation/gss/gss_c_af_lat)Added [#def GSS_C_AF_LOCAL](https://developer.apple.com/documentation/gss/gss_c_af_local)Added [#def GSS_C_AF_NBS](https://developer.apple.com/documentation/gss/gss_c_af_nbs)Added [#def GSS_C_AF_NS](https://developer.apple.com/documentation/gss/gss_c_af_ns)Added [#def GSS_C_AF_NULLADDR](https://developer.apple.com/documentation/gss/gss_c_af_nulladdr)Added [#def GSS_C_AF_OSI](https://developer.apple.com/documentation/gss/gss_c_af_osi)Added [#def GSS_C_AF_PUP](https://developer.apple.com/documentation/gss/gss_c_af_pup)Added [#def GSS_C_AF_SNA](https://developer.apple.com/documentation/gss/gss_c_af_sna)Added [#def GSS_C_AF_UNSPEC](https://developer.apple.com/documentation/gss/gss_c_af_unspec)Added [#def GSS_C_AF_X25](https://developer.apple.com/documentation/gss/gss_c_af_x25)Added [#def GSS_C_ANON_FLAG](https://developer.apple.com/documentation/gss/gss_c_anon_flag)Added [#def GSS_C_BOTH](https://developer.apple.com/documentation/gss/gss_c_both)Added [#def GSS_C_CALLING_ERROR_MASK](https://developer.apple.com/documentation/gss/gss_c_calling_error_mask)Added [#def GSS_C_CALLING_ERROR_OFFSET](https://developer.apple.com/documentation/gss/gss_c_calling_error_offset)Added [#def GSS_C_CONF_FLAG](https://developer.apple.com/documentation/gss/gss_c_conf_flag)Added [#def GSS_C_CRED_NO_UI](https://developer.apple.com/documentation/gss/gss_c_cred_no_ui)Added [#def GSS_C_DCE_STYLE](https://developer.apple.com/documentation/gss/gss_c_dce_style)Added [#def GSS_C_DELEG_FLAG](https://developer.apple.com/documentation/gss/gss_c_deleg_flag)Added [#def GSS_C_DELEG_POLICY_FLAG](https://developer.apple.com/documentation/gss/gss_c_deleg_policy_flag)Added #def GSS_C_EMPTY_BUFFERAdded [#def GSS_C_EXTENDED_ERROR_FLAG](https://developer.apple.com/documentation/gss/gss_c_extended_error_flag)Added [#def GSS_C_GSS_CODE](https://developer.apple.com/documentation/gss/gss_c_gss_code)Added [#def GSS_C_IDENTIFY_FLAG](https://developer.apple.com/documentation/gss/gss_c_identify_flag)Added [#def GSS_C_INDEFINITE](https://developer.apple.com/documentation/gss/gss_c_indefinite)Added [#def GSS_C_INITIATE](https://developer.apple.com/documentation/gss/gss_c_initiate)Added #def GSS_C_INQ_SSPI_SESSION_KEYAdded #def GSS_C_INQ_WIN2K_PAC_XAdded [#def GSS_C_INTEG_FLAG](https://developer.apple.com/documentation/gss/gss_c_integ_flag)Added [#def GSS_C_MECH_CODE](https://developer.apple.com/documentation/gss/gss_c_mech_code)Added [#def GSS_C_MUTUAL_FLAG](https://developer.apple.com/documentation/gss/gss_c_mutual_flag)Added [#def GSS_C_NO_BUFFER](https://developer.apple.com/documentation/gss/gss_c_no_buffer)Added [#def GSS_C_NO_BUFFER_SET](https://developer.apple.com/documentation/gss/gss_c_no_buffer_set)Added [#def GSS_C_NO_CHANNEL_BINDINGS](https://developer.apple.com/documentation/gss/gss_c_no_channel_bindings)Added [#def GSS_C_NO_CONTEXT](https://developer.apple.com/documentation/gss/gss_c_no_context)Added [#def GSS_C_NO_CREDENTIAL](https://developer.apple.com/documentation/gss/gss_c_no_credential)Added [#def GSS_C_NO_IOV_BUFFER](https://developer.apple.com/documentation/gss/gss_c_no_iov_buffer)Added [#def GSS_C_NO_NAME](https://developer.apple.com/documentation/gss/gss_c_no_name)Added [#def GSS_C_NO_OID](https://developer.apple.com/documentation/gss/gss_c_no_oid)Added [#def GSS_C_NO_OID_SET](https://developer.apple.com/documentation/gss/gss_c_no_oid_set)Added #def GSS_C_NT_ANONYMOUSAdded #def GSS_C_NT_DNAdded #def GSS_C_NT_EXPORT_NAMEAdded #def GSS_C_NT_HOSTBASED_SERVICEAdded #def GSS_C_NT_HOSTBASED_SERVICE_XAdded #def GSS_C_NT_MACHINE_UID_NAMEAdded #def GSS_C_NT_STRING_UID_NAMEAdded #def GSS_C_NT_USER_NAMEAdded [#def GSS_C_NULL_OID](https://developer.apple.com/documentation/gss/gss_c_null_oid)Added [#def GSS_C_NULL_OID_SET](https://developer.apple.com/documentation/gss/gss_c_null_oid_set)Added [#def GSS_C_OPTION_MASK](https://developer.apple.com/documentation/gss/gss_c_option_mask)Added [#def GSS_C_PRF_KEY_FULL](https://developer.apple.com/documentation/gss/gss_c_prf_key_full)Added [#def GSS_C_PRF_KEY_PARTIAL](https://developer.apple.com/documentation/gss/gss_c_prf_key_partial)Added [#def GSS_C_PROT_READY_FLAG](https://developer.apple.com/documentation/gss/gss_c_prot_ready_flag)Added [#def GSS_C_QOP_DEFAULT](https://developer.apple.com/documentation/gss/gss_c_qop_default)Added [#def GSS_C_REPLAY_FLAG](https://developer.apple.com/documentation/gss/gss_c_replay_flag)Added [#def GSS_C_ROUTINE_ERROR_MASK](https://developer.apple.com/documentation/gss/gss_c_routine_error_mask)Added [#def GSS_C_ROUTINE_ERROR_OFFSET](https://developer.apple.com/documentation/gss/gss_c_routine_error_offset)Added [#def GSS_C_SEQUENCE_FLAG](https://developer.apple.com/documentation/gss/gss_c_sequence_flag)Added [#def GSS_C_SUPPLEMENTARY_MASK](https://developer.apple.com/documentation/gss/gss_c_supplementary_mask)Added [#def GSS_C_SUPPLEMENTARY_OFFSET](https://developer.apple.com/documentation/gss/gss_c_supplementary_offset)Added [#def GSS_C_TRANS_FLAG](https://developer.apple.com/documentation/gss/gss_c_trans_flag)Added #def GSS_ERRORAdded #def GSS_IOV_BUFFER_FLAGSAdded #def GSS_IOV_BUFFER_TYPEAdded [#def GSS_IOV_BUFFER_TYPE_DATA](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_data)Added [#def GSS_IOV_BUFFER_TYPE_EMPTY](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_empty)Added [#def GSS_IOV_BUFFER_TYPE_FLAG_ALLOCATE](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_flag_allocate)Added [#def GSS_IOV_BUFFER_TYPE_FLAG_ALLOCATED](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_flag_allocated)Added [#def GSS_IOV_BUFFER_TYPE_FLAG_MASK](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_flag_mask)Added [#def GSS_IOV_BUFFER_TYPE_HEADER](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_header)Added [#def GSS_IOV_BUFFER_TYPE_MECH_PARAMS](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_mech_params)Added [#def GSS_IOV_BUFFER_TYPE_PADDING](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_padding)Added [#def GSS_IOV_BUFFER_TYPE_SIGN_ONLY](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_sign_only)Added [#def GSS_IOV_BUFFER_TYPE_STREAM](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_stream)Added [#def GSS_IOV_BUFFER_TYPE_TRAILER](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_trailer)Added [#def GSS_KRB5_CONF_C_QOP_DES](https://developer.apple.com/documentation/gss/gss_krb5_conf_c_qop_des)Added [#def GSS_KRB5_CONF_C_QOP_DES3_KD](https://developer.apple.com/documentation/gss/gss_krb5_conf_c_qop_des3_kd)Added #def GSS_ROUTINE_ERRORAdded #def GSS_SASL_DIGEST_MD5_MECHANISMAdded #def GSS_SUPPLEMENTARY_INFOAdded [#def GSS_S_BAD_BINDINGS](https://developer.apple.com/documentation/gss/gss_s_bad_bindings)Added [#def GSS_S_BAD_MECH](https://developer.apple.com/documentation/gss/gss_s_bad_mech)Added [#def GSS_S_BAD_MIC](https://developer.apple.com/documentation/gss/gss_s_bad_mic)Added [#def GSS_S_BAD_NAME](https://developer.apple.com/documentation/gss/gss_s_bad_name)Added [#def GSS_S_BAD_NAMETYPE](https://developer.apple.com/documentation/gss/gss_s_bad_nametype)Added [#def GSS_S_BAD_QOP](https://developer.apple.com/documentation/gss/gss_s_bad_qop)Added [#def GSS_S_BAD_SIG](https://developer.apple.com/documentation/gss/gss_s_bad_sig)Added [#def GSS_S_BAD_STATUS](https://developer.apple.com/documentation/gss/gss_s_bad_status)Added [#def GSS_S_CALL_BAD_STRUCTURE](https://developer.apple.com/documentation/gss/gss_s_call_bad_structure)Added [#def GSS_S_CALL_INACCESSIBLE_READ](https://developer.apple.com/documentation/gss/gss_s_call_inaccessible_read)Added [#def GSS_S_CALL_INACCESSIBLE_WRITE](https://developer.apple.com/documentation/gss/gss_s_call_inaccessible_write)Added [#def GSS_S_COMPLETE](https://developer.apple.com/documentation/gss/gss_s_complete)Added [#def GSS_S_CONTEXT_EXPIRED](https://developer.apple.com/documentation/gss/gss_s_context_expired)Added #def GSS_S_CONTINUE_NEEDEDAdded [#def GSS_S_CREDENTIALS_EXPIRED](https://developer.apple.com/documentation/gss/gss_s_credentials_expired)Added [#def GSS_S_DEFECTIVE_CREDENTIAL](https://developer.apple.com/documentation/gss/gss_s_defective_credential)Added [#def GSS_S_DEFECTIVE_TOKEN](https://developer.apple.com/documentation/gss/gss_s_defective_token)Added [#def GSS_S_DUPLICATE_ELEMENT](https://developer.apple.com/documentation/gss/gss_s_duplicate_element)Added #def GSS_S_DUPLICATE_TOKENAdded [#def GSS_S_FAILURE](https://developer.apple.com/documentation/gss/gss_s_failure)Added #def GSS_S_GAP_TOKENAdded [#def GSS_S_NAME_NOT_MN](https://developer.apple.com/documentation/gss/gss_s_name_not_mn)Added [#def GSS_S_NO_CONTEXT](https://developer.apple.com/documentation/gss/gss_s_no_context)Added [#def GSS_S_NO_CRED](https://developer.apple.com/documentation/gss/gss_s_no_cred)Added #def GSS_S_OLD_TOKENAdded [#def GSS_S_UNAUTHORIZED](https://developer.apple.com/documentation/gss/gss_s_unauthorized)Added [#def GSS_S_UNAVAILABLE](https://developer.apple.com/documentation/gss/gss_s_unavailable)Added #def GSS_S_UNSEQ_TOKENAdded [OM_uint32](https://developer.apple.com/documentation/gss/om_uint32)Added [OM_uint64](https://developer.apple.com/documentation/gss/om_uint64)Added [gss_OID](https://developer.apple.com/documentation/gss/gss_oid)Added [gss_OID_desc](https://developer.apple.com/documentation/gss/gss_oid_desc)Added [gss_OID_set](https://developer.apple.com/documentation/gss/gss_oid_set)Added [gss_OID_set_desc](https://developer.apple.com/documentation/gss/gss_oid_set_desc)Added [gss_aapl_initial_cred()](https://developer.apple.com/documentation/gss/1411909-gss_aapl_initial_cred)Added [gss_accept_sec_context()](https://developer.apple.com/documentation/gss/1438493-gss_accept_sec_context)Added [gss_acquire_cred()](https://developer.apple.com/documentation/gss/1438466-gss_acquire_cred)Added [gss_add_buffer_set_member()](https://developer.apple.com/documentation/gss/1438479-gss_add_buffer_set_member)Added [gss_add_cred()](https://developer.apple.com/documentation/gss/1438473-gss_add_cred)Added [gss_add_oid_set_member()](https://developer.apple.com/documentation/gss/1438411-gss_add_oid_set_member)Added [gss_auth_identity_t](https://developer.apple.com/documentation/gss/gss_auth_identity_t)Added [gss_buffer_desc](https://developer.apple.com/documentation/gss/gss_buffer_desc)Added [gss_buffer_set_desc](https://developer.apple.com/documentation/gss/gss_buffer_set_desc)Added [gss_buffer_set_t](https://developer.apple.com/documentation/gss/gss_buffer_set_t)Added [gss_buffer_t](https://developer.apple.com/documentation/gss/gss_buffer_t)Added [gss_canonicalize_name()](https://developer.apple.com/documentation/gss/1438494-gss_canonicalize_name)Added gss_channel_bindings_structAdded [gss_channel_bindings_t](https://developer.apple.com/documentation/gss/gss_channel_bindings_t)Added [gss_compare_name()](https://developer.apple.com/documentation/gss/1438437-gss_compare_name)Added [gss_context_time()](https://developer.apple.com/documentation/gss/1438487-gss_context_time)Added [gss_create_empty_buffer_set()](https://developer.apple.com/documentation/gss/1438537-gss_create_empty_buffer_set)Added [gss_create_empty_oid_set()](https://developer.apple.com/documentation/gss/1438489-gss_create_empty_oid_set)Added [gss_cred_id_t](https://developer.apple.com/documentation/gss/gss_cred_id_t)Added [gss_cred_usage_t](https://developer.apple.com/documentation/gss/gss_cred_usage_t)Added [gss_ctx_id_t](https://developer.apple.com/documentation/gss/gss_ctx_id_t)Added [gss_delete_sec_context()](https://developer.apple.com/documentation/gss/1438435-gss_delete_sec_context)Added [gss_destroy_cred()](https://developer.apple.com/documentation/gss/1438521-gss_destroy_cred)Added [gss_display_name()](https://developer.apple.com/documentation/gss/1438464-gss_display_name)Added [gss_display_status()](https://developer.apple.com/documentation/gss/1438535-gss_display_status)Added [gss_duplicate_name()](https://developer.apple.com/documentation/gss/1438418-gss_duplicate_name)Added [gss_duplicate_oid()](https://developer.apple.com/documentation/gss/1438533-gss_duplicate_oid)Added [gss_export_name()](https://developer.apple.com/documentation/gss/1438477-gss_export_name)Added [gss_export_sec_context()](https://developer.apple.com/documentation/gss/1438449-gss_export_sec_context)Added [gss_get_mic()](https://developer.apple.com/documentation/gss/1438530-gss_get_mic)Added [gss_import_name()](https://developer.apple.com/documentation/gss/1438453-gss_import_name)Added [gss_import_sec_context()](https://developer.apple.com/documentation/gss/1438484-gss_import_sec_context)Added [gss_indicate_mechs()](https://developer.apple.com/documentation/gss/1438424-gss_indicate_mechs)Added [gss_init_sec_context()](https://developer.apple.com/documentation/gss/1438476-gss_init_sec_context)Added [gss_inquire_context()](https://developer.apple.com/documentation/gss/1438458-gss_inquire_context)Added [gss_inquire_cred()](https://developer.apple.com/documentation/gss/1438531-gss_inquire_cred)Added [gss_inquire_cred_by_mech()](https://developer.apple.com/documentation/gss/1438518-gss_inquire_cred_by_mech)Added [gss_inquire_cred_by_oid()](https://developer.apple.com/documentation/gss/1438504-gss_inquire_cred_by_oid)Added [gss_inquire_mechs_for_name()](https://developer.apple.com/documentation/gss/1438481-gss_inquire_mechs_for_name)Added [gss_inquire_names_for_mech()](https://developer.apple.com/documentation/gss/1438523-gss_inquire_names_for_mech)Added [gss_inquire_sec_context_by_oid()](https://developer.apple.com/documentation/gss/1438525-gss_inquire_sec_context_by_oid)Added [gss_iov_buffer_desc](https://developer.apple.com/documentation/gss/gss_iov_buffer_desc)Added [gss_iov_buffer_t](https://developer.apple.com/documentation/gss/gss_iov_buffer_t)Added [gss_iter_creds()](https://developer.apple.com/documentation/gss/1438515-gss_iter_creds)Added [gss_iter_creds_f()](https://developer.apple.com/documentation/gss/1438438-gss_iter_creds_f)Added [gss_name_t](https://developer.apple.com/documentation/gss/gss_name_t)Added [gss_oid_equal()](https://developer.apple.com/documentation/gss/1438498-gss_oid_equal)Added [gss_oid_to_str()](https://developer.apple.com/documentation/gss/1438512-gss_oid_to_str)Added [gss_process_context_token()](https://developer.apple.com/documentation/gss/1438516-gss_process_context_token)Added [gss_pseudo_random()](https://developer.apple.com/documentation/gss/1438496-gss_pseudo_random)Added [gss_qop_t](https://developer.apple.com/documentation/gss/gss_qop_t)Added [gss_release_buffer()](https://developer.apple.com/documentation/gss/1438486-gss_release_buffer)Added [gss_release_buffer_set()](https://developer.apple.com/documentation/gss/1438428-gss_release_buffer_set)Added [gss_release_cred()](https://developer.apple.com/documentation/gss/1438461-gss_release_cred)Added [gss_release_name()](https://developer.apple.com/documentation/gss/1438451-gss_release_name)Added [gss_release_oid()](https://developer.apple.com/documentation/gss/1438455-gss_release_oid)Added [gss_release_oid_set()](https://developer.apple.com/documentation/gss/1438480-gss_release_oid_set)Added [gss_seal()](https://developer.apple.com/documentation/gss/1438459-gss_seal)Added [gss_set_cred_option()](https://developer.apple.com/documentation/gss/1438513-gss_set_cred_option)Added [gss_set_sec_context_option()](https://developer.apple.com/documentation/gss/1438491-gss_set_sec_context_option)Added [gss_sign()](https://developer.apple.com/documentation/gss/1438416-gss_sign)Added [gss_status_id_t](https://developer.apple.com/documentation/gss/gss_status_id_t)Added gss_store_cred()Added [gss_test_oid_set_member()](https://developer.apple.com/documentation/gss/1438442-gss_test_oid_set_member)Added [gss_uint32](https://developer.apple.com/documentation/gss/gss_uint32)Added [gss_unseal()](https://developer.apple.com/documentation/gss/1438456-gss_unseal)Added [gss_unwrap()](https://developer.apple.com/documentation/gss/1438520-gss_unwrap)Added [gss_verify()](https://developer.apple.com/documentation/gss/1438414-gss_verify)Added [gss_verify_mic()](https://developer.apple.com/documentation/gss/1438447-gss_verify_mic)Added [gss_wrap()](https://developer.apple.com/documentation/gss/1438527-gss_wrap)Added [gss_wrap_size_limit()](https://developer.apple.com/documentation/gss/1438419-gss_wrap_size_limit)Added [#def kGSSCredentialUsage](https://developer.apple.com/documentation/gss/kgsscredentialusage)Added [#def kGSSICCertificate](https://developer.apple.com/documentation/gss/kgssiccertificate)Added [#def kGSSICPassword](https://developer.apple.com/documentation/gss/kgssicpassword)Added [#def kGSS_C_ACCEPT](https://developer.apple.com/documentation/gss/kgss_c_accept)Added [#def kGSS_C_BOTH](https://developer.apple.com/documentation/gss/kgss_c_both)Added [#def kGSS_C_INITIATE](https://developer.apple.com/documentation/gss/kgss_c_initiate)gssapi_krb5.hAdded #def GSSKRB5_FUNCTION_DEPRECATEDAdded #def GSS_C_PEER_HAS_UPDATED_SPNEGOAdded #def GSS_IAKERB_MECHANISMAdded #def GSS_KRB5_CCACHE_NAME_XAdded #def GSS_KRB5_COMPAT_DES3_MIC_XAdded #def GSS_KRB5_COPY_CCACHE_XAdded #def GSS_KRB5_CRED_NO_CI_FLAGS_XAdded #def GSS_KRB5_EXPORT_LUCID_CONTEXT_V1_XAdded #def GSS_KRB5_EXPORT_LUCID_CONTEXT_XAdded #def GSS_KRB5_EXTRACT_AUTHZ_DATA_FROM_SEC_CONTEXT_XAdded #def GSS_KRB5_GET_ACCEPTOR_SUBKEY_XAdded #def GSS_KRB5_GET_AUTHTIME_XAdded #def GSS_KRB5_GET_INITIATOR_SUBKEY_XAdded #def GSS_KRB5_GET_SERVICE_KEYBLOCK_XAdded #def GSS_KRB5_GET_SUBKEY_XAdded #def GSS_KRB5_GET_TIME_OFFSET_XAdded #def GSS_KRB5_GET_TKT_FLAGS_XAdded #def GSS_KRB5_IMPORT_CRED_XAdded #def GSS_KRB5_MECHANISMAdded #def GSS_KRB5_NT_MACHINE_UID_NAMEAdded #def GSS_KRB5_NT_PRINCIPALAdded #def GSS_KRB5_NT_PRINCIPAL_NAMEAdded #def GSS_KRB5_NT_PRINCIPAL_NAME_REFERRALAdded #def GSS_KRB5_NT_STRING_UID_NAMEAdded #def GSS_KRB5_NT_USER_NAMEAdded #def GSS_KRB5_PLUGIN_REGISTER_XAdded #def GSS_KRB5_REGISTER_ACCEPTOR_IDENTITY_XAdded #def GSS_KRB5_SEND_TO_KDC_XAdded #def GSS_KRB5_SET_ALLOWABLE_ENCTYPES_XAdded #def GSS_KRB5_SET_DEFAULT_REALM_XAdded #def GSS_KRB5_SET_DNS_CANONICALIZE_XAdded #def GSS_KRB5_SET_TIME_OFFSET_XAdded #def GSS_PKU2U_MECHANISMAdded [gss_krb5_ccache_name()](https://developer.apple.com/documentation/gss/1438472-gss_krb5_ccache_name)Added [gss_krb5_cfx_keydata_t](https://developer.apple.com/documentation/gss/gss_krb5_cfx_keydata_t)Added [gss_krb5_copy_ccache()](https://developer.apple.com/documentation/gss/1438508-gss_krb5_copy_ccache)Added [gss_krb5_export_lucid_sec_context()](https://developer.apple.com/documentation/gss/1438433-gss_krb5_export_lucid_sec_contex)Added [gss_krb5_free_lucid_sec_context()](https://developer.apple.com/documentation/gss/1438483-gss_krb5_free_lucid_sec_context)Added [gss_krb5_lucid_context_v1_t](https://developer.apple.com/documentation/gss/gss_krb5_lucid_context_v1_t)Added [gss_krb5_lucid_context_version_t](https://developer.apple.com/documentation/gss/gss_krb5_lucid_context_version_t)Added [gss_krb5_lucid_key_t](https://developer.apple.com/documentation/gss/gss_krb5_lucid_key_t)Added #def gss_krb5_nt_general_nameAdded [gss_krb5_rfc1964_keydata_t](https://developer.apple.com/documentation/gss/gss_krb5_rfc1964_keydata_t)Added [gss_krb5_set_allowable_enctypes()](https://developer.apple.com/documentation/gss/1438431-gss_krb5_set_allowable_enctypes)Added #def gss_mech_krb5Added [gsskrb5_extract_authz_data_from_sec_context()](https://developer.apple.com/documentation/gss/1438468-gsskrb5_extract_authz_data_from_)Added [gsskrb5_register_acceptor_identity()](https://developer.apple.com/documentation/gss/1438421-gsskrb5_register_acceptor_identi)Added [krb5_gss_register_acceptor_identity()](https://developer.apple.com/documentation/gss/1438470-krb5_gss_register_acceptor_ident)gssapi_spnego.hAdded #def GSS_SPNEGO_MECHANISMAdded #def gss_mech_spnego

## iAd

ADBannerView.hAdded [-[ADBannerViewDelegate bannerViewWillLoadAd:]](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614636-bannerviewwillloadad)ADInterstitialAd.hAdded [-[ADInterstitialAdDelegate interstitialAdWillLoad:]](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614688-interstitialadwillload)

## ImageIO

CGImageProperties.hAdded [kCGImagePropertyPNGAuthor](https://developer.apple.com/documentation/imageio/kcgimagepropertypngauthor)Added [kCGImagePropertyPNGCopyright](https://developer.apple.com/documentation/imageio/kcgimagepropertypngcopyright)Added [kCGImagePropertyPNGCreationTime](https://developer.apple.com/documentation/imageio/kcgimagepropertypngcreationtime)Added [kCGImagePropertyPNGDescription](https://developer.apple.com/documentation/imageio/kcgimagepropertypngdescription)Added [kCGImagePropertyPNGModificationTime](https://developer.apple.com/documentation/imageio/kcgimagepropertypngmodificationtime)Added [kCGImagePropertyPNGSoftware](https://developer.apple.com/documentation/imageio/kcgimagepropertypngsoftware)Added [kCGImagePropertyPNGTitle](https://developer.apple.com/documentation/imageio/kcgimagepropertypngtitle)

## MapKit

MKAnnotation.hRemoved [-[MKAnnotation subtitle]](https://developer.apple.com/documentation/mapkit/mkannotation/1429520-subtitle)Removed [-[MKAnnotation title]](https://developer.apple.com/documentation/mapkit/mkannotation/1429522-title)Added [MKAnnotation.subtitle](https://developer.apple.com/documentation/mapkit/mkannotation/1429520-subtitle)Added [MKAnnotation.title](https://developer.apple.com/documentation/mapkit/mkannotation/1429522-title)MKFoundation.hAdded #def MK_CLASS_AVAILABLEAdded #def MK_CLASS_DEPRECATEDAdded #def MK_EXTERNMKMapView.hAdded [-[MKMapView setUserTrackingMode:animated:]](https://developer.apple.com/documentation/mapkit/mkmapview/1616205-setusertrackingmode)Added [MKMapView.userTrackingMode](https://developer.apple.com/documentation/mapkit/mkmapview/1616208-usertrackingmode)Added [-[MKMapViewDelegate mapView:didChangeUserTrackingMode:animated:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1616202-mapview)Added [MKUserTrackingMode](https://developer.apple.com/documentation/mapkit/mkusertrackingmode)Added [MKUserTrackingModeFollow](https://developer.apple.com/documentation/mapkit/mkusertrackingmode/follow)Added [MKUserTrackingModeFollowWithHeading](https://developer.apple.com/documentation/mapkit/mkusertrackingmode/mkusertrackingmodefollowwithheading)Added [MKUserTrackingModeNone](https://developer.apple.com/documentation/mapkit/mkusertrackingmode/mkusertrackingmodenone)MKPlacemark.hRemoved MKPlacemark.addressDictionaryRemoved MKPlacemark.administrativeAreaRemoved MKPlacemark.countryRemoved MKPlacemark.localityRemoved MKPlacemark.postalCodeRemoved MKPlacemark.subAdministrativeAreaRemoved MKPlacemark.subLocalityRemoved MKPlacemark.subThoroughfareRemoved MKPlacemark.thoroughfareModified [MKPlacemark](https://developer.apple.com/documentation/mapkit/mkplacemark)

|  | Superclass |
| --- | --- |
| From | NSObject |
| To | CLPlacemark |

MKReverseGeocoder.hAdded MK_CLASS_DEPRECATED() (no architecture available)Added bogusMethod (no architecture available)Added cancel (no architecture available)Added coordinate (no architecture available)Added delegate (no architecture available)Added initWithCoordinate (no architecture available)Added placemark (no architecture available)Added querying (no architecture available)Added [start](https://developer.apple.com/documentation/kernel/iodevicememory/initelement/start) (no architecture available)Modified [MKReverseGeocoder.coordinate](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/1618477-coordinate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [-[MKReverseGeocoder initWithCoordinate:]](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/1618471-initwithcoordinate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [MKReverseGeocoder.delegate](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/1618478-delegate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [MKReverseGeocoder.placemark](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/1618481-placemark)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [-[MKReverseGeocoderDelegate reverseGeocoder:didFindPlacemark:]](https://developer.apple.com/documentation/mapkit/mkreversegeocoderdelegate/1618476-reversegeocoder)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [-[MKReverseGeocoderDelegate reverseGeocoder:didFailWithError:]](https://developer.apple.com/documentation/mapkit/mkreversegeocoderdelegate/1618473-reversegeocoder)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [-[MKReverseGeocoder cancel]](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/1618479-cancel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [MKReverseGeocoder.querying](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/1618474-querying)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [-[MKReverseGeocoder start]](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/1618480-start)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

MKShape.hModified [MKShape.subtitle](https://developer.apple.com/documentation/mapkit/mkshape/1437592-subtitle)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*subtitle |
| To | @property(nonatomic, copy) NSString \*subtitle |

Modified [MKShape.title](https://developer.apple.com/documentation/mapkit/mkshape/1437594-title)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*title |
| To | @property(nonatomic, copy) NSString \*title |

MKUserLocation.hAdded [MKUserLocation.heading](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452721-heading)Modified [MKUserLocation.subtitle](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452562-subtitle)

|  | Declaration |
| --- | --- |
| From | @property(retain, nonatomic) NSString \*subtitle |
| To | @property(nonatomic, copy) NSString \*subtitle |

Modified [MKUserLocation.location](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452415-location)

|  | Declaration |
| --- | --- |
| From | @property(readonly, nonatomic) CLLocation \*location |
| To | @property(readonly, retain, nonatomic) CLLocation \*location |

Modified [MKUserLocation.title](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452058-title)

|  | Declaration |
| --- | --- |
| From | @property(retain, nonatomic) NSString \*title |
| To | @property(nonatomic, copy) NSString \*title |

MKUserTrackingBarButtonItem.hAdded [MKUserTrackingBarButtonItem](https://developer.apple.com/documentation/mapkit/mkusertrackingbarbuttonitem)Added [-[MKUserTrackingBarButtonItem initWithMapView:]](https://developer.apple.com/documentation/mapkit/mkusertrackingbarbuttonitem/1620146-initwithmapview)Added [MKUserTrackingBarButtonItem.mapView](https://developer.apple.com/documentation/mapkit/mkusertrackingbarbuttonitem/1620161-mapview)

## MediaPlayer

MPMediaItem.hAdded [-[MPMediaItemArtwork initWithImage:]](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621747-initwithimage)Added [MPMediaTypeAnyVideo](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypeanyvideo)Added [MPMediaTypeAudioITunesU](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypeaudioitunesu)Added [MPMediaTypeMovie](https://developer.apple.com/documentation/mediaplayer/mpmediatype/1621708-movie)Added [MPMediaTypeMusicVideo](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypemusicvideo)Added [MPMediaTypeTVShow](https://developer.apple.com/documentation/mediaplayer/mpmediatype/1621701-tvshow)Added [MPMediaTypeVideoITunesU](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypevideoitunesu)Added [MPMediaTypeVideoPodcast](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypevideopodcast)MPMoviePlayerController.hAdded [MPMoviePlayerController.airPlayVideoActive](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620906-isairplayvideoactive)Added [MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620802-mpmovieplayerisairplayvideoactiv)MPMusicPlayerController.hAdded [MPMusicPlayerController.indexOfNowPlayingItem](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624246-indexofnowplayingitem)MPNowPlayingInfoCenter.hAdded [MPNowPlayingInfoCenter](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter)Added [+[MPNowPlayingInfoCenter defaultCenter]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/1615899-defaultcenter)Added [MPNowPlayingInfoCenter.nowPlayingInfo](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/1615903-nowplayinginfo)Added [MPNowPlayingInfoPropertyChapterCount](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertychaptercount)Added [MPNowPlayingInfoPropertyChapterNumber](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertychapternumber)Added [MPNowPlayingInfoPropertyElapsedPlaybackTime](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyelapsedplaybacktime)Added [MPNowPlayingInfoPropertyPlaybackQueueCount](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyplaybackqueuecount)Added [MPNowPlayingInfoPropertyPlaybackQueueIndex](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyplaybackqueueindex)Added [MPNowPlayingInfoPropertyPlaybackRate](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyplaybackrate)

## MessageUI

MFMessageComposeViewController.hAdded [MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollertextmessageavailabilitydidchangenotification)Added [MFMessageComposeViewControllerTextMessageAvailabilityKey](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollertextmessageavailabilitykey)

## MobileCoreServices

No changes

## NewsstandKit

NKAssetDownload.hAdded [NKAssetDownload](https://developer.apple.com/documentation/newsstandkit/nkassetdownload)Added [NKAssetDownload.URLRequest](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615802-urlrequest)Added [-[NKAssetDownload downloadWithDelegate:]](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615792-download)Added [NKAssetDownload.identifier](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615807-identifier)Added [NKAssetDownload.issue](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615800-issue)Added [NKAssetDownload.userInfo](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615811-userinfo)NKIssue.hAdded [NKIssue](https://developer.apple.com/documentation/newsstandkit/nkissue)Added [-[NKIssue addAssetWithRequest:]](https://developer.apple.com/documentation/newsstandkit/nkissue/1615794-addasset)Added [NKIssue.contentURL](https://developer.apple.com/documentation/newsstandkit/nkissue/1615813-contenturl)Added [NKIssue.date](https://developer.apple.com/documentation/newsstandkit/nkissue/1615809-date)Added [NKIssue.downloadingAssets](https://developer.apple.com/documentation/newsstandkit/nkissue/1615791-downloadingassets)Added [NKIssue.name](https://developer.apple.com/documentation/newsstandkit/nkissue/1615789-name)Added [NKIssue.status](https://developer.apple.com/documentation/newsstandkit/nkissue/1615808-status)Added [NKIssueContentStatus](https://developer.apple.com/documentation/newsstandkit/nkissuecontentstatus)Added [NKIssueContentStatusAvailable](https://developer.apple.com/documentation/newsstandkit/nkissuecontentstatus/available)Added [NKIssueContentStatusDownloading](https://developer.apple.com/documentation/newsstandkit/nkissuecontentstatus/downloading)Added [NKIssueContentStatusNone](https://developer.apple.com/documentation/newsstandkit/nkissuecontentstatus/none)Added [NKIssueDownloadCompletedNotification](https://developer.apple.com/documentation/newsstandkit/nkissuedownloadcompletednotification)NKLibrary.hAdded [NKLibrary](https://developer.apple.com/documentation/newsstandkit/nklibrary)Added [-[NKLibrary addIssueWithName:date:]](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615804-addissue)Added [NKLibrary.currentlyReadingIssue](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615812-currentlyreadingissue)Added [NKLibrary.downloadingAssets](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615806-downloadingassets)Added [-[NKLibrary issueWithName:]](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615796-issuewithname)Added [NKLibrary.issues](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615803-issues)Added [-[NKLibrary removeIssue:]](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615810-removeissue)Added [+[NKLibrary sharedLibrary]](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615801-sharedlibrary)NKNSURLConnectionAdditions.hAdded [NSURLConnection.newsstandAssetDownload](https://developer.apple.com/documentation/foundation/nsurlconnection/1615799-newsstandassetdownload)Added NSURLConnection(NKAssetDownloadAdditions)

## OpenAL

oalMacOSX_OALExtensions.hAdded #def ALC_ASA_OBSTRUCTIONAdded #def ALC_ASA_OCCLUSIONAdded #def ALC_ASA_REVERB_EQ_BANDWITHAdded #def ALC_ASA_REVERB_EQ_FREQAdded #def ALC_ASA_REVERB_EQ_GAINAdded #def ALC_ASA_REVERB_GLOBAL_LEVELAdded #def ALC_ASA_REVERB_ONAdded #def ALC_ASA_REVERB_ROOM_TYPEAdded #def ALC_ASA_REVERB_ROOM_TYPE_CathedralAdded #def ALC_ASA_REVERB_ROOM_TYPE_LargeChamberAdded #def ALC_ASA_REVERB_ROOM_TYPE_LargeHallAdded #def ALC_ASA_REVERB_ROOM_TYPE_LargeHall2Added #def ALC_ASA_REVERB_ROOM_TYPE_LargeRoomAdded #def ALC_ASA_REVERB_ROOM_TYPE_LargeRoom2Added #def ALC_ASA_REVERB_ROOM_TYPE_MediumChamberAdded #def ALC_ASA_REVERB_ROOM_TYPE_MediumHallAdded #def ALC_ASA_REVERB_ROOM_TYPE_MediumHall2Added #def ALC_ASA_REVERB_ROOM_TYPE_MediumHall3Added #def ALC_ASA_REVERB_ROOM_TYPE_MediumRoomAdded #def ALC_ASA_REVERB_ROOM_TYPE_PlateAdded #def ALC_ASA_REVERB_ROOM_TYPE_SmallRoomAdded #def ALC_ASA_REVERB_SEND_LEVELAdded #def AL_QUEUE_HAS_LOOPEDAdded alSourceAddNotificationProcPtrAdded alSourceNotificationProcAdded alSourceRemoveNotificationProcPtrAdded alcASAGetListenerProcPtrAdded alcASAGetSourceProcPtrAdded alcASASetListenerProcPtrAdded alcASASetSourceProcPtr

## OpenGLES

glext.hAdded [#def GL_ACTIVE_PROGRAM_EXT](https://developer.apple.com/documentation/opengles/gl_active_program_ext)Added [#def GL_ALL_SHADER_BITS_EXT](https://developer.apple.com/documentation/opengles/gl_all_shader_bits_ext)Added [#def GL_ANY_SAMPLES_PASSED_CONSERVATIVE_EXT](https://developer.apple.com/documentation/opengles/gl_any_samples_passed_conservative_ext)Added [#def GL_ANY_SAMPLES_PASSED_EXT](https://developer.apple.com/documentation/opengles/gl_any_samples_passed_ext)Added [#def GL_BUFFER_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_buffer_object_ext)Added [#def GL_COMPARE_REF_TO_TEXTURE_EXT](https://developer.apple.com/documentation/opengles/gl_compare_ref_to_texture_ext)Added [#def GL_CURRENT_QUERY_EXT](https://developer.apple.com/documentation/opengles/gl_current_query_ext)Added [#def GL_EXT_color_buffer_half_float](https://developer.apple.com/documentation/opengles/gl_ext_color_buffer_half_float)Added [#def GL_EXT_debug_label](https://developer.apple.com/documentation/opengles/gl_ext_debug_label)Added [#def GL_EXT_debug_marker](https://developer.apple.com/documentation/opengles/gl_ext_debug_marker)Added [#def GL_EXT_occlusion_query_boolean](https://developer.apple.com/documentation/opengles/gl_ext_occlusion_query_boolean)Added [#def GL_EXT_separate_shader_objects](https://developer.apple.com/documentation/opengles/gl_ext_separate_shader_objects)Added [#def GL_EXT_shadow_samplers](https://developer.apple.com/documentation/opengles/gl_ext_shadow_samplers)Added [#def GL_EXT_texture_rg](https://developer.apple.com/documentation/opengles/gl_ext_texture_rg)Added [#def GL_FRAGMENT_SHADER_BIT_EXT](https://developer.apple.com/documentation/opengles/gl_fragment_shader_bit_ext)Added [#def GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT](https://developer.apple.com/documentation/opengles/gl_framebuffer_attachment_component_type_ext)Added [#def GL_OES_element_index_uint](https://developer.apple.com/documentation/opengles/gl_oes_element_index_uint)Added [#def GL_PROGRAM_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_program_object_ext)Added [#def GL_PROGRAM_PIPELINE_BINDING_EXT](https://developer.apple.com/documentation/opengles/gl_program_pipeline_binding_ext)Added [#def GL_PROGRAM_PIPELINE_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_program_pipeline_object_ext)Added [#def GL_PROGRAM_SEPARABLE_EXT](https://developer.apple.com/documentation/opengles/gl_program_separable_ext)Added [#def GL_QUERY_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_query_object_ext)Added [#def GL_QUERY_RESULT_AVAILABLE_EXT](https://developer.apple.com/documentation/opengles/gl_query_result_available_ext)Added [#def GL_QUERY_RESULT_EXT](https://developer.apple.com/documentation/opengles/gl_query_result_ext)Added [#def GL_R16F_EXT](https://developer.apple.com/documentation/opengles/gl_r16f_ext)Added [#def GL_R8_EXT](https://developer.apple.com/documentation/opengles/gl_r8_ext)Added [#def GL_RED_EXT](https://developer.apple.com/documentation/opengles/gl_red_ext)Added [#def GL_RG16F_EXT](https://developer.apple.com/documentation/opengles/gl_rg16f_ext)Added [#def GL_RG8_EXT](https://developer.apple.com/documentation/opengles/gl_rg8_ext)Added [#def GL_RGB16F_EXT](https://developer.apple.com/documentation/opengles/gl_rgb16f_ext)Added [#def GL_RGBA16F_EXT](https://developer.apple.com/documentation/opengles/gl_rgba16f_ext)Added [#def GL_RG_EXT](https://developer.apple.com/documentation/opengles/gl_rg_ext)Added [#def GL_SHADER_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_shader_object_ext)Added [#def GL_TEXTURE_COMPARE_FUNC_EXT](https://developer.apple.com/documentation/opengles/gl_texture_compare_func_ext)Added [#def GL_TEXTURE_COMPARE_MODE_EXT](https://developer.apple.com/documentation/opengles/gl_texture_compare_mode_ext)Added [#def GL_UNSIGNED_INT_OES](https://developer.apple.com/documentation/opengles/gl_unsigned_int_oes)Added [#def GL_UNSIGNED_NORMALIZED_EXT](https://developer.apple.com/documentation/opengles/gl_unsigned_normalized_ext)Added [#def GL_VERTEX_ARRAY_OBJECT_EXT](https://developer.apple.com/documentation/opengles/gl_vertex_array_object_ext)Added [#def GL_VERTEX_SHADER_BIT_EXT](https://developer.apple.com/documentation/opengles/gl_vertex_shader_bit_ext)Added GLhalfAdded [glActiveShaderProgramEXT()](https://developer.apple.com/documentation/opengles/1623883-glactiveshaderprogramext)Added [glBeginQueryEXT()](https://developer.apple.com/documentation/opengles/1624737-glbeginqueryext)Added [glBindProgramPipelineEXT()](https://developer.apple.com/documentation/opengles/1623765-glbindprogrampipelineext)Added [glCreateShaderProgramvEXT()](https://developer.apple.com/documentation/opengles/1623803-glcreateshaderprogramvext)Added [glDeleteProgramPipelinesEXT()](https://developer.apple.com/documentation/opengles/1623799-gldeleteprogrampipelinesext)Added [glDeleteQueriesEXT()](https://developer.apple.com/documentation/opengles/1624734-gldeletequeriesext)Added [glEndQueryEXT()](https://developer.apple.com/documentation/opengles/1624754-glendqueryext)Added [glGenProgramPipelinesEXT()](https://developer.apple.com/documentation/opengles/1623828-glgenprogrampipelinesext)Added [glGenQueriesEXT()](https://developer.apple.com/documentation/opengles/1624720-glgenqueriesext)Added [glGetObjectLabelEXT()](https://developer.apple.com/documentation/opengles/1614334-glgetobjectlabelext)Added [glGetProgramPipelineInfoLogEXT()](https://developer.apple.com/documentation/opengles/1623790-glgetprogrampipelineinfologext)Added [glGetProgramPipelineivEXT()](https://developer.apple.com/documentation/opengles/1623867-glgetprogrampipelineivext)Added glGetQueryObjectivEXT()Added [glGetQueryObjectuivEXT()](https://developer.apple.com/documentation/opengles/1624686-glgetqueryobjectuivext)Added [glGetQueryivEXT()](https://developer.apple.com/documentation/opengles/1624752-glgetqueryivext)Added [glInsertEventMarkerEXT()](https://developer.apple.com/documentation/opengles/1614284-glinserteventmarkerext)Added [glIsProgramPipelineEXT()](https://developer.apple.com/documentation/opengles/1623823-glisprogrampipelineext)Added [glIsQueryEXT()](https://developer.apple.com/documentation/opengles/1624711-glisqueryext)Added [glLabelObjectEXT()](https://developer.apple.com/documentation/opengles/1614324-gllabelobjectext)Added [glPopGroupMarkerEXT()](https://developer.apple.com/documentation/opengles/1614338-glpopgroupmarkerext)Added [glProgramParameteriEXT()](https://developer.apple.com/documentation/opengles/1623862-glprogramparameteriext)Added [glProgramUniform1fEXT()](https://developer.apple.com/documentation/opengles/1623822-glprogramuniform1fext)Added [glProgramUniform1fvEXT()](https://developer.apple.com/documentation/opengles/1623778-glprogramuniform1fvext)Added [glProgramUniform1iEXT()](https://developer.apple.com/documentation/opengles/1623830-glprogramuniform1iext)Added [glProgramUniform1ivEXT()](https://developer.apple.com/documentation/opengles/1623805-glprogramuniform1ivext)Added [glProgramUniform2fEXT()](https://developer.apple.com/documentation/opengles/1623858-glprogramuniform2fext)Added [glProgramUniform2fvEXT()](https://developer.apple.com/documentation/opengles/1623769-glprogramuniform2fvext)Added [glProgramUniform2iEXT()](https://developer.apple.com/documentation/opengles/1623782-glprogramuniform2iext)Added [glProgramUniform2ivEXT()](https://developer.apple.com/documentation/opengles/1623880-glprogramuniform2ivext)Added [glProgramUniform3fEXT()](https://developer.apple.com/documentation/opengles/1623780-glprogramuniform3fext)Added [glProgramUniform3fvEXT()](https://developer.apple.com/documentation/opengles/1623770-glprogramuniform3fvext)Added [glProgramUniform3iEXT()](https://developer.apple.com/documentation/opengles/1623793-glprogramuniform3iext)Added [glProgramUniform3ivEXT()](https://developer.apple.com/documentation/opengles/1623784-glprogramuniform3ivext)Added [glProgramUniform4fEXT()](https://developer.apple.com/documentation/opengles/1623829-glprogramuniform4fext)Added [glProgramUniform4fvEXT()](https://developer.apple.com/documentation/opengles/1623804-glprogramuniform4fvext)Added [glProgramUniform4iEXT()](https://developer.apple.com/documentation/opengles/1623851-glprogramuniform4iext)Added [glProgramUniform4ivEXT()](https://developer.apple.com/documentation/opengles/1623791-glprogramuniform4ivext)Added [glProgramUniformMatrix2fvEXT()](https://developer.apple.com/documentation/opengles/1623814-glprogramuniformmatrix2fvext)Added [glProgramUniformMatrix3fvEXT()](https://developer.apple.com/documentation/opengles/1623873-glprogramuniformmatrix3fvext)Added [glProgramUniformMatrix4fvEXT()](https://developer.apple.com/documentation/opengles/1623777-glprogramuniformmatrix4fvext)Added [glPushGroupMarkerEXT()](https://developer.apple.com/documentation/opengles/1614275-glpushgroupmarkerext)Added [glUseProgramStagesEXT()](https://developer.apple.com/documentation/opengles/1623776-gluseprogramstagesext)Added [glValidateProgramPipelineEXT()](https://developer.apple.com/documentation/opengles/1623826-glvalidateprogrampipelineext)

## QuartzCore

CAEmitterCell.hAdded [CAEmitterCell](https://developer.apple.com/documentation/quartzcore/caemittercell)Added [CAEmitterCell.alphaRange](https://developer.apple.com/documentation/quartzcore/caemittercell/1522110-alpharange)Added [CAEmitterCell.alphaSpeed](https://developer.apple.com/documentation/quartzcore/caemittercell/1522120-alphaspeed)Added [CAEmitterCell.birthRate](https://developer.apple.com/documentation/quartzcore/caemittercell/1522100-birthrate)Added [CAEmitterCell.blueRange](https://developer.apple.com/documentation/quartzcore/caemittercell/1522158-bluerange)Added [CAEmitterCell.blueSpeed](https://developer.apple.com/documentation/quartzcore/caemittercell/1522082-bluespeed)Added [CAEmitterCell.color](https://developer.apple.com/documentation/quartzcore/caemittercell/1522322-color)Added [CAEmitterCell.contents](https://developer.apple.com/documentation/quartzcore/caemittercell/1522109-contents)Added [CAEmitterCell.contentsRect](https://developer.apple.com/documentation/quartzcore/caemittercell/1522124-contentsrect)Added [+[CAEmitterCell defaultValueForKey:]](https://developer.apple.com/documentation/quartzcore/caemittercell/1521964-defaultvalue)Added [CAEmitterCell.emissionLatitude](https://developer.apple.com/documentation/quartzcore/caemittercell/1521857-emissionlatitude)Added [CAEmitterCell.emissionLongitude](https://developer.apple.com/documentation/quartzcore/caemittercell/1522013-emissionlongitude)Added [CAEmitterCell.emissionRange](https://developer.apple.com/documentation/quartzcore/caemittercell/1521847-emissionrange)Added [+[CAEmitterCell emitterCell]](https://developer.apple.com/documentation/quartzcore/caemittercell/1584370-emittercell)Added [CAEmitterCell.emitterCells](https://developer.apple.com/documentation/quartzcore/caemittercell/1521866-emittercells)Added [CAEmitterCell.enabled](https://developer.apple.com/documentation/quartzcore/caemittercell/1521831-enabled)Added [CAEmitterCell.greenRange](https://developer.apple.com/documentation/quartzcore/caemittercell/1521867-greenrange)Added [CAEmitterCell.greenSpeed](https://developer.apple.com/documentation/quartzcore/caemittercell/1521946-greenspeed)Added [CAEmitterCell.lifetime](https://developer.apple.com/documentation/quartzcore/caemittercell/1522075-lifetime)Added [CAEmitterCell.lifetimeRange](https://developer.apple.com/documentation/quartzcore/caemittercell/1522101-lifetimerange)Added [CAEmitterCell.magnificationFilter](https://developer.apple.com/documentation/quartzcore/caemittercell/1522228-magnificationfilter)Added [CAEmitterCell.minificationFilter](https://developer.apple.com/documentation/quartzcore/caemittercell/1522222-minificationfilter)Added [CAEmitterCell.minificationFilterBias](https://developer.apple.com/documentation/quartzcore/caemittercell/1521907-minificationfilterbias)Added [CAEmitterCell.name](https://developer.apple.com/documentation/quartzcore/caemittercell/1521909-name)Added [CAEmitterCell.redRange](https://developer.apple.com/documentation/quartzcore/caemittercell/1522176-redrange)Added [CAEmitterCell.redSpeed](https://developer.apple.com/documentation/quartzcore/caemittercell/1521859-redspeed)Added [CAEmitterCell.scale](https://developer.apple.com/documentation/quartzcore/caemittercell/1522287-scale)Added [CAEmitterCell.scaleRange](https://developer.apple.com/documentation/quartzcore/caemittercell/1521915-scalerange)Added [CAEmitterCell.scaleSpeed](https://developer.apple.com/documentation/quartzcore/caemittercell/1522241-scalespeed)Added [-[CAEmitterCell shouldArchiveValueForKey:]](https://developer.apple.com/documentation/quartzcore/caemittercell/1522005-shouldarchivevalue)Added [CAEmitterCell.spin](https://developer.apple.com/documentation/quartzcore/caemittercell/1522361-spin)Added [CAEmitterCell.spinRange](https://developer.apple.com/documentation/quartzcore/caemittercell/1522084-spinrange)Added [CAEmitterCell.style](https://developer.apple.com/documentation/quartzcore/caemittercell/1521925-style)Added [CAEmitterCell.velocity](https://developer.apple.com/documentation/quartzcore/caemittercell/1521837-velocity)Added [CAEmitterCell.velocityRange](https://developer.apple.com/documentation/quartzcore/caemittercell/1522330-velocityrange)Added [CAEmitterCell.xAcceleration](https://developer.apple.com/documentation/quartzcore/caemittercell/1521879-xacceleration)Added [CAEmitterCell.yAcceleration](https://developer.apple.com/documentation/quartzcore/caemittercell/1522077-yacceleration)Added [CAEmitterCell.zAcceleration](https://developer.apple.com/documentation/quartzcore/caemittercell/1522298-zacceleration)CAEmitterLayer.hAdded [CAEmitterLayer](https://developer.apple.com/documentation/quartzcore/caemitterlayer)Added [CAEmitterLayer.birthRate](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521976-birthrate)Added [CAEmitterLayer.emitterCells](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521923-emittercells)Added [CAEmitterLayer.emitterDepth](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521844-emitterdepth)Added [CAEmitterLayer.emitterMode](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522128-emittermode)Added [CAEmitterLayer.emitterPosition](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522289-emitterposition)Added [CAEmitterLayer.emitterShape](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521919-emittershape)Added [CAEmitterLayer.emitterSize](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521869-emittersize)Added [CAEmitterLayer.emitterZPosition](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522169-emitterzposition)Added [CAEmitterLayer.lifetime](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522144-lifetime)Added [CAEmitterLayer.preservesDepth](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521872-preservesdepth)Added [CAEmitterLayer.renderMode](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522104-rendermode)Added [CAEmitterLayer.scale](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521841-scale)Added [CAEmitterLayer.seed](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522079-seed)Added [CAEmitterLayer.spin](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521861-spin)Added [CAEmitterLayer.velocity](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522015-velocity)Added [kCAEmitterLayerAdditive](https://developer.apple.com/documentation/quartzcore/caemitterlayerrendermode/1521960-additive)Added [kCAEmitterLayerBackToFront](https://developer.apple.com/documentation/quartzcore/caemitterlayerrendermode/1522192-backtofront)Added [kCAEmitterLayerCircle](https://developer.apple.com/documentation/quartzcore/caemitterlayeremittershape/1521908-circle)Added [kCAEmitterLayerCuboid](https://developer.apple.com/documentation/quartzcore/caemitterlayeremittershape/1522036-cuboid)Added [kCAEmitterLayerLine](https://developer.apple.com/documentation/quartzcore/kcaemitterlayerline)Added [kCAEmitterLayerOldestFirst](https://developer.apple.com/documentation/quartzcore/caemitterlayerrendermode/1521902-oldestfirst)Added [kCAEmitterLayerOldestLast](https://developer.apple.com/documentation/quartzcore/kcaemitterlayeroldestlast)Added [kCAEmitterLayerOutline](https://developer.apple.com/documentation/quartzcore/kcaemitterlayeroutline)Added [kCAEmitterLayerPoint](https://developer.apple.com/documentation/quartzcore/caemitterlayeremittershape/1522188-point)Added [kCAEmitterLayerPoints](https://developer.apple.com/documentation/quartzcore/caemitterlayeremittermode/1522068-points)Added [kCAEmitterLayerRectangle](https://developer.apple.com/documentation/quartzcore/caemitterlayeremittershape/1521920-rectangle)Added [kCAEmitterLayerSphere](https://developer.apple.com/documentation/quartzcore/kcaemitterlayersphere)Added [kCAEmitterLayerSurface](https://developer.apple.com/documentation/quartzcore/kcaemitterlayersurface)Added [kCAEmitterLayerUnordered](https://developer.apple.com/documentation/quartzcore/kcaemitterlayerunordered)Added [kCAEmitterLayerVolume](https://developer.apple.com/documentation/quartzcore/kcaemitterlayervolume)

## QuickLook

QLPreviewController.hModified [QLPreviewController.delegate](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/1617005-delegate)

|  | Declaration |
| --- | --- |
| From | @property(assign) id delegate |
| To | @property(assign) id<QLPreviewControllerDelegate> delegate |

## Security

CipherSuite.hAdded [SSLCipherSuite](https://developer.apple.com/documentation/security/sslciphersuite)Added [SSL_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dhe_dss_export_with_des40_cbc_sha)Added [SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dhe_dss_with_3des_ede_cbc_sha)Added [SSL_DHE_DSS_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dhe_dss_with_des_cbc_sha)Added [SSL_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dhe_rsa_export_with_des40_cbc_sha)Added [SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dhe_rsa_with_3des_ede_cbc_sha)Added [SSL_DHE_RSA_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dhe_rsa_with_des_cbc_sha)Added [SSL_DH_DSS_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_dss_export_with_des40_cbc_sha)Added [SSL_DH_DSS_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dh_dss_with_3des_ede_cbc_sha)Added [SSL_DH_DSS_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dh_dss_with_des_cbc_sha)Added [SSL_DH_RSA_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_rsa_export_with_des40_cbc_sha)Added [SSL_DH_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dh_rsa_with_3des_ede_cbc_sha)Added [SSL_DH_RSA_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_rsa_with_des_cbc_sha)Added [SSL_DH_anon_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_anon_export_with_des40_cbc_sha)Added [SSL_DH_anon_EXPORT_WITH_RC4_40_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_anon_export_with_rc4_40_md5)Added [SSL_DH_anon_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dh_anon_with_3des_ede_cbc_sha)Added [SSL_DH_anon_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_anon_with_des_cbc_sha)Added [SSL_DH_anon_WITH_RC4_128_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_anon_with_rc4_128_md5)Added [SSL_FORTEZZA_DMS_WITH_FORTEZZA_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_fortezza_dms_with_fortezza_cbc_sha)Added [SSL_FORTEZZA_DMS_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_fortezza_dms_with_null_sha)Added [SSL_NO_SUCH_CIPHERSUITE](https://developer.apple.com/documentation/security/ssl_no_such_ciphersuite)Added [SSL_NULL_WITH_NULL_NULL](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_null_with_null_null)Added [SSL_RSA_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/ssl_rsa_export_with_des40_cbc_sha)Added [SSL_RSA_EXPORT_WITH_RC2_CBC_40_MD5](https://developer.apple.com/documentation/security/ssl_rsa_export_with_rc2_cbc_40_md5)Added [SSL_RSA_EXPORT_WITH_RC4_40_MD5](https://developer.apple.com/documentation/security/ssl_rsa_export_with_rc4_40_md5)Added [SSL_RSA_WITH_3DES_EDE_CBC_MD5](https://developer.apple.com/documentation/security/ssl_rsa_with_3des_ede_cbc_md5)Added [SSL_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/ssl_rsa_with_3des_ede_cbc_sha)Added [SSL_RSA_WITH_DES_CBC_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_with_des_cbc_md5)Added [SSL_RSA_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_with_des_cbc_sha)Added [SSL_RSA_WITH_IDEA_CBC_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_with_idea_cbc_md5)Added [SSL_RSA_WITH_IDEA_CBC_SHA](https://developer.apple.com/documentation/security/ssl_rsa_with_idea_cbc_sha)Added [SSL_RSA_WITH_NULL_MD5](https://developer.apple.com/documentation/security/ssl_rsa_with_null_md5)Added [SSL_RSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/ssl_rsa_with_null_sha)Added [SSL_RSA_WITH_RC2_CBC_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_with_rc2_cbc_md5)Added [SSL_RSA_WITH_RC4_128_MD5](https://developer.apple.com/documentation/security/ssl_rsa_with_rc4_128_md5)Added [SSL_RSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_with_rc4_128_sha)Added [TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_dss_with_3des_ede_cbc_sha)Added [TLS_DHE_DSS_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_dss_with_aes_128_cbc_sha)Added [TLS_DHE_DSS_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dhe_dss_with_aes_128_cbc_sha256)Added [TLS_DHE_DSS_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_dhe_dss_with_aes_128_gcm_sha256)Added [TLS_DHE_DSS_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_dss_with_aes_256_cbc_sha)Added [TLS_DHE_DSS_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_dss_with_aes_256_cbc_sha256)Added [TLS_DHE_DSS_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_dss_with_aes_256_gcm_sha384)Added [TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_rsa_with_3des_ede_cbc_sha)Added [TLS_DHE_RSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_rsa_with_aes_128_cbc_sha)Added [TLS_DHE_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dhe_rsa_with_aes_128_cbc_sha256)Added [TLS_DHE_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_rsa_with_aes_128_gcm_sha256)Added [TLS_DHE_RSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_rsa_with_aes_256_cbc_sha)Added [TLS_DHE_RSA_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_rsa_with_aes_256_cbc_sha256)Added [TLS_DHE_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_rsa_with_aes_256_gcm_sha384)Added [TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_dss_with_3des_ede_cbc_sha)Added [TLS_DH_DSS_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_dss_with_aes_128_cbc_sha)Added [TLS_DH_DSS_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_dss_with_aes_128_cbc_sha256)Added [TLS_DH_DSS_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_dss_with_aes_128_gcm_sha256)Added [TLS_DH_DSS_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_dss_with_aes_256_cbc_sha)Added [TLS_DH_DSS_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_dss_with_aes_256_cbc_sha256)Added [TLS_DH_DSS_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_dh_dss_with_aes_256_gcm_sha384)Added [TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_rsa_with_3des_ede_cbc_sha)Added [TLS_DH_RSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_rsa_with_aes_128_cbc_sha)Added [TLS_DH_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_rsa_with_aes_128_cbc_sha256)Added [TLS_DH_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_dh_rsa_with_aes_128_gcm_sha256)Added [TLS_DH_RSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_rsa_with_aes_256_cbc_sha)Added [TLS_DH_RSA_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_rsa_with_aes_256_cbc_sha256)Added [TLS_DH_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_rsa_with_aes_256_gcm_sha384)Added [TLS_DH_anon_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_anon_with_3des_ede_cbc_sha)Added [TLS_DH_anon_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_anon_with_aes_128_cbc_sha)Added [TLS_DH_anon_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_anon_with_aes_128_cbc_sha256)Added [TLS_DH_anon_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_anon_with_aes_128_gcm_sha256)Added [TLS_DH_anon_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_anon_with_aes_256_cbc_sha)Added [TLS_DH_anon_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_anon_with_aes_256_cbc_sha256)Added [TLS_DH_anon_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_dh_anon_with_aes_256_gcm_sha384)Added [TLS_DH_anon_WITH_RC4_128_MD5](https://developer.apple.com/documentation/security/tls_dh_anon_with_rc4_128_md5)Added [TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_3des_ede_cbc_sha)Added [TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_aes_128_cbc_sha)Added [TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_aes_128_cbc_sha256)Added [TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_ecdsa_with_aes_128_gcm_sha256)Added [TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_ecdsa_with_aes_256_cbc_sha)Added [TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_ecdsa_with_aes_256_cbc_sha384)Added [TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_aes_256_gcm_sha384)Added [TLS_ECDHE_ECDSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_null_sha)Added [TLS_ECDHE_ECDSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_ecdsa_with_rc4_128_sha)Added [TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_rsa_with_3des_ede_cbc_sha)Added [TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_rsa_with_aes_128_cbc_sha)Added [TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_128_cbc_sha256)Added [TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_128_gcm_sha256)Added [TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_rsa_with_aes_256_cbc_sha)Added [TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_256_cbc_sha384)Added [TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_256_gcm_sha384)Added [TLS_ECDHE_RSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_rsa_with_null_sha)Added [TLS_ECDHE_RSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_rsa_with_rc4_128_sha)Added [TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_ecdsa_with_3des_ede_cbc_sha)Added [TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_aes_128_cbc_sha)Added [TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_ecdh_ecdsa_with_aes_128_cbc_sha256)Added [TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_aes_128_gcm_sha256)Added [TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_ecdsa_with_aes_256_cbc_sha)Added [TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/tls_ecdh_ecdsa_with_aes_256_cbc_sha384)Added [TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_aes_256_gcm_sha384)Added [TLS_ECDH_ECDSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_null_sha)Added [TLS_ECDH_ECDSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_rc4_128_sha)Added [TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_3des_ede_cbc_sha)Added [TLS_ECDH_RSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_aes_128_cbc_sha)Added [TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_aes_128_cbc_sha256)Added [TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_aes_128_gcm_sha256)Added [TLS_ECDH_RSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_aes_256_cbc_sha)Added [TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_aes_256_cbc_sha384)Added [TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_aes_256_gcm_sha384)Added [TLS_ECDH_RSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_null_sha)Added [TLS_ECDH_RSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_rc4_128_sha)Added [TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_anon_with_3des_ede_cbc_sha)Added [TLS_ECDH_anon_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_anon_with_aes_128_cbc_sha)Added [TLS_ECDH_anon_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_anon_with_aes_256_cbc_sha)Added [TLS_ECDH_anon_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_anon_with_null_sha)Added [TLS_ECDH_anon_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_anon_with_rc4_128_sha)Added [TLS_EMPTY_RENEGOTIATION_INFO_SCSV](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_empty_renegotiation_info_scsv)Added [TLS_NULL_WITH_NULL_NULL](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_null_with_null_null)Added [TLS_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_3des_ede_cbc_sha)Added [TLS_RSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_with_aes_128_cbc_sha)Added [TLS_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_aes_128_cbc_sha256)Added [TLS_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_rsa_with_aes_128_gcm_sha256)Added [TLS_RSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_with_aes_256_cbc_sha)Added [TLS_RSA_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_rsa_with_aes_256_cbc_sha256)Added [TLS_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_aes_256_gcm_sha384)Added [TLS_RSA_WITH_NULL_MD5](https://developer.apple.com/documentation/security/tls_rsa_with_null_md5)Added [TLS_RSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_null_sha)Added [TLS_RSA_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/tls_rsa_with_null_sha256)Added [TLS_RSA_WITH_RC4_128_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_rc4_128_md5)Added [TLS_RSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_rsa_with_rc4_128_sha)SecureTransport.hAdded [SSLAddDistinguishedName()](https://developer.apple.com/documentation/security/1400906-ssladddistinguishedname)Added [SSLAuthenticate](https://developer.apple.com/documentation/security/sslauthenticate)Added [SSLClientCertificateState](https://developer.apple.com/documentation/security/sslclientcertificatestate)Added [SSLClose()](https://developer.apple.com/documentation/security/1397869-sslclose)Added [SSLConnectionRef](https://developer.apple.com/documentation/security/sslconnectionref)Added [SSLConnectionType](https://developer.apple.com/documentation/security/sslconnectiontype)Added [SSLContextGetTypeID()](https://developer.apple.com/documentation/security/1398165-sslcontextgettypeid)Added [SSLContextRef](https://developer.apple.com/documentation/security/sslcontextref)Added [SSLCopyDistinguishedNames()](https://developer.apple.com/documentation/security/1398461-sslcopydistinguishednames)Added [SSLCopyPeerTrust()](https://developer.apple.com/documentation/security/1397674-sslcopypeertrust)Added [SSLCreateContext()](https://developer.apple.com/documentation/security/1393063-sslcreatecontext)Added [SSLGetBufferedReadSize()](https://developer.apple.com/documentation/security/1394958-sslgetbufferedreadsize)Added [SSLGetClientCertificateState()](https://developer.apple.com/documentation/security/1396612-sslgetclientcertificatestate)Added [SSLGetConnection()](https://developer.apple.com/documentation/security/1397993-sslgetconnection)Added [SSLGetDatagramWriteSize()](https://developer.apple.com/documentation/security/1401259-sslgetdatagramwritesize)Added [SSLGetEnabledCiphers()](https://developer.apple.com/documentation/security/1399101-sslgetenabledciphers)Added [SSLGetMaxDatagramRecordSize()](https://developer.apple.com/documentation/security/1399678-sslgetmaxdatagramrecordsize)Added [SSLGetNegotiatedCipher()](https://developer.apple.com/documentation/security/1394448-sslgetnegotiatedcipher)Added [SSLGetNegotiatedProtocolVersion()](https://developer.apple.com/documentation/security/1397382-sslgetnegotiatedprotocolversion)Added [SSLGetNumberEnabledCiphers()](https://developer.apple.com/documentation/security/1399570-sslgetnumberenabledciphers)Added [SSLGetNumberSupportedCiphers()](https://developer.apple.com/documentation/security/1402304-sslgetnumbersupportedciphers)Added [SSLGetPeerDomainName()](https://developer.apple.com/documentation/security/1400295-sslgetpeerdomainname)Added [SSLGetPeerDomainNameLength()](https://developer.apple.com/documentation/security/1398086-sslgetpeerdomainnamelength)Added [SSLGetPeerID()](https://developer.apple.com/documentation/security/1395882-sslgetpeerid)Added [SSLGetProtocolVersionMax()](https://developer.apple.com/documentation/security/1396167-sslgetprotocolversionmax)Added [SSLGetProtocolVersionMin()](https://developer.apple.com/documentation/security/1395690-sslgetprotocolversionmin)Added [SSLGetSessionOption()](https://developer.apple.com/documentation/security/1392604-sslgetsessionoption)Added [SSLGetSessionState()](https://developer.apple.com/documentation/security/1393517-sslgetsessionstate)Added [SSLGetSupportedCiphers()](https://developer.apple.com/documentation/security/1395230-sslgetsupportedciphers)Added [SSLHandshake()](https://developer.apple.com/documentation/security/1400161-sslhandshake)Added [SSLProtocol](https://developer.apple.com/documentation/security/sslprotocol)Added [SSLProtocolSide](https://developer.apple.com/documentation/security/sslprotocolside)Added [SSLRead()](https://developer.apple.com/documentation/security/1394324-sslread)Added [SSLReadFunc](https://developer.apple.com/documentation/security/sslreadfunc)Added [SSLSessionOption](https://developer.apple.com/documentation/security/sslsessionoption)Added [SSLSessionState](https://developer.apple.com/documentation/security/sslsessionstate)Added [SSLSetCertificate()](https://developer.apple.com/documentation/security/1392400-sslsetcertificate)Added [SSLSetClientSideAuthenticate()](https://developer.apple.com/documentation/security/1397567-sslsetclientsideauthenticate)Added [SSLSetConnection()](https://developer.apple.com/documentation/security/1398843-sslsetconnection)Added [SSLSetDatagramHelloCookie()](https://developer.apple.com/documentation/security/1398936-sslsetdatagramhellocookie)Added [SSLSetEnabledCiphers()](https://developer.apple.com/documentation/security/1397188-sslsetenabledciphers)Added [SSLSetEncryptionCertificate()](https://developer.apple.com/documentation/security/1398098-sslsetencryptioncertificate)Added [SSLSetIOFuncs()](https://developer.apple.com/documentation/security/1396081-sslsetiofuncs)Added [SSLSetMaxDatagramRecordSize()](https://developer.apple.com/documentation/security/1394978-sslsetmaxdatagramrecordsize)Added [SSLSetPeerDomainName()](https://developer.apple.com/documentation/security/1393047-sslsetpeerdomainname)Added [SSLSetPeerID()](https://developer.apple.com/documentation/security/1400006-sslsetpeerid)Added [SSLSetProtocolVersionMax()](https://developer.apple.com/documentation/security/1393798-sslsetprotocolversionmax)Added [SSLSetProtocolVersionMin()](https://developer.apple.com/documentation/security/1398139-sslsetprotocolversionmin)Added [SSLSetSessionOption()](https://developer.apple.com/documentation/security/1399173-sslsetsessionoption)Added [SSLWrite()](https://developer.apple.com/documentation/security/1400864-sslwrite)Added [SSLWriteFunc](https://developer.apple.com/documentation/security/sslwritefunc)Added [errSSLBadCert](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslbadcert)Added [errSSLBadCipherSuite](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslbadciphersuite)Added [errSSLBadConfiguration](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslbadconfiguration)Added [errSSLBadRecordMac](https://developer.apple.com/documentation/security/errsslbadrecordmac)Added [errSSLBufferOverflow](https://developer.apple.com/documentation/security/errsslbufferoverflow)Added [errSSLCertExpired](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslcertexpired)Added [errSSLCertNotYetValid](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslcertnotyetvalid)Added errSSLClientAuthCompletedAdded [errSSLClientCertRequested](https://developer.apple.com/documentation/security/errsslclientcertrequested)Added [errSSLClosedAbort](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslclosedabort)Added [errSSLClosedGraceful](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslclosedgraceful)Added [errSSLClosedNoNotify](https://developer.apple.com/documentation/security/errsslclosednonotify)Added [errSSLConnectionRefused](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslconnectionrefused)Added [errSSLCrypto](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslcrypto)Added [errSSLDecryptionFail](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errssldecryptionfail)Added [errSSLFatalAlert](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslfatalalert)Added [errSSLHostNameMismatch](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslhostnamemismatch)Added [errSSLIllegalParam](https://developer.apple.com/documentation/security/errsslillegalparam)Added [errSSLInternal](https://developer.apple.com/documentation/security/errsslinternal)Added errSSLLastAdded [errSSLModuleAttach](https://developer.apple.com/documentation/security/errsslmoduleattach)Added [errSSLNegotiation](https://developer.apple.com/documentation/security/errsslnegotiation)Added [errSSLNoRootCert](https://developer.apple.com/documentation/security/errsslnorootcert)Added [errSSLPeerAccessDenied](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeeraccessdenied)Added [errSSLPeerAuthCompleted](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerauthcompleted)Added [errSSLPeerBadCert](https://developer.apple.com/documentation/security/errsslpeerbadcert)Added [errSSLPeerBadRecordMac](https://developer.apple.com/documentation/security/errsslpeerbadrecordmac)Added [errSSLPeerCertExpired](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeercertexpired)Added [errSSLPeerCertRevoked](https://developer.apple.com/documentation/security/errsslpeercertrevoked)Added [errSSLPeerCertUnknown](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeercertunknown)Added [errSSLPeerDecodeError](https://developer.apple.com/documentation/security/errsslpeerdecodeerror)Added [errSSLPeerDecompressFail](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerdecompressfail)Added [errSSLPeerDecryptError](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerdecrypterror)Added [errSSLPeerDecryptionFail](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerdecryptionfail)Added [errSSLPeerExportRestriction](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerexportrestriction)Added [errSSLPeerHandshakeFail](https://developer.apple.com/documentation/security/errsslpeerhandshakefail)Added [errSSLPeerInsufficientSecurity](https://developer.apple.com/documentation/security/errsslpeerinsufficientsecurity)Added [errSSLPeerInternalError](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerinternalerror)Added [errSSLPeerNoRenegotiation](https://developer.apple.com/documentation/security/errsslpeernorenegotiation)Added [errSSLPeerProtocolVersion](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerprotocolversion)Added [errSSLPeerRecordOverflow](https://developer.apple.com/documentation/security/errsslpeerrecordoverflow)Added [errSSLPeerUnexpectedMsg](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerunexpectedmsg)Added [errSSLPeerUnknownCA](https://developer.apple.com/documentation/security/errsslpeerunknownca)Added [errSSLPeerUnsupportedCert](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerunsupportedcert)Added [errSSLPeerUserCancelled](https://developer.apple.com/documentation/security/errsslpeerusercancelled)Added [errSSLProtocol](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslprotocol)Added [errSSLRecordOverflow](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslrecordoverflow)Added [errSSLServerAuthCompleted](https://developer.apple.com/documentation/security/secure_transport/1503828-secure_transport_result_codes/errsslserverauthcompleted)Added [errSSLSessionNotFound](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslsessionnotfound)Added [errSSLUnknownRootCert](https://developer.apple.com/documentation/security/errsslunknownrootcert)Added [errSSLWouldBlock](https://developer.apple.com/documentation/security/errsslwouldblock)Added [errSSLXCertChainInvalid](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslxcertchaininvalid)Added [kAlwaysAuthenticate](https://developer.apple.com/documentation/security/sslauthenticate/alwaysauthenticate)Added [kDTLSProtocol1](https://developer.apple.com/documentation/security/sslprotocol/dtlsprotocol1)Added [kNeverAuthenticate](https://developer.apple.com/documentation/security/sslauthenticate/neverauthenticate)Added [kSSLAborted](https://developer.apple.com/documentation/security/sslsessionstate/ksslaborted)Added [kSSLClientCertNone](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertnone)Added [kSSLClientCertRejected](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertrejected)Added [kSSLClientCertRequested](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertrequested)Added [kSSLClientCertSent](https://developer.apple.com/documentation/security/sslclientcertificatestate/certsent)Added [kSSLClientSide](https://developer.apple.com/documentation/security/sslprotocolside/ksslclientside)Added [kSSLClosed](https://developer.apple.com/documentation/security/sslsessionstate/ksslclosed)Added [kSSLConnected](https://developer.apple.com/documentation/security/sslsessionstate/connected)Added [kSSLDatagramType](https://developer.apple.com/documentation/security/sslconnectiontype/kssldatagramtype)Added [kSSLHandshake](https://developer.apple.com/documentation/security/sslsessionstate/handshake)Added [kSSLIdle](https://developer.apple.com/documentation/security/sslsessionstate/idle)Added [kSSLProtocol2](https://developer.apple.com/documentation/security/sslprotocol/sslprotocol2)Added [kSSLProtocol3](https://developer.apple.com/documentation/security/sslprotocol/sslprotocol3)Added [kSSLProtocol3Only](https://developer.apple.com/documentation/security/sslprotocol/ksslprotocol3only)Added [kSSLProtocolAll](https://developer.apple.com/documentation/security/sslprotocol/sslprotocolall)Added [kSSLProtocolUnknown](https://developer.apple.com/documentation/security/sslprotocol/sslprotocolunknown)Added [kSSLServerSide](https://developer.apple.com/documentation/security/sslprotocolside/ksslserverside)Added [kSSLSessionOptionBreakOnCertRequested](https://developer.apple.com/documentation/security/sslsessionoption/breakoncertrequested)Added [kSSLSessionOptionBreakOnClientAuth](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonclientauth)Added [kSSLSessionOptionBreakOnServerAuth](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonserverauth)Added [kSSLStreamType](https://developer.apple.com/documentation/security/sslconnectiontype/ksslstreamtype)Added [kTLSProtocol1](https://developer.apple.com/documentation/security/sslprotocol/ktlsprotocol1)Added [kTLSProtocol11](https://developer.apple.com/documentation/security/sslprotocol/tlsprotocol11)Added [kTLSProtocol12](https://developer.apple.com/documentation/security/sslprotocol/tlsprotocol12)Added [kTLSProtocol1Only](https://developer.apple.com/documentation/security/sslprotocol/tlsprotocol1only)Added [kTryAuthenticate](https://developer.apple.com/documentation/security/sslauthenticate/tryauthenticate)

## StoreKit

SKPayment.hModified [+[SKPayment paymentWithProductIdentifier:]](https://developer.apple.com/documentation/storekit/skpayment/1623907-paymentwithproductidentifier)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

## SystemConfiguration

No changes

## Twitter

TWRequest.hAdded TWRequestAdded TWRequest.URLAdded TWRequest.accountAdded -[TWRequest addMultiPartData:withName:type:]Added -[TWRequest initWithURL:parameters:requestMethod:]Added TWRequest.parametersAdded -[TWRequest performRequestWithHandler:]Added TWRequest.requestMethodAdded -[TWRequest signedURLRequest]Added TWRequestHandlerAdded TWRequestMethodAdded TWRequestMethodDELETEAdded TWRequestMethodGETAdded TWRequestMethodPOSTTWTweetComposeViewController.hAdded TWTweetComposeViewControllerAdded -[TWTweetComposeViewController addImage:]Added -[TWTweetComposeViewController addURL:]Added +[TWTweetComposeViewController canSendTweet]Added TWTweetComposeViewController.completionHandlerAdded -[TWTweetComposeViewController removeAllImages]Added -[TWTweetComposeViewController removeAllURLs]Added -[TWTweetComposeViewController setInitialText:]Added TWTweetComposeViewControllerCompletionHandlerAdded TWTweetComposeViewControllerResultAdded TWTweetComposeViewControllerResultCancelledAdded TWTweetComposeViewControllerResultDone

## UIKit

UIAccelerometer.hModified [-[UIAccelerometerDelegate accelerometer:didAccelerate:]](https://developer.apple.com/documentation/uikit/uiaccelerometerdelegate/1620653-accelerometer)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

UIAccessibility.hAdded [NSObject.accessibilityActivationPoint](https://developer.apple.com/documentation/objectivec/nsobject/1615179-accessibilityactivationpoint)Added [NSObject.accessibilityElementsHidden](https://developer.apple.com/documentation/objectivec/nsobject/1615080-accessibilityelementshidden)Added [-[NSObject accessibilityPerformEscape]](https://developer.apple.com/documentation/objectivec/nsobject/1615091-accessibilityperformescape)Added [NSObject.accessibilityViewIsModal](https://developer.apple.com/documentation/objectivec/nsobject/1615089-accessibilityviewismodal)Added [UIAccessibilityReadingContent](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent)Added [-[UIAccessibilityReadingContent accessibilityContentForLineNumber:]](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/1615163-accessibilitycontent)Added [-[UIAccessibilityReadingContent accessibilityFrameForLineNumber:]](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/1615171-accessibilityframeforlinenumber)Added [-[UIAccessibilityReadingContent accessibilityLineNumberForPoint:]](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/1615107-accessibilitylinenumberforpoint)Added [-[UIAccessibilityReadingContent accessibilityPageContent]](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/1615157-accessibilitypagecontent)Added [UIAccessibilityClosedCaptioningStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibilityclosedcaptioningstatusdidchangenotification)Added [UIAccessibilityIsClosedCaptioningEnabled()](https://developer.apple.com/documentation/uikit/uiaccessibility/1615112-isclosedcaptioningenabled)Added [UIAccessibilityIsMonoAudioEnabled()](https://developer.apple.com/documentation/uikit/uiaccessibility/1615123-ismonoaudioenabled)Added [UIAccessibilityMonoAudioStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibilitymonoaudiostatusdidchangenotification)Added [UIAccessibilityScrollDirectionNext](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilityscrolldirection/next)Added [UIAccessibilityScrollDirectionPrevious](https://developer.apple.com/documentation/uikit/uiaccessibilityscrolldirection/uiaccessibilityscrolldirectionprevious)UIAccessibilityConstants.hAdded [UIAccessibilityTraitAllowsDirectInteraction](https://developer.apple.com/documentation/uikit/uiaccessibilitytraitallowsdirectinteraction)Added [UIAccessibilityTraitCausesPageTurn](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1620205-causespageturn)UIAccessibilityElement.hModified [UIAccessibilityElement](https://developer.apple.com/documentation/uikit/uiaccessibilityelement)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | UIAccessibilityIdentification |

UIAccessibilityIdentification.hAdded [UIAccessibilityIdentification](https://developer.apple.com/documentation/uikit/uiaccessibilityidentification)Added [UIAccessibilityIdentification.accessibilityIdentifier](https://developer.apple.com/documentation/uikit/uiaccessibilityidentification/1623132-accessibilityidentifier)Added UIImage(UIAccessibility)Added UIView(UIAccessibility)UIAccessibilityZoom.hAdded [UIAccessibilityRegisterGestureConflictWithZoom()](https://developer.apple.com/documentation/uikit/uiaccessibility/1624919-registergestureconflictwithzoom)Added [UIAccessibilityZoomFocusChanged()](https://developer.apple.com/documentation/uikit/uiaccessibility/1624921-zoomfocuschanged)Added [UIAccessibilityZoomType](https://developer.apple.com/documentation/uikit/uiaccessibility/zoomtype)Added [UIAccessibilityZoomTypeInsertionPoint](https://developer.apple.com/documentation/uikit/uiaccessibility/zoomtype/insertionpoint)UIActivityIndicatorView.hAdded UIActivityIndicatorView.UI_APPEARANCE_SELECTOR (no architecture available)Added [UIActivityIndicatorView.color](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622836-color)UIAlertView.hAdded [UIAlertView.alertViewStyle](https://developer.apple.com/documentation/uikit/uialertview/1620780-alertviewstyle)Added [-[UIAlertView textFieldAtIndex:]](https://developer.apple.com/documentation/uikit/uialertview/1620757-textfieldatindex)Added [-[UIAlertViewDelegate alertViewShouldEnableFirstOtherButton:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620774-alertviewshouldenablefirstotherb)Added [UIAlertViewStyle](https://developer.apple.com/documentation/uikit/uialertviewstyle)Added [UIAlertViewStyleDefault](https://developer.apple.com/documentation/uikit/uialertviewstyle/uialertviewstyledefault)Added [UIAlertViewStyleLoginAndPasswordInput](https://developer.apple.com/documentation/uikit/uialertviewstyle/uialertviewstyleloginandpasswordinput)Added [UIAlertViewStylePlainTextInput](https://developer.apple.com/documentation/uikit/uialertviewstyle/uialertviewstyleplaintextinput)Added [UIAlertViewStyleSecureTextInput](https://developer.apple.com/documentation/uikit/uialertviewstyle/uialertviewstylesecuretextinput)UIAppearance.hAdded [UIAppearance](https://developer.apple.com/documentation/uikit/uiappearance)Added [+[UIAppearance appearance]](https://developer.apple.com/documentation/uikit/uiappearance/1615010-appearance)Added [+[UIAppearance appearanceWhenContainedIn:]](https://developer.apple.com/documentation/uikit/uiappearance/1615006-appearancewhencontainedin)Added [UIAppearanceContainer](https://developer.apple.com/documentation/uikit/uiappearancecontainer)Added [#def UI_APPEARANCE_SELECTOR](https://developer.apple.com/documentation/uikit/ui_appearance_selector)UIApplication.hAdded [-[UIApplication setNewsstandIconImage:]](https://developer.apple.com/documentation/uikit/uiapplication/1623016-setnewsstandiconimage)Added [UIApplication.userInterfaceLayoutDirection](https://developer.apple.com/documentation/uikit/uiapplication/1623025-userinterfacelayoutdirection)Added [UIApplicationDelegate.window](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623056-window)Added UIApplication(UINewsstand)Added [UIApplicationLaunchOptionsNewsstandDownloadsKey](https://developer.apple.com/documentation/uikit/uiapplicationlaunchoptionsnewsstanddownloadskey)Added [UIRemoteNotificationTypeNewsstandContentAvailability](https://developer.apple.com/documentation/uikit/uiremotenotificationtype/1622977-newsstandcontentavailability)Added [UIUserInterfaceLayoutDirection](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection)Added [UIUserInterfaceLayoutDirectionLeftToRight](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection/lefttoright)Added [UIUserInterfaceLayoutDirectionRightToLeft](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection/righttoleft)UIBarButtonItem.hAdded UIBarButtonItem.UI_APPEARANCE_SELECTOR (no architecture available)Added [-[UIBarButtonItem backButtonBackgroundImageForState:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617125-backbuttonbackgroundimageforstat)Added [-[UIBarButtonItem backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617120-backbuttonbackgroundverticalposi)Added [-[UIBarButtonItem backButtonTitlePositionAdjustmentForBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617145-backbuttontitlepositionadjustmen)Added [-[UIBarButtonItem backgroundImageForState:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617134-backgroundimageforstate)Added [-[UIBarButtonItem backgroundVerticalPositionAdjustmentForBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617143-backgroundverticalpositionadjust)Added [-[UIBarButtonItem initWithImage:landscapeImagePhone:style:target:action:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617118-init)Added [-[UIBarButtonItem setBackButtonBackgroundImage:forState:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617128-setbackbuttonbackgroundimage)Added [-[UIBarButtonItem setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617124-setbackbuttonbackgroundverticalp)Added [-[UIBarButtonItem setBackButtonTitlePositionAdjustment:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617139-setbackbuttontitlepositionadjust)Added [-[UIBarButtonItem setBackgroundImage:forState:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617138-setbackgroundimage)Added [-[UIBarButtonItem setBackgroundVerticalPositionAdjustment:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617141-setbackgroundverticalpositionadj)Added [-[UIBarButtonItem setTitlePositionAdjustment:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617149-settitlepositionadjustment)Added [UIBarButtonItem.tintColor](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617135-tintcolor)Added [-[UIBarButtonItem titlePositionAdjustmentForBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617160-titlepositionadjustmentforbarmet)Added [UIBarMetrics](https://developer.apple.com/documentation/uikit/uibarmetrics)Added [UIBarMetricsDefault](https://developer.apple.com/documentation/uikit/uibarmetrics/default)Added [UIBarMetricsLandscapePhone](https://developer.apple.com/documentation/uikit/uibarmetrics/1624859-landscapephone)Modified [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCoding |

UIBarItem.hAdded [UIBarItem.landscapeImagePhone](https://developer.apple.com/documentation/uikit/uibaritem/1616421-landscapeimagephone)Added [UIBarItem.landscapeImagePhoneInsets](https://developer.apple.com/documentation/uikit/uibaritem/1616420-landscapeimagephoneinsets)Added [-[UIBarItem setTitleTextAttributes:forState:]](https://developer.apple.com/documentation/uikit/uibaritem/1616414-settitletextattributes)Added [-[UIBarItem titleTextAttributesForState:]](https://developer.apple.com/documentation/uikit/uibaritem/1616422-titletextattributesforstate)Modified [UIBarItem](https://developer.apple.com/documentation/uikit/uibaritem)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | UIAppearance |

UIButton.hAdded [UIButton.tintColor](https://developer.apple.com/documentation/uikit/uibutton/1624025-tintcolor)UIColor.hAdded [-[CIColor initWithColor:]](https://developer.apple.com/documentation/coreimage/cicolor/1528762-init)Added [UIColor.CIColor](https://developer.apple.com/documentation/uikit/uicolor/1621951-cicolor)Added [+[UIColor colorWithCIColor:]](https://developer.apple.com/documentation/uikit/uicolor/1621940-colorwithcicolor)Added [-[UIColor getHue:saturation:brightness:alpha:]](https://developer.apple.com/documentation/uikit/uicolor/1621949-gethue)Added [-[UIColor getRed:green:blue:alpha:]](https://developer.apple.com/documentation/uikit/uicolor/1621919-getred)Added [-[UIColor getWhite:alpha:]](https://developer.apple.com/documentation/uikit/uicolor/1621927-getwhite)Added [-[UIColor initWithCIColor:]](https://developer.apple.com/documentation/uikit/uicolor/1621938-initwithcicolor)Added CIColor(UIKitAdditions)UIDatePicker.hModified [UIDatePicker.locale](https://developer.apple.com/documentation/uikit/uidatepicker/1615995-locale)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

UIDevice.hModified UIDevice.uniqueIdentifier

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

UIDocument.hAdded [UIDocument](https://developer.apple.com/documentation/uikit/uidocument)Added [-[UIDocument autosaveWithCompletionHandler:]](https://developer.apple.com/documentation/uikit/uidocument/1619981-autosave)Added [-[UIDocument changeCountTokenForSaveOperation:]](https://developer.apple.com/documentation/uikit/uidocument/1619954-changecounttoken)Added [-[UIDocument closeWithCompletionHandler:]](https://developer.apple.com/documentation/uikit/uidocument/1619976-close)Added [-[UIDocument contentsForType:error:]](https://developer.apple.com/documentation/uikit/uidocument/1619978-contentsfortype)Added [-[UIDocument disableEditing]](https://developer.apple.com/documentation/uikit/uidocument/1619958-disableediting)Added [UIDocument.documentState](https://developer.apple.com/documentation/uikit/uidocument/1619982-documentstate)Added [-[UIDocument enableEditing]](https://developer.apple.com/documentation/uikit/uidocument/1619987-enableediting)Added [-[UIDocument fileAttributesToWriteToURL:forSaveOperation:error:]](https://developer.apple.com/documentation/uikit/uidocument/1619947-fileattributestowrite)Added [UIDocument.fileModificationDate](https://developer.apple.com/documentation/uikit/uidocument/1619952-filemodificationdate)Added [-[UIDocument fileNameExtensionForType:saveOperation:]](https://developer.apple.com/documentation/uikit/uidocument/1619969-filenameextensionfortype)Added [UIDocument.fileType](https://developer.apple.com/documentation/uikit/uidocument/1619992-filetype)Added [UIDocument.fileURL](https://developer.apple.com/documentation/uikit/uidocument/1619990-fileurl)Added [-[UIDocument finishedHandlingError:recovered:]](https://developer.apple.com/documentation/uikit/uidocument/1619960-finishedhandlingerror)Added [-[UIDocument handleError:userInteractionPermitted:]](https://developer.apple.com/documentation/uikit/uidocument/1619955-handleerror)Added [-[UIDocument hasUnsavedChanges]](https://developer.apple.com/documentation/uikit/uidocument/1619965-hasunsavedchanges)Added [-[UIDocument initWithFileURL:]](https://developer.apple.com/documentation/uikit/uidocument/1619979-initwithfileurl)Added [-[UIDocument loadFromContents:ofType:error:]](https://developer.apple.com/documentation/uikit/uidocument/1619971-loadfromcontents)Added [UIDocument.localizedName](https://developer.apple.com/documentation/uikit/uidocument/1619959-localizedname)Added [-[UIDocument openWithCompletionHandler:]](https://developer.apple.com/documentation/uikit/uidocument/1619977-open)Added [-[UIDocument performAsynchronousFileAccessUsingBlock:]](https://developer.apple.com/documentation/uikit/uidocument/1619980-performasynchronousfileaccess)Added [-[UIDocument readFromURL:error:]](https://developer.apple.com/documentation/uikit/uidocument/1619967-readfromurl)Added [-[UIDocument revertToContentsOfURL:completionHandler:]](https://developer.apple.com/documentation/uikit/uidocument/1619974-reverttocontentsofurl)Added [-[UIDocument saveToURL:forSaveOperation:completionHandler:]](https://developer.apple.com/documentation/uikit/uidocument/1619988-save)Added [-[UIDocument savingFileType]](https://developer.apple.com/documentation/uikit/uidocument/1619991-savingfiletype)Added [UIDocument.undoManager](https://developer.apple.com/documentation/uikit/uidocument/1619953-undomanager)Added [-[UIDocument updateChangeCount:]](https://developer.apple.com/documentation/uikit/uidocument/1619961-updatechangecount)Added [-[UIDocument updateChangeCountWithToken:forSaveOperation:]](https://developer.apple.com/documentation/uikit/uidocument/1619975-updatechangecountwithtoken)Added [-[UIDocument userInteractionNoLongerPermittedForError:]](https://developer.apple.com/documentation/uikit/uidocument/1619993-userinteractionnolongerpermitted)Added [-[UIDocument writeContents:andAttributes:safelyToURL:forSaveOperation:error:]](https://developer.apple.com/documentation/uikit/uidocument/1619951-writecontents)Added [-[UIDocument writeContents:toURL:forSaveOperation:originalContentsURL:error:]](https://developer.apple.com/documentation/uikit/uidocument/1619989-writecontents)Added [UIDocumentChangeCleared](https://developer.apple.com/documentation/uikit/uidocumentchangekind/uidocumentchangecleared)Added [UIDocumentChangeDone](https://developer.apple.com/documentation/uikit/uidocument/changekind/done)Added [UIDocumentChangeKind](https://developer.apple.com/documentation/uikit/uidocumentchangekind)Added [UIDocumentChangeRedone](https://developer.apple.com/documentation/uikit/uidocumentchangekind/uidocumentchangeredone)Added [UIDocumentChangeUndone](https://developer.apple.com/documentation/uikit/uidocument/changekind/undone)Added [UIDocumentSaveForCreating](https://developer.apple.com/documentation/uikit/uidocumentsaveoperation/uidocumentsaveforcreating)Added [UIDocumentSaveForOverwriting](https://developer.apple.com/documentation/uikit/uidocumentsaveoperation/uidocumentsaveforoverwriting)Added [UIDocumentSaveOperation](https://developer.apple.com/documentation/uikit/uidocumentsaveoperation)Added [UIDocumentState](https://developer.apple.com/documentation/uikit/uidocumentstate)Added [UIDocumentStateChangedNotification](https://developer.apple.com/documentation/uikit/uidocumentstatechangednotification)Added [UIDocumentStateClosed](https://developer.apple.com/documentation/uikit/uidocument/state/1619956-closed)Added [UIDocumentStateEditingDisabled](https://developer.apple.com/documentation/uikit/uidocument/state/1619946-editingdisabled)Added [UIDocumentStateInConflict](https://developer.apple.com/documentation/uikit/uidocumentstate/uidocumentstateinconflict)Added [UIDocumentStateNormal](https://developer.apple.com/documentation/uikit/uidocumentstate/uidocumentstatenormal)Added [UIDocumentStateSavingError](https://developer.apple.com/documentation/uikit/uidocument/state/1619966-savingerror)UIGeometry.hAdded [-[NSCoder decodeUIOffsetForKey:]](https://developer.apple.com/documentation/foundation/nscoder/1624507-decodeuioffsetforkey)Added [-[NSCoder encodeUIOffset:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1624494-encodeuioffset)Added [-[NSValue UIOffsetValue]](https://developer.apple.com/documentation/foundation/nsvalue/1624526-uioffsetvalue)Added [+[NSValue valueWithUIOffset:]](https://developer.apple.com/documentation/foundation/nsvalue/1624530-init)Added [NSStringFromUIOffset()](https://developer.apple.com/documentation/foundation/nscoder/1624491-string)Added [UIOffset](https://developer.apple.com/documentation/uikit/uioffset)Added [UIOffsetEqualToOffset()](https://developer.apple.com/documentation/uikit/1624521-uioffsetequaltooffset)Added [UIOffsetFromString()](https://developer.apple.com/documentation/foundation/nscoder/1624509-uioffset)Added [UIOffsetMake()](https://developer.apple.com/documentation/uikit/uioffset/1624515-init)Added [UIOffsetZero](https://developer.apple.com/documentation/uikit/uioffset/1624501-zero)UIGestureRecognizerSubclass.hRemoved UIGestureRecognizer()Added UIGestureRecognizer(ForSubclassEyesOnly)UIImage.hAdded [-[CIImage initWithImage:]](https://developer.apple.com/documentation/coreimage/ciimage/1624119-initwithimage)Added [-[CIImage initWithImage:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1624098-initwithimage)Added [UIImage.CIImage](https://developer.apple.com/documentation/uikit/uiimage/1624129-ciimage)Added [+[UIImage animatedImageNamed:duration:]](https://developer.apple.com/documentation/uikit/uiimage/1624094-animatedimagenamed)Added [+[UIImage animatedImageWithImages:duration:]](https://developer.apple.com/documentation/uikit/uiimage/1624149-animatedimagewithimages)Added [+[UIImage animatedResizableImageNamed:capInsets:duration:]](https://developer.apple.com/documentation/uikit/uiimage/1624143-animatedresizableimagenamed)Added [UIImage.capInsets](https://developer.apple.com/documentation/uikit/uiimage/1624097-capinsets)Added [UIImage.duration](https://developer.apple.com/documentation/uikit/uiimage/1624155-duration)Added [+[UIImage imageWithCIImage:]](https://developer.apple.com/documentation/uikit/uiimage/1624111-imagewithciimage)Added [UIImage.images](https://developer.apple.com/documentation/uikit/uiimage/1624117-images)Added [-[UIImage initWithCIImage:]](https://developer.apple.com/documentation/uikit/uiimage/1624114-initwithciimage)Added [-[UIImage resizableImageWithCapInsets:]](https://developer.apple.com/documentation/uikit/uiimage/1624102-resizableimagewithcapinsets)Added CIImage(UIKitAdditions)Added UIImage(UIImageDeprecated)Modified [-[UIImage stretchableImageWithLeftCapWidth:topCapHeight:]](https://developer.apple.com/documentation/uikit/uiimage/1624145-stretchableimagewithleftcapwidth)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [UIImage](https://developer.apple.com/documentation/uikit/uiimage)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCoding |

Modified [+[UIImage imageWithCGImage:]](https://developer.apple.com/documentation/uikit/uiimage/1624126-imagewithcgimage)

|  | Declaration |
| --- | --- |
| From | + (UIImage \*)imageWithCGImage:(CGImageRef)imageRef |
| To | + (UIImage \*)imageWithCGImage:(CGImageRef)cgImage |

Modified [-[UIImage initWithCGImage:]](https://developer.apple.com/documentation/uikit/uiimage/1624090-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCGImage:(CGImageRef)imageRef |
| To | - (id)initWithCGImage:(CGImageRef)cgImage |

Modified [+[UIImage imageWithCGImage:scale:orientation:]](https://developer.apple.com/documentation/uikit/uiimage/1624124-imagewithcgimage)

|  | Declaration |
| --- | --- |
| From | + (UIImage \*)imageWithCGImage:(CGImageRef)imageRef scale:(CGFloat)scale orientation:(UIImageOrientation)orientation |
| To | + (UIImage \*)imageWithCGImage:(CGImageRef)cgImage scale:(CGFloat)scale orientation:(UIImageOrientation)orientation |

Modified [UIImage.topCapHeight](https://developer.apple.com/documentation/uikit/uiimage/1624116-topcapheight)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [UIImage.leftCapWidth](https://developer.apple.com/documentation/uikit/uiimage/1624148-leftcapwidth)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [-[UIImage initWithCGImage:scale:orientation:]](https://developer.apple.com/documentation/uikit/uiimage/1624091-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCGImage:(CGImageRef)imageRef scale:(CGFloat)scale orientation:(UIImageOrientation)orientation |
| To | - (id)initWithCGImage:(CGImageRef)cgImage scale:(CGFloat)scale orientation:(UIImageOrientation)orientation |

UIImagePickerController.hAdded [UIImagePickerControllerQualityTypeIFrame1280x720](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/qualitytype/typeiframe1280x720)Added [UIImagePickerControllerQualityTypeIFrame960x540](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerqualitytype/uiimagepickercontrollerqualitytypeiframe960x540)UIInterface.hAdded [+[UIColor underPageBackgroundColor]](https://developer.apple.com/documentation/uikit/uicolor/1623406-underpagebackgroundcolor)UIManagedDocument.hAdded [UIManagedDocument](https://developer.apple.com/documentation/uikit/uimanageddocument)Added [-[UIManagedDocument additionalContentForURL:error:]](https://developer.apple.com/documentation/uikit/uimanageddocument/1622665-additionalcontent)Added [-[UIManagedDocument configurePersistentStoreCoordinatorForURL:ofType:modelConfiguration:storeOptions:error:]](https://developer.apple.com/documentation/uikit/uimanageddocument/1622674-configurepersistentstorecoordina)Added [UIManagedDocument.managedObjectContext](https://developer.apple.com/documentation/uikit/uimanageddocument/1622667-managedobjectcontext)Added [UIManagedDocument.managedObjectModel](https://developer.apple.com/documentation/uikit/uimanageddocument/1622669-managedobjectmodel)Added [UIManagedDocument.modelConfiguration](https://developer.apple.com/documentation/uikit/uimanageddocument/1622671-modelconfiguration)Added [+[UIManagedDocument persistentStoreName]](https://developer.apple.com/documentation/uikit/uimanageddocument/1622672-persistentstorename)Added [UIManagedDocument.persistentStoreOptions](https://developer.apple.com/documentation/uikit/uimanageddocument/1622666-persistentstoreoptions)Added [-[UIManagedDocument persistentStoreTypeForFileType:]](https://developer.apple.com/documentation/uikit/uimanageddocument/1622673-persistentstoretypeforfiletype)Added [-[UIManagedDocument readAdditionalContentFromURL:error:]](https://developer.apple.com/documentation/uikit/uimanageddocument/1622670-readadditionalcontentfromurl)Added [-[UIManagedDocument writeAdditionalContent:toURL:originalContentsURL:error:]](https://developer.apple.com/documentation/uikit/uimanageddocument/1622668-writeadditionalcontent)UINavigationBar.hAdded UINavigationBar.UI_APPEARANCE_SELECTOR (no architecture available)Added [-[UINavigationBar backgroundImageForBarMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624962-backgroundimage)Added [-[UINavigationBar setBackgroundImage:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624926-setbackgroundimage)Added [-[UINavigationBar setTitleVerticalPositionAdjustment:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624959-settitleverticalpositionadjustme)Added [UINavigationBar.titleTextAttributes](https://developer.apple.com/documentation/uikit/uinavigationbar/1624953-titletextattributes)Added [-[UINavigationBar titleVerticalPositionAdjustmentForBarMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624966-titleverticalpositionadjustment)Added [UINavigationItem.leftBarButtonItems](https://developer.apple.com/documentation/uikit/uinavigationitem/1624946-leftbarbuttonitems)Added [UINavigationItem.leftItemsSupplementBackButton](https://developer.apple.com/documentation/uikit/uinavigationitem/1624933-leftitemssupplementbackbutton)Added [UINavigationItem.rightBarButtonItems](https://developer.apple.com/documentation/uikit/uinavigationitem/1624956-rightbarbuttonitems)Added [-[UINavigationItem setLeftBarButtonItems:animated:]](https://developer.apple.com/documentation/uikit/uinavigationitem/1624949-setleftbarbuttonitems)Added [-[UINavigationItem setRightBarButtonItems:animated:]](https://developer.apple.com/documentation/uikit/uinavigationitem/1624939-setrightbarbuttonitems)UIPageViewController.hAdded [UIPageViewController](https://developer.apple.com/documentation/uikit/uipageviewcontroller)Added [UIPageViewController.dataSource](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614117-datasource)Added [UIPageViewController.delegate](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614089-delegate)Added [UIPageViewController.doubleSided](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614098-isdoublesided)Added [UIPageViewController.gestureRecognizers](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614107-gesturerecognizers)Added [-[UIPageViewController initWithTransitionStyle:navigationOrientation:options:]](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614105-init)Added [UIPageViewController.navigationOrientation](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614097-navigationorientation)Added [-[UIPageViewController setViewControllers:direction:animated:completion:]](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614087-setviewcontrollers)Added [UIPageViewController.spineLocation](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614085-spinelocation)Added [UIPageViewController.transitionStyle](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614092-transitionstyle)Added [UIPageViewController.viewControllers](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614106-viewcontrollers)Added [UIPageViewControllerDataSource](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource)Added [-[UIPageViewControllerDataSource pageViewController:viewControllerAfterViewController:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/1614118-pageviewcontroller)Added [-[UIPageViewControllerDataSource pageViewController:viewControllerBeforeViewController:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/1614086-pageviewcontroller)Added [UIPageViewControllerDelegate](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate)Added [-[UIPageViewControllerDelegate pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614090-pageviewcontroller)Added [-[UIPageViewControllerDelegate pageViewController:spineLocationForInterfaceOrientation:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614083-pageviewcontroller)Added [UIPageViewControllerNavigationDirection](https://developer.apple.com/documentation/uikit/uipageviewcontroller/navigationdirection)Added [UIPageViewControllerNavigationDirectionForward](https://developer.apple.com/documentation/uikit/uipageviewcontrollernavigationdirection/uipageviewcontrollernavigationdirectionforward)Added [UIPageViewControllerNavigationDirectionReverse](https://developer.apple.com/documentation/uikit/uipageviewcontrollernavigationdirection/uipageviewcontrollernavigationdirectionreverse)Added [UIPageViewControllerNavigationOrientation](https://developer.apple.com/documentation/uikit/uipageviewcontroller/navigationorientation)Added [UIPageViewControllerNavigationOrientationHorizontal](https://developer.apple.com/documentation/uikit/uipageviewcontrollernavigationorientation/uipageviewcontrollernavigationorientationhorizontal)Added [UIPageViewControllerNavigationOrientationVertical](https://developer.apple.com/documentation/uikit/uipageviewcontroller/navigationorientation/vertical)Added [UIPageViewControllerOptionSpineLocationKey](https://developer.apple.com/documentation/uikit/uipageviewcontroller/optionskey/1614082-spinelocation)Added [UIPageViewControllerSpineLocation](https://developer.apple.com/documentation/uikit/uipageviewcontrollerspinelocation)Added [UIPageViewControllerSpineLocationMax](https://developer.apple.com/documentation/uikit/uipageviewcontroller/spinelocation/max)Added [UIPageViewControllerSpineLocationMid](https://developer.apple.com/documentation/uikit/uipageviewcontroller/spinelocation/mid)Added [UIPageViewControllerSpineLocationMin](https://developer.apple.com/documentation/uikit/uipageviewcontrollerspinelocation/uipageviewcontrollerspinelocationmin)Added [UIPageViewControllerSpineLocationNone](https://developer.apple.com/documentation/uikit/uipageviewcontroller/spinelocation/none)Added [UIPageViewControllerTransitionStyle](https://developer.apple.com/documentation/uikit/uipageviewcontrollertransitionstyle)Added [UIPageViewControllerTransitionStylePageCurl](https://developer.apple.com/documentation/uikit/uipageviewcontrollertransitionstyle/uipageviewcontrollertransitionstylepagecurl)UIPickerView.hModified [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, UITableViewDataSource |

UIPopoverBackgroundView.hAdded [UIPopoverBackgroundView](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview)Added +[UIPopoverBackgroundView arrowBase]Added [UIPopoverBackgroundView.arrowDirection](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview/1619355-arrowdirection)Added +[UIPopoverBackgroundView arrowHeight]Added [UIPopoverBackgroundView.arrowOffset](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview/1619347-arrowoffset)Added +[UIPopoverBackgroundView contentViewInsets]UIPopoverController.hAdded [UIPopoverController.popoverBackgroundViewClass](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624659-popoverbackgroundviewclass)Added [UIPopoverController.popoverLayoutMargins](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624657-layoutmargins)Modified [UIPopoverController](https://developer.apple.com/documentation/uikit/uipopovercontroller)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | UIAppearanceContainer |

UIProgressView.hAdded UIProgressView.UI_APPEARANCE_SELECTOR (no architecture available)Added [UIProgressView.progressImage](https://developer.apple.com/documentation/uikit/uiprogressview/1619837-progressimage)Added [UIProgressView.progressTintColor](https://developer.apple.com/documentation/uikit/uiprogressview/1619836-progresstintcolor)Added [-[UIProgressView setProgress:animated:]](https://developer.apple.com/documentation/uikit/uiprogressview/1619846-setprogress)Added [UIProgressView.trackImage](https://developer.apple.com/documentation/uikit/uiprogressview/1619843-trackimage)Added [UIProgressView.trackTintColor](https://developer.apple.com/documentation/uikit/uiprogressview/1619841-tracktintcolor)UIReferenceLibraryViewController.hAdded [UIReferenceLibraryViewController](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller)Added [+[UIReferenceLibraryViewController dictionaryHasDefinitionForTerm:]](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/1624810-dictionaryhasdefinitionforterm)Added [-[UIReferenceLibraryViewController initWithTerm:]](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/1624808-initwithterm)UIResponder.hAdded -[NSObject makeTextWritingDirectionLeftToRight:]Added -[NSObject makeTextWritingDirectionRightToLeft:]UIScreen.hAdded [UIScreen.brightness](https://developer.apple.com/documentation/uikit/uiscreen/1617830-brightness)Added [UIScreen.overscanCompensation](https://developer.apple.com/documentation/uikit/uiscreen/1617818-overscancompensation)Added [UIScreen.wantsSoftwareDimming](https://developer.apple.com/documentation/uikit/uiscreen/1617821-wantssoftwaredimming)Added [UIScreenBrightnessDidChangeNotification](https://developer.apple.com/documentation/uikit/uiscreen/1617832-brightnessdidchangenotification)Added [UIScreenOverscanCompensation](https://developer.apple.com/documentation/uikit/uiscreenoverscancompensation)Added [UIScreenOverscanCompensationInsetApplicationFrame](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation/1617828-insetapplicationframe)Added [UIScreenOverscanCompensationInsetBounds](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation/insetbounds)Added [UIScreenOverscanCompensationScale](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation/scale)UIScrollView.hAdded [UIScrollView.panGestureRecognizer](https://developer.apple.com/documentation/uikit/uiscrollview/1619425-pangesturerecognizer)Added [UIScrollView.pinchGestureRecognizer](https://developer.apple.com/documentation/uikit/uiscrollview/1619381-pinchgesturerecognizer)Added [-[UIScrollViewDelegate scrollViewWillEndDragging:withVelocity:targetContentOffset:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619385-scrollviewwillenddragging)UISearchBar.hAdded UISearchBar.UI_APPEARANCE_SELECTOR (no architecture available)Added [UISearchBar.backgroundImage](https://developer.apple.com/documentation/uikit/uisearchbar/1624276-backgroundimage)Added [-[UISearchBar imageForSearchBarIcon:state:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624296-imageforsearchbaricon)Added [-[UISearchBar positionAdjustmentForSearchBarIcon:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624323-positionadjustmentforsearchbaric)Added [UISearchBar.scopeBarBackgroundImage](https://developer.apple.com/documentation/uikit/uisearchbar/1624317-scopebarbackgroundimage)Added [-[UISearchBar scopeBarButtonBackgroundImageForState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624311-scopebarbuttonbackgroundimage)Added [-[UISearchBar scopeBarButtonDividerImageForLeftSegmentState:rightSegmentState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624313-scopebarbuttondividerimageforlef)Added [-[UISearchBar scopeBarButtonTitleTextAttributesForState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624309-scopebarbuttontitletextattribute)Added [-[UISearchBar searchFieldBackgroundImageForState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624288-searchfieldbackgroundimage)Added [UISearchBar.searchFieldBackgroundPositionAdjustment](https://developer.apple.com/documentation/uikit/uisearchbar/1624320-searchfieldbackgroundpositionadj)Added [UISearchBar.searchTextPositionAdjustment](https://developer.apple.com/documentation/uikit/uisearchbar/1624297-searchtextpositionadjustment)Added [-[UISearchBar setImage:forSearchBarIcon:state:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624330-setimage)Added [-[UISearchBar setPositionAdjustment:forSearchBarIcon:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624278-setpositionadjustment)Added [-[UISearchBar setScopeBarButtonBackgroundImage:forState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624290-setscopebarbuttonbackgroundimage)Added [-[UISearchBar setScopeBarButtonDividerImage:forLeftSegmentState:rightSegmentState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624308-setscopebarbuttondividerimage)Added [-[UISearchBar setScopeBarButtonTitleTextAttributes:forState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624277-setscopebarbuttontitletextattrib)Added [-[UISearchBar setSearchFieldBackgroundImage:forState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624307-setsearchfieldbackgroundimage)Added UISearchBar.spellCheckingTypeAdded [UISearchBarIcon](https://developer.apple.com/documentation/uikit/uisearchbaricon)Added [UISearchBarIconBookmark](https://developer.apple.com/documentation/uikit/uisearchbaricon/uisearchbariconbookmark)Added [UISearchBarIconClear](https://developer.apple.com/documentation/uikit/uisearchbaricon/uisearchbariconclear)Added [UISearchBarIconResultsList](https://developer.apple.com/documentation/uikit/uisearchbaricon/uisearchbariconresultslist)Added [UISearchBarIconSearch](https://developer.apple.com/documentation/uikit/uisearchbar/icon/search)UISearchDisplayController.hAdded [UISearchDisplayController.searchResultsTitle](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620386-searchresultstitle)UISegmentedControl.hAdded UISegmentedControl.UI_APPEARANCE_SELECTOR (no architecture available)Added [UISegmentedControl.apportionsSegmentWidthsByContent](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618578-apportionssegmentwidthsbycontent)Added [-[UISegmentedControl backgroundImageForState:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618583-backgroundimage)Added [-[UISegmentedControl contentPositionAdjustmentForSegmentType:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618593-contentpositionadjustmentforsegm)Added [-[UISegmentedControl dividerImageForLeftSegmentState:rightSegmentState:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618565-dividerimage)Added [-[UISegmentedControl setBackgroundImage:forState:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618571-setbackgroundimage)Added [-[UISegmentedControl setContentPositionAdjustment:forSegmentType:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618555-setcontentpositionadjustment)Added [-[UISegmentedControl setDividerImage:forLeftSegmentState:rightSegmentState:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618558-setdividerimage)Added [-[UISegmentedControl setTitleTextAttributes:forState:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618570-settitletextattributes)Added [-[UISegmentedControl titleTextAttributesForState:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618566-titletextattributesforstate)Added [UISegmentedControlSegment](https://developer.apple.com/documentation/uikit/uisegmentedcontrolsegment)Added [UISegmentedControlSegmentAlone](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segment/alone)Added [UISegmentedControlSegmentAny](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segment/any)Added [UISegmentedControlSegmentCenter](https://developer.apple.com/documentation/uikit/uisegmentedcontrolsegment/uisegmentedcontrolsegmentcenter)Added [UISegmentedControlSegmentLeft](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segment/left)Added [UISegmentedControlSegmentRight](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segment/right)UISlider.hAdded UISlider.UI_APPEARANCE_SELECTOR (no architecture available)Added [UISlider.maximumTrackTintColor](https://developer.apple.com/documentation/uikit/uislider/1621334-maximumtracktintcolor)Added [UISlider.minimumTrackTintColor](https://developer.apple.com/documentation/uikit/uislider/1621348-minimumtracktintcolor)Added [UISlider.thumbTintColor](https://developer.apple.com/documentation/uikit/uislider/1621332-thumbtintcolor)UISplitViewController.hAdded [-[UISplitViewControllerDelegate splitViewController:shouldHideViewController:inOrientation:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623174-splitviewcontroller)UIStepper.hAdded [UIStepper](https://developer.apple.com/documentation/uikit/uistepper)Added [UIStepper.autorepeat](https://developer.apple.com/documentation/uikit/uistepper/1624079-autorepeat)Added [UIStepper.continuous](https://developer.apple.com/documentation/uikit/uistepper/1624082-iscontinuous)Added [UIStepper.maximumValue](https://developer.apple.com/documentation/uikit/uistepper/1624075-maximumvalue)Added [UIStepper.minimumValue](https://developer.apple.com/documentation/uikit/uistepper/1624078-minimumvalue)Added [UIStepper.stepValue](https://developer.apple.com/documentation/uikit/uistepper/1624083-stepvalue)Added [UIStepper.value](https://developer.apple.com/documentation/uikit/uistepper/1624076-value)Added [UIStepper.wraps](https://developer.apple.com/documentation/uikit/uistepper/1624068-wraps)UIStoryboard.hAdded [UIStoryboard](https://developer.apple.com/documentation/uikit/uistoryboard)Added [-[UIStoryboard instantiateInitialViewController]](https://developer.apple.com/documentation/uikit/uistoryboard/1616213-instantiateinitialviewcontroller)Added [-[UIStoryboard instantiateViewControllerWithIdentifier:]](https://developer.apple.com/documentation/uikit/uistoryboard/1616214-instantiateviewcontrollerwithide)Added [+[UIStoryboard storyboardWithName:bundle:]](https://developer.apple.com/documentation/uikit/uistoryboard/1616216-init)UIStoryboardPopoverSegue.hAdded [UIStoryboardPopoverSegue](https://developer.apple.com/documentation/uikit/uistoryboardpopoversegue)Added [UIStoryboardPopoverSegue.popoverController](https://developer.apple.com/documentation/uikit/uistoryboardpopoversegue/1624759-popovercontroller)UIStoryboardSegue.hAdded [UIStoryboardSegue](https://developer.apple.com/documentation/uikit/uistoryboardsegue)Added [UIStoryboardSegue.destinationViewController](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621916-destinationviewcontroller)Added [UIStoryboardSegue.identifier](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621909-identifier)Added [-[UIStoryboardSegue initWithIdentifier:source:destination:]](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621908-initwithidentifier)Added [-[UIStoryboardSegue perform]](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621912-perform)Added [UIStoryboardSegue.sourceViewController](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621918-source)UIStringDrawing.hAdded [UITextAttributeFont](https://developer.apple.com/documentation/uikit/uitextattributefont)Added [UITextAttributeTextColor](https://developer.apple.com/documentation/uikit/uitextattributetextcolor)Added [UITextAttributeTextShadowColor](https://developer.apple.com/documentation/uikit/uitextattributetextshadowcolor)Added [UITextAttributeTextShadowOffset](https://developer.apple.com/documentation/uikit/uitextattributetextshadowoffset)UISwitch.hAdded UISwitch.UI_APPEARANCE_SELECTOR (no architecture available)Added [UISwitch.onTintColor](https://developer.apple.com/documentation/uikit/uiswitch/1623687-ontintcolor)UITabBar.hAdded UITabBar.UI_APPEARANCE_SELECTOR (no architecture available)Added [UITabBar.backgroundImage](https://developer.apple.com/documentation/uikit/uitabbar/1623469-backgroundimage)Added [UITabBar.selectedImageTintColor](https://developer.apple.com/documentation/uikit/uitabbar/1623470-selectedimagetintcolor)Added [UITabBar.selectionIndicatorImage](https://developer.apple.com/documentation/uikit/uitabbar/1623456-selectionindicatorimage)Added [UITabBar.tintColor](https://developer.apple.com/documentation/uikit/uitabbar/1623460-tintcolor)UITabBarItem.hAdded -[UITabBarItem UI_APPEARANCE_SELECTOR] (no architecture available)Added [-[UITabBarItem finishedSelectedImage]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617051-finishedselectedimage)Added [-[UITabBarItem finishedUnselectedImage]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617053-finishedunselectedimage)Added [-[UITabBarItem setFinishedSelectedImage:withFinishedUnselectedImage:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617063-setfinishedselectedimage)Added [-[UITabBarItem setTitlePositionAdjustment:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617070-titlepositionadjustment)Added [-[UITabBarItem titlePositionAdjustment]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617070-titlepositionadjustment)UITableView.hAdded [UITableView.allowsMultipleSelection](https://developer.apple.com/documentation/uikit/uitableview/1614938-allowsmultipleselection)Added [UITableView.allowsMultipleSelectionDuringEditing](https://developer.apple.com/documentation/uikit/uitableview/1614944-allowsmultipleselectionduringedi)Added [-[UITableView indexPathsForSelectedRows]](https://developer.apple.com/documentation/uikit/uitableview/1614864-indexpathsforselectedrows)Added [-[UITableView moveRowAtIndexPath:toIndexPath:]](https://developer.apple.com/documentation/uikit/uitableview/1614987-moverow)Added [-[UITableView moveSection:toSection:]](https://developer.apple.com/documentation/uikit/uitableview/1614940-movesection)Added [-[UITableView registerNib:forCellReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uitableview/1614937-register)Added [-[UITableViewDelegate tableView:canPerformAction:forRowAtIndexPath:withSender:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614898-tableview)Added [-[UITableViewDelegate tableView:performAction:forRowAtIndexPath:withSender:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614980-tableview)Added [-[UITableViewDelegate tableView:shouldShowMenuForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614950-tableview)Added [UITableViewAutomaticDimension](https://developer.apple.com/documentation/uikit/uitableviewautomaticdimension)Added [UITableViewRowAnimationAutomatic](https://developer.apple.com/documentation/uikit/uitableview/rowanimation/automatic)Modified [-[UITableView dequeueReusableCellWithIdentifier:]](https://developer.apple.com/documentation/uikit/uitableview/1614891-dequeuereusablecell)

|  | Declaration |
| --- | --- |
| From | - (UITableViewCell \*)dequeueReusableCellWithIdentifier:(NSString \*)identifier |
| To | - (id)dequeueReusableCellWithIdentifier:(NSString \*)identifier |

Modified [NSIndexPath.row](https://developer.apple.com/documentation/foundation/nsindexpath/1614853-row)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSUInteger row |
| To | @property(nonatomic, readonly) NSInteger row |

Modified [NSIndexPath.section](https://developer.apple.com/documentation/foundation/nsindexpath/1528298-section)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSUInteger section |
| To | @property(nonatomic, readonly) NSInteger section |

Modified [+[NSIndexPath indexPathForRow:inSection:]](https://developer.apple.com/documentation/foundation/nsindexpath/1614934-init)

|  | Declaration |
| --- | --- |
| From | + (NSIndexPath \*)indexPathForRow:(NSUInteger)row inSection:(NSUInteger)section |
| To | + (NSIndexPath \*)indexPathForRow:(NSInteger)row inSection:(NSInteger)section |

UITableViewCell.hAdded [UITableViewCell.multipleSelectionBackgroundView](https://developer.apple.com/documentation/uikit/uitableviewcell/1623275-multipleselectionbackgroundview)Modified [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, UIGestureRecognizerDelegate |

UITextField.hModified [UITextField](https://developer.apple.com/documentation/uikit/uitextfield)

|  | Protocols |
| --- | --- |
| From | NSCoding, UITextInputTraits |
| To | NSCoding, UITextInput |

UITextInput.hAdded [+[UITextInputMode activeInputModes]](https://developer.apple.com/documentation/uikit/uitextinputmode/1614522-activeinputmodes)Modified [UITextInputTokenizer](https://developer.apple.com/documentation/uikit/uitextinputtokenizer)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSObject |

Modified [UITextInputDelegate](https://developer.apple.com/documentation/uikit/uitextinputdelegate)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSObject |

UITextInputTraits.hAdded [UITextInputTraits.spellCheckingType](https://developer.apple.com/documentation/uikit/uitextinputtraits/1624461-spellcheckingtype)Added [UIKeyboardTypeTwitter](https://developer.apple.com/documentation/uikit/uikeyboardtype/twitter)Added [UITextSpellCheckingType](https://developer.apple.com/documentation/uikit/uitextspellcheckingtype)Added [UITextSpellCheckingTypeDefault](https://developer.apple.com/documentation/uikit/uitextspellcheckingtype/default)Added [UITextSpellCheckingTypeNo](https://developer.apple.com/documentation/uikit/uitextspellcheckingtype/uitextspellcheckingtypeno)Added [UITextSpellCheckingTypeYes](https://developer.apple.com/documentation/uikit/uitextspellcheckingtype/uitextspellcheckingtypeyes)UITextView.hModified [UITextView](https://developer.apple.com/documentation/uikit/uitextview)

|  | Protocols |
| --- | --- |
| From | UITextInputTraits |
| To | UITextInput |

UIToolbar.hAdded UIToolbar.UI_APPEARANCE_SELECTOR (no architecture available)Added [-[UIToolbar backgroundImageForToolbarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uitoolbar/1617998-backgroundimagefortoolbarpositio)Added [-[UIToolbar setBackgroundImage:forToolbarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uitoolbar/1618003-setbackgroundimage)Added [UIToolbarPosition](https://developer.apple.com/documentation/uikit/uitoolbar/uitoolbarposition)Added [UIToolbarPositionAny](https://developer.apple.com/documentation/uikit/uitoolbar/uitoolbarposition/uitoolbarpositionany)Added [UIToolbarPositionBottom](https://developer.apple.com/documentation/uikit/uitoolbar/uitoolbarposition/uitoolbarpositionbottom)Added [UIToolbarPositionTop](https://developer.apple.com/documentation/uikit/uitoolbar/uitoolbarposition/uitoolbarpositiontop)UIView.hAdded [UIViewAnimationOptionTransitionCrossDissolve](https://developer.apple.com/documentation/uikit/uiview/animationoptions/1622499-transitioncrossdissolve)Added [UIViewAnimationOptionTransitionFlipFromBottom](https://developer.apple.com/documentation/uikit/uiview/animationoptions/1622632-transitionflipfrombottom)Added [UIViewAnimationOptionTransitionFlipFromTop](https://developer.apple.com/documentation/uikit/uiviewanimationoptions/uiviewanimationoptiontransitionflipfromtop)Modified [UIView](https://developer.apple.com/documentation/uikit/uiview)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, UIAppearance, UIAppearanceContainer |

UIViewController.hAdded [-[UIViewController addChildViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621394-addchildviewcontroller)Added [+[UIViewController attemptRotationToDeviceOrientation]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621400-attemptrotationtodeviceorientati)Added [-[UIViewController automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621393-automaticallyforwardappearancean)Added [UIViewController.childViewControllers](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621452-children)Added [UIViewController.definesPresentationContext](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621456-definespresentationcontext)Added [-[UIViewController didMoveToParentViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621405-didmove)Added [-[UIViewController dismissViewControllerAnimated:completion:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621505-dismissviewcontrolleranimated)Added -[UIViewController isBeingDismissed]Added -[UIViewController isBeingPresented]Added -[UIViewController isMovingFromParentViewController]Added -[UIViewController isMovingToParentViewController]Added [-[UIViewController performSegueWithIdentifier:sender:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621413-performseguewithidentifier)Added [-[UIViewController prepareForSegue:sender:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621490-prepareforsegue)Added [-[UIViewController presentViewController:animated:completion:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621380-presentviewcontroller)Added [UIViewController.presentedViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621407-presentedviewcontroller)Added [UIViewController.presentingViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621430-presentingviewcontroller)Added [UIViewController.providesPresentationContextTransitionStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621356-providespresentationcontexttrans)Added [-[UIViewController removeFromParentViewController]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621425-removefromparentviewcontroller)Added [UIViewController.storyboard](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621399-storyboard)Added [-[UIViewController transitionFromViewController:toViewController:duration:options:animations:completion:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621363-transition)Added [-[UIViewController viewDidLayoutSubviews]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621398-viewdidlayoutsubviews)Added [-[UIViewController viewWillLayoutSubviews]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621437-viewwilllayoutsubviews)Added [-[UIViewController viewWillUnload]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621427-viewwillunload)Added [-[UIViewController willMoveToParentViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621381-willmovetoparentviewcontroller)Added UIViewController(UIContainerViewControllerCallbacks)Added UIViewController(UIContainerViewControllerProtectedMethods)Added [UIViewControllerHierarchyInconsistencyException](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621513-hierarchyinconsistencyexception)Modified [-[UIViewController willAnimateFirstHalfOfRotationToInterfaceOrientation:duration:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621469-willanimatefirsthalfofrotationto)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, UIAppearanceContainer |

Modified [-[UIViewController willAnimateSecondHalfOfRotationFromInterfaceOrientation:duration:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621509-willanimatesecondhalfofrotationf)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

Modified [-[UIViewController didAnimateFirstHalfOfRotationToInterfaceOrientation:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621496-didanimatefirsthalfofrotationtoi)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 5.0 |

UIWebView.hAdded [UIWebView.mediaPlaybackAllowsAirPlay](https://developer.apple.com/documentation/uikit/uiwebview/1617973-mediaplaybackallowsairplay)Added [UIWebView.scrollView](https://developer.apple.com/documentation/uikit/uiwebview/1617955-scrollview)UIWindow.hAdded [UIKeyboardDidChangeFrameNotification](https://developer.apple.com/documentation/uikit/uikeyboarddidchangeframenotification)Added [UIKeyboardWillChangeFrameNotification](https://developer.apple.com/documentation/uikit/uiresponder/1621623-keyboardwillchangeframenotificat)

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
