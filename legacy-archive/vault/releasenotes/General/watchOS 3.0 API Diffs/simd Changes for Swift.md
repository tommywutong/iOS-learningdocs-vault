---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Swift/simd.html
archived_at: '2026-07-18T02:58:36.669170Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# simd Changes for Swift

### simd

Removed matrix_from_columns(_: vector_float2, _: vector_float2) -> matrix_float2x2Removed matrix_from_diagonal(_: vector_float2) -> matrix_float2x2Removed matrix_from_rows(_: vector_float2, _: vector_float2) -> matrix_float2x2Removed [matrix_multiply(_: matrix_float2x2, _: vector_float2) -> vector_float2](https://developer.apple.com/documentation/simd/1417858-matrix_multiply)Removed vector_abs(_: vector_int2) -> vector_int2Removed vector_all(_: vector_int2) -> BoolRemoved vector_any(_: vector_int2) -> BoolRemoved vector_bitselect(_: vector_int2, _: vector_int2, _: vector_int2) -> vector_int2Removed vector_clamp(_: vector_int2, _: vector_int2, _: vector_int2) -> vector_int2Removed vector_cross(_: vector_float2, _: vector_float2) -> vector_float3Removed vector_distance(_: vector_float2, _: vector_float2) -> FloatRemoved vector_distance_squared(_: vector_float2, _: vector_float2) -> FloatRemoved vector_dot(_: vector_float2, _: vector_float2) -> FloatRemoved vector_double(_: vector_int2) -> vector_double2Removed vector_fast_distance(_: vector_float2, _: vector_float2) -> FloatRemoved vector_fast_length(_: vector_float2) -> FloatRemoved vector_fast_normalize(_: vector_float2) -> vector_float2Removed vector_fast_project(_: vector_float2, _: vector_float2) -> vector_float2Removed vector_float(_: vector_int2) -> vector_float2Removed vector_int(_: vector_int2) -> vector_int2Removed vector_int_sat(_: vector_int2) -> vector_int2Removed vector_length(_: vector_float2) -> FloatRemoved vector_length_squared(_: vector_float2) -> FloatRemoved vector_max(_: vector_int2, _: vector_int2) -> vector_int2Removed vector_min(_: vector_int2, _: vector_int2) -> vector_int2Removed vector_norm_inf(_: vector_float2) -> FloatRemoved vector_norm_one(_: vector_float2) -> FloatRemoved vector_normalize(_: vector_float2) -> vector_float2Removed vector_precise_distance(_: vector_float2, _: vector_float2) -> FloatRemoved vector_precise_length(_: vector_float2) -> FloatRemoved vector_precise_normalize(_: vector_float2) -> vector_float2Removed vector_precise_project(_: vector_float2, _: vector_float2) -> vector_float2Removed vector_project(_: vector_float2, _: vector_float2) -> vector_float2Removed vector_reduce_add(_: vector_int2) -> Int32Removed vector_reduce_max(_: vector_int2) -> Int32Removed vector_reduce_min(_: vector_int2) -> Int32Removed vector_reflect(_: vector_float2, _: vector_float2) -> vector_float2Removed vector_refract(_: vector_float2, _: vector_float2, _: Float) -> vector_float2Removed vector_select(_: vector_float2, _: vector_float2, _: vector_int2) -> vector_float2Added [uint2 [struct]](https://developer.apple.com/documentation/simd/uint2)Added [uint2.debugDescription](https://developer.apple.com/documentation/simd/uint2/1690550-debugdescription)Added [uint2.init()](https://developer.apple.com/documentation/simd/uint2/1690592-init)Added [uint2.init(_: [UInt32])](https://developer.apple.com/documentation/simd/uint2/1690515-init)Added [uint2.init(_: UInt32)](https://developer.apple.com/documentation/simd/uint2/1690520-init)Added [uint2.init(_: UInt32, _: UInt32)](https://developer.apple.com/documentation/simd/uint2/1690554-init)Added [uint2.init(arrayLiteral: UInt32)](https://developer.apple.com/documentation/simd/uint2/1690549-init)Added [uint2.init(x: UInt32, y: UInt32)](https://developer.apple.com/documentation/simd/uint2/1690571-init)Added [uint2.subscript(_: Int) -> UInt32](https://developer.apple.com/documentation/simd/uint2/1690541-subscript)Added [uint2.x](https://developer.apple.com/documentation/simd/uint2/1690517-x)Added [uint2.y](https://developer.apple.com/documentation/simd/uint2/1690514-y)Added [uint3 [struct]](https://developer.apple.com/documentation/simd/uint3)Added [uint3.debugDescription](https://developer.apple.com/documentation/simd/uint3/1690525-debugdescription)Added [uint3.init()](https://developer.apple.com/documentation/simd/uint3/1690518-init)Added [uint3.init(_: UInt32)](https://developer.apple.com/documentation/simd/uint3/1690526-init)Added [uint3.init(_: [UInt32])](https://developer.apple.com/documentation/simd/uint3/1690593-init)Added [uint3.init(_: UInt32, _: UInt32, _: UInt32)](https://developer.apple.com/documentation/simd/uint3/1690509-init)Added [uint3.init(arrayLiteral: UInt32)](https://developer.apple.com/documentation/simd/uint3/1690547-init)Added [uint3.init(x: UInt32, y: UInt32, z: UInt32)](https://developer.apple.com/documentation/simd/uint3/1690529-init)Added [uint3.subscript(_: Int) -> UInt32](https://developer.apple.com/documentation/simd/uint3/1690580-subscript)Added [uint3.x](https://developer.apple.com/documentation/simd/uint3/1690512-x)Added [uint3.y](https://developer.apple.com/documentation/simd/uint3/1690510-y)Added [uint3.z](https://developer.apple.com/documentation/simd/uint3/1690566-z)Added [uint4 [struct]](https://developer.apple.com/documentation/simd/uint4)Added [uint4.debugDescription](https://developer.apple.com/documentation/simd/uint4/1690548-debugdescription)Added [uint4.init()](https://developer.apple.com/documentation/simd/uint4/1690570-init)Added [uint4.init(_: UInt32)](https://developer.apple.com/documentation/simd/uint4/1690583-init)Added [uint4.init(_: [UInt32])](https://developer.apple.com/documentation/simd/uint4/1690535-init)Added [uint4.init(_: UInt32, _: UInt32, _: UInt32, _: UInt32)](https://developer.apple.com/documentation/simd/uint4/1690540-init)Added [uint4.init(arrayLiteral: UInt32)](https://developer.apple.com/documentation/simd/uint4/1690531-init)Added [uint4.init(x: UInt32, y: UInt32, z: UInt32, w: UInt32)](https://developer.apple.com/documentation/simd/uint4/1690551-init)Added [uint4.subscript(_: Int) -> UInt32](https://developer.apple.com/documentation/simd/uint4/1690581-subscript)Added [uint4.w](https://developer.apple.com/documentation/simd/uint4/1690532-w)Added [uint4.x](https://developer.apple.com/documentation/simd/uint4/1690533-x)Added [uint4.y](https://developer.apple.com/documentation/simd/uint4/1690530-y)Added [uint4.z](https://developer.apple.com/documentation/simd/uint4/1690524-z)Added &\*(_: UInt32, _: uint3) -> uint3Added &\*(_: uint3, _: UInt32) -> uint3Added &\*(_: UInt32, _: uint4) -> uint4Added &\*(_: uint2, _: UInt32) -> uint2Added &\*(_: uint3, _: uint3) -> uint3Added &\*(_: uint2, _: uint2) -> uint2Added &\*(_: UInt32, _: uint2) -> uint2Added &\*(_: uint4, _: UInt32) -> uint4Added &\*(_: uint4, _: uint4) -> uint4Added &+(_: uint3, _: uint3) -> uint3Added &+(_: uint2, _: uint2) -> uint2Added &+(_: uint4, _: uint4) -> uint4Added &-(_: uint3, _: uint3) -> uint3Added &-(_: uint2, _: uint2) -> uint2Added &-(_: uint4, _: uint4) -> uint4Added -(_: uint2) -> uint2Added -(_: uint4) -> uint4Added -(_: uint3) -> uint3Added /(_: uint4, _: uint4) -> uint4Added /(_: uint3, _: uint3) -> uint3Added /(_: uint2, _: uint2) -> uint2Added /=(_: uint3, _: uint3)Added /=(_: uint2, _: uint2)Added /=(_: uint4, _: uint4)Added [clamp(_: uint2, min: uint2, max: uint2) -> uint2](https://developer.apple.com/documentation/simd/1690579-clamp)Added [clamp(_: uint3, min: UInt32, max: UInt32) -> uint3](https://developer.apple.com/documentation/simd/1690545-clamp)Added [clamp(_: uint3, min: uint3, max: uint3) -> uint3](https://developer.apple.com/documentation/simd/1690538-clamp)Added [clamp(_: uint2, min: UInt32, max: UInt32) -> uint2](https://developer.apple.com/documentation/simd/1690565-clamp)Added [clamp(_: uint4, min: UInt32, max: UInt32) -> uint4](https://developer.apple.com/documentation/simd/1690563-clamp)Added [clamp(_: uint4, min: uint4, max: uint4) -> uint4](https://developer.apple.com/documentation/simd/1690513-clamp)Added matrix_almost_equal_elements(_: matrix_float2x3, _: matrix_float2x3, _: Float) -> BoolAdded matrix_almost_equal_elements(_: matrix_double2x2, _: matrix_double2x2, _: Double) -> BoolAdded matrix_almost_equal_elements(_: matrix_double4x2, _: matrix_double4x2, _: Double) -> BoolAdded matrix_almost_equal_elements(_: matrix_float4x3, _: matrix_float4x3, _: Float) -> BoolAdded matrix_almost_equal_elements(_: matrix_double2x4, _: matrix_double2x4, _: Double) -> BoolAdded matrix_almost_equal_elements(_: matrix_double4x4, _: matrix_double4x4, _: Double) -> BoolAdded matrix_almost_equal_elements(_: matrix_float3x2, _: matrix_float3x2, _: Float) -> BoolAdded matrix_almost_equal_elements(_: matrix_double3x4, _: matrix_double3x4, _: Double) -> BoolAdded matrix_almost_equal_elements(_: matrix_double3x2, _: matrix_double3x2, _: Double) -> BoolAdded matrix_almost_equal_elements(_: matrix_double3x3, _: matrix_double3x3, _: Double) -> BoolAdded matrix_almost_equal_elements(_: matrix_double2x3, _: matrix_double2x3, _: Double) -> BoolAdded matrix_almost_equal_elements(_: matrix_float3x4, _: matrix_float3x4, _: Float) -> BoolAdded matrix_almost_equal_elements(_: matrix_float2x4, _: matrix_float2x4, _: Float) -> BoolAdded matrix_almost_equal_elements(_: matrix_double4x3, _: matrix_double4x3, _: Double) -> BoolAdded matrix_almost_equal_elements(_: matrix_float4x4, _: matrix_float4x4, _: Float) -> BoolAdded matrix_almost_equal_elements(_: matrix_float3x3, _: matrix_float3x3, _: Float) -> BoolAdded matrix_almost_equal_elements(_: matrix_float4x2, _: matrix_float4x2, _: Float) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_double3x2, _: matrix_double3x2, _: Double) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_double2x3, _: matrix_double2x3, _: Double) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_double2x2, _: matrix_double2x2, _: Double) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_double3x3, _: matrix_double3x3, _: Double) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_float3x4, _: matrix_float3x4, _: Float) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_double3x4, _: matrix_double3x4, _: Double) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_float4x4, _: matrix_float4x4, _: Float) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_float3x2, _: matrix_float3x2, _: Float) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_float3x3, _: matrix_float3x3, _: Float) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_double2x4, _: matrix_double2x4, _: Double) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_float4x3, _: matrix_float4x3, _: Float) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_double4x3, _: matrix_double4x3, _: Double) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_float4x2, _: matrix_float4x2, _: Float) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_float2x4, _: matrix_float2x4, _: Float) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_double4x2, _: matrix_double4x2, _: Double) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_double4x4, _: matrix_double4x4, _: Double) -> BoolAdded matrix_almost_equal_elements_relative(_: matrix_float2x3, _: matrix_float2x3, _: Float) -> BoolAdded matrix_determinant(_: matrix_float3x3) -> FloatAdded matrix_determinant(_: matrix_double2x2) -> DoubleAdded matrix_determinant(_: matrix_float4x4) -> FloatAdded matrix_determinant(_: matrix_double3x3) -> DoubleAdded matrix_determinant(_: matrix_double4x4) -> DoubleAdded matrix_equal(_: matrix_float2x3, _: matrix_float2x3) -> BoolAdded matrix_equal(_: matrix_float3x2, _: matrix_float3x2) -> BoolAdded matrix_equal(_: matrix_double2x3, _: matrix_double2x3) -> BoolAdded matrix_equal(_: matrix_float4x3, _: matrix_float4x3) -> BoolAdded matrix_equal(_: matrix_double2x2, _: matrix_double2x2) -> BoolAdded matrix_equal(_: matrix_double4x4, _: matrix_double4x4) -> BoolAdded matrix_equal(_: matrix_float2x4, _: matrix_float2x4) -> BoolAdded matrix_equal(_: matrix_double4x2, _: matrix_double4x2) -> BoolAdded matrix_equal(_: matrix_double4x3, _: matrix_double4x3) -> BoolAdded matrix_equal(_: matrix_float3x3, _: matrix_float3x3) -> BoolAdded matrix_equal(_: matrix_double2x4, _: matrix_double2x4) -> BoolAdded matrix_equal(_: matrix_float4x4, _: matrix_float4x4) -> BoolAdded matrix_equal(_: matrix_float3x4, _: matrix_float3x4) -> BoolAdded matrix_equal(_: matrix_double3x3, _: matrix_double3x3) -> BoolAdded matrix_equal(_: matrix_double3x2, _: matrix_double3x2) -> BoolAdded matrix_equal(_: matrix_float4x2, _: matrix_float4x2) -> BoolAdded matrix_equal(_: matrix_double3x4, _: matrix_double3x4) -> BoolAdded matrix_invert(_: matrix_double2x2) -> matrix_double2x2Added matrix_invert(_: matrix_float3x3) -> matrix_float3x3Added matrix_invert(_: matrix_float4x4) -> matrix_float4x4Added matrix_invert(_: matrix_double4x4) -> matrix_double4x4Added matrix_invert(_: matrix_double3x3) -> matrix_double3x3Added matrix_linear_combination(_: Float, _: matrix_float4x2, _: Float, _: matrix_float4x2) -> matrix_float4x2Added matrix_linear_combination(_: Float, _: matrix_float3x4, _: Float, _: matrix_float3x4) -> matrix_float3x4Added matrix_linear_combination(_: Double, _: matrix_double3x4, _: Double, _: matrix_double3x4) -> matrix_double3x4Added matrix_linear_combination(_: Double, _: matrix_double4x4, _: Double, _: matrix_double4x4) -> matrix_double4x4Added matrix_linear_combination(_: Float, _: matrix_float3x3, _: Float, _: matrix_float3x3) -> matrix_float3x3Added matrix_linear_combination(_: Float, _: matrix_float2x4, _: Float, _: matrix_float2x4) -> matrix_float2x4Added matrix_linear_combination(_: Double, _: matrix_double3x3, _: Double, _: matrix_double3x3) -> matrix_double3x3Added matrix_linear_combination(_: Double, _: matrix_double2x3, _: Double, _: matrix_double2x3) -> matrix_double2x3Added matrix_linear_combination(_: Double, _: matrix_double4x3, _: Double, _: matrix_double4x3) -> matrix_double4x3Added matrix_linear_combination(_: Float, _: matrix_float4x4, _: Float, _: matrix_float4x4) -> matrix_float4x4Added matrix_linear_combination(_: Double, _: matrix_double3x2, _: Double, _: matrix_double3x2) -> matrix_double3x2Added matrix_linear_combination(_: Float, _: matrix_float4x3, _: Float, _: matrix_float4x3) -> matrix_float4x3Added matrix_linear_combination(_: Double, _: matrix_double2x4, _: Double, _: matrix_double2x4) -> matrix_double2x4Added matrix_linear_combination(_: Float, _: matrix_float2x3, _: Float, _: matrix_float2x3) -> matrix_float2x3Added matrix_linear_combination(_: Double, _: matrix_double4x2, _: Double, _: matrix_double4x2) -> matrix_double4x2Added matrix_linear_combination(_: Double, _: matrix_double2x2, _: Double, _: matrix_double2x2) -> matrix_double2x2Added matrix_linear_combination(_: Float, _: matrix_float3x2, _: Float, _: matrix_float3x2) -> matrix_float3x2Added matrix_multiply(_: matrix_double2x4, _: matrix_double2x2) -> matrix_double2x4Added matrix_multiply(_: matrix_double3x3, _: matrix_double3x3) -> matrix_double3x3Added matrix_multiply(_: matrix_double2x4, _: matrix_double4x2) -> matrix_double4x4Added matrix_multiply(_: matrix_double2x3, _: matrix_double2x2) -> matrix_double2x3Added matrix_multiply(_: matrix_float3x4, _: matrix_float3x3) -> matrix_float3x4Added matrix_multiply(_: matrix_float4x4, _: matrix_float3x4) -> matrix_float3x4Added matrix_multiply(_: matrix_double4x4, _: matrix_double3x4) -> matrix_double3x4Added matrix_multiply(_: matrix_float2x2, _: matrix_float2x2) -> matrix_float2x2Added matrix_multiply(_: matrix_float2x3, _: matrix_float2x2) -> matrix_float2x3Added matrix_multiply(_: matrix_double4x2, _: matrix_double3x4) -> matrix_double3x2Added matrix_multiply(_: matrix_float2x4, _: matrix_float2x2) -> matrix_float2x4Added matrix_multiply(_: matrix_double3x4, _: matrix_double3x3) -> matrix_double3x4Added matrix_multiply(_: matrix_float3x3, _: matrix_float3x3) -> matrix_float3x3Added matrix_multiply(_: matrix_float2x3, _: matrix_float3x2) -> matrix_float3x3Added matrix_multiply(_: matrix_float3x4, _: matrix_float2x3) -> matrix_float2x4Added matrix_multiply(_: matrix_double4x2, _: matrix_double4x4) -> matrix_double4x2Added matrix_multiply(_: matrix_double2x2, _: matrix_double3x2) -> matrix_double3x2Added matrix_multiply(_: matrix_double3x2, _: matrix_double2x3) -> matrix_double2x2Added matrix_multiply(_: matrix_double3x3, _: matrix_double2x3) -> matrix_double2x3Added matrix_multiply(_: matrix_float2x4, _: matrix_float4x2) -> matrix_float4x4Added matrix_multiply(_: matrix_float3x2, _: matrix_float2x3) -> matrix_float2x2Added matrix_multiply(_: matrix_double3x4, _: matrix_double2x3) -> matrix_double2x4Added matrix_multiply(_: matrix_float4x4, _: matrix_float2x4) -> matrix_float2x4Added matrix_multiply(_: matrix_float4x2, _: matrix_float3x4) -> matrix_float3x2Added matrix_multiply(_: matrix_double2x3, _: matrix_double4x2) -> matrix_double4x3Added matrix_multiply(_: matrix_float4x2, _: matrix_float2x4) -> matrix_float2x2Added matrix_multiply(_: matrix_float4x2, _: matrix_float4x4) -> matrix_float4x2Added matrix_multiply(_: matrix_float2x3, _: matrix_float4x2) -> matrix_float4x3Added matrix_multiply(_: matrix_float3x3, _: matrix_float4x3) -> matrix_float4x3Added matrix_multiply(_: matrix_double4x2, _: matrix_double2x4) -> matrix_double2x2Added matrix_multiply(_: matrix_double4x3, _: matrix_double3x4) -> matrix_double3x3Added matrix_multiply(_: matrix_float4x3, _: matrix_float3x4) -> matrix_float3x3Added matrix_multiply(_: matrix_float3x2, _: matrix_float4x3) -> matrix_float4x2Added matrix_multiply(_: matrix_double2x3, _: matrix_double3x2) -> matrix_double3x3Added matrix_multiply(_: matrix_double3x2, _: matrix_double3x3) -> matrix_double3x2Added matrix_multiply(_: matrix_double2x4, _: matrix_double3x2) -> matrix_double3x4Added matrix_multiply(_: matrix_double3x3, _: matrix_double4x3) -> matrix_double4x3Added matrix_multiply(_: matrix_float4x4, _: matrix_float4x4) -> matrix_float4x4Added matrix_multiply(_: matrix_double2x2, _: matrix_double4x2) -> matrix_double4x2Added matrix_multiply(_: matrix_float4x3, _: matrix_float4x4) -> matrix_float4x3Added matrix_multiply(_: matrix_double4x3, _: matrix_double2x4) -> matrix_double2x3Added matrix_multiply(_: matrix_float3x4, _: matrix_float4x3) -> matrix_float4x4Added [matrix_multiply(_: matrix_float2x4, _: matrix_float3x2) -> matrix_float3x4](https://developer.apple.com/documentation/simd/1417858-matrix_multiply)Added matrix_multiply(_: matrix_float2x2, _: matrix_float4x2) -> matrix_float4x2Added matrix_multiply(_: matrix_float4x3, _: matrix_float2x4) -> matrix_float2x3Added matrix_multiply(_: matrix_double3x4, _: matrix_double4x3) -> matrix_double4x4Added matrix_multiply(_: matrix_double3x2, _: matrix_double4x3) -> matrix_double4x2Added matrix_multiply(_: matrix_float3x3, _: matrix_float2x3) -> matrix_float2x3Added matrix_multiply(_: matrix_float3x2, _: matrix_float3x3) -> matrix_float3x2Added matrix_multiply(_: matrix_double2x2, _: matrix_double2x2) -> matrix_double2x2Added matrix_multiply(_: matrix_double4x4, _: matrix_double2x4) -> matrix_double2x4Added matrix_multiply(_: matrix_double4x3, _: matrix_double4x4) -> matrix_double4x3Added matrix_multiply(_: matrix_float2x2, _: matrix_float3x2) -> matrix_float3x2Added matrix_multiply(_: matrix_double4x4, _: matrix_double4x4) -> matrix_double4x4Added matrix_scale(_: Float, _: matrix_float4x4) -> matrix_float4x4Added matrix_scale(_: Double, _: matrix_double3x2) -> matrix_double3x2Added matrix_scale(_: Float, _: matrix_float4x2) -> matrix_float4x2Added matrix_scale(_: Float, _: matrix_float2x3) -> matrix_float2x3Added matrix_scale(_: Double, _: matrix_double2x3) -> matrix_double2x3Added matrix_scale(_: Double, _: matrix_double4x3) -> matrix_double4x3Added matrix_scale(_: Float, _: matrix_float2x4) -> matrix_float2x4Added matrix_scale(_: Float, _: matrix_float4x3) -> matrix_float4x3Added matrix_scale(_: Double, _: matrix_double3x4) -> matrix_double3x4Added [matrix_scale(_: Double, _: matrix_double4x2) -> matrix_double4x2](https://developer.apple.com/documentation/simd/1417839-matrix_scale)Added matrix_scale(_: Double, _: matrix_double3x3) -> matrix_double3x3Added matrix_scale(_: Float, _: matrix_float3x2) -> matrix_float3x2Added matrix_scale(_: Float, _: matrix_float3x3) -> matrix_float3x3Added matrix_scale(_: Float, _: matrix_float3x4) -> matrix_float3x4Added matrix_scale(_: Double, _: matrix_double4x4) -> matrix_double4x4Added matrix_scale(_: Double, _: matrix_double2x4) -> matrix_double2x4Added matrix_scale(_: Double, _: matrix_double2x2) -> matrix_double2x2Added matrix_transpose(_: matrix_double2x3) -> matrix_double3x2Added matrix_transpose(_: matrix_double2x2) -> matrix_double2x2Added matrix_transpose(_: matrix_double3x4) -> matrix_double4x3Added matrix_transpose(_: matrix_double2x4) -> matrix_double4x2Added matrix_transpose(_: matrix_float4x4) -> matrix_float4x4Added matrix_transpose(_: matrix_float4x2) -> matrix_float2x4Added matrix_transpose(_: matrix_float4x3) -> matrix_float3x4Added matrix_transpose(_: matrix_double3x2) -> matrix_double2x3Added matrix_transpose(_: matrix_float2x3) -> matrix_float3x2Added matrix_transpose(_: matrix_float2x4) -> matrix_float4x2Added matrix_transpose(_: matrix_float3x2) -> matrix_float2x3Added matrix_transpose(_: matrix_double4x4) -> matrix_double4x4Added matrix_transpose(_: matrix_float3x3) -> matrix_float3x3Added matrix_transpose(_: matrix_double3x3) -> matrix_double3x3Added matrix_transpose(_: matrix_float3x4) -> matrix_float4x3Added matrix_transpose(_: matrix_double4x3) -> matrix_double3x4Added matrix_transpose(_: matrix_double4x2) -> matrix_double2x4Added [max(_: uint3, _: UInt32) -> uint3](https://developer.apple.com/documentation/simd/1690585-max)Added [max(_: uint4, _: uint4) -> uint4](https://developer.apple.com/documentation/simd/1690542-max)Added [max(_: uint3, _: uint3) -> uint3](https://developer.apple.com/documentation/simd/1690576-max)Added [max(_: uint2, _: uint2) -> uint2](https://developer.apple.com/documentation/simd/1690594-max)Added [max(_: uint2, _: UInt32) -> uint2](https://developer.apple.com/documentation/simd/1690578-max)Added [max(_: uint4, _: UInt32) -> uint4](https://developer.apple.com/documentation/simd/1690575-max)Added [min(_: uint4, _: uint4) -> uint4](https://developer.apple.com/documentation/simd/1690584-min)Added [min(_: uint3, _: uint3) -> uint3](https://developer.apple.com/documentation/simd/1690528-min)Added [min(_: uint2, _: uint2) -> uint2](https://developer.apple.com/documentation/simd/1690582-min)Added [min(_: uint2, _: UInt32) -> uint2](https://developer.apple.com/documentation/simd/1690511-min)Added [min(_: uint4, _: UInt32) -> uint4](https://developer.apple.com/documentation/simd/1690568-min)Added [min(_: uint3, _: UInt32) -> uint3](https://developer.apple.com/documentation/simd/1690544-min)Added [packed_uint2](https://developer.apple.com/documentation/simd/packed_uint2)Added [packed_uint4](https://developer.apple.com/documentation/simd/packed_uint4)Added [reduce_add(_: uint4) -> UInt32](https://developer.apple.com/documentation/simd/1690590-reduce_add)Added [reduce_add(_: uint3) -> UInt32](https://developer.apple.com/documentation/simd/1690536-reduce_add)Added [reduce_add(_: uint2) -> UInt32](https://developer.apple.com/documentation/simd/1690539-reduce_add)Added [reduce_max(_: uint4) -> UInt32](https://developer.apple.com/documentation/simd/1690553-reduce_max)Added [reduce_max(_: uint2) -> UInt32](https://developer.apple.com/documentation/simd/1690543-reduce_max)Added [reduce_max(_: uint3) -> UInt32](https://developer.apple.com/documentation/simd/1690537-reduce_max)Added [reduce_min(_: uint2) -> UInt32](https://developer.apple.com/documentation/simd/1690521-reduce_min)Added [reduce_min(_: uint3) -> UInt32](https://developer.apple.com/documentation/simd/1690558-reduce_min)Added [reduce_min(_: uint4) -> UInt32](https://developer.apple.com/documentation/simd/1690567-reduce_min)Added [SIMD_LIBRARY_VERSION](https://developer.apple.com/documentation/simd/simd_library_version)Added [vector2(_: Double, _: Double) -> vector_double2](https://developer.apple.com/documentation/simd/1424392-vector2)Added [vector2(_: Float, _: Float) -> vector_float2](https://developer.apple.com/documentation/simd/1640242-vector2)Added [vector2(_: UInt32, _: UInt32) -> vector_uint2](https://developer.apple.com/documentation/simd/2918994-vector2)Added [vector3(_: UInt32, _: UInt32, _: UInt32) -> vector_uint3](https://developer.apple.com/documentation/simd/2918996-vector3)Added [vector3(_: Float, _: Float, _: Float) -> vector_float3](https://developer.apple.com/documentation/simd/1640205-vector3)Added [vector3(_: Double, _: Double, _: Double) -> vector_double3](https://developer.apple.com/documentation/simd/1424915-vector3)Added [vector4(_: Double, _: Double, _: Double, _: Double) -> vector_double4](https://developer.apple.com/documentation/simd/2918998-vector4)Added [vector4(_: UInt32, _: UInt32, _: UInt32, _: UInt32) -> vector_uint4](https://developer.apple.com/documentation/simd/1425315-vector4)Added [vector4(_: Float, _: Float, _: Float, _: Float) -> vector_float4](https://developer.apple.com/documentation/simd/1640364-vector4)Added vector_clamp(_: Float, _: Float, _: Float) -> FloatAdded vector_clamp(_: Double, _: Double, _: Double) -> DoubleAdded vector_fast_recip(_: Double) -> DoubleAdded vector_fast_rsqrt(_: Double) -> DoubleAdded vector_fract(_: Double) -> DoubleAdded vector_mix(_: Double, _: Double, _: Double) -> DoubleAdded vector_precise_recip(_: Double) -> DoubleAdded vector_precise_rsqrt(_: Double) -> DoubleAdded vector_recip(_: Double) -> DoubleAdded vector_rsqrt(_: Double) -> DoubleAdded vector_sign(_: Double) -> DoubleAdded vector_smoothstep(_: Double, _: Double, _: Double) -> DoubleAdded vector_step(_: Double, _: Double) -> DoubleAdded [vector_uint2](https://developer.apple.com/documentation/simd/vector_uint2)Added [vector_uint3](https://developer.apple.com/documentation/simd/vector_uint3)Added [vector_uint4](https://developer.apple.com/documentation/simd/vector_uint4)Modified [double2 [struct]](https://developer.apple.com/documentation/simd/double2)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct double2 : ArrayLiteralConvertible, CustomDebugStringConvertible {     var x: Double     var y: Double     init()     init(_ x: Double, _ y: Double)     init(x x: Double, y y: Double)     init(_ scalar: Double)     init(_ array: [Double])     init(arrayLiteral elements: Double...)     subscript (_ index: Int) -> Double     var debugDescription: String { get } } ``` | ArrayLiteralConvertible, CustomDebugStringConvertible |
| To | ``` struct double2 : ExpressibleByArrayLiteral, CustomDebugStringConvertible {     var x: Double     var y: Double     init()     init(_ x: Double, _ y: Double)     init(x x: Double, y y: Double)     init(_ scalar: Double)     init(_ array: [Double])     init(arrayLiteral elements: Double...)     subscript(_ index: Int) -> Double     var debugDescription: String { get } } ``` | CustomDebugStringConvertible, ExpressibleByArrayLiteral |

Modified [double2.subscript(_: Int) -> Double](https://developer.apple.com/documentation/simd/double2/1424054-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> Double ``` |
| To | ``` subscript(_ index: Int) -> Double ``` |

Modified double2x2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct double2x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double2)     init(_ columns: [double2])     init(rows rows: [double2])     init(_ cmatrix: matrix_double2x2)     var cmatrix: matrix_double2x2 { get }     subscript (_ column: Int) -> double2     subscript (_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double2x2 { get }     var inverse: double2x2 { get } } ``` |
| To | ``` struct double2x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double2)     init(_ columns: [double2])     init(rows rows: [double2])     init(_ cmatrix: matrix_double2x2)     var cmatrix: matrix_double2x2 { get }     subscript(_ column: Int) -> double2     subscript(_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double2x2 { get }     var inverse: double2x2 { get } } ``` |

Modified double2x2.subscript(_: Int) -> double2

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> double2 ``` |
| To | ``` subscript(_ column: Int) -> double2 ``` |

