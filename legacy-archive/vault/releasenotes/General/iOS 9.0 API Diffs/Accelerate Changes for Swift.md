---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/Accelerate.html
archived_at: '2026-07-18T02:56:39.869030Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Accelerate Changes for Swift

### Accelerate

Removed CBLAS_DIAG.valueRemoved CBLAS_ORDER.valueRemoved CBLAS_SIDE.valueRemoved CBLAS_TRANSPOSE.valueRemoved CBLAS_UPLO.valueRemoved DSPDoubleSplitComplex.init()Removed DSPDoubleSplitComplex.init(realp: UnsafeMutablePointer<Double>, imagp: UnsafeMutablePointer<Double>)Removed DSPSplitComplex.init()Removed DSPSplitComplex.init(realp: UnsafeMutablePointer<Float>, imagp: UnsafeMutablePointer<Float>)Removed vDSP_DCT_Type [struct]Removed vDSP_DCT_Type.init(_: UInt32)Removed vDSP_DCT_Type.valueRemoved vDSP_DFT_Direction [struct]Removed vDSP_DFT_Direction.init(_: Int32)Removed vDSP_DFT_Direction.valueRemoved vImage_InterpolationMethod.valueRemoved vImageARGBType.valueRemoved vImageMDTableUsageHint.valueRemoved vImageYpCbCrType.valueRemoved vDSP_DCT_IIRemoved vDSP_DCT_IIIRemoved vDSP_DCT_IVRemoved vDSP_DFT_FORWARDRemoved vDSP_DFT_INVERSEAdded CBLAS_DIAG.init(rawValue: UInt32)Added CBLAS_DIAG.rawValueAdded CBLAS_ORDER.init(rawValue: UInt32)Added CBLAS_ORDER.rawValueAdded CBLAS_SIDE.init(rawValue: UInt32)Added CBLAS_SIDE.rawValueAdded CBLAS_TRANSPOSE.init(rawValue: UInt32)Added CBLAS_TRANSPOSE.rawValueAdded CBLAS_UPLO.init(rawValue: UInt32)Added CBLAS_UPLO.rawValueAdded [sparse_matrix_property [struct]](https://developer.apple.com/documentation/accelerate/sparse_matrix_property)Added sparse_matrix_property.init(_: UInt32)Added sparse_matrix_property.init(rawValue: UInt32)Added sparse_matrix_property.rawValueAdded [sparse_norm [struct]](https://developer.apple.com/documentation/accelerate/sparse_norm)Added sparse_norm.init(_: UInt32)Added sparse_norm.init(rawValue: UInt32)Added sparse_norm.rawValueAdded [sparse_status [struct]](https://developer.apple.com/documentation/accelerate/sparse_status)Added sparse_status.init(_: Int32)Added sparse_status.init(rawValue: Int32)Added sparse_status.rawValueAdded vDSP_DCT_Type [enum]Added vDSP_DCT_Type.IIAdded vDSP_DCT_Type.IIIAdded vDSP_DCT_Type.IVAdded [vDSP_DFT_Direction [enum]](https://developer.apple.com/documentation/accelerate/vdsp_dft_direction)Added [vDSP_DFT_Direction.FORWARD](https://developer.apple.com/documentation/accelerate/vdsp_dft_direction/vdsp_dft_forward)Added [vDSP_DFT_Direction.INVERSE](https://developer.apple.com/documentation/accelerate/vdsp_dft_direction/inverse)Added vImage_InterpolationMethod.init(rawValue: UInt32)Added vImage_InterpolationMethod.rawValueAdded vImageARGBType.init(rawValue: UInt32)Added vImageARGBType.rawValueAdded vImageMDTableUsageHint.init(rawValue: UInt32)Added vImageMDTableUsageHint.rawValueAdded [vImageWhitePoint [struct]](https://developer.apple.com/documentation/accelerate/vimagewhitepoint)Added vImageWhitePoint.init()Added vImageWhitePoint.init(white_x: Float, white_y: Float)Added [vImageWhitePoint.white_x](https://developer.apple.com/documentation/accelerate/vimagewhitepoint/1498251-white_x)Added [vImageWhitePoint.white_y](https://developer.apple.com/documentation/accelerate/vimagewhitepoint/1498267-white_y)Added vImageYpCbCrType.init(rawValue: UInt32)Added vImageYpCbCrType.rawValueAdded [kvImageHDRContent](https://developer.apple.com/documentation/accelerate/kvimagehdrcontent)Added [SPARSE_CANNOT_SET_PROPERTY](https://developer.apple.com/documentation/accelerate/sparse_cannot_set_property)Added [sparse_commit(_: UnsafeMutablePointer<Void>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545870-sparse_commit)Added [sparse_dimension](https://developer.apple.com/documentation/accelerate/sparse_dimension)Added [sparse_elementwise_norm_double(_: sparse_matrix_double, _: sparse_norm) -> Double](https://developer.apple.com/documentation/accelerate/1546486-sparse_elementwise_norm_double)Added [sparse_elementwise_norm_float(_: sparse_matrix_float, _: sparse_norm) -> Float](https://developer.apple.com/documentation/accelerate/1544954-sparse_elementwise_norm_float)Added [sparse_extract_block_double(_: sparse_matrix_double, _: sparse_index, _: sparse_index, _: sparse_dimension, _: sparse_dimension, _: UnsafeMutablePointer<Double>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1544385-sparse_extract_block_double)Added [sparse_extract_block_float(_: sparse_matrix_float, _: sparse_index, _: sparse_index, _: sparse_dimension, _: sparse_dimension, _: UnsafeMutablePointer<Float>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545554-sparse_extract_block_float)Added [sparse_extract_sparse_column_double(_: sparse_matrix_double, _: sparse_index, _: sparse_index, _: UnsafeMutablePointer<sparse_index>, _: sparse_dimension, _: UnsafeMutablePointer<Double>, _: UnsafeMutablePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545309-sparse_extract_sparse_column_dou)Added [sparse_extract_sparse_column_float(_: sparse_matrix_float, _: sparse_index, _: sparse_index, _: UnsafeMutablePointer<sparse_index>, _: sparse_dimension, _: UnsafeMutablePointer<Float>, _: UnsafeMutablePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1544689-sparse_extract_sparse_column_flo)Added [sparse_extract_sparse_row_double(_: sparse_matrix_double, _: sparse_index, _: sparse_index, _: UnsafeMutablePointer<sparse_index>, _: sparse_dimension, _: UnsafeMutablePointer<Double>, _: UnsafeMutablePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545736-sparse_extract_sparse_row_double)Added [sparse_extract_sparse_row_float(_: sparse_matrix_float, _: sparse_index, _: sparse_index, _: UnsafeMutablePointer<sparse_index>, _: sparse_dimension, _: UnsafeMutablePointer<Float>, _: UnsafeMutablePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546148-sparse_extract_sparse_row_float)Added [sparse_get_block_dimension_for_col(_: UnsafeMutablePointer<Void>, _: sparse_index) -> Int](https://developer.apple.com/documentation/accelerate/1546658-sparse_get_block_dimension_for_c)Added [sparse_get_block_dimension_for_row(_: UnsafeMutablePointer<Void>, _: sparse_index) -> Int](https://developer.apple.com/documentation/accelerate/1546661-sparse_get_block_dimension_for_r)Added [sparse_get_matrix_nonzero_count(_: UnsafeMutablePointer<Void>) -> Int](https://developer.apple.com/documentation/accelerate/1546682-sparse_get_matrix_nonzero_count)Added [sparse_get_matrix_nonzero_count_for_column(_: UnsafeMutablePointer<Void>, _: sparse_index) -> Int](https://developer.apple.com/documentation/accelerate/1545287-sparse_get_matrix_nonzero_count_)Added [sparse_get_matrix_nonzero_count_for_row(_: UnsafeMutablePointer<Void>, _: sparse_index) -> Int](https://developer.apple.com/documentation/accelerate/1546965-sparse_get_matrix_nonzero_count_)Added [sparse_get_matrix_number_of_columns(_: UnsafeMutablePointer<Void>) -> sparse_dimension](https://developer.apple.com/documentation/accelerate/1544948-sparse_get_matrix_number_of_colu)Added [sparse_get_matrix_number_of_rows(_: UnsafeMutablePointer<Void>) -> sparse_dimension](https://developer.apple.com/documentation/accelerate/1546683-sparse_get_matrix_number_of_rows)Added [sparse_get_matrix_property(_: UnsafeMutablePointer<Void>, _: sparse_matrix_property) -> Int](https://developer.apple.com/documentation/accelerate/1545269-sparse_get_matrix_property)Added [sparse_get_vector_nonzero_count_double(_: sparse_dimension, _: UnsafePointer<Double>, _: sparse_stride) -> Int](https://developer.apple.com/documentation/accelerate/1545336-sparse_get_vector_nonzero_count_)Added [sparse_get_vector_nonzero_count_float(_: sparse_dimension, _: UnsafePointer<Float>, _: sparse_stride) -> Int](https://developer.apple.com/documentation/accelerate/1546927-sparse_get_vector_nonzero_count_)Added [SPARSE_ILLEGAL_PARAMETER](https://developer.apple.com/documentation/accelerate/sparse_illegal_parameter)Added [sparse_index](https://developer.apple.com/documentation/accelerate/sparse_index)Added [sparse_inner_product_dense_double(_: sparse_dimension, _: UnsafePointer<Double>, _: UnsafePointer<sparse_index>, _: UnsafePointer<Double>, _: sparse_stride) -> Double](https://developer.apple.com/documentation/accelerate/1544388-sparse_inner_product_dense_doubl)Added [sparse_inner_product_dense_float(_: sparse_dimension, _: UnsafePointer<Float>, _: UnsafePointer<sparse_index>, _: UnsafePointer<Float>, _: sparse_stride) -> Float](https://developer.apple.com/documentation/accelerate/1544780-sparse_inner_product_dense_float)Added [sparse_inner_product_sparse_double(_: sparse_dimension, _: sparse_dimension, _: UnsafePointer<Double>, _: UnsafePointer<sparse_index>, _: UnsafePointer<Double>, _: UnsafePointer<sparse_index>) -> Double](https://developer.apple.com/documentation/accelerate/1546608-sparse_inner_product_sparse_doub)Added [sparse_inner_product_sparse_float(_: sparse_dimension, _: sparse_dimension, _: UnsafePointer<Float>, _: UnsafePointer<sparse_index>, _: UnsafePointer<Float>, _: UnsafePointer<sparse_index>) -> Float](https://developer.apple.com/documentation/accelerate/1545123-sparse_inner_product_sparse_floa)Added [sparse_insert_block_double(_: sparse_matrix_double, _: UnsafePointer<Double>, _: sparse_dimension, _: sparse_dimension, _: sparse_index, _: sparse_index) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546050-sparse_insert_block_double)Added [sparse_insert_block_float(_: sparse_matrix_float, _: UnsafePointer<Float>, _: sparse_dimension, _: sparse_dimension, _: sparse_index, _: sparse_index) -> sparse_status](https://developer.apple.com/documentation/accelerate/1544469-sparse_insert_block_float)Added [sparse_insert_col_double(_: sparse_matrix_double, _: sparse_index, _: sparse_dimension, _: UnsafePointer<Double>, _: UnsafePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546659-sparse_insert_col_double)Added [sparse_insert_col_float(_: sparse_matrix_float, _: sparse_index, _: sparse_dimension, _: UnsafePointer<Float>, _: UnsafePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545348-sparse_insert_col_float)Added [sparse_insert_entries_double(_: sparse_matrix_double, _: sparse_dimension, _: UnsafePointer<Double>, _: UnsafePointer<sparse_index>, _: UnsafePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546631-sparse_insert_entries_double)Added [sparse_insert_entries_float(_: sparse_matrix_float, _: sparse_dimension, _: UnsafePointer<Float>, _: UnsafePointer<sparse_index>, _: UnsafePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546585-sparse_insert_entries_float)Added [sparse_insert_entry_double(_: sparse_matrix_double, _: Double, _: sparse_index, _: sparse_index) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546876-sparse_insert_entry_double)Added [sparse_insert_entry_float(_: sparse_matrix_float, _: Float, _: sparse_index, _: sparse_index) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546606-sparse_insert_entry_float)Added [sparse_insert_row_double(_: sparse_matrix_double, _: sparse_index, _: sparse_dimension, _: UnsafePointer<Double>, _: UnsafePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545913-sparse_insert_row_double)Added [sparse_insert_row_float(_: sparse_matrix_float, _: sparse_index, _: sparse_dimension, _: UnsafePointer<Float>, _: UnsafePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545432-sparse_insert_row_float)Added [SPARSE_LOWER_SYMMETRIC](https://developer.apple.com/documentation/accelerate/sparse_matrix_property/sparse_lower_symmetric)Added [SPARSE_LOWER_TRIANGULAR](https://developer.apple.com/documentation/accelerate/sparse_matrix_property/sparse_lower_triangular)Added [sparse_matrix_block_create_double(_: sparse_dimension, _: sparse_dimension, _: sparse_dimension, _: sparse_dimension) -> sparse_matrix_double](https://developer.apple.com/documentation/accelerate/1546690-sparse_matrix_block_create_doubl)Added [sparse_matrix_block_create_float(_: sparse_dimension, _: sparse_dimension, _: sparse_dimension, _: sparse_dimension) -> sparse_matrix_float](https://developer.apple.com/documentation/accelerate/1544775-sparse_matrix_block_create_float)Added [sparse_matrix_create_double(_: sparse_dimension, _: sparse_dimension) -> sparse_matrix_double](https://developer.apple.com/documentation/accelerate/1544642-sparse_matrix_create_double)Added [sparse_matrix_create_float(_: sparse_dimension, _: sparse_dimension) -> sparse_matrix_float](https://developer.apple.com/documentation/accelerate/1546996-sparse_matrix_create_float)Added [sparse_matrix_destroy(_: UnsafeMutablePointer<Void>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546691-sparse_matrix_destroy)Added [sparse_matrix_double](https://developer.apple.com/documentation/accelerate/sparse_matrix_double)Added [sparse_matrix_float](https://developer.apple.com/documentation/accelerate/sparse_matrix_float)Added [sparse_matrix_product_dense_double(_: CBLAS_ORDER, _: CBLAS_TRANSPOSE, _: sparse_dimension, _: Double, _: sparse_matrix_double, _: UnsafePointer<Double>, _: sparse_dimension, _: UnsafeMutablePointer<Double>, _: sparse_dimension) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546216-sparse_matrix_product_dense_doub)Added [sparse_matrix_product_dense_float(_: CBLAS_ORDER, _: CBLAS_TRANSPOSE, _: sparse_dimension, _: Float, _: sparse_matrix_float, _: UnsafePointer<Float>, _: sparse_dimension, _: UnsafeMutablePointer<Float>, _: sparse_dimension) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545734-sparse_matrix_product_dense_floa)Added [sparse_matrix_trace_double(_: sparse_matrix_double, _: sparse_index) -> Double](https://developer.apple.com/documentation/accelerate/1544239-sparse_matrix_trace_double)Added [sparse_matrix_trace_float(_: sparse_matrix_float, _: sparse_index) -> Float](https://developer.apple.com/documentation/accelerate/1545041-sparse_matrix_trace_float)Added [sparse_matrix_triangular_solve_dense_double(_: CBLAS_ORDER, _: CBLAS_TRANSPOSE, _: sparse_dimension, _: Double, _: sparse_matrix_double, _: UnsafeMutablePointer<Double>, _: sparse_dimension) -> sparse_status](https://developer.apple.com/documentation/accelerate/1544750-sparse_matrix_triangular_solve_d)Added [sparse_matrix_triangular_solve_dense_float(_: CBLAS_ORDER, _: CBLAS_TRANSPOSE, _: sparse_dimension, _: Float, _: sparse_matrix_float, _: UnsafeMutablePointer<Float>, _: sparse_dimension) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546684-sparse_matrix_triangular_solve_d)Added [sparse_matrix_variable_block_create_double(_: sparse_dimension, _: sparse_dimension, _: UnsafePointer<sparse_dimension>, _: UnsafePointer<sparse_dimension>) -> sparse_matrix_double](https://developer.apple.com/documentation/accelerate/1546650-sparse_matrix_variable_block_cre)Added [sparse_matrix_variable_block_create_float(_: sparse_dimension, _: sparse_dimension, _: UnsafePointer<sparse_dimension>, _: UnsafePointer<sparse_dimension>) -> sparse_matrix_float](https://developer.apple.com/documentation/accelerate/1546234-sparse_matrix_variable_block_cre)Added [sparse_matrix_vector_product_dense_double(_: CBLAS_TRANSPOSE, _: Double, _: sparse_matrix_double, _: UnsafePointer<Double>, _: sparse_stride, _: UnsafeMutablePointer<Double>, _: sparse_stride) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546125-sparse_matrix_vector_product_den)Added [sparse_matrix_vector_product_dense_float(_: CBLAS_TRANSPOSE, _: Float, _: sparse_matrix_float, _: UnsafePointer<Float>, _: sparse_stride, _: UnsafeMutablePointer<Float>, _: sparse_stride) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545507-sparse_matrix_vector_product_den)Added [SPARSE_NORM_INF](https://developer.apple.com/documentation/accelerate/sparse_norm_inf)Added [SPARSE_NORM_ONE](https://developer.apple.com/documentation/accelerate/sparse_norm_one)Added [SPARSE_NORM_R1](https://developer.apple.com/documentation/accelerate/sparse_norm_r1)Added [SPARSE_NORM_TWO](https://developer.apple.com/documentation/accelerate/sparse_norm/sparse_norm_two)Added [sparse_operator_norm_double(_: sparse_matrix_double, _: sparse_norm) -> Double](https://developer.apple.com/documentation/accelerate/1546432-sparse_operator_norm_double)Added [sparse_operator_norm_float(_: sparse_matrix_float, _: sparse_norm) -> Float](https://developer.apple.com/documentation/accelerate/1546614-sparse_operator_norm_float)Added [sparse_outer_product_dense_double(_: sparse_dimension, _: sparse_dimension, _: sparse_dimension, _: Double, _: UnsafePointer<Double>, _: sparse_stride, _: UnsafePointer<Double>, _: UnsafePointer<sparse_index>, _: UnsafeMutablePointer<sparse_matrix_double>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546587-sparse_outer_product_dense_doubl)Added [sparse_outer_product_dense_float(_: sparse_dimension, _: sparse_dimension, _: sparse_dimension, _: Float, _: UnsafePointer<Float>, _: sparse_stride, _: UnsafePointer<Float>, _: UnsafePointer<sparse_index>, _: UnsafeMutablePointer<sparse_matrix_float>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546589-sparse_outer_product_dense_float)Added [sparse_pack_vector_double(_: sparse_dimension, _: sparse_dimension, _: UnsafePointer<Double>, _: sparse_stride, _: UnsafeMutablePointer<Double>, _: UnsafeMutablePointer<sparse_index>) -> Int](https://developer.apple.com/documentation/accelerate/1544402-sparse_pack_vector_double)Added [sparse_pack_vector_float(_: sparse_dimension, _: sparse_dimension, _: UnsafePointer<Float>, _: sparse_stride, _: UnsafeMutablePointer<Float>, _: UnsafeMutablePointer<sparse_index>) -> Int](https://developer.apple.com/documentation/accelerate/1546385-sparse_pack_vector_float)Added [sparse_permute_cols_double(_: sparse_matrix_double, _: UnsafePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545537-sparse_permute_cols_double)Added [sparse_permute_cols_float(_: sparse_matrix_float, _: UnsafePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545945-sparse_permute_cols_float)Added [sparse_permute_rows_double(_: sparse_matrix_double, _: UnsafePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1546664-sparse_permute_rows_double)Added [sparse_permute_rows_float(_: sparse_matrix_float, _: UnsafePointer<sparse_index>) -> sparse_status](https://developer.apple.com/documentation/accelerate/1544648-sparse_permute_rows_float)Added [sparse_set_matrix_property(_: UnsafeMutablePointer<Void>, _: sparse_matrix_property) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545140-sparse_set_matrix_property)Added [sparse_stride](https://developer.apple.com/documentation/accelerate/sparse_stride)Added [SPARSE_SUCCESS](https://developer.apple.com/documentation/accelerate/sparse_status/sparse_success)Added [SPARSE_SYSTEM_ERROR](https://developer.apple.com/documentation/accelerate/sparse_status/sparse_system_error)Added [sparse_unpack_vector_double(_: sparse_dimension, _: sparse_dimension, _: Bool, _: UnsafePointer<Double>, _: UnsafePointer<sparse_index>, _: UnsafeMutablePointer<Double>, _: sparse_stride)](https://developer.apple.com/documentation/accelerate/1545438-sparse_unpack_vector_double)Added [sparse_unpack_vector_float(_: sparse_dimension, _: sparse_dimension, _: Bool, _: UnsafePointer<Float>, _: UnsafePointer<sparse_index>, _: UnsafeMutablePointer<Float>, _: sparse_stride)](https://developer.apple.com/documentation/accelerate/1545010-sparse_unpack_vector_float)Added [SPARSE_UPPER_SYMMETRIC](https://developer.apple.com/documentation/accelerate/sparse_matrix_property/sparse_upper_symmetric)Added [SPARSE_UPPER_TRIANGULAR](https://developer.apple.com/documentation/accelerate/sparse_matrix_property/sparse_upper_triangular)Added [sparse_vector_add_with_scale_dense_double(_: sparse_dimension, _: Double, _: UnsafePointer<Double>, _: UnsafePointer<sparse_index>, _: UnsafeMutablePointer<Double>, _: sparse_stride)](https://developer.apple.com/documentation/accelerate/1546181-sparse_vector_add_with_scale_den)Added [sparse_vector_add_with_scale_dense_float(_: sparse_dimension, _: Float, _: UnsafePointer<Float>, _: UnsafePointer<sparse_index>, _: UnsafeMutablePointer<Float>, _: sparse_stride)](https://developer.apple.com/documentation/accelerate/1544316-sparse_vector_add_with_scale_den)Added [sparse_vector_norm_double(_: sparse_dimension, _: UnsafePointer<Double>, _: UnsafePointer<sparse_index>, _: sparse_norm) -> Double](https://developer.apple.com/documentation/accelerate/1546785-sparse_vector_norm_double)Added [sparse_vector_norm_float(_: sparse_dimension, _: UnsafePointer<Float>, _: UnsafePointer<sparse_index>, _: sparse_norm) -> Float](https://developer.apple.com/documentation/accelerate/1546410-sparse_vector_norm_float)Added [sparse_vector_triangular_solve_dense_double(_: CBLAS_TRANSPOSE, _: Double, _: sparse_matrix_double, _: UnsafeMutablePointer<Double>, _: sparse_stride) -> sparse_status](https://developer.apple.com/documentation/accelerate/1545435-sparse_vector_triangular_solve_d)Added [sparse_vector_triangular_solve_dense_float(_: CBLAS_TRANSPOSE, _: Float, _: sparse_matrix_float, _: UnsafeMutablePointer<Float>, _: sparse_stride) -> sparse_status](https://developer.apple.com/documentation/accelerate/1544828-sparse_vector_triangular_solve_d)Added [vDSP_biquadm_SetActiveFilters(_: vDSP_biquadm_Setup, _: UnsafePointer<Bool>)](https://developer.apple.com/documentation/accelerate/1450108-vdsp_biquadm_setactivefilters)Added [vDSP_biquadm_SetCoefficientsDouble(_: vDSP_biquadm_Setup, _: UnsafePointer<Double>, _: vDSP_Length, _: vDSP_Length, _: vDSP_Length, _: vDSP_Length)](https://developer.apple.com/documentation/accelerate/1450453-vdsp_biquadm_setcoefficientsdoub)Added [vDSP_biquadm_SetCoefficientsSingle(_: vDSP_biquadm_Setup, _: UnsafePointer<Float>, _: vDSP_Length, _: vDSP_Length, _: vDSP_Length, _: vDSP_Length)](https://developer.apple.com/documentation/accelerate/1450128-vdsp_biquadm_setcoefficientssing)Added [vDSP_biquadm_SetTargetsDouble(_: vDSP_biquadm_Setup, _: UnsafePointer<Double>, _: Float, _: Float, _: vDSP_Length, _: vDSP_Length, _: vDSP_Length, _: vDSP_Length)](https://developer.apple.com/documentation/accelerate/1450703-vdsp_biquadm_settargetsdouble)Added [vDSP_biquadm_SetTargetsSingle(_: vDSP_biquadm_Setup, _: UnsafePointer<Float>, _: Float, _: Float, _: vDSP_Length, _: vDSP_Length, _: vDSP_Length, _: vDSP_Length)](https://developer.apple.com/documentation/accelerate/1450077-vdsp_biquadm_settargetssingle)Added [vImageCreateMonochromeColorSpaceWithWhitePointAndTransferFunction(_: UnsafePointer<vImageWhitePoint>, _: UnsafePointer<vImageTransferFunction>, _: CGColorRenderingIntent, _: vImage_Flags, _: UnsafeMutablePointer<vImage_Error>) -> Unmanaged<CGColorSpace>!](https://developer.apple.com/documentation/accelerate/1498186-vimagecreatemonochromecolorspace)Added [vImageMatrixMultiply_ARGB8888ToPlanar8(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafePointer<Int16>, _: Int32, _: UnsafePointer<Int16>, _: Int32, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1546979-vimagematrixmultiply_argb8888top)Added [vImageMatrixMultiply_ARGBFFFFToPlanarF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafePointer<Float>, _: UnsafePointer<Float>, _: Float, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1546678-vimagematrixmultiply_argbfffftop)Added [vImagePremultipliedAlphaBlendDarken_RGBA8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1410644-vimagepremultipliedalphablenddar)Added [vImagePremultipliedAlphaBlendLighten_RGBA8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1410672-vimagepremultipliedalphablendlig)Added [vImagePremultipliedAlphaBlendMultiply_RGBA8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1410664-vimagepremultipliedalphablendmul)Added [vImagePremultipliedAlphaBlendScreen_RGBA8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1410729-vimagepremultipliedalphablendscr)Added [vImageSymmetricPiecewisePolynomial_PlanarF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<UnsafePointer<Float>>, _: UnsafePointer<Float>, _: UInt32, _: UInt32, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1544253-vimagesymmetricpiecewisepolynomi)Modified CBLAS_DIAG [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBLAS_DIAG {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct CBLAS_DIAG : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified CBLAS_ORDER [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBLAS_ORDER {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct CBLAS_ORDER : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified CBLAS_SIDE [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBLAS_SIDE {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct CBLAS_SIDE : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified CBLAS_TRANSPOSE [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBLAS_TRANSPOSE {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct CBLAS_TRANSPOSE : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified CBLAS_UPLO [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBLAS_UPLO {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct CBLAS_UPLO : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [DSPDoubleSplitComplex [struct]](https://developer.apple.com/documentation/accelerate/dspdoublesplitcomplex)

|  | Declaration |
| --- | --- |
| From | ``` struct DSPDoubleSplitComplex {     var realp: UnsafeMutablePointer<Double>     var imagp: UnsafeMutablePointer<Double>     init()     init(realp realp: UnsafeMutablePointer<Double>, imagp imagp: UnsafeMutablePointer<Double>) } ``` |
| To | ``` struct DSPDoubleSplitComplex {     var realp: UnsafeMutablePointer<Double>     var imagp: UnsafeMutablePointer<Double> } ``` |

Modified [DSPSplitComplex [struct]](https://developer.apple.com/documentation/accelerate/dspsplitcomplex)

|  | Declaration |
| --- | --- |
| From | ``` struct DSPSplitComplex {     var realp: UnsafeMutablePointer<Float>     var imagp: UnsafeMutablePointer<Float>     init()     init(realp realp: UnsafeMutablePointer<Float>, imagp imagp: UnsafeMutablePointer<Float>) } ``` |
| To | ``` struct DSPSplitComplex {     var realp: UnsafeMutablePointer<Float>     var imagp: UnsafeMutablePointer<Float> } ``` |

Modified OS_la_object

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_la_object { } ``` | -- |
| To | ``` protocol OS_la_object : NSObjectProtocol { } ``` | NSObjectProtocol |

Modified [vImage_CGImageFormat [struct]](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified [vImage_CGImageFormat.bitmapInfo](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/1399030-bitmapinfo)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [vImage_CGImageFormat.bitsPerComponent](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/1399086-bitspercomponent)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [vImage_CGImageFormat.bitsPerPixel](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/1399088-bitsperpixel)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [vImage_CGImageFormat.colorSpace](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/1399048-colorspace)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [vImage_CGImageFormat.decode](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/1399034-decode)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified vImage_CGImageFormat.init(bitsPerComponent: UInt32, bitsPerPixel: UInt32, colorSpace: Unmanaged<CGColorSpace>!, bitmapInfo: CGBitmapInfo, version: UInt32, decode: UnsafePointer<CGFloat>, renderingIntent: CGColorRenderingIntent)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified [vImage_CGImageFormat.renderingIntent](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/1399022-renderingintent)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [vImage_CGImageFormat.version](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/1399090-version)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [vImage_InterpolationMethod [struct]](https://developer.apple.com/documentation/accelerate/vimage_interpolationmethod)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct vImage_InterpolationMethod {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct vImage_InterpolationMethod : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [vImageARGBType [struct]](https://developer.apple.com/documentation/accelerate/vimageargbtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct vImageARGBType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct vImageARGBType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [vImageMDTableUsageHint [struct]](https://developer.apple.com/documentation/accelerate/vimagemdtableusagehint)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct vImageMDTableUsageHint {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct vImageMDTableUsageHint : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [vImageYpCbCrType [struct]](https://developer.apple.com/documentation/accelerate/vimageypcbcrtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct vImageYpCbCrType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct vImageYpCbCrType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [BLASParamErrorProc](https://developer.apple.com/documentation/accelerate/blasparamerrorproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias BLASParamErrorProc = CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int32>, UnsafePointer<Int32>) -> Void)> ``` |
| To | ``` typealias BLASParamErrorProc = (UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int32>, UnsafePointer<Int32>) -> Void ``` |

Modified cgees_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgees_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_complex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __w: UnsafeMutablePointer<__CLPK_complex>, _ __vs: UnsafeMutablePointer<__CLPK_complex>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_complex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_real>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func cgees_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp!, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_complex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __w: UnsafeMutablePointer<__CLPK_complex>, _ __vs: UnsafeMutablePointer<__CLPK_complex>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_complex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_real>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified cgeesx_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgeesx_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_complex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __w: UnsafeMutablePointer<__CLPK_complex>, _ __vs: UnsafeMutablePointer<__CLPK_complex>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_real>, _ __rcondv: UnsafeMutablePointer<__CLPK_real>, _ __work: UnsafeMutablePointer<__CLPK_complex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_real>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func cgeesx_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp!, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_complex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __w: UnsafeMutablePointer<__CLPK_complex>, _ __vs: UnsafeMutablePointer<__CLPK_complex>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_real>, _ __rcondv: UnsafeMutablePointer<__CLPK_real>, _ __work: UnsafeMutablePointer<__CLPK_complex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_real>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified cgges_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgges_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_complex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_complex>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alpha: UnsafeMutablePointer<__CLPK_complex>, _ __beta: UnsafeMutablePointer<__CLPK_complex>, _ __vsl: UnsafeMutablePointer<__CLPK_complex>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_complex>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_complex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_real>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func cgges_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp!, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_complex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_complex>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alpha: UnsafeMutablePointer<__CLPK_complex>, _ __beta: UnsafeMutablePointer<__CLPK_complex>, _ __vsl: UnsafeMutablePointer<__CLPK_complex>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_complex>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_complex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_real>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified cggesx_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_complex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cggesx_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_complex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_complex>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alpha: UnsafeMutablePointer<__CLPK_complex>, _ __beta: UnsafeMutablePointer<__CLPK_complex>, _ __vsl: UnsafeMutablePointer<__CLPK_complex>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_complex>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_real>, _ __rcondv: UnsafeMutablePointer<__CLPK_real>, _ __work: UnsafeMutablePointer<__CLPK_complex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_real>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func cggesx_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp!, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_complex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_complex>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alpha: UnsafeMutablePointer<__CLPK_complex>, _ __beta: UnsafeMutablePointer<__CLPK_complex>, _ __vsl: UnsafeMutablePointer<__CLPK_complex>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_complex>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_real>, _ __rcondv: UnsafeMutablePointer<__CLPK_real>, _ __work: UnsafeMutablePointer<__CLPK_complex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_real>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified dgees_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dgees_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublereal>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __wr: UnsafeMutablePointer<__CLPK_doublereal>, _ __wi: UnsafeMutablePointer<__CLPK_doublereal>, _ __vs: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_doublereal>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func dgees_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp!, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublereal>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __wr: UnsafeMutablePointer<__CLPK_doublereal>, _ __wi: UnsafeMutablePointer<__CLPK_doublereal>, _ __vs: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_doublereal>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified dgeesx_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dgeesx_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublereal>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __wr: UnsafeMutablePointer<__CLPK_doublereal>, _ __wi: UnsafeMutablePointer<__CLPK_doublereal>, _ __vs: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_doublereal>, _ __rcondv: UnsafeMutablePointer<__CLPK_doublereal>, _ __work: UnsafeMutablePointer<__CLPK_doublereal>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func dgeesx_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp!, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublereal>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __wr: UnsafeMutablePointer<__CLPK_doublereal>, _ __wi: UnsafeMutablePointer<__CLPK_doublereal>, _ __vs: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_doublereal>, _ __rcondv: UnsafeMutablePointer<__CLPK_doublereal>, _ __work: UnsafeMutablePointer<__CLPK_doublereal>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified dgges_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dgges_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublereal>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alphar: UnsafeMutablePointer<__CLPK_doublereal>, _ __alphai: UnsafeMutablePointer<__CLPK_doublereal>, _ __beta: UnsafeMutablePointer<__CLPK_doublereal>, _ __vsl: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_doublereal>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func dgges_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp!, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublereal>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alphar: UnsafeMutablePointer<__CLPK_doublereal>, _ __alphai: UnsafeMutablePointer<__CLPK_doublereal>, _ __beta: UnsafeMutablePointer<__CLPK_doublereal>, _ __vsl: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_doublereal>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified dggesx_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dggesx_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublereal>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alphar: UnsafeMutablePointer<__CLPK_doublereal>, _ __alphai: UnsafeMutablePointer<__CLPK_doublereal>, _ __beta: UnsafeMutablePointer<__CLPK_doublereal>, _ __vsl: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_doublereal>, _ __rcondv: UnsafeMutablePointer<__CLPK_doublereal>, _ __work: UnsafeMutablePointer<__CLPK_doublereal>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func dggesx_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp!, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublereal>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alphar: UnsafeMutablePointer<__CLPK_doublereal>, _ __alphai: UnsafeMutablePointer<__CLPK_doublereal>, _ __beta: UnsafeMutablePointer<__CLPK_doublereal>, _ __vsl: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_doublereal>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_doublereal>, _ __rcondv: UnsafeMutablePointer<__CLPK_doublereal>, _ __work: UnsafeMutablePointer<__CLPK_doublereal>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified la_deallocator_t

|  | Declaration |
| --- | --- |
| From | ``` typealias la_deallocator_t = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias la_deallocator_t = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified la_matrix_from_double_buffer_nocopy(_: UnsafeMutablePointer<Double>, _: la_count_t, _: la_count_t, _: la_count_t, _: la_hint_t, _: la_deallocator_t!, _: la_attribute_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_matrix_from_double_buffer_nocopy(_ buffer: UnsafeMutablePointer<Double>, _ matrix_rows: la_count_t, _ matrix_cols: la_count_t, _ matrix_row_stride: la_count_t, _ matrix_hint: la_hint_t, _ deallocator: la_deallocator_t, _ attributes: la_attribute_t) -> la_object_t! ``` |
| To | ``` func la_matrix_from_double_buffer_nocopy(_ buffer: UnsafeMutablePointer<Double>, _ matrix_rows: la_count_t, _ matrix_cols: la_count_t, _ matrix_row_stride: la_count_t, _ matrix_hint: la_hint_t, _ deallocator: la_deallocator_t!, _ attributes: la_attribute_t) -> la_object_t! ``` |

Modified la_matrix_from_float_buffer_nocopy(_: UnsafeMutablePointer<Float>, _: la_count_t, _: la_count_t, _: la_count_t, _: la_hint_t, _: la_deallocator_t!, _: la_attribute_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_matrix_from_float_buffer_nocopy(_ buffer: UnsafeMutablePointer<Float>, _ matrix_rows: la_count_t, _ matrix_cols: la_count_t, _ matrix_row_stride: la_count_t, _ matrix_hint: la_hint_t, _ deallocator: la_deallocator_t, _ attributes: la_attribute_t) -> la_object_t! ``` |
| To | ``` func la_matrix_from_float_buffer_nocopy(_ buffer: UnsafeMutablePointer<Float>, _ matrix_rows: la_count_t, _ matrix_cols: la_count_t, _ matrix_row_stride: la_count_t, _ matrix_hint: la_hint_t, _ deallocator: la_deallocator_t!, _ attributes: la_attribute_t) -> la_object_t! ``` |

Modified la_object_t

|  | Declaration |
| --- | --- |
| From | ``` typealias la_object_t = NSObject ``` |
| To | ``` typealias la_object_t = OS_la_object ``` |

Modified [SetBLASParamErrorProc(_: BLASParamErrorProc!)](https://developer.apple.com/documentation/accelerate/1513246-setblasparamerrorproc)

|  | Declaration |
| --- | --- |
| From | ``` func SetBLASParamErrorProc(_ __ErrorProc: BLASParamErrorProc) ``` |
| To | ``` func SetBLASParamErrorProc(_ __ErrorProc: BLASParamErrorProc!) ``` |

Modified sgees_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sgees_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_real>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __wr: UnsafeMutablePointer<__CLPK_real>, _ __wi: UnsafeMutablePointer<__CLPK_real>, _ __vs: UnsafeMutablePointer<__CLPK_real>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_real>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func sgees_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp!, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_real>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __wr: UnsafeMutablePointer<__CLPK_real>, _ __wi: UnsafeMutablePointer<__CLPK_real>, _ __vs: UnsafeMutablePointer<__CLPK_real>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_real>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified sgeesx_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sgeesx_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_real>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __wr: UnsafeMutablePointer<__CLPK_real>, _ __wi: UnsafeMutablePointer<__CLPK_real>, _ __vs: UnsafeMutablePointer<__CLPK_real>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_real>, _ __rcondv: UnsafeMutablePointer<__CLPK_real>, _ __work: UnsafeMutablePointer<__CLPK_real>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func sgeesx_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp!, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_real>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __wr: UnsafeMutablePointer<__CLPK_real>, _ __wi: UnsafeMutablePointer<__CLPK_real>, _ __vs: UnsafeMutablePointer<__CLPK_real>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_real>, _ __rcondv: UnsafeMutablePointer<__CLPK_real>, _ __work: UnsafeMutablePointer<__CLPK_real>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified sgges_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sgges_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_real>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_real>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alphar: UnsafeMutablePointer<__CLPK_real>, _ __alphai: UnsafeMutablePointer<__CLPK_real>, _ __beta: UnsafeMutablePointer<__CLPK_real>, _ __vsl: UnsafeMutablePointer<__CLPK_real>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_real>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_real>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func sgges_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp!, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_real>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_real>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alphar: UnsafeMutablePointer<__CLPK_real>, _ __alphai: UnsafeMutablePointer<__CLPK_real>, _ __beta: UnsafeMutablePointer<__CLPK_real>, _ __vsl: UnsafeMutablePointer<__CLPK_real>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_real>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_real>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified sggesx_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_real>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sggesx_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_real>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_real>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alphar: UnsafeMutablePointer<__CLPK_real>, _ __alphai: UnsafeMutablePointer<__CLPK_real>, _ __beta: UnsafeMutablePointer<__CLPK_real>, _ __vsl: UnsafeMutablePointer<__CLPK_real>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_real>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_real>, _ __rcondv: UnsafeMutablePointer<__CLPK_real>, _ __work: UnsafeMutablePointer<__CLPK_real>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func sggesx_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp!, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_real>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_real>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alphar: UnsafeMutablePointer<__CLPK_real>, _ __alphai: UnsafeMutablePointer<__CLPK_real>, _ __beta: UnsafeMutablePointer<__CLPK_real>, _ __vsl: UnsafeMutablePointer<__CLPK_real>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_real>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_real>, _ __rcondv: UnsafeMutablePointer<__CLPK_real>, _ __work: UnsafeMutablePointer<__CLPK_real>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified [vDSP_fft3_zop(_: FFTSetup, _: UnsafePointer<DSPSplitComplex>, _: vDSP_Stride, _: UnsafePointer<DSPSplitComplex>, _: vDSP_Stride, _: vDSP_Length, _: FFTDirection)](https://developer.apple.com/documentation/accelerate/1450494-vdsp_fft3_zop)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [vDSP_fft3_zopD(_: FFTSetupD, _: UnsafePointer<DSPDoubleSplitComplex>, _: vDSP_Stride, _: UnsafePointer<DSPDoubleSplitComplex>, _: vDSP_Stride, _: vDSP_Length, _: FFTDirection)](https://developer.apple.com/documentation/accelerate/1450124-vdsp_fft3_zopd)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [vDSP_fft5_zop(_: FFTSetup, _: UnsafePointer<DSPSplitComplex>, _: vDSP_Stride, _: UnsafePointer<DSPSplitComplex>, _: vDSP_Stride, _: vDSP_Length, _: FFTDirection)](https://developer.apple.com/documentation/accelerate/1450044-vdsp_fft5_zop)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [vDSP_fft5_zopD(_: FFTSetupD, _: UnsafePointer<DSPDoubleSplitComplex>, _: vDSP_Stride, _: UnsafePointer<DSPDoubleSplitComplex>, _: vDSP_Stride, _: vDSP_Length, _: FFTDirection)](https://developer.apple.com/documentation/accelerate/1450738-vdsp_fft5_zopd)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [vImageAffineWarp_ARGB16S(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_AffineTransform>, _: UnsafePointer<Int16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509164-vimageaffinewarp_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarp_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform>, _ backColor: UnsafeMutablePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarp_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform>, _ backColor: UnsafePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarp_ARGB16U(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_AffineTransform>, _: UnsafePointer<UInt16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509156-vimageaffinewarp_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarp_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform>, _ backColor: UnsafeMutablePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarp_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform>, _ backColor: UnsafePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarp_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_AffineTransform>, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509182-vimageaffinewarp_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarp_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform>, _ backColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarp_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform>, _ backColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarp_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_AffineTransform>, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509245-vimageaffinewarp_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarp_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform>, _ backColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarp_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform>, _ backColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarpCG_ARGB16S(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_CGAffineTransform>, _: UnsafePointer<Int16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509246-vimageaffinewarpcg_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarpCG_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_CGAffineTransform>, _ backColor: UnsafeMutablePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarpCG_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_CGAffineTransform>, _ backColor: UnsafePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarpCG_ARGB16U(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_CGAffineTransform>, _: UnsafePointer<UInt16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509186-vimageaffinewarpcg_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarpCG_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_CGAffineTransform>, _ backColor: UnsafeMutablePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarpCG_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_CGAffineTransform>, _ backColor: UnsafePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarpCG_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_CGAffineTransform>, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509276-vimageaffinewarpcg_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarpCG_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_CGAffineTransform>, _ backColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarpCG_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_CGAffineTransform>, _ backColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarpCG_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_CGAffineTransform>, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509263-vimageaffinewarpcg_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarpCG_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_CGAffineTransform>, _ backColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarpCG_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_CGAffineTransform>, _ backColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarpD_ARGB16S(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_AffineTransform_Double>, _: UnsafePointer<Int16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509282-vimageaffinewarpd_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarpD_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform_Double>, _ backColor: UnsafeMutablePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarpD_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform_Double>, _ backColor: UnsafePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarpD_ARGB16U(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_AffineTransform_Double>, _: UnsafePointer<UInt16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509292-vimageaffinewarpd_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarpD_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform_Double>, _ backColor: UnsafeMutablePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarpD_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform_Double>, _ backColor: UnsafePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarpD_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_AffineTransform_Double>, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509211-vimageaffinewarpd_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarpD_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform_Double>, _ backColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarpD_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform_Double>, _ backColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageAffineWarpD_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: UnsafePointer<vImage_AffineTransform_Double>, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509214-vimageaffinewarpd_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageAffineWarpD_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform_Double>, _ backColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageAffineWarpD_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ transform: UnsafePointer<vImage_AffineTransform_Double>, _ backColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageBoxConvolve_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: vImagePixelCount, _: vImagePixelCount, _: UInt32, _: UInt32, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1515945-vimageboxconvolve_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageBoxConvolve_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel_height: UInt32, _ kernel_width: UInt32, _ backgroundColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageBoxConvolve_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel_height: UInt32, _ kernel_width: UInt32, _ backgroundColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageCGImageFormat_IsEqual(_: UnsafePointer<vImage_CGImageFormat>, _: UnsafePointer<vImage_CGImageFormat>) -> Bool](https://developer.apple.com/documentation/accelerate/1399126-vimagecgimageformat_isequal)

|  | Declaration |
| --- | --- |
| From | ``` func vImageCGImageFormat_IsEqual(_ f1: UnsafePointer<vImage_CGImageFormat>, _ f2: UnsafePointer<vImage_CGImageFormat>) -> Boolean ``` |
| To | ``` func vImageCGImageFormat_IsEqual(_ f1: UnsafePointer<vImage_CGImageFormat>, _ f2: UnsafePointer<vImage_CGImageFormat>) -> Bool ``` |

Modified [vImageConvolve_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: vImagePixelCount, _: vImagePixelCount, _: UnsafePointer<Int16>, _: UInt32, _: UInt32, _: Int32, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1515923-vimageconvolve_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvolve_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Int16>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ divisor: Int32, _ backgroundColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvolve_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Int16>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ divisor: Int32, _ backgroundColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageConvolve_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: vImagePixelCount, _: vImagePixelCount, _: UnsafePointer<Float>, _: UInt32, _: UInt32, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1515929-vimageconvolve_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvolve_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Float>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ backgroundColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvolve_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Float>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ backgroundColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageConvolveMultiKernel_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: vImagePixelCount, _: vImagePixelCount, _: UnsafeMutablePointer<UnsafePointer<Int16>>, _: UInt32, _: UInt32, _: UnsafePointer<Int32>, _: UnsafePointer<Int32>, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1515930-vimageconvolvemultikernel_argb88)

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvolveMultiKernel_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernels: UnsafeMutablePointer<UnsafePointer<Int16>>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ divisors: UnsafePointer<Int32>, _ biases: UnsafePointer<Int32>, _ backgroundColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvolveMultiKernel_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernels: UnsafeMutablePointer<UnsafePointer<Int16>>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ divisors: UnsafePointer<Int32>, _ biases: UnsafePointer<Int32>, _ backgroundColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageConvolveMultiKernel_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: vImagePixelCount, _: vImagePixelCount, _: UnsafeMutablePointer<UnsafePointer<Float>>, _: UInt32, _: UInt32, _: UnsafePointer<Float>, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1515931-vimageconvolvemultikernel_argbff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvolveMultiKernel_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernels: UnsafeMutablePointer<UnsafePointer<Float>>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ biases: UnsafePointer<Float>, _ backgroundColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvolveMultiKernel_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernels: UnsafeMutablePointer<UnsafePointer<Float>>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ biases: UnsafePointer<Float>, _ backgroundColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageConvolveWithBias_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: vImagePixelCount, _: vImagePixelCount, _: UnsafePointer<Int16>, _: UInt32, _: UInt32, _: Int32, _: Int32, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1515933-vimageconvolvewithbias_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvolveWithBias_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Int16>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ divisor: Int32, _ bias: Int32, _ backgroundColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvolveWithBias_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Int16>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ divisor: Int32, _ bias: Int32, _ backgroundColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageConvolveWithBias_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: vImagePixelCount, _: vImagePixelCount, _: UnsafePointer<Float>, _: UInt32, _: UInt32, _: Float, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1515924-vimageconvolvewithbias_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvolveWithBias_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Float>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ bias: Float, _ backgroundColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvolveWithBias_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Float>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ bias: Float, _ backgroundColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageCreateCGImageFromBuffer(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_CGImageFormat>, _: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!, _: UnsafeMutablePointer<Void>, _: vImage_Flags, _: UnsafeMutablePointer<vImage_Error>) -> Unmanaged<CGImage>!](https://developer.apple.com/documentation/accelerate/1399036-vimagecreatecgimagefrombuffer)

|  | Declaration |
| --- | --- |
| From | ``` func vImageCreateCGImageFromBuffer(_ buf: UnsafePointer<vImage_Buffer>, _ format: UnsafePointer<vImage_CGImageFormat>, _ callback: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)>, _ userData: UnsafeMutablePointer<Void>, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>) -> Unmanaged<CGImage>! ``` |
| To | ``` func vImageCreateCGImageFromBuffer(_ buf: UnsafePointer<vImage_Buffer>, _ format: UnsafePointer<vImage_CGImageFormat>, _ callback: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!, _ userData: UnsafeMutablePointer<Void>, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>) -> Unmanaged<CGImage>! ``` |

Modified [vImageCVImageFormat_SetUserData(_: vImageCVImageFormat, _: UnsafeMutablePointer<Void>, _: ((vImageCVImageFormat!, UnsafeMutablePointer<Void>) -> Void)!) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1498220-vimagecvimageformat_setuserdata)

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_SetUserData(_ format: vImageCVImageFormat, _ userData: UnsafeMutablePointer<Void>, _ userDataReleaseCallback: CFunctionPointer<((vImageCVImageFormat!, UnsafeMutablePointer<Void>) -> Void)>) -> vImage_Error ``` |
| To | ``` func vImageCVImageFormat_SetUserData(_ format: vImageCVImageFormat, _ userData: UnsafeMutablePointer<Void>, _ userDataReleaseCallback: ((vImageCVImageFormat!, UnsafeMutablePointer<Void>) -> Void)!) -> vImage_Error ``` |

Modified [vImageGetResamplingFilterSize(_: Float, _: ((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)!, _: Float, _: vImage_Flags) -> Int](https://developer.apple.com/documentation/accelerate/1509252-vimagegetresamplingfiltersize)

|  | Declaration |
| --- | --- |
| From | ``` func vImageGetResamplingFilterSize(_ scale: Float, _ kernelFunc: CFunctionPointer<((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)>, _ kernelWidth: Float, _ flags: vImage_Flags) -> Int ``` |
| To | ``` func vImageGetResamplingFilterSize(_ scale: Float, _ kernelFunc: ((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)!, _ kernelWidth: Float, _ flags: vImage_Flags) -> Int ``` |

Modified [vImageHorizontalShear_ARGB16S(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Float, _: Float, _: ResamplingFilter, _: UnsafePointer<Int16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509194-vimagehorizontalshear_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` func vImageHorizontalShear_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageHorizontalShear_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageHorizontalShear_ARGB16U(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Float, _: Float, _: ResamplingFilter, _: UnsafePointer<UInt16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509274-vimagehorizontalshear_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` func vImageHorizontalShear_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageHorizontalShear_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageHorizontalShear_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Float, _: Float, _: ResamplingFilter, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509237-vimagehorizontalshear_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageHorizontalShear_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageHorizontalShear_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageHorizontalShear_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Float, _: Float, _: ResamplingFilter, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509273-vimagehorizontalshear_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageHorizontalShear_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageHorizontalShear_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageHorizontalShearD_ARGB16S(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Double, _: Double, _: ResamplingFilter, _: UnsafePointer<Int16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509268-vimagehorizontalsheard_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` func vImageHorizontalShearD_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageHorizontalShearD_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageHorizontalShearD_ARGB16U(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Double, _: Double, _: ResamplingFilter, _: UnsafePointer<UInt16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509248-vimagehorizontalsheard_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` func vImageHorizontalShearD_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageHorizontalShearD_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageHorizontalShearD_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Double, _: Double, _: ResamplingFilter, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509178-vimagehorizontalsheard_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageHorizontalShearD_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageHorizontalShearD_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageHorizontalShearD_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Double, _: Double, _: ResamplingFilter, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509269-vimagehorizontalsheard_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageHorizontalShearD_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageHorizontalShearD_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageMultidimensionalTable_Create(_: UnsafePointer<UInt16>, _: UInt32, _: UInt32, _: UnsafePointer<UInt8>, _: vImageMDTableUsageHint, _: vImage_Flags, _: UnsafeMutablePointer<vImage_Error>) -> vImage_MultidimensionalTable](https://developer.apple.com/documentation/accelerate/1544435-vimagemultidimensionaltable_crea)

|  | Declaration |
| --- | --- |
| From | ``` func vImageMultidimensionalTable_Create(_ tableData: UnsafePointer<UInt16>, _ numSrcChannels: UInt32, _ numDestChannels: UInt32, _ table_entries_per_dimension: UnsafeMutablePointer<UInt8>, _ hint: vImageMDTableUsageHint, _ flags: vImage_Flags, _ err: UnsafeMutablePointer<vImage_Error>) -> vImage_MultidimensionalTable ``` |
| To | ``` func vImageMultidimensionalTable_Create(_ tableData: UnsafePointer<UInt16>, _ numSrcChannels: UInt32, _ numDestChannels: UInt32, _ table_entries_per_dimension: UnsafePointer<UInt8>, _ hint: vImageMDTableUsageHint, _ flags: vImage_Flags, _ err: UnsafeMutablePointer<vImage_Error>) -> vImage_MultidimensionalTable ``` |

Modified [vImageNewResamplingFilterForFunctionUsingBuffer(_: ResamplingFilter, _: Float, _: ((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)!, _: Float, _: UnsafeMutablePointer<Void>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509217-vimagenewresamplingfilterforfunc)

|  | Declaration |
| --- | --- |
| From | ``` func vImageNewResamplingFilterForFunctionUsingBuffer(_ filter: ResamplingFilter, _ scale: Float, _ kernelFunc: CFunctionPointer<((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)>, _ kernelWidth: Float, _ userData: UnsafeMutablePointer<Void>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageNewResamplingFilterForFunctionUsingBuffer(_ filter: ResamplingFilter, _ scale: Float, _ kernelFunc: ((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)!, _ kernelWidth: Float, _ userData: UnsafeMutablePointer<Void>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageRichardsonLucyDeConvolve_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: vImagePixelCount, _: vImagePixelCount, _: UnsafePointer<Int16>, _: UnsafePointer<Int16>, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: Int32, _: Int32, _: UnsafePointer<UInt8>, _: UInt32, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1515928-vimagerichardsonlucydeconvolve_a)

|  | Declaration |
| --- | --- |
| From | ``` func vImageRichardsonLucyDeConvolve_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Int16>, _ kernel2: UnsafePointer<Int16>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ kernel_height2: UInt32, _ kernel_width2: UInt32, _ divisor: Int32, _ divisor2: Int32, _ backgroundColor: UnsafeMutablePointer<UInt8>, _ iterationCount: UInt32, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageRichardsonLucyDeConvolve_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Int16>, _ kernel2: UnsafePointer<Int16>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ kernel_height2: UInt32, _ kernel_width2: UInt32, _ divisor: Int32, _ divisor2: Int32, _ backgroundColor: UnsafePointer<UInt8>, _ iterationCount: UInt32, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageRichardsonLucyDeConvolve_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: vImagePixelCount, _: vImagePixelCount, _: UnsafePointer<Float>, _: UnsafePointer<Float>, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UnsafePointer<Float>, _: UInt32, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1515927-vimagerichardsonlucydeconvolve_a)

|  | Declaration |
| --- | --- |
| From | ``` func vImageRichardsonLucyDeConvolve_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Float>, _ kernel2: UnsafePointer<Float>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ kernel_height2: UInt32, _ kernel_width2: UInt32, _ backgroundColor: UnsafeMutablePointer<Float>, _ iterationCount: UInt32, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageRichardsonLucyDeConvolve_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Float>, _ kernel2: UnsafePointer<Float>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ kernel_height2: UInt32, _ kernel_width2: UInt32, _ backgroundColor: UnsafePointer<Float>, _ iterationCount: UInt32, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageRotate_ARGB16S(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: Float, _: UnsafePointer<Int16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509206-vimagerotate_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` func vImageRotate_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ angleInRadians: Float, _ backColor: UnsafeMutablePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageRotate_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ angleInRadians: Float, _ backColor: UnsafePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageRotate_ARGB16U(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: Float, _: UnsafePointer<UInt16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509235-vimagerotate_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` func vImageRotate_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ angleInRadians: Float, _ backColor: UnsafeMutablePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageRotate_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ angleInRadians: Float, _ backColor: UnsafePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageRotate_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: Float, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509284-vimagerotate_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageRotate_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ angleInRadians: Float, _ backColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageRotate_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ angleInRadians: Float, _ backColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageRotate_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: Float, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509192-vimagerotate_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageRotate_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ angleInRadians: Float, _ backColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageRotate_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ angleInRadians: Float, _ backColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageTentConvolve_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafeMutablePointer<Void>, _: vImagePixelCount, _: vImagePixelCount, _: UInt32, _: UInt32, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1515935-vimagetentconvolve_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageTentConvolve_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel_height: UInt32, _ kernel_width: UInt32, _ backgroundColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageTentConvolve_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel_height: UInt32, _ kernel_width: UInt32, _ backgroundColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageVerticalShear_ARGB16S(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Float, _: Float, _: ResamplingFilter, _: UnsafePointer<Int16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509154-vimageverticalshear_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` func vImageVerticalShear_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageVerticalShear_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageVerticalShear_ARGB16U(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Float, _: Float, _: ResamplingFilter, _: UnsafePointer<UInt16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509227-vimageverticalshear_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` func vImageVerticalShear_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageVerticalShear_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageVerticalShear_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Float, _: Float, _: ResamplingFilter, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509256-vimageverticalshear_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageVerticalShear_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageVerticalShear_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageVerticalShear_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Float, _: Float, _: ResamplingFilter, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509261-vimageverticalshear_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageVerticalShear_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageVerticalShear_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter, _ backColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageVerticalShearD_ARGB16S(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Double, _: Double, _: ResamplingFilter, _: UnsafePointer<Int16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509278-vimageverticalsheard_argb16s)

|  | Declaration |
| --- | --- |
| From | ``` func vImageVerticalShearD_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageVerticalShearD_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageVerticalShearD_ARGB16U(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Double, _: Double, _: ResamplingFilter, _: UnsafePointer<UInt16>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509225-vimageverticalsheard_argb16u)

|  | Declaration |
| --- | --- |
| From | ``` func vImageVerticalShearD_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageVerticalShearD_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageVerticalShearD_ARGB8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Double, _: Double, _: ResamplingFilter, _: UnsafePointer<UInt8>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509222-vimageverticalsheard_argb8888)

|  | Declaration |
| --- | --- |
| From | ``` func vImageVerticalShearD_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageVerticalShearD_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified [vImageVerticalShearD_ARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImagePixelCount, _: vImagePixelCount, _: Double, _: Double, _: ResamplingFilter, _: UnsafePointer<Float>, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509254-vimageverticalsheard_argbffff)

|  | Declaration |
| --- | --- |
| From | ``` func vImageVerticalShearD_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafeMutablePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageVerticalShearD_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter, _ backColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified zgees_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func zgees_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __w: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __vs: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_doublereal>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func zgees_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp!, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __w: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __vs: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_doublereal>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified zgeesx_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func zgeesx_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __w: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __vs: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_doublereal>, _ __rcondv: UnsafeMutablePointer<__CLPK_doublereal>, _ __work: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_doublereal>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func zgeesx_(_ __jobvs: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __select: __CLPK_L_fp!, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __w: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __vs: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvs: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_doublereal>, _ __rcondv: UnsafeMutablePointer<__CLPK_doublereal>, _ __work: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_doublereal>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified zgges_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func zgges_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alpha: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __beta: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __vsl: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_doublereal>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func zgges_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp!, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alpha: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __beta: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __vsl: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __work: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_doublereal>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

Modified zggesx_(_: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: __CLPK_L_fp!, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_doublecomplex>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_doublereal>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_integer>, _: UnsafeMutablePointer<__CLPK_logical>, _: UnsafeMutablePointer<__CLPK_integer>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func zggesx_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alpha: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __beta: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __vsl: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_doublereal>, _ __rcondv: UnsafeMutablePointer<__CLPK_doublereal>, _ __work: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_doublereal>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |
| To | ``` func zggesx_(_ __jobvsl: UnsafeMutablePointer<Int8>, _ __jobvsr: UnsafeMutablePointer<Int8>, _ __sort: UnsafeMutablePointer<Int8>, _ __selctg: __CLPK_L_fp!, _ __sense: UnsafeMutablePointer<Int8>, _ __n: UnsafeMutablePointer<__CLPK_integer>, _ __a: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lda: UnsafeMutablePointer<__CLPK_integer>, _ __b: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldb: UnsafeMutablePointer<__CLPK_integer>, _ __sdim: UnsafeMutablePointer<__CLPK_integer>, _ __alpha: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __beta: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __vsl: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvsl: UnsafeMutablePointer<__CLPK_integer>, _ __vsr: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __ldvsr: UnsafeMutablePointer<__CLPK_integer>, _ __rconde: UnsafeMutablePointer<__CLPK_doublereal>, _ __rcondv: UnsafeMutablePointer<__CLPK_doublereal>, _ __work: UnsafeMutablePointer<__CLPK_doublecomplex>, _ __lwork: UnsafeMutablePointer<__CLPK_integer>, _ __rwork: UnsafeMutablePointer<__CLPK_doublereal>, _ __iwork: UnsafeMutablePointer<__CLPK_integer>, _ __liwork: UnsafeMutablePointer<__CLPK_integer>, _ __bwork: UnsafeMutablePointer<__CLPK_logical>, _ __info: UnsafeMutablePointer<__CLPK_integer>) -> Int32 ``` |

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
