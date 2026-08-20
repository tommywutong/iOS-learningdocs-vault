---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/Python.html
archived_at: '2026-07-18T02:54:05.922672Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# Python Changes

## Python

__multiarray_api.hAdded #def NpyIter_AdvancedNewAdded NpyIter_AdvancedNew() (no architecture available)Added NpyIter_Copy() (no architecture available)Added #def NpyIter_CopyAdded #def NpyIter_CreateCompatibleStridesAdded NpyIter_CreateCompatibleStrides() (no architecture available)Added NpyIter_Deallocate() (no architecture available)Added #def NpyIter_DeallocateAdded NpyIter_DebugPrint() (no architecture available)Added #def NpyIter_DebugPrintAdded #def NpyIter_EnableExternalLoopAdded NpyIter_EnableExternalLoop() (no architecture available)Added NpyIter_GetAxisStrideArray() (no architecture available)Added #def NpyIter_GetAxisStrideArrayAdded #def NpyIter_GetBufferSizeAdded NpyIter_GetBufferSize() (no architecture available)Added NpyIter_GetDataPtrArray() (no architecture available)Added #def NpyIter_GetDataPtrArrayAdded #def NpyIter_GetDescrArrayAdded NpyIter_GetDescrArray() (no architecture available)Added #def NpyIter_GetGetMultiIndexAdded NpyIter_GetGetMultiIndex() (no architecture available)Added NpyIter_GetIndexPtr() (no architecture available)Added #def NpyIter_GetIndexPtrAdded NpyIter_GetInitialDataPtrArray() (no architecture available)Added #def NpyIter_GetInitialDataPtrArrayAdded NpyIter_GetInnerFixedStrideArray() (no architecture available)Added #def NpyIter_GetInnerFixedStrideArrayAdded NpyIter_GetInnerLoopSizePtr() (no architecture available)Added #def NpyIter_GetInnerLoopSizePtrAdded #def NpyIter_GetInnerStrideArrayAdded NpyIter_GetInnerStrideArray() (no architecture available)Added NpyIter_GetIterIndex() (no architecture available)Added #def NpyIter_GetIterIndexAdded NpyIter_GetIterIndexRange() (no architecture available)Added #def NpyIter_GetIterIndexRangeAdded #def NpyIter_GetIterNextAdded NpyIter_GetIterNext() (no architecture available)Added #def NpyIter_GetIterSizeAdded NpyIter_GetIterSize() (no architecture available)Added NpyIter_GetIterView() (no architecture available)Added #def NpyIter_GetIterViewAdded #def NpyIter_GetNDimAdded NpyIter_GetNDim() (no architecture available)Added #def NpyIter_GetNOpAdded NpyIter_GetNOp() (no architecture available)Added NpyIter_GetOperandArray() (no architecture available)Added #def NpyIter_GetOperandArrayAdded NpyIter_GetReadFlags() (no architecture available)Added #def NpyIter_GetReadFlagsAdded #def NpyIter_GetShapeAdded NpyIter_GetShape() (no architecture available)Added NpyIter_GetWriteFlags() (no architecture available)Added #def NpyIter_GetWriteFlagsAdded #def NpyIter_GotoIndexAdded NpyIter_GotoIndex() (no architecture available)Added #def NpyIter_GotoIterIndexAdded NpyIter_GotoIterIndex() (no architecture available)Added #def NpyIter_GotoMultiIndexAdded NpyIter_GotoMultiIndex() (no architecture available)Added NpyIter_HasDelayedBufAlloc() (no architecture available)Added #def NpyIter_HasDelayedBufAllocAdded NpyIter_HasExternalLoop() (no architecture available)Added #def NpyIter_HasExternalLoopAdded #def NpyIter_HasIndexAdded NpyIter_HasIndex() (no architecture available)Added #def NpyIter_HasMultiIndexAdded NpyIter_HasMultiIndex() (no architecture available)Added NpyIter_IsBuffered() (no architecture available)Added #def NpyIter_IsBufferedAdded NpyIter_IsGrowInner() (no architecture available)Added #def NpyIter_IsGrowInnerAdded #def NpyIter_IterationNeedsAPIAdded NpyIter_IterationNeedsAPI() (no architecture available)Added #def NpyIter_MultiNewAdded NpyIter_MultiNew() (no architecture available)Added NpyIter_New() (no architecture available)Added #def NpyIter_NewAdded #def NpyIter_RemoveAxisAdded NpyIter_RemoveAxis() (no architecture available)Added #def NpyIter_RemoveMultiIndexAdded NpyIter_RemoveMultiIndex() (no architecture available)Added NpyIter_RequiresBuffering() (no architecture available)Added #def NpyIter_RequiresBufferingAdded NpyIter_Reset() (no architecture available)Added #def NpyIter_ResetAdded NpyIter_ResetBasePointers() (no architecture available)Added #def NpyIter_ResetBasePointersAdded NpyIter_ResetToIterIndexRange() (no architecture available)Added #def NpyIter_ResetToIterIndexRangeAdded #def NpyIter_TypeAdded NpyIter_Type (no architecture available)Added #def PyArray_CanCastArrayToAdded PyArray_CanCastArrayTo() (no architecture available)Added #def PyArray_CanCastTypeToAdded PyArray_CanCastTypeTo() (no architecture available)Added PyArray_CastingConverter() (no architecture available)Added #def PyArray_CastingConverterAdded #def PyArray_ConvertClipmodeSequenceAdded PyArray_ConvertClipmodeSequence() (no architecture available)Added #def PyArray_CountNonzeroAdded PyArray_CountNonzero() (no architecture available)Added #def PyArray_DatetimeStructToDatetimeAdded PyArray_DatetimeStructToDatetime() (no architecture available)Added PyArray_DatetimeToDatetimeStruct() (no architecture available)Added #def PyArray_DatetimeToDatetimeStructAdded PyArray_EinsteinSum() (no architecture available)Added #def PyArray_EinsteinSumAdded #def PyArray_GetArrayParamsFromObjectAdded PyArray_GetArrayParamsFromObject() (no architecture available)Added #def PyArray_MatrixProduct2Added PyArray_MatrixProduct2() (no architecture available)Added #def PyArray_MinScalarTypeAdded PyArray_MinScalarType() (no architecture available)Added PyArray_NewLikeArray() (no architecture available)Added #def PyArray_NewLikeArrayAdded PyArray_PromoteTypes() (no architecture available)Added #def PyArray_PromoteTypesAdded PyArray_ResultType() (no architecture available)Added #def PyArray_ResultTypeAdded PyArray_SetDatetimeParseFunction() (no architecture available)Added #def PyArray_SetDatetimeParseFunctionAdded PyArray_TimedeltaStructToTimedelta() (no architecture available)Added #def PyArray_TimedeltaStructToTimedeltaAdded #def PyArray_TimedeltaToTimedeltaStructAdded PyArray_TimedeltaToTimedeltaStruct() (no architecture available)Added PyDatetimeArrType_Type (no architecture available)Added #def PyDatetimeArrType_TypeAdded #def PyHalfArrType_TypeAdded PyHalfArrType_Type (no architecture available)Added #def PyTimeIntegerArrType_TypeAdded PyTimeIntegerArrType_Type (no architecture available)Added PyTimedeltaArrType_Type (no architecture available)Added #def PyTimedeltaArrType_Type__ufunc_api.hAdded PyUFunc_e_e() (no architecture available)Added #def PyUFunc_e_eAdded PyUFunc_e_e_As_d_d() (no architecture available)Added #def PyUFunc_e_e_As_d_dAdded #def PyUFunc_e_e_As_f_fAdded PyUFunc_e_e_As_f_f() (no architecture available)Added #def PyUFunc_ee_eAdded PyUFunc_ee_e() (no architecture available)Added #def PyUFunc_ee_e_As_dd_dAdded PyUFunc_ee_e_As_dd_d() (no architecture available)Added PyUFunc_ee_e_As_ff_f() (no architecture available)Added #def PyUFunc_ee_e_As_ff_farrayscalars.hAdded PyDatetimeScalarObjectAdded PyHalfScalarObjectAdded PyTimedeltaScalarObjecthalffloat.hAdded #def NPY_HALF_NANAdded #def NPY_HALF_NEGONEAdded #def NPY_HALF_NINFAdded #def NPY_HALF_NZEROAdded #def NPY_HALF_ONEAdded #def NPY_HALF_PINFAdded #def NPY_HALF_PZEROAdded #def NPY_HALF_ZEROAdded npy_double_to_half()Added npy_doublebits_to_halfbits()Added npy_float_to_half()Added npy_floatbits_to_halfbits()Added npy_half_copysign()Added npy_half_eq()Added npy_half_eq_nonan()Added npy_half_ge()Added npy_half_gt()Added npy_half_isfinite()Added npy_half_isinf()Added npy_half_isnan()Added npy_half_iszero()Added npy_half_le()Added npy_half_le_nonan()Added npy_half_lt()Added npy_half_lt_nonan()Added npy_half_ne()Added npy_half_nextafter()Added npy_half_signbit()Added npy_half_spacing()Added npy_half_to_double()Added npy_half_to_float()Added npy_halfbits_to_doublebits()Added npy_halfbits_to_floatbits()ndarrayobject.hAdded NPY_DATETIMEAdded NPY_HALFAdded NPY_HALFLTRAdded NPY_KEEPORDERAdded NPY_NTYPES_ABI_COMPATIBLEAdded NPY_TIMEDELTAndarraytypes.hAdded NPY_CASTINGAdded NPY_EQUIV_CASTINGAdded #def NPY_ITER_ALIGNEDAdded #def NPY_ITER_ALLOCATEAdded #def NPY_ITER_BUFFEREDAdded #def NPY_ITER_COMMON_DTYPEAdded #def NPY_ITER_CONTIGAdded #def NPY_ITER_COPYAdded #def NPY_ITER_C_INDEXAdded #def NPY_ITER_DELAY_BUFALLOCAdded #def NPY_ITER_DONT_NEGATE_STRIDESAdded #def NPY_ITER_EXTERNAL_LOOPAdded #def NPY_ITER_F_INDEXAdded #def NPY_ITER_GLOBAL_FLAGSAdded #def NPY_ITER_GROWINNERAdded #def NPY_ITER_MULTI_INDEXAdded #def NPY_ITER_NBOAdded #def NPY_ITER_NO_BROADCASTAdded #def NPY_ITER_NO_SUBTYPEAdded #def NPY_ITER_PER_OP_FLAGSAdded #def NPY_ITER_RANGEDAdded #def NPY_ITER_READONLYAdded #def NPY_ITER_READWRITEAdded #def NPY_ITER_REDUCE_OKAdded #def NPY_ITER_REFS_OKAdded #def NPY_ITER_UPDATEIFCOPYAdded #def NPY_ITER_WRITEONLYAdded #def NPY_ITER_ZEROSIZE_OKAdded NPY_NO_CASTINGAdded NPY_SAFE_CASTINGAdded NPY_SAME_KIND_CASTINGAdded NPY_UNSAFE_CASTINGAdded NpyIterAdded NpyIter_GetMultiIndexFuncAdded NpyIter_IterNextFuncAdded PyArray_DatetimeMetaDataAdded #def PyArray_ISDATETIMEAdded #def PyArray_IS_C_CONTIGUOUSAdded #def PyArray_IS_F_CONTIGUOUSAdded #def PyDataType_GetDatetimeMetaDataAdded #def PyDataType_ISDATETIMEAdded #def PyTypeNum_ISDATETIMEAdded npy_datetimestructAdded npy_timedeltastructnoprefix.hAdded #def BITSOF_HALFAdded #def SIZEOF_HALFnpy_common.hAdded #def NPY_BITSOF_HALFAdded #def NPY_FLOAT16Added #def NPY_HALF_FMTAdded #def NPY_SIZEOF_HALFAdded npy_halfModified npy_float16