Modified double2x2.subscript(_: Int, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Double ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Double ``` |

Modified double2x3 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct double2x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double2)     init(_ columns: [double3])     init(rows rows: [double2])     init(_ cmatrix: matrix_double2x3)     var cmatrix: matrix_double2x3 { get }     subscript (_ column: Int) -> double3     subscript (_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double3x2 { get } } ``` |
| To | ``` struct double2x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double2)     init(_ columns: [double3])     init(rows rows: [double2])     init(_ cmatrix: matrix_double2x3)     var cmatrix: matrix_double2x3 { get }     subscript(_ column: Int) -> double3     subscript(_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double3x2 { get } } ``` |

Modified double2x3.subscript(_: Int) -> double3

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> double3 ``` |
| To | ``` subscript(_ column: Int) -> double3 ``` |

Modified double2x3.subscript(_: Int, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Double ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Double ``` |

Modified double2x4 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct double2x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double2)     init(_ columns: [double4])     init(rows rows: [double2])     init(_ cmatrix: matrix_double2x4)     var cmatrix: matrix_double2x4 { get }     subscript (_ column: Int) -> double4     subscript (_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double4x2 { get } } ``` |
| To | ``` struct double2x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double2)     init(_ columns: [double4])     init(rows rows: [double2])     init(_ cmatrix: matrix_double2x4)     var cmatrix: matrix_double2x4 { get }     subscript(_ column: Int) -> double4     subscript(_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double4x2 { get } } ``` |

Modified double2x4.subscript(_: Int) -> double4

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> double4 ``` |
| To | ``` subscript(_ column: Int) -> double4 ``` |

Modified double2x4.subscript(_: Int, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Double ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Double ``` |

Modified [double3 [struct]](https://developer.apple.com/documentation/simd/double3)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct double3 : ArrayLiteralConvertible, CustomDebugStringConvertible {     var x: Double     var y: Double     var z: Double     init()     init(_ x: Double, _ y: Double, _ z: Double)     init(x x: Double, y y: Double, z z: Double)     init(_ scalar: Double)     init(_ array: [Double])     init(arrayLiteral elements: Double...)     subscript (_ index: Int) -> Double     var debugDescription: String { get } } ``` | ArrayLiteralConvertible, CustomDebugStringConvertible |
| To | ``` struct double3 : ExpressibleByArrayLiteral, CustomDebugStringConvertible {     var x: Double     var y: Double     var z: Double     init()     init(_ x: Double, _ y: Double, _ z: Double)     init(x x: Double, y y: Double, z z: Double)     init(_ scalar: Double)     init(_ array: [Double])     init(arrayLiteral elements: Double...)     subscript(_ index: Int) -> Double     var debugDescription: String { get } } extension double3 {     init(_ v: SCNVector3) } ``` | CustomDebugStringConvertible, ExpressibleByArrayLiteral |

Modified [double3.subscript(_: Int) -> Double](https://developer.apple.com/documentation/simd/double3/1424417-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> Double ``` |
| To | ``` subscript(_ index: Int) -> Double ``` |

Modified double3x2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct double3x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double2)     init(_ columns: [double2])     init(rows rows: [double3])     init(_ cmatrix: matrix_double3x2)     var cmatrix: matrix_double3x2 { get }     subscript (_ column: Int) -> double2     subscript (_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double2x3 { get } } ``` |
| To | ``` struct double3x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double2)     init(_ columns: [double2])     init(rows rows: [double3])     init(_ cmatrix: matrix_double3x2)     var cmatrix: matrix_double3x2 { get }     subscript(_ column: Int) -> double2     subscript(_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double2x3 { get } } ``` |

Modified double3x2.subscript(_: Int) -> double2

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> double2 ``` |
| To | ``` subscript(_ column: Int) -> double2 ``` |

Modified double3x2.subscript(_: Int, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Double ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Double ``` |

Modified double3x3 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct double3x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double3)     init(_ columns: [double3])     init(rows rows: [double3])     init(_ cmatrix: matrix_double3x3)     var cmatrix: matrix_double3x3 { get }     subscript (_ column: Int) -> double3     subscript (_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double3x3 { get }     var inverse: double3x3 { get } } ``` |
| To | ``` struct double3x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double3)     init(_ columns: [double3])     init(rows rows: [double3])     init(_ cmatrix: matrix_double3x3)     var cmatrix: matrix_double3x3 { get }     subscript(_ column: Int) -> double3     subscript(_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double3x3 { get }     var inverse: double3x3 { get } } ``` |

Modified double3x3.subscript(_: Int) -> double3

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> double3 ``` |
| To | ``` subscript(_ column: Int) -> double3 ``` |

Modified double3x3.subscript(_: Int, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Double ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Double ``` |

Modified double3x4 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct double3x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double3)     init(_ columns: [double4])     init(rows rows: [double3])     init(_ cmatrix: matrix_double3x4)     var cmatrix: matrix_double3x4 { get }     subscript (_ column: Int) -> double4     subscript (_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double4x3 { get } } ``` |
| To | ``` struct double3x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double3)     init(_ columns: [double4])     init(rows rows: [double3])     init(_ cmatrix: matrix_double3x4)     var cmatrix: matrix_double3x4 { get }     subscript(_ column: Int) -> double4     subscript(_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double4x3 { get } } ``` |

Modified double3x4.subscript(_: Int) -> double4

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> double4 ``` |
| To | ``` subscript(_ column: Int) -> double4 ``` |

Modified double3x4.subscript(_: Int, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Double ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Double ``` |

Modified [double4 [struct]](https://developer.apple.com/documentation/simd/double4)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct double4 : ArrayLiteralConvertible, CustomDebugStringConvertible {     var x: Double     var y: Double     var z: Double     var w: Double     init()     init(_ x: Double, _ y: Double, _ z: Double, _ w: Double)     init(x x: Double, y y: Double, z z: Double, w w: Double)     init(_ scalar: Double)     init(_ array: [Double])     init(arrayLiteral elements: Double...)     subscript (_ index: Int) -> Double     var debugDescription: String { get } } ``` | ArrayLiteralConvertible, CustomDebugStringConvertible |
| To | ``` struct double4 : ExpressibleByArrayLiteral, CustomDebugStringConvertible {     var x: Double     var y: Double     var z: Double     var w: Double     init()     init(_ x: Double, _ y: Double, _ z: Double, _ w: Double)     init(x x: Double, y y: Double, z z: Double, w w: Double)     init(_ scalar: Double)     init(_ array: [Double])     init(arrayLiteral elements: Double...)     subscript(_ index: Int) -> Double     var debugDescription: String { get } } extension double4 {     init(_ v: SCNVector4) } ``` | CustomDebugStringConvertible, ExpressibleByArrayLiteral |

Modified [double4.subscript(_: Int) -> Double](https://developer.apple.com/documentation/simd/double4/1425770-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> Double ``` |
| To | ``` subscript(_ index: Int) -> Double ``` |

Modified double4x2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct double4x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double2)     init(_ columns: [double2])     init(rows rows: [double4])     init(_ cmatrix: matrix_double4x2)     var cmatrix: matrix_double4x2 { get }     subscript (_ column: Int) -> double2     subscript (_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double2x4 { get } } ``` |
| To | ``` struct double4x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double2)     init(_ columns: [double2])     init(rows rows: [double4])     init(_ cmatrix: matrix_double4x2)     var cmatrix: matrix_double4x2 { get }     subscript(_ column: Int) -> double2     subscript(_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double2x4 { get } } ``` |

Modified double4x2.subscript(_: Int) -> double2

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> double2 ``` |
| To | ``` subscript(_ column: Int) -> double2 ``` |

Modified double4x2.subscript(_: Int, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Double ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Double ``` |

Modified double4x3 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct double4x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double3)     init(_ columns: [double3])     init(rows rows: [double4])     init(_ cmatrix: matrix_double4x3)     var cmatrix: matrix_double4x3 { get }     subscript (_ column: Int) -> double3     subscript (_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double3x4 { get } } ``` |
| To | ``` struct double4x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double3)     init(_ columns: [double3])     init(rows rows: [double4])     init(_ cmatrix: matrix_double4x3)     var cmatrix: matrix_double4x3 { get }     subscript(_ column: Int) -> double3     subscript(_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double3x4 { get } } ``` |

Modified double4x3.subscript(_: Int) -> double3

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> double3 ``` |
| To | ``` subscript(_ column: Int) -> double3 ``` |

Modified double4x3.subscript(_: Int, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Double ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Double ``` |

Modified double4x4 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct double4x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double4)     init(_ columns: [double4])     init(rows rows: [double4])     init(_ cmatrix: matrix_double4x4)     var cmatrix: matrix_double4x4 { get }     subscript (_ column: Int) -> double4     subscript (_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double4x4 { get }     var inverse: double4x4 { get } } ``` |
| To | ``` struct double4x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Double)     init(diagonal diagonal: double4)     init(_ columns: [double4])     init(rows rows: [double4])     init(_ cmatrix: matrix_double4x4)     var cmatrix: matrix_double4x4 { get }     subscript(_ column: Int) -> double4     subscript(_ column: Int, _ row: Int) -> Double     var debugDescription: String { get }     var transpose: double4x4 { get }     var inverse: double4x4 { get } } extension double4x4 {     init(_ m: SCNMatrix4) } ``` |

Modified double4x4.subscript(_: Int) -> double4

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> double4 ``` |
| To | ``` subscript(_ column: Int) -> double4 ``` |

Modified double4x4.subscript(_: Int, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Double ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Double ``` |

Modified [float2 [struct]](https://developer.apple.com/documentation/simd/float2)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct float2 : ArrayLiteralConvertible, CustomDebugStringConvertible {     var x: Float     var y: Float     init()     init(_ x: Float, _ y: Float)     init(x x: Float, y y: Float)     init(_ scalar: Float)     init(_ array: [Float])     init(arrayLiteral elements: Float...)     subscript (_ index: Int) -> Float     var debugDescription: String { get } } ``` | ArrayLiteralConvertible, CustomDebugStringConvertible |
| To | ``` struct float2 : ExpressibleByArrayLiteral, CustomDebugStringConvertible {     var x: Float     var y: Float     init()     init(_ x: Float, _ y: Float)     init(x x: Float, y y: Float)     init(_ scalar: Float)     init(_ array: [Float])     init(arrayLiteral elements: Float...)     subscript(_ index: Int) -> Float     var debugDescription: String { get } } ``` | CustomDebugStringConvertible, ExpressibleByArrayLiteral |

Modified [float2.subscript(_: Int) -> Float](https://developer.apple.com/documentation/simd/float2/1424081-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> Float ``` |
| To | ``` subscript(_ index: Int) -> Float ``` |

Modified float2x2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct float2x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float2)     init(_ columns: [float2])     init(rows rows: [float2])     init(_ cmatrix: matrix_float2x2)     var cmatrix: matrix_float2x2 { get }     subscript (_ column: Int) -> float2     subscript (_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float2x2 { get }     var inverse: float2x2 { get } } ``` |
| To | ``` struct float2x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float2)     init(_ columns: [float2])     init(rows rows: [float2])     init(_ cmatrix: matrix_float2x2)     var cmatrix: matrix_float2x2 { get }     subscript(_ column: Int) -> float2     subscript(_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float2x2 { get }     var inverse: float2x2 { get } } ``` |

Modified float2x2.subscript(_: Int) -> float2

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> float2 ``` |
| To | ``` subscript(_ column: Int) -> float2 ``` |

Modified float2x2.subscript(_: Int, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Float ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Float ``` |

Modified float2x3 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct float2x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float2)     init(_ columns: [float3])     init(rows rows: [float2])     init(_ cmatrix: matrix_float2x3)     var cmatrix: matrix_float2x3 { get }     subscript (_ column: Int) -> float3     subscript (_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float3x2 { get } } ``` |
| To | ``` struct float2x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float2)     init(_ columns: [float3])     init(rows rows: [float2])     init(_ cmatrix: matrix_float2x3)     var cmatrix: matrix_float2x3 { get }     subscript(_ column: Int) -> float3     subscript(_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float3x2 { get } } ``` |

Modified float2x3.subscript(_: Int) -> float3

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> float3 ``` |
| To | ``` subscript(_ column: Int) -> float3 ``` |

Modified float2x3.subscript(_: Int, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Float ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Float ``` |

Modified float2x4 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct float2x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float2)     init(_ columns: [float4])     init(rows rows: [float2])     init(_ cmatrix: matrix_float2x4)     var cmatrix: matrix_float2x4 { get }     subscript (_ column: Int) -> float4     subscript (_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float4x2 { get } } ``` |
| To | ``` struct float2x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float2)     init(_ columns: [float4])     init(rows rows: [float2])     init(_ cmatrix: matrix_float2x4)     var cmatrix: matrix_float2x4 { get }     subscript(_ column: Int) -> float4     subscript(_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float4x2 { get } } ``` |

Modified float2x4.subscript(_: Int) -> float4

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> float4 ``` |
| To | ``` subscript(_ column: Int) -> float4 ``` |

Modified float2x4.subscript(_: Int, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Float ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Float ``` |

Modified [float3 [struct]](https://developer.apple.com/documentation/simd/float3)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct float3 : ArrayLiteralConvertible, CustomDebugStringConvertible {     var x: Float     var y: Float     var z: Float     init()     init(_ x: Float, _ y: Float, _ z: Float)     init(x x: Float, y y: Float, z z: Float)     init(_ scalar: Float)     init(_ array: [Float])     init(arrayLiteral elements: Float...)     subscript (_ index: Int) -> Float     var debugDescription: String { get } } ``` | ArrayLiteralConvertible, CustomDebugStringConvertible |
| To | ``` struct float3 : ExpressibleByArrayLiteral, CustomDebugStringConvertible {     var x: Float     var y: Float     var z: Float     init()     init(_ x: Float, _ y: Float, _ z: Float)     init(x x: Float, y y: Float, z z: Float)     init(_ scalar: Float)     init(_ array: [Float])     init(arrayLiteral elements: Float...)     subscript(_ index: Int) -> Float     var debugDescription: String { get } } extension float3 {     init(_ v: SCNVector3) } ``` | CustomDebugStringConvertible, ExpressibleByArrayLiteral |

Modified [float3.subscript(_: Int) -> Float](https://developer.apple.com/documentation/simd/float3/1424032-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> Float ``` |
| To | ``` subscript(_ index: Int) -> Float ``` |

Modified float3x2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct float3x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float2)     init(_ columns: [float2])     init(rows rows: [float3])     init(_ cmatrix: matrix_float3x2)     var cmatrix: matrix_float3x2 { get }     subscript (_ column: Int) -> float2     subscript (_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float2x3 { get } } ``` |
| To | ``` struct float3x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float2)     init(_ columns: [float2])     init(rows rows: [float3])     init(_ cmatrix: matrix_float3x2)     var cmatrix: matrix_float3x2 { get }     subscript(_ column: Int) -> float2     subscript(_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float2x3 { get } } ``` |

Modified float3x2.subscript(_: Int) -> float2

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> float2 ``` |
| To | ``` subscript(_ column: Int) -> float2 ``` |

