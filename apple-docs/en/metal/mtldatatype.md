---
title: MTLDataType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldatatype
source_url: 'https://developer.apple.com/documentation/metal/mtldatatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldatatype.json'
content_hash: 'sha256:ecc1d74454dfae28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDataType

<sub>Enumeration</sub>

The parameter type options for GPU functions, such as shaders and compute kernels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLDataType
```

## Overview

Metal reports or accepts this type in several reflection and configuration contexts, such as:

- The [type](mtlfunctionconstant/type.md) property of [MTLFunctionConstant](mtlfunctionconstant.md)
- The [attributeType](mtlattribute/attributetype.md) property of [MTLAttribute](mtlattribute.md)
- The [attributeType](mtlvertexattribute/attributetype.md) property of [MTLVertexAttribute](mtlvertexattribute.md)
- The [- setConstantValue:type:withName:](<mtlfunctionconstantvalues/setconstantvalue(__type_withname_).md>) method of [MTLFunctionConstantValues](mtlfunctionconstantvalues.md)

### Normalized integer types

Color types with `Snorm` in the name are normalized signed integer types. For these types, values in the range `[-1.0, 1.0]` map to `[MIN_INT, MAX_INT]`, where `MIN_INT` is the most negative integer and `MAX_INT` is the most positive integer for the number of bits in the storage size. Positive values and zero distribute uniformly in the range `[0.0, 1.0]`, and negative integer values greater than `(MIN_INT + 1)` distribute uniformly in the range `(-1.0, 0.0)`.

> [!important] Important
> For normalized signed integer types, the values `MIN_INT` and `(MIN_INT + 1)` both map to `-1.0`.

Color types with `Unorm` in the name are normalized unsigned integer types. For these types, values in the range `[0.0, 1.0]` map to `[0, MAX_UINT]`, where `MAX_UINT` is the largest unsigned integer for the number of bits in the storage size.

Metal stores data in little-endian byte order, with the least-significant byte at the lowest memory address. Formats with multibyte components also store each component in little-endian byte order.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### 64-bit integer types

- [MTLDataTypeLong](mtldatatype/long.md) — A 64-bit, signed integer value.
- [MTLDataTypeLong2](mtldatatype/long2.md) — A two-component vector with 64-bit, signed integer values.
- [MTLDataTypeLong3](mtldatatype/long3.md) — A three-component vector with 64-bit, signed integer values.
- [MTLDataTypeLong4](mtldatatype/long4.md) — A four-component vector with 64-bit, signed integer values.
- [MTLDataTypeULong](mtldatatype/ulong.md) — A 64-bit, unsigned integer value.
- [MTLDataTypeULong2](mtldatatype/ulong2.md) — A two-component vector with 64-bit, unsigned integer values.
- [MTLDataTypeULong3](mtldatatype/ulong3.md) — A three-component vector with 64-bit, unsigned integer values.
- [MTLDataTypeULong4](mtldatatype/ulong4.md) — A four-component vector with 64-bit, unsigned integer values.

### 64-bit color integer types

- [MTLDataTypeRGBA16Snorm](mtldatatype/rgba16snorm.md) — An ordinary pixel with four components, each of which is a 16-bit, normalized, signed integer value.
- [MTLDataTypeRGBA16Unorm](mtldatatype/rgba16unorm.md) — An ordinary pixel with four components, each of which is a 16-bit, normalized, unsigned integer value.

### 32-bit floating-point types

- [MTLDataTypeFloat](mtldatatype/float.md) — A 32-bit floating-point value.
- [MTLDataTypeFloat2](mtldatatype/float2.md) — A two-component vector with 32-bit floating-point values.
- [MTLDataTypeFloat3](mtldatatype/float3.md) — A three-component vector with 32-bit floating-point values.
- [MTLDataTypeFloat4](mtldatatype/float4.md) — A four-component vector with 32-bit floating-point values.

### 32-bit floating-point matrix types

- [MTLDataTypeFloat2x2](mtldatatype/float2x2.md) — A 2x2 component matrix with 32-bit floating-point values.
- [MTLDataTypeFloat2x3](mtldatatype/float2x3.md) — A 2x3 component matrix with 32-bit floating-point values.
- [MTLDataTypeFloat2x4](mtldatatype/float2x4.md) — A 2x4 component matrix with 32-bit floating-point values.
- [MTLDataTypeFloat3x2](mtldatatype/float3x2.md) — A 3x2 component matrix with 32-bit floating-point values.
- [MTLDataTypeFloat3x3](mtldatatype/float3x3.md) — A 3x3 component matrix with 32-bit floating-point values.
- [MTLDataTypeFloat3x4](mtldatatype/float3x4.md) — A 3x4 component matrix with 32-bit floating-point values.
- [MTLDataTypeFloat4x2](mtldatatype/float4x2.md) — A 4x2 component matrix with 32-bit floating-point values.
- [MTLDataTypeFloat4x3](mtldatatype/float4x3.md) — A 4x3 component matrix with 32-bit floating-point values.
- [MTLDataTypeFloat4x4](mtldatatype/float4x4.md) — A 4x4 component matrix with 32-bit floating-point values.

### 32-bit color floating-point types

- [MTLDataTypeRGB9E5Float](mtldatatype/rgb9e5float.md) — A packed 32-bit format with three color components, each of which is a 9-bit floating-point value.
- [MTLDataTypeRG11B10Float](mtldatatype/rg11b10float.md) — A packed 32-bit format with three floating-point color components, two of which are 11-bit values, and one is a 10-bit value.

### 32-bit color integer types

- [MTLDataTypeRGBA8Snorm](mtldatatype/rgba8snorm.md) — An ordinary pixel with four components, each of which is an 8-bit, normalized, signed integer value.
- [MTLDataTypeRGBA8Unorm](mtldatatype/rgba8unorm.md) — An ordinary pixel with four components, each of which is an 8-bit, normalized, unsigned integer value.
- [MTLDataTypeRGBA8Unorm_sRGB](mtldatatype/rgba8unorm_srgb.md) — An ordinary pixel with four components, each of which is an 8-bit, normalized, unsigned integer value in the sRGB color space.
- [MTLDataTypeRG16Snorm](mtldatatype/rg16snorm.md) — An ordinary pixel with two components, each of which is a 16-bit, normalized, signed integer value.
- [MTLDataTypeRG16Unorm](mtldatatype/rg16unorm.md) — An ordinary pixel with two components, each of which is a 16-bit, normalized, unsigned integer value.
- [MTLDataTypeRGB10A2Unorm](mtldatatype/rgb10a2unorm.md) — A packed 32-bit format with three color components, each of which is a 10-bit, normalized, unsigned integer value.

### 32-bit integer types

- [MTLDataTypeInt](mtldatatype/int.md) — A 32-bit, signed integer value.
- [MTLDataTypeInt2](mtldatatype/int2.md) — A two-component vector with 32-bit, signed integer values.
- [MTLDataTypeInt3](mtldatatype/int3.md) — A three-component vector with 32-bit, signed integer values.
- [MTLDataTypeInt4](mtldatatype/int4.md) — A four-component vector with 32-bit, signed integer values.
- [MTLDataTypeUInt](mtldatatype/uint.md) — A 32-bit, unsigned integer value.
- [MTLDataTypeUInt2](mtldatatype/uint2.md) — A two-component vector with 32-bit, unsigned integer values.
- [MTLDataTypeUInt3](mtldatatype/uint3.md) — A three-component vector with 32-bit, unsigned integer values.
- [MTLDataTypeUInt4](mtldatatype/uint4.md) — A four-component vector with 32-bit, unsigned integer values.

### 16-bit floating-point types

- [MTLDataTypeHalf](mtldatatype/half.md) — A 16-bit floating-point value.
- [MTLDataTypeHalf2](mtldatatype/half2.md) — A two-component vector with 16-bit floating-point values.
- [MTLDataTypeHalf3](mtldatatype/half3.md) — A three-component vector with 16-bit floating-point values.
- [MTLDataTypeHalf4](mtldatatype/half4.md) — A four-component vector with 16-bit floating-point values.

### 16-bit floating-point matrix types

- [MTLDataTypeHalf2x2](mtldatatype/half2x2.md) — A 2x2 component matrix with 16-bit floating-point values.
- [MTLDataTypeHalf2x3](mtldatatype/half2x3.md) — A 2x3 component matrix with 16-bit floating-point values.
- [MTLDataTypeHalf2x4](mtldatatype/half2x4.md) — A 2x4 component matrix with 16-bit floating-point values.
- [MTLDataTypeHalf3x2](mtldatatype/half3x2.md) — A 3x2 component matrix with 16-bit floating-point values.
- [MTLDataTypeHalf3x3](mtldatatype/half3x3.md) — A 3x3 component matrix with 16-bit floating-point values.
- [MTLDataTypeHalf3x4](mtldatatype/half3x4.md) — A 3x4 component matrix with 16-bit floating-point values.
- [MTLDataTypeHalf4x2](mtldatatype/half4x2.md) — A 4x2 component matrix with 16-bit floating-point values.
- [MTLDataTypeHalf4x3](mtldatatype/half4x3.md) — A 4x3 component matrix with 16-bit floating-point values.
- [MTLDataTypeHalf4x4](mtldatatype/half4x4.md) — A 4x4 component matrix with 16-bit floating-point values.

### 16-bit brain floating-point types

- [MTLDataTypeBFloat](mtldatatype/bfloat.md) — A 16-bit, brain floating-point value.
- [MTLDataTypeBFloat2](mtldatatype/bfloat2.md) — A two-component vector with 16-bit, brain floating-point values.
- [MTLDataTypeBFloat3](mtldatatype/bfloat3.md) — A three-component vector with 16-bit, brain floating-point values.
- [MTLDataTypeBFloat4](mtldatatype/bfloat4.md) — A four-component vector with 16-bit, brain floating-point values.

### 16-bit integer types

- [MTLDataTypeShort](mtldatatype/short.md) — A 16-bit, signed integer value.
- [MTLDataTypeShort2](mtldatatype/short2.md) — A two-component vector with 16-bit, signed integer values.
- [MTLDataTypeShort3](mtldatatype/short3.md) — A three-component vector with 16-bit, signed integer values.
- [MTLDataTypeShort4](mtldatatype/short4.md) — A four-component vector with 16-bit, signed integer values.
- [MTLDataTypeUShort](mtldatatype/ushort.md) — A 16-bit, unsigned integer value.
- [MTLDataTypeUShort2](mtldatatype/ushort2.md) — A two-component vector with 16-bit, unsigned integer values.
- [MTLDataTypeUShort3](mtldatatype/ushort3.md) — A three-component vector with 16-bit, unsigned integer values.
- [MTLDataTypeUShort4](mtldatatype/ushort4.md) — A four-component vector with 16-bit, unsigned integer values.

### 16-bit color integer types

- [MTLDataTypeRG8Snorm](mtldatatype/rg8snorm.md) — An ordinary pixel with two components, each of which is an 8-bit, normalized, signed integer value.
- [MTLDataTypeRG8Unorm](mtldatatype/rg8unorm.md) — An ordinary pixel with two components, each of which is an 8-bit, normalized, unsigned integer value.
- [MTLDataTypeR16Snorm](mtldatatype/r16snorm.md) — An ordinary pixel with one component that’s a 16-bit, normalized, signed integer value.
- [MTLDataTypeR16Unorm](mtldatatype/r16unorm.md) — An ordinary pixel with one component that’s a 16-bit, normalized, unsigned integer value.

### 8-bit integer types

- [MTLDataTypeChar](mtldatatype/char.md) — An 8-bit, signed integer value.
- [MTLDataTypeChar2](mtldatatype/char2.md) — A two-component vector with 8-bit, signed integer values.
- [MTLDataTypeChar3](mtldatatype/char3.md) — A three-component vector with 8-bit, signed integer values.
- [MTLDataTypeChar4](mtldatatype/char4.md) — A four-component vector with 8-bit, signed integer values.
- [MTLDataTypeUChar](mtldatatype/uchar.md) — An 8-bit, unsigned integer value.
- [MTLDataTypeUChar2](mtldatatype/uchar2.md) — A two-component vector with 8-bit, unsigned integer values.
- [MTLDataTypeUChar3](mtldatatype/uchar3.md) — A three-component vector with 8-bit, unsigned integer values.
- [MTLDataTypeUChar4](mtldatatype/uchar4.md) — A four-component vector with 8-bit, unsigned integer values.

### 8-bit color integer types

- [MTLDataTypeR8Snorm](mtldatatype/r8snorm.md) — An ordinary pixel with one component that’s an 8-bit, normalized, signed integer value.
- [MTLDataTypeR8Unorm](mtldatatype/r8unorm.md) — An ordinary pixel with one component that’s an 8-bit, normalized, unsigned integer value.

### Boolean types

- [MTLDataTypeBool](mtldatatype/bool.md) — A Boolean value.
- [MTLDataTypeBool2](mtldatatype/bool2.md) — A two-component Boolean vector.
- [MTLDataTypeBool3](mtldatatype/bool3.md) — A three-component Boolean vector.
- [MTLDataTypeBool4](mtldatatype/bool4.md) — A four-component Boolean vector.

### Resource types

- [MTLDataTypeTensor](mtldatatype/tensor.md) — Represents a data type corresponding to a machine learning tensor.
- [MTLDataTypeSampler](mtldatatype/sampler.md) — A Metal texture sampler instance.
- [MTLDataTypeTexture](mtldatatype/texture.md) — A Metal texture resource instance.
- [MTLDataTypeRenderPipeline](mtldatatype/renderpipeline.md) — A Metal render pipeline instance.
- [MTLDataTypeComputePipeline](mtldatatype/computepipeline.md) — A Metal compute pipeline instance.
- [MTLDataTypeDepthStencilState](mtldatatype/depthstencilstate.md) — Represents a data type corresponding to a depth-stencil state object.
- [MTLDataTypeIndirectCommandBuffer](mtldatatype/indirectcommandbuffer.md) — An indirect command buffer resource instance.
- [MTLDataTypeVisibleFunctionTable](mtldatatype/visiblefunctiontable.md) — A table of visible functions that a render or compute pipeline can call.
- [MTLDataTypeIntersectionFunctionTable](mtldatatype/intersectionfunctiontable.md) — A table of intersection functions that a render or compute pipeline can call.
- [MTLDataTypePrimitiveAccelerationStructure](mtldatatype/primitiveaccelerationstructure.md) — A low-level ray-tracing acceleration structure for a set of primitives.
- [MTLDataTypeInstanceAccelerationStructure](mtldatatype/instanceaccelerationstructure.md) — A high-level, ray-tracing acceleration structure for a set of low-level primitive instances.

### Collection types

- [MTLDataTypeStruct](mtldatatype/struct.md) — A structure instance.
- [MTLDataTypeArray](mtldatatype/array.md) — An array instance.
- [MTLDataTypePointer](mtldatatype/pointer.md) — A pointer.

### Sentinel values

- [MTLDataTypeNone](mtldatatype/none.md) — A sentinel value that represents a GPU function parameter that doesn’t have a valid data type.

### Swift support

- [init(rawValue:)](<mtldatatype/init(rawvalue_).md>) — Creates a data type instance from a raw integer value.

## See Also

### Shader types

- [MTLType](mtltype.md) — A description of a data type.
- [MTLArrayType](mtlarraytype.md) — A description of an array.
- [MTLStructType](mtlstructtype.md) — A description of a structure.
- [MTLStructMember](mtlstructmember.md) — An instance that provides information about a field in a structure.
- [MTLPointerType](mtlpointertype.md) — A description of a pointer.
- [MTLTextureReferenceType](mtltexturereferencetype.md) — A description of a texture.