|  | Header |
| --- | --- |
| From | ndarrayobject.h |
| To | npy_common.h |

npy_math.hAdded npy_set_floatstatus_divbyzero()Added npy_set_floatstatus_invalid()Added npy_set_floatstatus_overflow()Added npy_set_floatstatus_underflow()old_defines.hAdded #def PyArray_COMPLEX32Added #def PyArray_FLOAT16Added #def PyArray_HALFAdded #def PyArray_HALFLTRpyobjc-compat.hRemoved #def CGFLOAT_DEFINEDRemoved [#def CGFLOAT_IS_DOUBLE](https://developer.apple.com/documentation/coregraphics/cgfloat_is_double)Removed [#def CGFLOAT_MAX](https://developer.apple.com/documentation/coregraphics/cgfloat_max)Removed [#def CGFLOAT_MIN](https://developer.apple.com/documentation/coregraphics/cgfloat_min)Removed [CGFloat](https://developer.apple.com/documentation/coregraphics/cgfloat) (no architecture available)Removed #def NSINTEGER_DEFINEDRemoved [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) (no architecture available)Removed [#def NSIntegerMax](https://developer.apple.com/documentation/objectivec/nsintegermax)Removed [#def NSIntegerMin](https://developer.apple.com/documentation/objectivec/nsintegermin)Removed [NSUInteger](https://developer.apple.com/documentation/objectivec/nsuinteger) (no architecture available)Removed [#def NSUIntegerMax](https://developer.apple.com/documentation/objectivec/nsuintegermax)

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