Modified float3x2.subscript(_: Int, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Float ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Float ``` |

Modified float3x3 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct float3x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float3)     init(_ columns: [float3])     init(rows rows: [float3])     init(_ cmatrix: matrix_float3x3)     var cmatrix: matrix_float3x3 { get }     subscript (_ column: Int) -> float3     subscript (_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float3x3 { get }     var inverse: float3x3 { get } } ``` |
| To | ``` struct float3x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float3)     init(_ columns: [float3])     init(rows rows: [float3])     init(_ cmatrix: matrix_float3x3)     var cmatrix: matrix_float3x3 { get }     subscript(_ column: Int) -> float3     subscript(_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float3x3 { get }     var inverse: float3x3 { get } } ``` |

Modified float3x3.subscript(_: Int) -> float3

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> float3 ``` |
| To | ``` subscript(_ column: Int) -> float3 ``` |

Modified float3x3.subscript(_: Int, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Float ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Float ``` |

Modified float3x4 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct float3x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float3)     init(_ columns: [float4])     init(rows rows: [float3])     init(_ cmatrix: matrix_float3x4)     var cmatrix: matrix_float3x4 { get }     subscript (_ column: Int) -> float4     subscript (_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float4x3 { get } } ``` |
| To | ``` struct float3x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float3)     init(_ columns: [float4])     init(rows rows: [float3])     init(_ cmatrix: matrix_float3x4)     var cmatrix: matrix_float3x4 { get }     subscript(_ column: Int) -> float4     subscript(_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float4x3 { get } } ``` |

Modified float3x4.subscript(_: Int) -> float4

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> float4 ``` |
| To | ``` subscript(_ column: Int) -> float4 ``` |

Modified float3x4.subscript(_: Int, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Float ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Float ``` |

Modified [float4 [struct]](https://developer.apple.com/documentation/simd/float4)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct float4 : ArrayLiteralConvertible, CustomDebugStringConvertible {     var x: Float     var y: Float     var z: Float     var w: Float     init()     init(_ x: Float, _ y: Float, _ z: Float, _ w: Float)     init(x x: Float, y y: Float, z z: Float, w w: Float)     init(_ scalar: Float)     init(_ array: [Float])     init(arrayLiteral elements: Float...)     subscript (_ index: Int) -> Float     var debugDescription: String { get } } ``` | ArrayLiteralConvertible, CustomDebugStringConvertible |
| To | ``` struct float4 : ExpressibleByArrayLiteral, CustomDebugStringConvertible {     var x: Float     var y: Float     var z: Float     var w: Float     init()     init(_ x: Float, _ y: Float, _ z: Float, _ w: Float)     init(x x: Float, y y: Float, z z: Float, w w: Float)     init(_ scalar: Float)     init(_ array: [Float])     init(arrayLiteral elements: Float...)     subscript(_ index: Int) -> Float     var debugDescription: String { get } } extension float4 {     init(_ v: SCNVector4) } ``` | CustomDebugStringConvertible, ExpressibleByArrayLiteral |

Modified [float4.subscript(_: Int) -> Float](https://developer.apple.com/documentation/simd/float4/1426138-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> Float ``` |
| To | ``` subscript(_ index: Int) -> Float ``` |

Modified float4x2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct float4x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float2)     init(_ columns: [float2])     init(rows rows: [float4])     init(_ cmatrix: matrix_float4x2)     var cmatrix: matrix_float4x2 { get }     subscript (_ column: Int) -> float2     subscript (_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float2x4 { get } } ``` |
| To | ``` struct float4x2 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float2)     init(_ columns: [float2])     init(rows rows: [float4])     init(_ cmatrix: matrix_float4x2)     var cmatrix: matrix_float4x2 { get }     subscript(_ column: Int) -> float2     subscript(_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float2x4 { get } } ``` |

Modified float4x2.subscript(_: Int) -> float2

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> float2 ``` |
| To | ``` subscript(_ column: Int) -> float2 ``` |

Modified float4x2.subscript(_: Int, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Float ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Float ``` |

Modified float4x3 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct float4x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float3)     init(_ columns: [float3])     init(rows rows: [float4])     init(_ cmatrix: matrix_float4x3)     var cmatrix: matrix_float4x3 { get }     subscript (_ column: Int) -> float3     subscript (_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float3x4 { get } } ``` |
| To | ``` struct float4x3 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float3)     init(_ columns: [float3])     init(rows rows: [float4])     init(_ cmatrix: matrix_float4x3)     var cmatrix: matrix_float4x3 { get }     subscript(_ column: Int) -> float3     subscript(_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float3x4 { get } } ``` |

Modified float4x3.subscript(_: Int) -> float3

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> float3 ``` |
| To | ``` subscript(_ column: Int) -> float3 ``` |

Modified float4x3.subscript(_: Int, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Float ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Float ``` |

Modified float4x4 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct float4x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float4)     init(_ columns: [float4])     init(rows rows: [float4])     init(_ cmatrix: matrix_float4x4)     var cmatrix: matrix_float4x4 { get }     subscript (_ column: Int) -> float4     subscript (_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float4x4 { get }     var inverse: float4x4 { get } } ``` |
| To | ``` struct float4x4 : CustomDebugStringConvertible {     init()     init(_ scalar: Float)     init(diagonal diagonal: float4)     init(_ columns: [float4])     init(rows rows: [float4])     init(_ cmatrix: matrix_float4x4)     var cmatrix: matrix_float4x4 { get }     subscript(_ column: Int) -> float4     subscript(_ column: Int, _ row: Int) -> Float     var debugDescription: String { get }     var transpose: float4x4 { get }     var inverse: float4x4 { get } } extension float4x4 {     init(_ m: SCNMatrix4) } ``` |

Modified float4x4.subscript(_: Int) -> float4

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int) -> float4 ``` |
| To | ``` subscript(_ column: Int) -> float4 ``` |

Modified float4x4.subscript(_: Int, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ column: Int, _ row: Int) -> Float ``` |
| To | ``` subscript(_ column: Int, _ row: Int) -> Float ``` |

Modified [int2 [struct]](https://developer.apple.com/documentation/simd/int2)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct int2 : ArrayLiteralConvertible, CustomDebugStringConvertible {     var x: Int32     var y: Int32     init()     init(_ x: Int32, _ y: Int32)     init(x x: Int32, y y: Int32)     init(_ scalar: Int32)     init(_ array: [Int32])     init(arrayLiteral elements: Int32...)     subscript (_ index: Int) -> Int32     var debugDescription: String { get } } ``` | ArrayLiteralConvertible, CustomDebugStringConvertible |
| To | ``` struct int2 : ExpressibleByArrayLiteral, CustomDebugStringConvertible {     var x: Int32     var y: Int32     init()     init(_ x: Int32, _ y: Int32)     init(x x: Int32, y y: Int32)     init(_ scalar: Int32)     init(_ array: [Int32])     init(arrayLiteral elements: Int32...)     subscript(_ index: Int) -> Int32     var debugDescription: String { get } } ``` | CustomDebugStringConvertible, ExpressibleByArrayLiteral |

Modified [int2.subscript(_: Int) -> Int32](https://developer.apple.com/documentation/simd/int2/1426013-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> Int32 ``` |
| To | ``` subscript(_ index: Int) -> Int32 ``` |

Modified [int3 [struct]](https://developer.apple.com/documentation/simd/int3)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct int3 : ArrayLiteralConvertible, CustomDebugStringConvertible {     var x: Int32     var y: Int32     var z: Int32     init()     init(_ x: Int32, _ y: Int32, _ z: Int32)     init(x x: Int32, y y: Int32, z z: Int32)     init(_ scalar: Int32)     init(_ array: [Int32])     init(arrayLiteral elements: Int32...)     subscript (_ index: Int) -> Int32     var debugDescription: String { get } } ``` | ArrayLiteralConvertible, CustomDebugStringConvertible |
| To | ``` struct int3 : ExpressibleByArrayLiteral, CustomDebugStringConvertible {     var x: Int32     var y: Int32     var z: Int32     init()     init(_ x: Int32, _ y: Int32, _ z: Int32)     init(x x: Int32, y y: Int32, z z: Int32)     init(_ scalar: Int32)     init(_ array: [Int32])     init(arrayLiteral elements: Int32...)     subscript(_ index: Int) -> Int32     var debugDescription: String { get } } ``` | CustomDebugStringConvertible, ExpressibleByArrayLiteral |

Modified [int3.subscript(_: Int) -> Int32](https://developer.apple.com/documentation/simd/int3/1424983-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> Int32 ``` |
| To | ``` subscript(_ index: Int) -> Int32 ``` |

Modified [int4 [struct]](https://developer.apple.com/documentation/simd/int4)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct int4 : ArrayLiteralConvertible, CustomDebugStringConvertible {     var x: Int32     var y: Int32     var z: Int32     var w: Int32     init()     init(_ x: Int32, _ y: Int32, _ z: Int32, _ w: Int32)     init(x x: Int32, y y: Int32, z z: Int32, w w: Int32)     init(_ scalar: Int32)     init(_ array: [Int32])     init(arrayLiteral elements: Int32...)     subscript (_ index: Int) -> Int32     var debugDescription: String { get } } ``` | ArrayLiteralConvertible, CustomDebugStringConvertible |
| To | ``` struct int4 : ExpressibleByArrayLiteral, CustomDebugStringConvertible {     var x: Int32     var y: Int32     var z: Int32     var w: Int32     init()     init(_ x: Int32, _ y: Int32, _ z: Int32, _ w: Int32)     init(x x: Int32, y y: Int32, z z: Int32, w w: Int32)     init(_ scalar: Int32)     init(_ array: [Int32])     init(arrayLiteral elements: Int32...)     subscript(_ index: Int) -> Int32     var debugDescription: String { get } } ``` | CustomDebugStringConvertible, ExpressibleByArrayLiteral |

Modified [int4.subscript(_: Int) -> Int32](https://developer.apple.com/documentation/simd/int4/1425183-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> Int32 ``` |
| To | ``` subscript(_ index: Int) -> Int32 ``` |

Modified &\*(_: int2, _: Int32) -> int2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &*(_ lhs: int2, _ rhs: Int32) -> int2 ``` |
| To | ``` func &*(_ lhs: int2, _ rhs: Int32) -> int2 ``` |

Modified &\*(_: int2, _: int2) -> int2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &*(_ lhs: int2, _ rhs: int2) -> int2 ``` |
| To | ``` func &*(_ lhs: int2, _ rhs: int2) -> int2 ``` |

Modified &\*(_: Int32, _: int2) -> int2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &*(_ lhs: Int32, _ rhs: int2) -> int2 ``` |
| To | ``` func &*(_ lhs: Int32, _ rhs: int2) -> int2 ``` |

Modified &\*(_: int3, _: int3) -> int3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &*(_ lhs: int3, _ rhs: int3) -> int3 ``` |
| To | ``` func &*(_ lhs: int3, _ rhs: int3) -> int3 ``` |

Modified &\*(_: Int32, _: int3) -> int3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &*(_ lhs: Int32, _ rhs: int3) -> int3 ``` |
| To | ``` func &*(_ lhs: Int32, _ rhs: int3) -> int3 ``` |

Modified &\*(_: Int32, _: int4) -> int4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &*(_ lhs: Int32, _ rhs: int4) -> int4 ``` |
| To | ``` func &*(_ lhs: Int32, _ rhs: int4) -> int4 ``` |

Modified &\*(_: int3, _: Int32) -> int3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &*(_ lhs: int3, _ rhs: Int32) -> int3 ``` |
| To | ``` func &*(_ lhs: int3, _ rhs: Int32) -> int3 ``` |

Modified &\*(_: int4, _: int4) -> int4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &*(_ lhs: int4, _ rhs: int4) -> int4 ``` |
| To | ``` func &*(_ lhs: int4, _ rhs: int4) -> int4 ``` |

Modified &\*(_: int4, _: Int32) -> int4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &*(_ lhs: int4, _ rhs: Int32) -> int4 ``` |
| To | ``` func &*(_ lhs: int4, _ rhs: Int32) -> int4 ``` |

Modified &+(_: int2, _: int2) -> int2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &+(_ lhs: int2, _ rhs: int2) -> int2 ``` |
| To | ``` func &+(_ lhs: int2, _ rhs: int2) -> int2 ``` |

Modified &+(_: int4, _: int4) -> int4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &+(_ lhs: int4, _ rhs: int4) -> int4 ``` |
| To | ``` func &+(_ lhs: int4, _ rhs: int4) -> int4 ``` |

Modified &+(_: int3, _: int3) -> int3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &+(_ lhs: int3, _ rhs: int3) -> int3 ``` |
| To | ``` func &+(_ lhs: int3, _ rhs: int3) -> int3 ``` |

Modified &-(_: int4, _: int4) -> int4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &-(_ lhs: int4, _ rhs: int4) -> int4 ``` |
| To | ``` func &-(_ lhs: int4, _ rhs: int4) -> int4 ``` |

Modified &-(_: int3, _: int3) -> int3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &-(_ lhs: int3, _ rhs: int3) -> int3 ``` |
| To | ``` func &-(_ lhs: int3, _ rhs: int3) -> int3 ``` |

Modified &-(_: int2, _: int2) -> int2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func &-(_ lhs: int2, _ rhs: int2) -> int2 ``` |
| To | ``` func &-(_ lhs: int2, _ rhs: int2) -> int2 ``` |

Modified \*(_: Double, _: double4x2) -> double4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double4x2) -> double4x2 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double4x2) -> double4x2 ``` |

Modified \*(_: double3x3, _: Double) -> double3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x3, _ rhs: Double) -> double3x3 ``` |
| To | ``` func *(_ lhs: double3x3, _ rhs: Double) -> double3x3 ``` |

Modified \*(_: float4x4, _: float4x4) -> float4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x4, _ rhs: float4x4) -> float4x4 ``` |
| To | ``` func *(_ lhs: float4x4, _ rhs: float4x4) -> float4x4 ``` |

Modified \*(_: double3x2, _: double3) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x2, _ rhs: double3) -> double2 ``` |
| To | ``` func *(_ lhs: double3x2, _ rhs: double3) -> double2 ``` |

Modified \*(_: double2, _: double2x2) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2, _ rhs: double2x2) -> double2 ``` |
| To | ``` func *(_ lhs: double2, _ rhs: double2x2) -> double2 ``` |

Modified \*(_: Double, _: double3x2) -> double3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double3x2) -> double3x2 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double3x2) -> double3x2 ``` |

Modified \*(_: double3x4, _: double3x3) -> double3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x4, _ rhs: double3x3) -> double3x4 ``` |
| To | ``` func *(_ lhs: double3x4, _ rhs: double3x3) -> double3x4 ``` |

Modified \*(_: float2, _: float2) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2, _ rhs: float2) -> float2 ``` |
| To | ``` func *(_ lhs: float2, _ rhs: float2) -> float2 ``` |

Modified \*(_: float2x3, _: float4x2) -> float4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x3, _ rhs: float4x2) -> float4x3 ``` |
| To | ``` func *(_ lhs: float2x3, _ rhs: float4x2) -> float4x3 ``` |

Modified \*(_: float3x3, _: Float) -> float3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x3, _ rhs: Float) -> float3x3 ``` |
| To | ``` func *(_ lhs: float3x3, _ rhs: Float) -> float3x3 ``` |

Modified \*(_: double3x2, _: double2x3) -> double2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x2, _ rhs: double2x3) -> double2x2 ``` |
| To | ``` func *(_ lhs: double3x2, _ rhs: double2x3) -> double2x2 ``` |

Modified \*(_: double4x3, _: double2x4) -> double2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x3, _ rhs: double2x4) -> double2x3 ``` |
| To | ``` func *(_ lhs: double4x3, _ rhs: double2x4) -> double2x3 ``` |

Modified \*(_: double3x2, _: double4x3) -> double4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x2, _ rhs: double4x3) -> double4x2 ``` |
| To | ``` func *(_ lhs: double3x2, _ rhs: double4x3) -> double4x2 ``` |

Modified \*(_: float4x4, _: float4) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x4, _ rhs: float4) -> float4 ``` |
| To | ``` func *(_ lhs: float4x4, _ rhs: float4) -> float4 ``` |

Modified \*(_: Float, _: float3x3) -> float3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float3x3) -> float3x3 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float3x3) -> float3x3 ``` |

Modified \*(_: double2x2, _: double2x2) -> double2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x2, _ rhs: double2x2) -> double2x2 ``` |
| To | ``` func *(_ lhs: double2x2, _ rhs: double2x2) -> double2x2 ``` |

Modified \*(_: double4x4, _: double4) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x4, _ rhs: double4) -> double4 ``` |
| To | ``` func *(_ lhs: double4x4, _ rhs: double4) -> double4 ``` |

Modified \*(_: double3, _: double2x3) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3, _ rhs: double2x3) -> double2 ``` |
| To | ``` func *(_ lhs: double3, _ rhs: double2x3) -> double2 ``` |

Modified \*(_: float3x2, _: Float) -> float3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x2, _ rhs: Float) -> float3x2 ``` |
| To | ``` func *(_ lhs: float3x2, _ rhs: Float) -> float3x2 ``` |

Modified \*(_: double3x3, _: double4x3) -> double4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x3, _ rhs: double4x3) -> double4x3 ``` |
| To | ``` func *(_ lhs: double3x3, _ rhs: double4x3) -> double4x3 ``` |

Modified \*(_: float3, _: Float) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3, _ rhs: Float) -> float3 ``` |
| To | ``` func *(_ lhs: float3, _ rhs: Float) -> float3 ``` |

Modified \*(_: double4x2, _: double2x4) -> double2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x2, _ rhs: double2x4) -> double2x2 ``` |
| To | ``` func *(_ lhs: double4x2, _ rhs: double2x4) -> double2x2 ``` |

Modified \*(_: float2, _: float3x2) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2, _ rhs: float3x2) -> float3 ``` |
| To | ``` func *(_ lhs: float2, _ rhs: float3x2) -> float3 ``` |

Modified \*(_: double2, _: double3x2) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2, _ rhs: double3x2) -> double3 ``` |
| To | ``` func *(_ lhs: double2, _ rhs: double3x2) -> double3 ``` |

Modified \*(_: float3x3, _: float4x3) -> float4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x3, _ rhs: float4x3) -> float4x3 ``` |
| To | ``` func *(_ lhs: float3x3, _ rhs: float4x3) -> float4x3 ``` |

Modified \*(_: double4x3, _: Double) -> double4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x3, _ rhs: Double) -> double4x3 ``` |
| To | ``` func *(_ lhs: double4x3, _ rhs: Double) -> double4x3 ``` |

Modified \*(_: double2x4, _: double3x2) -> double3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x4, _ rhs: double3x2) -> double3x4 ``` |
| To | ``` func *(_ lhs: double2x4, _ rhs: double3x2) -> double3x4 ``` |

Modified \*(_: double3, _: double3) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3, _ rhs: double3) -> double3 ``` |
| To | ``` func *(_ lhs: double3, _ rhs: double3) -> double3 ``` |

Modified \*(_: Double, _: double2x4) -> double2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double2x4) -> double2x4 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double2x4) -> double2x4 ``` |

Modified \*(_: float2x4, _: float2x2) -> float2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x4, _ rhs: float2x2) -> float2x4 ``` |
| To | ``` func *(_ lhs: float2x4, _ rhs: float2x2) -> float2x4 ``` |

Modified \*(_: float4, _: float4) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4, _ rhs: float4) -> float4 ``` |
| To | ``` func *(_ lhs: float4, _ rhs: float4) -> float4 ``` |

Modified \*(_: Double, _: double4x4) -> double4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double4x4) -> double4x4 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double4x4) -> double4x4 ``` |

Modified \*(_: float2, _: float2x2) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2, _ rhs: float2x2) -> float2 ``` |
| To | ``` func *(_ lhs: float2, _ rhs: float2x2) -> float2 ``` |

Modified \*(_: Double, _: double4x3) -> double4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double4x3) -> double4x3 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double4x3) -> double4x3 ``` |

Modified \*(_: double2x4, _: Double) -> double2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x4, _ rhs: Double) -> double2x4 ``` |
| To | ``` func *(_ lhs: double2x4, _ rhs: Double) -> double2x4 ``` |

Modified \*(_: double2, _: Double) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2, _ rhs: Double) -> double2 ``` |
| To | ``` func *(_ lhs: double2, _ rhs: Double) -> double2 ``` |

Modified \*(_: float3x4, _: float4x3) -> float4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x4, _ rhs: float4x3) -> float4x4 ``` |
| To | ``` func *(_ lhs: float3x4, _ rhs: float4x3) -> float4x4 ``` |

Modified \*(_: float2x4, _: float4x2) -> float4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x4, _ rhs: float4x2) -> float4x4 ``` |
| To | ``` func *(_ lhs: float2x4, _ rhs: float4x2) -> float4x4 ``` |

Modified \*(_: Float, _: float3x2) -> float3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float3x2) -> float3x2 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float3x2) -> float3x2 ``` |

Modified \*(_: float3x2, _: float3) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x2, _ rhs: float3) -> float2 ``` |
| To | ``` func *(_ lhs: float3x2, _ rhs: float3) -> float2 ``` |

Modified \*(_: float4x4, _: Float) -> float4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x4, _ rhs: Float) -> float4x4 ``` |
| To | ``` func *(_ lhs: float4x4, _ rhs: Float) -> float4x4 ``` |

Modified \*(_: float4, _: float4x4) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4, _ rhs: float4x4) -> float4 ``` |
| To | ``` func *(_ lhs: float4, _ rhs: float4x4) -> float4 ``` |

Modified \*(_: Float, _: float4x2) -> float4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float4x2) -> float4x2 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float4x2) -> float4x2 ``` |

Modified \*(_: float3, _: float2x3) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3, _ rhs: float2x3) -> float2 ``` |
| To | ``` func *(_ lhs: float3, _ rhs: float2x3) -> float2 ``` |

Modified \*(_: double2, _: double4x2) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2, _ rhs: double4x2) -> double4 ``` |
| To | ``` func *(_ lhs: double2, _ rhs: double4x2) -> double4 ``` |

Modified \*(_: float4, _: Float) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4, _ rhs: Float) -> float4 ``` |
| To | ``` func *(_ lhs: float4, _ rhs: Float) -> float4 ``` |

Modified \*(_: float2x3, _: float2) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x3, _ rhs: float2) -> float3 ``` |
| To | ``` func *(_ lhs: float2x3, _ rhs: float2) -> float3 ``` |

Modified \*(_: double4x4, _: double2x4) -> double2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x4, _ rhs: double2x4) -> double2x4 ``` |
| To | ``` func *(_ lhs: double4x4, _ rhs: double2x4) -> double2x4 ``` |

Modified \*(_: float4x2, _: Float) -> float4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x2, _ rhs: Float) -> float4x2 ``` |
| To | ``` func *(_ lhs: float4x2, _ rhs: Float) -> float4x2 ``` |

Modified \*(_: float4, _: float3x4) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4, _ rhs: float3x4) -> float3 ``` |
| To | ``` func *(_ lhs: float4, _ rhs: float3x4) -> float3 ``` |

Modified \*(_: float4x2, _: float3x4) -> float3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x2, _ rhs: float3x4) -> float3x2 ``` |
| To | ``` func *(_ lhs: float4x2, _ rhs: float3x4) -> float3x2 ``` |

Modified \*(_: double3x4, _: double4x3) -> double4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x4, _ rhs: double4x3) -> double4x4 ``` |
| To | ``` func *(_ lhs: double3x4, _ rhs: double4x3) -> double4x4 ``` |

Modified \*(_: double3x3, _: double3x3) -> double3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x3, _ rhs: double3x3) -> double3x3 ``` |
| To | ``` func *(_ lhs: double3x3, _ rhs: double3x3) -> double3x3 ``` |

Modified \*(_: double2x2, _: Double) -> double2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x2, _ rhs: Double) -> double2x2 ``` |
| To | ``` func *(_ lhs: double2x2, _ rhs: Double) -> double2x2 ``` |

Modified \*(_: double3x4, _: Double) -> double3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x4, _ rhs: Double) -> double3x4 ``` |
| To | ``` func *(_ lhs: double3x4, _ rhs: Double) -> double3x4 ``` |

Modified \*(_: double3x3, _: double2x3) -> double2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x3, _ rhs: double2x3) -> double2x3 ``` |
| To | ``` func *(_ lhs: double3x3, _ rhs: double2x3) -> double2x3 ``` |

Modified \*(_: float2x3, _: float3x2) -> float3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x3, _ rhs: float3x2) -> float3x3 ``` |
| To | ``` func *(_ lhs: float2x3, _ rhs: float3x2) -> float3x3 ``` |

Modified \*(_: double4x2, _: double4) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x2, _ rhs: double4) -> double2 ``` |
| To | ``` func *(_ lhs: double4x2, _ rhs: double4) -> double2 ``` |

Modified \*(_: double4x2, _: double3x4) -> double3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x2, _ rhs: double3x4) -> double3x2 ``` |
| To | ``` func *(_ lhs: double4x2, _ rhs: double3x4) -> double3x2 ``` |

Modified \*(_: double4x2, _: double4x4) -> double4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x2, _ rhs: double4x4) -> double4x2 ``` |
| To | ``` func *(_ lhs: double4x2, _ rhs: double4x4) -> double4x2 ``` |

Modified \*(_: float4x3, _: float4x4) -> float4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x3, _ rhs: float4x4) -> float4x3 ``` |
| To | ``` func *(_ lhs: float4x3, _ rhs: float4x4) -> float4x3 ``` |

Modified \*(_: Double, _: double2x2) -> double2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double2x2) -> double2x2 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double2x2) -> double2x2 ``` |

Modified \*(_: Float, _: float3) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float3) -> float3 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float3) -> float3 ``` |

Modified \*(_: float3x3, _: float2x3) -> float2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x3, _ rhs: float2x3) -> float2x3 ``` |
| To | ``` func *(_ lhs: float3x3, _ rhs: float2x3) -> float2x3 ``` |

Modified \*(_: float3, _: float4x3) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3, _ rhs: float4x3) -> float4 ``` |
| To | ``` func *(_ lhs: float3, _ rhs: float4x3) -> float4 ``` |

Modified \*(_: double2x3, _: double2) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x3, _ rhs: double2) -> double3 ``` |
| To | ``` func *(_ lhs: double2x3, _ rhs: double2) -> double3 ``` |

Modified \*(_: double2x3, _: double4x2) -> double4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x3, _ rhs: double4x2) -> double4x3 ``` |
| To | ``` func *(_ lhs: double2x3, _ rhs: double4x2) -> double4x3 ``` |

Modified \*(_: float3x2, _: float3x3) -> float3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x2, _ rhs: float3x3) -> float3x2 ``` |
| To | ``` func *(_ lhs: float3x2, _ rhs: float3x3) -> float3x2 ``` |

Modified \*(_: float4x2, _: float2x4) -> float2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x2, _ rhs: float2x4) -> float2x2 ``` |
| To | ``` func *(_ lhs: float4x2, _ rhs: float2x4) -> float2x2 ``` |

Modified \*(_: float4x3, _: float3x4) -> float3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x3, _ rhs: float3x4) -> float3x3 ``` |
| To | ``` func *(_ lhs: float4x3, _ rhs: float3x4) -> float3x3 ``` |

Modified \*(_: float3x2, _: float2x3) -> float2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x2, _ rhs: float2x3) -> float2x2 ``` |
| To | ``` func *(_ lhs: float3x2, _ rhs: float2x3) -> float2x2 ``` |

Modified \*(_: Double, _: double3x3) -> double3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double3x3) -> double3x3 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double3x3) -> double3x3 ``` |

Modified \*(_: double2x3, _: double2x2) -> double2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x3, _ rhs: double2x2) -> double2x3 ``` |
| To | ``` func *(_ lhs: double2x3, _ rhs: double2x2) -> double2x3 ``` |

Modified \*(_: double2x4, _: double2x2) -> double2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x4, _ rhs: double2x2) -> double2x4 ``` |
| To | ``` func *(_ lhs: double2x4, _ rhs: double2x2) -> double2x4 ``` |

Modified \*(_: float4x3, _: Float) -> float4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x3, _ rhs: Float) -> float4x3 ``` |
| To | ``` func *(_ lhs: float4x3, _ rhs: Float) -> float4x3 ``` |

Modified \*(_: float3x4, _: Float) -> float3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x4, _ rhs: Float) -> float3x4 ``` |
| To | ``` func *(_ lhs: float3x4, _ rhs: Float) -> float3x4 ``` |

Modified \*(_: double2x2, _: double3x2) -> double3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x2, _ rhs: double3x2) -> double3x2 ``` |
| To | ``` func *(_ lhs: double2x2, _ rhs: double3x2) -> double3x2 ``` |

Modified \*(_: Float, _: float2x3) -> float2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float2x3) -> float2x3 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float2x3) -> float2x3 ``` |

Modified \*(_: double4, _: double3x4) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4, _ rhs: double3x4) -> double3 ``` |
| To | ``` func *(_ lhs: double4, _ rhs: double3x4) -> double3 ``` |

Modified \*(_: double3x4, _: double3) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x4, _ rhs: double3) -> double4 ``` |
| To | ``` func *(_ lhs: double3x4, _ rhs: double3) -> double4 ``` |

Modified \*(_: double3, _: Double) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3, _ rhs: Double) -> double3 ``` |
| To | ``` func *(_ lhs: double3, _ rhs: Double) -> double3 ``` |

Modified \*(_: float4x3, _: float4) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x3, _ rhs: float4) -> float3 ``` |
| To | ``` func *(_ lhs: float4x3, _ rhs: float4) -> float3 ``` |

Modified \*(_: Float, _: float4) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float4) -> float4 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float4) -> float4 ``` |

Modified \*(_: Float, _: float2x2) -> float2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float2x2) -> float2x2 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float2x2) -> float2x2 ``` |

Modified \*(_: float2x4, _: float3x2) -> float3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x4, _ rhs: float3x2) -> float3x4 ``` |
| To | ``` func *(_ lhs: float2x4, _ rhs: float3x2) -> float3x4 ``` |

Modified \*(_: double4x2, _: Double) -> double4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x2, _ rhs: Double) -> double4x2 ``` |
| To | ``` func *(_ lhs: double4x2, _ rhs: Double) -> double4x2 ``` |

Modified \*(_: double3x3, _: double3) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x3, _ rhs: double3) -> double3 ``` |
| To | ``` func *(_ lhs: double3x3, _ rhs: double3) -> double3 ``` |

Modified \*(_: double4, _: double2x4) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4, _ rhs: double2x4) -> double2 ``` |
| To | ``` func *(_ lhs: double4, _ rhs: double2x4) -> double2 ``` |

Modified \*(_: Double, _: double2) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double2) -> double2 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double2) -> double2 ``` |

Modified \*(_: double4x4, _: double4x4) -> double4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x4, _ rhs: double4x4) -> double4x4 ``` |
| To | ``` func *(_ lhs: double4x4, _ rhs: double4x4) -> double4x4 ``` |

Modified \*(_: float2x2, _: float2x2) -> float2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x2, _ rhs: float2x2) -> float2x2 ``` |
| To | ``` func *(_ lhs: float2x2, _ rhs: float2x2) -> float2x2 ``` |

Modified \*(_: float2x4, _: Float) -> float2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x4, _ rhs: Float) -> float2x4 ``` |
| To | ``` func *(_ lhs: float2x4, _ rhs: Float) -> float2x4 ``` |

Modified \*(_: float2, _: float4x2) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2, _ rhs: float4x2) -> float4 ``` |
| To | ``` func *(_ lhs: float2, _ rhs: float4x2) -> float4 ``` |

Modified \*(_: float4x2, _: float4x4) -> float4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x2, _ rhs: float4x4) -> float4x2 ``` |
| To | ``` func *(_ lhs: float4x2, _ rhs: float4x4) -> float4x2 ``` |

Modified \*(_: double2x3, _: double3x2) -> double3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x3, _ rhs: double3x2) -> double3x3 ``` |
| To | ``` func *(_ lhs: double2x3, _ rhs: double3x2) -> double3x3 ``` |

Modified \*(_: float4x4, _: float2x4) -> float2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x4, _ rhs: float2x4) -> float2x4 ``` |
| To | ``` func *(_ lhs: float4x4, _ rhs: float2x4) -> float2x4 ``` |

Modified \*(_: float2x2, _: float4x2) -> float4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x2, _ rhs: float4x2) -> float4x2 ``` |
| To | ``` func *(_ lhs: float2x2, _ rhs: float4x2) -> float4x2 ``` |

Modified \*(_: float2, _: Float) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2, _ rhs: Float) -> float2 ``` |
| To | ``` func *(_ lhs: float2, _ rhs: Float) -> float2 ``` |

Modified \*(_: float3, _: float3x3) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3, _ rhs: float3x3) -> float3 ``` |
| To | ``` func *(_ lhs: float3, _ rhs: float3x3) -> float3 ``` |

Modified \*(_: float3x3, _: float3x3) -> float3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x3, _ rhs: float3x3) -> float3x3 ``` |
| To | ``` func *(_ lhs: float3x3, _ rhs: float3x3) -> float3x3 ``` |

Modified \*(_: float3x4, _: float3x3) -> float3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x4, _ rhs: float3x3) -> float3x4 ``` |
| To | ``` func *(_ lhs: float3x4, _ rhs: float3x3) -> float3x4 ``` |

Modified \*(_: Float, _: float4x3) -> float4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float4x3) -> float4x3 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float4x3) -> float4x3 ``` |

Modified \*(_: float4x4, _: float3x4) -> float3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x4, _ rhs: float3x4) -> float3x4 ``` |
| To | ``` func *(_ lhs: float4x4, _ rhs: float3x4) -> float3x4 ``` |

Modified \*(_: float3x3, _: float3) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x3, _ rhs: float3) -> float3 ``` |
| To | ``` func *(_ lhs: float3x3, _ rhs: float3) -> float3 ``` |

Modified \*(_: Float, _: float2) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float2) -> float2 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float2) -> float2 ``` |

Modified \*(_: double2x2, _: double2) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x2, _ rhs: double2) -> double2 ``` |
| To | ``` func *(_ lhs: double2x2, _ rhs: double2) -> double2 ``` |

Modified \*(_: double3, _: double4x3) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3, _ rhs: double4x3) -> double4 ``` |
| To | ``` func *(_ lhs: double3, _ rhs: double4x3) -> double4 ``` |

Modified \*(_: float2x2, _: float2) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x2, _ rhs: float2) -> float2 ``` |
| To | ``` func *(_ lhs: float2x2, _ rhs: float2) -> float2 ``` |

Modified \*(_: double4x4, _: Double) -> double4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x4, _ rhs: Double) -> double4x4 ``` |
| To | ``` func *(_ lhs: double4x4, _ rhs: Double) -> double4x4 ``` |

Modified \*(_: float2x3, _: float2x2) -> float2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x3, _ rhs: float2x2) -> float2x3 ``` |
| To | ``` func *(_ lhs: float2x3, _ rhs: float2x2) -> float2x3 ``` |

Modified \*(_: float3x4, _: float3) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x4, _ rhs: float3) -> float4 ``` |
| To | ``` func *(_ lhs: float3x4, _ rhs: float3) -> float4 ``` |

Modified \*(_: float3, _: float3) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3, _ rhs: float3) -> float3 ``` |
| To | ``` func *(_ lhs: float3, _ rhs: float3) -> float3 ``` |

Modified \*(_: double2x4, _: double4x2) -> double4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x4, _ rhs: double4x2) -> double4x4 ``` |
| To | ``` func *(_ lhs: double2x4, _ rhs: double4x2) -> double4x4 ``` |

Modified \*(_: double4x3, _: double4x4) -> double4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x3, _ rhs: double4x4) -> double4x3 ``` |
| To | ``` func *(_ lhs: double4x3, _ rhs: double4x4) -> double4x3 ``` |

Modified \*(_: Double, _: double3) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double3) -> double3 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double3) -> double3 ``` |

Modified \*(_: float2x2, _: float3x2) -> float3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x2, _ rhs: float3x2) -> float3x2 ``` |
| To | ``` func *(_ lhs: float2x2, _ rhs: float3x2) -> float3x2 ``` |

Modified \*(_: float4x2, _: float4) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x2, _ rhs: float4) -> float2 ``` |
| To | ``` func *(_ lhs: float4x2, _ rhs: float4) -> float2 ``` |

Modified \*(_: double4, _: double4) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4, _ rhs: double4) -> double4 ``` |
| To | ``` func *(_ lhs: double4, _ rhs: double4) -> double4 ``` |

Modified \*(_: Double, _: double2x3) -> double2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double2x3) -> double2x3 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double2x3) -> double2x3 ``` |

Modified \*(_: float2x3, _: Float) -> float2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x3, _ rhs: Float) -> float2x3 ``` |
| To | ``` func *(_ lhs: float2x3, _ rhs: Float) -> float2x3 ``` |

Modified \*(_: Float, _: float4x4) -> float4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float4x4) -> float4x4 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float4x4) -> float4x4 ``` |

Modified \*(_: double3, _: double3x3) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3, _ rhs: double3x3) -> double3 ``` |
| To | ``` func *(_ lhs: double3, _ rhs: double3x3) -> double3 ``` |

Modified \*(_: double3x2, _: Double) -> double3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x2, _ rhs: Double) -> double3x2 ``` |
| To | ``` func *(_ lhs: double3x2, _ rhs: Double) -> double3x2 ``` |

Modified \*(_: Double, _: double3x4) -> double3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double3x4) -> double3x4 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double3x4) -> double3x4 ``` |

Modified \*(_: Double, _: double4) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: double4) -> double4 ``` |
| To | ``` func *(_ lhs: Double, _ rhs: double4) -> double4 ``` |

Modified \*(_: float3x4, _: float2x3) -> float2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x4, _ rhs: float2x3) -> float2x4 ``` |
| To | ``` func *(_ lhs: float3x4, _ rhs: float2x3) -> float2x4 ``` |

Modified \*(_: float3x2, _: float4x3) -> float4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float3x2, _ rhs: float4x3) -> float4x2 ``` |
| To | ``` func *(_ lhs: float3x2, _ rhs: float4x3) -> float4x2 ``` |

Modified \*(_: double4x3, _: double4) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x3, _ rhs: double4) -> double3 ``` |
| To | ``` func *(_ lhs: double4x3, _ rhs: double4) -> double3 ``` |

Modified \*(_: double2x2, _: double4x2) -> double4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x2, _ rhs: double4x2) -> double4x2 ``` |
| To | ``` func *(_ lhs: double2x2, _ rhs: double4x2) -> double4x2 ``` |

Modified \*(_: float4x3, _: float2x4) -> float2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4x3, _ rhs: float2x4) -> float2x3 ``` |
| To | ``` func *(_ lhs: float4x3, _ rhs: float2x4) -> float2x3 ``` |

Modified \*(_: double4, _: double4x4) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4, _ rhs: double4x4) -> double4 ``` |
| To | ``` func *(_ lhs: double4, _ rhs: double4x4) -> double4 ``` |

Modified \*(_: float2x4, _: float2) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x4, _ rhs: float2) -> float4 ``` |
| To | ``` func *(_ lhs: float2x4, _ rhs: float2) -> float4 ``` |

Modified \*(_: Float, _: float2x4) -> float2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float2x4) -> float2x4 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float2x4) -> float2x4 ``` |

Modified \*(_: double4x4, _: double3x4) -> double3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x4, _ rhs: double3x4) -> double3x4 ``` |
| To | ``` func *(_ lhs: double4x4, _ rhs: double3x4) -> double3x4 ``` |

Modified \*(_: double3x2, _: double3x3) -> double3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x2, _ rhs: double3x3) -> double3x2 ``` |
| To | ``` func *(_ lhs: double3x2, _ rhs: double3x3) -> double3x2 ``` |

Modified \*(_: double4x3, _: double3x4) -> double3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4x3, _ rhs: double3x4) -> double3x3 ``` |
| To | ``` func *(_ lhs: double4x3, _ rhs: double3x4) -> double3x3 ``` |

Modified \*(_: double2x4, _: double2) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x4, _ rhs: double2) -> double4 ``` |
| To | ``` func *(_ lhs: double2x4, _ rhs: double2) -> double4 ``` |

Modified \*(_: float2x2, _: Float) -> float2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float2x2, _ rhs: Float) -> float2x2 ``` |
| To | ``` func *(_ lhs: float2x2, _ rhs: Float) -> float2x2 ``` |

Modified \*(_: Float, _: float3x4) -> float3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: float3x4) -> float3x4 ``` |
| To | ``` func *(_ lhs: Float, _ rhs: float3x4) -> float3x4 ``` |

Modified \*(_: double4, _: Double) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double4, _ rhs: Double) -> double4 ``` |
| To | ``` func *(_ lhs: double4, _ rhs: Double) -> double4 ``` |

Modified \*(_: double3x4, _: double2x3) -> double2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double3x4, _ rhs: double2x3) -> double2x4 ``` |
| To | ``` func *(_ lhs: double3x4, _ rhs: double2x3) -> double2x4 ``` |

Modified \*(_: float4, _: float2x4) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: float4, _ rhs: float2x4) -> float2 ``` |
| To | ``` func *(_ lhs: float4, _ rhs: float2x4) -> float2 ``` |

Modified \*(_: double2x3, _: Double) -> double2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2x3, _ rhs: Double) -> double2x3 ``` |
| To | ``` func *(_ lhs: double2x3, _ rhs: Double) -> double2x3 ``` |

Modified \*(_: double2, _: double2) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: double2, _ rhs: double2) -> double2 ``` |
| To | ``` func *(_ lhs: double2, _ rhs: double2) -> double2 ``` |

Modified \*=(_: float4x2, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float4x2, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float4x2, _ rhs: Float) ``` |

Modified \*=(_: float3x3, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float3x3, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float3x3, _ rhs: Float) ``` |

Modified \*=(_: float3, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float3, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float3, _ rhs: Float) ``` |

Modified \*=(_: float2x2, _: float2x2)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float2x2, _ rhs: float2x2) ``` |
| To | ``` func *=(_ lhs: inout float2x2, _ rhs: float2x2) ``` |

Modified \*=(_: float4x2, _: float4x4)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float4x2, _ rhs: float4x4) ``` |
| To | ``` func *=(_ lhs: inout float4x2, _ rhs: float4x4) ``` |

Modified \*=(_: float3x2, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float3x2, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float3x2, _ rhs: Float) ``` |

Modified \*=(_: float3x2, _: float3x3)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float3x2, _ rhs: float3x3) ``` |
| To | ``` func *=(_ lhs: inout float3x2, _ rhs: float3x3) ``` |

Modified \*=(_: double3x2, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double3x2, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double3x2, _ rhs: Double) ``` |

Modified \*=(_: double2x3, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double2x3, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double2x3, _ rhs: Double) ``` |

Modified \*=(_: float2x4, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float2x4, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float2x4, _ rhs: Float) ``` |

Modified \*=(_: double2x3, _: double2x2)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double2x3, _ rhs: double2x2) ``` |
| To | ``` func *=(_ lhs: inout double2x3, _ rhs: double2x2) ``` |

Modified \*=(_: float2x4, _: float2x2)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float2x4, _ rhs: float2x2) ``` |
| To | ``` func *=(_ lhs: inout float2x4, _ rhs: float2x2) ``` |

Modified \*=(_: double4, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double4, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double4, _ rhs: Double) ``` |

Modified \*=(_: double3x4, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double3x4, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double3x4, _ rhs: Double) ``` |

Modified \*=(_: float4x4, _: float4x4)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float4x4, _ rhs: float4x4) ``` |
| To | ``` func *=(_ lhs: inout float4x4, _ rhs: float4x4) ``` |

Modified \*=(_: float2, _: float2)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float2, _ rhs: float2) ``` |
| To | ``` func *=(_ lhs: inout float2, _ rhs: float2) ``` |

Modified \*=(_: float3x3, _: float3x3)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float3x3, _ rhs: float3x3) ``` |
| To | ``` func *=(_ lhs: inout float3x3, _ rhs: float3x3) ``` |

Modified \*=(_: double3, _: double3)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double3, _ rhs: double3) ``` |
| To | ``` func *=(_ lhs: inout double3, _ rhs: double3) ``` |

Modified \*=(_: float3x4, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float3x4, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float3x4, _ rhs: Float) ``` |

Modified \*=(_: double4x4, _: double4x4)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double4x4, _ rhs: double4x4) ``` |
| To | ``` func *=(_ lhs: inout double4x4, _ rhs: double4x4) ``` |

Modified \*=(_: double4x2, _: double4x4)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double4x2, _ rhs: double4x4) ``` |
| To | ``` func *=(_ lhs: inout double4x2, _ rhs: double4x4) ``` |

Modified \*=(_: double3x4, _: double3x3)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double3x4, _ rhs: double3x3) ``` |
| To | ``` func *=(_ lhs: inout double3x4, _ rhs: double3x3) ``` |

Modified \*=(_: double4x4, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double4x4, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double4x4, _ rhs: Double) ``` |

Modified \*=(_: double4, _: double4)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double4, _ rhs: double4) ``` |
| To | ``` func *=(_ lhs: inout double4, _ rhs: double4) ``` |

Modified \*=(_: double2, _: double2)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double2, _ rhs: double2) ``` |
| To | ``` func *=(_ lhs: inout double2, _ rhs: double2) ``` |

Modified \*=(_: double3x3, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double3x3, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double3x3, _ rhs: Double) ``` |

Modified \*=(_: float2x3, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float2x3, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float2x3, _ rhs: Float) ``` |

Modified \*=(_: float2x2, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float2x2, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float2x2, _ rhs: Float) ``` |

Modified \*=(_: double3x2, _: double3x3)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double3x2, _ rhs: double3x3) ``` |
| To | ``` func *=(_ lhs: inout double3x2, _ rhs: double3x3) ``` |

Modified \*=(_: float2, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float2, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float2, _ rhs: Float) ``` |

Modified \*=(_: double2, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double2, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double2, _ rhs: Double) ``` |

Modified \*=(_: float2x3, _: float2x2)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float2x3, _ rhs: float2x2) ``` |
| To | ``` func *=(_ lhs: inout float2x3, _ rhs: float2x2) ``` |

Modified \*=(_: double4x3, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double4x3, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double4x3, _ rhs: Double) ``` |

Modified \*=(_: double2x2, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double2x2, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double2x2, _ rhs: Double) ``` |

Modified \*=(_: float3, _: float3)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float3, _ rhs: float3) ``` |
| To | ``` func *=(_ lhs: inout float3, _ rhs: float3) ``` |

Modified \*=(_: double2x2, _: double2x2)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double2x2, _ rhs: double2x2) ``` |
| To | ``` func *=(_ lhs: inout double2x2, _ rhs: double2x2) ``` |

Modified \*=(_: float3x4, _: float3x3)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float3x4, _ rhs: float3x3) ``` |
| To | ``` func *=(_ lhs: inout float3x4, _ rhs: float3x3) ``` |

Modified \*=(_: double3x3, _: double3x3)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double3x3, _ rhs: double3x3) ``` |
| To | ``` func *=(_ lhs: inout double3x3, _ rhs: double3x3) ``` |

Modified \*=(_: double2x4, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double2x4, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double2x4, _ rhs: Double) ``` |

Modified \*=(_: float4x4, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float4x4, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float4x4, _ rhs: Float) ``` |

Modified \*=(_: double4x3, _: double4x4)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double4x3, _ rhs: double4x4) ``` |
| To | ``` func *=(_ lhs: inout double4x3, _ rhs: double4x4) ``` |

Modified \*=(_: double3, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double3, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double3, _ rhs: Double) ``` |

Modified \*=(_: float4x3, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float4x3, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float4x3, _ rhs: Float) ``` |

Modified \*=(_: double2x4, _: double2x2)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double2x4, _ rhs: double2x2) ``` |
| To | ``` func *=(_ lhs: inout double2x4, _ rhs: double2x2) ``` |

Modified \*=(_: float4, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float4, _ rhs: Float) ``` |
| To | ``` func *=(_ lhs: inout float4, _ rhs: Float) ``` |

Modified \*=(_: float4x3, _: float4x4)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float4x3, _ rhs: float4x4) ``` |
| To | ``` func *=(_ lhs: inout float4x3, _ rhs: float4x4) ``` |

Modified \*=(_: float4, _: float4)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: float4, _ rhs: float4) ``` |
| To | ``` func *=(_ lhs: inout float4, _ rhs: float4) ``` |

Modified \*=(_: double4x2, _: Double)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: double4x2, _ rhs: Double) ``` |
| To | ``` func *=(_ lhs: inout double4x2, _ rhs: Double) ``` |

Modified +(_: double2x4, _: double2x4) -> double2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double2x4, _ rhs: double2x4) -> double2x4 ``` |
| To | ``` func +(_ lhs: double2x4, _ rhs: double2x4) -> double2x4 ``` |

Modified +(_: float4x2, _: float4x2) -> float4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float4x2, _ rhs: float4x2) -> float4x2 ``` |
| To | ``` func +(_ lhs: float4x2, _ rhs: float4x2) -> float4x2 ``` |

Modified +(_: double2x2, _: double2x2) -> double2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double2x2, _ rhs: double2x2) -> double2x2 ``` |
| To | ``` func +(_ lhs: double2x2, _ rhs: double2x2) -> double2x2 ``` |

Modified +(_: float2, _: float2) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float2, _ rhs: float2) -> float2 ``` |
| To | ``` func +(_ lhs: float2, _ rhs: float2) -> float2 ``` |

Modified +(_: float2x4, _: float2x4) -> float2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float2x4, _ rhs: float2x4) -> float2x4 ``` |
| To | ``` func +(_ lhs: float2x4, _ rhs: float2x4) -> float2x4 ``` |

Modified +(_: double2, _: double2) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double2, _ rhs: double2) -> double2 ``` |
| To | ``` func +(_ lhs: double2, _ rhs: double2) -> double2 ``` |

Modified +(_: float4x3, _: float4x3) -> float4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float4x3, _ rhs: float4x3) -> float4x3 ``` |
| To | ``` func +(_ lhs: float4x3, _ rhs: float4x3) -> float4x3 ``` |

Modified +(_: double3, _: double3) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double3, _ rhs: double3) -> double3 ``` |
| To | ``` func +(_ lhs: double3, _ rhs: double3) -> double3 ``` |

Modified +(_: double3x4, _: double3x4) -> double3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double3x4, _ rhs: double3x4) -> double3x4 ``` |
| To | ``` func +(_ lhs: double3x4, _ rhs: double3x4) -> double3x4 ``` |

Modified +(_: float4, _: float4) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float4, _ rhs: float4) -> float4 ``` |
| To | ``` func +(_ lhs: float4, _ rhs: float4) -> float4 ``` |

Modified +(_: float4x4, _: float4x4) -> float4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float4x4, _ rhs: float4x4) -> float4x4 ``` |
| To | ``` func +(_ lhs: float4x4, _ rhs: float4x4) -> float4x4 ``` |

Modified +(_: float2x3, _: float2x3) -> float2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float2x3, _ rhs: float2x3) -> float2x3 ``` |
| To | ``` func +(_ lhs: float2x3, _ rhs: float2x3) -> float2x3 ``` |

Modified +(_: float3x4, _: float3x4) -> float3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float3x4, _ rhs: float3x4) -> float3x4 ``` |
| To | ``` func +(_ lhs: float3x4, _ rhs: float3x4) -> float3x4 ``` |

Modified +(_: float2x2, _: float2x2) -> float2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float2x2, _ rhs: float2x2) -> float2x2 ``` |
| To | ``` func +(_ lhs: float2x2, _ rhs: float2x2) -> float2x2 ``` |

Modified +(_: float3x2, _: float3x2) -> float3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float3x2, _ rhs: float3x2) -> float3x2 ``` |
| To | ``` func +(_ lhs: float3x2, _ rhs: float3x2) -> float3x2 ``` |

Modified +(_: float3, _: float3) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float3, _ rhs: float3) -> float3 ``` |
| To | ``` func +(_ lhs: float3, _ rhs: float3) -> float3 ``` |

Modified +(_: double4, _: double4) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double4, _ rhs: double4) -> double4 ``` |
| To | ``` func +(_ lhs: double4, _ rhs: double4) -> double4 ``` |

Modified +(_: double4x3, _: double4x3) -> double4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double4x3, _ rhs: double4x3) -> double4x3 ``` |
| To | ``` func +(_ lhs: double4x3, _ rhs: double4x3) -> double4x3 ``` |

Modified +(_: double4x2, _: double4x2) -> double4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double4x2, _ rhs: double4x2) -> double4x2 ``` |
| To | ``` func +(_ lhs: double4x2, _ rhs: double4x2) -> double4x2 ``` |

Modified +(_: float3x3, _: float3x3) -> float3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: float3x3, _ rhs: float3x3) -> float3x3 ``` |
| To | ``` func +(_ lhs: float3x3, _ rhs: float3x3) -> float3x3 ``` |

Modified +(_: double3x2, _: double3x2) -> double3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double3x2, _ rhs: double3x2) -> double3x2 ``` |
| To | ``` func +(_ lhs: double3x2, _ rhs: double3x2) -> double3x2 ``` |

Modified +(_: double4x4, _: double4x4) -> double4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double4x4, _ rhs: double4x4) -> double4x4 ``` |
| To | ``` func +(_ lhs: double4x4, _ rhs: double4x4) -> double4x4 ``` |

Modified +(_: double2x3, _: double2x3) -> double2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double2x3, _ rhs: double2x3) -> double2x3 ``` |
| To | ``` func +(_ lhs: double2x3, _ rhs: double2x3) -> double2x3 ``` |

Modified +(_: double3x3, _: double3x3) -> double3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: double3x3, _ rhs: double3x3) -> double3x3 ``` |
| To | ``` func +(_ lhs: double3x3, _ rhs: double3x3) -> double3x3 ``` |

Modified +=(_: double3x3, _: double3x3)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double3x3, _ rhs: double3x3) ``` |
| To | ``` func +=(_ lhs: inout double3x3, _ rhs: double3x3) ``` |

Modified +=(_: double2x2, _: double2x2)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double2x2, _ rhs: double2x2) ``` |
| To | ``` func +=(_ lhs: inout double2x2, _ rhs: double2x2) ``` |

Modified +=(_: float4, _: float4)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float4, _ rhs: float4) ``` |
| To | ``` func +=(_ lhs: inout float4, _ rhs: float4) ``` |

Modified +=(_: float2, _: float2)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float2, _ rhs: float2) ``` |
| To | ``` func +=(_ lhs: inout float2, _ rhs: float2) ``` |

Modified +=(_: float2x4, _: float2x4)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float2x4, _ rhs: float2x4) ``` |
| To | ``` func +=(_ lhs: inout float2x4, _ rhs: float2x4) ``` |

Modified +=(_: float4x4, _: float4x4)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float4x4, _ rhs: float4x4) ``` |
| To | ``` func +=(_ lhs: inout float4x4, _ rhs: float4x4) ``` |

Modified +=(_: float3x2, _: float3x2)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float3x2, _ rhs: float3x2) ``` |
| To | ``` func +=(_ lhs: inout float3x2, _ rhs: float3x2) ``` |

Modified +=(_: double3, _: double3)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double3, _ rhs: double3) ``` |
| To | ``` func +=(_ lhs: inout double3, _ rhs: double3) ``` |

Modified +=(_: double4x3, _: double4x3)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double4x3, _ rhs: double4x3) ``` |
| To | ``` func +=(_ lhs: inout double4x3, _ rhs: double4x3) ``` |

Modified +=(_: double2x4, _: double2x4)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double2x4, _ rhs: double2x4) ``` |
| To | ``` func +=(_ lhs: inout double2x4, _ rhs: double2x4) ``` |

Modified +=(_: double3x2, _: double3x2)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double3x2, _ rhs: double3x2) ``` |
| To | ``` func +=(_ lhs: inout double3x2, _ rhs: double3x2) ``` |

Modified +=(_: float3x3, _: float3x3)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float3x3, _ rhs: float3x3) ``` |
| To | ``` func +=(_ lhs: inout float3x3, _ rhs: float3x3) ``` |

Modified +=(_: float4x3, _: float4x3)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float4x3, _ rhs: float4x3) ``` |
| To | ``` func +=(_ lhs: inout float4x3, _ rhs: float4x3) ``` |

Modified +=(_: float4x2, _: float4x2)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float4x2, _ rhs: float4x2) ``` |
| To | ``` func +=(_ lhs: inout float4x2, _ rhs: float4x2) ``` |

Modified +=(_: float2x3, _: float2x3)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float2x3, _ rhs: float2x3) ``` |
| To | ``` func +=(_ lhs: inout float2x3, _ rhs: float2x3) ``` |

Modified +=(_: double4x4, _: double4x4)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double4x4, _ rhs: double4x4) ``` |
| To | ``` func +=(_ lhs: inout double4x4, _ rhs: double4x4) ``` |

Modified +=(_: float2x2, _: float2x2)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float2x2, _ rhs: float2x2) ``` |
| To | ``` func +=(_ lhs: inout float2x2, _ rhs: float2x2) ``` |

Modified +=(_: double3x4, _: double3x4)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double3x4, _ rhs: double3x4) ``` |
| To | ``` func +=(_ lhs: inout double3x4, _ rhs: double3x4) ``` |

Modified +=(_: float3, _: float3)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float3, _ rhs: float3) ``` |
| To | ``` func +=(_ lhs: inout float3, _ rhs: float3) ``` |

Modified +=(_: double2x3, _: double2x3)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double2x3, _ rhs: double2x3) ``` |
| To | ``` func +=(_ lhs: inout double2x3, _ rhs: double2x3) ``` |

Modified +=(_: double4x2, _: double4x2)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double4x2, _ rhs: double4x2) ``` |
| To | ``` func +=(_ lhs: inout double4x2, _ rhs: double4x2) ``` |

Modified +=(_: double2, _: double2)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double2, _ rhs: double2) ``` |
| To | ``` func +=(_ lhs: inout double2, _ rhs: double2) ``` |

Modified +=(_: double4, _: double4)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: double4, _ rhs: double4) ``` |
| To | ``` func +=(_ lhs: inout double4, _ rhs: double4) ``` |

Modified +=(_: float3x4, _: float3x4)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: float3x4, _ rhs: float3x4) ``` |
| To | ``` func +=(_ lhs: inout float3x4, _ rhs: float3x4) ``` |

Modified -(_: double2) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double2) -> double2 ``` |
| To | ``` prefix func -(_ rhs: double2) -> double2 ``` |

Modified -(_: float3x2) -> float3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float3x2) -> float3x2 ``` |
| To | ``` prefix func -(_ rhs: float3x2) -> float3x2 ``` |

Modified -(_: float2x4) -> float2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float2x4) -> float2x4 ``` |
| To | ``` prefix func -(_ rhs: float2x4) -> float2x4 ``` |

Modified -(_: double3x2) -> double3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double3x2) -> double3x2 ``` |
| To | ``` prefix func -(_ rhs: double3x2) -> double3x2 ``` |

Modified -(_: double4x2) -> double4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double4x2) -> double4x2 ``` |
| To | ``` prefix func -(_ rhs: double4x2) -> double4x2 ``` |

Modified -(_: double2x4) -> double2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double2x4) -> double2x4 ``` |
| To | ``` prefix func -(_ rhs: double2x4) -> double2x4 ``` |

Modified -(_: float4x2) -> float4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float4x2) -> float4x2 ``` |
| To | ``` prefix func -(_ rhs: float4x2) -> float4x2 ``` |

Modified -(_: double4x3) -> double4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double4x3) -> double4x3 ``` |
| To | ``` prefix func -(_ rhs: double4x3) -> double4x3 ``` |

Modified -(_: float4x3) -> float4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float4x3) -> float4x3 ``` |
| To | ``` prefix func -(_ rhs: float4x3) -> float4x3 ``` |

Modified -(_: double2x3) -> double2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double2x3) -> double2x3 ``` |
| To | ``` prefix func -(_ rhs: double2x3) -> double2x3 ``` |

Modified -(_: int2) -> int2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: int2) -> int2 ``` |
| To | ``` prefix func -(_ rhs: int2) -> int2 ``` |

Modified -(_: double3x3) -> double3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double3x3) -> double3x3 ``` |
| To | ``` prefix func -(_ rhs: double3x3) -> double3x3 ``` |

Modified -(_: float2) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float2) -> float2 ``` |
| To | ``` prefix func -(_ rhs: float2) -> float2 ``` |

Modified -(_: double3x4) -> double3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double3x4) -> double3x4 ``` |
| To | ``` prefix func -(_ rhs: double3x4) -> double3x4 ``` |

Modified -(_: float2x3) -> float2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float2x3) -> float2x3 ``` |
| To | ``` prefix func -(_ rhs: float2x3) -> float2x3 ``` |

Modified -(_: float3x3) -> float3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float3x3) -> float3x3 ``` |
| To | ``` prefix func -(_ rhs: float3x3) -> float3x3 ``` |

Modified -(_: float4) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float4) -> float4 ``` |
| To | ``` prefix func -(_ rhs: float4) -> float4 ``` |

Modified -(_: float4x4) -> float4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float4x4) -> float4x4 ``` |
| To | ``` prefix func -(_ rhs: float4x4) -> float4x4 ``` |

Modified -(_: double4x4) -> double4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double4x4) -> double4x4 ``` |
| To | ``` prefix func -(_ rhs: double4x4) -> double4x4 ``` |

Modified -(_: float3x4) -> float3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float3x4) -> float3x4 ``` |
| To | ``` prefix func -(_ rhs: float3x4) -> float3x4 ``` |

Modified -(_: double2x2) -> double2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double2x2) -> double2x2 ``` |
| To | ``` prefix func -(_ rhs: double2x2) -> double2x2 ``` |

Modified -(_: int4) -> int4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: int4) -> int4 ``` |
| To | ``` prefix func -(_ rhs: int4) -> int4 ``` |

Modified -(_: double3) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double3) -> double3 ``` |
| To | ``` prefix func -(_ rhs: double3) -> double3 ``` |

Modified -(_: float2x2) -> float2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float2x2) -> float2x2 ``` |
| To | ``` prefix func -(_ rhs: float2x2) -> float2x2 ``` |

Modified -(_: float3) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: float3) -> float3 ``` |
| To | ``` prefix func -(_ rhs: float3) -> float3 ``` |

Modified -(_: double4) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: double4) -> double4 ``` |
| To | ``` prefix func -(_ rhs: double4) -> double4 ``` |

Modified -(_: int3) -> int3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result prefix func -(_ rhs: int3) -> int3 ``` |
| To | ``` prefix func -(_ rhs: int3) -> int3 ``` |

Modified -(_: double2x2, _: double2x2) -> double2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double2x2, _ rhs: double2x2) -> double2x2 ``` |
| To | ``` func -(_ lhs: double2x2, _ rhs: double2x2) -> double2x2 ``` |

Modified -(_: double4x3, _: double4x3) -> double4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double4x3, _ rhs: double4x3) -> double4x3 ``` |
| To | ``` func -(_ lhs: double4x3, _ rhs: double4x3) -> double4x3 ``` |

Modified -(_: float2x4, _: float2x4) -> float2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float2x4, _ rhs: float2x4) -> float2x4 ``` |
| To | ``` func -(_ lhs: float2x4, _ rhs: float2x4) -> float2x4 ``` |

Modified -(_: double4x4, _: double4x4) -> double4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double4x4, _ rhs: double4x4) -> double4x4 ``` |
| To | ``` func -(_ lhs: double4x4, _ rhs: double4x4) -> double4x4 ``` |

Modified -(_: float2x2, _: float2x2) -> float2x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float2x2, _ rhs: float2x2) -> float2x2 ``` |
| To | ``` func -(_ lhs: float2x2, _ rhs: float2x2) -> float2x2 ``` |

Modified -(_: float4, _: float4) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float4, _ rhs: float4) -> float4 ``` |
| To | ``` func -(_ lhs: float4, _ rhs: float4) -> float4 ``` |

Modified -(_: float4x3, _: float4x3) -> float4x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float4x3, _ rhs: float4x3) -> float4x3 ``` |
| To | ``` func -(_ lhs: float4x3, _ rhs: float4x3) -> float4x3 ``` |

Modified -(_: double2, _: double2) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double2, _ rhs: double2) -> double2 ``` |
| To | ``` func -(_ lhs: double2, _ rhs: double2) -> double2 ``` |

Modified -(_: double3, _: double3) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double3, _ rhs: double3) -> double3 ``` |
| To | ``` func -(_ lhs: double3, _ rhs: double3) -> double3 ``` |

Modified -(_: double2x3, _: double2x3) -> double2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double2x3, _ rhs: double2x3) -> double2x3 ``` |
| To | ``` func -(_ lhs: double2x3, _ rhs: double2x3) -> double2x3 ``` |

Modified -(_: double4, _: double4) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double4, _ rhs: double4) -> double4 ``` |
| To | ``` func -(_ lhs: double4, _ rhs: double4) -> double4 ``` |

Modified -(_: float3x4, _: float3x4) -> float3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float3x4, _ rhs: float3x4) -> float3x4 ``` |
| To | ``` func -(_ lhs: float3x4, _ rhs: float3x4) -> float3x4 ``` |

Modified -(_: float3x3, _: float3x3) -> float3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float3x3, _ rhs: float3x3) -> float3x3 ``` |
| To | ``` func -(_ lhs: float3x3, _ rhs: float3x3) -> float3x3 ``` |

Modified -(_: float4x4, _: float4x4) -> float4x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float4x4, _ rhs: float4x4) -> float4x4 ``` |
| To | ``` func -(_ lhs: float4x4, _ rhs: float4x4) -> float4x4 ``` |

Modified -(_: double3x4, _: double3x4) -> double3x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double3x4, _ rhs: double3x4) -> double3x4 ``` |
| To | ``` func -(_ lhs: double3x4, _ rhs: double3x4) -> double3x4 ``` |

Modified -(_: float2x3, _: float2x3) -> float2x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float2x3, _ rhs: float2x3) -> float2x3 ``` |
| To | ``` func -(_ lhs: float2x3, _ rhs: float2x3) -> float2x3 ``` |

Modified -(_: double2x4, _: double2x4) -> double2x4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double2x4, _ rhs: double2x4) -> double2x4 ``` |
| To | ``` func -(_ lhs: double2x4, _ rhs: double2x4) -> double2x4 ``` |

Modified -(_: float3x2, _: float3x2) -> float3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float3x2, _ rhs: float3x2) -> float3x2 ``` |
| To | ``` func -(_ lhs: float3x2, _ rhs: float3x2) -> float3x2 ``` |

Modified -(_: float3, _: float3) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float3, _ rhs: float3) -> float3 ``` |
| To | ``` func -(_ lhs: float3, _ rhs: float3) -> float3 ``` |

Modified -(_: float2, _: float2) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float2, _ rhs: float2) -> float2 ``` |
| To | ``` func -(_ lhs: float2, _ rhs: float2) -> float2 ``` |

Modified -(_: double4x2, _: double4x2) -> double4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double4x2, _ rhs: double4x2) -> double4x2 ``` |
| To | ``` func -(_ lhs: double4x2, _ rhs: double4x2) -> double4x2 ``` |

Modified -(_: double3x2, _: double3x2) -> double3x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double3x2, _ rhs: double3x2) -> double3x2 ``` |
| To | ``` func -(_ lhs: double3x2, _ rhs: double3x2) -> double3x2 ``` |

Modified -(_: double3x3, _: double3x3) -> double3x3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: double3x3, _ rhs: double3x3) -> double3x3 ``` |
| To | ``` func -(_ lhs: double3x3, _ rhs: double3x3) -> double3x3 ``` |

Modified -(_: float4x2, _: float4x2) -> float4x2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: float4x2, _ rhs: float4x2) -> float4x2 ``` |
| To | ``` func -(_ lhs: float4x2, _ rhs: float4x2) -> float4x2 ``` |

Modified -=(_: double2, _: double2)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double2, _ rhs: double2) ``` |
| To | ``` func -=(_ lhs: inout double2, _ rhs: double2) ``` |

Modified -=(_: float2x3, _: float2x3)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float2x3, _ rhs: float2x3) ``` |
| To | ``` func -=(_ lhs: inout float2x3, _ rhs: float2x3) ``` |

Modified -=(_: double3x4, _: double3x4)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double3x4, _ rhs: double3x4) ``` |
| To | ``` func -=(_ lhs: inout double3x4, _ rhs: double3x4) ``` |

Modified -=(_: float3x3, _: float3x3)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float3x3, _ rhs: float3x3) ``` |
| To | ``` func -=(_ lhs: inout float3x3, _ rhs: float3x3) ``` |

Modified -=(_: double2x3, _: double2x3)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double2x3, _ rhs: double2x3) ``` |
| To | ``` func -=(_ lhs: inout double2x3, _ rhs: double2x3) ``` |

Modified -=(_: double3x2, _: double3x2)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double3x2, _ rhs: double3x2) ``` |
| To | ``` func -=(_ lhs: inout double3x2, _ rhs: double3x2) ``` |

Modified -=(_: double2x2, _: double2x2)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double2x2, _ rhs: double2x2) ``` |
| To | ``` func -=(_ lhs: inout double2x2, _ rhs: double2x2) ``` |

Modified -=(_: float2x4, _: float2x4)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float2x4, _ rhs: float2x4) ``` |
| To | ``` func -=(_ lhs: inout float2x4, _ rhs: float2x4) ``` |

Modified -=(_: double3x3, _: double3x3)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double3x3, _ rhs: double3x3) ``` |
| To | ``` func -=(_ lhs: inout double3x3, _ rhs: double3x3) ``` |

Modified -=(_: float4x2, _: float4x2)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float4x2, _ rhs: float4x2) ``` |
| To | ``` func -=(_ lhs: inout float4x2, _ rhs: float4x2) ``` |

Modified -=(_: float4x4, _: float4x4)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float4x4, _ rhs: float4x4) ``` |
| To | ``` func -=(_ lhs: inout float4x4, _ rhs: float4x4) ``` |

Modified -=(_: float4x3, _: float4x3)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float4x3, _ rhs: float4x3) ``` |
| To | ``` func -=(_ lhs: inout float4x3, _ rhs: float4x3) ``` |

Modified -=(_: float2, _: float2)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float2, _ rhs: float2) ``` |
| To | ``` func -=(_ lhs: inout float2, _ rhs: float2) ``` |

Modified -=(_: double4x2, _: double4x2)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double4x2, _ rhs: double4x2) ``` |
| To | ``` func -=(_ lhs: inout double4x2, _ rhs: double4x2) ``` |

Modified -=(_: double4, _: double4)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double4, _ rhs: double4) ``` |
| To | ``` func -=(_ lhs: inout double4, _ rhs: double4) ``` |

Modified -=(_: float4, _: float4)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float4, _ rhs: float4) ``` |
| To | ``` func -=(_ lhs: inout float4, _ rhs: float4) ``` |

Modified -=(_: double2x4, _: double2x4)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double2x4, _ rhs: double2x4) ``` |
| To | ``` func -=(_ lhs: inout double2x4, _ rhs: double2x4) ``` |

Modified -=(_: double4x4, _: double4x4)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double4x4, _ rhs: double4x4) ``` |
| To | ``` func -=(_ lhs: inout double4x4, _ rhs: double4x4) ``` |

Modified -=(_: float2x2, _: float2x2)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float2x2, _ rhs: float2x2) ``` |
| To | ``` func -=(_ lhs: inout float2x2, _ rhs: float2x2) ``` |

Modified -=(_: double4x3, _: double4x3)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double4x3, _ rhs: double4x3) ``` |
| To | ``` func -=(_ lhs: inout double4x3, _ rhs: double4x3) ``` |

Modified -=(_: float3x4, _: float3x4)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float3x4, _ rhs: float3x4) ``` |
| To | ``` func -=(_ lhs: inout float3x4, _ rhs: float3x4) ``` |

Modified -=(_: float3, _: float3)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float3, _ rhs: float3) ``` |
| To | ``` func -=(_ lhs: inout float3, _ rhs: float3) ``` |

Modified -=(_: float3x2, _: float3x2)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: float3x2, _ rhs: float3x2) ``` |
| To | ``` func -=(_ lhs: inout float3x2, _ rhs: float3x2) ``` |

Modified -=(_: double3, _: double3)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: double3, _ rhs: double3) ``` |
| To | ``` func -=(_ lhs: inout double3, _ rhs: double3) ``` |

Modified /(_: float2, _: float2) -> float2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func /(_ lhs: float2, _ rhs: float2) -> float2 ``` |
| To | ``` func /(_ lhs: float2, _ rhs: float2) -> float2 ``` |

Modified /(_: int2, _: int2) -> int2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func /(_ lhs: int2, _ rhs: int2) -> int2 ``` |
| To | ``` func /(_ lhs: int2, _ rhs: int2) -> int2 ``` |

Modified /(_: double4, _: double4) -> double4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func /(_ lhs: double4, _ rhs: double4) -> double4 ``` |
| To | ``` func /(_ lhs: double4, _ rhs: double4) -> double4 ``` |

Modified /(_: double2, _: double2) -> double2

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func /(_ lhs: double2, _ rhs: double2) -> double2 ``` |
| To | ``` func /(_ lhs: double2, _ rhs: double2) -> double2 ``` |

Modified /(_: double3, _: double3) -> double3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func /(_ lhs: double3, _ rhs: double3) -> double3 ``` |
| To | ``` func /(_ lhs: double3, _ rhs: double3) -> double3 ``` |

Modified /(_: float4, _: float4) -> float4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func /(_ lhs: float4, _ rhs: float4) -> float4 ``` |
| To | ``` func /(_ lhs: float4, _ rhs: float4) -> float4 ``` |

Modified /(_: int4, _: int4) -> int4

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func /(_ lhs: int4, _ rhs: int4) -> int4 ``` |
| To | ``` func /(_ lhs: int4, _ rhs: int4) -> int4 ``` |

Modified /(_: float3, _: float3) -> float3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func /(_ lhs: float3, _ rhs: float3) -> float3 ``` |
| To | ``` func /(_ lhs: float3, _ rhs: float3) -> float3 ``` |

Modified /(_: int3, _: int3) -> int3

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func /(_ lhs: int3, _ rhs: int3) -> int3 ``` |
| To | ``` func /(_ lhs: int3, _ rhs: int3) -> int3 ``` |

Modified /=(_: double4, _: double4)

|  | Declaration |
| --- | --- |
| From | ``` func /=(inout _ lhs: double4, _ rhs: double4) ``` |
| To | ``` func /=(_ lhs: inout double4, _ rhs: double4) ``` |

Modified /=(_: int3, _: int3)

|  | Declaration |
| --- | --- |
| From | ``` func /=(inout _ lhs: int3, _ rhs: int3) ``` |
| To | ``` func /=(_ lhs: inout int3, _ rhs: int3) ``` |

Modified /=(_: float2, _: float2)

|  | Declaration |
| --- | --- |
| From | ``` func /=(inout _ lhs: float2, _ rhs: float2) ``` |
| To | ``` func /=(_ lhs: inout float2, _ rhs: float2) ``` |

Modified /=(_: float4, _: float4)

|  | Declaration |
| --- | --- |
| From | ``` func /=(inout _ lhs: float4, _ rhs: float4) ``` |
| To | ``` func /=(_ lhs: inout float4, _ rhs: float4) ``` |

Modified /=(_: float3, _: float3)

|  | Declaration |
| --- | --- |
| From | ``` func /=(inout _ lhs: float3, _ rhs: float3) ``` |
| To | ``` func /=(_ lhs: inout float3, _ rhs: float3) ``` |

Modified /=(_: int4, _: int4)

|  | Declaration |
| --- | --- |
| From | ``` func /=(inout _ lhs: int4, _ rhs: int4) ``` |
| To | ``` func /=(_ lhs: inout int4, _ rhs: int4) ``` |

Modified /=(_: double2, _: double2)

|  | Declaration |
| --- | --- |
| From | ``` func /=(inout _ lhs: double2, _ rhs: double2) ``` |
| To | ``` func /=(_ lhs: inout double2, _ rhs: double2) ``` |

Modified /=(_: double3, _: double3)

|  | Declaration |
| --- | --- |
| From | ``` func /=(inout _ lhs: double3, _ rhs: double3) ``` |
| To | ``` func /=(_ lhs: inout double3, _ rhs: double3) ``` |

Modified /=(_: int2, _: int2)

|  | Declaration |
| --- | --- |
| From | ``` func /=(inout _ lhs: int2, _ rhs: int2) ``` |
| To | ``` func /=(_ lhs: inout int2, _ rhs: int2) ``` |

Modified [abs(_: int4) -> int4](https://developer.apple.com/documentation/simd/1425956-abs)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func abs(_ x: int4) -> int4 ``` |
| To | ``` func abs(_ x: int4) -> int4 ``` |

Modified [abs(_: float3) -> float3](https://developer.apple.com/documentation/simd/1425562-abs)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func abs(_ x: float3) -> float3 ``` |
| To | ``` func abs(_ x: float3) -> float3 ``` |

Modified [abs(_: double3) -> double3](https://developer.apple.com/documentation/simd/1425474-abs)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func abs(_ x: double3) -> double3 ``` |
| To | ``` func abs(_ x: double3) -> double3 ``` |

Modified [abs(_: float2) -> float2](https://developer.apple.com/documentation/simd/1424564-abs)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func abs(_ x: float2) -> float2 ``` |
| To | ``` func abs(_ x: float2) -> float2 ``` |

Modified [abs(_: int3) -> int3](https://developer.apple.com/documentation/simd/1424075-abs)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func abs(_ x: int3) -> int3 ``` |
| To | ``` func abs(_ x: int3) -> int3 ``` |

Modified [abs(_: int2) -> int2](https://developer.apple.com/documentation/simd/1425358-abs)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func abs(_ x: int2) -> int2 ``` |
| To | ``` func abs(_ x: int2) -> int2 ``` |

Modified [abs(_: double2) -> double2](https://developer.apple.com/documentation/simd/1424038-abs)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func abs(_ x: double2) -> double2 ``` |
| To | ``` func abs(_ x: double2) -> double2 ``` |

Modified [abs(_: float4) -> float4](https://developer.apple.com/documentation/simd/1424627-abs)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func abs(_ x: float4) -> float4 ``` |
| To | ``` func abs(_ x: float4) -> float4 ``` |

Modified [abs(_: double4) -> double4](https://developer.apple.com/documentation/simd/1425342-abs)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func abs(_ x: double4) -> double4 ``` |
| To | ``` func abs(_ x: double4) -> double4 ``` |

Modified [ceil(_: float4) -> float4](https://developer.apple.com/documentation/simd/1424649-ceil)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ceil(_ x: float4) -> float4 ``` |
| To | ``` func ceil(_ x: float4) -> float4 ``` |

Modified [ceil(_: float3) -> float3](https://developer.apple.com/documentation/simd/1425334-ceil)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ceil(_ x: float3) -> float3 ``` |
| To | ``` func ceil(_ x: float3) -> float3 ``` |

Modified [ceil(_: double2) -> double2](https://developer.apple.com/documentation/simd/1424139-ceil)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ceil(_ x: double2) -> double2 ``` |
| To | ``` func ceil(_ x: double2) -> double2 ``` |

Modified [ceil(_: double3) -> double3](https://developer.apple.com/documentation/simd/1424244-ceil)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ceil(_ x: double3) -> double3 ``` |
| To | ``` func ceil(_ x: double3) -> double3 ``` |

Modified [ceil(_: double4) -> double4](https://developer.apple.com/documentation/simd/1424460-ceil)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ceil(_ x: double4) -> double4 ``` |
| To | ``` func ceil(_ x: double4) -> double4 ``` |

Modified [ceil(_: float2) -> float2](https://developer.apple.com/documentation/simd/1424572-ceil)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ceil(_ x: float2) -> float2 ``` |
| To | ``` func ceil(_ x: float2) -> float2 ``` |

Modified [clamp(_: double4, min: double4, max: double4) -> double4](https://developer.apple.com/documentation/simd/1424085-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: double4, min min: double4, max max: double4) -> double4 ``` |
| To | ``` func clamp(_ x: double4, min min: double4, max max: double4) -> double4 ``` |

Modified [clamp(_: float2, min: Float, max: Float) -> float2](https://developer.apple.com/documentation/simd/1425100-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: float2, min min: Float, max max: Float) -> float2 ``` |
| To | ``` func clamp(_ x: float2, min min: Float, max max: Float) -> float2 ``` |

Modified [clamp(_: int4, min: Int32, max: Int32) -> int4](https://developer.apple.com/documentation/simd/1424889-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: int4, min min: Int32, max max: Int32) -> int4 ``` |
| To | ``` func clamp(_ x: int4, min min: Int32, max max: Int32) -> int4 ``` |

Modified [clamp(_: int3, min: int3, max: int3) -> int3](https://developer.apple.com/documentation/simd/1424774-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: int3, min min: int3, max max: int3) -> int3 ``` |
| To | ``` func clamp(_ x: int3, min min: int3, max max: int3) -> int3 ``` |

Modified [clamp(_: float4, min: Float, max: Float) -> float4](https://developer.apple.com/documentation/simd/1424237-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: float4, min min: Float, max max: Float) -> float4 ``` |
| To | ``` func clamp(_ x: float4, min min: Float, max max: Float) -> float4 ``` |

Modified [clamp(_: int4, min: int4, max: int4) -> int4](https://developer.apple.com/documentation/simd/1424945-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: int4, min min: int4, max max: int4) -> int4 ``` |
| To | ``` func clamp(_ x: int4, min min: int4, max max: int4) -> int4 ``` |

Modified [clamp(_: int2, min: int2, max: int2) -> int2](https://developer.apple.com/documentation/simd/1425740-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: int2, min min: int2, max max: int2) -> int2 ``` |
| To | ``` func clamp(_ x: int2, min min: int2, max max: int2) -> int2 ``` |

Modified [clamp(_: float2, min: float2, max: float2) -> float2](https://developer.apple.com/documentation/simd/1424099-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: float2, min min: float2, max max: float2) -> float2 ``` |
| To | ``` func clamp(_ x: float2, min min: float2, max max: float2) -> float2 ``` |

Modified [clamp(_: int2, min: Int32, max: Int32) -> int2](https://developer.apple.com/documentation/simd/1425726-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: int2, min min: Int32, max max: Int32) -> int2 ``` |
| To | ``` func clamp(_ x: int2, min min: Int32, max max: Int32) -> int2 ``` |

Modified [clamp(_: float3, min: float3, max: float3) -> float3](https://developer.apple.com/documentation/simd/1424703-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: float3, min min: float3, max max: float3) -> float3 ``` |
| To | ``` func clamp(_ x: float3, min min: float3, max max: float3) -> float3 ``` |

Modified [clamp(_: double2, min: double2, max: double2) -> double2](https://developer.apple.com/documentation/simd/1424444-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: double2, min min: double2, max max: double2) -> double2 ``` |
| To | ``` func clamp(_ x: double2, min min: double2, max max: double2) -> double2 ``` |

Modified [clamp(_: int3, min: Int32, max: Int32) -> int3](https://developer.apple.com/documentation/simd/1425756-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: int3, min min: Int32, max max: Int32) -> int3 ``` |
| To | ``` func clamp(_ x: int3, min min: Int32, max max: Int32) -> int3 ``` |

Modified [clamp(_: double2, min: Double, max: Double) -> double2](https://developer.apple.com/documentation/simd/1424903-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: double2, min min: Double, max max: Double) -> double2 ``` |
| To | ``` func clamp(_ x: double2, min min: Double, max max: Double) -> double2 ``` |

Modified [clamp(_: float4, min: float4, max: float4) -> float4](https://developer.apple.com/documentation/simd/1425778-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: float4, min min: float4, max max: float4) -> float4 ``` |
| To | ``` func clamp(_ x: float4, min min: float4, max max: float4) -> float4 ``` |

Modified [clamp(_: float3, min: Float, max: Float) -> float3](https://developer.apple.com/documentation/simd/1425461-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: float3, min min: Float, max max: Float) -> float3 ``` |
| To | ``` func clamp(_ x: float3, min min: Float, max max: Float) -> float3 ``` |

Modified [clamp(_: double3, min: Double, max: Double) -> double3](https://developer.apple.com/documentation/simd/1425835-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: double3, min min: Double, max max: Double) -> double3 ``` |
| To | ``` func clamp(_ x: double3, min min: Double, max max: Double) -> double3 ``` |

Modified [clamp(_: double4, min: Double, max: Double) -> double4](https://developer.apple.com/documentation/simd/1424320-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: double4, min min: Double, max max: Double) -> double4 ``` |
| To | ``` func clamp(_ x: double4, min min: Double, max max: Double) -> double4 ``` |

Modified [clamp(_: double3, min: double3, max: double3) -> double3](https://developer.apple.com/documentation/simd/1424826-clamp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func clamp(_ x: double3, min min: double3, max max: double3) -> double3 ``` |
| To | ``` func clamp(_ x: double3, min min: double3, max max: double3) -> double3 ``` |

Modified [cross(_: double3, _: double3) -> double3](https://developer.apple.com/documentation/simd/1425041-cross)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cross(_ x: double3, _ y: double3) -> double3 ``` |
| To | ``` func cross(_ x: double3, _ y: double3) -> double3 ``` |

Modified [cross(_: float2, _: float2) -> float3](https://developer.apple.com/documentation/simd/1425055-cross)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cross(_ x: float2, _ y: float2) -> float3 ``` |
| To | ``` func cross(_ x: float2, _ y: float2) -> float3 ``` |

Modified [cross(_: float3, _: float3) -> float3](https://developer.apple.com/documentation/simd/1425275-cross)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cross(_ x: float3, _ y: float3) -> float3 ``` |
| To | ``` func cross(_ x: float3, _ y: float3) -> float3 ``` |

Modified [cross(_: double2, _: double2) -> double3](https://developer.apple.com/documentation/simd/1425908-cross)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cross(_ x: double2, _ y: double2) -> double3 ``` |
| To | ``` func cross(_ x: double2, _ y: double2) -> double3 ``` |

Modified [distance(_: double2, _: double2) -> Double](https://developer.apple.com/documentation/simd/1426116-distance)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance(_ x: double2, _ y: double2) -> Double ``` |
| To | ``` func distance(_ x: double2, _ y: double2) -> Double ``` |

Modified [distance(_: float4, _: float4) -> Float](https://developer.apple.com/documentation/simd/1426295-distance)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance(_ x: float4, _ y: float4) -> Float ``` |
| To | ``` func distance(_ x: float4, _ y: float4) -> Float ``` |

Modified [distance(_: double4, _: double4) -> Double](https://developer.apple.com/documentation/simd/1424334-distance)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance(_ x: double4, _ y: double4) -> Double ``` |
| To | ``` func distance(_ x: double4, _ y: double4) -> Double ``` |

Modified [distance(_: float3, _: float3) -> Float](https://developer.apple.com/documentation/simd/1424991-distance)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance(_ x: float3, _ y: float3) -> Float ``` |
| To | ``` func distance(_ x: float3, _ y: float3) -> Float ``` |

Modified [distance(_: double3, _: double3) -> Double](https://developer.apple.com/documentation/simd/1425128-distance)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance(_ x: double3, _ y: double3) -> Double ``` |
| To | ``` func distance(_ x: double3, _ y: double3) -> Double ``` |

Modified [distance(_: float2, _: float2) -> Float](https://developer.apple.com/documentation/simd/1426060-distance)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance(_ x: float2, _ y: float2) -> Float ``` |
| To | ``` func distance(_ x: float2, _ y: float2) -> Float ``` |

Modified [distance_squared(_: double3, _: double3) -> Double](https://developer.apple.com/documentation/simd/1425021-distance_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance_squared(_ x: double3, _ y: double3) -> Double ``` |
| To | ``` func distance_squared(_ x: double3, _ y: double3) -> Double ``` |

Modified [distance_squared(_: float3, _: float3) -> Float](https://developer.apple.com/documentation/simd/1425820-distance_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance_squared(_ x: float3, _ y: float3) -> Float ``` |
| To | ``` func distance_squared(_ x: float3, _ y: float3) -> Float ``` |

Modified [distance_squared(_: double2, _: double2) -> Double](https://developer.apple.com/documentation/simd/1424071-distance_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance_squared(_ x: double2, _ y: double2) -> Double ``` |
| To | ``` func distance_squared(_ x: double2, _ y: double2) -> Double ``` |

Modified [distance_squared(_: float4, _: float4) -> Float](https://developer.apple.com/documentation/simd/1426170-distance_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance_squared(_ x: float4, _ y: float4) -> Float ``` |
| To | ``` func distance_squared(_ x: float4, _ y: float4) -> Float ``` |

Modified [distance_squared(_: float2, _: float2) -> Float](https://developer.apple.com/documentation/simd/1425086-distance_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance_squared(_ x: float2, _ y: float2) -> Float ``` |
| To | ``` func distance_squared(_ x: float2, _ y: float2) -> Float ``` |

Modified [distance_squared(_: double4, _: double4) -> Double](https://developer.apple.com/documentation/simd/1424440-distance_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func distance_squared(_ x: double4, _ y: double4) -> Double ``` |
| To | ``` func distance_squared(_ x: double4, _ y: double4) -> Double ``` |

Modified [dot(_: float4, _: float4) -> Float](https://developer.apple.com/documentation/simd/1425023-dot)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func dot(_ x: float4, _ y: float4) -> Float ``` |
| To | ``` func dot(_ x: float4, _ y: float4) -> Float ``` |

Modified [dot(_: double4, _: double4) -> Double](https://developer.apple.com/documentation/simd/1424326-dot)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func dot(_ x: double4, _ y: double4) -> Double ``` |
| To | ``` func dot(_ x: double4, _ y: double4) -> Double ``` |

Modified [dot(_: float3, _: float3) -> Float](https://developer.apple.com/documentation/simd/1425918-dot)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func dot(_ x: float3, _ y: float3) -> Float ``` |
| To | ``` func dot(_ x: float3, _ y: float3) -> Float ``` |

Modified [dot(_: double3, _: double3) -> Double](https://developer.apple.com/documentation/simd/1424226-dot)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func dot(_ x: double3, _ y: double3) -> Double ``` |
| To | ``` func dot(_ x: double3, _ y: double3) -> Double ``` |

Modified [dot(_: float2, _: float2) -> Float](https://developer.apple.com/documentation/simd/1424972-dot)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func dot(_ x: float2, _ y: float2) -> Float ``` |
| To | ``` func dot(_ x: float2, _ y: float2) -> Float ``` |

Modified [dot(_: double2, _: double2) -> Double](https://developer.apple.com/documentation/simd/1426158-dot)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func dot(_ x: double2, _ y: double2) -> Double ``` |
| To | ``` func dot(_ x: double2, _ y: double2) -> Double ``` |

Modified [floor(_: double2) -> double2](https://developer.apple.com/documentation/simd/1425027-floor)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func floor(_ x: double2) -> double2 ``` |
| To | ``` func floor(_ x: double2) -> double2 ``` |

Modified [floor(_: double4) -> double4](https://developer.apple.com/documentation/simd/1425378-floor)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func floor(_ x: double4) -> double4 ``` |
| To | ``` func floor(_ x: double4) -> double4 ``` |

Modified [floor(_: float2) -> float2](https://developer.apple.com/documentation/simd/1425500-floor)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func floor(_ x: float2) -> float2 ``` |
| To | ``` func floor(_ x: float2) -> float2 ``` |

Modified [floor(_: float3) -> float3](https://developer.apple.com/documentation/simd/1425267-floor)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func floor(_ x: float3) -> float3 ``` |
| To | ``` func floor(_ x: float3) -> float3 ``` |

Modified [floor(_: double3) -> double3](https://developer.apple.com/documentation/simd/1424312-floor)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func floor(_ x: double3) -> double3 ``` |
| To | ``` func floor(_ x: double3) -> double3 ``` |

Modified [floor(_: float4) -> float4](https://developer.apple.com/documentation/simd/1424993-floor)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func floor(_ x: float4) -> float4 ``` |
| To | ``` func floor(_ x: float4) -> float4 ``` |

Modified [fmax(_: double4, _: double4) -> double4](https://developer.apple.com/documentation/simd/1426120-fmax)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmax(_ x: double4, _ y: double4) -> double4 ``` |
| To | ``` func fmax(_ x: double4, _ y: double4) -> double4 ``` |

Modified [fmax(_: float3, _: float3) -> float3](https://developer.apple.com/documentation/simd/1425925-fmax)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmax(_ x: float3, _ y: float3) -> float3 ``` |
| To | ``` func fmax(_ x: float3, _ y: float3) -> float3 ``` |

Modified [fmax(_: double2, _: double2) -> double2](https://developer.apple.com/documentation/simd/1425386-fmax)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmax(_ x: double2, _ y: double2) -> double2 ``` |
| To | ``` func fmax(_ x: double2, _ y: double2) -> double2 ``` |

Modified [fmax(_: float2, _: float2) -> float2](https://developer.apple.com/documentation/simd/1424077-fmax)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmax(_ x: float2, _ y: float2) -> float2 ``` |
| To | ``` func fmax(_ x: float2, _ y: float2) -> float2 ``` |

Modified [fmax(_: float4, _: float4) -> float4](https://developer.apple.com/documentation/simd/1425380-fmax)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmax(_ x: float4, _ y: float4) -> float4 ``` |
| To | ``` func fmax(_ x: float4, _ y: float4) -> float4 ``` |

Modified [fmax(_: double3, _: double3) -> double3](https://developer.apple.com/documentation/simd/1424948-fmax)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmax(_ x: double3, _ y: double3) -> double3 ``` |
| To | ``` func fmax(_ x: double3, _ y: double3) -> double3 ``` |

Modified [fmin(_: float4, _: float4) -> float4](https://developer.apple.com/documentation/simd/1425132-fmin)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmin(_ x: float4, _ y: float4) -> float4 ``` |
| To | ``` func fmin(_ x: float4, _ y: float4) -> float4 ``` |

Modified [fmin(_: double4, _: double4) -> double4](https://developer.apple.com/documentation/simd/1425812-fmin)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmin(_ x: double4, _ y: double4) -> double4 ``` |
| To | ``` func fmin(_ x: double4, _ y: double4) -> double4 ``` |

Modified [fmin(_: float3, _: float3) -> float3](https://developer.apple.com/documentation/simd/1424926-fmin)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmin(_ x: float3, _ y: float3) -> float3 ``` |
| To | ``` func fmin(_ x: float3, _ y: float3) -> float3 ``` |

Modified [fmin(_: float2, _: float2) -> float2](https://developer.apple.com/documentation/simd/1425676-fmin)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmin(_ x: float2, _ y: float2) -> float2 ``` |
| To | ``` func fmin(_ x: float2, _ y: float2) -> float2 ``` |

Modified [fmin(_: double2, _: double2) -> double2](https://developer.apple.com/documentation/simd/1425651-fmin)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmin(_ x: double2, _ y: double2) -> double2 ``` |
| To | ``` func fmin(_ x: double2, _ y: double2) -> double2 ``` |

Modified [fmin(_: double3, _: double3) -> double3](https://developer.apple.com/documentation/simd/1424555-fmin)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmin(_ x: double3, _ y: double3) -> double3 ``` |
| To | ``` func fmin(_ x: double3, _ y: double3) -> double3 ``` |

Modified [fract(_: float3) -> float3](https://developer.apple.com/documentation/simd/1425146-fract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fract(_ x: float3) -> float3 ``` |
| To | ``` func fract(_ x: float3) -> float3 ``` |

Modified [fract(_: float2) -> float2](https://developer.apple.com/documentation/simd/1424503-fract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fract(_ x: float2) -> float2 ``` |
| To | ``` func fract(_ x: float2) -> float2 ``` |

Modified [fract(_: double4) -> double4](https://developer.apple.com/documentation/simd/1425760-fract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fract(_ x: double4) -> double4 ``` |
| To | ``` func fract(_ x: double4) -> double4 ``` |

Modified [fract(_: float4) -> float4](https://developer.apple.com/documentation/simd/1426347-fract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fract(_ x: float4) -> float4 ``` |
| To | ``` func fract(_ x: float4) -> float4 ``` |

Modified [fract(_: double3) -> double3](https://developer.apple.com/documentation/simd/1424810-fract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fract(_ x: double3) -> double3 ``` |
| To | ``` func fract(_ x: double3) -> double3 ``` |

Modified [fract(_: double2) -> double2](https://developer.apple.com/documentation/simd/1424568-fract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fract(_ x: double2) -> double2 ``` |
| To | ``` func fract(_ x: double2) -> double2 ``` |

Modified [length(_: float3) -> Float](https://developer.apple.com/documentation/simd/1425508-length)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length(_ x: float3) -> Float ``` |
| To | ``` func length(_ x: float3) -> Float ``` |

Modified [length(_: float2) -> Float](https://developer.apple.com/documentation/simd/1425738-length)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length(_ x: float2) -> Float ``` |
| To | ``` func length(_ x: float2) -> Float ``` |

Modified [length(_: float4) -> Float](https://developer.apple.com/documentation/simd/1425346-length)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length(_ x: float4) -> Float ``` |
| To | ``` func length(_ x: float4) -> Float ``` |

Modified [length(_: double3) -> Double](https://developer.apple.com/documentation/simd/1425079-length)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length(_ x: double3) -> Double ``` |
| To | ``` func length(_ x: double3) -> Double ``` |

Modified [length(_: double4) -> Double](https://developer.apple.com/documentation/simd/1425728-length)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length(_ x: double4) -> Double ``` |
| To | ``` func length(_ x: double4) -> Double ``` |

Modified [length(_: double2) -> Double](https://developer.apple.com/documentation/simd/1425329-length)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length(_ x: double2) -> Double ``` |
| To | ``` func length(_ x: double2) -> Double ``` |

Modified [length_squared(_: double3) -> Double](https://developer.apple.com/documentation/simd/1425432-length_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length_squared(_ x: double3) -> Double ``` |
| To | ``` func length_squared(_ x: double3) -> Double ``` |

Modified [length_squared(_: double2) -> Double](https://developer.apple.com/documentation/simd/1425912-length_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length_squared(_ x: double2) -> Double ``` |
| To | ``` func length_squared(_ x: double2) -> Double ``` |

Modified [length_squared(_: float4) -> Float](https://developer.apple.com/documentation/simd/1425075-length_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length_squared(_ x: float4) -> Float ``` |
| To | ``` func length_squared(_ x: float4) -> Float ``` |

Modified [length_squared(_: double4) -> Double](https://developer.apple.com/documentation/simd/1425126-length_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length_squared(_ x: double4) -> Double ``` |
| To | ``` func length_squared(_ x: double4) -> Double ``` |

Modified [length_squared(_: float3) -> Float](https://developer.apple.com/documentation/simd/1425884-length_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length_squared(_ x: float3) -> Float ``` |
| To | ``` func length_squared(_ x: float3) -> Float ``` |

Modified [length_squared(_: float2) -> Float](https://developer.apple.com/documentation/simd/1424456-length_squared)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func length_squared(_ x: float2) -> Float ``` |
| To | ``` func length_squared(_ x: float2) -> Float ``` |

Modified [max(_: int2, _: Int32) -> int2](https://developer.apple.com/documentation/simd/1426341-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ vector: int2, _ scalar: Int32) -> int2 ``` |
| To | ``` func max(_ vector: int2, _ scalar: Int32) -> int2 ``` |

Modified [max(_: float4, _: Float) -> float4](https://developer.apple.com/documentation/simd/1425546-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ vector: float4, _ scalar: Float) -> float4 ``` |
| To | ``` func max(_ vector: float4, _ scalar: Float) -> float4 ``` |

Modified [max(_: float2, _: Float) -> float2](https://developer.apple.com/documentation/simd/1425786-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ vector: float2, _ scalar: Float) -> float2 ``` |
| To | ``` func max(_ vector: float2, _ scalar: Float) -> float2 ``` |

Modified [max(_: double4, _: Double) -> double4](https://developer.apple.com/documentation/simd/1424735-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ vector: double4, _ scalar: Double) -> double4 ``` |
| To | ``` func max(_ vector: double4, _ scalar: Double) -> double4 ``` |

Modified [max(_: int4, _: Int32) -> int4](https://developer.apple.com/documentation/simd/1424839-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ vector: int4, _ scalar: Int32) -> int4 ``` |
| To | ``` func max(_ vector: int4, _ scalar: Int32) -> int4 ``` |

Modified [max(_: double2, _: double2) -> double2](https://developer.apple.com/documentation/simd/1424117-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ x: double2, _ y: double2) -> double2 ``` |
| To | ``` func max(_ x: double2, _ y: double2) -> double2 ``` |

Modified [max(_: double3, _: double3) -> double3](https://developer.apple.com/documentation/simd/1425607-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ x: double3, _ y: double3) -> double3 ``` |
| To | ``` func max(_ x: double3, _ y: double3) -> double3 ``` |

Modified [max(_: float3, _: Float) -> float3](https://developer.apple.com/documentation/simd/1424834-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ vector: float3, _ scalar: Float) -> float3 ``` |
| To | ``` func max(_ vector: float3, _ scalar: Float) -> float3 ``` |

Modified [max(_: int3, _: int3) -> int3](https://developer.apple.com/documentation/simd/1425185-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ x: int3, _ y: int3) -> int3 ``` |
| To | ``` func max(_ x: int3, _ y: int3) -> int3 ``` |

Modified [max(_: double4, _: double4) -> double4](https://developer.apple.com/documentation/simd/1425077-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ x: double4, _ y: double4) -> double4 ``` |
| To | ``` func max(_ x: double4, _ y: double4) -> double4 ``` |

Modified [max(_: float2, _: float2) -> float2](https://developer.apple.com/documentation/simd/1425356-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ x: float2, _ y: float2) -> float2 ``` |
| To | ``` func max(_ x: float2, _ y: float2) -> float2 ``` |

Modified [max(_: float4, _: float4) -> float4](https://developer.apple.com/documentation/simd/1424152-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ x: float4, _ y: float4) -> float4 ``` |
| To | ``` func max(_ x: float4, _ y: float4) -> float4 ``` |

Modified [max(_: float3, _: float3) -> float3](https://developer.apple.com/documentation/simd/1425006-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ x: float3, _ y: float3) -> float3 ``` |
| To | ``` func max(_ x: float3, _ y: float3) -> float3 ``` |

Modified [max(_: int4, _: int4) -> int4](https://developer.apple.com/documentation/simd/1424533-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ x: int4, _ y: int4) -> int4 ``` |
| To | ``` func max(_ x: int4, _ y: int4) -> int4 ``` |

Modified [max(_: int2, _: int2) -> int2](https://developer.apple.com/documentation/simd/1424048-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ x: int2, _ y: int2) -> int2 ``` |
| To | ``` func max(_ x: int2, _ y: int2) -> int2 ``` |

Modified [max(_: double3, _: Double) -> double3](https://developer.apple.com/documentation/simd/1425008-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ vector: double3, _ scalar: Double) -> double3 ``` |
| To | ``` func max(_ vector: double3, _ scalar: Double) -> double3 ``` |

Modified [max(_: double2, _: Double) -> double2](https://developer.apple.com/documentation/simd/1424515-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ vector: double2, _ scalar: Double) -> double2 ``` |
| To | ``` func max(_ vector: double2, _ scalar: Double) -> double2 ``` |

Modified [max(_: int3, _: Int32) -> int3](https://developer.apple.com/documentation/simd/1424645-max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func max(_ vector: int3, _ scalar: Int32) -> int3 ``` |
| To | ``` func max(_ vector: int3, _ scalar: Int32) -> int3 ``` |

Modified [min(_: float2, _: Float) -> float2](https://developer.apple.com/documentation/simd/1425939-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ vector: float2, _ scalar: Float) -> float2 ``` |
| To | ``` func min(_ vector: float2, _ scalar: Float) -> float2 ``` |

Modified [min(_: int2, _: Int32) -> int2](https://developer.apple.com/documentation/simd/1425448-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ vector: int2, _ scalar: Int32) -> int2 ``` |
| To | ``` func min(_ vector: int2, _ scalar: Int32) -> int2 ``` |

Modified [min(_: int4, _: int4) -> int4](https://developer.apple.com/documentation/simd/1425991-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ x: int4, _ y: int4) -> int4 ``` |
| To | ``` func min(_ x: int4, _ y: int4) -> int4 ``` |

Modified [min(_: int3, _: int3) -> int3](https://developer.apple.com/documentation/simd/1426097-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ x: int3, _ y: int3) -> int3 ``` |
| To | ``` func min(_ x: int3, _ y: int3) -> int3 ``` |

Modified [min(_: float4, _: float4) -> float4](https://developer.apple.com/documentation/simd/1424173-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ x: float4, _ y: float4) -> float4 ``` |
| To | ``` func min(_ x: float4, _ y: float4) -> float4 ``` |

Modified [min(_: int2, _: int2) -> int2](https://developer.apple.com/documentation/simd/1425033-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ x: int2, _ y: int2) -> int2 ``` |
| To | ``` func min(_ x: int2, _ y: int2) -> int2 ``` |

Modified [min(_: float3, _: Float) -> float3](https://developer.apple.com/documentation/simd/1426129-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ vector: float3, _ scalar: Float) -> float3 ``` |
| To | ``` func min(_ vector: float3, _ scalar: Float) -> float3 ``` |

Modified [min(_: float4, _: Float) -> float4](https://developer.apple.com/documentation/simd/1424357-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ vector: float4, _ scalar: Float) -> float4 ``` |
| To | ``` func min(_ vector: float4, _ scalar: Float) -> float4 ``` |

Modified [min(_: double4, _: double4) -> double4](https://developer.apple.com/documentation/simd/1425411-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ x: double4, _ y: double4) -> double4 ``` |
| To | ``` func min(_ x: double4, _ y: double4) -> double4 ``` |

Modified [min(_: float3, _: float3) -> float3](https://developer.apple.com/documentation/simd/1424135-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ x: float3, _ y: float3) -> float3 ``` |
| To | ``` func min(_ x: float3, _ y: float3) -> float3 ``` |

Modified [min(_: double4, _: Double) -> double4](https://developer.apple.com/documentation/simd/1426273-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ vector: double4, _ scalar: Double) -> double4 ``` |
| To | ``` func min(_ vector: double4, _ scalar: Double) -> double4 ``` |

Modified [min(_: int4, _: Int32) -> int4](https://developer.apple.com/documentation/simd/1424113-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ vector: int4, _ scalar: Int32) -> int4 ``` |
| To | ``` func min(_ vector: int4, _ scalar: Int32) -> int4 ``` |

Modified [min(_: double3, _: double3) -> double3](https://developer.apple.com/documentation/simd/1425224-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ x: double3, _ y: double3) -> double3 ``` |
| To | ``` func min(_ x: double3, _ y: double3) -> double3 ``` |

Modified [min(_: double3, _: Double) -> double3](https://developer.apple.com/documentation/simd/1425247-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ vector: double3, _ scalar: Double) -> double3 ``` |
| To | ``` func min(_ vector: double3, _ scalar: Double) -> double3 ``` |

Modified [min(_: float2, _: float2) -> float2](https://developer.apple.com/documentation/simd/1425867-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ x: float2, _ y: float2) -> float2 ``` |
| To | ``` func min(_ x: float2, _ y: float2) -> float2 ``` |

Modified [min(_: double2, _: Double) -> double2](https://developer.apple.com/documentation/simd/1425517-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ vector: double2, _ scalar: Double) -> double2 ``` |
| To | ``` func min(_ vector: double2, _ scalar: Double) -> double2 ``` |

Modified [min(_: int3, _: Int32) -> int3](https://developer.apple.com/documentation/simd/1425527-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ vector: int3, _ scalar: Int32) -> int3 ``` |
| To | ``` func min(_ vector: int3, _ scalar: Int32) -> int3 ``` |

Modified [min(_: double2, _: double2) -> double2](https://developer.apple.com/documentation/simd/1425057-min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func min(_ x: double2, _ y: double2) -> double2 ``` |
| To | ``` func min(_ x: double2, _ y: double2) -> double2 ``` |

Modified [mix(_: double2, _: double2, t: Double) -> double2](https://developer.apple.com/documentation/simd/1424104-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: double2, _ y: double2, t t: Double) -> double2 ``` |
| To | ``` func mix(_ x: double2, _ y: double2, t t: Double) -> double2 ``` |

Modified [mix(_: float2, _: float2, t: Float) -> float2](https://developer.apple.com/documentation/simd/1425404-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: float2, _ y: float2, t t: Float) -> float2 ``` |
| To | ``` func mix(_ x: float2, _ y: float2, t t: Float) -> float2 ``` |

Modified [mix(_: float2, _: float2, t: float2) -> float2](https://developer.apple.com/documentation/simd/1425480-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: float2, _ y: float2, t t: float2) -> float2 ``` |
| To | ``` func mix(_ x: float2, _ y: float2, t t: float2) -> float2 ``` |

Modified [mix(_: float3, _: float3, t: Float) -> float3](https://developer.apple.com/documentation/simd/1425031-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: float3, _ y: float3, t t: Float) -> float3 ``` |
| To | ``` func mix(_ x: float3, _ y: float3, t t: Float) -> float3 ``` |

Modified [mix(_: float4, _: float4, t: Float) -> float4](https://developer.apple.com/documentation/simd/1425169-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: float4, _ y: float4, t t: Float) -> float4 ``` |
| To | ``` func mix(_ x: float4, _ y: float4, t t: Float) -> float4 ``` |

Modified [mix(_: double4, _: double4, t: double4) -> double4](https://developer.apple.com/documentation/simd/1424778-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: double4, _ y: double4, t t: double4) -> double4 ``` |
| To | ``` func mix(_ x: double4, _ y: double4, t t: double4) -> double4 ``` |

Modified [mix(_: double4, _: double4, t: Double) -> double4](https://developer.apple.com/documentation/simd/1426327-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: double4, _ y: double4, t t: Double) -> double4 ``` |
| To | ``` func mix(_ x: double4, _ y: double4, t t: Double) -> double4 ``` |

Modified [mix(_: float4, _: float4, t: float4) -> float4](https://developer.apple.com/documentation/simd/1424450-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: float4, _ y: float4, t t: float4) -> float4 ``` |
| To | ``` func mix(_ x: float4, _ y: float4, t t: float4) -> float4 ``` |

Modified [mix(_: double2, _: double2, t: double2) -> double2](https://developer.apple.com/documentation/simd/1425576-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: double2, _ y: double2, t t: double2) -> double2 ``` |
| To | ``` func mix(_ x: double2, _ y: double2, t t: double2) -> double2 ``` |

Modified [mix(_: double3, _: double3, t: Double) -> double3](https://developer.apple.com/documentation/simd/1425662-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: double3, _ y: double3, t t: Double) -> double3 ``` |
| To | ``` func mix(_ x: double3, _ y: double3, t t: Double) -> double3 ``` |

Modified [mix(_: float3, _: float3, t: float3) -> float3](https://developer.apple.com/documentation/simd/1424891-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: float3, _ y: float3, t t: float3) -> float3 ``` |
| To | ``` func mix(_ x: float3, _ y: float3, t t: float3) -> float3 ``` |

Modified [mix(_: double3, _: double3, t: double3) -> double3](https://developer.apple.com/documentation/simd/1424171-mix)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func mix(_ x: double3, _ y: double3, t t: double3) -> double3 ``` |
| To | ``` func mix(_ x: double3, _ y: double3, t t: double3) -> double3 ``` |

Modified [norm_inf(_: double2) -> Double](https://developer.apple.com/documentation/simd/1426205-norm_inf)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_inf(_ x: double2) -> Double ``` |
| To | ``` func norm_inf(_ x: double2) -> Double ``` |

Modified [norm_inf(_: double4) -> Double](https://developer.apple.com/documentation/simd/1425601-norm_inf)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_inf(_ x: double4) -> Double ``` |
| To | ``` func norm_inf(_ x: double4) -> Double ``` |

Modified [norm_inf(_: float3) -> Float](https://developer.apple.com/documentation/simd/1425859-norm_inf)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_inf(_ x: float3) -> Float ``` |
| To | ``` func norm_inf(_ x: float3) -> Float ``` |

Modified [norm_inf(_: float4) -> Float](https://developer.apple.com/documentation/simd/1424091-norm_inf)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_inf(_ x: float4) -> Float ``` |
| To | ``` func norm_inf(_ x: float4) -> Float ``` |

Modified [norm_inf(_: double3) -> Double](https://developer.apple.com/documentation/simd/1425674-norm_inf)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_inf(_ x: double3) -> Double ``` |
| To | ``` func norm_inf(_ x: double3) -> Double ``` |

Modified [norm_inf(_: float2) -> Float](https://developer.apple.com/documentation/simd/1425284-norm_inf)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_inf(_ x: float2) -> Float ``` |
| To | ``` func norm_inf(_ x: float2) -> Float ``` |

Modified [norm_one(_: float3) -> Float](https://developer.apple.com/documentation/simd/1425989-norm_one)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_one(_ x: float3) -> Float ``` |
| To | ``` func norm_one(_ x: float3) -> Float ``` |

Modified [norm_one(_: double2) -> Double](https://developer.apple.com/documentation/simd/1424252-norm_one)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_one(_ x: double2) -> Double ``` |
| To | ``` func norm_one(_ x: double2) -> Double ``` |

Modified [norm_one(_: double4) -> Double](https://developer.apple.com/documentation/simd/1424069-norm_one)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_one(_ x: double4) -> Double ``` |
| To | ``` func norm_one(_ x: double4) -> Double ``` |

Modified [norm_one(_: float2) -> Float](https://developer.apple.com/documentation/simd/1426286-norm_one)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_one(_ x: float2) -> Float ``` |
| To | ``` func norm_one(_ x: float2) -> Float ``` |

Modified [norm_one(_: float4) -> Float](https://developer.apple.com/documentation/simd/1424711-norm_one)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_one(_ x: float4) -> Float ``` |
| To | ``` func norm_one(_ x: float4) -> Float ``` |

Modified [norm_one(_: double3) -> Double](https://developer.apple.com/documentation/simd/1424800-norm_one)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func norm_one(_ x: double3) -> Double ``` |
| To | ``` func norm_one(_ x: double3) -> Double ``` |

Modified [normalize(_: double2) -> double2](https://developer.apple.com/documentation/simd/1424023-normalize)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func normalize(_ x: double2) -> double2 ``` |
| To | ``` func normalize(_ x: double2) -> double2 ``` |

Modified [normalize(_: float4) -> float4](https://developer.apple.com/documentation/simd/1426343-normalize)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func normalize(_ x: float4) -> float4 ``` |
| To | ``` func normalize(_ x: float4) -> float4 ``` |

Modified [normalize(_: float2) -> float2](https://developer.apple.com/documentation/simd/1426190-normalize)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func normalize(_ x: float2) -> float2 ``` |
| To | ``` func normalize(_ x: float2) -> float2 ``` |

Modified [normalize(_: double3) -> double3](https://developer.apple.com/documentation/simd/1426124-normalize)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func normalize(_ x: double3) -> double3 ``` |
| To | ``` func normalize(_ x: double3) -> double3 ``` |

Modified [normalize(_: double4) -> double4](https://developer.apple.com/documentation/simd/1424278-normalize)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func normalize(_ x: double4) -> double4 ``` |
| To | ``` func normalize(_ x: double4) -> double4 ``` |

Modified [normalize(_: float3) -> float3](https://developer.apple.com/documentation/simd/1426148-normalize)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func normalize(_ x: float3) -> float3 ``` |
| To | ``` func normalize(_ x: float3) -> float3 ``` |

Modified [project(_: float4, _: float4) -> float4](https://developer.apple.com/documentation/simd/1425962-project)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func project(_ x: float4, _ y: float4) -> float4 ``` |
| To | ``` func project(_ x: float4, _ y: float4) -> float4 ``` |

Modified [project(_: float2, _: float2) -> float2](https://developer.apple.com/documentation/simd/1425987-project)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func project(_ x: float2, _ y: float2) -> float2 ``` |
| To | ``` func project(_ x: float2, _ y: float2) -> float2 ``` |

Modified [project(_: double2, _: double2) -> double2](https://developer.apple.com/documentation/simd/1424727-project)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func project(_ x: double2, _ y: double2) -> double2 ``` |
| To | ``` func project(_ x: double2, _ y: double2) -> double2 ``` |

Modified [project(_: double3, _: double3) -> double3](https://developer.apple.com/documentation/simd/1426131-project)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func project(_ x: double3, _ y: double3) -> double3 ``` |
| To | ``` func project(_ x: double3, _ y: double3) -> double3 ``` |

Modified [project(_: float3, _: float3) -> float3](https://developer.apple.com/documentation/simd/1425226-project)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func project(_ x: float3, _ y: float3) -> float3 ``` |
| To | ``` func project(_ x: float3, _ y: float3) -> float3 ``` |

Modified [project(_: double4, _: double4) -> double4](https://developer.apple.com/documentation/simd/1424248-project)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func project(_ x: double4, _ y: double4) -> double4 ``` |
| To | ``` func project(_ x: double4, _ y: double4) -> double4 ``` |

Modified [recip(_: float4) -> float4](https://developer.apple.com/documentation/simd/1426080-recip)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func recip(_ x: float4) -> float4 ``` |
| To | ``` func recip(_ x: float4) -> float4 ``` |

Modified [recip(_: Float) -> Float](https://developer.apple.com/documentation/simd/1424989-recip)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func recip(_ x: Float) -> Float ``` |
| To | ``` func recip(_ x: Float) -> Float ``` |

Modified [recip(_: double3) -> double3](https://developer.apple.com/documentation/simd/1424668-recip)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func recip(_ x: double3) -> double3 ``` |
| To | ``` func recip(_ x: double3) -> double3 ``` |

Modified [recip(_: float3) -> float3](https://developer.apple.com/documentation/simd/1424680-recip)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func recip(_ x: float3) -> float3 ``` |
| To | ``` func recip(_ x: float3) -> float3 ``` |

Modified [recip(_: double4) -> double4](https://developer.apple.com/documentation/simd/1425012-recip)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func recip(_ x: double4) -> double4 ``` |
| To | ``` func recip(_ x: double4) -> double4 ``` |

Modified [recip(_: double2) -> double2](https://developer.apple.com/documentation/simd/1424350-recip)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func recip(_ x: double2) -> double2 ``` |
| To | ``` func recip(_ x: double2) -> double2 ``` |

Modified [recip(_: float2) -> float2](https://developer.apple.com/documentation/simd/1426058-recip)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func recip(_ x: float2) -> float2 ``` |
| To | ``` func recip(_ x: float2) -> float2 ``` |

Modified [recip(_: Double) -> Double](https://developer.apple.com/documentation/simd/1425435-recip)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func recip(_ x: Double) -> Double ``` |
| To | ``` func recip(_ x: Double) -> Double ``` |

Modified [reduce_add(_: double3) -> Double](https://developer.apple.com/documentation/simd/1424316-reduce_add)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_add(_ x: double3) -> Double ``` |
| To | ``` func reduce_add(_ x: double3) -> Double ``` |

Modified [reduce_add(_: float3) -> Float](https://developer.apple.com/documentation/simd/1424629-reduce_add)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_add(_ x: float3) -> Float ``` |
| To | ``` func reduce_add(_ x: float3) -> Float ``` |

Modified [reduce_add(_: double2) -> Double](https://developer.apple.com/documentation/simd/1424482-reduce_add)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_add(_ x: double2) -> Double ``` |
| To | ``` func reduce_add(_ x: double2) -> Double ``` |

Modified [reduce_add(_: double4) -> Double](https://developer.apple.com/documentation/simd/1424390-reduce_add)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_add(_ x: double4) -> Double ``` |
| To | ``` func reduce_add(_ x: double4) -> Double ``` |

Modified [reduce_add(_: int3) -> Int32](https://developer.apple.com/documentation/simd/1425354-reduce_add)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_add(_ x: int3) -> Int32 ``` |
| To | ``` func reduce_add(_ x: int3) -> Int32 ``` |

Modified [reduce_add(_: float4) -> Float](https://developer.apple.com/documentation/simd/1424507-reduce_add)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_add(_ x: float4) -> Float ``` |
| To | ``` func reduce_add(_ x: float4) -> Float ``` |

Modified [reduce_add(_: int4) -> Int32](https://developer.apple.com/documentation/simd/1425437-reduce_add)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_add(_ x: int4) -> Int32 ``` |
| To | ``` func reduce_add(_ x: int4) -> Int32 ``` |

Modified [reduce_add(_: float2) -> Float](https://developer.apple.com/documentation/simd/1424776-reduce_add)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_add(_ x: float2) -> Float ``` |
| To | ``` func reduce_add(_ x: float2) -> Float ``` |

Modified [reduce_add(_: int2) -> Int32](https://developer.apple.com/documentation/simd/1425249-reduce_add)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_add(_ x: int2) -> Int32 ``` |
| To | ``` func reduce_add(_ x: int2) -> Int32 ``` |

Modified [reduce_max(_: int3) -> Int32](https://developer.apple.com/documentation/simd/1426095-reduce_max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_max(_ x: int3) -> Int32 ``` |
| To | ``` func reduce_max(_ x: int3) -> Int32 ``` |

Modified [reduce_max(_: double4) -> Double](https://developer.apple.com/documentation/simd/1425657-reduce_max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_max(_ x: double4) -> Double ``` |
| To | ``` func reduce_max(_ x: double4) -> Double ``` |

Modified [reduce_max(_: float4) -> Float](https://developer.apple.com/documentation/simd/1424478-reduce_max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_max(_ x: float4) -> Float ``` |
| To | ``` func reduce_max(_ x: float4) -> Float ``` |

Modified [reduce_max(_: double2) -> Double](https://developer.apple.com/documentation/simd/1425203-reduce_max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_max(_ x: double2) -> Double ``` |
| To | ``` func reduce_max(_ x: double2) -> Double ``` |

Modified [reduce_max(_: int4) -> Int32](https://developer.apple.com/documentation/simd/1425910-reduce_max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_max(_ x: int4) -> Int32 ``` |
| To | ``` func reduce_max(_ x: int4) -> Int32 ``` |

Modified [reduce_max(_: int2) -> Int32](https://developer.apple.com/documentation/simd/1424828-reduce_max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_max(_ x: int2) -> Int32 ``` |
| To | ``` func reduce_max(_ x: int2) -> Int32 ``` |

Modified [reduce_max(_: float2) -> Float](https://developer.apple.com/documentation/simd/1425484-reduce_max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_max(_ x: float2) -> Float ``` |
| To | ``` func reduce_max(_ x: float2) -> Float ``` |

Modified [reduce_max(_: float3) -> Float](https://developer.apple.com/documentation/simd/1426122-reduce_max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_max(_ x: float3) -> Float ``` |
| To | ``` func reduce_max(_ x: float3) -> Float ``` |

Modified [reduce_max(_: double3) -> Double](https://developer.apple.com/documentation/simd/1426174-reduce_max)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_max(_ x: double3) -> Double ``` |
| To | ``` func reduce_max(_ x: double3) -> Double ``` |

Modified [reduce_min(_: float4) -> Float](https://developer.apple.com/documentation/simd/1424464-reduce_min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_min(_ x: float4) -> Float ``` |
| To | ``` func reduce_min(_ x: float4) -> Float ``` |

Modified [reduce_min(_: float3) -> Float](https://developer.apple.com/documentation/simd/1426198-reduce_min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_min(_ x: float3) -> Float ``` |
| To | ``` func reduce_min(_ x: float3) -> Float ``` |

Modified [reduce_min(_: int2) -> Int32](https://developer.apple.com/documentation/simd/1425454-reduce_min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_min(_ x: int2) -> Int32 ``` |
| To | ``` func reduce_min(_ x: int2) -> Int32 ``` |

Modified [reduce_min(_: float2) -> Float](https://developer.apple.com/documentation/simd/1424647-reduce_min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_min(_ x: float2) -> Float ``` |
| To | ``` func reduce_min(_ x: float2) -> Float ``` |

Modified [reduce_min(_: double4) -> Double](https://developer.apple.com/documentation/simd/1424501-reduce_min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_min(_ x: double4) -> Double ``` |
| To | ``` func reduce_min(_ x: double4) -> Double ``` |

Modified [reduce_min(_: int4) -> Int32](https://developer.apple.com/documentation/simd/1424517-reduce_min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_min(_ x: int4) -> Int32 ``` |
| To | ``` func reduce_min(_ x: int4) -> Int32 ``` |

Modified [reduce_min(_: double2) -> Double](https://developer.apple.com/documentation/simd/1424804-reduce_min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_min(_ x: double2) -> Double ``` |
| To | ``` func reduce_min(_ x: double2) -> Double ``` |

Modified [reduce_min(_: int3) -> Int32](https://developer.apple.com/documentation/simd/1424749-reduce_min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_min(_ x: int3) -> Int32 ``` |
| To | ``` func reduce_min(_ x: int3) -> Int32 ``` |

Modified [reduce_min(_: double3) -> Double](https://developer.apple.com/documentation/simd/1424755-reduce_min)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reduce_min(_ x: double3) -> Double ``` |
| To | ``` func reduce_min(_ x: double3) -> Double ``` |

Modified [reflect(_: double3, n: double3) -> double3](https://developer.apple.com/documentation/simd/1426275-reflect)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reflect(_ x: double3, n n: double3) -> double3 ``` |
| To | ``` func reflect(_ x: double3, n n: double3) -> double3 ``` |

Modified [reflect(_: float3, n: float3) -> float3](https://developer.apple.com/documentation/simd/1426133-reflect)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reflect(_ x: float3, n n: float3) -> float3 ``` |
| To | ``` func reflect(_ x: float3, n n: float3) -> float3 ``` |

Modified [reflect(_: double2, n: double2) -> double2](https://developer.apple.com/documentation/simd/1425078-reflect)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reflect(_ x: double2, n n: double2) -> double2 ``` |
| To | ``` func reflect(_ x: double2, n n: double2) -> double2 ``` |

Modified [reflect(_: double4, n: double4) -> double4](https://developer.apple.com/documentation/simd/1425340-reflect)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reflect(_ x: double4, n n: double4) -> double4 ``` |
| To | ``` func reflect(_ x: double4, n n: double4) -> double4 ``` |

Modified [reflect(_: float4, n: float4) -> float4](https://developer.apple.com/documentation/simd/1425645-reflect)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reflect(_ x: float4, n n: float4) -> float4 ``` |
| To | ``` func reflect(_ x: float4, n n: float4) -> float4 ``` |

Modified [reflect(_: float2, n: float2) -> float2](https://developer.apple.com/documentation/simd/1424770-reflect)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func reflect(_ x: float2, n n: float2) -> float2 ``` |
| To | ``` func reflect(_ x: float2, n n: float2) -> float2 ``` |

Modified [refract(_: float3, n: float3, eta: Float) -> float3](https://developer.apple.com/documentation/simd/1425933-refract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func refract(_ x: float3, n n: float3, eta eta: Float) -> float3 ``` |
| To | ``` func refract(_ x: float3, n n: float3, eta eta: Float) -> float3 ``` |

Modified [refract(_: float2, n: float2, eta: Float) -> float2](https://developer.apple.com/documentation/simd/1424794-refract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func refract(_ x: float2, n n: float2, eta eta: Float) -> float2 ``` |
| To | ``` func refract(_ x: float2, n n: float2, eta eta: Float) -> float2 ``` |

Modified [refract(_: double3, n: double3, eta: Double) -> double3](https://developer.apple.com/documentation/simd/1426015-refract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func refract(_ x: double3, n n: double3, eta eta: Double) -> double3 ``` |
| To | ``` func refract(_ x: double3, n n: double3, eta eta: Double) -> double3 ``` |

Modified [refract(_: double4, n: double4, eta: Double) -> double4](https://developer.apple.com/documentation/simd/1424470-refract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func refract(_ x: double4, n n: double4, eta eta: Double) -> double4 ``` |
| To | ``` func refract(_ x: double4, n n: double4, eta eta: Double) -> double4 ``` |

Modified [refract(_: float4, n: float4, eta: Float) -> float4](https://developer.apple.com/documentation/simd/1425197-refract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func refract(_ x: float4, n n: float4, eta eta: Float) -> float4 ``` |
| To | ``` func refract(_ x: float4, n n: float4, eta eta: Float) -> float4 ``` |

Modified [refract(_: double2, n: double2, eta: Double) -> double2](https://developer.apple.com/documentation/simd/1425571-refract)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func refract(_ x: double2, n n: double2, eta eta: Double) -> double2 ``` |
| To | ``` func refract(_ x: double2, n n: double2, eta eta: Double) -> double2 ``` |

Modified [rsqrt(_: double4) -> double4](https://developer.apple.com/documentation/simd/1424737-rsqrt)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rsqrt(_ x: double4) -> double4 ``` |
| To | ``` func rsqrt(_ x: double4) -> double4 ``` |

Modified [rsqrt(_: Float) -> Float](https://developer.apple.com/documentation/simd/1424786-rsqrt)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rsqrt(_ x: Float) -> Float ``` |
| To | ``` func rsqrt(_ x: Float) -> Float ``` |

Modified [rsqrt(_: float2) -> float2](https://developer.apple.com/documentation/simd/1426127-rsqrt)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rsqrt(_ x: float2) -> float2 ``` |
| To | ``` func rsqrt(_ x: float2) -> float2 ``` |

Modified [rsqrt(_: float4) -> float4](https://developer.apple.com/documentation/simd/1424229-rsqrt)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rsqrt(_ x: float4) -> float4 ``` |
| To | ``` func rsqrt(_ x: float4) -> float4 ``` |

Modified [rsqrt(_: Double) -> Double](https://developer.apple.com/documentation/simd/1425655-rsqrt)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rsqrt(_ x: Double) -> Double ``` |
| To | ``` func rsqrt(_ x: Double) -> Double ``` |

Modified [rsqrt(_: float3) -> float3](https://developer.apple.com/documentation/simd/1425941-rsqrt)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rsqrt(_ x: float3) -> float3 ``` |
| To | ``` func rsqrt(_ x: float3) -> float3 ``` |

Modified [rsqrt(_: double2) -> double2](https://developer.apple.com/documentation/simd/1426033-rsqrt)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rsqrt(_ x: double2) -> double2 ``` |
| To | ``` func rsqrt(_ x: double2) -> double2 ``` |

Modified [rsqrt(_: double3) -> double3](https://developer.apple.com/documentation/simd/1424672-rsqrt)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rsqrt(_ x: double3) -> double3 ``` |
| To | ``` func rsqrt(_ x: double3) -> double3 ``` |

Modified [sign(_: float4) -> float4](https://developer.apple.com/documentation/simd/1424874-sign)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sign(_ x: float4) -> float4 ``` |
| To | ``` func sign(_ x: float4) -> float4 ``` |

Modified [sign(_: double2) -> double2](https://developer.apple.com/documentation/simd/1424107-sign)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sign(_ x: double2) -> double2 ``` |
| To | ``` func sign(_ x: double2) -> double2 ``` |

Modified [sign(_: float2) -> float2](https://developer.apple.com/documentation/simd/1426186-sign)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sign(_ x: float2) -> float2 ``` |
| To | ``` func sign(_ x: float2) -> float2 ``` |

Modified [sign(_: double3) -> double3](https://developer.apple.com/documentation/simd/1424093-sign)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sign(_ x: double3) -> double3 ``` |
| To | ``` func sign(_ x: double3) -> double3 ``` |

Modified [sign(_: float3) -> float3](https://developer.apple.com/documentation/simd/1424284-sign)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sign(_ x: float3) -> float3 ``` |
| To | ``` func sign(_ x: float3) -> float3 ``` |

Modified [sign(_: double4) -> double4](https://developer.apple.com/documentation/simd/1424046-sign)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sign(_ x: double4) -> double4 ``` |
| To | ``` func sign(_ x: double4) -> double4 ``` |

Modified [sign(_: Float) -> Float](https://developer.apple.com/documentation/simd/1425615-sign)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sign(_ x: Float) -> Float ``` |
| To | ``` func sign(_ x: Float) -> Float ``` |

Modified [sign(_: Double) -> Double](https://developer.apple.com/documentation/simd/1424664-sign)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sign(_ x: Double) -> Double ``` |
| To | ``` func sign(_ x: Double) -> Double ``` |

Modified [smoothstep(_: float4, edge0: float4, edge1: float4) -> float4](https://developer.apple.com/documentation/simd/1424625-smoothstep)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func smoothstep(_ x: float4, edge0 edge0: float4, edge1 edge1: float4) -> float4 ``` |
| To | ``` func smoothstep(_ x: float4, edge0 edge0: float4, edge1 edge1: float4) -> float4 ``` |

Modified [smoothstep(_: double4, edge0: double4, edge1: double4) -> double4](https://developer.apple.com/documentation/simd/1425136-smoothstep)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func smoothstep(_ x: double4, edge0 edge0: double4, edge1 edge1: double4) -> double4 ``` |
| To | ``` func smoothstep(_ x: double4, edge0 edge0: double4, edge1 edge1: double4) -> double4 ``` |

Modified [smoothstep(_: double3, edge0: double3, edge1: double3) -> double3](https://developer.apple.com/documentation/simd/1425949-smoothstep)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func smoothstep(_ x: double3, edge0 edge0: double3, edge1 edge1: double3) -> double3 ``` |
| To | ``` func smoothstep(_ x: double3, edge0 edge0: double3, edge1 edge1: double3) -> double3 ``` |

Modified [smoothstep(_: double2, edge0: double2, edge1: double2) -> double2](https://developer.apple.com/documentation/simd/1424759-smoothstep)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func smoothstep(_ x: double2, edge0 edge0: double2, edge1 edge1: double2) -> double2 ``` |
| To | ``` func smoothstep(_ x: double2, edge0 edge0: double2, edge1 edge1: double2) -> double2 ``` |

Modified [smoothstep(_: float2, edge0: float2, edge1: float2) -> float2](https://developer.apple.com/documentation/simd/1425491-smoothstep)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func smoothstep(_ x: float2, edge0 edge0: float2, edge1 edge1: float2) -> float2 ``` |
| To | ``` func smoothstep(_ x: float2, edge0 edge0: float2, edge1 edge1: float2) -> float2 ``` |

Modified [smoothstep(_: float3, edge0: float3, edge1: float3) -> float3](https://developer.apple.com/documentation/simd/1425015-smoothstep)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func smoothstep(_ x: float3, edge0 edge0: float3, edge1 edge1: float3) -> float3 ``` |
| To | ``` func smoothstep(_ x: float3, edge0 edge0: float3, edge1 edge1: float3) -> float3 ``` |

Modified [step(_: float3, edge: float3) -> float3](https://developer.apple.com/documentation/simd/1424378-step)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func step(_ x: float3, edge edge: float3) -> float3 ``` |
| To | ``` func step(_ x: float3, edge edge: float3) -> float3 ``` |

Modified [step(_: float4, edge: float4) -> float4](https://developer.apple.com/documentation/simd/1424361-step)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func step(_ x: float4, edge edge: float4) -> float4 ``` |
| To | ``` func step(_ x: float4, edge edge: float4) -> float4 ``` |

Modified [step(_: double3, edge: double3) -> double3](https://developer.apple.com/documentation/simd/1425450-step)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func step(_ x: double3, edge edge: double3) -> double3 ``` |
| To | ``` func step(_ x: double3, edge edge: double3) -> double3 ``` |

Modified [step(_: Double, edge: Double) -> Double](https://developer.apple.com/documentation/simd/1424159-step)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func step(_ x: Double, edge edge: Double) -> Double ``` |
| To | ``` func step(_ x: Double, edge edge: Double) -> Double ``` |

Modified [step(_: float2, edge: float2) -> float2](https://developer.apple.com/documentation/simd/1425643-step)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func step(_ x: float2, edge edge: float2) -> float2 ``` |
| To | ``` func step(_ x: float2, edge edge: float2) -> float2 ``` |

Modified [step(_: double4, edge: double4) -> double4](https://developer.apple.com/documentation/simd/1425720-step)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func step(_ x: double4, edge edge: double4) -> double4 ``` |
| To | ``` func step(_ x: double4, edge edge: double4) -> double4 ``` |

Modified [step(_: double2, edge: double2) -> double2](https://developer.apple.com/documentation/simd/1425402-step)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func step(_ x: double2, edge edge: double2) -> double2 ``` |
| To | ``` func step(_ x: double2, edge edge: double2) -> double2 ``` |

Modified [step(_: Float, edge: Float) -> Float](https://developer.apple.com/documentation/simd/1425754-step)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func step(_ x: Float, edge edge: Float) -> Float ``` |
| To | ``` func step(_ x: Float, edge edge: Float) -> Float ``` |

Modified [trunc(_: float2) -> float2](https://developer.apple.com/documentation/simd/1425931-trunc)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func trunc(_ x: float2) -> float2 ``` |
| To | ``` func trunc(_ x: float2) -> float2 ``` |

Modified [trunc(_: float3) -> float3](https://developer.apple.com/documentation/simd/1425191-trunc)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func trunc(_ x: float3) -> float3 ``` |
| To | ``` func trunc(_ x: float3) -> float3 ``` |

Modified [trunc(_: double2) -> double2](https://developer.apple.com/documentation/simd/1425730-trunc)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func trunc(_ x: double2) -> double2 ``` |
| To | ``` func trunc(_ x: double2) -> double2 ``` |

Modified [trunc(_: double4) -> double4](https://developer.apple.com/documentation/simd/1424095-trunc)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func trunc(_ x: double4) -> double4 ``` |
| To | ``` func trunc(_ x: double4) -> double4 ``` |

Modified [trunc(_: double3) -> double3](https://developer.apple.com/documentation/simd/1425160-trunc)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func trunc(_ x: double3) -> double3 ``` |
| To | ``` func trunc(_ x: double3) -> double3 ``` |

Modified [trunc(_: float4) -> float4](https://developer.apple.com/documentation/simd/1425742-trunc)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func trunc(_ x: float4) -> float4 ``` |
| To | ``` func trunc(_ x: float4) -> float4 ``` |

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
